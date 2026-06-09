# Makefile for the raylib demos in this folder.
#
# Usage:
#   make            # build everything
#   make boids      # build just the boids simulation
#   make run        # build and launch the boids simulation
#   make clean      # remove built binaries

CXX      := g++
CXXFLAGS := -std=c++17 -O2 -Wall

# Locate raylib via Homebrew.
RAYLIB_PREFIX := $(shell brew --prefix raylib)
RAYLIB_INC    := -I$(RAYLIB_PREFIX)/include
RAYLIB_LIB    := -L$(RAYLIB_PREFIX)/lib -lraylib

# macOS frameworks raylib depends on.
FRAMEWORKS := -framework OpenGL -framework Cocoa -framework IOKit \
              -framework CoreVideo -framework CoreAudio

.PHONY: all run clean

all: boids mandelbrot

boids: boids.cpp
	$(CXX) $(CXXFLAGS) $< -o $@ $(RAYLIB_INC) $(RAYLIB_LIB) $(FRAMEWORKS)

mandelbrot: mandelbrot.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

run: boids
	./boids

clean:
	rm -f boids mandelbrot
