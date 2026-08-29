#!/bin/bash
cd "$(dirname "$0")"
jobs=()
for k in 12 18 24; do for r in 1 2 3; do h=$((k/r)); for C in 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.7; do
  N=$(python3 -c "print(round($C*$k*$k))"); jobs+=("$r $h $N 200000")
done; done; done
printf '%s\n' "${jobs[@]}" | xargs -P 3 -L 1 sh -c './tg $0 $1 $2 $3 11 >> out/fix2.txt'
echo done > out/DONE2
