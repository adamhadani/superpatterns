#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w10-alon-numerics
cat jobs.txt | xargs -P 12 -L 1 sh -c './tchain $0 $1 $2 $3 >> out/chain_$2_$0.txt'
echo DONE > out/jobs.done
