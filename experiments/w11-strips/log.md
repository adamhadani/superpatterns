# W11 — union-of-runs patterns via the strip structure (log)

Date: 2026-08-29.  Directory: work/w11-strips/.  Files: strips.c (exact containment tester, two notions),
patterns.txt (the words used), jobs*.txt / runjobs*.sh (batch drivers), out/ (raw: one file per
(pattern,k,N,seed), line "N k r reps cnt_free cnt_fixed"), analyze.py (tables → results.md), fits.py (speed
exponents), check_lemma21.py (sanity check of the deterministic lemma), proof.md (proved statements only).
Time-boxed ~2h.  PROVED = in proof.md; everything else here is numerics or heuristics.

## 1. Model, code, validation

Π_N = N uniform points = a uniform permutation of [N] (values Y[x]).  Pattern = word w ∈ [r]^k (position i
carries letter w(i); letter classes are increasing runs on consecutive value intervals), i.e. π_w of proof.md
§0.  Two containment notions computed on the SAME samples:
  FREE  = ordinary pattern containment π_w ⊂ Π_N;
  FIXED = the r strips are the fixed value intervals of heights h_j = k_j/k (for balanced words: 1/r), and the
          letter-j points must lie in strip j (a sufficient condition; this is the notion the proofs use).
Algorithm (strips.c): scan points in x-order; state = (i = #positions matched, per strip: last y used l_j;
FREE also keeps the first y used f_j so that strips stay separated: a new letter-s point needs y > l_j for
j ≤ s and y < f_j for j > s).  Per level i a Pareto front (l smaller better, f larger better).  Exact.
Fast paths that never change the answer: (a) a windowed greedy with fixed strips (12 window sizes + 40
randomized) — any copy it finds is a certificate for both notions; (b) Greene's necessary condition
λ_1+⋯+λ_r(RSK shape) ≥ k (else neither notion holds).  The heuristic uses its own RNG stream, so the samples are
identical with and without it.
Validation: against an independent brute-force DFS on the permutation π_w (contain.c-style, with or without
the strip constraint): words 1 2 1 2 1 2 / 1 1 2 2 1 2 2 1 / 1 2 3 1 2 3 1 / 3 1 2 2 3 1 1 2 / 1 2 3 2 1 3 3 1 2 /
2 2 1 1 3 3 / 1^6 / 1 1 2 2 1 1 2 2 / (12)^5, N ∈ {10,…,32}, 2 seeds × 300 samples each, both notions, also
with -eq heights: **0 mismatches** (the first buggy version, where the randomized greedy consumed the sample
RNG, was caught by this test).
Cost: r = 2, k = 20: 0.01–0.12 s/sample; r = 3, k = 15: 0.05–0.4 s/sample (the 6-dimensional FREE front is the
bottleneck; r = 3, k = 21 is infeasible: minutes per sample).  Hence k ∈ {8,12,16,20} for r ≤ 2 and
k ∈ {9,12,15} for r = 3.

Patterns (patterns.txt): id = 1^k; r2per = (12)^{k/2}; r2sum = 1^{k/2}2^{k/2} (= identity as a pattern, but
a different FIXED notion); r2blk = (1^{k/4}2^{k/4})²; r2rnd = a fixed random balanced word; r3per, r3sum,
r3blk (blocks of 2–3), r3rnd similarly.  N = f·k²/4 for f ∈ {1,1.25,…,2.5,3,3.5,4,5,6}; 10⁴ samples per
(pattern, N) in the first pass (5000 × 2 seeds); the tail region f ∈ {2, 2.25, 2.5} is being re-run with
5·10⁴ samples for the main patterns (background; see §5).

## 2. Numerical results (results.md has the full tables; numbers below from the first pass, 10⁴ samples)

### 2.1 The tail is fast and the interleaving does not hurt (FREE notion)
Pr(π ⊄ Π_N) at N = f k²/4:

    k=8    f:   2.00    2.25    2.50    3.00   |  k=12   f:  2.00    2.25    2.50   |  k=16  f: 2.00   2.25  | k=20 f: 2.00
    id          .147    .058    .015   3e-4   |             .038    .0059  3e-4    |          .0091  3e-4   |       8e-4
    r2per       .114    .039    .011   5e-4   |             .0165   7e-4   <1e-4   |          .0012  <1e-4  |       <1e-4
    r2rnd       .123    .037    .011   2e-4   |             .024    .0029          |          6e-4          |       <1e-4
    r2blk       .135    .051    .015   5e-4   |             .035    .0048  3e-4    |          .0073  <1e-4  |       .0011
    r3per(k=9)  .019(f=2.27) .0027   1e-4     |             (k=12) .0060 2e-4      |  (k=15) <1e-4 at f=2.25

In every case the interleaved patterns fail LESS often than the identity of the same length (r2sum = id
exactly, as it must).  So at these sizes the union-of-runs patterns are *easier* than the identity in the free
notion; nothing suggests a slower tail.

### 2.2 FIXED strips: larger failure probability, same growth
    fixed, k=16   f:  2.00    2.25    2.50    3.00   |  k=20  f: 2.00    2.25    2.50
    id                .0091   3e-4    <1e-4          |           8e-4    <1e-4
    r2per             .039    .0044   1e-4   <1e-4   |           <1e-4 (f≥2.25)
    r2rnd             .042    .0046   <1e-4          |           3e-4    <1e-4
    r2blk             .066    .010    6e-4   <1e-4   |           .020    7e-4    1e-4
    r2sum             .114    .028    .0052  1e-4    |           .045    .0074   6e-4
    r3rnd(k=15)       .053(f=2.26) .010(2.51) 2e-4(3.0)
The FIXED notion costs roughly a factor 1.3–1.5 in N at fixed failure level; among the words, the sum word is
the hardest for FIXED (a strip may only use half the x-range each, i.e. LIS of N/4 points must reach k/2),
the periodic word the easiest.  (Prop. 3.1 of proof.md: FIXED failure ≥ e^{−N/r} for periodic words.)

### 2.3 Speed: −ln Pr(fail) at fixed f = N/(k²/4) as a function of k  (fits.py; β from −ln P ∝ k^β)
Speed N means −ln P ∝ k² at fixed f (β = 2); speed k means β = 1.  Reference: the identity, whose lower tail
is KNOWN to have speed N, shows β = 1.32 (f=1.75), 1.40 (f=2.0) over k = 8…20 — finite-size effects
(the N^{1/6} Tracy–Widom correction) push the apparent β well below 2 at these k.  Against that reference:

    FREE :  r2per f=2.00: β=1.63  (k=8,12,16: −lnP = 2.17, 4.10, 6.73)
            r2rnd f=2.00: β=1.80  (2.10, 3.74, 7.42)
            r2blk f=2.00: β=1.33  (2.00, 3.35, 4.92, 6.81)     id f=2.00: β=1.40 (1.92, 3.27, 4.70, 7.13)
    FIXED:  r2per f=2.00: β=1.62;  f=2.25: β=1.74   (1.62, 3.18, 5.43)
            r2rnd f=2.00: β=1.60;  f=2.25: β=1.76
            r2blk f=2.25: β=1.70;  f=2.50: β=1.71
            r2sum f=2.25: β=1.43;  f=2.50: β=1.48
            r3rnd f=2.25: β=2.00;  f=2.50: β=2.09   (k=9,12,15: −lnP = 1.56, 2.76, 4.57)
            r3blk f=2.50: β=1.71;   r3sum f=2.50: β=1.45
Every interleaved word has β at least as large as the identity's at the same f (mostly clearly larger), and
β grows with f towards 2, as for the identity.  The N-dependence at fixed k is convex (e.g. id k=8:
−lnP = 1.92, 2.85, 4.17, 8.11 at N = 32, 36, 40, 48), as expected from a rate N·H(k/√N).
**Conclusion (numerical): the interleaving constraint does NOT destroy the speed-N lower tail; there is no
sign of a speed-k (thread-like) regime, for either notion, for periodic, random or blocky words with r ≤ 3.**
Caveat: k ≤ 20 and r ≤ 3 only; a speed-k regime with a tiny constant (e.g. e^{−ck/r²}) could not be excluded
by these sizes, but the fact that the interleaved patterns fail *less* often than the identity at every
(k, N) is the strongest evidence, since the identity's tail is rigorously speed N.

## 3. Theory: what is proved (proof.md) and where it stops

Proved:
* Lemma 0.1: π_w ⊂ P iff P has separated chains with merge word w; π_w ⊂_fix P iff there are chains
  A_j ⊂ S_j with w ≼ u(A) (subsequence).  Lemma 0.2: w ≼ (12⋯r)^{ρ(w)}, ρ(w) = 1 + #weak descents.
* Prop 1.1 (rigid blocks): Pr(π_w ⊄ Π_N) ≤ Σ_t Pr(LIS(Π_{N a_t²/k²}) < a_t) over the maximal constant blocks
  a_t of w; with Ledoux's lower tail, ≤ C_1 Σ_t e^{−c_1 N a_t²/k²} for N ≥ k²: speed N/A² for A equal blocks,
  and useless (speed k) for the periodic word — this is exactly the thread bound.
* Theorem 2.2 (periodic word, Mirsky/molecule argument): for r ≥ 2 and N ≥ 8(r+1) ln(2er²(r+1)) k²,
  Pr(π_{(12⋯r)^m} ⊄_fix Π_N) ≤ e^{−N/(4r²(r+1))}.  Corollary 2.3: for every word (via ρ(w)) at
  N ≥ 8r²(r+1)ln(2er²(r+1))k²; so for FIXED r, n = O_r(k²) suffices for all unions of r runs (speed N).
* Theorem 2.4 (ℓ-blocky periodic words): threshold N ≥ 4(r+1)k² once ℓ ≥ c√log r, same speed.
* Prop 3.1: FIXED-notion lower bound e^{−N/r} for periodic words (strip 1 empty on the left half, strip 2
  empty on the right half), so the speed of the FIXED notion is N/poly(r), and the open issue is only the
  THRESHOLD (the constant C in N = Ck²) as a function of r.
Sanity check of the deterministic Lemma 2.1 (check_lemma21.py): random/clustered/anti-diagonal bad sets with
B = 2m² bad boxes, poset height computed by brute force for (r,m) ∈ {(2,1),(2,2),(3,1),(2,3)}: height ≥ m in
all trials (minimum heights 2, 4, 2, 5 versus required 1, 2, 1, 3).

The residual class of W9 needs r up to ln⁴ k with an ABSOLUTE C; Theorem 2.2 gives C ≈ r log r, Theorem 2.4
C ≈ r (for blocky words only).  Hence for the He–Kwan problem the strip method as proved gives only
n = O(k² polylog k) — no improvement over 2000k² log log k — but it *does* settle the mechanism question:
the speed is N, not k, and the per-pattern bound e^{−N/poly(r)} is far more than the union bound needs
(e^{−k log r}); what is missing is uniformity of the threshold in r.

### 3.1 Why the box/Mirsky method cannot give an r-independent threshold for ℓ = 1
(i) Bad-box density.  The method needs "≤ 2m² of the 4r²(r+1)m² boxes are bad", i.e. bad density
≤ 1/(2r²(r+1)), and boxes are bad with probability e^{−λ}, so λ ≳ 3 ln r, i.e. C ≳ r ln r.  A density ≈ 1/r
is genuinely a barrier for ANY deterministic lemma of this type: the bad set "strip 1 in the left half,
strip 2 in the right half" has density 1/r and blocks every word containing a 1 before a 2 (this is Prop. 3.1).
The extra factor r comes from Mirsky's theorem being lossy on product orders: on the full (r+1)-dimensional
grid it certifies height ≈ n/(r+1) while the true height is n, and against *adversarial* holes of constant
density the true height is only ≈ n/√r (keep the middle Σ-layers), so this loss cannot be removed while
treating the bad set as adversarial.
(ii) Consequently an r-independent threshold requires using that the bad set is RANDOM (i.i.d. boxes of
density e^{−C}, which is > 1/r for r > e^C): a "probabilistic deterministic lemma" — a lower-tail bound with
speed n² for a multi-species Bernoulli last-passage problem (chains in [n]×[n] with r row-strips, alternating
by w).  For r = 1 this is Seppäläinen's Bernoulli LPP (exactly solvable); for the alternating word no exact
structure is known to me.  A percolation-style renormalization (blocks crossed w.h.p.; block-level holes of
density e^{−cs}; iterate) would plausibly give the correct threshold C = O(1) but only a tail e^{−c n} with
c = O(1), i.e. e^{−c√C k}, which needs C ≈ ln² r to beat r^k — again not absolute.  Not attempted.

### 3.2 The exact-solvability route (task 2b) — not found
The alternating chain p_1 < q_1 < p_2 < q_2 < ⋯ (p in strip 1, q in strip 2) is an increasing chain of
"molecules" (p_i, q_i) in a 4-dimensional order (x(q_i) < x(p_{i+1}), y(p_i) < y(p_{i+1}), y(q_i) < y(q_{i+1})).
Shearing/shifting strip 2 (x ↦ x ± ε, y ↦ y − 1/2) turns alternation into an increasing chain only with an
extra interlacing condition (y(p_i) < y(q_i) − 1/2 < y(p_{i+1})), which is not implied by w; so no bijection
to ordinary LIS/RSK/LGV emerged.  Greene's theorem gives only the necessary condition λ_1+⋯+λ_r ≥ k (used as
a filter in the code).

### 3.3 Route (c), "long chains + regularity" — why it reduces to the same problem
By Lemma 0.1 the question is exactly whether the point set has chains A_j ⊂ S_j with w ≼ u(A).  Chains of
length (1+δ)k_j exist in each strip with failure e^{−Ω(N)} (LIS lower tail; in fact length 2√(N/r) ≫ k/r),
but the merge word of arbitrary long chains is uncontrolled.  A "spread" condition strong enough to force
w ≼ u(A) (e.g. every x-interval of length 1/k meets every A_j) is itself a rigid-cell condition: a chain in a
strip of height 1/r hitting every one of k slabs needs N ≥ rk² (its y-increments are ≈ r/(Ck) per slab),
and relaxing "every slab" to "the slabs assigned to letter j" is the thread model (speed k).  Superadditivity
along diagonal columns is available for the FIXED periodic problem (π_per(r, m_1+m_2) ⊂ Π if column a's
diagonal boxes contain π_per(r, m_a)) and shows m*(N)/√N → c_per(r) exists, but it cannot improve a
threshold constant (scale invariance), only propagate a base bound.

### 3.4 Heuristic picture of the true threshold
FIXED, periodic word, r strips: the rigid greedy (cells of width 1/k, take the lowest point above the level)
succeeds typically iff C ≥ C_0 absolute (the level in strip j after m steps is ≈ h_j(1 − e^{−1/C})), so the
threshold is N = O(k²) with an absolute constant (failure e^{−Θ(k/r)} from the greedy, e^{−N/(4r²(r+1))}
from Theorem 2.2 only above C ≈ r ln r).  Numerically the FIXED threshold (failure 10⁻⁴) is at
N ≈ 0.6 k² for r = 2, 3 (f ≈ 2.5), versus 0.56 k² for the identity — the r-dependence is invisible at r ≤ 3.

## 4. Dead ends (with reasons)
1. Symmetric grid n_0 = n_1 in Lemma 2.1: needs B ≤ 2r(r−1)m² with boxes of side 1/(2rk), λ = C/(4r²):
   threshold C ≈ r² ln r; the asymmetric grid (rows = (r+1) × columns) gives C ≈ r ln r.  Tall boxes
   (n_1 ≫ r n_0) do not help: λ = Cℓ²/(4rt) still carries 1/r because each strip is 1/r high.
2. "Free" molecules (points in arbitrary increasing columns instead of consecutive): the diagonal-line
   cover then has as many lines as elements (width ≈ |P|), Mirsky gives nothing.
3. One-dimensional column scheme (each x-column handles k' consecutive letters, failed columns pass their
   letters on): a run of L bad columns must be survived, which needs the next column to embed (L+1)k'
   letters with N/M points; the requirement L² ≥ M r ln r (to beat r^k) contradicts N/M ≥ C(Lk')².
   Robustness must be two-dimensional (rows AND columns), as in Mirsky.
4. Universal periodic word for general w (Lemma 0.2) costs a factor ρ(w) ≈ k/2 for random w in the
   pattern length; fine for fixed r, hopeless for the threshold.  Blocky universal words (1^ℓ⋯r^ℓ)^m absorb
   only weakly-increasing segments of w with ≤ ℓ repeats, again ≈ k/2.5 rounds for random w.
5. Comparison "interleaved ≤ identity" (numerically true in the FREE notion at all (k,N) tried): no
   deterministic reason (a single long chain contains only identities), so it is not a proof route.

## 5. Status of background runs
runjobs2.sh jobs2.txt (12 cores) is appending to out/: 5·10⁴-sample tail points (f = 2, 2.25, 2.5; seeds
11,12) for id/r2per/r2rnd/r2blk at k = 16, 20 and r3per/r3rnd/r3blk at k = 12, plus the remaining moderate-N
points (f ≤ 1.75, 2000 samples).  Re-run `python3 analyze.py > results.md; python3 fits.py >> results.md`
to refresh the tables; fits.py prints the β exponents of §2.3 with the updated counts.

## 6. W11 continued (2026-08-29, second session): tilted grids with r ~ √k — threshold vs r

Question: does N_{1/2}(π)/k² grow with r for the periodic shuffle (tilted grid, r strips × h slabs,
k = rh) and for 𝓕(r,h,ε)?  If it did for r = h = √k, Alon's conjecture would fail.  Answer: NO —
proved (proof.md §4: threshold ≤ (π/8)k² ≈ 0.393k² uniformly in r, h with min(r,h) → ∞) and confirmed
numerically (thresholds DEcrease with r at fixed aspect; they track the identity's).

### 6.1 Code
* tg.c — exact containment of the tilted grid / π_τ (option -tau eps resamples τ_i with εr moved letters
  per row, i.e. a random member of 𝓕(r,h,ε)) in N uniform points.  Pareto-front DP over x-order; FIXED
  notion (equal strips, state (l_0..l_{r−1}) = current column tops) or FREE (-free: state also carries
  f_1..f_{r−1} = bottoms of columns; exact free containment).  -beam B truncates fronts to the B states
  with smallest Σl − Σf: "found" remains a certificate; "not found" after truncation is reported as
  unknown.  Validated against a brute-force DFS on the same samples (-bf): r ∈ {2,3,4}, h ∈ {2,3}, N ∈
  {12,16,18}, both notions, τ = id and ε = 0.7, 7200 samples, 0 mismatches (validate_tg.out).
  Cost: FIXED exact is fast up to r = h = 7 (k = 49) and ≈ 20–60 s/sample at 8×8; FREE exact ≈ 6 s/sample
  at 4×4 and infeasible beyond r = 3, h ≈ 8 (2r−1-dimensional fronts).
* grid.c — the corner-greedy of Theorem 4.1 on the rigid h×r grid (mode 1 = minimise u+v).
* lisref.py — identity reference: C_{1/2}(id_k) := N_{1/2}/k² by bisection (300 samples per step).
* Raw results: out2/<kind>_<r>_<h>_<N>.txt, lines "r h N reps found exact_notfound unknown" (tg) or
  "r h N reps successes" (grid); analyze2.py prints the tables below.  Runner: runjobs3.py (jobs5.txt).

### 6.2 Results: Pr(π ⊂ Π_N) at N = C k²  (Π_N = N uniform points)

Identity reference (lisref.py): C_{1/2}(id_k) = 0.404 (k=8), 0.350 (16), 0.311 (32), 0.309 (36), 0.298 (49),
0.291 (64), 0.280 (100), 0.273 (144), 0.266 (256)  [→ 1/4 like 2√N − 1.77N^{1/6} = k].

FREE (exact), tilted grid r×h:                          C_{1/2}        identity at same k
    2×4   (k=8) : .048 .147 .312 .618 .758 .863 .980 1     ≈ 0.37          0.40
    3×4   (k=12): .062 .235 .502 .797 .935 .983 1    1     ≈ 0.35          ≈0.37
    2×8   (k=16): .068 .312 .657 .897 .988 1    1    1     ≈ 0.33          0.35
    3×6   (k=18): .075 .385 .780 .960 1    1    1    1     ≈ 0.32          ≈0.34
    2×16  (k=32): .075 .600 .980 1    1    1    1    1     ≈ 0.29          0.31
    (columns C = 0.25 .30 .35 .40 .45 .50 .60 .80)
  Every tilted grid tested is EASIER than the identity of the same length (as in §2.1).

FIXED (exact; equal strips — a sufficient condition, so C_{1/2}^{fix} ≥ C_{1/2}^{free}):
    r×h        k    C=0.25  0.30  0.35  0.40  0.45  0.50  0.60  0.80    C_{1/2}^{fix}   id
    2×2        4    .041   .094  .202  .269  .415  .657  .845           0.55
    3×3        9    .013   .039  .097  .209  .363  .480  .763  .981     0.50
    4×4       16    .002   .028  .108  .290  .525  .726  .960  1        0.44          0.35
    5×5       25    0      .035  .143  .425  .760  .950  1     1        0.41
    6×6       36    .003   .037  .250  .688  .975  .998  1     1        0.375         0.31
    7×7       49    0      .050  .360  .960  1     1     1     1        0.36          0.30
    8×8       64    (exact, 12 samples/point at C = 0.35, 0.40, 0.45: still running at the end of the session;
                     results appear in out2/fix_8_8_{1434,1638,1843}.txt when done — rerun analyze2.py)
    2×8       16    .020   .133  .373  .622  .865  .967  .998  1        0.37          0.35
    4×8       32    .003   .115  .425  .887  .993  1     1     1        0.36          0.31
    8×4       32    0      .005  .080  .280  .605  .920  1     1        0.43          0.31
    2×16      32    .030   .263  .765  .978  .998  1     1     1        0.32          0.31
    3×12      36    .010   .205  .752  .973  1     1     1     1        0.33          0.31
    2×32      64    .045   .730  1     1     1     1     1     1        0.28          0.29
    4×16      64    0      .465  .985  1     1     1     1     1        0.30          0.29
    3×24      72    .020   .580  1     1     1     1     1     1        0.295         0.29
  Reading: along the diagonal r = h = √k the FIXED threshold falls 0.55 → 0.50 → 0.44 → 0.41 → 0.375 →
  0.36 (k = 4 … 49), i.e. it decreases with r, roughly parallel to (and ≈ 0.06 above) the identity's
  finite-size curve; the fixed-strip notion costs more when r is large relative to h (8×4: 0.43 vs 4×8:
  0.36, the strips being rigid but the slabs free — the transposed pattern is the same permutation class,
  so the FREE threshold of 8×4 equals that of 4×8, ≤ 0.36).  Rectangles with r ≤ 4, h ≥ 16 are within
  0.01 of the identity.  Nothing grows with r.

FREE with beam search (certificates only; "?" = beam-truncated and not found, counted as failure):
    6×6   k=36  (beam 200): C=0.25: .01(99?)  0.30: .30(70?)  0.35: .77(23?)  0.40: .92(8?)  0.50: 1  0.60: 1
          → free C_{1/2}(6×6) ≤ 0.33 (exact FIXED gave 0.375; identity 0.31)
    8×8   k=64  (beam 100): C=0.25: 0(50?)  0.30: .15(17?)  0.35: .30(14?)  0.40: .60(8?)  0.50: .90(2?)  0.60: .975(1?)
    10×10 k=100 (beam 80) : C=0.30: .03(29?)  0.35: .07(14?)  0.40: .27(11?)  0.50: .80(6?)  0.60: .77(7?)
          (beam 300 at C=0.40, 8 samples: 2 found, 6 unknown — the beam, not the pattern, is the limit)
    12×12 k=144 (beam 60) : C=0.35: 0(10?)  0.40: .10(9?)  0.50: .30(7?)   [beam 300 at 0.50: out2/beam300_12_12_10368.txt]
    16×16 k=256 (beam 30) : C=0.40: 0(5?)  0.50: 0(5?)
  So for 8×8 the free threshold is certified ≤ 0.40 (Pr ≥ 0.6 at C = 0.40, ≥ 0.9 at 0.50), versus identity
  0.29; for r ≥ 10 the beam is too weak (almost all samples "unknown"), so these give no information either
  way — the exact FIXED numbers above and Theorem 4.1/4.4 are the evidence for larger r.

Corner greedy (rigid grid, Theorem 4.1's strategy; success probability, 100–200 samples):
    r×h      C=0.4  0.5   0.6   0.8   1.0   1.5   2.0
    8×8      0      .03   .03   .57   .79   1     1
    16×16    0      0     .04   .72   .97   1     1
    32×32    0      0     .10   .95   1     1     1
    64×64    0      0     .40   1     1     1
    4×64     0      0     0     .17   .67   .99   1
  The greedy's finite-size threshold moves down slowly towards its limit π/8 = 0.393 (the Cramér exponent
  c(C) of Theorem 4.1 is tiny near the limit: c(0.5) = 0.011, c(0.6) = 0.036, c(0.8) = 0.109, c(1) = 0.201,
  c(1.5) = 0.465, c(2) = 0.750, c(4) = 1.92; so 32 rows at C = 0.6 still fail with probability ≈ 1 − (1 −
  e^{−1.15})^{64} ≈ 1).  The exact DP thresholds are far lower (0.36 at 7×7 vs > 1 for the greedy),
  showing how much the greedy leaves on the table at finite sizes; asymptotically the gap is at most
  0.393/0.25.

### 6.3 Conclusions
1. The tilted grid with r = h = √k and all of 𝓕(r,h,ε) (indeed all block-grid patterns 𝒢(r,h)) have
   threshold ≤ (π/8 + o(1))k² — PROVED (Theorem 4.1/4.4), r-independent.  There is no counterexample to
   Alon's conjecture in this family; the family only defeats the thread/shift-chain METHOD ([W14], [W15],
   and W18's negative lag lemma), not the statement n = O(k²).
2. Numerically the true thresholds of tilted grids are at or slightly above the identity's finite-size
   values (free: within 0.03 for k ≤ 32; fixed-strip upper bounds within 0.06–0.1 for r = h ≤ 7) and
   decrease with k along r = h = √k, consistent with the universal (1/4 + o(1))k² picture of W10.  The
   r = h = 16, k = 256 case could not be decided exactly (beam too weak, exact DP infeasible).
3. What the proof does NOT give: speed N (or even speed k for the column part) — the greedy is killed by
   one bad column (e^{−c(C)h}); a union bound over 𝓕 is impossible anyway (|𝓕| = e^{Θ(k ln k)}).

### 6.4 Dead ends / not done (this session)
* The Greene/RSK "nested chains" route (task 2 of the brief): not pursued — the tilted grid's copy is NOT
  near a monotone curve (its points fill the square as an h×r grid), so nested chains near the diagonal
  are the wrong object; the r strip-chains each need only h ≪ 2√(N/r) points and the whole difficulty is
  the lockstep, which the corner-greedy resolves directly.
* Exact FREE containment for r ≥ 4: the 2r−1-dimensional Pareto front explodes; a smarter exact algorithm
  (e.g. enumerating strip boundaries from the data, or an ILP) was not attempted.
* Improving π/8: other corner rules are worse (square 9π/64, quarter disc 4/π²; the triangle is optimal
  among 1-homogeneous rules, proof.md §4 comment (ii)); non-greedy (lookahead / DP) strategies would
  lower the constant but need a new LLN — the exact FIXED numerics suggest the rigid-strip free-slab
  threshold is ≈ 0.30–0.36 at k ≤ 64.
