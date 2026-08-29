#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w2-construction
for m in 8 10 12 17; do for s in 1 2 3; do ./sa 6 17 $m 200000 $s > runs/k6_n17_m${m}_s$s.txt 2>/dev/null & done; done; wait
for m in 8 9 10 12 14; do for s in 1 2; do ./sa 7 24 $m 100000 $s > runs/k7_n24_m${m}_s$s.txt 2>/dev/null & done; done; wait
