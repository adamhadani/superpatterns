#!/bin/zsh
cd "$(dirname "$0")"
for C in 0.8 0.85 0.9 1.0; do for k in 100 200 400; do
  nice -n 15 ./gg runs $k $C 300 21 2 0 0.7 0.75
  nice -n 15 ./gg runs $k $C 300 21 2 0 0.5 0.5
done; done
