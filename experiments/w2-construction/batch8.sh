#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w2-construction
./sa3 8 9 4 3000 1 > runs/sa3_k8_m9_B4_s1.txt 2>runs/sa3_k8_m9_B4_s1.err &
./sa3 8 9 4 3000 2 > runs/sa3_k8_m9_B4_s2.txt 2>runs/sa3_k8_m9_B4_s2.err &
./sa3 9 10 4 1500 1 > runs/sa3_k9_m10_B4_s1.txt 2>runs/sa3_k9_m10_B4_s1.err &
./sa3 9 10 4 1500 2 > runs/sa3_k9_m10_B4_s2.txt 2>runs/sa3_k9_m10_B4_s2.err &
wait
