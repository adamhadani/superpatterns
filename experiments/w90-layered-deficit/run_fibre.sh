#!/bin/sh
# Stage-by-stage evaluation of the exact fibre formula (fibre_cost.py), n = 10^4, first 63 flips.
cd "$(dirname "$0")"
for s in 1 2 3 4 5 6; do python3 fibre_cost.py mc 10000 20000 $((500+s)) 64 60 > out/fibre_n10000_I64_s$s.txt & done; wait
echo done > out/FIBRE_DONE
