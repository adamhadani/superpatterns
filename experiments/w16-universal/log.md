# W16 — universal absence constant κ: log (2026-08-29, continued after the rate-limit kill)

Inherited from the first W16 agent (do not redo): thresholds.out/json (contain_gen, k = 8..16), scan2d_80.out
(potential x+λy for the identity: best κ = 2.2757 at λ = 1, vs 2.2787 — no gain), pairs.py (written, never run:
it imported scipy, which is not installed; the import was unused and is removed), contain_gen.c, exact_all.c.

## 13:20  Reading + first checks
* contain_gen.c has MAXK = 16: its k = 20 output is garbage (pi[] overflow); the k ≤ 16 rows of thresholds.out are fine.
  Wrote contain_mrv.c (CSP search: most-constrained pattern element first + per-cell counting prune); agrees with
  contain_gen on k = 8 (300 common samples, identical fractions) and is the only one valid for k > 16.
* The half-probability thresholds are in `thresholds.out`; note that random patterns are contained MORE easily than
  the identity at every k ≤ 16 (n_half 3–6 % lower), i.e. at finite k the identity is the HARDEST pattern, not the
  easiest.  The W16 question "is κ = 2 universal" is therefore whether n_rand/n_id → 1 (both → k²/4) or whether random
  patterns have an asymptotic constant strictly below 1/4 (then κ_univ > 2 and c_τ ≤ 2/|τ| cannot come from a
  universal bound).

## 13:25  Level-2 conditions of lex-minimality — theory (details in proof.md §2)
Lex-min ⇒ for every r, no copy P' with p'_i = p_i (i < r) and x'_r < x_r.  Two-point moves (p_r → q, p_j → q') add
something beyond the strips only when p_j is a RANK neighbour of p_r (π(j) = π(r) ± 1); then, with r < j:
   no q in cell (col r, band m+1) with q' in cell (col j+1, band m+1) above q         [m = π(r), π(j) = m+1]
   (+ if j = r+1: no increasing pair inside cell (col r, band m+1)),
and mirror for π(j) = m−1.  Factor for the two-cell part: F(a,b) = e^{−a−b}(a e^a − b e^b)/(a−b), a = g_r h_{m+1},
b = g_{j+1} h_{m+1}; same-cell part: e^{−μ} I₀(2√μ).  CONSEQUENCE for a universal bound: the two-cell part couples
column r with column j+1 = π^{-1}(π(r)+1)+1, i.e. positions that are far apart for a generic π (rank-adjacency and
position-adjacency are two unrelated Hamiltonian paths on the k points).  After the W12 relabelling the h-chain is
no longer Markov; the transfer-operator method only sees the same-cell part, which exists only at positions r with
π(r+1) = π(r) ± 1 (≈ 2 positions for a random π, k−1 for the identity/decreasing).  So level 2 gives NO universal
gain in the transfer framework (sup over π of the bound is still 2.279, e.g. for any π without ±1 adjacencies).
* Ran pairs.py (n = 40, coarse) and pairs2.py (same-grid comparison, n = 80 / 40):
  identity: level 1 2.2816 → level 2 (same-cell part only) 2.2435 (n = 80; continuum ≈ 2.279 → ≈ 2.240);
  decreasing: level 1 2.2912 → level 2 (two-cell part only) 2.2617 (n = 40).  Gain ≈ 0.03–0.04 per level: the
  lex-min hierarchy converges to the truth (κ = 2 for the identity) slowly.  Not certified (no CW certificate).

## 13:30  Route (b): mixed leftmost/lowest rules
"Both strips empty" copies need not exist (k = 1: two points (0.1,0.9),(0.9,0.1)).  What does exist: for any split
[k] = L ⊔ D, the copy minimising Σ_{r∈L} x_r + Σ_{r∈D} y_r has the x-strip of every r ∈ L and the y-strip of every
r ∈ D empty (proof.md Prop. 1).  For the identity with L = odd, D = even (regions disjoint) the transfer computation
(mixedLD.py, 2-step kernel on pairs) gives κ = 2.347 vs 2.291 for all-leftmost on the same grid: WORSE.  The all-left
rule is the balanced one (every column meets two bands); unbalancing (three bands / one band) loses.  Dead.
* Potential x+λy (first agent): 2.2757 for the identity, and for general π the regions of neighbouring r overlap
  (col r+1 when π(r+1) = π(r)−1), so even this 0.003 is not available universally.  Dead.

## 13:35  Route (c) dead — and why random π is structurally different from the identity
RSK/Greene only bites for near-monotone π.  Coarse-graining the square into m² cells of side δ/√N: a copy of the
identity occupies a monotone path of ≈ m cells with ≈ 2δ points each; a copy of a random π at k ≈ 2√N puts ≈ 1 point
in each of ≈ k cells spread over the whole square (cell (a,b) receives the positions in block a whose ranks lie in
block b: ≈ (2δ)²/k ≪ 1 points).  So for random π the copies are spread out, and the clustering of copies that makes
Pr(π ⊂ Π_N) ≪ E#copies comes only from (i) single-point moves (the strips — identical for all π, W12 Prop. 3) and
(ii) moves of subsets connected in the union of the rank-path and the position-path.  For the identity the two paths
coincide (intervals can be re-routed: path entropy e^{Θ(k)}, closing the gap from 2.279 to 2); for random π the
level-2 pairs still give a per-point gain (every rank-adjacent pair has a two-cell condition), so the truth for random
π is strictly below 2.279 — whether it is 2 is exactly the open question.

## 13:40  Numerics: E#leftmost-canonical vs thresholds (E_lc.py)
E_k(N) = N^k/(k!)² · E exp(−N Σ g'_m (h_{m−1}+h_m)) by Monte Carlo (pattern-independent).  N with E_k = 1:
k = 8: 23.5, 10: 33.5, 12: 45, 14: 58, 16: 73  (N/k² = .367 .335 .313 .296 .285 → .1925 = 1/2.279²).
Half thresholds n/k²: id .405 .373 .360 .345 .341 (→ .25);  rand .384 .362 .348 .334 .321.
rand − E_lc: .017 .027 .036 .038 .036;  id − E_lc: .038 .038 .048 .049 .056.
At the random-π threshold E[#leftmost-canonical | contained] ≈ 2.2 (k=8) … 7 (k=16); identity: 3 … 11.
So both have super-strip clustering growing with k; the random one grows more slowly.  Inconclusive at k ≤ 16.

## 13:50  Lemma 2 / Theorem 3 checked by brute force (check_lemma2.py → check_lemma2.out)
6 patterns (k = 4, 5), N = 8, 10, 1500 Poisson samples each, all copies enumerated, lex-min copy tested against the
strips and conditions (ii)/(iii): 0 violations; E_level2 ≥ Pr(contain) always (e.g. 1234: 0.665 ≥ 0.551;
24513 (sic 2,5,3,1,4): 0.508 ≥ 0.391).
Found and recorded: pairs.py's "decreasing level 2" applied a vacuous two-cell factor (cell (r+1, m−1) is a strip
cell for the decreasing pattern) — its 2.262 is invalid; by the reflection y ↦ 1−y the decreasing pattern's
level-2 bound equals the identity's (2.240).

## 13:55  Level-2 gain for random π vs identity by Monte Carlo (level2_mc.py, level2_big.py → *.out)
Theorem 3's integral with all pairwise-disjoint non-vacuous pair conditions.  E^{(2)}/E_lc, log per point:
k=16 N=86: id −0.040, rand −0.032…−0.037; k=20 N=115: id −0.033, rand −0.028…−0.031; k=24 N=150: id −0.030,
rand −0.026…−0.028; k=32 N=250: id −0.028, rand −0.025…−0.026.  Random π gets ≈ 90 % of the identity's level-2
clustering through the NON-LOCAL two-cell conditions (rank-adjacent pairs at distant positions).  Best evidence so
far that the whole lex-min hierarchy behaves alike for all π (κ_univ = 2), but nothing rigorous beyond Theorem 3.

## 14:05  Fit of the thresholds (k = 8..16), n_½ = (k/2 + a k^{1/3})²
k:        8      10     12     14     16
a_id:    .544   .513   .523   .507   .532   (stable ≈ 0.52: the Tracy–Widom form of the LIS threshold, as expected)
a_rand:  .478   .471   .472   .451   .423   (drifting DOWN: the random-π correction is not of order k^{1/3}; it is
          either a lower-order correction to k²/4 — then n_rand/n_id → 1 from below — or the signature of a limit
          below 1/4.  rand/id ratio: .949 .971 .967 .967 .942, no trend.)  k = 20 (contain_mrv, 120 samples) pending in
          thresholds_k20.out; the run is CPU-starved by the machine load (≈ 170) and may finish after this report.

## 14:20  k = 20 thresholds (contain_mrv, 120 samples, n = 120..160, 918 s wall; thresholds_k20.out/json)
id 135.6 (n/k² = .339, a_id = .61 ± .05);  rand 120.8, 121.7, ≈120, 124.3 (mean ≈ 121.7, n/k² = .304, a_rand = .38).
Ratio rand/id = 0.90 — the gap is WIDENING (.95 .97 .97 .97 .94 .90 for k = 8..20), not closing.  E_lc = 1 at N = 106
(.265 k²); rand − E_lc = .039 (was .036–.038 at k = 12–16, stable); id − E_lc = .074 (growing).
Reading: the identity's threshold carries the full Tracy–Widom k^{1/3} correction (a ≈ 0.5–0.6, stable), while the
random patterns sit at a nearly constant offset ≈ 0.04 k² above the strip-bound threshold (which → 0.1925 k²).
If that offset persists, lim n_rand/k² ≈ 0.23 < 1/4, i.e. κ_univ ≈ 2.09 > 2 and the identity is NOT the
asymptotically easiest pattern; if the offset instead grows slowly, both limits can still be 1/4.  120-sample
statistics (±3 % in n_½) cannot separate these; k = 24–32 with ≥ 500 samples would (contain_mrv: ≈ 1 CPU-s per
sample at k = 20, growing ≈ 3× per +4 in k on this loaded machine).
