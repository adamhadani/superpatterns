# W14 — the entropy lemma (E) is false; structure of shift chains of run-unions

Date: 2026-08-29.  Everything in this file is proved in full.  Numerics, heuristics and the exact
remaining gap are in log.md.  Notation as in [W13] (work/w13-global-event/proof.md) and [W9]
(work/w9-alon-threads/proof.md).

## 0. Setting

π ∈ S_k is 0-indexed.  π ∈ 𝓛_r means: the values [k] = {0,…,k−1} are split into ≤ r intervals
V_1 < V_2 < ⋯ < V_r (V_j = [S_j, S_j + h_j), S_1 = 0, S_{j+1} = S_j + h_j) such that
p := π^{-1} is increasing on each V_j.  Write w ∈ [r]^k for the *interleaving word*, w(a) = j iff
π(a) ∈ V_j; given the sizes (h_j), w determines π (the positions carrying letter j receive the values
of V_j in increasing order) and distinct words give distinct π.

For Δ ≥ 1 the map b(a) := p(π(a) − Δ) is defined on {a : π(a) ≥ Δ}; a Δ-shift chain is a set A on
which b is increasing, and L_Δ(π) = max |A| ([W9] §0; this equals HK's LIS definition because a
partial injection and its inverse have the same longest increasing subsequence).  As in [W13] §4,
ℓ_r := ⌈(ln r + 1)/29⌉, λ_r := (ℓ_r − 1)(ln r + 10), T_r := L(r, ℓ_r) = ⌈k/λ_r⌉,
F(π) := {Δ ∈ [k] : L_Δ(π) > T_r}, and

  j(π) := max { |T| : T ⊆ {0,1,…,k}, t − t' ∉ F(π) for all t ≠ t' ∈ T }

(the largest number of mutually good shifts).  Note L_k(π) = 0, so {0, k} is always mutually good and
j(π) ≥ 2.  The lemma (E) of [W13] log §4 reads: for every j ≥ 1,
#{π ∈ 𝓛_r : j(π) ≤ j} ≤ e^{(29j − 1)k}.

## 1. Shift chains of run-unions

For Δ ≥ 1 and 1 ≤ j' ≤ j ≤ r put  B_{j,j'}(Δ) := V_j ∩ (V_{j'} + Δ) = {v ∈ V_j : v − Δ ∈ V_{j'}}.
This is an interval of values (intersection of two intervals), of size
β_{j,j'}(Δ) := ( min(S_j + h_j, S_{j'} + h_{j'} + Δ) − max(S_j, S_{j'} + Δ) )^+,
and the nonempty blocks partition the value set [Δ, k).

**Lemma 1 (structure of L_Δ on 𝓛_r).**  Let π ∈ 𝓛_r with sizes (h_j) and word w.
(a) (Chains as value sets.)  A ⊆ [k] is a Δ-shift chain iff, with U := π(A) ⊆ [Δ, k), the two maps
    v ↦ p(v) and v ↦ p(v − Δ) induce the same linear order on U.  Hence L_Δ(π) is the length of the
    longest increasing subsequence of the sequence Q_Δ := (p(v − Δ))_{v ∈ [Δ,k)} listed in increasing
    order of p(v) (computable in O(k log k)).
(b) (Free chains.)  For every block, π^{-1}(B_{j,j'}(Δ)) is a Δ-shift chain.  Consequently

      L_Δ(π) ≥ β_Δ(π) := max_{j' ≤ j} β_{j,j'}(Δ),

    a quantity depending only on the interval sizes (h_j), not on the word w.  In particular, if
    S_j − S_{j'} = D then L_Δ(π) ≥ min(h_j, h_{j'}) − |Δ − D| for all Δ, and L_Δ(π) ≥ h_j − Δ.
(c) (Periodic words.)  Let k = rh, all h_j = h and w = (1 2 ⋯ r)^h (π is the "tilted grid",
    π(ir + j) = jh + i for 0 ≤ i < h, 0 ≤ j < r, runs and letters 0-indexed).  Then for
    Δ = dh + e with 0 ≤ d < r, 0 ≤ e < h,

      L_Δ(π) = max( (h − e)(r − d), e(r − d − 1) ).

    In particular L_Δ(π) ≥ (h/2)(r/2 − 1) ≥ k/4 − h/2 for every Δ ≤ k/2, and π^{-1} is the tilted
    grid with the roles of (r, h) exchanged (π^{-1}(jh + i) = ir + j), so the same holds for π^{-1}.

*Proof.*  (a) b(a) = p(π(a) − Δ), and a = p(π(a)).  Writing v = π(a), A is a chain iff for
v, v' ∈ U: p(v) < p(v') ⇒ p(v − Δ) < p(v' − Δ); as both maps are injective this is the statement
that they induce the same order on U.  Listing U by increasing p(v), the sequence p(v − Δ) must be
increasing, so chains of value set U correspond to increasing subsequences of Q_Δ and conversely.

(b) On B = B_{j,j'}(Δ) the map v ↦ p(v) is increasing (p is increasing on V_j ⊇ B) and so is
v ↦ p(v − Δ) (p is increasing on V_{j'} ∋ v − Δ).  By (a), π^{-1}(B) is a chain, of size
β_{j,j'}(Δ).  The formula for β_{j,j'} is the length of the intersection of [S_j, S_j + h_j) and
[S_{j'} + Δ, S_{j'} + h_{j'} + Δ); with S_j − S_{j'} = D this is ≥ min(h_j, h_{j'}) − |Δ − D|, and
j = j' gives h_j − Δ.

(c) Positions are a = ir + j (0 ≤ i < h, 0 ≤ j < r), π(a) = jh + i, and p(j'h + i') = i'r + j'.
For Δ = dh + e:  if i ≥ e then π(a) − Δ = (j − d)h + (i − e), defined iff j ≥ d, and
b(a) = (i − e)r + (j − d) = a − (er + d);  if i < e then π(a) − Δ = (j − d − 1)h + (i − e + h),
defined iff j ≥ d + 1, and b(a) = (i − e + h)r + (j − d − 1) = a + (h − e)r − d − 1.
Let G_1 := {ir + j : i ≥ e, j ≥ d} (|G_1| = (h − e)(r − d)) and G_2 := {ir + j : i < e, j ≥ d + 1}
(|G_2| = e(r − d − 1)); b is a translation on each, hence increasing on each.  Every element of G_2
is a position < er and every element of G_1 is a position ≥ er.  For a' ∈ G_2, a ∈ G_1 (so a' < a):
b(a) − b(a') = (a − a') − er − d − (h − e)r + d + 1 = a − a' − (k − 1) ≤ 0, so no chain contains both
an element of G_2 and an element of G_1.  Hence every chain lies in G_1 or in G_2, and both are
chains: L_Δ = max(|G_1|, |G_2|).  For Δ ≤ k/2 we have d ≤ r/2; if e ≤ h/2 then
(h − e)(r − d) ≥ (h/2)(r/2), otherwise e(r − d − 1) ≥ (h/2)(r/2 − 1).  The formula for π^{-1} is
immediate from π(ir + j) = jh + i.  ∎

*Remark.*  (b) is the whole point: two increasing runs whose value intervals are (nearly) translates
of each other by Δ produce a Δ-chain of length ≈ min(h_j, h_{j'}) *whatever the interleaving is*.
The chain length L_Δ therefore carries no information about the word w beyond the sizes, and no
compression/decoding argument on w can bound the number of π with such chains.  This is what kills
(E), as follows.

## 2. (E) is false

**Theorem 2.**  Let r ≥ e^{75} and let k be large enough that r ≤ k/(2 ln(k+1)) (the range of
[W13] Theorem 5).  Then

  #{ π ∈ 𝓛_r : j(π) = 2 }  ≥  exp( (1 − θ_r) k ln r − k/2 − 16 ln r ),   θ_r := 2.08 (√(λ_r + 8) + 1)/λ_r,

and θ_r ≤ 0.176, so the left side is ≥ e^{61.3 k} > e^{57 k}.  In particular (E) fails for j = 2, and
the patterns in question have ℓ_r ≥ 3, so they are exactly the (G1)-patterns of [W13] log §4: they
are not covered by [W13] Theorem 5, and no entropy bound of the form (E) can cover them.

*Proof.*  Write λ := λ_r and T := T_r = ⌈k/λ⌉.  Since ln r ≥ 75, ℓ_r ≥ 3 and λ ≥ 2(ln r + 10) ≥ 170;
also λ ≤ (ln r/29 + 1)(ln r + 10) ≤ ln² k, so k ≥ 50λ once k ≥ e^{75} (which holds as k ≥ r).

*Construction.*  Put h := 2T + 2, g := 2T + 3 (= h + 1), U := ⌈(k/2 − T − 1)/g⌉, a := ⌈√(U + 1)⌉,
and let M := {0, 1, …, a − 1} ∪ {ia − 1 : 2 ≤ i ≤ a}, so |M| ≤ 2a − 1 =: r'.
(M is a sparse ruler: every d ∈ [1, a² − 1] is a difference of two elements of M — for d ≤ a − 1
take d − 0; for a ≤ d ≤ a² − 1 put i := ⌊d/a⌋ + 1 ∈ [2, a] and x := ia − 1 − d = a − 1 − (d mod a)
∈ [0, a − 1], so d = (ia − 1) − x.)
For m ∈ M let V^{(m)} := [mg, mg + h) ("tall runs"); these are pairwise disjoint since g > h.  They
fit in [k): using g ≤ 2k/λ + 5 ≤ 2.1k/λ (k ≥ 50λ), U + 1 ≤ k/(2g) + 2 and a² − 1 ≤ (√(U+1) + 1)² − 1
≤ k/(2g) + 2 + 2√(k/(2g) + 2), we get
(a² − 1)g + h ≤ k/2 + 3g + 2√(gk/2 + 2g²) ≤ k( 1/2 + 6.3/λ + 2.1/√λ ) ≤ 0.7k     (λ ≥ 170).
The complement [k) \ ⋃_m V^{(m)} consists of the |M| − 1 gaps between consecutive tall runs, each of
size g − h = 1, and the top gap [ (a²−1)g + h, k ) of size N ≥ 0.3k.  Split the top gap into
R := r − 2r' + 1 ≥ r/2 intervals of sizes differing by at most one (the *small runs*), and make each
size-1 gap its own run.  This gives a partition of [k) into at most r' + (r' − 1) + R = r intervals,
so every word w with the corresponding multiplicities defines a pattern π ∈ 𝓛_r.

*All shifts Δ ≤ k/2 are bad, for every word w.*  Let 1 ≤ Δ ≤ ⌊k/2⌋.  If Δ ≤ T + 1, Lemma 1(b)
applied to the tall run V^{(0)} against itself gives L_Δ(π) ≥ h − Δ ≥ T + 1.  Otherwise the
intervals [dg − (T+1), dg + (T+1)], d = 1, …, U, have length 2T + 3 = g and tile
[g − T − 1, Ug + T + 1] ⊇ [T + 2, k/2] (because Ug ≥ k/2 − T − 1 by the choice of U), so
Δ = dg + x with 1 ≤ d ≤ U ≤ a² − 1 and |x| ≤ T + 1.  Pick m > m' in M with m − m' = d; the tall runs
V^{(m)}, V^{(m')} have starts differing by dg, so by Lemma 1(b)
L_Δ(π) ≥ h − |Δ − dg| = h − |x| ≥ h − T − 1 = T + 1.
In both cases L_Δ(π) > T, i.e. Δ ∈ F(π).

*Hence j(π) = 2.*  If 0 ≤ t_1 < t_2 < t_3 ≤ k, then (t_2 − t_1) + (t_3 − t_2) ≤ k, so one of the two
differences is ≤ ⌊k/2⌋ and lies in F(π): no three shifts are mutually good.  As {0, k} is mutually
good, j(π) = 2.

*Counting.*  Fix the positions of all letters of the tall runs and of the size-1 runs arbitrarily
(one choice), and let the R small-run letters occupy the remaining N' := N − 0 ... precisely
N' := k − r'h − (|M| − 1) ≥ k − r'h − r' positions in any order consistent with the multiplicities:
this gives N'!/∏_{i ≤ R} n_i! distinct words, where (n_i) is a composition of N' into R parts
differing by at most one.  Such a composition maximises the multinomial coefficient (moving a unit
from a part n_1 ≥ n_2 + 2 to n_2 multiplies it by n_1/(n_2 + 1) ≥ 1), the number of compositions of
N' into R parts is ≤ (N' + 1)^{R−1}, and the multinomials sum to R^{N'}; hence the count is at least
R^{N'} (N' + 1)^{−(R−1)} ≥ exp( N' ln R − R ln(k+1) ).
Now R ln(k+1) ≤ r ln(k+1) ≤ k/2; ln R ≥ ln r − ln 2 ≥ ln r − 4r'/r·... more simply
ln R ≥ ln(r − 2r') ≥ ln r − 4r'/r ≥ ln r − 1/k (as r ≥ e^{75}, r' ≤ 30); and
r'h ≤ (2√(U+1) + 1)(2k/λ + 4) ≤ (√(λ + 8) + 1)(2k/λ)(1 + 2λ/k) ≤ θ_r k   (using U + 1 ≤ λ/4 + 2 since
g ≥ 2k/λ, and k ≥ 50λ).  Therefore
N' ln R ≥ (k − θ_r k − r')(ln r − 1/k) ≥ (1 − θ_r) k ln r − r' ln r − 1 ≥ (1 − θ_r)k ln r − 16 ln r,
which gives the displayed bound.  Finally θ_r is decreasing in λ and θ = 0.1755 at λ = 170, so
(1 − θ_r) ln r − 1/2 ≥ 0.824 · 75 − 0.5 = 61.3.  ∎

*Remarks.*  (1) The constant 29 (= D_100) plays no role: for any C, with ℓ_r = ⌈(ln r+1)/D_C⌉
threads and thresholds k/λ, λ = Θ(ln² r), the same family has j(π) = 2 and size
r^{k(1 − O(1/√λ))} = r^{k(1 − O(1/ln r))}, while the union bound has only e^{−2kD_C} per pattern; so
for ln r > 2D_C(1 + o(1)) the mechanism "ℓ threads at shifts with pairwise L_Δ ≤ k/λ" cannot cover
𝓛_r, whatever the entropy lemma.  (2) The obstruction is not entropic: by Lemma 1(b) the long chains
exist for every interleaving.  Numerically (log.md §2) the *actual* overlap of two threads on such
π is O(1) cells, i.e. the chain bound [W9] Lemma 3 is what fails, not the pattern.

## 3. Small positive extensions

**Proposition 3.**  With the setting of [W13] Theorem 5 (q = 2k, m = 100k, n = 800k²), w.h.p. the
random matrix M contains every π ∈ 𝓛_r for every r ≤ e^{57} and every π ∈ 𝓓_r for every r ≤ e^{28},
with no quasirandomness condition.

*Proof.*  For r ≤ e^{28} (resp. e^{14}) this is [W13] Theorem 5 with ℓ = 1.  Otherwise ℓ_r = 2
(resp. ℓ'_r = 2), and in step (c) of the proof of [W13] Theorem 5 take the shifts t_1 = 0, t_2 = k
instead of the greedy choice: they satisfy t_2 ≤ k = q − k, and every k-shift chain is empty
(no a has π(a) ≥ k), so the hypotheses of [W13] Theorem 4 hold with any (L, s, ρ), in particular
with (L(r,2), s(r,2), r) for which the arithmetic (a) was verified.  Thus Pr(M ⊅ π, 𝓑) ≤ e^{−58k}
for every π in the class, and the union bounds (d) are unchanged.  ∎

(This is just the observation that two row-disjoint threads are always available in 2k rows; it
extends the unconditional range from e^{28} to e^{57} and is the best the mechanism gives without
overlapping threads.)

**Proposition 4 (symmetries).**  Let 𝒞 ⊆ S_k be a class such that a uniformly random σ ∈ S_n
contains every π ∈ 𝒞 w.h.p.  Then the same holds for the classes 𝒞^{-1}, 𝒞^{rev}, 𝒞^{comp} and
their compositions (the orbit of 𝒞 under the dihedral group of the square).

*Proof.*  σ contains π iff σ^{-1} contains π^{-1} (invert an occurrence), iff σ^{rev} contains
π^{rev}, iff σ^{comp} contains π^{comp}; and σ^{-1}, σ^{rev}, σ^{comp} are again uniform.  ∎

In particular [W13] Theorem 5 and Proposition 3 also cover: patterns with ≤ r − 1 descents
(π^{-1} ∈ 𝓛_r) under the corresponding condition on π^{-1}, and unions of ≤ r *decreasing* runs.
By Lemma 1(c), however, the inverse of a periodic shuffle is a periodic shuffle (with r and h
exchanged) and has all shifts Δ ≤ k/2 bad as well, so inversion does not help for (G1).

## 4. What a chain forces on the word: the contiguous case

The following is the only entropy statement about chains that is true, and it concerns a much
finer statistic than L_Δ.  Call positions a, a+1, …, a+L−1 a *contiguous Δ-chain* if b is defined
on them and b(a + x) = b(a) + x for 0 ≤ x < L (the two threads would then ride together on
consecutive elements, W9 log §2.1(a)); let 𝒞_Δ(π) be the largest such L.

**Lemma 5.**  Fix the interval sizes (h_j).  For every Δ and L,
#{ w ∈ [r]^k : 𝒞_Δ(π_w) ≥ L } ≤ k² · r^{k − L}.

*Proof.*  Given (a, b(a)) (≤ k² choices), decode w from left to right.  Let c := max(a, b(a)),
c' := min(a, b(a)) < c, and let y = c + x with 0 ≤ x < L.  When we reach y we know w on [0, y), in
particular the letter j' = w(c' + x) and the number i' of earlier occurrences of j', hence the value
π(c' + x) = S_{j'} + i'.  If c' = b(a) then π(a + x) = π(b(a) + x) + Δ, and if c' = a then
π(b(a) + x) = π(a + x) − Δ; in either case π(y) is determined, and w(y) is the index of the interval
containing π(y).  So the L letters w(c), …, w(c + L − 1) are determined by the earlier ones and the
number of words is ≤ k² r^{k−L}.  ∎

For a single shift this is the "near-periodicity" of [W13] log §4 made precise; the multi-shift
version is discussed (and shown to be tight in an unexpected way) in log.md §4.
