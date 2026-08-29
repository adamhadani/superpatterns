# W21 — half-probability containment thresholds n_½(π) for k = 20..40 (numerics)

Question: does lim n_½(π)/k² equal 1/4 for random π (as for the identity), or is it strictly below?
See `results.md` (tables + verdict) and `log.md` (chronology).

## Files
- `contain_bc.c` — containment tester (CSP: 2-D bounds consistency + cell-count prune + per-cell LIS/LDS prune,
  MRV branching).  `cc -O3 -march=native -o contain_bc contain_bc.c`.
  Usage: `./contain_bc n samples seed pat1 pat2 ...` (patterns as comma lists, 1-based; k ≤ 64, n < 2048).
  Prints `<pat> <fraction> hits=<h> nodes=<N> sec=<t>` per pattern; all patterns are tested on the same samples.
  `VERBOSE=1` prints one line `S <sample> <pattern-index> <0/1>` per test; `NOLIS=1` disables the LIS/LDS prune.
- `lis.c` / `lis_v.c` — LIS oracle with the identical RNG stream (`./lis n samples seed k1 k2 ...`).
- `contain_gen.c`, `contain_mrv.c` — W16's solvers (copies; contain_gen has VERBOSE patched in) used for validation.
- `validate.py` (contain_bc vs contain_gen, k = 6..12, 56 000 per-sample comparisons) and `validate_lis.py`
  (identity vs LIS oracle at k = 20..32, 1200 samples): 0 mismatches.
- `pats.py` — pattern definitions:
  - identity `ident(k)`, decreasing `dec(k)`;
  - random π: `randpats(k, m)`: `random.seed(100+k)` then m successive `random.shuffle` of 1..k
    (Python 3.14 `random`; the first four coincide with W16's rand0..3 — checked against thresholds_k20.out);
  - layered `(21)^{k/2}`: 2,1,4,3,6,5,...;
  - tilted r×r grid `tilted(r)`: position a·r+b ↦ value b·r+(r−1−a)+1 (LIS = LDS = r);
  - `dechalf(k)`: k,k−1,…,k/2+1 followed by a `random.seed(1000+k)` shuffle of 1..k/2 (LDS ≥ k/2).
- `sweep.py tag k samples n1,n2,... name=pat ...` — runs contain_bc for each n (seed = 1000+n) in parallel
  (`W` workers), writes `tag.json`.  Launchers: `run_k.sh tag k samples ns W [m]` (identity + m random π),
  `run_struct.sh tag k samples ns W` (id, dec, layered, dechalf, tilted if k is a square, r0).
- `fit.py tag.json` — logistic fit p(n) = 1/(1+exp(−(n−m)/w)) by maximum likelihood on the points with
  0.1 < p < 0.9; n_½ = m; 95 % CI by parametric bootstrap (400 resamples).
- `lis_thr.py` → `lis_thr.out/json` — identity thresholds from the LIS, 10^5 samples per point, k = 8..48.
- `analyze.py` — all tables and the k-dependence fits (forms A–D), prints what is in results.md.

## Exact rerun commands used
```
python3 lis_thr.py > lis_thr.out
./run_k.sh k20 20 2000 100,105,...,165 2        # step 5
./run_k.sh k24 24 2000 145,150,...,215 4
./run_k.sh k28 28 2000 195,200,...,265 3
./run_k.sh k32 32 2000 250,256,...,340 3        # step 6
./run_k.sh k36 36 1000 320,328,...,376 2 4      # 4 random π
./run_k.sh k40 40 600  400,412,...,460 3 4
./run_struct.sh s20 20 2000 95,100,...,160 1
./run_struct.sh s24 24 2000 135,140,...,210 1
./run_struct.sh s25 25 2000 150,156,...,222 1
./run_struct.sh s36 36 1000 ... 1
python3 analyze.py > analyze.out
```
