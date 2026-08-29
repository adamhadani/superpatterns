#!/bin/zsh
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w11-strips
P=${2:-4}
cat $1 | xargs -P $P -I{} zsh -c 'IFS=$'"'"'\t'"'"' read name cmd <<< "{}"; f=out2/$name.txt; [ -s $f ] || { eval "$cmd" > $f.tmp 2>/dev/null && mv $f.tmp $f; }'
