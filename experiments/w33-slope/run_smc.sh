#!/bin/bash
# usage: run_smc.sh classfile nmax pop seeds outdir
cf=$1; nmax=$2; pop=$3; seeds=$4; od=$5; mkdir -p $od
while read pat mult; do
  for s in $(seq 1 $seeds); do
    [ -s $od/${pat}_s$s.txt ] || ./avoid2 smc $pat $nmax $pop $s > $od/${pat}_s$s.txt
  done
done < $cf
