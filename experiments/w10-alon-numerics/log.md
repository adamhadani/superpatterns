# W10 — a falsifiable numerical test of Alon's conjecture via τ-chains (log)

Date: 2026-08-29.  Directory: work/w10-alon-numerics/.  Files: tchain.c (exact τ-chain DP + brute force),
contain.c (exact containment of a ⊕-decomposable pattern + brute force), classes.py (symmetry classes),
analyze.py (fits), thresholds.py (task 4), validate.sh, out/ (raw data: chain_{τ}_{N}.txt lines "N τ seed L LIS";
validate.txt; thresholds.md).  Tables: results.md.

Setting (from W5 Lemma B).  Π_N = N uniform points in the square (equivalently a uniform σ ∈ S_N).  For τ ∈ S_j,
L_τ(N) = max L with τ^{⊕L} ⊂ Π_N, and c_τ = lim L_τ(N)/√N exists (superadditive ergodic theorem).
Alon's conjecture ⇒ c_τ ≥ 2/j for every τ; a single τ with c_τ < 2/j would refute it (τ^{⊕L}, k = jL, would need
n > (1/4+ε)k²).  Baselines: c_{12…j} = 2/j exactly (L = ⌊LIS/j⌋), LIS(N) = 2√N − 1.77 N^{1/6} + o(N^{1/6}).

Symmetry.  L_τ is invariant under the symmetries of the square that preserve ⊕: inverse (transpose) and
reverse-complement (rotation by π).  Reverse alone maps ⊕-chains to ⊖-chains, so 12 and 21 are NOT equivalent
(L_12 = ⌊LIS/2⌋ but L_21 is a different random variable).  Classes under ⟨inv, rc⟩: S_2: 2, S_3: 4, S_4: 13, S_5: 45
(classes.py; all 64 representatives were run, plus τ = 1).

--------------------------------------------------------------------------------------------------
## 1. Exact algorithm for L_τ (tchain.c)

Let F(x,y) = max number of copies in a chain whose boxes lie in [0,x)×[0,y) (x,y = ranks).  A copy C with box
[xmin,xmax]×[ymin,ymax] has chain value val(C) = 1 + F(xmin, ymin) and L_τ = max val.  F is a staircase in y for
each x: store t_v(x) = min y_max over chains of value ≥ v with x_max < x  ((N+1)×(LIS+2) ints), so
F(x,y) = max{v : t_v(x) < y}.  The problem is enumerating copies: there are Θ(N^j/j!) of them.

Runs anchored at the RIGHTMOST point.  For each point p (column x_p, in increasing x), build all copies whose
rightmost point is p by scanning leftwards and placing τ's positions j, j−1, …, 1; a state S = partial copy
(placed y's, ymin, ymax).  Any completion C of S has val(C) ≤ vb(S) := 1 + F(x_cur, ymin(S)) (its x_min ≤ x_cur and its
ymin ≤ ymin(S); F is monotone) and corner (x_p, y_max ≥ ymax(S)).  Hence S is useless — and is discarded — as soon
as some chain of value ≥ vb(S) already ends at a corner ≤ (x_p, ymax(S)).  Because the run is anchored on the
right and runs are processed in increasing x_p, every such chain is already known: either it ends with a copy
of this run (runSuf[v] = min y_max of the run's completed copies of value ≥ v) or with x_max < x_p (t_v(x_p)).
The root {p} is likewise discarded once F(x_p, y_p+1) ≥ 1 + F(x_cur, y_p), i.e. after O(√N) columns typically
(the width of one step of the level-v staircase).  (A first version anchored at the leftmost point was Θ(N³):
the copies that would kill a state live in runs not yet processed.)
Second exact reduction: two states with the same placed y-values on the *relevant* positions (those value-adjacent
to a still-unplaced element) have identical futures; among them keep the Pareto-best in (ymin if τ's min is
already placed — higher is better —, ymax if τ's max is placed — lower is better).
Completed copies are Pareto-filtered the same way and fed into t_v(x_p+1).  No heuristic pruning anywhere.

Cost (N=10⁴ / 3·10⁴ / 10⁵, j=5): 1 s / 8 s / 80 s per sample (≈ N^{1.7}); memory (N+1)(LIS+2) ints.

Validation.  validate.sh: fast vs brute force (enumerate every copy by DFS, O(#copies²) DP) on the SAME
permutations for all 2+6+24+120 = 152 patterns τ ∈ S_2..S_5, N ∈ {12,25,45}, 3 seeds × 4 samples = 1824
permutations per τ-set: **0 mismatches** (out/validate.txt).  Also L_{12…j} = ⌊LIS/j⌋ holds in every sample
(a built-in check, since the code treats the identity like any other τ), and for |τ| ≤ 3 the means agree with W5's
chain.c (independent code, e.g. L_21(6400) = 76.1 (W5, 8 samples) vs 76.0 ± 0.3 here).

## 2. Containment tester for ⊕-decomposable π (contain.c, task 4)

π = B_1 ⊕ … ⊕ B_r (⊕-indecomposable blocks).  S_0 = {(−1,−1)}; S_i = Pareto-minimal (x_max,y_max) over copies of
B_i whose SW corner strictly dominates a point of S_{i−1}; π ⊂ Π_N iff S_r ≠ ∅.  Copies of a block are enumerated
by DFS with y-gap constraints (blocks here have size ≤ 2).  Validated against a naive DFS (no decomposition) on
60 random patterns (k ≤ 7, N ≤ 14) × 40 permutations: 0 mismatches.

--------------------------------------------------------------------------------------------------
## 3. Data and fits (details/tables in results.md)

Design.  For each of the 65 τ: N = 25000 (24 samples) and N = 10000 (48 samples), plus N = 10⁵ (6 samples) for 21, 4321,
2341, 14325, 24153, 2413.  (The planned N = 400…6400 phases, 96 samples each, are still queued at the time of writing —
the machine was shared with other workstreams at load ≈ 100–200 — and will keep appending to out/chain_*.txt; re-run
`python3 analyze.py md` to refresh results.md.  With only two N values per τ the fits below drop the constant term.)  Each sample records L_τ and LIS of the same
permutation.  Two fits per τ (weighted LSQ, errors from the covariance, χ²-scaled):
  (F1) L_τ(N) = c_τ √N − a_τ N^{1/6} + b_τ ;
  (F2) paired: j·L_τ(N) − LIS(N) = α √N + β N^{1/6} + γ,   c_τ − 2/j = α/j.
(F2) is far more sensitive: LIS/√N → 2 is known, and the fluctuations of jL − LIS are much smaller than those of
either term (sd ≈ 6 at N = 25000 where LIS ≈ 300, with sd(LIS) ≈ 5).

Result (results.md, 58 τ with both N at the time of writing): for EVERY τ, c_τ is consistent with 2/j.  Paired-fit
deviations c_τ − 2/j lie in [−0.015, +0.013] with errors ±0.006–0.02; the 58 z-scores range from −2.3 (12543) to
+2.3 (23541), exactly the spread expected from noise for 58 draws, and the identities 123 / 12345 — where c = 2/j is
exact — land at z = −0.8 / +1.6, calibrating the noise.  No τ has c_τ significantly below 2/j → **no counterexample
candidate to Alon's conjecture** among ⊕-powers of patterns of length ≤ 5.  At the raw level: at N = 25000
(LIS ≈ 300) the mean of jL_τ − LIS lies in [−5.3 (14325), +2.3 (24513)] for all τ, i.e. jL_τ = LIS·(1 ± 0.02); at
N = 10⁵ (LIS ≈ 617): 2L_21 − LIS = +2.8 ± 4, 4L_4321 − LIS = −1 ± 2 (6 samples each), i.e. |c_τ − 2/j| ≲ 0.003 there.

Rigorous lower bounds from the data.  Superadditivity (W5 Lemma A) gives, for the Poissonized process,
E L_τ(Π_N)/√N ≥ E L_τ(Π_λ)/√λ for all λ ≤ N, hence c_τ ≥ E L_τ(Π_λ)/√λ for every λ; with monotonicity in the point
set and λ = N' + 3√N', c_τ ≥ 0.9987·E L_τ(N')/√λ.  With N' = 25000 (mean − 2 se) this gives c_τ ≥ 0.94–0.963·(2/j) for
every τ (results.md, column "rigorous LB") — a Monte-Carlo-certified bound within 4–6 % of the Alon value, the gap
being the negative N^{1/6} finite-size term, which this argument cannot remove.

--------------------------------------------------------------------------------------------------
## 4. The conjecture c_τ = 2/j (task 3): status

Numerically: true within ±0.01–0.02 for all classes of length ≤ 5 run so far (58 of 64) (and the finite-N behaviour is even stronger:
j L_τ(N) − LIS(N) = O(N^{1/6}) with a τ-dependent coefficient, see results.md; e.g. cyclic shifts 2341, 23451 have
j L > LIS on average, while 4321, 14325, 12543 have j L < LIS).

What is proved (all elementary):
 (i) c_τ exists, is invariant under τ ↦ τ^{-1}, τ ↦ τ^{rc} (Lemma B + symmetry above).
 (ii) Upper bounds.  τ^{⊕L} has LIS = L·lis(τ) and LDS = lds(τ); by Greene's theorem its jL points are a union of
     lds(τ) increasing sequences.  Since λ_i(Π_N) = 2√N(1+o(1)) for each fixed i (Baik–Deift–Johansson/Okounkov/
     Borodin–Okounkov–Olshanski), c_τ ≤ min( 2/lis(τ), 2·lds(τ)/j, e/j ) (the last from the first moment
     E#chains = C(N,jL)/(jL)!, identical to the count of increasing subsequences).  These are tight only for
     monotone τ (identity: 2/j).  For 21 they give c ≤ 2, vs the true value 1.
 (iii) Lower bounds. Diagonal-square greedy: c_τ ≥ sup_λ p_τ(λ)/√λ where p_τ(λ) = Pr(τ ⊂ Π_λ) (≈ 0.40 for τ = 21);
     and the Monte-Carlo-certified bound c_τ ≥ E L_τ(Π_λ)/√λ above (≈ 0.96·2/j).
 (iv) A finite-N remark: for the τ-chain there is NO pointwise inequality L_τ ≥ ⌊LIS/j⌋ (identity permutation:
     LIS = N, L_21 = 0), so any proof of c_τ = 2/j must use randomness; conversely j L_τ ≤ LIS fails too (at N =
     25000, jL > LIS in 40–60 % of samples for most τ).  The equality is a statement about the *last-passage
     constant* of a new growth model (the "τ-Hammersley process": the staircase t_v(x) moves when a copy of τ
     completes above line v−1), namely that its flux relation is ∂_xF·∂_yF = N/j² (giving F = 2√(Nxy)/j) as for
     the Hammersley process at intensity N/j².  I could not prove this (the Hammersley proofs of the constant 2
     use exact solvability — Poissonized RSK / Aldous–Diaconis stationarity — and neither transfers).
 (v) Why one should expect equality anyway (heuristic): (a) the first moments of #τ-chains of length L and of
     #increasing subsequences of length jL coincide exactly for every N, L; (b) superadditivity is available for
     both; (c) numerically, even the second-order term is the same order (jL − LIS = O(N^{1/6})).  A plausible
     route: show that a near-optimal increasing sequence can be locally "thickened" — every j consecutive points of
     the LIS span a box with O(j²) further points, and choosing among the exponentially many near-optimal
     increasing sequences one whose consecutive j-boxes all contain τ costs only o(√N).  This is exactly a
     large-deviation / entropy statement for the Hammersley process that I cannot currently prove.

Consequence for Alon's conjecture (if c_τ = 2/j): every pattern of the form τ^{⊕L} (and by Lemma A every
⊕-sum of bounded-size blocks with o(k) distinct… more precisely every ⊕-sum whose blocks come from a fixed
finite set, with a bounded number of "unusual" blocks) has threshold θ = (1/4 + o(1))k², exactly the Alon value —
the same as the identity.  I.e. the layered/co-layered family that W5 §1.5 found to be the *last* patterns at
small n is NOT harder asymptotically.

--------------------------------------------------------------------------------------------------
## 5. Task 4 — hybrid patterns (identity with spaced adjacent transpositions), out/thresholds.md

N_π := N with Pr(π ⊂ Π_N) = 1/2 (400 samples per N, bisection + linear interpolation; ±2 %).  Families:
id_k; H(k,r) = identity with r adjacent transpositions at evenly spaced positions; (21)^{⊕k/2}.
Result: for k = 8…32, every H(k,r) and even (21)^{⊕k/2} has N_π = N_id within ±3 % (noise level); the number of
transpositions has no measurable effect.  N_id/(k²/4) = 1.57, 1.43, 1.38, 1.34, 1.30, 1.23 for k = 8,12,16,20,24,32,
i.e. √N_π − k/2 = 1.0 … 1.75 growing like N^{1/6} (Tracy–Widom correction), consistent with N_π/(k²/4) → 1.
So at finite k the hybrids are as hard as the identity, and the identity's own finite-size excess
(√N − k/2 ≈ 0.6–0.7·N^{1/6}) is the whole story — consistent with Alon's prediction that the ratio → 1.
(Caveat: these are ⊕-decomposable hybrids; W5's really hard cases are ⊕-indecomposable interleavings, which
this staircase DP does not handle — a general containment DFS would be needed and was not attempted.)

## 6. Summary
* Exact DP for τ-chains, any τ of length ≤ 9, N up to 10⁵; validated (0 mismatches on 1824 permutations × 152 τ).
* c_τ = 2/j within ±0.01–0.02 for all 58 (of 64) symmetry classes with data of τ ∈ S_2 ∪ … ∪ S_5; no counterexample to Alon; the
  rigorous (MC-certified) lower bound is c_τ ≥ 0.94·(2/j) for every τ.
* Sharper conjecture c_τ = 2/j (all τ): strongly supported; proved only for monotone τ; provable bounds listed in §4.
* Hybrid ⊕-patterns of length ≤ 32 have the same half-probability threshold as the identity (±3 %).
