#!/bin/zsh
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w11-strips
tr '\t' '|' < $1 | xargs -P 12 -I{} sh -c 'IFS="|" read n k N s w reps <<EOF2
{}
EOF2
f=out/${n}_${k}_${N}_${s}.txt; [ -s $f ] || { ./strips $N $reps $s "$w" > $f.tmp && mv $f.tmp $f; }'
