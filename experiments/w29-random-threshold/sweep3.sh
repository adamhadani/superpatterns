#!/bin/zsh
run() { h=$1; ns=$2; for mode in 0 1; do for beta in 0.5 0.6 0.7 0.8; do for w in 1.5 2 2.5 3; do ./strip $h $w $beta $mode $beta $ns 23; done; done; done; }
( run 64 10000 ) > sweep3_a.out 2>&1 &
( run 256 1500 ) > sweep3_b.out 2>&1 &
( run 1024 150 ) > sweep3_c.out 2>&1 &
wait
