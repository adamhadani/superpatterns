#!/bin/sh
# Independent cross-check batches (numpy PCG64 permutations; W40 pruned.c vs W90 l21_paired.c; Python LIS).
cd "$(dirname "$0")"
# Binaries are built into $W90_BIN (default /tmp/w90-bin); they are not kept in the repository.
W90_BIN=${W90_BIN:-/tmp/w90-bin}; mkdir -p "$W90_BIN"
[ -x "$W90_BIN/l21_paired" ]     || cc -O2 -o "$W90_BIN/l21_paired" l21_paired.c -lm
[ -x "$W90_BIN/layered_paired" ] || cc -O2 -o "$W90_BIN/layered_paired" layered_paired.c -lm
[ -x "$W90_BIN/hybrid_profile" ] || cc -O2 -o "$W90_BIN/hybrid_profile" hybrid_profile.c -lm
[ -x "$W90_BIN/w40_pruned" ]     || cc -O2 -o "$W90_BIN/w40_pruned" ../w40-c21-frontier/pruned.c
W40=${W40:-$W90_BIN/w40_pruned}; W90=${W90:-$W90_BIN/l21_paired}
for s in 11 12 13 14 15 16; do python3 crosscheck_w40.py $W40 $W90 10000 12000 $s > out/cross_n10000_s$s.txt & done; wait
for s in 21 22 23 24 25 26; do python3 crosscheck_w40.py $W40 $W90 100000 1500 $s > out/cross_n100000_s$s.txt & done; wait
for s in 31 32 33 34; do python3 crosscheck_w40.py $W40 $W90 1000000 60 $s > out/cross_n1000000_s$s.txt & done; wait
echo done > out/CROSS_DONE
