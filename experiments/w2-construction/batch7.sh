#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w2-construction
./sa3 9 10 3 3000 1 > runs/sa3_k9_m10_B3_s1.txt 2>runs/sa3_k9_m10_B3_s1.err &
./sa3 9 11 3 1500 1 > runs/sa3_k9_m11_B3_s1.txt 2>runs/sa3_k9_m11_B3_s1.err &
./sa3 9 12 3 800 1 > runs/sa3_k9_m12_B3_s1.txt 2>runs/sa3_k9_m12_B3_s1.err &
wait
