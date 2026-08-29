# W11 — union-of-runs patterns via strips: proved statements

Date: 2026-08-29.  Everything below is proved in full here, except where a published theorem is cited
explicitly (the LIS lower tail).  Numerics, heuristics and dead ends are in log.md.

## 0. Setting and notation

Π_N is a Poisson point process of intensity N on [0,1]² (all statements transfer to N i.i.d. uniform
points and to a uniform σ ∈ S_n by the standard coupling; see Remark 0.3).

A *word* w ∈ [r]^k with letter counts k_j = #{i : w(i) = j} defines the pattern π_w ∈ S_k by
π_w(i) = (k_1 + ⋯ + k_{w(i)−1}) + #{i' ≤ i : w(i') = w(i)}: the positions carrying letter j form an
increasing run of length k_j occupying the value interval (k_1+⋯+k_{j−1}, k_1+⋯+k_j].  Every union of r
increasing runs on disjoint value intervals is of this form.  Special words: the *periodic* word
(12⋯r)^m (k = rm), the *ℓ-blocky periodic* word (1^ℓ 2^ℓ ⋯ r^ℓ)^m (k = rmℓ), and the sum word
1^{k_1} 2^{k_2} ⋯ r^{k_r} (π_w = ⊕-sum of increasing runs = the identity).

For a finite point set P ⊂ [0,1]² in general position (distinct x's and y's), a *chain* is a subset
increasing in both coordinates.  Chains A_1, …, A_r are *separated* if max y(A_j) < min y(A_{j+1}) for
all j (empty chains impose no condition).  Their *merge word* u(A_1,…,A_r) ∈ [r]^{Σ|A_j|} lists, in
increasing x-order, the index j of the chain each point belongs to.  For words, v ≼ u means v is a
subsequence of u.

Two containment notions are used.  *Free* containment is ordinary pattern containment π_w ⊂ P.
*Fixed-strip* containment (heights h_1,…,h_r > 0, Σh_j = 1; default h_j = k_j/k or h_j = 1/r): the
strips are S_j = [0,1] × [H_{j−1}, H_j), H_j = h_1+⋯+h_j, and π_w ⊂_fix P means there are chains
A_j ⊂ P ∩ S_j, |A_j| = k_j, with u(A_1,…,A_r) = w.  Trivially π_w ⊂_fix P ⇒ π_w ⊂ P, so every upper
bound below on Pr(π_w ⊄_fix Π_N) is an upper bound on Pr(π_w ⊄ Π_N).

**Lemma 0.1 (merge-word criterion).**  (a) If A_1,…,A_r ⊂ P are separated chains and w ≼ u(A_1,…,A_r),
then π_w ⊂ A_1 ∪ ⋯ ∪ A_r.  (b) π_w ⊂ P iff P contains separated chains A_1,…,A_r with u(A) = w.
(c) π_w ⊂_fix P iff there are chains A_j ⊂ P ∩ S_j (j = 1..r) with w ≼ u(A_1,…,A_r).

*Proof.*  (a) Fix an occurrence of w as a subsequence of u = u(A): positions t_1 < ⋯ < t_k of the
x-sorted list of ∪A_j such that the point at t_i belongs to A_{w(i)}.  These k points have x-order
1,…,k; the points with letter j form a subset of the chain A_j, hence increase in y along positions;
and all points of A_j lie below all points of A_{j'} for j < j' (separation).  So their y-order is that
of π_w.  (b) "If" is (a).  "Only if": in a copy of π_w the points carrying letter j form a chain
(letter-j positions are an increasing run of π_w), the chains are separated because the letter classes
occupy increasing value intervals, and their merge word is w.  (c) Chains in distinct strips are
separated, so "if" is (a); "only if" is as in (b), the letter-j points lying in S_j by definition.  ∎

*Warning.*  With given chains A_j, π_w ⊂ ∪A_j does not imply w ≼ u(A): the identity 1234 = π_{1122}
lies in A_1 ∪ A_2 with A_1 = {1,2,3}, A_2 = {4}, while u = 1112 ⋡ 1122.  Only (b), (c) are used.

**Lemma 0.2 (universal periodic word).**  Let ρ(w) = 1 + #{i < k : w(i+1) ≤ w(i)}.  Then
w ≼ (12⋯r)^{ρ(w)}, hence π_w ⊂ π_{(12⋯r)^{ρ(w)}}, and ρ(w) ≤ k.

*Proof.*  Embed w greedily: letter w(1) into the first period; if w(i+1) > w(i) the next letter fits in
the same period after w(i), otherwise it goes into the next period.  The number of periods used is
ρ(w).  The pattern statement follows from Lemma 0.1 applied to the point set π_{(12⋯r)^ρ} itself
(its letter classes are separated chains with merge word (12⋯r)^ρ).  ∎

**Remark 0.3 (de-Poissonization).**  If Π_{N} ⊂ Q in the natural coupling of a Poisson process with
|Π_N| ≤ n and n i.i.d. uniform points Q (Q ⊇ Π_N), then Pr(π ⊄ Q) ≤ Pr(π ⊄ Π_N) + Pr(Poisson(N) > n).
With N = n/2, Pr(Poisson(n/2) > n) ≤ exp(−(n/2)(2 ln 2 − 1)) ≤ e^{−0.19 n}.  A uniform σ ∈ S_n contains
π iff n i.i.d. uniform points do.

**Cited fact (LIS lower tail; speed N).**  Let L(Π_λ) be the length of the longest chain of Π_λ.
There are universal constants C_1, c_1 > 0 with
   Pr( L(Π_λ) ≤ (2 − ε)√λ ) ≤ C_1 exp(−c_1 ε³ λ),   0 < ε ≤ 2, λ > 0            (LT)
(Ledoux 2005/2007, "Deviation inequalities on largest eigenvalues", §5, via the Tracy–Widom left tail;
the speed-λ lower tail LDP with explicit rate is Deuschel–Zeitouni 1999).  By affine invariance of
Poisson processes, (LT) applies to the points of Π_N in any axis-parallel rectangle R with λ = N·area(R).

## 1. Rigid blocks: words with few letter changes

Write w = j_1^{a_1} j_2^{a_2} ⋯ j_A^{a_A} with j_t ≠ j_{t+1} (A = number of maximal constant blocks,
a_1+⋯+a_A = k).  Use the fixed strips with h_j = k_j/k.

**Proposition 1.1.**  For every N > 0,
   Pr(π_w ⊄_fix Π_N) ≤ Σ_{t=1}^{A} Pr( L(Π_{N a_t²/k²}) ≤ a_t − 1 ).
In particular, if N ≥ k² then Pr(π_w ⊄ Π_N) ≤ C_1 Σ_t exp(−c_1 N a_t²/k²), and for equal blocks
a_t = k/A this is ≤ A·C_1 exp(−c_1 N/A²).

*Proof.*  Cut the x-axis into consecutive intervals I_1,…,I_A of lengths a_1/k,…,a_A/k.  Inside strip
S_j (height k_j/k) cut consecutive horizontal sub-strips of heights a_t/k for the blocks t with j_t = j,
in the order of t; they tile S_j because Σ_{t: j_t=j} a_t = k_j.  Let R_t = I_t × (sub-strip of block t),
a rectangle of area a_t²/k².  If every R_t contains a chain of length a_t, take such chains: their union
in x-order reads block 1, block 2, …; block t's points lie in S_{j_t} and, within a strip, later blocks
lie in higher sub-strips, so the letter-j points form a chain in S_j and the merge word is w.  Lemma 0.1
gives π_w ⊂_fix Π_N.  Hence failure requires some R_t to have L(Π_N ∩ R_t) ≤ a_t − 1, and Π_N ∩ R_t is a
Poisson process of intensity N a_t²/k² (up to an affine map).  For the second claim apply (LT) with
λ = N a_t²/k² and (2−ε)√λ = a_t, i.e. 2 − ε = k/√N ≤ 1, so ε ≥ 1.  ∎

*Comments.*  (i) For the sum word (A = r, a_t = k_j) this is the ⊕-sum bound: speed N/r² for equal
runs.  (ii) For the periodic word A = k and the bound degenerates to k·Pr(Poisson(N/k²) = 0) = k e^{−N/k²}
= k e^{−C}: this is the "threads" bound (speed k after amplification), and it is exactly the situation
in which the interleaving matters.  (iii) The bound is monotone in the block structure only through the
a_t: any two words with the same block-size multiset get the same bound.

## 2. Periodic and blocky words: a Mirsky/molecule bound with speed N

Fix r ≥ 2, ℓ ≥ 1, m ≥ 1, the word w = (1^ℓ 2^ℓ ⋯ r^ℓ)^m (k = rmℓ; ℓ = 1 is the periodic word), and
equal strips h_j = 1/r.  Let
   n_0 = 2m (column groups),  n_1 = 2(r+1)m (rows per strip).
Grid: box-columns of width 1/(r n_0) indexed by a ∈ {0,…,r n_0 − 1}; inside strip j, rows of height
1/(r n_1) indexed by b ∈ {1,…,n_1}.  Box (a, j, b) is the corresponding rectangle; there are
r n_0 · r n_1 = 4r²(r+1)m² boxes, each of area 1/(4r²(r+1)m²), so each contains Poisson(λ) points with
   λ = N / (4 r² (r+1) m²),
independently over boxes.  Call a box *good* if it contains a chain of length ℓ (for ℓ = 1: nonempty),
and let B be the number of bad boxes; the bad indicators are i.i.d. Bernoulli(p), p = Pr(L(Π_λ) ≤ ℓ−1).

**Lemma 2.1 (deterministic).**  If B ≤ 2m² then π_w ⊂_fix Π_N.

*Proof.*  A *molecule* is a tuple (c, b_1, …, b_r) with c ∈ {0,…,n_0−1}, b_j ∈ {1,…,n_1}, such that the r
boxes (rc + j − 1, j, b_j), j = 1..r, are all good.  For each good box fix a chain of length ℓ inside
it.  Order molecules by (c, b) ≺ (c', b') iff c < c' and b_j < b'_j for all j.  A chain of molecules
μ_1 ≺ ⋯ ≺ μ_m yields a copy of π_w: take, for each t and j, the ℓ-chain of the box (r c_t + j − 1, j,
b_{t,j}).  In x-order, the boxes of μ_t occupy the consecutive box-columns r c_t, …, r c_t + r − 1, all
to the left of those of μ_{t+1} (r c_{t+1} ≥ r c_t + r).  So the merge word is (1^ℓ ⋯ r^ℓ)^m = w.  Within
strip j, the ℓ-chains of μ_1, …, μ_m lie in rows b_{1,j} < ⋯ < b_{m,j}, hence their union is a chain in
S_j.  Lemma 0.1 (fixed version) applies.

It remains to show that the poset P of molecules has a chain of length m when B ≤ 2m².
*Lower bound on |P|.*  Let G_{c,j} = {b : box (rc + j − 1, j, b) is good} and B_{c,j} = n_1 − |G_{c,j}|;
Σ_{c,j} B_{c,j} ≤ B.  Then |P| = Σ_c Π_j |G_{c,j}| = n_1^r Σ_c Π_j (1 − B_{c,j}/n_1) ≥
n_1^r Σ_c (1 − Σ_j B_{c,j}/n_1) ≥ n_0 n_1^r − n_1^{r−1} B.
*Upper bound on the width.*  Every antichain of P has size ≤ n_1^r + r n_0 n_1^{r−1}: the grid
{0,…,n_0−1} × {1,…,n_1}^r is partitioned into the "diagonal lines" {e + t(1,1,…,1) : t ∈ Z} ∩ grid;
each line is a chain for ≺ (all coordinates strictly increase), so an antichain meets it at most once;
each line has a unique element with c = 0 or some b_j = 1, so there are at most n_1^r + r n_0 n_1^{r−1}
lines.
*Mirsky.*  By Mirsky's theorem P is the union of h antichains, h = the maximum chain length, so
   h ≥ |P| / width ≥ (n_0 n_1 − B) / (n_1 + r n_0) = (4(r+1)m² − B) / (2(2r+1)m).
This is ≥ m iff B ≤ 4(r+1)m² − 2(2r+1)m² = 2m².  ∎

**Theorem 2.2 (periodic word, ℓ = 1).**  Let r ≥ 2, k = rm, w = (12⋯r)^m and
   N ≥ 8 (r+1) ln(2e r²(r+1)) · k².
Then  Pr(π_w ⊄_fix Π_N) ≤ exp( − N / (4 r² (r+1)) ).

*Proof.*  Here p = e^{−λ} with λ = N/(4(r+1)k²) ≥ 2 ln(2er²(r+1)).  By Lemma 2.1 and the union bound
over sets of 2m² boxes,
Pr(fail) ≤ Pr(B ≥ 2m²) ≤ C(4r²(r+1)m², 2m²) p^{2m²} ≤ (2e r²(r+1))^{2m²} e^{−2m²λ}
 = exp(−2m² (λ − ln(2er²(r+1)))) ≤ exp(−m²λ) = exp(−N/(4r²(r+1))).  ∎

**Corollary 2.3 (every word, r fixed).**  For every w ∈ [r]^k (r ≥ 2) with ρ = ρ(w) ≤ k as in Lemma 0.2,
if N ≥ 8(r+1) ln(2er²(r+1)) r² ρ² (in particular if N ≥ 8 r²(r+1) ln(2er²(r+1)) k²), then
Pr(π_w ⊄ Π_N) ≤ exp(−N/(4r²(r+1))).  Consequently, for each fixed r, a uniformly random permutation of
length n ≥ 16 r²(r+1) ln(2er²(r+1)) k² + O(1) contains every union-of-r-runs pattern of length k with
probability ≥ 1 − r^k e^{−n/(8r²(r+1))} − e^{−0.19n} → 1.

*Proof.*  π_w ⊂ π_{(12⋯r)^ρ} (Lemma 0.2), and the latter is a periodic word with k' = rρ letters;
apply Theorem 2.2 with k' (free containment is implied by fixed-strip containment).  The last sentence
is Remark 0.3 plus a union bound over the r^k words.  ∎

**Theorem 2.4 (ℓ-blocky periodic words; threshold linear in r).**  Let r ≥ 2, ℓ ≥ 1, k = rmℓ,
w = (1^ℓ ⋯ r^ℓ)^m, N = C k² with C ≥ 4(r+1), and suppose
   ℓ² ≥ 8 (r+1) ln(2e C_1 r²(r+1)) / (c_1 C)      (with C = 4(r+1): ℓ² ≥ 2 ln(2eC_1r²(r+1))/c_1).
Then Pr(π_w ⊄_fix Π_N) ≤ exp( − c_1 N / (4 r² (r+1)) ).

*Proof.*  λ = Cℓ²/(4(r+1)) ≥ ℓ², so (2−ε)√λ = ℓ has ε = 2 − ℓ/√λ ≥ 1 and (LT) gives
p ≤ C_1 e^{−c_1 λ}.  As in Theorem 2.2, Pr(B ≥ 2m²) ≤ (2er²(r+1))^{2m²} (C_1 e^{−c_1λ})^{2m²}
= exp(−2m²(c_1 λ − ln(2eC_1 r²(r+1)))) ≤ exp(−m² c_1 λ) = exp(−c_1 N/(4r²(r+1))) under the stated
condition on ℓ.  ∎

*Comments.*  (i) Both theorems have speed N (per pattern), which is what the union bound over the
e^{Θ(k log r)} residual patterns of W9 needs — provided N is above the threshold.  (ii) The thresholds
are N ≥ 8(r+1)ln(2er²(r+1)) k² (ℓ = 1) and N ≥ 4(r+1)k² (ℓ ≳ √log r).  They grow with r, so for the
residual class of W9 (r up to ln⁴ k) they only give n = O(k² · polylog k) — no improvement on He–Kwan;
for bounded r they give the optimal order n = O_r(k²) with exponentially small failure.  log.md §3
explains why the box/Mirsky method cannot give an r-independent threshold for ℓ = 1.

## 3. A lower bound for the fixed-strip model

**Proposition 3.1.**  For w = (12⋯r)^m (any m ≥ 1), any r ≥ 2 and equal strips,
Pr(π_w ⊄_fix Π_N) ≥ e^{−N/r}.  More generally, for any w containing the factor "12" (a letter 1
immediately or eventually followed by a letter 2 — i.e. w has a 1 before some 2),
Pr(π_w ⊄_fix Π_N) ≥ exp(−N(h_1 + h_2)/2).

*Proof.*  On the event that S_1 ∩ {x < 1/2} and S_2 ∩ {x > 1/2} contain no points (probability
exp(−N(h_1+h_2)/2)), every point of S_1 lies to the right of every point of S_2, so no chain in S_1
has a point preceding a point of a chain in S_2, and w, which needs a 1 before a 2, cannot be a
subsequence of any merge word (Lemma 0.1).  ∎

So for the fixed-strip periodic pattern the failure probability lies between e^{−N/r} and
e^{−N/(4r²(r+1))} (the latter for N above the threshold of Theorem 2.2): the speed is N/poly(r), and
it is the *threshold*, not the speed, that the method does not control uniformly in r.

## 4. Block-grid patterns (tilted grids and the family 𝓕): an r-independent threshold (π/8)k²

Added 2026-08-29 (W11 continued).  This section removes the r-dependence of the threshold for the
periodic word, for the whole family 𝓕(r,h,ε) of [W15] §4, and more generally for the following class.

**Definition (block-grid patterns).**  Let r, h ≥ 1, k = rh.  For τ = (τ_0,…,τ_{h−1}) ∈ (S_r)^h let
   π_τ(ir + s) := τ_i(s)·h + i        (0 ≤ i < h, 0 ≤ s < r; positions and values 0-indexed),
and 𝒢(r,h) := {π_τ : τ ∈ (S_r)^h}.  Thus π_τ is a permutation of [k] (the pair (τ_i(s), i) determines
(i,s)); τ_i = id for all i gives the tilted grid π(ir+s) = sh + i, which is the periodic word (12⋯r)^h of §0
(letter j = value block [jh,(j+1)h)); and 𝓕(r,h,ε) = {π_τ : |Fix τ_i| ≥ (1−ε)r ∀i} ⊆ 𝒢(r,h) ([W15] §4).
Geometrically: positions are cut into h consecutive *slabs* of r positions, values into r consecutive
*strips* of h values; every (slab, strip) pair contains exactly one entry of π_τ; inside slab i the
entries visit the strips in the order τ_i(0), τ_i(1), …, τ_i(r−1); inside strip j the entries are
ordered by slab index (π_τ^{-1} is increasing on each strip, [W15] Lemma 9).

**Notation.**  Π_N is the Poisson process of intensity N on [0,1]²; write N = C k².  The *cell* (i,j) is
the rectangle [i/h, (i+1)/h) × [j/r, (j+1)/r) (area 1/k).  For C > 0 let (U, V) be the random vector
with density  C·exp(−C(u+v)²/2)  on the quadrant u, v > 0 (this is a probability density: in the
coordinates t = u+v, w = u/t it reads C t e^{−Ct²/2} dt·dw on (0,∞)×(0,1)); so T := U+V has
Pr(T > t) = e^{−Ct²/2}, W := U/T is uniform on (0,1) and independent of T, and

   E U = E V = E[T]/2 = (1/2)∫_0^∞ e^{−Ct²/2} dt = √(π/(8C)).                                  (4.1)

Let  Λ_C(θ) := ln E e^{θU}  (finite for all θ ∈ ℝ, since U ≤ T has a Gaussian tail) and

   c(C) := sup_{θ > 0} ( θ − Λ_C(θ) ) ≥ 0,   with c(C) > 0  iff  E U < 1  iff  C > π/8.           (4.2)

(Cramér: θ − Λ_C(θ) = θ(1 − E U) − O(θ²) > 0 for small θ > 0 when E U < 1; conversely if E U ≥ 1 then
Λ_C(θ) ≥ θ E U ≥ θ by Jensen.)  Numerically c(0.5) = 0.011, c(0.6) = 0.036, c(0.8) = 0.109, c(1) = 0.201,
c(1.5) = 0.465, c(2) = 0.750, c(4) = 1.92 (log.md §6).

**Theorem 4.1 (corner-greedy embedding).**  For all r, h ≥ 1, k = rh, every π ∈ 𝒢(r,h) and every C > 0,
with N = Ck²,
   Pr( π ⊄ Π_N )  ≤  h·Pr( U_1 + ⋯ + U_r ≥ r ) + r·Pr( V_1 + ⋯ + V_h ≥ h )  ≤  h e^{−c(C) r} + r e^{−c(C) h},
where U_1, U_2, … (resp. V_1, V_2, …) are i.i.d. copies of U (resp. V).  In particular, for every fixed
C > π/8 ≈ 0.3927,  Pr(π ⊄ Π_N) → 0 as min(r,h) → ∞, uniformly over π ∈ 𝒢(r,h) — for instance for the
tilted grids and for all of 𝓕(r,h,ε) with r = h = √k:  Pr(fail) ≤ 2√k·e^{−c(C)√k}.

*Proof.*  *Step 1 (extended cell processes).*  For each cell (i,j) let Π^{(i,j)} be the point process on
ℝ² consisting of Π_N ∩ cell(i,j) together with an independent Poisson process of intensity N on
ℝ² \ cell(i,j).  Each Π^{(i,j)} is a Poisson process of intensity N on ℝ², and the k processes Π^{(i,j)}
are mutually independent (they are the restrictions of Π_N to disjoint cells, each completed by its own
independent process).

*Step 2 (the greedy).*  Process the cells in the order (i,s) lexicographic, i = 0..h−1, s = 0..r−1, the
(i,s)-th cell being (i, j) with j := τ_i(s).  Maintain a *row level* a ∈ ℝ, reset to a := i/h at the start
of row i, and *column levels* b_j ∈ ℝ, initialised b_j := j/r.  At cell (i,j) let p = p_{i,s} be the point
of Π^{(i,j)} in the open quadrant Q := {x > a, y > b_j} that minimises φ(x,y) := (x − a) + (y − b_j)
(a.s. unique and existing, since {φ < t} ∩ Q has finite area t²/2 and Π^{(i,j)} is a Poisson process
on the plane); put
   U_{i,s} := k·(x(p) − a),   V_{i,s} := k·(y(p) − b_j),
and update a := x(p), b_j := y(p).

*Step 3 (law of the increments).*  The levels (a, b_j) at cell (i,s) are functions of the processes of
the cells processed earlier, hence independent of Π^{(i,j)}.  Conditionally on them, Π^{(i,j)} ∩ Q is a
Poisson process of intensity N on the fixed quadrant Q, and by the Mecke formula the density of the
minimiser of φ at the point (a + u/k, b_j + v/k) (u, v > 0) is
   N·exp(−N·area{φ < (u+v)/k}) · (1/k²) du dv = (N/k²) exp(−(N/k²)(u+v)²/2) du dv = C e^{−C(u+v)²/2} du dv.
(The factor 1/k² is the Jacobian of (u,v) ↦ (a + u/k, b_j + v/k); area{φ < t} = t²/2.)  So, conditionally
on the past, (U_{i,s}, V_{i,s}) has the law of (U,V), whatever the past: the k vectors (U_{i,s}, V_{i,s})
are i.i.d. with the law of (U,V).

*Step 4 (the good event gives a copy).*  Let E be the event
   ∀i: Σ_{s<r} U_{i,s} < r     and     ∀j: Σ_{i<h} V_{i, τ_i^{-1}(j)} < h.
(The second sum runs over the h cells of column j, one per row, since every τ_i is a bijection.)  On E, by
induction along the processing order, every chosen point p_{i,s} lies in its cell (i, τ_i(s)) and hence
belongs to Π_N: indeed its x-coordinate is  i/h + (Σ_{s' ≤ s} U_{i,s'})/k < i/h + r/k = (i+1)/h  and
> a ≥ i/h, and its y-coordinate is  j/r + (Σ_{i' ≤ i} V_{i', τ_{i'}^{-1}(j)})/k < j/r + h/k = (j+1)/r
and > b_j ≥ j/r.  (If all earlier points lie in their cells, the current levels a, b_j are the coordinates
of points inside the current slab and strip, so the displayed identities hold.)
The k points p_{i,s} then form a copy of π_τ: they lie in distinct cells, so they are distinct.  x-order:
all points of row i lie in slab i, slabs are ordered by i, and within row i, x(p_{i,s}) > a = x(p_{i,s−1});
so the x-rank of p_{i,s} is ir + s.  y-order: p_{i,s} lies in strip j = τ_i(s), strips are ordered by j,
and within strip j the points are p_{i, τ_i^{-1}(j)}, i = 0..h−1, with y(p_{i,·}) > b_j = y of the
previous point of the column, so y increases with i; hence the y-rank of p_{i,s} is jh + i = π_τ(ir + s).
Therefore  Pr(π_τ ⊄ Π_N) ≤ Pr(E^c).

*Step 5 (tail).*  By Step 3 and the union bound over the h rows and r columns,
Pr(E^c) ≤ h Pr(Σ_{s<r} U_s ≥ r) + r Pr(Σ_{i<h} V_i ≥ h), and by Chernoff's bound
Pr(Σ_{s<r} U_s ≥ r) ≤ inf_θ e^{−θ r} (E e^{θU})^r = e^{−c(C) r}; the same for V (same law).  ∎

**Corollary 4.2 (the family 𝓕 is not a counterexample to Alon's conjecture).**  For every ε and every
π ∈ 𝓕(r,h,ε) ⊆ 𝒢(r,h), a uniformly random σ ∈ S_n with n ≥ 2Ck² (C > π/8) contains π with probability
≥ 1 − h e^{−c(C) r} − r e^{−c(C) h} − e^{−0.19 n}  (Remark 0.3); for r = h = √k this tends to 1, and
n = 0.8 k² suffices asymptotically.  In particular the residual family of the thread method ([W15]
Corollary 13, [W14]) has threshold ≤ (π/8 + o(1))k², below the identity's rigid-slab threshold k² and
within a factor π/2 of the value k²/4 conjectured for all patterns.

*Comments.*  (i) The proof uses nothing about τ except that each τ_i is a bijection; the rows may visit
the strips in any order.  By reflection in the diagonal (Pr(π ⊂ Π_N) = Pr(π^{-1} ⊂ Π_N)), the same bound
holds for the inverses, i.e. for patterns in which each *strip* visits the slabs in an arbitrary order
while each slab is increasing.  (ii) The choice φ = u + v is optimal among all "corner rules" that pick
the minimiser of a 1-homogeneous function ψ(u,v): for such a rule the minimiser p of ψ over
the Poisson points has density C e^{−C|R| ψ(u,v)²}, R := {ψ ≤ 1}, and one finds
E U = (3/2)√(π/(4C)) · (∫_R u du dv)/|R|^{3/2}; minimising the symmetric
functional ∫_R (u+v)/|R|^{3/2} over regions R gives the level set of u + v, i.e. the triangle.  (Squares
give C > 9π/64, quarter discs C > 4/π².)  (iii) The bound is a *threshold* statement (speed min(r,h)), not a
speed-N bound: one bad row (probability e^{−c r}) kills the greedy.  For bounded r Theorem 2.2 gives speed N
above its own threshold; for bounded h apply (i).  (iv) The union bound over 𝓕 is out of reach for any
per-pattern bound at N = O(k²) ([W15] Cor. 13, |𝓕| = e^{Θ(k ln k)}); the point of Theorem 4.1 is that each
member of 𝓕 individually has a small threshold, so 𝓕 cannot be a counterexample to n = O(k²), and the
obstruction it poses is only to the *method* (union bounds over shift-chain hypotheses).

### 4.3 Free slabs: the row part at speed k

The slabs in Theorem 4.1 were only used to make the cells disjoint.  They can be dropped (the strips are
kept), at the price of a "fresh quadrant" lemma.

**Lemma 4.3 (fresh quadrant).**  Let Π be a Poisson process of intensity N on ℝ², let Q = {x > a, y > b}
be a fixed open quadrant, φ(x,y) := (x − a) + (y − b), p* the a.s. unique minimiser of φ on Π ∩ Q, and
Δ(p) := {(x,y) ∈ Q : φ(x,y) ≤ φ(p)} the closed triangle below p.  Then for all measurable g ≥ 0 on ℝ² and
F ≥ 0 on point configurations,
   E[ g(p*) F(Π ∩ (Q ∖ Δ(p*))) ] = ∫_Q g(p) e^{−N|Δ(p)|} E[ F(Π ∩ (Q ∖ Δ(p))) ] N dp.
In words: p* has density N e^{−N|Δ(p)|} = N e^{−Nφ(p)²/2} on Q, and conditionally on p* = p the process
outside the explored triangle, Π ∩ (Q ∖ Δ(p)), is a Poisson process of intensity N on Q ∖ Δ(p).

*Proof.*  p* is the unique point p ∈ Π ∩ Q with Π ∩ Δ°(p) = ∅ (Δ° the interior of the triangle, i.e.
{φ < φ(p)} ∩ Q), so the left side equals E Σ_{p ∈ Π ∩ Q} 1{Π ∩ Δ°(p) = ∅} g(p) F(Π ∩ (Q ∖ Δ(p))).  By the
Mecke equation this is ∫_Q E[1{Π ∩ Δ°(p) = ∅} g(p) F(Π ∩ (Q ∖ Δ(p)))] N dp (adding the point p to Π does
not change Π ∩ Δ°(p) nor Π ∩ (Q ∖ Δ(p)), since p ∉ Δ°(p) and p ∈ Δ(p)).  The sets Δ°(p) and Q ∖ Δ(p) are
disjoint, so the indicator and F(…) are independent, and Pr(Π ∩ Δ°(p) = ∅) = e^{−N|Δ(p)|}.  ∎

**Theorem 4.4 (rigid strips, free slabs).**  For all r, h ≥ 1, k = rh, π ∈ 𝒢(r,h), C > 0 and N = Ck²,
   Pr( π ⊄ Π_N )  ≤  Pr( U_1 + ⋯ + U_k ≥ k ) + r·Pr( V_1 + ⋯ + V_h ≥ h )  ≤  e^{−c(C) k} + r e^{−c(C) h},
and by reflection in the diagonal also  Pr(π ⊄ Π_N) ≤ e^{−c(C)k} + h e^{−c(C) r}.

*Proof.*  For each strip j let Π^{(j)} := (Π_N ∩ S_j) ∪ (independent Poisson process of intensity N on
ℝ² ∖ S_j), S_j = [0,1] × [j/r, (j+1)/r): independent Poisson processes of intensity N on ℝ².  Run the
greedy of Theorem 4.1 with the following changes: the row level a is initialised a := 0 once and is *not*
reset between rows; at the (i,s)-th step (j = τ_i(s)) the search is over Π^{(j)} ∩ Q_{i,s}, Q_{i,s} := {x > a,
y > b_j}, minimising φ = (x − a) + (y − b_j); define U_{i,s} := k(x(p) − a), V_{i,s} := k(y(p) − b_j) and
update a := x(p), b_j := y(p) as before.
*Increments are i.i.d.*  Fix j.  The searches in Π^{(j)} are those of the h cells of column j, at steps
(i, τ_i^{-1}(j)), i = 0, …, h−1.  Let (a, b_j) be the corner of the m-th such search and Δ_m the closed
triangle it explores (the one of Lemma 4.3 for its corner and minimiser).  For m' < m the corner of the
m-th search satisfies a ≥ x(p_{m'}) and b_j ≥ y(p_{m'}) (a is the x-coordinate of the most recent point
of the whole construction, which is to the right of p_{m'}; b_j = y(p_{m−1}) ≥ y(p_{m'}) by the column
chain), hence every point of Q_m satisfies φ_{m'} > φ_{m'}(p_{m'}): Q_m ∩ Δ_{m'} = ∅.  Now condition on the
whole past of the construction before the m-th search in Π^{(j)}.  That past is a function of the other
processes Π^{(j')}, j' ≠ j (independent of Π^{(j)}), and of the earlier searches in Π^{(j)}; applying
Lemma 4.3 inductively to the earlier searches (the (m−1)-th search is over the quadrant Q_{m−1}, on which
Π^{(j)} is conditionally Poisson by the induction hypothesis; the lemma then makes Π^{(j)} conditionally
Poisson on Q_{m−1} ∖ Δ_{m−1}, and Q_m ⊆ Q_{m−1} ∖ Δ_{m−1} is a function of the past), the conditional law of
Π^{(j)} ∩ Q_m given the past is that of a Poisson process of intensity N on Q_m.  Hence, exactly as in Step 3 of Theorem 4.1, (U, V) of the
m-th search has the law of (U,V) of (4.1) conditionally on the past.  Thus all k vectors (U_{i,s},
V_{i,s}) are i.i.d.
*Good event.*  Let E := { Σ_{(i,s)} U_{i,s} < k } ∩ { ∀j: Σ_{i<h} V_{i,τ_i^{-1}(j)} < h }.  On E, inductively,
every chosen point has x-coordinate  Σ_{(i',s') ≤ (i,s)} U/k < 1 and y-coordinate in [j/r, j/r + h/k)
= S_j, so it is a point of Π_N.  The x-order of the chosen points is the processing order (each point is
to the right of its predecessor), the y-order is by strip, then by column chain: as in Step 4 of Theorem
4.1 the points form a copy of π_τ.  Finally Pr(E^c) ≤ Pr(Σ_{t<k} U_t ≥ k) + r Pr(Σ_{i<h} V_i ≥ h) and Chernoff
gives the exponentials.  ∎

*Comments.*  (i) For r = h = √k the bound is e^{−c(C)k} + √k e^{−c(C)√k}; the column term is the bottleneck.
(ii) The threshold constant is unchanged (π/8), because free slabs do not change the mean increment; they
only let the row fluctuations average over all k steps.  (iii) Theorem 4.4 with C = 1 and r ≤ h gives
Pr(π ⊄ Π_{k²}) ≤ e^{−0.2k} + r e^{−0.2h} ≤ (r+1) e^{−0.2h} = (r+1)e^{−0.2k/r} for every π ∈ 𝒢(r,h),
which for r ≤ k/(6 ln k) is ≤ (r+1) k^{−1.2}: this covers, per pattern, every block-grid pattern with
r ≤ k/(6 ln k), with a threshold (N = k²) independent of r.
