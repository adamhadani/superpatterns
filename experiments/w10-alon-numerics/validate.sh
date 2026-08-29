#!/bin/bash
# fast vs brute force on identical permutations, all tau in S_3,S_4,S_5
python3 -c "
import itertools
for j in (2,3,4,5):
    for p in itertools.permutations(range(1,j+1)): print(''.join(map(str,p)))
" > taus.txt
fail=0; tot=0
while read t; do
  for N in 12 25 45; do
    for seed in 1 2 3; do
      a=$(./tchain $N 4 $t $seed | awk '{print $4}' | tr '\n' ' ')
      b=$(./tchain -bf $N 4 $t $seed | awk '{print $4}' | tr '\n' ' ')
      tot=$((tot+1))
      if [ "$a" != "$b" ]; then echo "MISMATCH tau=$t N=$N seed=$seed fast=[$a] bf=[$b]"; fail=$((fail+1)); fi
    done
  done
done < taus.txt
echo "validation: $tot cases (x4 samples), $fail mismatches"
