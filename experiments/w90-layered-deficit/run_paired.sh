#!/bin/sh
# usage: run_l21.sh ; runs paired L21/LIS batches, 7 parallel workers per size
cd "$(dirname "$0")"
# Binaries are built into $W90_BIN (default /tmp/w90-bin); they are not kept in the repository.
W90_BIN=${W90_BIN:-/tmp/w90-bin}; mkdir -p "$W90_BIN"
[ -x "$W90_BIN/l21_paired" ]     || cc -O2 -o "$W90_BIN/l21_paired" l21_paired.c -lm
[ -x "$W90_BIN/layered_paired" ] || cc -O2 -o "$W90_BIN/layered_paired" layered_paired.c -lm
[ -x "$W90_BIN/hybrid_profile" ] || cc -O2 -o "$W90_BIN/hybrid_profile" hybrid_profile.c -lm
[ -x "$W90_BIN/w40_pruned" ]     || cc -O2 -o "$W90_BIN/w40_pruned" ../w40-c21-frontier/pruned.c
run() { n=$1; per=$2; for w in 1 2 3 4 5 6 7; do "$W90_BIN/l21_paired" $n $per $((n+1000*w)) > out/l21_n${n}_w${w}.txt & done; wait; }
run 1000 100000
run 10000 60000
run 100000 20000
run 1000000 4000
run 10000000 400
echo done > out/DONE
