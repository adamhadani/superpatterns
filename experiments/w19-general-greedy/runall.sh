#!/bin/zsh
cd "$(dirname "$0")"
( for k in 64 100 144; do for C in 0.5 1 2; do
    nice -n 15 ./gg rows $k $C 400 7
    for L in 0 2 3 4; do nice -n 15 ./gg runs $k $C 400 7 $L; done
    nice -n 15 ./gg verbatim $k $C 100 7 $(python3 -c "import math;print(int(math.sqrt($k)))")
  done; done ) > out_general.txt 2>&1 &
( for k in 64 100 144; do r=$(python3 -c "import math;print(int(math.sqrt($k)))"); for C in 1 2 4 8; do for d in 0 0.25 0.4; do
    nice -n 15 ./gg grid $k $C 400 7 $r $d
  done; done; done ) > out_grid.txt 2>&1 &
wait
