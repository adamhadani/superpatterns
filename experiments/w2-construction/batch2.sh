#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w2-construction
for s in 11 12 13 14; do ./sa 7 24 24 400000 $s 4 11 18 24 21 14 7 3 10 17 20 13 6 2 9 16 23 19 12 5 1 8 15 22 > runs/k7_n24_seedzeta_s$s.txt 2>/dev/null & done
for s in 21 22 23 24; do ./sa 7 24 24 600000 $s > runs/k7_n24_m24_s$s.txt 2>/dev/null & done
wait
