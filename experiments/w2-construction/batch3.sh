#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w2-construction
for s in 1 2 3 4; do ./sa2 6 17 7 300000 $s > runs/sa2_k6_n17_m7_s$s.txt 2>/dev/null & done
for s in 1 2; do ./sa2 6 17 8 300000 $s > runs/sa2_k6_n17_m8_s$s.txt 2>/dev/null & done
wait
for s in 1 2 3 4; do ./sa2 7 24 8 300000 $s > runs/sa2_k7_n24_m8_s$s.txt 2>/dev/null & done
for s in 1 2; do ./sa2 7 24 9 300000 $s > runs/sa2_k7_n24_m9_s$s.txt 2>/dev/null & done
wait
