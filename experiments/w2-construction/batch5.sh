#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w2-construction
./sa3 8 9 3 6000 1 > runs/sa3_k8_m9_B3_s1.txt 2>/dev/null &
./sa3 8 9 3 6000 2 > runs/sa3_k8_m9_B3_s2.txt 2>/dev/null &
./sa3 8 10 3 4000 2 > runs/sa3_k8_m10_B3_s2.txt 2>/dev/null &
./sa2 8 30 9 4000 1 > runs/sa2_k8_n30_m9_s1.txt 2>/dev/null &
./sa2 8 31 9 4000 1 > runs/sa2_k8_n31_m9_s1.txt 2>/dev/null &
./sa2 8 31 10 4000 2 > runs/sa2_k8_n31_m10_s2.txt 2>/dev/null &
wait
