// =============================================================================
//  CRYPT CRAWLER  -  a self-contained terminal roguelike in C++17
// -----------------------------------------------------------------------------
//  Descend 10 floors of a procedurally generated crypt, fight what lives down
//  there, grab loot, level up, and escape with the Sunstone Amulet.
//
//  Build:
//      Linux / macOS :  g++ -std=c++17 -O2 -o crypt_crawler crypt_crawler.cpp
//      Windows (MinGW):  g++ -std=c++17 -O2 -o crypt_crawler.exe crypt_crawler.cpp
//
//  Run:
//      ./crypt_crawler          (Linux / macOS)
//      crypt_crawler.exe        (Windows)
//
//  Controls:
//      W / A / S / D   or   H / J / K / L   or   arrow-ish vi keys  -> move
//      .  or  space   -> wait a turn
//      q              -> quit
//  Move INTO a monster to attack it. Walk onto loot to pick it up.
//  Step on the '>' stairs to descend.
// =============================================================================

#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <algorithm>
#include <chrono>
#include <cstdint>

// ----------------------------------------------------------------------------
//  Platform layer: raw single-key input + ANSI color enablement
// ----------------------------------------------------------------------------
#ifdef _WIN32
  #include <conio.h>
  #include <windows.h>
  static void setupTerminal() {
      // Enable ANSI escape sequence processing on modern Windows terminals.
      HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
      DWORD mode = 0;
      if (GetConsoleMode(h, &mode))
          SetConsoleMode(h, mode | ENABLE_VIRTUAL_TERMINAL_PROCESSING);
  }
  static void restoreTerminal() {}
  static int readKey() { return _getch(); }
#else
  #include <termios.h>
  #include <unistd.h>
  static termios g_oldTerm;
  static bool    g_termSaved = false;
  static void setupTerminal() {
      if (tcgetattr(STDIN_FILENO, &g_oldTerm) == 0) {
          g_termSaved = true;
          termios t = g_oldTerm;
          t.c_lflag &= ~(ICANON | ECHO);   // raw-ish: no line buffering, no echo
          t.c_cc[VMIN]  = 1;
          t.c_cc[VTIME] = 0;
          tcsetattr(STDIN_FILENO, TCSANOW, &t);
      }
  }
  static void restoreTerminal() {
      if (g_termSaved) tcsetattr(STDIN_FILENO, TCSANOW, &g_oldTerm);
  }
  static int readKey() {
      unsigned char c = 0;
      if (read(STDIN_FILENO, &c, 1) <= 0) return -1; // EOF -> signal quit
      return static_cast<int>(c);
  }
#endif

// ----------------------------------------------------------------------------
//  ANSI helpers
// ----------------------------------------------------------------------------
namespace col {
    const char* RESET = "\033[0m";
    const char* DIM    = "\033[90m";   // dark gray
    const char* WALL   = "\033[38;5;240m";
    const char* FLOOR  = "\033[38;5;236m";
    const char* PLAYER = "\033[1;93m";  // bright yellow
    const char* MON    = "\033[1;91m";  // bright red
    const char* POTION = "\033[1;95m";  // magenta
    const char* GOLD   = "\033[1;33m";  // gold
    const char* STAIRS = "\033[1;96m";  // cyan
    const char* AMULET = "\033[1;92m";  // bright green
    const char* HUD    = "\033[1;97m";
    const char* WARN   = "\033[1;91m";
    const char* GOODMSG= "\033[1;92m";
}

// ----------------------------------------------------------------------------
//  RNG
// ----------------------------------------------------------------------------
static std::mt19937 g_rng(
    static_cast<unsigned>(
        std::chrono::high_resolution_clock::now().time_since_epoch().count()));
static int randi(int lo, int hi) {  // inclusive
    std::uniform_int_distribution<int> d(lo, hi);
    return d(g_rng);
}

// ----------------------------------------------------------------------------
//  Map
// ----------------------------------------------------------------------------
const int MAP_W = 64;
const int MAP_H = 20;

struct Rect { int x, y, w, h;
    int cx() const { return x + w / 2; }
    int cy() const { return y + h / 2; }
    bool intersects(const Rect& o) const {
        return x <= o.x + o.w && x + w >= o.x &&
               y <= o.y + o.h && y + h >= o.y;
    }
};

struct Map {
    std::vector<char> tiles;   // '#', '.', '>', '*'
    Map() : tiles(MAP_W * MAP_H, '#') {}
    char  get(int x, int y) const {
        if (x < 0 || y < 0 || x >= MAP_W || y >= MAP_H) return '#';
        return tiles[y * MAP_W + x];
    }
    void  set(int x, int y, char c) {
        if (x < 0 || y < 0 || x >= MAP_W || y >= MAP_H) return;
        tiles[y * MAP_W + x] = c;
    }
    bool walkable(int x, int y) const {
        char c = get(x, y);
        return c == '.' || c == '>' || c == '*';
    }
};

// ----------------------------------------------------------------------------
//  Entities
// ----------------------------------------------------------------------------
struct Monster {
    int x, y;
    int hp, maxhp, atk;
    char glyph;
    std::string name;
    bool alive = true;
};

struct Player {
    int x = 0, y = 0;
    int hp = 24, maxhp = 24;
    int atk = 5;
    int gold = 0;
    int xp = 0, level = 1, nextXp = 10;
};

// ----------------------------------------------------------------------------
//  Items on the floor
// ----------------------------------------------------------------------------
struct Item {
    int x, y;
    char type;   // '!' potion, '$' gold
    int amount;
    bool taken = false;
};

// ----------------------------------------------------------------------------
//  Game
// ----------------------------------------------------------------------------
struct Game {
    Map map;
    Player player;
    std::vector<Monster> monsters;
    std::vector<Item> items;
    std::vector<Rect> rooms;
    std::vector<std::string> log;
    int depth = 1;
    bool running = true;
    bool won = false;

    static const int MAX_DEPTH = 10;

    void message(const std::string& s) {
        log.push_back(s);
        if (log.size() > 4) log.erase(log.begin());
    }

    // --- dungeon generation -------------------------------------------------
    void carveRoom(const Rect& r) {
        for (int yy = r.y; yy < r.y + r.h; ++yy)
            for (int xx = r.x; xx < r.x + r.w; ++xx)
                map.set(xx, yy, '.');
    }
    void carveHTunnel(int x1, int x2, int y) {
        for (int x = std::min(x1, x2); x <= std::max(x1, x2); ++x)
            if (map.get(x, y) == '#') map.set(x, y, '.');
    }
    void carveVTunnel(int y1, int y2, int x) {
        for (int y = std::min(y1, y2); y <= std::max(y1, y2); ++y)
            if (map.get(x, y) == '#') map.set(x, y, '.');
    }

    void generateLevel() {
        map = Map();
        monsters.clear();
        items.clear();
        rooms.clear();

        int wanted = randi(7, 10);
        for (int i = 0; i < wanted * 3 && (int)rooms.size() < wanted; ++i) {
            int w = randi(5, 11);
            int h = randi(3, 6);
            int x = randi(1, MAP_W - w - 2);
            int y = randi(1, MAP_H - h - 2);
            Rect r{ x, y, w, h };
            bool ok = true;
            for (auto& other : rooms)
                if (r.intersects(other)) { ok = false; break; }
            if (!ok) continue;

            carveRoom(r);
            if (!rooms.empty()) {
                // connect to previous room with an L-corridor
                int px = rooms.back().cx(), py = rooms.back().cy();
                if (randi(0, 1)) {
                    carveHTunnel(px, r.cx(), py);
                    carveVTunnel(py, r.cy(), r.cx());
                } else {
                    carveVTunnel(py, r.cy(), px);
                    carveHTunnel(px, r.cx(), r.cy());
                }
            }
            rooms.push_back(r);
        }

        // place player in the first room
        player.x = rooms.front().cx();
        player.y = rooms.front().cy();

        // place stairs (or amulet on the final floor) in the last room
        if (depth >= MAX_DEPTH)
            map.set(rooms.back().cx(), rooms.back().cy(), '*'); // Sunstone Amulet
        else
            map.set(rooms.back().cx(), rooms.back().cy(), '>');

        spawnMonsters();
        spawnItems();
    }

    bool tileFree(int x, int y) {
        if (!map.walkable(x, y)) return false;
        if (x == player.x && y == player.y) return false;
        for (auto& m : monsters)
            if (m.alive && m.x == x && m.y == y) return false;
        return true;
    }

    void spawnMonsters() {
        struct Kind { std::string name; char g; int hp, atk; int minDepth; };
        std::vector<Kind> kinds = {
            { "rat",        'r', 4,  2, 1 },
            { "kobold",     'k', 7,  3, 1 },
            { "skeleton",   's', 11, 4, 3 },
            { "ghoul",      'g', 16, 6, 5 },
            { "wraith",     'w', 22, 8, 7 },
            { "bone lord",  'B', 34, 11, 9 },
        };
        int count = 4 + depth + randi(0, 3);
        for (int i = 0; i < count; ++i) {
            // pick a room that's not the starting room
            if (rooms.size() < 2) break;
            const Rect& r = rooms[randi(1, (int)rooms.size() - 1)];
            int x = randi(r.x, r.x + r.w - 1);
            int y = randi(r.y, r.y + r.h - 1);
            if (!tileFree(x, y)) continue;

            // choose a kind eligible for this depth, biased toward tougher
            std::vector<Kind> pool;
            for (auto& k : kinds) if (k.minDepth <= depth) pool.push_back(k);
            Kind k = pool[randi(0, (int)pool.size() - 1)];
            int hpScale = (depth - 1);
            monsters.push_back(Monster{
                x, y, k.hp + hpScale, k.hp + hpScale,
                k.atk + depth / 3, k.g, k.name });
        }
    }

    void spawnItems() {
        int potions = randi(1, 3);
        int golds   = randi(2, 4);
        auto placeOn = [&](char type, int amount) {
            for (int tries = 0; tries < 50; ++tries) {
                const Rect& r = rooms[randi(0, (int)rooms.size() - 1)];
                int x = randi(r.x, r.x + r.w - 1);
                int y = randi(r.y, r.y + r.h - 1);
                if (tileFree(x, y) && !(x == player.x && y == player.y)
                    && map.get(x, y) == '.') {
                    items.push_back(Item{ x, y, type, amount });
                    return;
                }
            }
        };
        for (int i = 0; i < potions; ++i) placeOn('!', randi(8, 14));
        for (int i = 0; i < golds; ++i)   placeOn('$', randi(5, 25));
    }

    // --- combat & turns -----------------------------------------------------
    Monster* monsterAt(int x, int y) {
        for (auto& m : monsters)
            if (m.alive && m.x == x && m.y == y) return &m;
        return nullptr;
    }

    void gainXp(int amount) {
        player.xp += amount;
        while (player.xp >= player.nextXp) {
            player.xp -= player.nextXp;
            player.level++;
            player.nextXp = 10 + player.level * 8;
            player.maxhp += 6;
            player.hp = player.maxhp;          // full heal on level up
            player.atk += 2;
            message(std::string(col::GOODMSG) +
                    "You reach level " + std::to_string(player.level) +
                    "!  (+6 HP, +2 ATK)" + col::RESET);
        }
    }

    void attack(Monster& m) {
        int dmg = player.atk + randi(-1, 2);
        if (dmg < 1) dmg = 1;
        m.hp -= dmg;
        if (m.hp <= 0) {
            m.alive = false;
            int reward = 3 + (m.maxhp / 4);
            message("You slay the " + m.name + "! (+" +
                    std::to_string(reward) + " XP)");
            gainXp(reward);
        } else {
            message("You hit the " + m.name + " for " +
                    std::to_string(dmg) + ".");
        }
    }

    void pickup(int x, int y) {
        for (auto& it : items) {
            if (!it.taken && it.x == x && it.y == y) {
                if (it.type == '!') {
                    int heal = it.amount;
                    player.hp = std::min(player.maxhp, player.hp + heal);
                    message(std::string(col::GOODMSG) + "You quaff a potion (+" +
                            std::to_string(heal) + " HP)." + col::RESET);
                } else {
                    player.gold += it.amount;
                    message("You pick up " + std::to_string(it.amount) +
                            " gold.");
                }
                it.taken = true;
            }
        }
    }

    void monstersAct() {
        for (auto& m : monsters) {
            if (!m.alive) continue;
            int dx = player.x - m.x;
            int dy = player.y - m.y;
            // adjacent (orthogonal)? attack.
            if (std::abs(dx) + std::abs(dy) == 1) {
                int dmg = m.atk + randi(-1, 1);
                if (dmg < 1) dmg = 1;
                player.hp -= dmg;
                message(std::string(col::WARN) + "The " + m.name +
                        " hits you for " + std::to_string(dmg) + "." + col::RESET);
                continue;
            }
            // only pursue if reasonably close (cheap "vision")
            if (std::abs(dx) + std::abs(dy) > 9) continue;

            int stepX = (dx == 0) ? 0 : (dx > 0 ? 1 : -1);
            int stepY = (dy == 0) ? 0 : (dy > 0 ? 1 : -1);
            // try the longer axis first
            bool moved = false;
            if (std::abs(dx) >= std::abs(dy)) {
                if (stepX && tileFree(m.x + stepX, m.y)) { m.x += stepX; moved = true; }
                else if (stepY && tileFree(m.x, m.y + stepY)) { m.y += stepY; moved = true; }
            } else {
                if (stepY && tileFree(m.x, m.y + stepY)) { m.y += stepY; moved = true; }
                else if (stepX && tileFree(m.x + stepX, m.y)) { m.x += stepX; moved = true; }
            }
            (void)moved;
        }
    }

    void descend() {
        depth++;
        if (depth > MAX_DEPTH) { won = true; running = false; return; }
        message(std::string(col::STAIRS) + "You descend to floor " +
                std::to_string(depth) + "..." + col::RESET);
        generateLevel();
    }

    // attempt a player move/action by delta; returns true if a turn passed
    bool tryMove(int dx, int dy) {
        int nx = player.x + dx, ny = player.y + dy;
        if (Monster* m = monsterAt(nx, ny)) { attack(*m); return true; }
        if (!map.walkable(nx, ny)) return false;   // bump wall: free
        player.x = nx; player.y = ny;
        char t = map.get(nx, ny);
        if (t == '*') { won = true; running = false; return true; }
        if (t == '>') { descend(); return true; }
        pickup(nx, ny);
        return true;
    }

    // --- rendering ----------------------------------------------------------
    void render() {
        std::string out;
        out.reserve(MAP_W * MAP_H * 12);
        out += "\033[2J\033[H";   // clear + home

        out += std::string(col::HUD) + "  CRYPT CRAWLER";
        out += "   Floor " + std::to_string(depth) + "/" +
               std::to_string(MAX_DEPTH);
        out += std::string(col::RESET) + "\n";

        for (int y = 0; y < MAP_H; ++y) {
            out += "  ";
            for (int x = 0; x < MAP_W; ++x) {
                if (x == player.x && y == player.y) {
                    out += std::string(col::PLAYER) + "@" + col::RESET;
                    continue;
                }
                if (Monster* m = monsterAt(x, y)) {
                    out += std::string(col::MON) + m->glyph + col::RESET;
                    continue;
                }
                bool drewItem = false;
                for (auto& it : items)
                    if (!it.taken && it.x == x && it.y == y) {
                        out += std::string(it.type == '!' ? col::POTION : col::GOLD)
                               + it.type + col::RESET;
                        drewItem = true; break;
                    }
                if (drewItem) continue;

                char c = map.get(x, y);
                switch (c) {
                    case '#': out += std::string(col::WALL)   + "#" + col::RESET; break;
                    case '.': out += std::string(col::FLOOR)  + "." + col::RESET; break;
                    case '>': out += std::string(col::STAIRS) + ">" + col::RESET; break;
                    case '*': out += std::string(col::AMULET) + "*" + col::RESET; break;
                    default:  out += ' '; break;
                }
            }
            out += "\n";
        }

        // HUD
        out += "\n  " + std::string(col::HUD);
        out += "HP " + std::to_string(player.hp) + "/" +
               std::to_string(player.maxhp);
        out += "   LVL " + std::to_string(player.level);
        out += "   XP " + std::to_string(player.xp) + "/" +
               std::to_string(player.nextXp);
        out += "   ATK " + std::to_string(player.atk);
        out += "   Gold " + std::to_string(player.gold);
        out += std::string(col::RESET) + "\n\n";

        // message log
        for (auto& line : log) out += "  " + line + "\n";
        out += std::string(col::DIM) +
               "\n  move: wasd / hjkl   wait: .   quit: q" + col::RESET + "\n";

        std::cout << out << std::flush;
    }
};

// ----------------------------------------------------------------------------
//  Main loop
// ----------------------------------------------------------------------------
int main() {
    setupTerminal();
    std::cout << "\033[?25l"; // hide cursor

    Game game;
    game.generateLevel();
    game.message("You enter the crypt. Find the Sunstone Amulet on floor 10.");

    while (game.running && game.player.hp > 0) {
        game.render();
        int key = readKey();
        bool turn = false;
        switch (key) {
            case 'w': case 'k': turn = game.tryMove(0, -1); break;
            case 's': case 'j': turn = game.tryMove(0,  1); break;
            case 'a': case 'h': turn = game.tryMove(-1, 0); break;
            case 'd': case 'l': turn = game.tryMove(1,  0); break;
            case '.': case ' ': turn = true; break;           // wait
            case 'q': case -1:  game.running = false; break;  // quit / EOF
            default: break;
        }
        if (turn && game.running && game.player.hp > 0)
            game.monstersAct();
    }

    game.render();
    std::cout << "\033[?25h"; // show cursor

    if (game.won) {
        std::cout << "\n  " << col::AMULET
                  << "*** You grasp the Sunstone Amulet and escape the crypt! ***"
                  << col::RESET << "\n";
        std::cout << "  Final level " << game.player.level
                  << ", gold " << game.player.gold << ".  You win!\n\n";
    } else if (game.player.hp <= 0) {
        std::cout << "\n  " << col::WARN
                  << "You died on floor " << game.depth << ". The crypt keeps you."
                  << col::RESET << "\n\n";
    } else {
        std::cout << "\n  You leave the crypt. Until next time.\n\n";
    }

    restoreTerminal();
    return 0;
}
