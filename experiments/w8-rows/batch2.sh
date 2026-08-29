#!/bin/zsh
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w8-rows; R=runs
EXH=1 nohup ./wild -k 7 -m 8 -P 3 > $R/wild_k7_P3m8_EXH.out 2> $R/wild_k7_P3m8_EXH.err &
EXH=1 nohup ./wild -k 6 -m 8 -P 2 > $R/wild_k6_P2m8_EXH.out 2> $R/wild_k6_P2m8_EXH.err &
nohup ./wild -k 8 -m 9  -P 3 -i 20000 -s 1 > $R/wild_k8_P3m9.out 2> $R/wild_k8_P3m9.err &
nohup ./wild -k 8 -m 10 -P 3 -i 20000 -s 1 > $R/wild_k8_P3m10.out 2> $R/wild_k8_P3m10.err &
nohup ./wild -k 8 -n 29 -m 10 -i 20000 -s 1 > $R/wild_k8n29_m10.out 2> $R/wild_k8n29_m10.err &
nohup ./wild -k 8 -n 29 -m 12 -i 20000 -s 1 > $R/wild_k8n29_m12.out 2> $R/wild_k8n29_m12.err &
nohup ./wild -k 9 -m 12 -P 3 -i 5000 -s 1 > $R/wild_k9_P3m12.out 2> $R/wild_k9_P3m12.err &
nohup ./wild -k 9 -n 38 -m 13 -i 5000 -s 1 > $R/wild_k9n38_m13.out 2> $R/wild_k9n38_m13.err &
