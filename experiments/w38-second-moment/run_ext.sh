#!/bin/bash
# W38 extension: k=11,12 at C=0.25 (N=30,36), exact_can2.
cd "$(dirname "$0")"
while [ ! -f out/gridcan2.done ]; do sleep 15; done
./exact_can2 11 30 40 11 > out/exactcan_k11_C0.25.txt
echo K11DONE
./exact_can2 12 36 16 11 > out/exactcan_k12_C0.25.txt
echo K12DONE > out/ext.done
