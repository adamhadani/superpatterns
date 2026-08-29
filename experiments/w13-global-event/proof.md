# W13 — a global event with no log k in its union bound; unions of increasing runs at n = O(k²)

Date: 2026-08-29.  Everything in this file is proved in full.  Numerics, heuristics and the exact
remaining gap are in log.md.  Notation as in W9 (work/w9-alon-threads/proof.md), which we cite as
[W9]; He–Kwan (arXiv:1911.12878) is [HK].

## 0. Setting and the two classes of patterns

M is a uniformly random q × m zero-one matrix, q = 2k, m = Ck.  H-threads, intervals I_a, zero-run
profile (z_a), Δ-shift chains, L_Δ(π), the run r(c) of a cell and Lemma 0 / Lemma 3 / Lemma 5 are as in
[W9].  π ∈ S_k is 0-indexed.

**Definitions.**  For π ∈ S_k and A ⊆ [k] let LDS(π|_A) be the length of the longest decreasing
subsequence of the sequence (π(a))_{a ∈ A} (a in increasing order).  Put

  𝓓_r := { π ∈ S_k : LDS(π) ≤ r }        (π is a union of ≤ r increasing subsequences),
  𝓛_r := { π ∈ S_k : the values [k] can be split into ≤ r intervals V_1,…,V_r such that on each V_j
            the map v ↦ π^{-1}(v) is increasing }   (unions of ≤ r increasing runs on value intervals).

𝓛_r ⊆ 𝓓_r.  |𝓛_r| ≤ (k+1)^{r} r^{k} (choose the interval sizes, then for each position the run it
belongs to; the values are then forced), and |𝓓_r| ≤ r^{2k} (Lemma 1 below with j = k).  𝓛_r is the
"residual class" of [W9] log.md §5 (there with equal interval sizes).

## 1. Staircase sets and their count

**Definition.**  A set S of cells of [q] × [m] is a *ρ-staircase set* if its cells have pairwise
distinct rows and pairwise distinct columns, and S is a union of at most ρ *monotone chains*, a
monotone chain being a set of cells whose rows and columns increase together (c = (y,x), c' = (y',x')
in the chain, x < x' ⇒ y < y').  Equivalently: list S by increasing column; the resulting sequence
of rows has longest decreasing subsequence ≤ ρ (a sequence with LDS ≤ ρ is a union of ≤ ρ
increasing subsequences — patience sorting / the dual of Erdős–Szekeres; conversely the union of ρ
increasing subsequences has LDS ≤ ρ by pigeonhole).

**Lemma 1 (count).**  The number of ρ-staircase sets of size j in [q] × [m] is at most
C(q,j) · C(m,j) · ρ^{2j}.

*Proof.*  Choose the j rows and the j columns (C(q,j)C(m,j) ways).  S is then determined by the
bijection σ ∈ S_j sending the i-th smallest column to the rank of the row it carries.  S is a union
of ≤ ρ monotone chains iff [j] can be partitioned into ρ classes on each of which σ is increasing.
Label every position i ∈ [j] and every value v ∈ [j] by its class; the two labellings determine σ,
because within a class the positions must be matched to the values in increasing order.  There are
at most ρ^j · ρ^j pairs of labellings.  ∎

(This is the classical bound #{σ ∈ S_j : LDS(σ) ≤ ρ} ≤ ρ^{2j}; checked by brute force for j ≤ 8 in
out_exp5.txt.)

**Definition (the global event).**  For integers L, s, ρ let 𝓑_{L,s,ρ} be the event

  for every ρ-staircase set S with |S| ≤ L:  Σ_{c∈S} r(c) < s.

**Lemma 2.**  If s ≥ 4L and L ≤ k, then Pr(¬𝓑_{L,s,ρ}) ≤ L · (e² q m ρ² / L²)^L · e^{−s/8}.

*Proof.*  The cells of a staircase set lie in distinct rows, so [W9] Lemma 5 (= [HK] Lemma 2.3)
applies to each S of size j ≤ L: Pr(Σ_S r ≥ s) ≤ e^{−s/8} as s ≥ 4L ≥ 4j.  Union bound with Lemma 1:
Pr(¬𝓑) ≤ Σ_{j ≤ L} C(q,j)C(m,j)ρ^{2j} e^{−s/8} ≤ Σ_{j≤L} f(j) e^{−s/8}, f(j) := (e² q m ρ²/j²)^j.
f is increasing on j ≤ √(qm)·ρ (log f has derivative ln(e²qmρ²/j²) − 2 ≥ 0 there), and L ≤ k ≤ √(qm)
since q = 2k, m ≥ k; hence Σ_{j≤L} f(j) ≤ L f(L).  ∎

Compared with [W9] Lemma 6 (count 2(qm)^L, forcing s ≳ 16 L ln k), the count is now
(e²qmρ²/L²)^L = (2e²C ρ² (k/L)²)^L, i.e. e^{O(L·log(ρk/L))}: no log k when ρ and k/L are
polylogarithmic (or smaller) — this is the object-count reduction asked for in W13.

## 2. Chains of run-unions are staircase sets

**Lemma 3.**  Let π ∈ S_k, let thread t reach the elements of A ⊆ [k], and for a ∈ A let X_a be the
first cell of the interval I_a (the cell in row π(a)+t at which the thread starts seeking a).  Then
{X_a : a ∈ A} is a ρ-staircase set with ρ = LDS(π|_A).  In particular ρ ≤ r whenever π ∈ 𝓓_r (for
every A), and for π ∈ 𝓛_r the monotone chains can be taken to be the sets {X_a : a ∈ A, π(a) ∈ V_j}.
The same holds for the modified ("pretending") procedure of [W9] Theorem 7.

*Proof.*  The thread scans left to right and the intervals I_a are disjoint and visited in increasing
order of a, so the columns of X_a are strictly increasing in a; the rows π(a)+t are distinct.
Listing the X_a by column is listing them by a, and the row sequence is (π(a)+t)_{a∈A}, whose LDS is
LDS(π|_A); by the equivalence in §1 the set is a ρ-staircase set.  If π ∈ 𝓛_r, then for a < a' in A
with π(a), π(a') ∈ V_j we have π(a) < π(a') (π^{-1} is increasing on V_j), so each set
{X_a : π(a) ∈ V_j} is a monotone chain, and there are ≤ r of them.  The modified procedure has the
same interval structure ([W9] Theorem 7 (iii)).  ∎

## 3. Amplification with the staircase event

**Theorem 4 (= [W9] Theorem 7 with 𝓑 in place of 𝒜).**  Let q = 2k, let t_1 < ⋯ < t_ℓ ≤ k be shifts,
and let L, ρ, s be integers such that for all i < j every (t_j − t_i)-shift chain A of π satisfies
|A| ≤ L and LDS(π|_A) ≤ ρ.  If s ≥ 4L and (ℓ−1)(s+L) ≤ m/2, then

  Pr( M does not contain π, and 𝓑_{L,s,ρ} ) ≤ Pr( Bin( ℓ(m/2 − k), 1/2 ) ≤ ℓ(k−1) ).

*Proof.*  Repeat the proof of [W9] Theorem 7 verbatim with the following change in rule (b) of the
modified procedure: a cell c about to be looked at is *pretended* to be a one iff there is a
ρ-staircase set S of ≤ L cells such that Σ_{c'∈S} r̃(c') would become ≥ s if c were exposed as 0
(r̃ = known run, as in [W9]).  Facts (i) and (ii) of that proof hold with 𝓑_{L,s,ρ} in place of
𝒜_{L,s} by the same argument (on 𝓑 every pretended cell is a genuine one, so the modified procedure
coincides with the real one; and Σ_S r̃ < s for every ρ-staircase S of ≤ L cells at all times).
For (iii): by [W9] Lemma 3 the cells shared by threads t_i and t_j (i<j) lie in ⋃_{a∈A} Ĩ_a for a
(t_j − t_i)-shift chain A of elements reached by thread i, with |Ĩ_a| ≤ r̃(X_a) + 1.  By hypothesis
|A| ≤ L and LDS(π|_A) ≤ ρ, so by Lemma 3 {X_a : a ∈ A} is a ρ-staircase set of ≤ L cells and by (ii)
Σ_{a∈A} r̃(X_a) < s.  Hence |T̃_i ∩ T̃_j| ≤ s + L, and the rest of the proof (Bonferroni, |P| ≤ ℓ(k−1),
Lemma 0 with N = ℓ(m/2−k), K = ℓ(k−1)) is unchanged.  ∎

Write D_C := (C/2 − 1) · D( 2/(C−2) ‖ 1/2 ), D(p‖1/2) = ln 2 + p ln p + (1−p) ln(1−p), so that
(Chernoff–Hoeffding, K ≤ N/2)   Pr(Bin(ℓ(m/2−k),1/2) ≤ ℓ(k−1)) ≤ Pr(Bin(ℓk(C/2−1),1/2) ≤ ℓk) ≤ e^{−ℓ k D_C}.
Values: D_18 = 8·D(1/8‖1/2) > 2.5 (as in [W9]); D_36 = 17·D(1/17‖1/2) > 7.9; D_100 = 49·D(1/49‖1/2) > 29.

## 4. Unions of increasing runs at n = 800k²

Fix C = 100, m = 100k, q = 2k.  For 1 ≤ r ≤ k and an integer ℓ ≥ 1 define

  λ(r,ℓ) := (ℓ − 1)(ln r + 10),      L(r,ℓ) := ⌈ k/λ(r,ℓ) ⌉   (:= k if ℓ = 1),
  s(r,ℓ) := 8 L(r,ℓ) ( ln(2e²·100·r²·λ(r,ℓ)²) + 2 ),
  F(π; r,ℓ) := { Δ ∈ [k] : L_Δ(π) > L(r,ℓ) },
  𝓓_r^{qr}(ℓ) := { π ∈ 𝓓_r : ℓ (2|F(π;r,ℓ)| + 1) ≤ k },

and the two thread numbers  ℓ_r := ⌈(ln r + 1)/29⌉  (for 𝓛_r)  and  ℓ'_r := ⌈(2 ln r + 1)/29⌉  (for 𝓓_r).
Note ℓ_r = 1 for r ≤ e^{28}, and then F = ∅ and 𝓓_r^{qr}(1) = 𝓓_r.

**Theorem 5.**  For k sufficiently large, w.h.p. the random 2k × 100k matrix M contains every π in

  ⋃_{r ≤ k/(2 ln(k+1))} ( 𝓛_r ∩ 𝓓_r^{qr}(ℓ_r) )   ∪   ⋃_{r ≤ k} 𝓓_r^{qr}(ℓ'_r);

hence ([HK] Lemma 2.2) w.h.p. a uniformly random permutation of length n = 800k² contains every such π.

In words: n = O(k²) handles every union of r increasing runs on value intervals, for every r, provided
fewer than k/(2ℓ_r) − 1/2 shifts Δ have a Δ-shift chain longer than k/λ(r,ℓ_r), where ℓ_r ≈ ln r/29
threads are used and λ(r,ℓ_r) ≈ (ln r/29)(ln r + 10) = O(ln² r).  For r ≤ e^{28} there is no condition
at all (single thread).  For random interleavings the condition holds with F = ∅ (log.md §2.1:
max_Δ L_Δ ≤ 1.5k/√r ≪ k/λ), so the class contains all "run-quasirandom" residual patterns of [W9].
The second family interpolates up to r = k, where 𝓓_k = S_k and the condition is [W9]'s
quasirandomness with threshold k/λ(k,ℓ'_k) ≈ 14.5k/ln²k (versus k/(3 ln² k) in [W9] Theorem 8).

*Proof.*  (a) *Arithmetic.*  Fix r and ℓ ∈ {ℓ_r, ℓ'_r} with ℓ ≥ 2; write λ, L, s for λ(r,ℓ), L(r,ℓ),
s(r,ℓ).  Then s ≥ 4L.  Since k/L ≤ λ, the count in Lemma 2 is (e² q m r²/L²)^L ≤ (2e²·100·r²λ²)^L
=: K^L, and s/8 = L(ln K + 2), so Pr(¬𝓑_{L,s,r}) ≤ L K^L e^{−L ln K − 2L} = L e^{−2L} ≤ e^{−L}.
Next, 8 ln K + 17 = 8 ln(200e²) + 16 ln r + 16 ln λ + 17 ≤ 16 ln r + 16 ln λ + 75.4, so
(ℓ−1)(s+L) = (ℓ−1) L (8 ln K + 17) ≤ (ℓ−1)(k/λ + 1)(16 ln r + 16 ln λ + 75.4).
We claim 49λ ≥ (ℓ−1)(16 ln r + 16 ln λ + 75.4).  Dividing by ℓ−1 and using λ = (ℓ−1)(ln r+10) this
reads 49 ln r + 490 ≥ 16 ln r + 16 ln λ + 75.4, i.e. 33 ln r + 414 ≥ 16 ln((ℓ−1)(ln r + 10)); as
ℓ − 1 ≤ (2 ln r+1)/29 + 1 ≤ ln r + 10 the right side is ≤ 32 ln(ln r + 10), and 32 ln(ln r+10)
≤ 33 ln r + 414 for all r ≥ 1 (equal to 73.7 at r = 1; the derivative in ln r of the left side is
≤ 3.2 < 33).  Hence (ℓ−1)(s+L) ≤ 49k + (ℓ−1)(16 ln r + 16 ln λ + 75.4) ≤ 49k + 100 ln²k ≤ 50k = m/2
for k large (ℓ − 1 ≤ ln k, λ ≤ ln² k, r ≤ k).

(b) *Global events.*  Let 𝓑 := ⋂ 𝓑_{L(r,ℓ), s(r,ℓ), r} over all r ≤ k and ℓ ∈ {ℓ_r, ℓ'_r} with ℓ ≥ 2.
For these, λ(r,ℓ) ≤ ((2 ln k+1)/29)(ln k + 10) ≤ ln² k for large k, so L(r,ℓ) ≥ k/ln² k and
Pr(¬𝓑) ≤ 2k · e^{−k/ln² k} → 0.

(c) *One pattern.*  Fix r, ℓ ∈ {ℓ_r, ℓ'_r} and π ∈ 𝓓_r^{qr}(ℓ).  If ℓ = 1, a single thread gives
Pr(M ⊅ π) ≤ Pr(Bin(m,1/2) ≤ k−1) ≤ Pr(Bin(m/2−k,1/2) ≤ k−1) by [W9] Lemma 0.  If ℓ ≥ 2, choose
shifts in {0,…,k} greedily: each chosen t forbids t and t ± F(π;r,ℓ), at most 2|F|+1 values, and
ℓ(2|F|+1) ≤ k < k+1, so there are shifts t_1 < ⋯ < t_ℓ with all differences outside F.  For i < j
every (t_j − t_i)-shift chain A has |A| ≤ L_{t_j−t_i}(π) ≤ L(r,ℓ) and LDS(π|_A) ≤ LDS(π) ≤ r, so
Theorem 4 applies (hypotheses by (a)) with (L, s, ρ) = (L(r,ℓ), s(r,ℓ), r).  In both cases
Pr(M ⊅ π, 𝓑) ≤ e^{−ℓ k D_100} ≤ e^{−29 ℓ k}.

(d) *Union bound.*  For the first family, 29ℓ_r ≥ ln r + 1, and
Σ_{r ≤ k/(2 ln(k+1))} |𝓛_r| e^{−k(ln r+1)} ≤ Σ_r (k+1)^r r^k e^{−k ln r − k} ≤ Σ_r e^{r ln(k+1) − k}
≤ k e^{−k/2} → 0.  For the second, 29ℓ'_r ≥ 2 ln r + 1 and Σ_{r ≤ k} |𝓓_r| e^{−k(2 ln r + 1)}
≤ Σ_{r≤k} r^{2k} e^{−2k ln r − k} = k e^{−k} → 0.  Adding Pr(¬𝓑) → 0 proves the theorem.  ∎

*Remarks.*  (1) The constant: C = 100 was chosen so that ℓ_r = 1 up to r = e^{28} and the arithmetic
in (a) is slack; any C ≥ 18 works with r-dependent thresholds (D_C ≥ 2.5 gives ℓ_r = ⌈(ln r+1)/2.5⌉
and λ a larger multiple of ln² r).  (2) Compared with [W9] Theorem 8 (which needs L_Δ(π) ≤ k/(3 ln² k)):
for π ∈ 𝓛_r, r ≤ ln⁴ k, the chain threshold is now k/λ(r,ℓ_r) ≥ 29k/((ln r+1)(ln r+10))
≥ k/(2 ln² ln k) — larger by a factor ≈ ln² k/ln² ln k — exactly because s is O(L log r) instead of
O(L log k).  (3) What is *not* covered: π ∈ 𝓛_r (or 𝓓_r) with ≥ k/(2ℓ_r) shifts Δ having chains
longer than k/λ ("structured interleavings", e.g. periodic interleaving words; see log.md §2, §4), and
patterns outside ⋃_r 𝓓_r^{qr} (HK-structured maps whose chains have large LDS *and* many long chains).

## 5. A general form (arbitrary π)

**Corollary 6.**  Let m = Ck, C ≥ 18, ℓ := ⌈(ln k + 1)/D_C⌉ + 1, and for π ∈ S_k let
ρ(π) := max_Δ max { LDS(π|_A) : A a Δ-shift chain }.  Suppose L ≤ k and s := 8L(ln(2e²Cρ(π)²(k/L)²) + 2)
satisfy (ℓ−1)(s+L) ≤ m/2, and that fewer than k/(2ℓ) − 1/2 shifts Δ have L_Δ(π) > L.  Then
Pr(M ⊅ π, 𝓑_{L,s,ρ(π)}) ≤ k^{−k} e^{−k}, and Pr(¬𝓑_{L,s,ρ(π)}) ≤ e^{−L}.
(Proof: as in Theorem 5 (a)–(c).)  For a fixed ρ and L = k/λ the constraint reads
(ℓ−1)·(k/λ)·(16 ln(ρλ) + 8 ln(2e²C) + 17) ≤ Ck/2, i.e. λ ≈ (32 ln k/(C D_C)) · ln(ρλ): the admissible
chain length is k/λ with λ = O(ln k · ln(ρ ln k)) instead of [W9]'s λ = 3 ln² k — an improvement only
when ρ = k^{o(1)}, i.e. when the shift chains of π are unions of few monotone pieces.
