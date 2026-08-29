#!/bin/zsh
# usage: runjobs.sh jobsfile reps [P] — each line "name k N seed word" -> out/name_k_N_seed.txt (line: N k r reps cnt_free cnt_fixed)
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w11-strips
reps=$2; P=${3:-12}
tr '\t' '|' < $1 | xargs -P $P -I{} sh -c 'IFS="|" read n k N s w <<EOF2
{}
EOF2
f=out/${n}_${k}_${N}_${s}.txt; [ -s $f ] || { ./strips $N '"$reps"' $s "$w" > $f.tmp && mv $f.tmp $f; }'
