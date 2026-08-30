#!/bin/bash
# W38 canonical grid: pairs_can (1e6 samples/j) for k=4..10, C in {0.15,...,1}; exact_can where binom(N,k) <= 4e7.
cd "$(dirname "$0")"; mkdir -p out
for k in 4 5 6 7 8 9 10; do for C in 0.15 0.2 0.25 0.3 0.5 1; do
  N=$(python3 -c "print(round($C*$k*$k))"); [ $N -lt $k ] && continue
  ./pairs_can $k $N 1000000 7 > out/pairscan_k${k}_C${C}.txt
  B=$(python3 -c "from math import comb;print(comb($N,$k))")
  if [ $B -le 40000000 ]; then S=$(python3 -c "print(max(50,min(4000,int(2e9/$B))))"); ./exact_can $k $N $S 11 > out/exactcan_k${k}_C${C}.txt; fi
done; done
echo DONE > out/gridcan.done
