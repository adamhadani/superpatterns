#!/bin/sh
# W91: brute-force checks of the deterministic lemmas (about 3 minutes on 5 cores). Output: out/gadget_checks.txt
cd "$(dirname "$0")"; mkdir -p out
python3 gadget_check.py tie            > out/chk_tie.txt &
python3 gadget_check.py dp 8 300 11    > out/chk_dp.txt &
python3 gadget_check.py canon 40 400 12 > out/chk_canon.txt &
python3 gadget_check.py plant 14 3000 13 > out/chk_plant14.txt &
python3 gadget_check.py plant 24 1500 14 > out/chk_plant24.txt &
wait
python3 gadget_check.py plant 36 500 15 > out/chk_plant36.txt &
python3 gadget_check.py plant 48 150 16 > out/chk_plant48.txt &
python3 gadget_check.py mecke 4 40000 17 > out/chk_mecke4.txt &
python3 gadget_check.py mecke 6 12000 18 > out/chk_mecke6.txt &
wait
cat out/chk_tie.txt out/chk_dp.txt out/chk_canon.txt out/chk_plant14.txt out/chk_plant24.txt out/chk_plant36.txt \
    out/chk_plant48.txt out/chk_mecke4.txt out/chk_mecke6.txt > out/gadget_checks.txt
touch out/CHECKS_DONE
