# W38 — results: pattern-averaged second moment, plain vs leftmost-canonical

All commands reproducible; seeds fixed. Tools: `exact.c`, `exact_can.c` (per-σ exhaustive enumeration of
all C(N,k) k-subsets bucketed by pattern code — exact Σ_π M_π², Σ_π Y_π² per σ; MC over σ only),
`pairs.c`, `pairs_can.c` (stratified MC over pairs with |A∩B| = j, exact hypergeometric weights),
`relaxed.py`, `rate.py` (heuristic §3 of proof.md). Grids: `./run_grid.sh`, `./run_grid_can2.sh`;
summaries: `python3 summarize.py`, `python3 summarize2.py` (outputs in `out/`).
R_avg := E_π E[M_π²]/μ² = k!·p_coll (Theorem 1); R_can := E_π E[Y_π²]/(E_π E Y_π)² (Theorem 2,
leftmost-canonical copies). Bounds: E_π Pr(π ⊆ σ_N) ≥ 1/R_avg and ≥ 1/R_can.

## 1. PLAIN second moment: fails for C < ≈1/2 — R_avg = e^{Θ(k)} at C ≤ 0.3

ln R_avg (stratified MC, 2·10^6 samples/overlap; exhaustive-enumeration check in brackets, MC over
50–4000 σ; ± = 1 SE relative):

| k  | C=0.15 | C=0.2 | C=0.25 | C=0.3 | C=0.5 | C=1 |
|----|--------|-------|--------|-------|-------|-----|
| 4  | —      | —     | 3.18 [3.18] | 2.15 [2.15] | 1.01 [1.00] | 0.36 [0.36] |
| 5  | —      | 4.79 [4.79] | 3.51 [3.51] | 2.22 [2.21] | 1.17 [1.18] | 0.41 [0.40] |
| 6  | —      | 5.08 [5.08] | 3.45 [3.46] | 2.54 [2.55] | 1.19 [1.19] | 0.43 [0.44] |
| 7  | 8.53 [8.53] | 4.92 [4.91] | 3.76 [3.76] | 2.69 [2.68] | 1.32 [1.31] | 0.46 |
| 8  | 7.52 [7.52] | 5.20 [5.18] | 3.85 [3.86] | 2.98 [3.00] | 1.40 [1.33] | 0.46 |
| 9  | 8.39 [8.40] | 5.66 [5.68] | 4.13 [4.13] | 3.16 [3.16] | 1.56 | 0.33±0.14 |
| 10 | 8.59 [8.59] | 5.83 [5.85] | 4.32 [4.26] | 3.14±0.08 [3.22] | 1.18±0.25 | 0.70±0.45 |

Readings. (i) At C = 0.2, 0.25, 0.3 the growth of ln R_avg over k = 7..10 is ≈ 0.30, 0.17, 0.16 per unit
k — R_avg = e^{Θ(k)}: **the plain averaged second moment fails at C = 1/4** (and 0.3). At C = 0.5 the
slope is ≈ 0.04±0.03 (marginal, consistent with the heuristic rate 0 at C = 1/2); at C = 1 flat (→
heuristic limit ln R = 2.08). (ii) Overlap decomposition (out/pairs_k*_C*.txt): at C = 0.25 the sum is
dominated by j/k ≈ 0.6–0.7 at k = 8–10 (e.g. k=10: term_7 = 20.4 of R = 74.8); the j=0 term is exactly
P(J=0) (Theorem 1b), the j = O(1) terms are O(1). (iii) Heuristic rate function (proof.md §3, rate.py):
max_θ r(θ) = 0.389 / 0.237 / 0.141 / 0.079 / 0.000 at C = 0.15 / 0.2 / 0.25 / 0.3 / 0.5;
**C₂(plain, heuristic) = 0.4998 ≈ 1/2**, dominant θ*(0.25) = 0.62. Finite-k agreement is loose
(relaxed.py at k=10, C=0.25 gives 8.3 vs measured 4.3 — e^{O(1)} offsets are visible; the SLOPE in k is
what matches: 0.17 measured vs 0.14 asymptotic). (iv) Sanity: 1/R_avg ≤ E_π Pr(π⊆σ) holds in every cell,
e.g. k=10, C=0.25: 1/R_avg = 0.013 ≤ measured E_π Pr = 0.049 (from E#distinct/k!, exact run).

## 2. CANONICAL second moment: R_can = 1/E[Y_π] + D with D bounded — works down to C ≈ 0.2

Leftmost-canonical copies Y_π (W12 rule; Theorem 2 + Lemma 3 of proof.md). Exact enumeration only
(pairs_can MC has fatal zero-hit bias at C ≥ 0.5 for the small-j terms — do not use it; its C ≤ 0.3
totals agree with exact within 2 SE). D := off-diagonal part = R_can − k!E[ΣY]/(EΣY)² (the diagonal is
1/E Y_π → 0 whenever E Y_π = e^{Θ(k)} → ∞, i.e. all C > 0.1925).

TABLE-CANONICAL (filled by summarize2.py)

Readings: TBD.

## 3. Small-j analytics check

Theorem 1b: p_0 = 1/k! exact (proved). Continuum-limit claim (proof.md §3): for j = 1, N ≫ k²:
k!·p_1 → π/4 ≈ 0.785 (collision of two binomial rank pairs, E[(u(1−u))^{−1/2}]² /(4π)).
Test at k=8, C=5 (N=320, 2·10^7 samples/j): k!p_1 = TBD.
Large j: term_{k−1}/term_k = Q_{k−1} = 4Ck(1+O(1/k)) (size-biased cells): measured k=10, C=0.25:
Q_9 = μ·term_9 = 0.90·6.04 = 5.4 vs 4Ck·(N−k)/N·(k/(k+1))² ≈ 5.0 ✓.

## 4. Quenched vs annealed (where the average is made)

k=8, C=0.25 (N=16, 4000 σ, exact): plain E[M_π²]/μ² = 23.4 / 39.0 / 50.6 / 58.4 / 60.5 for 5 fixed
random π and 81.8 for the identity, vs annealed R_avg = 47.5: factor-3.5 spread, identity worst — the
average has a substantial hard-π component (cf. W28: no hard core but factor ≤ 4 spread of p_π).
k=9, C=0.25 (N=20): plain 27.2–48.9 random, identity 123.5.
CANONICAL k=8, C=0.25: E[Y_π²]/(E Y_π)² = 20.6 / 21.3 / 21.6 / 21.8 / 24.2 (random), 21.4 (identity);
E Y_π = 0.054–0.062 (pattern-independence of E Y_π, exact in the Poisson model per W12, holds to ≈10%
here at N=16): **the canonical ratio is nearly pattern-uniform** — restricting to canonical copies
removes not only the e^{Θ(k)} growth but also the π-dispersion of the second moment. (Most of 21.4 is
the diagonal 1/E Y_π ≈ 17; off-diagonal ≈ 4.)

## 5. Comparison with W21 and the constants

W21: random-π half-probability threshold n_½/k² = .347, .323, .307, .295, .286, .278 at k = 12..32,
fits → 0.20–0.23; identity → 1/4 (from above, .30 at k=40). Our C = 0.25 column sits below every finite-k
threshold (so E_π Pr < 1/2 throughout is expected — measured 0.049 at k=10) and the canonical-copy
first-moment threshold is 0.1925 (W12). The W38 canonical evidence (R_can bounded for C ≥ ≈0.2–0.25,
TBD) is consistent with the true random-π constant lying in [0.1925, 0.23] and with W21's extrapolation.
