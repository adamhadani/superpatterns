# W90 — Layered patterns are harder than the identity: block-flip theorem, exact deficit identity, and numerical evidence that c₂₁ < 1

Date: 10 November 2026. Status of each item is stated explicitly; nothing here is claimed beyond its label.

**Summary.** Let L₂₁(σ) be the largest m such that σ contains 21^{⊕m} = 2 1 4 3 … (2m)(2m−1), and
c₂₁ = lim L₂₁(σ_n)/√n. Alon's conjecture (a uniform σ_n with n = (1+ε)k²/4 contains every pattern of length k,
for every fixed ε > 0) requires c₂₁ ≥ 1.

| Item | Statement | Status |
|:--|:--|:--|
| Theorem 1 | For all patterns α, β and all n: #{σ∈S_n ⊇ α⊕21⊕β} ≤ #{σ∈S_n ⊇ α⊕12⊕β}, with an exact formula for the difference | **Proved** (§2), brute-force checked n ≤ 8 (§5) |
| Corollary 2 | P(σ_n ⊇ 21^{⊕m}) ≤ P(LIS(σ_n) ≥ 2m) for all n, m; hence L₂₁ ≤_st ⌊LIS/2⌋ and **c₂₁ ≤ 1** | **Proved** (prior rigorous bound in this repo: 1.140, W12) |
| Proposition 4 | Equality in Theorem 1 when α or β is empty; smallest defect is a 3-point lens with conditional weight 1/3; first discrepancy for 21^{⊕3} vs 123456 is exactly one permutation at n = 9 | **Proved** / exhaustively verified |
| Numerical finding | E⌊LIS/2⌋ − E L₂₁ = (0.00113 ± 0.00002)·√n for n = 10³ … 10⁸, i.e. **c₂₁ ≈ 0.99887 < 1** | **Numerical** (1.29·10⁶ paired samples, plus 8.1·10⁴ from an independent program and RNG); not a proof |
| Consequence | If c₂₁ < 1 then Alon's conjecture is false: 21^{⊕k/2} needs n ≥ k²/(4c₂₁²) ≈ 1.0023·k²/4 | Conditional on the numerical finding |
| Open | Rigorous proof that liminf (E⌊LIS/2⌋ − E L₂₁)/√n > 0 | **Open** — reduced in §4 to positivity of an explicit non-negative local quantity |

Prior art for the inequality: Bóna (|Av_n(1234)| < |Av_n(1324)|, n ≥ 7); Burstein–Pantone, *Two examples of
unbalanced Wilf-equivalence* (1234 ∼ {1324, 3416725}), arXiv:1402.3842; Jelínek–Karpilovskij, *Fillings of skew
shapes avoiding diagonal patterns*, DMTCS 22:2 (2021), arXiv:2002.12308 (for every skew shape, #fillings avoiding
δ₂ = #fillings avoiding ι₂ and φ_D; they conjecture the analogous inequality for chains of every size k and note
it is known only for k ≤ 2). Theorem 1 is the transversal case k = 2 in the language of patterns; the short proof
below is self-contained. Backelin–West–Xin (I_k ⊕ τ ∼ J_k ⊕ τ) gives the equality case. No priority is claimed for
Theorem 1. I found no prior statement of the asymptotic consequence for random permutations or of its relevance
to Alon's conjecture (searches 10 Nov 2026; see log.md).

--------------------------------------------------------------------------------------------------
## 1. Setting and notation

A *configuration* is a finite set P ⊂ ℝ² with pairwise distinct x-coordinates and pairwise distinct
y-coordinates; σ ∈ S_n is identified with P_σ = {(i, σ(i))}. For z, w ∈ ℝ² write z < w if both coordinates are
strictly smaller. A set Q of points *contains* a pattern γ if some |γ| of its points are order-isomorphic to γ
(every set contains the empty pattern). For z ∈ ℝ² put SW(z) = {p ∈ P : p < z}, NE(z) = {p ∈ P : p > z}.
For a NW of b (x_a < x_b, y_a > y_b) the *corners* of the pair are a∧b = (x_a, y_b) and a∨b = (x_b, y_a).

Fix patterns α, β (possibly empty) and define

  U = U_α(P) = {z ∈ ℝ² : SW(z) contains α},   S = S_β(P) = {z ∈ ℝ² : NE(z) contains β}.

U is an up-set (z ∈ U, z ≤ z′ ⇒ z′ ∈ U), S is a down-set; U = ℝ² if α = ∅ and S = ℝ² if β = ∅.
The *inside points* are I = P ∩ U ∩ S, the *outside points* O = P ∖ I. Let X, Y be the sets of x- and
y-coordinates of I, and N = |I|. The *board* is D = {(x, y) ∈ X × Y : (x, y) ∈ U_α(O) ∩ S_β(O)}.
A *valid filling* is a bijection f : X → Y whose graph Γ_f lies in D. A *D-inversion* of f is a pair a, b ∈ Γ_f,
a NW of b, with a∧b ∈ U_α(O) and a∨b ∈ S_β(O).

## 2. The block-flip theorem

**Lemma 1 (reading the middle block).** P contains α⊕12⊕β iff there are p < q in P with p ∈ U and q ∈ S; in that
case p, q ∈ I. P contains α⊕21⊕β iff there are a, b ∈ P, a NW of b, with a∧b ∈ U and a∨b ∈ S; in that case a, b ∈ I.

*Proof.* A copy of α⊕B⊕β (B a 2-point block) is A ∪ {two points} ∪ B′ with A a copy of α, B′ a copy of β, every
point of A below-left of both middle points and every point of B′ above-right of both. For B = 12 with middle
points p < q: "A < p and A < q" is "A ⊂ SW(p)", so a suitable A exists iff p ∈ U; likewise B′ exists iff q ∈ S.
Then p < q ∈ S gives p ∈ S and q > p ∈ U gives q ∈ U, so both are inside. For B = 21 with a NW of b: "A < a and
A < b" is "A < a∧b", i.e. A ⊂ SW(a∧b); "B′ > a and B′ > b" is B′ ⊂ NE(a∨b). Then a∧b ≤ a ≤ a∨b (coordinatewise,
weakly) gives a ∈ U ∩ S since U is an up-set and S a down-set; same for b. ∎

**Lemma 2 (U and S are determined by the outside points).** U_α(P) = U_α(O) and S_β(P) = S_β(O).

*Proof.* ⊇ holds because O ⊂ P. Let z ∈ U_α(P), α ≠ ∅, and among the copies of α inside SW(z) choose one, A, whose
rightmost point has the smallest x-coordinate. If A contained an inside point p, then p ∈ U_α(P) gives a copy A′ of
α inside SW(p) ⊂ SW(z), all of whose points lie strictly to the left of p, contradicting the choice of A. So A ⊂ O
and z ∈ U_α(O). The statement for S is the mirror image. ∎

**Lemma 3 (fibres).** Let f be any valid filling of the board D of P and put P_f = O ∪ Γ_f. Then the outside points
of P_f are exactly O, its inside points are exactly Γ_f, and U_α(P_f) = U_α(O), S_β(P_f) = S_β(O). Consequently the
set of configurations having outside points O and inside coordinate sets X, Y is {P_f : f a valid filling of D}.

*Proof.* Points of Γ_f lie in U_α(O) ∩ S_β(O) ⊂ U_α(P_f) ∩ S_β(P_f), so they are inside for P_f. Let o ∈ O. By
Lemma 2 for P, o ∉ U_α(O) ∩ S_β(O); say o ∉ U_α(O) (the other case is symmetric). Suppose o ∈ U_α(P_f), witnessed
by a copy A ⊂ SW(o) in P_f. If A ⊂ O then o ∈ U_α(O), impossible; so A contains some g ∈ Γ_f, and g ∈ U_α(O)
gives a copy A′ ⊂ O of α with A′ < g < o, again o ∈ U_α(O). Hence o is outside for P_f. The last claims follow
from Lemma 2 applied to P_f, and P itself is P_f for the bijection f it induces. ∎

**Lemma 4 (two sorting arguments).** Let D be the board of some configuration and suppose D has a valid filling.
(i) The decreasing bijection f_dec is a valid filling, and it is the only valid filling without an increasing pair.
(ii) D has at least one valid filling without a D-inversion.

*Proof.* (i) If a valid f has an increasing pair p < q in Γ_f, replace p, q by p′ = (x_p, y_q), q′ = (x_q, y_p).
Both lie in the rectangle [p, q]; they are ≥ p ∈ U_α(O) and ≤ q ∈ S_β(O), hence in D. The new bijection is valid
and has strictly more inversions; iterate until no increasing pair remains. (ii) If a valid f has a D-inversion
(a, b), replace a, b by a∧b and a∨b. Now a∧b ∈ U_α(O) by assumption and a∧b ≤ a ∈ S_β(O); a∨b ∈ S_β(O) by
assumption and a∨b ≥ a ∈ U_α(O). So the new bijection is valid, and it has strictly fewer inversions; iterate. ∎

**Theorem 1 (block flip).** For all patterns α, β (possibly empty) and every n,

  #{σ ∈ S_n : σ ⊇ α⊕12⊕β} − #{σ ∈ S_n : σ ⊇ α⊕21⊕β} = Σ_φ (a(φ) − 1) ≥ 0,

where φ runs over the fibres of σ ↦ (O, X, Y) with I ≠ ∅ and a(φ) ≥ 1 is the number of valid fillings of the
board of φ that have no D-inversion. Equivalently, for uniform σ_n,

  P(σ_n ⊇ α⊕12⊕β) − P(σ_n ⊇ α⊕21⊕β) = E[ (a − 1)/F ],        (★)

F = number of valid fillings of the fibre of σ_n (the conditional law of σ_n given its fibre is uniform on it).

*Proof.* By Lemma 3 the fibre of P is in bijection with the valid fillings of its board, and U, S are the same
for all members. By Lemma 1 a member P_f contains α⊕12⊕β iff Γ_f has an increasing pair, i.e. (Lemma 4(i)) iff
f ≠ f_dec; and it contains α⊕21⊕β iff f has a D-inversion. So a fibre with F members has F − 1 members containing
the first pattern and F − a containing the second; the difference is a − 1 ≥ 0 by Lemma 4(ii). Fibres with I = ∅
contain neither pattern. ∎

**Corollary 2.** For all n and m, P(σ_n ⊇ 21^{⊕m}) ≤ P(LIS(σ_n) ≥ 2m). Hence L₂₁(σ_n) is stochastically dominated
by ⌊LIS(σ_n)/2⌋, E L₂₁(σ_n) ≤ E⌊LIS(σ_n)/2⌋, and c₂₁ ≤ 1. More generally, in any direct sum of blocks, replacing
blocks 12 by 21 never increases the containment probability.

*Proof.* Apply Theorem 1 m times with α = 12^{⊕(m−1−i)}, β = 21^{⊕i}, i = 0, …, m−1. For the constant use
E LIS(σ_n)/√n → 2 (Logan–Shepp, Vershik–Kerov) and the existence of c₂₁ (W5 Lemma B). ∎

**Corollary 3 (exact deficit).** With H_i(m) = P(σ_n ⊇ 12^{⊕(m−i)} ⊕ 21^{⊕i}),

  E⌊LIS(σ_n)/2⌋ − E L₂₁(σ_n) = Σ_{m≥1} (H_0(m) − H_m(m)) = Σ_{m≥1} Σ_{i=0}^{m−1} E[(a − 1)/F]_{α=12^{⊕(m−1−i)}, β=21^{⊕i}},

a sum of non-negative terms; the terms with i = 0 or i = m − 1 vanish (Proposition 4(a)).

## 3. Equality cases and the smallest defect

**Proposition 4.** (a) If α = ∅ or β = ∅ then a(φ) = 1 for every fibre, so equality holds in Theorem 1
(this is the k = 2 case of Backelin–West–Xin). (b) If N ≤ 2 then a = 1. (c) If N = 3 then a = 2 exactly when
D = X × Y minus the two cells (x₁, y₁) and (x₃, y₃) (x₁<x₂<x₃, y₁<y₂<y₃), i.e. the lowest-left cell is not in U and
the highest-right cell is not in S; then F = 3 (fillings 321, 231, 312), the two D-inversion-free fillings are 231
and 312, and the fibre contributes (a − 1)/F = 1/3 to (★). Otherwise a = 1.

*Proof.* (a) Let α = ∅, so U = ℝ² and a D-inversion is an inversion (a, b) with a∨b ∈ S. Let f be valid and
D-inversion-free, let y* = max Y and let (x_j, y*) ∈ Γ_f. The cells of row y* lying in D form an initial segment
x₁, …, x_t of the columns (S is a down-set). For i > j the point of column x_i lies below-right of (x_j, y*), so
(x_i, y*) ∉ S; with (x_j, y*) ∈ S this forces j = t. Remove row y* and column x_t; the rest is again a board of
the same kind with a D-inversion-free filling, and induction shows f is unique. The case β = ∅ is the mirror image.
(b), (c): exhaustive enumeration of all boards S ∩ U inside [N]² for N ≤ 3 (`skew_boards.py`). ∎

Geometrically (c) says: ∂U has an outer notch and ∂S has an outer notch facing each other, and three free points sit
around them so that the inversion pair "straddles" the notch of U (its corner a∧b falls into the explored region) —
each of its points is usable as the next point of an increasing continuation, but the pair is not usable as the
next 21 block. For α = β = 1 the smallest instance is n = 7 (the fibre of 3416725, cf. Burstein–Pantone); for
α = β = 21 it is n = 9, giving |Av₉(214365)| = |Av₉(123456)| + 1.

## 4. What is not proved: strict asymptotic deficit

Write D(n) = 2(E⌊LIS(σ_n)/2⌋ − E L₂₁(σ_n)) ≥ 0. Since E⌊LIS/2⌋/√n → 1 and E L₂₁/√n → c₂₁,

  c₂₁ = 1 − lim_{n→∞} D(n)/(2√n).

So **c₂₁ < 1 ⟺ lim D(n)/√n > 0**, and by Corollary 3 D(n) is an explicit sum of non-negative local terms
E[(a−1)/F]. The heuristic reason the sum is of order √n: the i-th flip contributes only when the region
U ∩ S between the level-2(m−1−i) "front" from the south-west and the level-i front from the north-east is a few
small lenses, which for each i happens for O(1) values of m, and then a defect lens as in Proposition 4(c) is
present with probability bounded below; there are ≍ √n values of i. This is consistent with the data in §5 but
is **not** proved here. A proof needs a lower bound, uniform over a positive fraction of the stages, on the
probability that the marginal region consists of one defect lens plus harmless lenses (lenses with at most one
free point contribute a factor 1). The missing ingredient is a tightness statement for the number of free points
within a bounded number of levels of the maximum ("near-maximiser tightness"), or a softer substitute.

## 5. Verification and numerical evidence

**Exhaustive counts** (`exact_dist.c`, all of S_n; `#{L₂₁ ≥ m}` vs `#{⌊LIS/2⌋ ≥ m}`): identical for n ≤ 8; the
deficits #{⌊LIS/2⌋ ≥ m} − #{L₂₁ ≥ m} are

| n | m = 3 | m = 4 | E⌊LIS/2⌋ − E L₂₁ |
|--:|--:|--:|--:|
| 9 | 1 | 0 | 2.8·10⁻⁶ |
| 10 | 66 | 0 | 1.8·10⁻⁵ |
| 11 | 2 565 | 2 | 6.4·10⁻⁵ |
| 12 | 77 232 | 213 | 1.6·10⁻⁴ |

All deficits are ≥ 0 (Corollary 2) and m = 2 is exact (2143 ∼ 1234), as Proposition 4(a) predicts.

**Fibre identity** (`verify_fibers.py`): for (α, β) ∈ {(1,1), (21,21), (12,12), (1,21), (132,1), (231,21), (∅,1)}
and all σ ∈ S_n, n ≤ 8 (and (21,21) at n = 9), the script recomputes U, S, the fibres and the boards from the
definitions and checks Lemma 1, Lemma 3, Lemma 4 and the identity of Theorem 1 with no exceptions. It reproduces
|Av₇(1324)| − |Av₇(1234)| = 1 and |Av₈(1324)| − |Av₈(1234)| = 26 = 15793 − 15767.

**Paired simulation for 21^{⊕m}** (`l21_paired.c`, xoshiro256** permutations; L₂₁ and LIS on the same σ_n):

| n | samples | E LIS | E L₂₁ | D(n) = E[2⌊LIS/2⌋ − 2L₂₁] | D(n)/√n |
|--:|--:|--:|--:|--:|--:|
| 10³ | 700 000 | 58.1748 | 28.8003 | 0.0736 ± 0.0040 | 0.00233 ± 0.00013 |
| 10⁴ | 420 000 | 192.2978 | 95.7774 | 0.2412 ± 0.0079 | 0.00241 ± 0.00008 |
| 10⁵ | 140 000 | 620.9003 | 309.8561 | 0.688 ± 0.021 | 0.00218 ± 0.00007 |
| 10⁶ | 28 000 | 1982.8267 | 990.0109 | 2.304 ± 0.070 | 0.00230 ± 0.00007 |
| 10⁷ | 2 800 | 6298.9221 | 3145.7750 | 6.88 ± 0.34 | 0.00218 ± 0.00011 |
| 10⁸ | 150 | 19960.8067 | 9969.6467 | 20.96 ± 2.18 | 0.00210 ± 0.00022 |

Weighted mean D(n)/√n = 0.002269 ± 0.000036 (χ² = 7.1 on 5 d.o.f., p ≈ 0.21); a pure power law D ∝ n^b fitted to
the six points has b = 0.491 ± 0.006 (1.5 standard errors from ½; the alternatives b = 1/3 and b = 1/6, which
would leave c₂₁ = 1, are excluded at more than 25 standard errors). Table: `out/l21_table.txt`. Hence, numerically, c₂₁ = 1 − 0.00113 ± 0.00002 ≈ 0.99887 and the containment threshold of
21^{⊕k/2} is k²/(4c₂₁²) ≈ 1.0023·k²/4.

The L₂₁ sweep was validated against an O(n³) dynamic programme on 180 000 random permutations (n ≤ 60) and against
the exhaustive counts above. **Independent cross-check** (`crosscheck_w40.py`): numpy PCG64 permutations, L₂₁
computed by both `l21_paired.c` and the independently written W40 `pruned.c` (0 disagreements on 81 240
permutations), LIS in pure Python: D(10⁴) = 0.238 ± 0.019, D(10⁵) = 0.774 ± 0.081, D(10⁶) = 3.4 ± 0.8.

**Other layered patterns** (`layered_paired.c`; periodic layer sizes; D = E[K_I − K], where K is the length of the
longest contained prefix made of complete layers and K_I the same for the increasing pattern cut into blocks of
the same sizes). See `out/family_table.txt` for the full table; D/√n at n = 10⁴ / 10⁵:

| layer sizes | 2 | 3 | 4 | 5 | 6 | 1,2 | 1,3 | 1,4 | 2,3 | 1,1,2 | 1,1,1,2 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| D/√n ·10³ | 2.8 / 2.4 | 5.2 / 5.0 | 7.5 / 7.5 | 9.3 / 9.6 | 10.5 / 10.4 | 1.9 / 1.7 | 3.8 / 3.4 | 5.4 / 5.6 | 3.6 / 3.8 | 1.3 / 1.3 | 0.65 / 1.15 |

(standard errors ≈ 0.3·10⁻³; n = 10⁶ values agree, see the table file). Larger layers at n = 10⁵:
size 8: 12.4 ± 0.7, size 10: 13.5 ± 1.0, size 12: 14.2 ± 1.3, size 16: 16.7 ± 2.1 (·10⁻³). The deficit is positive
for every family tested, roughly additive in the number of non-trivial layers, and still increasing with the
layer size at 16; e.g. layers of size 6 would need n ≈ 1.0105·k²/4 and layers of size 12 about 1.014·k²/4. The
hardest layered pattern has not been located.

**The fibre formula at scale** (`fibre_cost.py`, `out/fibre_table.txt`). Written as E[X − Y] = E Σ_{b≥Y−1}(1 − 1/a_b), the
exact identity can be evaluated stage by stage by brute force over fillings. On all of S₈ and S₉ it reproduces
Σ(LIS − N) exactly (1 and 46). At n = 10⁴, flips 1…63, 120 000 permutations: formula 0.15641 ± 0.00083 against
0.153 ± 0.012 measured directly on the same permutations. Each stage contributes 0.0024–0.0027; contributing levels
have a = 2 and 3–8 inside points (3 points in 20% of the cases).

**Cost per flipped block** (`hybrid_profile.c`, `out/hybrid_table.txt`): for the pattern 21^{⊕i} ⊕ 1 ⊕ 1 ⊕ …,
E[LIS − N_i] is linear in i with slope ≈ 0.0025 per block at n = 10⁴ (i ≤ 64) and n = 10⁵ (i ≤ 192), and 0 within
error at i = 1 (the equality case). For layer sizes ≥ 3 the inequality itself is only conjectural (Jelínek–Karpilovskij conjecture
for k ≥ 3); the data are consistent with it.

## 6. Reproduction

```sh
cd experiments/w90-layered-deficit
cc -O2 -o /tmp/exact_dist exact_dist.c && for n in 9 10 11 12; do /tmp/exact_dist $n; done
cc -O2 -o /tmp/l21_paired l21_paired.c -lm && /tmp/l21_paired 60 20000 1 v      # brute-force validation
/tmp/l21_paired 1000000 4000 1                                                   # one paired batch
cc -O2 -o /tmp/layered_paired layered_paired.c -lm && /tmp/layered_paired 3 16 3000 1 v
python3 verify_fibers.py 8 ; python3 skew_boards.py
python3 fibre_cost.py exact 8 ; python3 fibre_cost.py mc 10000 200 1 64 60     # exact identity, stage by stage
python3 aggregate.py ; python3 aggregate_family.py                               # tables from out/
```
