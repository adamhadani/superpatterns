#!/bin/zsh
cd "$(dirname "$0")"
for C in 0.5 0.6 0.7 0.8 0.9 1.0 1.2; do
  nice -n 15 ./gg rows 100 $C 400 11
  nice -n 15 ./gg runs 100 $C 400 11 2 0
  nice -n 15 ./gg runs 100 $C 400 11 2 1
  nice -n 15 ./gg runs 100 $C 400 11 3 1
done
