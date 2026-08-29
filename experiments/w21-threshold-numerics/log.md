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

## k = 32, 36 done; k = 12, 16 added (contain_bc, 8 random π each, 4000 samples) for the k-fit
k=32: rand mean 285.0 (sd 0.9) vs id 318.7 → ratio .894;  k=36 (4 π, 1000 samples): 352.9 vs 397.9 → .887.
Ratio series k = 12..36: .959 .936 .924 .911 .904 .894 .887 — monotone, no sign of turning up.
n_rand − k²/4 = 22.8 25.7 28.2 29.0 28.9 (k = 20..36): flat since k = 28.  Forcing c = 1/4 needs a NEGATIVE
k^{4/3} term (e = −0.67); free fits give c = 0.20–0.23 for all forms, while the same forms on the exact identity
series give 0.255–0.274 (true value 1/4) — the bias of the forms is upward, so bias-corrected c_rand is if
anything lower.  Launched k = 40 (4 π, 600 samples, n = 400..460 step 12) and s36 (6×6 tilted grid).
Dead end noted: contain_mrv (W16) is ~100× slower than contain_bc at k=20 and was hopeless at k ≥ 28 for the
identity (52 M nodes/sample) — the LIS/LDS cell prune fixed that (identity now O(1) nodes).

## k = 40 done (4 π, 600 samples, n = 400..460 step 12; ≈ 2000–3300 s wall per n with 3 workers on the loaded machine)
rand mean 427.9 (sd 1.3) vs id(LIS) 485.7 → ratio .881.  n_rand − k²/4 = 27.9: DECREASING now (28.9 at k = 36).
Full series k = 12..40: ratio .959 .936 .924 .911 .904 .894 .887 .881.
Log-log re-analysis (coordinator/W25): slope of log(n/k² − 1/4) vs log k is −0.62 for the identity (LIS,
control; TW predicts −2/3) but −1.4 (k = 12..40) / −1.7 (k = 20..40) for random π, per pattern −1.6…−1.8,
with poor fits; the c that makes the random series TW-like (slope −2/3) is 0.200–0.203 (same estimator gives
0.220 for the identity, so bias-corrected ≈ 0.23).  Results in results.md §3a.
Structured: 6×6 tilted grid at k = 36: 350.4 vs random 351.8 (same); identity 397.9.
s24 (layered (21)^{12} etc.) still running at the time of the k = 40 fit — the layered pattern costs ≈ 0.5 s/sample
at k = 24 (the LIS/LDS prune does not help it: LDS = 2 in every cell); filled in below when done.
Negative/inconclusive: nothing in the data supports a common limit 1/4; the only escape is a correction term
that is positive at k ≤ 40 and negative later (n = k²/4 + d k − e k^{4/3}), which no finite-k experiment excludes.
