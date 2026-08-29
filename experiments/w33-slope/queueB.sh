#!/bin/bash
cd "$(dirname "$0")"
# S_6: a spread of classes (identity, layered, generic) ; S_7: a few
printf "123456 1\n654321 1\n213456 1\n215436 1\n321654 1\n123654 1\n134256 1\n142536 1\n153624 1\n246135 1\n251364 1\n315264 1\n361425 1\n415263 1\n462513 1\n526314 1\n" > sel6.txt
./run_smc.sh sel6.txt 58 1500 1 smc6
printf "1234567 1\n7654321 1\n1765432 1\n2135476 1\n2461735 1\n3517264 1\n4162735 1\n5274163 1\n" > sel7.txt
./run_smc.sh sel7.txt 78 1000 1 smc7
echo DONE > queueB.done
