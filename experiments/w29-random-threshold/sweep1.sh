#!/bin/zsh
# coarse sweep at h=16,64: modes 0,1,2; beta in {0.6,0.8,0.9,1}; w in {0.5,1,2,4}
for h in 16 64; do for beta in 0.6 0.8 0.9 1.0; do
  ./strip $h 100 $beta 2 $beta 20000 7
  for mode in 0 1; do for w in 0.5 1 2 4; do ./strip $h $w $beta $mode $beta 20000 7; done; done
done; done
