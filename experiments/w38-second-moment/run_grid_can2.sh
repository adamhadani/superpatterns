#!/bin/bash
# W38 canonical grid v2: exact_can2 (with overlap decomposition) wherever binom(N,k) <= 4e7.
cd "$(dirname "$0")"; mkdir -p out
for k in 4 5 6 7 8 9 10; do for C in 0.15 0.2 0.25 0.3 0.5 1; do
  N=$(python3 -c "print(round($C*$k*$k))"); [ $N -lt $k ] && continue
  B=$(python3 -c "from math import comb;print(comb($N,$k))")
  if [ $B -le 40000000 ]; then S=$(python3 -c "print(max(60,min(4000,int(2e9/$B))))"); ./exact_can2 $k $N $S 11 > out/exactcan_k${k}_C${C}.txt; fi
done; done
echo DONE > out/gridcan2.done
