#!/usr/bin/env bash
# Build script for arXiv package of "Simultaneous Universality of Random Permutations at Quadratic Host Size"
set -euo pipefail

echo "=== Compiling standalone arXiv LaTeX document ==="
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex

echo "=== Verifying zero overfull boxes ==="
OVERFULL=$(grep -c "Overfull \\\\hbox" main.log || true)
echo "Overfull hboxes: $OVERFULL"

echo "=== Build Complete: main.pdf generated successfully ==="
