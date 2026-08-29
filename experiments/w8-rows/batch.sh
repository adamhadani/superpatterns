#!/bin/zsh
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w8-rows
R=runs
# k=8, n=29 : word+Q wild rows / free / monotone-mixed
nohup ./sa4 -k 8 -n 29 -m 10 -R 3 -Q 2 -s 801 -i 2000000 -o $R/k8n29_m10_Q2_s801.out 2> $R/k8n29_m10_Q2_s801.err &
nohup ./sa4 -k 8 -n 29 -m 11 -R 3 -Q 3 -s 802 -i 2000000 -o $R/k8n29_m11_Q3_s802.out 2> $R/k8n29_m11_Q3_s802.err &
nohup ./sa4 -k 8 -n 29 -m 10 -R 2      -s 803 -i 2000000 -o $R/k8n29_m10_R2_s803.out 2> $R/k8n29_m10_R2_s803.err &
nohup ./sa4 -k 8 -n 29 -m 11 -R 1      -s 804 -i 2000000 -o $R/k8n29_m11_R1_s804.out 2> $R/k8n29_m11_R1_s804.err &
# periodic block families with free row patterns (covering-radius test)
nohup ./sa4 -k 7 -m 8  -P 3 -R 2 -s 701 -i 400000 -o $R/k7_P3m8_R2_s701.out 2> $R/k7_P3m8_R2_s701.err &
nohup ./sa4 -k 8 -m 9  -P 3 -R 2 -s 811 -i 400000 -o $R/k8_P3m9_R2_s811.out 2> $R/k8_P3m9_R2_s811.err &
nohup ./sa4 -k 8 -m 10 -P 3 -R 2 -s 812 -i 400000 -o $R/k8_P3m10_R2_s812.out 2> $R/k8_P3m10_R2_s812.err &
nohup ./sa4 -k 6 -m 8  -P 2 -R 2 -s 601 -i 400000 -o $R/k6_P2m8_R2_s601.out 2> $R/k6_P2m8_R2_s601.err &
# k=9
nohup ./sa4 -k 9 -n 38 -m 12 -R 3 -Q 3 -s 901 -i 400000 -o $R/k9n38_m12_Q3_s901.out 2> $R/k9n38_m12_Q3_s901.err &
nohup ./sa4 -k 9 -n 38 -m 13 -R 2      -s 902 -i 400000 -o $R/k9n38_m13_R2_s902.out 2> $R/k9n38_m13_R2_s902.err &
nohup ./sa4 -k 9 -m 12 -P 3 -R 2       -s 911 -i 100000 -o $R/k9_P3m12_R2_s911.out 2> $R/k9_P3m12_R2_s911.err &
