#!/bin/sh
# review-2 numerical runs; at most 4 processes at a time. Usage: sh run_all.sh   (from this directory; needs ./l21rev)
# est: per T, 4 seeds x S samples.   cut: per T, 4 seeds x S samples.
set -e
mkdir -p out
run4() { mode=$1; T=$2; S=$3; base=$4
  for j in 1 2 3 4; do ./l21rev $mode $T $S $((base+j)) > out/${mode}_T${T}_s$((base+j)).txt & done; wait; }
run4 est 10 50000 1000
run4 est 20 50000 1100
run4 est 25 50000 1200
run4 est 40 50000 1300
run4 est 50 50000 1400
run4 est 80 25000 1500
run4 est 100 25000 1600
run4 est 200 10000 1700
run4 est 400 5000 1800
run4 est 800 2500 1900
touch out/EST_DONE
run4 cut 10 500 2000
run4 cut 20 250 2100
run4 cut 40 75 2200
touch out/CUT_DONE
