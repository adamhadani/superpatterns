#!/bin/zsh
# finer sweep; 3 parallel workers (one per h-group)
run() { h=$1; ns=$2; for beta in 0.8 0.85 0.9 0.95 1.0; do ./strip $h 100 $beta 2 $beta $ns 11; for w in 3 4 6 8 12; do ./strip $h $w $beta 1 $beta $ns 11; done; done; }
( run 16 40000; run 128 4000 ) > sweep2_a.out 2>&1 &
( run 32 20000; run 256 1500 ) > sweep2_b.out 2>&1 &
( run 64 10000; run 512 400 ) > sweep2_c.out 2>&1 &
wait
