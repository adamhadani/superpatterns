#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w10-alon-numerics
for t in 21 4321 2341 14325 24153 2413; do for s in 1 2 3 4 5 6; do echo "100000 1 $t $((900000+s))"; done; done | nice -n 5 xargs -P 4 -L 1 sh -c './tchain $0 $1 $2 $3 >> out/chain_$2_$0.txt'
echo DONE > out/big.done
