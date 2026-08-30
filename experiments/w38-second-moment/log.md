# W38 log — second moment on copies (plain and leftmost-canonical), averaged over π

2026-08-30
- Tools (C, gcc -O2): exact.c / exact_can.c (per-σ exhaustive enumeration of all k-subsets, bucketed by pattern code;
  exact Σ_π M_π² and Σ_π Y_π² per σ, MC over σ), pairs.c / pairs_can.c (stratified MC over pairs (A,B) with |A∩B| = j,
  hypergeometric weights). relaxed.py: asymptotic "relaxed cell-counting" formula for the plain R_avg.
- Cross-checks: exact vs pairs agree at (k,N) = (5,8), (6,12) within SE for both plain and canonical; canonical term
  j = k−1 is exactly 0 (Lemma: no single-point replacement of a canonical copy is canonical).
- Bug fixed: exact_can 1-based DFS loop bound (was dropping subsets; plain R came out 2.15 instead of 9.2).
- Grids launched: run_grid.sh (plain), run_grid_can.sh (canonical). Outputs in out/.
- rate.py: k→∞ rate of relaxed heuristic: C2_plain = 0.4998 (≈ 1/2?); failure exponent at C=1/4: 0.141 (theta*=0.62).
- exact_can2: added exact overlap decomposition of canonical same-pattern pairs (canonical copies are few; sort by
  pattern code, popcount masks). Confirms Lemma 3 (j=k−1 absent) exactly at every cell inspected.
- pairs_can at C≥0.5 unusable (zero-hit bias for small j: canonical collisions too rare; R_can<1 outputs are that bias);
  canonical numbers below use exact_can2 only. Grid v2 relaunched (run_grid_can2.sh).
- Quenched (k=8, C=0.25, 4000 sigma): plain E[M^2]/mu^2 = 23–82 over 5 random pi + id (id worst, 82);
  canonical EY^2/(EY)^2 = 20.6–24.2 (id 21.4): the canonical ratio is nearly pattern-uniform.
- pairs 8 320 (C=5) launched: continuum-limit check of k!p_1 → pi/4 (§3 small-j analytics).
