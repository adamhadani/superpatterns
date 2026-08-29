#!/bin/bash
# fixed-strip absence probabilities: r in 1,2,3; k = 12,18,24,30; N = C k^2
cd "$(dirname "$0")"
jobs=()
for k in 12 18 24 30; do for r in 1 2 3; do h=$((k/r)); for C in 0.5 0.75 1 1.5 2 3; do
  N=$(python3 -c "print(round($C*$k*$k))"); reps=100000
  jobs+=("$r $h $N $reps")
done; done; done
printf '%s\n' "${jobs[@]}" | xargs -P 3 -L 1 sh -c './tg $0 $1 $2 $3 7 >> out/fix.txt'
echo done > out/DONE
