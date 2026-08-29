#!/bin/zsh
cd "$(dirname "$0")"
for C in 0.78 0.8 0.85; do for k in 100 200 400 800; do
  nice -n 15 ./gg runs $k $C 300 23 2 1 0.4 1.1
done; done
