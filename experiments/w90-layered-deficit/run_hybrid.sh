#!/bin/sh
# Hybrid profile: cost of converting the first i blocks 12 -> 21 (rest of the pattern increasing), paired with LIS.
cd "$(dirname "$0")"
# Binaries are built into $W90_BIN (default /tmp/w90-bin); they are not kept in the repository.
W90_BIN=${W90_BIN:-/tmp/w90-bin}; mkdir -p "$W90_BIN"
[ -x "$W90_BIN/l21_paired" ]     || cc -O2 -o "$W90_BIN/l21_paired" l21_paired.c -lm
[ -x "$W90_BIN/layered_paired" ] || cc -O2 -o "$W90_BIN/layered_paired" layered_paired.c -lm
[ -x "$W90_BIN/hybrid_profile" ] || cc -O2 -o "$W90_BIN/hybrid_profile" hybrid_profile.c -lm
[ -x "$W90_BIN/w40_pruned" ]     || cc -O2 -o "$W90_BIN/w40_pruned" ../w40-c21-frontier/pruned.c
BIN=${BIN:-$W90_BIN/hybrid_profile}
for s in 1 2 3; do $BIN 10000 20000 $((7000+s)) 1,2,3,4,6,8,12,16,24,32,48,64 > out/hybrid_n10000_s$s.txt & done; wait
for s in 1 2 3; do $BIN 100000 1500 $((8000+s)) 8,16,32,64,128,192,256 > out/hybrid_n100000_s$s.txt & done; wait
echo done > out/HYBRID_DONE
