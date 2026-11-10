#!/bin/sh
# Family sweep: paired (layered prefix length, LIS) for several periodic layer-size sequences.
# Each job: layered_paired <sizes> <n> <samples> <seed>  -> out/fam_<sizes>_n<n>_s<seed>.txt
cd "$(dirname "$0")"
# Binaries are built into $W90_BIN (default /tmp/w90-bin); they are not kept in the repository.
W90_BIN=${W90_BIN:-/tmp/w90-bin}; mkdir -p "$W90_BIN"
[ -x "$W90_BIN/l21_paired" ]     || cc -O2 -o "$W90_BIN/l21_paired" l21_paired.c -lm
[ -x "$W90_BIN/layered_paired" ] || cc -O2 -o "$W90_BIN/layered_paired" layered_paired.c -lm
[ -x "$W90_BIN/hybrid_profile" ] || cc -O2 -o "$W90_BIN/hybrid_profile" hybrid_profile.c -lm
[ -x "$W90_BIN/w40_pruned" ]     || cc -O2 -o "$W90_BIN/w40_pruned" ../w40-c21-frontier/pruned.c
BIN=${BIN:-$W90_BIN/layered_paired}
jobs() {
  for sz in 2 3 4 5 6 1,2 1,3 1,4 2,3 1,1,2 1,1,1,2 1,2,2; do
    for seed in 1 2 3; do echo "$sz 10000 10000 $seed"; done
  done
  for sz in 2 3 4 5 6 1,2 1,3 1,4 2,3 1,1,2 1,1,1,2 1,2,2; do
    for seed in 1 2 3; do echo "$sz 100000 2000 $seed"; done
  done
  for sz in 2 3 4 1,2 1,3 1,4 2,3 1,1,2 1,1,1,2 1,2,2; do
    for seed in 1 2 3; do echo "$sz 1000000 200 $seed"; done
  done
  for sz in 5 6; do for seed in 1 2 3; do echo "$sz 1000000 70 $seed"; done; done
}
jobs | xargs -P ${NPROC:-5} -L 1 sh -c 'f=out/fam_$(echo $1 | tr , _)_n$2_s$4.txt; '"$BIN"' $1 $2 $3 $(($2+$4)) > $f' _
echo done > out/FAM_DONE
