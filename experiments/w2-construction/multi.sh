#!/bin/bash
# usage: multi.sh k n m iters nseeds tag
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w2-construction
k=$1; n=$2; m=$3; it=$4; ns=$5; tag=$6
out=runs/multi_$tag.txt; : > $out
for s in $(seq 1 $ns); do
  r=$(./sa2 $k $n $m $it $((s+1000)) 2>/dev/null)
  mask=$(echo "$r" | sed 's/.*dirmask=\([0-9]*\).*/\1/'); word=$(echo "$r" | sed 's/.*: //')
  p=$(./polish $k $n $m $mask $word | tail -1)
  echo "seed $s: SA $r | polish $p" >> $out
done
echo done >> $out
