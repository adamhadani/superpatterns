#!/bin/zsh
# usage: run_smc.sh k nmax pop seed outdir
k=$1; nmax=$2; pop=$3; seed=$4; out=$5; mkdir -p $out
while read p w; do [ -s $out/$p.txt ] || ./avoid2 smc $p $nmax $pop $seed > $out/$p.txt; done < classes$k.txt
