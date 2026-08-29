#!/bin/bash
cd /Users/adamhadani/Development/math-proofs/superpatterns/work/w10-alon-numerics
while true; do
  n=$(cat out/chain_*_25000.txt 2>/dev/null | wc -l | tr -d ' ')
  if [ "$n" -ge 1540 ] || ls out/chain_*_10000.txt >/dev/null 2>&1; then break; fi
  sleep 10
done
pkill -f runjobs.sh; pkill -f "xargs -P 12"; sleep 1
# kill only the main-plan tchain processes (not the N=100000 ones)
for p in $(pgrep -f "^./tchain "); do args=$(ps -o args= -p $p); case "$args" in *" 100000 "*) ;; *) kill $p;; esac; done
python3 - <<'PY'
jobs=[]
taus=[l.strip() for l in open('reps.txt')]+['1']
plan=[(10000,48,6),(6400,96,6),(2500,96,4),(1000,96,4),(400,96,4)]
for N,tot,chunks in plan:
    for t in taus:
        per=tot//chunks
        for c in range(chunks): jobs.append(f"{N} {per} {t} {N*7+c+1}")
open('jobs2.txt','w').write('\n'.join(jobs)+'\n')
PY
rm -f out/chain_*_10000.txt out/chain_*_6400.txt out/chain_*_2500.txt out/chain_*_1000.txt out/chain_*_400.txt
cat jobs2.txt | xargs -P 10 -L 1 sh -c './tchain $0 $1 $2 $3 >> out/chain_$2_$0.txt'
echo DONE > out/jobs2.done
