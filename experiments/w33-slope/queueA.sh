#!/bin/bash
cd "$(dirname "$0")"
./run_smc.sh ../w27-comparison/classes4.txt 40 3000 2 smc4
./run_smc.sh ../w27-comparison/classes5.txt 40 2000 1 smc5
mkdir -p exact
while read pat mult; do ./avoid2 exact $pat 11 > exact/$pat.txt; done < ../w27-comparison/classes4.txt
while read pat mult; do ./avoid2 exact $pat 10 > exact/$pat.txt; done < ../w27-comparison/classes5.txt
echo DONE > queueA.done
