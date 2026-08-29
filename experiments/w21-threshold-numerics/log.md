# W21 threshold numerics — log

## Start
Read w16 proof.md §4, log.md, contain_mrv.c, contain_gen.c.  Machine load at start ≈ 19 (other agents + SAT job);
I will use ≤ 4–6 processes at a time.
Plan: new solver contain_bc.c = contain_mrv + 2D bounds consistency (position chain and rank chain propagate
min/max feasible position/value of every unplaced element to its neighbours, iterated to a fixpoint; O(k log n)
per pass via the dominance-count table), same cell-count prune, MRV branching.  Validate vs contain_gen (k ≤ 12)
and vs an LIS oracle for the identity; then thresholds for k = 20, 24, 28, 32.

## contain_bc.c written and validated
- 2-D bounds consistency (position chain + rank chain, binary searches on the dominance table) + cell-count prune
  + per-cell LIS/LDS prune (points of a gap cell must have LIS ≥ LIS(sub-pattern in the cell), same for LDS).
- validate.py: 56 000 per-sample comparisons vs contain_gen (k = 6..12, random π + identity, n around threshold):
  0 mismatches.  validate_lis.py: identity vs LIS oracle (lis_v.c, same RNG stream), 300 samples each at
  (k,n) = (20,135),(24,190),(28,255),(32,330): 0 mismatches.
- Speed (1 core, loaded machine): k=20 n=135: contain_mrv 85 s / 40 samples (id+1 rand); contain_bc 0.02 s.
  Identity is now trivial (LIS prune fires at the root).  Random π: k=24 n=185 ≈ 2 ms/sample; k=28 n=225 ≈ 12 ms;
  k=32 n=300 ≈ 50–90 ms/sample per pattern.  Before the LIS prune the identity cost 8 s/sample at k=28 (52 M nodes).
- Bug found and fixed while developing: the first version of the LIS prune applied it to singleton cells only
  (rep[] recorded the last element of the cell instead of the first); the bug was conservative (never wrong,
  only useless) and node counts exposed it.
- Patterns: pats.py; random.seed(100+k) then 8 shuffles — the first 4 coincide with W16's rand0..3.

## Sweeps launched (sweep.py, 2000 samples per point, seed 1000+n, all patterns on the same samples)
k=20: n = 100..165 step 5;  k=24: n = 145..215 step 5.

## Results so far (logistic fits, fit.py; details in results.md)
k=20: id 132.7 (LIS 1e5: 132.9), rand mean 122.8 (8 π, sd 1.4)  ratio .925
k=24: id 186.4 (LIS 186.2),      rand mean 169.7 (sd 0.6)        ratio .911
k=28: id 248.1 (LIS 248.0),      rand mean 224.2 (sd 1.4)        ratio .904
Identity LIS thresholds k=8..48 (lis_thr.out).  Calibration: free-constant fits to the EXACT identity series
give an implied limit 0.255–0.258 (forms A, C) or 0.274 (form B) instead of 1/4 — the fits are biased upward
by 2–10 % at k ≤ 48, so an "implied limit" for random π must be read with the same bias in mind.
(n_rand − k²/4)/k = 1.14, 1.07, 1.01 at k = 20, 24, 28: decreasing linearly, as c < 1/4 predicts.
Structured, k=25: tilted 5×5 grid n_half ≈ random π (slightly below), identity = decreasing (as it must).
Launched k=36 (4 random π, 1000 samples); k=40 to follow (≈1.5 s/sample near threshold).
