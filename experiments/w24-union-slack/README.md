# W24 — slack of the union bound for random permutations

Question (W22 review §A item 2): for uniformly random σ_n and M = #{π ∈ S_k : π ⊄ σ_n},
how large is R(n,k) = E[M | M > 0] = E[M] / Pr(M > 0)?  ln R is exactly the (natural-log) factor by which
the union bound Pr(M>0) ≤ E[M] = Σ_π Pr(π ⊄ σ_n) overshoots.

Files
- `mslack.c` — sampler/checker (from w5-random/sp.c). `./mslack K N SAMPLES SEED [DUMPMAX]` prints one line per
  random σ_N: `M c1 c2 ...` (codes of the missing k-patterns, only if M ≤ DUMPMAX), then a `#` summary line.
- `patlib.py` — code ↔ pattern conversion (same mixed-radix code as the C), LIS/LDS/runs/symmetries, naive brute force.
- `selftest.py` + `mslack_stdin.c` — cross-check of the missing *sets* against the naive brute force.
- `run_queue.sh queueX.txt` — runs the grid lines `K N SAMPLES SEED` sequentially into `out/k{K}_n{N}_s{SEED}.txt`.
- `analyze.py [tables|fits|pairs|struct|all]` — all tables in results.md (pools every seed file per (k,n)).
- `results.md` — tables and verdict; `log.md` — chronological log; `queue.log` — run timestamps.

Rerun
```
cc -O3 -march=native -o mslack mslack.c
cc -O3 -o mslack_stdin mslack_stdin.c && python3 selftest.py 6 20 10      # optional self-test
./run_queue.sh queueA.txt & ./run_queue.sh queueB.txt & ./run_queue.sh queueC.txt &   # ~3-4 h, 3 cores
python3 analyze.py all > analysis.txt
```
Add lines to a queue file (or a new file with a different SEED) to get more samples; analyze.py pools all seeds.
