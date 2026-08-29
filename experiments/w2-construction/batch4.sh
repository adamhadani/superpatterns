#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w2-construction
for s in 1 2 3; do ./sa3 7 8 3 200000 $s > runs/sa3_k7_m8_B3_s$s.txt 2>/dev/null & done
./sa3 8 10 3 4000 1 > runs/sa3_k8_m10_B3_s1.txt 2>/dev/null &
./sa3 8 8 4 4000 1 > runs/sa3_k8_m8_B4_s1.txt 2>/dev/null &
wait
