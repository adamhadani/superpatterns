#!/bin/bash
# usage: ./run_allpat.sh N [P]   -- exact counts for all patterns (k<=7) at length N.
# Enumerates only sigma with sigma(1)<sigma(N) and sigma(1)+sigma(N)<=N+1 (Klein 4-group
# fundamental domain); combine.py reconstructs full counts.  P = parallelism (default 10).
set -e
N=$1; P=${2:-10}
D=$(dirname "$0")/data/n$N
mkdir -p "$D"
TASKS=""
for ((a=1;a<=N;a++)); do for ((b=a+1;b<=N;b++)); do
  s=$((a+b))
  if [ $s -lt $((N+1)) ]; then TASKS="$TASKS $N $a $b $D/lt_${a}_${b}.txt"$'\n'; fi
  if [ $s -eq $((N+1)) ]; then TASKS="$TASKS $N $a $b $D/eq_${a}_${b}.txt"$'\n'; fi
done; done
echo "$TASKS" | grep -v '^ *$' | xargs -P $P -L1 $(dirname "$0")/allpat
echo done n=$N
