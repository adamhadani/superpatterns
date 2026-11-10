#!/bin/sh
# Follow-up batches: (i) larger layer sizes at n = 10^5; (ii) the pure 21 pattern at n = 10^8.
cd "$(dirname "$0")"
# Binaries are built into $W90_BIN (default /tmp/w90-bin); they are not kept in the repository.
W90_BIN=${W90_BIN:-/tmp/w90-bin}; mkdir -p "$W90_BIN"
[ -x "$W90_BIN/l21_paired" ]     || cc -O2 -o "$W90_BIN/l21_paired" l21_paired.c -lm
[ -x "$W90_BIN/layered_paired" ] || cc -O2 -o "$W90_BIN/layered_paired" layered_paired.c -lm
[ -x "$W90_BIN/hybrid_profile" ] || cc -O2 -o "$W90_BIN/hybrid_profile" hybrid_profile.c -lm
[ -x "$W90_BIN/w40_pruned" ]     || cc -O2 -o "$W90_BIN/w40_pruned" ../w40-c21-frontier/pruned.c
LAY=${LAY:-$W90_BIN/layered_paired}; L21=${L21:-$W90_BIN/l21_paired}
{
  for seed in 1 2 3; do echo "L 8 100000 500 $seed"; echo "L 10 100000 300 $seed"; echo "L 12 100000 200 $seed"; echo "L 16 100000 80 $seed"; done
  for w in 1 2 3 4 5; do echo "P 100000000 30 $w"; done
} | xargs -P ${NPROC:-5} -L 1 sh -c '
  if [ "$1" = L ]; then '"$LAY"' $2 $3 $4 $(($3+$5)) > out/fam_$2_n$3_s$5.txt;
  else '"$L21"' $2 $3 $(($2+1000*$4)) | grep "^n=" > out/l21_n$2_w$4.txt; fi' _
echo done > out/FOLLOWUP_DONE
