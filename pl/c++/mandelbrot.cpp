// mandelbrot.cpp — Render the Mandelbrot set in your terminal with ANSI colors.
//
// Each terminal cell is mapped to a point in the complex plane. We iterate the
// classic z = z^2 + c map and color each pixel by how quickly it escapes to
// infinity. Points that never escape (inside the set) are drawn in black.

#include <complex>
#include <cstdint>
#include <iostream>
#include <string>

int main() {
    // Output resolution (characters). Tweak to taste / terminal size.
    constexpr int width  = 100;
    constexpr int height = 40;

    // Region of the complex plane to view.
    constexpr double minRe = -2.5, maxRe = 1.0;
    constexpr double minIm = -1.25, maxIm = 1.25;

    constexpr int maxIter = 200;

    std::string frame;
    frame.reserve(static_cast<std::size_t>(width) * height * 20);

    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            const double re = minRe + (maxRe - minRe) * x / (width  - 1);
            const double im = minIm + (maxIm - minIm) * y / (height - 1);

            const std::complex<double> c(re, im);
            std::complex<double> z(0.0, 0.0);

            int iter = 0;
            while (iter < maxIter && std::norm(z) <= 4.0) {
                z = z * z + c;
                ++iter;
            }

            if (iter == maxIter) {
                // Inside the set: draw a solid black block.
                frame += "\033[48;5;0m \033[0m";
            } else {
                // Map escape time to a smooth 256-color gradient.
                const std::uint8_t color =
                    static_cast<std::uint8_t>(16 + (iter * 200 / maxIter) % 216);
                frame += "\033[48;5;" + std::to_string(color) + "m \033[0m";
            }
        }
        frame += '\n';
    }

    std::cout << frame;
    std::cout << "\nMandelbrot set — " << width << "x" << height
              << ", " << maxIter << " iterations.\n";
    return 0;
}
