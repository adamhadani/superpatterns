# W16 — the universal absence constant κ: what is proved, what is not (2026-08-29)

Setting and notation as in W12 proof.md §2: Π_N Poisson of intensity N on [0,1]²; π ∈ S_k; for a copy
P = {p_1, …, p_k} (x-increasing, p_r of y-rank π(r)) put x_0 = 0, x_{k+1} = 1, y_{(0)} = 0, y_{(k+1)} = 1,
   columns  C_c = (x_{c−1}, x_c), c = 1..k+1, g_c = |C_c|;   bands  B_b = (y_{(b)}, y_{(b+1)}), b = 0..k, h_b = |B_b|;
   cell (c,b) = C_c × B_b.
The x-strip of p_r is S_r = cell(r, π(r)−1) ∪ cell(r, π(r)); the y-strip is S'_r = cell(r, π(r)−1) ∪ cell(r+1, π(r)−1).
A copy is *lex-min* if it minimises (x_1, x_2, …, x_k) lexicographically among all copies; a.s. it exists and is
unique when π ⊂ Π_N, hence
   E #{lex-min copies of π in Π_N} = Pr(π ⊂ Π_N)   exactly.                                            (0)

**Bottom line.**  The best rigorous universal constant remains W12's: for every π ∈ S_k,
Pr(π ⊂ Π_N) ≤ 668 N^{−1/2} e^{3√N − 1.3163 k}, i.e. κ = 2.279 (certificate W12 §2.4).  Nothing below is a
certified improvement of it.  What is new: (1) the second level of the lex-min hierarchy for arbitrary π
(Lemma 2, Theorem 3), which explains structurally why the transfer-operator method cannot go below 2.279
uniformly in π; (2) negative results for the two other canonical rules that were proposed (Prop. 1, §3);
(3) numerics (§5) on whether the identity is the extremal pattern.

--------------------------------------------------------------------------------------------------
## 1. Mixed canonical rules (route (b))

**Proposition 1.**  Let [k] = L ⊔ D.  If π ⊂ Π_N then Π_N contains a copy P with S_r ∩ Π_N = ∅ for all r ∈ L and
S'_r ∩ Π_N = ∅ for all r ∈ D.
*Proof.*  Among the finitely many copies take one minimising Φ(P) = Σ_{r∈L} x_r + Σ_{r∈D} y_r.  If r ∈ L and
q ∈ S_r ∩ Π_N, then (P ∖ {p_r}) ∪ {q} is a copy (q lies in the allowed box of p_r) whose x-coordinates are those of
P except that x_r is replaced by x_q < x_r, and whose y-coordinates in positions D are unchanged (r ∉ D), so
Φ decreases: contradiction.  Symmetrically for r ∈ D.  ∎

The "both strips empty for every r" copy that the task description asked for need NOT exist (k = 1, points
(0.1, 0.9) and (0.9, 0.1): neither is leftmost and lowest).  Only the split rules of Prop. 1 are available.
For the identity with L = odd, D = even the regions are pairwise disjoint (the y-strip of an even r lies in
band r−1 and columns r, r+1; the x-strips of r±1 lie in columns r±1 and bands r−2, r−1 resp. r, r+1, so the only
possible overlap, cell(r+1, r−1), is not in S_{r+1}), and the Mecke/Chernoff computation of W12 §2.3 goes through
with the g's integrated out: factors 1/(s + h_{r−2} + h_{r−1} + h_r) for odd r and 1/(s + h_{r−1}) for even r,
a two-step transfer operator on pairs (mixedLD.py).  Result on the n = 40 grid: κ = 2.347 (mixed) versus 2.291
(all-leftmost on the same grid): the unbalanced rule is WORSE.  Since the all-leftmost rule is π-independent
(W12 Prop. 3) and every split rule is a π-dependent perturbation of it that lost for the identity, route (b) is
closed.  (The x+λy potential of the first W16 agent gives 2.2757 for the identity — a 0.003 gain — and for a general
π its empty regions overlap between positions r, r+1 whenever π(r+1) = π(r) − 1, so not even that is universal.)

--------------------------------------------------------------------------------------------------
## 2. Second level of the lex-min hierarchy, for every π

**Lemma 2 (two-point moves).**  Let P be the lex-min copy of π.  Then, besides S_r ∩ Π_N = ∅ for all r
(level 1 = W12 Claim A), for every m ∈ {1, …, k−1}, with r = π^{-1}(m) and j = π^{-1}(m+1):
 (ii) if r < j: there are no q, q' ∈ Π_N with q ∈ cell(r, m+1), y_{q'} > y_q, x_{q'} > x_q, and
      q' ∈ cell(j+1, m+1), or (if j = r+1) q' ∈ cell(r, m+1);
 (iii) if j < r: there are no q, q' ∈ Π_N with q ∈ cell(j, m−1), y_{q'} < y_q, x_{q'} > x_q, and
      q' ∈ cell(r+1, m−1), or (if r = j+1) q' ∈ cell(j, m−1).
*Proof of (ii).*  Suppose q, q' exist and let P' = (P ∖ {p_r, p_j}) ∪ {q, q'}.  x-order of P': x_{r−1} < x_q < x_r,
so q occupies position r; if q' ∈ cell(j+1, m+1) then x_j < x_{q'} < x_{j+1} and q' occupies position j (the points
p_{r+1}, …, p_{j−1} are between q and q' when j > r+1; when j = r+1 nothing is); if j = r+1 and q' ∈ cell(r, m+1)
with x_{q'} > x_q then x_q < x_{q'} < x_r < x_{r+2}, and again q' occupies position r+1 = j.  y-order: the y-values
of P ∖ {p_r, p_j} are the y_{(i)}, i ∉ {m, m+1}; both q and q' lie in B_{m+1} = (y_{(m+1)}, y_{(m+2)}) and y_q < y_{q'},
so q has rank m and q' rank m+1 in P'.  Hence P' is a copy of π with x'_i = x_i for i < r and x'_r = x_q < x_r:
lexicographically smaller than P, contradiction.  (iii) is the mirror image (q at position j, rank m+1; q' at
position r, rank m; x'_j = x_q < x_j).  ∎

Remarks.  (a) The two-cell part of (ii) is vacuous when j+1 ≤ k and π(j+1) = m+2 (then cell(j+1, m+1) ⊂ S_{j+1}
is already empty); that of (iii) is vacuous when r+1 ≤ k and π(r+1) = m−1.  For the identity every two-cell part
is vacuous and every same-cell part is present ("no increasing pair in cell(r, r+1)"); for the decreasing pattern
the mirror statement holds — as it must, since y ↦ 1−y maps lex-min copies of id_k to lex-min copies of the
decreasing pattern (the computation "decreasing, level 2" in pairs.py applied a two-cell factor that is vacuous
there, on top of the strip factor of the same cell; its output is invalid and is superseded by the identity's).
(b) For a pattern without the adjacencies π(r+1) = π(r) ± 1 (a random π has ≈ 2 of them) only two-cell parts
exist, and they couple column π^{-1}(m) with column π^{-1}(m+1)+1: positions that are far apart for a generic π.
(c) The cells of the two-cell part of (ii)/(iii) are never strip cells when the part is non-vacuous; two ascent
pairs (r < j) use different bands, two descent pairs use different bands, so each of the two families is
pairwise cell-disjoint and disjoint from the strips.

(Lemma 2 and Theorem 3 were brute-force checked, check_lemma2.py: 6 patterns of length 4–5, ≈ 5000 lex-min copies,
0 violations; and E^{(2)} ≥ Pr(π ⊂ Π_N) in every case, e.g. 0.665 ≥ 0.551 for 1234 at N = 8.)

**Theorem 3 (level-2 Mecke bound).**  Let M ⊂ {1..k−1} be a set of indices m such that the cells used by the
non-vacuous parts chosen for m ∈ M are pairwise disjoint (e.g. all ascent pairs, or all descent pairs, or
same-cell parts only).  Then
   Pr(π ⊂ Π_N) ≤ N^k ∫_{Δ_x × Δ_y} exp(−N Σ_r g_r (h_{π(r)−1} + h_{π(r)})) · Π_{m∈M} Φ_m dg dh,
where, with a = N g_{c_1} h_b, b' = N g_{c_2} h_b for the two cells (c_1,b), (c_2,b) of m,
   Φ_m = F(a, b') := e^{−a−b'} (a e^{a} − b' e^{b'})/(a − b')         (two-cell part; F(a,a) = (1+a)e^{−a}),
   Φ_m = e^{−μ} I_0(2√μ), μ = N g_{c_1} h_b                                (same-cell part).
*Proof.*  By (0) and Lemma 2, Pr(π ⊂ Π_N) = E#lex-min ≤ E#{copies P satisfying level 1 and the chosen parts for
m ∈ M}.  Apply the Mecke formula as in W12 §2.2; conditionally on the k points, Π_N restricted to the union of
the strips and the chosen cells is a Poisson process, and the events "S_r empty", "part m holds" depend on
disjoint regions, hence are independent.  The probability that a Poisson cell A of mean a and a Poisson cell B of
mean b' in the same band contain no q ∈ A, q' ∈ B with y_{q'} > y_q (heights i.i.d. uniform in the band):
Σ_{i,i'} e^{−a}a^i/i! · e^{−b'}b'^{i'}/i'! · i!i'!/(i+i')! = e^{−a−b'} Σ_n (a^{n+1} − b'^{n+1})/((a−b') n!) = F(a,b');
the probability that a Poisson cell of mean μ contains no increasing (or no decreasing) pair is
Σ_i e^{−μ} μ^i/(i!)² = e^{−μ} I_0(2√μ).  ∎

**Corollary 4 (identity; numerical, not certified).**  With M = all m, the same-cell parts, and the Chernoff
weights e^{−sΣg − tΣh}, integrating out g_r gives Φ(u,v,w) = e^{w/(s+u+v+w)}/(s+u+v+w) (u,v,w = h_{r−1},h_r,h_{r+1})
in place of 1/(s+u+v), a transfer operator on pairs (pairs.py).  On an n = 80 grid: κ_id ≤ 2.2435 at s = t = 1.4,
versus 2.2816 for level 1 on the same grid (continuum 2.2787), i.e. ≈ 2.240 in the continuum.  The lex-min
hierarchy therefore gains ≈ 0.04 per level at the identity (it must converge to the truth κ = 2 by (0)).

**Why this does not improve the universal constant.**  For a generic π the h-chain obtained after integrating
the g's is no longer Markov: g_{c} with c = π^{-1}(m+1)+1 enters the strip factor with bands π(c)−1, π(c) and
the pair factor with band m+1, and π(c) is unrelated to m.  The transfer-operator (Collatz–Wielandt) method
only sees the same-cell parts, which exist only at the ≈ 2 positions of a random π with π(r+1) = π(r) ± 1, so
sup_π of the transfer bound is still 2.279.  Product bounds F(a,b') ≤ φ(a)ψ(b') that would decouple the two
columns do not exist (F(a,0) = 1 forces φ(a)ψ(0) ≥ 1 for all a, and F(a,a) → 0), and Hölder splitting of the
k−1 factors is useless (it tends to ess sup F = 1).  Genuinely global tools would be needed.

--------------------------------------------------------------------------------------------------
## 3. Route (c) (RSK / Erdős–Szekeres) — dead, and what the coarse-graining shows
Greene's theorem constrains the shape λ(Π_N) ≈ √N·(limit shape) only through lis(π), lds(π); for a random π
these are ≈ 2√k = O(N^{1/4}) ≪ 2√N, no constraint at all.  The instructive fact behind this: tile the square by
cells of side δ/√N.  A copy of the identity at k ≈ 2√N occupies a monotone path of ≈ √N/δ cells with ≈ 2δ
points each (its clustering — copies re-routing through other cells — is the LPP path entropy that brings 2.279
down to 2).  A copy of a random π puts its k points into ≈ k different cells spread over the whole square (cell
(a,b) receives the positions of block a whose ranks fall in block b: ≈ (2δ)²/k ≪ 1 points).  No monotone-path
or shape argument can see such copies.  Nevertheless the per-point clustering of copies of a random π at level 2
is quantitatively the same as the identity's (§5), which is the evidence for universality.

--------------------------------------------------------------------------------------------------
## 4. Is the identity the extremal pattern?  (thresholds, numerics; contain_gen for k ≤ 16, contain_mrv for k = 20)
Half-probability containment thresholds n_½(π) for uniform σ_n (thresholds.out; k = 20 in thresholds_k20.out;
contain_gen.c has MAXK = 16 and is invalid beyond it, contain_mrv.c agrees with it on common samples):
   k      8      10     12     14     16     20
   id     25.9   37.3   51.8   67.6   87.3   135.6
   rand   24.3–24.7  35.7–36.8  49.7–50.4  64.2–66.4  81.5–83.0  120–124
   ratio  .949   .971   .967   .967   .942   .90
   n_½/k²: id .405 .373 .360 .345 .341 .339 ; rand (mean) .384 .362 .348 .334 .321 .304 ; E_lc = 1 at .367 .335 .313 .296 .285 .265
(E_lc(N) = E#leftmost-canonical copies, pattern-independent, E_lc.py; its threshold tends to 1/2.279² = 0.1925.)
Random patterns are contained MORE easily than the identity at every k tested, by 3–10 % in n, and the gap WIDENS
from k = 16 to k = 20 (±2–3 % sampling error).  Random patterns sit at a nearly constant offset ≈ 0.04 k² above the
strip-bound threshold N_lc (rand − N_lc/k² = .036 .038 .036 .039 for k = 12..20) while the identity's offset grows
(.048 .049 .056 .074).  Both n_½/k² decrease with k; the identity's limit is 1/4 with a
Tracy–Widom correction (n_½ ≈ (k/2 + 0.9 k^{1/3})²), the random ones' limit is the open question: it lies in
[0.1925, 0.25] (the lower end by W12's theorem, the upper end if the identity is asymptotically the easiest).
A fit n_½ = (k/2 + a k^{1/3})² gives a stable a ≈ 0.51–0.61 for the identity (Tracy–Widom) but a drifting
a = .48 .47 .47 .45 .42 .38 for random π: their correction is NOT of order k^{1/3}.  The simplest reading of the data
is lim n_rand/k² ≈ 0.23 < 1/4 (κ_univ ≈ 2.09 > 2, identity NOT the asymptotically easiest pattern); the reading
"both → 1/4, random with a lower-order correction" is not excluded.  Honest answer: leaning to κ_univ > 2, undecided;
k = 24–32 with ≥ 500 samples (contain_mrv) would decide.

## 5. Level-2 clustering: identity vs random π (level2_mc.py, Monte Carlo of Theorem 3's integral)
E^{(2)}(π,N)/E_lc(N), k = 16:  N = 78: id 0.578, rand 0.594–0.639;  N = 86: id 0.530, rand 0.549–0.599;
k = 12, N = 48: id 0.649, rand 0.659–0.726.  Larger k at N with E_lc ≈ 1.4–2.6 (level2_big.out), log-ratio per point:
k = 20: id −0.033, rand −0.028…−0.031;  k = 24: id −0.030, rand −0.026…−0.028;  k = 32: id −0.028, rand −0.025…−0.026.
So random patterns receive ≈ 90 % of the identity's level-2 gain: the second
level of the lex-min hierarchy removes almost the same amount of clustering for random patterns (through the
non-local two-cell conditions) as for the identity (through the local same-cell conditions).  This is the best
evidence we have that the whole hierarchy behaves alike for all π — i.e. that κ_univ = 2 — but it is not a proof,
and level 3+ for random π involves subsets connected in the union of the rank path and the position path, whose
enumeration is not transfer-tractable.

## 6. Conclusion
Rigorous: κ = 2.279 (W12, unchanged; certificate there).  Rigorous and new: Prop. 1, Lemma 2, Theorem 3.
Numerical: level 2 gives κ_id ≈ 2.240 (transfer, uncertified) and a comparable gain for random π (Monte Carlo);
mixed leftmost/lowest rules and potentials x+λy do not help; RSK does not apply.  Open: whether
lim n_½(π)/k² = 1/4 for random π (equivalently κ_univ = 2); the k = 20 data (ratio rand/id = 0.90, widening) lean
towards a limit ≈ 0.23 < 1/4, i.e. κ_univ > 2 — which would mean c_τ ≤ 2/|τ| can never follow from a π-uniform bound.
