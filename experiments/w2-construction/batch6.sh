#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w2-construction
for s in 1 2 3; do ./sa2 7 23 8 300000 $s > runs/sa2_k7_n23_m8_s$s.txt 2>/dev/null & done
for s in 1 2; do ./sa2 7 23 9 300000 $s > runs/sa2_k7_n23_m9_s$s.txt 2>/dev/null & done
wait
