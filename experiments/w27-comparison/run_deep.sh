#!/bin/zsh
# targeted deep-tail runs: identity vs 1 ⊕ dec ⊕ 1 vs layered vs grid, larger populations
while pgrep -f "run_smc.sh 5" > /dev/null; do sleep 20; done
for p in 123456 154326 214365 142536; do [ -s deep/$p.txt ] || ./avoid2 smc $p 60 5000 3 > deep/$p.txt; done
for p in 1234567 1654327 1324657 1526374; do [ -s deep/$p.txt ] || ./avoid2 smc $p 74 3000 3 > deep/$p.txt; done
for p in 12345678 16543278 21436587 15263748 13572468; do [ -s deep/$p.txt ] || ./avoid2 smc $p 96 2000 3 > deep/$p.txt; done
