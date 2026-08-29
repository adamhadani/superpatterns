#!/bin/sh
# usage: run_queue.sh QUEUEFILE ; each line: K N SAMPLES SEED  -> out/k{K}_n{N}_s{SEED}.txt
cd "$(dirname "$0")"
while read k n s seed; do
  [ -z "$k" ] && continue
  f=out/k${k}_n${n}_s${seed}.txt
  [ -f "$f" ] && grep -q '^#' "$f" && continue
  nice -n 5 ./mslack $k $n $s $seed 5000 > $f.tmp && mv $f.tmp $f
  echo "$(date +%H:%M) done $f: $(tail -1 $f)" >> queue.log
done < "$1"
