// boids.cpp — Interactive boids flocking simulation with raylib.
//
// Craig Reynolds' classic three rules — separation, alignment, cohesion —
// produce emergent flocking from simple local interactions. This build adds:
//   * velocity-based HSV coloring so the flock shimmers as it turns
//   * motion-blur trails via a translucent fade rectangle each frame
//   * an interactive predator: hold the LEFT mouse button to scatter the flock,
//     hold the RIGHT mouse button to attract it
//   * live, tweakable parameters (see the keyboard controls below)
//
// Controls:
//   Left mouse   - repel boids from cursor (predator)
//   Right mouse  - attract boids to cursor
//   Up / Down    - increase / decrease number of boids
//   Q / A        - increase / decrease perception radius
//   Space        - pause / resume
//   R            - reset the flock
//   Esc          - quit

#include "raylib.h"
#include "raymath.h"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <vector>

namespace {

constexpr int   kScreenWidth  = 1280;
constexpr int   kScreenHeight = 800;
constexpr float kMaxSpeed     = 4.5f;
constexpr float kMaxForce     = 0.18f;

struct Boid {
    Vector2 position;
    Vector2 velocity;
};

// Clamp a vector's length to at most maxLen.
Vector2 LimitMagnitude(Vector2 v, float maxLen) {
    const float lenSq = v.x * v.x + v.y * v.y;
    if (lenSq > maxLen * maxLen && lenSq > 0.0f) {
        const float scale = maxLen / std::sqrt(lenSq);
        v.x *= scale;
        v.y *= scale;
    }
    return v;
}

// Steer from a desired velocity toward a capped steering force.
Vector2 SteerToward(Vector2 desired, Vector2 velocity) {
    desired = LimitMagnitude(desired, kMaxSpeed);
    Vector2 steer = Vector2Subtract(desired, velocity);
    return LimitMagnitude(steer, kMaxForce);
}

Boid MakeRandomBoid() {
    Boid b;
    b.position = {
        static_cast<float>(GetRandomValue(0, kScreenWidth)),
        static_cast<float>(GetRandomValue(0, kScreenHeight)),
    };
    const float angle = static_cast<float>(GetRandomValue(0, 359)) * DEG2RAD;
    const float speed = 2.0f + static_cast<float>(GetRandomValue(0, 100)) / 50.0f;
    b.velocity = { std::cos(angle) * speed, std::sin(angle) * speed };
    return b;
}

void ResetFlock(std::vector<Boid>& boids, int count) {
    boids.clear();
    boids.reserve(static_cast<std::size_t>(count));
    for (int i = 0; i < count; ++i) boids.push_back(MakeRandomBoid());
}

}  // namespace

int main() {
    SetConfigFlags(FLAG_MSAA_4X_HINT | FLAG_VSYNC_HINT);
    InitWindow(kScreenWidth, kScreenHeight, "Boids — flocking simulation (raylib)");
    SetTargetFPS(60);

    int   boidCount  = 400;
    float perception = 55.0f;   // neighbor radius
    bool  paused     = false;

    std::vector<Boid> boids;
    ResetFlock(boids, boidCount);

    // Trail buffer: a render texture we fade slightly each frame.
    RenderTexture2D canvas = LoadRenderTexture(kScreenWidth, kScreenHeight);
    BeginTextureMode(canvas);
    ClearBackground(BLACK);
    EndTextureMode();

    while (!WindowShouldClose()) {
        // ---- Input -------------------------------------------------------
        if (IsKeyPressed(KEY_SPACE)) paused = !paused;
        if (IsKeyPressed(KEY_R))     ResetFlock(boids, boidCount);

        if (IsKeyPressed(KEY_UP)) {
            boidCount = std::min(boidCount + 50, 3000);
            while (static_cast<int>(boids.size()) < boidCount) boids.push_back(MakeRandomBoid());
        }
        if (IsKeyPressed(KEY_DOWN)) {
            boidCount = std::max(boidCount - 50, 50);
            boids.resize(static_cast<std::size_t>(boidCount));
        }
        if (IsKeyDown(KEY_Q)) perception = std::min(perception + 1.0f, 160.0f);
        if (IsKeyDown(KEY_A)) perception = std::max(perception - 1.0f, 15.0f);

        const Vector2 mouse   = GetMousePosition();
        const bool    repel   = IsMouseButtonDown(MOUSE_BUTTON_LEFT);
        const bool    attract = IsMouseButtonDown(MOUSE_BUTTON_RIGHT);
        const float   percepSq = perception * perception;

        // ---- Simulation --------------------------------------------------
        if (!paused) {
            std::vector<Vector2> newVel(boids.size());

            for (std::size_t i = 0; i < boids.size(); ++i) {
                const Boid& self = boids[i];

                Vector2 sep = {0, 0}, ali = {0, 0}, coh = {0, 0};
                int neighbors = 0;

                for (std::size_t j = 0; j < boids.size(); ++j) {
                    if (i == j) continue;
                    const Vector2 diff = Vector2Subtract(self.position, boids[j].position);
                    const float distSq = diff.x * diff.x + diff.y * diff.y;
                    if (distSq > percepSq || distSq <= 0.0001f) continue;

                    // Separation weighted by inverse distance.
                    sep = Vector2Add(sep, Vector2Scale(diff, 1.0f / distSq));
                    ali = Vector2Add(ali, boids[j].velocity);
                    coh = Vector2Add(coh, boids[j].position);
                    ++neighbors;
                }

                Vector2 accel = {0, 0};
                if (neighbors > 0) {
                    const float inv = 1.0f / static_cast<float>(neighbors);
                    Vector2 sepSteer = SteerToward(sep, self.velocity);
                    Vector2 aliSteer = SteerToward(Vector2Scale(ali, inv), self.velocity);
                    Vector2 cohTarget = Vector2Subtract(Vector2Scale(coh, inv), self.position);
                    Vector2 cohSteer = SteerToward(cohTarget, self.velocity);

                    accel = Vector2Add(accel, Vector2Scale(sepSteer, 1.6f));
                    accel = Vector2Add(accel, Vector2Scale(aliSteer, 1.0f));
                    accel = Vector2Add(accel, Vector2Scale(cohSteer, 1.0f));
                }

                // Predator / attractor from the mouse.
                if (repel || attract) {
                    Vector2 toMouse = Vector2Subtract(mouse, self.position);
                    const float d = Vector2Length(toMouse);
                    if (d < 220.0f && d > 0.1f) {
                        Vector2 dir = Vector2Scale(toMouse, 1.0f / d);
                        const float strength = (1.0f - d / 220.0f) * 1.8f;
                        if (repel)   accel = Vector2Subtract(accel, Vector2Scale(dir, strength));
                        if (attract) accel = Vector2Add(accel, Vector2Scale(dir, strength));
                    }
                }

                Vector2 v = Vector2Add(self.velocity, accel);
                v = LimitMagnitude(v, kMaxSpeed);
                newVel[i] = v;
            }

            // Integrate + wrap around screen edges.
            for (std::size_t i = 0; i < boids.size(); ++i) {
                boids[i].velocity = newVel[i];
                boids[i].position = Vector2Add(boids[i].position, boids[i].velocity);

                if (boids[i].position.x < 0)             boids[i].position.x += kScreenWidth;
                if (boids[i].position.x >= kScreenWidth)  boids[i].position.x -= kScreenWidth;
                if (boids[i].position.y < 0)             boids[i].position.y += kScreenHeight;
                if (boids[i].position.y >= kScreenHeight) boids[i].position.y -= kScreenHeight;
            }
        }

        // ---- Draw flock into the trail canvas ----------------------------
        BeginTextureMode(canvas);
        // Fade previous frame slightly to create motion trails.
        DrawRectangle(0, 0, kScreenWidth, kScreenHeight, Color{0, 0, 0, 28});

        for (const Boid& b : boids) {
            const float speed = Vector2Length(b.velocity);
            const float hue   = std::fmod(speed / kMaxSpeed * 200.0f + 190.0f, 360.0f);
            const Color col   = ColorFromHSV(hue, 0.85f, 1.0f);

            // Draw each boid as a little triangle pointing along its velocity.
            const float angle = std::atan2(b.velocity.y, b.velocity.x);
            const float size  = 5.0f;
            const Vector2 tip = {
                b.position.x + std::cos(angle) * size * 1.8f,
                b.position.y + std::sin(angle) * size * 1.8f,
            };
            const Vector2 left = {
                b.position.x + std::cos(angle + 2.5f) * size,
                b.position.y + std::sin(angle + 2.5f) * size,
            };
            const Vector2 right = {
                b.position.x + std::cos(angle - 2.5f) * size,
                b.position.y + std::sin(angle - 2.5f) * size,
            };
            DrawTriangle(tip, left, right, col);
        }
        EndTextureMode();

        // ---- Composite to screen + HUD -----------------------------------
        BeginDrawing();
        ClearBackground(BLACK);
        // RenderTextures are flipped vertically, so draw with a negative source height.
        DrawTextureRec(canvas.texture,
                       Rectangle{0, 0, (float)canvas.texture.width, (float)-canvas.texture.height},
                       Vector2{0, 0}, WHITE);

        DrawRectangle(10, 10, 330, 150, Color{0, 0, 0, 150});
        DrawText(TextFormat("Boids: %d", boidCount), 24, 24, 20, RAYWHITE);
        DrawText(TextFormat("Perception: %.0f", perception), 24, 50, 20, RAYWHITE);
        DrawText(TextFormat("FPS: %d%s", GetFPS(), paused ? "  [PAUSED]" : ""), 24, 76, 20, RAYWHITE);
        DrawText("LMB scatter | RMB attract", 24, 106, 18, GRAY);
        DrawText("Up/Down count  Q/A radius  R reset", 24, 130, 18, GRAY);

        EndDrawing();
    }

    UnloadRenderTexture(canvas);
    CloseWindow();
    return 0;
}
