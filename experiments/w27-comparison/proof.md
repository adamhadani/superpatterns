# W27 — The comparison principle: statements and proofs

Notation. Π_N = uniform random permutation of length N (equivalently N i.i.d. uniform points in the unit square,
ordered by x, ranked by y). p_π(N) := Pr(π ⊄ Π_N). id_k = 12⋯k. Av_N(π) = #π-avoiders of length N, so
p_π(N) = Av_N(π)/N!. Tags: PROVED / HEURISTIC / NUMERICAL.

## 0. What Alon's conjecture needs, and what CP would give (PROVED, elementary)

**Lemma 0.1 (union bound).** If max_{π∈S_k} p_π(N) ≤ e^{−(1+ε)k ln k} for all large k then Π_N is a k-superpattern
w.h.p. Proof: Σ_π p_π(N) ≤ k!·max ≤ e^{k ln k − (1+ε) k ln k} → 0. ∎

**Lemma 0.2 (block splitting; independence of disjoint position blocks).** For M ≤ N,
p_π(N) ≤ p_π(M)^{⌊N/M⌋}. Proof: the standardisations of Π_N on ⌊N/M⌋ disjoint position blocks of length M are
independent uniform elements of S_M (conditionally on the value sets of the blocks the orders inside the blocks are
independent and uniform), and π ⊄ Π_N forces π ⊄ every block. ∎

Consequences. (a) Any bound p_π(C_0k²) ≤ e^{−ιk²} valid for all π ∈ S_k (one C_0, one ι > 0) already gives
p_π(N) ≤ e^{−(ι/C_0)(N − C_0k²)} — speed N — and Alon's conjecture with n = C_0k² by Lemma 0.1 (ιk² ≫ k ln k).
(b) Conversely the known per-pattern bound (W19 Thm 11: p_π(0.757k²) ≤ e^{−ηk} for all π) gives only speed N/k:
p_π(N) ≤ e^{−ηN/(0.757k)}, i.e. e^{−Θ(k)} at N ≍ k², and Alon only at N = O(k² ln k) (worse than He–Kwan's
k² log log k). So the entire content of the problem, in this language, is the **exponent k² versus k at N ≍ k²**:
a per-pattern tail of exponent ω(k ln k) at N = O(k²), uniformly in π.

**Lemma 0.3 (CP ⇒ Alon).** Suppose CP(K, a): p_π(N) ≤ e^{ak} p_{id}(N/K) for all π ∈ S_k, N. Then Π_N is a
k-superpattern w.h.p. for N = K(1/4 + ε)k², any ε > 0 (with a = o(ln k) allowed). Proof: p_id(M) = Pr(LIS(Π_M) < k) =
exp(−M H_0(k/√M)(1+o(1))) for k/√M → x ∈ (0,2) (Deuschel–Zeitouni 1999; H_0 > 0 on (0,2)); with M = N/K =
(1/4+ε)k², x = 1/√(1/4+ε) < 2, so p_π(N) ≤ e^{ak − c_ε k²} and Lemma 0.1 applies. With the explicit W23 certificate
bound p_id(M) ≤ (M+k)^k (e(k−1)²/(M−k+1))^M one gets the same with N = K e² k² and no asymptotic input. ∎

Remark (only the tail matters). CP at N below the identity's threshold is vacuous (both sides ≈ 1). The
principle is a statement about the LOWER-TAIL LARGE DEVIATIONS of "number of copies = 0" for every π, compared with
the LIS lower tail. Lemma 0.2(a) shows that CP "above threshold" (N ≥ C k² for one fixed C) is all that is needed
(task item (iv)): a bound at one N = C_0k² with exponent ≫ k ln k propagates to all larger N.

## 1. CP(1) is false at fixed k; the correct formulation is asymptotic in k (PROVED / exact enumeration)

**Fact 1.1.** Av_7(1324) = 2762 > 2761 = Av_7(1234) (Bóna; re-verified here by avoid.c), and Av_N(1324) > Av_N(1234)
for all N ≥ 7, with L(1324) ≈ 11.60 > 9 = L(1234). Hence for k = 4 the ratio p_π(N)/p_id(N) exceeds 1 from
N = 7 = 0.44 k² on and grows like (L(1324)/9)^N: **identity-hardest-at-every-N (CP with K = 1) fails already at
k = 4**, inside the window N ∈ [k²/2, 3k²/2].

**Fact 1.2 (CP(K), K > 1, is unfalsifiable at fixed k).** For fixed π ∈ S_k and K > 1,
p_id(N/K)/p_π(N) ≥ Av_{N/K}(id_k)/(N/K)! · N!/Av_N(π) ≥ N!/((N/K)! L(π)^N (N/K)^{...}) → ∞, since N! ≫ (N/K)! e^{O(N)}.
So Stanley–Wilf effects (L(π) = 2^{Θ(k)} for typical π, Fox 2013) never contradict CP(K) with K > 1 at fixed k: the
only content of CP is uniformity in k in the window N ≍ k². The right object is the **per-point rate**
I_π(C) := −(1/N) ln p_π(N) at N = Ck² (finite k), and the conjecture becomes a comparison of rate functions:

**Conjecture CP* (rate form).** There are C_0 < ∞ and ι > 0 such that for all k and all π ∈ S_k,
I_π(C_0) ≥ ι, i.e. p_π(C_0k²) ≤ e^{−ιC_0k²}. (Stronger, "identity-hardest asymptotically":
liminf_k min_{π∈S_k} I_π(C)/I_id(C) ≥ 1/K for every C > K/4.)

**Heuristic 1.3 (why the identity should be the cheapest to avoid at N ≍ k²).** Lower bounds on p_π come from
π-avoiding classes 𝒞: p_π(N) ≥ Pr(Π_N ∈ 𝒞). The identity has the class of merges of k−1 decreasing sequences, of
growth rate (k−1)² and, at N = Ck², probability e^{−N ln(4C/e)(1+o(1))} (DZ). For a random π ∈ S_k every monotone
subsequence has length ≤ (2+o(1))√k, so π is not a merge of m monotone sequences for m < √k/2 and not
(a×b)-griddable by monotone cells for a+b < 2√k; the corresponding π-avoiding classes have growth rates m² ≲ k/4 and
ab ≲ k, i.e. cost per point ≈ ln(Ck) − O(1) ≫ ln(4C/e). The Stanley–Wilf class Av(π) itself has growth 2^{Θ(k)} ≫ k²,
but that growth is only reached for N ≫ 2^{Θ(k)} (Fact 1.2). So at N ≍ k² every *structured* avoidance
mechanism is far more expensive for random π than for the identity — consistent with the W21 thresholds (random π
contained 11% earlier at k = 36) and with CP*. The finite-k crossovers of Fact 1.1 are the small-k shadow of the
Stanley–Wilf regime; §3 measures how the crossover n_×(π) moves with k.

## 2. What is proved: speed-N tails for a class of patterns, and closure properties

### 2.1 Coarse-graining + Mirsky: direct sums of bounded blocks (PROVED)

Setting. Π_N as N i.i.d. uniform points in [0,1]²; cut the square into a g×g array of cells (area 1/g² each).
n_c = number of points in cell c (multinomial(N; 1/g², …, 1/g²)); given (n_c) the standardised patterns of the cells
are independent and uniform. Fix b ≥ 1 and call a cell **good** if its pattern contains every τ ∈ S_b (it is a
b-superpattern). Let q_b(n) = Pr(Π_n is a b-superpattern), nondecreasing in n, and q̄ = q̄_b(N, g) := E q_b(n_c),
n_c ~ Bin(N, 1/g²). Write L := ln(1/(1−q̄)).

**Theorem 2.1.** Let π = τ_1 ⊕ τ_2 ⊕ ⋯ ⊕ τ_h with |τ_i| ≤ b for all i (or the same with ⊖ throughout). Then for
every g ≥ 1,
      p_π(N) ≤ 16^{g(h−1)} · (1 − q̄)^{g² − (h−1)(2g−1)}.
In particular, with g = ⌊√(N/m)⌋ (m = points per cell) and N ≥ mΛ²h² for a Λ with (1 − 2/Λ)L > (ln 16)/Λ,
      p_π(N) ≤ exp(−ι N),   ι = [(1 − 2/Λ)L − (ln 16)/Λ]/m  > 0,
where L = L_b(m) depends only on b and m (not on k, h or the τ_i). Since h ≤ k, N ≥ mΛ²k² suffices.

*Proof.* (a) If the good cells contain a chain c_1 < c_2 < ⋯ < c_h that is strictly increasing in both cell
coordinates, then π ⊂ Π_N: every point of c_i lies strictly SW of every point of c_{i+1}, cell c_i is good so it
contains a copy of τ_i, and the union of these copies is a copy of τ_1 ⊕ ⋯ ⊕ τ_h.
(b) (Mirsky) If the poset of good cells (strict product order on [g]²) has no chain of length h, the good cells are
covered by h−1 antichains. An antichain of [g]² (no two cells with x < x′ and y < y′) is contained in a maximal
one, which is a weakly decreasing staircase (a lattice path of 2g−1 cells); there are ≤ C(2g−2, g−1) ≤ 4^g maximal
antichains, each with ≤ 2^{2g−1} subsets, so ≤ 16^g antichains, and a union S of h−1 of them has |S| ≤ (h−1)(2g−1).
Hence {no h-chain of good cells} ⊆ ∪_S {every cell outside S is bad}, a union of ≤ 16^{g(h−1)} events.
(c) For a fixed set T of cells, Pr(all c ∈ T bad) = E ∏_{c∈T} (1 − q_b(n_c)) (conditional independence given counts).
The functions n ↦ 1 − q_b(n) are nonnegative and nonincreasing and the multinomial vector (n_c) is negatively
associated (Joag-Dev–Proschan), so E ∏_{c∈T} f(n_c) ≤ ∏_{c∈T} E f(n_c) = (1 − q̄)^{|T|}. Combine with (b), |T| ≥
g² − (h−1)(2g−1). (d) With g ≥ Λh: exponent ≤ gh ln 16 − (g² − 2gh)L ≤ −g²[(1−2/Λ)L − (ln 16)/Λ] and g² ≥ N/m − O(√N/m);
absorb the O(√N) into the constant or read ι as the asymptotic rate. ∎

**Corollary 2.2 (explicit instances; q̄ computed with Poisson(m) counts, which is what Bin(N, m/N) tends to).**
(i) Identity (b = 1, q_1(n) = 1[n ≥ 1], q̄ = 1 − e^{−m}): m = 5, L = 5.0, Λ = 3: ι = (5/3 − 0.924)/5 = 0.148 for
N ≥ 45k². (The DZ/W23 rate ln(C/e) is far better; the point is an elementary speed-N proof by a mechanism that
does not use the LIS structure.)
(ii) Layered patterns with all layers of length ≤ b, in particular (21)^{k/2} (b = 2; q_2(n) = 1 − 1/n! − 1[n ≤ 1]·(1−1/n!)
i.e. "n ≥ 2 and not increasing"): m = 6 gives q̄ = 0.938, L = 2.78, Λ = 4: ι = (1.39 − 0.69)/6 = 0.116 for N ≥ 96h² = 24k².
This is the first speed-N tail bound for (21)^{k/2} and for every layered pattern with bounded layers; W19's
greedy has failure speed ≤ min(k, strip height) = 2 for these patterns, so it could not give it.
(iii) Every ⊕-sum (or ⊖-sum) of blocks of size ≤ b: p_π(N) ≤ e^{−ι_b N} for N ≥ Λ_b k², where m = m_b must make a
uniform Π_m a b-superpattern with probability bounded away from 0 — m_b = O(b² log log b) by He–Kwan, m_b = O(b²) if
Alon's conjecture holds at scale b. So Alon's conjecture at scale b implies uniform speed-N tails (with C_0 = O(1))
for all block-diagonal patterns with blocks ≤ b, of any total length k.

Remark. CP itself is NOT proved for these patterns: Theorem 2.1 gives I_π(C) ≥ ι_b > 0 (the CP* form), not
I_π(C) ≥ I_id(C)/K. The rate ι_b degrades with b like 1/m_b ≈ 1/b², so the theorem says nothing uniform over
patterns whose blocks grow with k.

### 2.2 Direct sums of two arbitrary patterns (PROVED, trivial but useful)

**Lemma 2.3.** For α ∈ S_a, β ∈ S_b and any x, y ∈ (0,1):
p_{α⊕β}(N) ≤ E p_α(Bin(N, xy)) + E p_β(Bin(N, (1−x)(1−y))), and the same for ⊖ with the NW/SE boxes.
Proof: the points in [0,x]×[0,y] and in [x,1]×[y,1] form uniform patterns of binomial sizes, and a copy of α in the
first plus a copy of β in the second is a copy of α ⊕ β. ∎
With x = y = a/(a+b) the two boxes receive N a²/k² and N b²/k² points: the *same* C = N/k² for both parts. Hence
CP* (uniform rate ι at C_0) is closed under ⊕ and ⊖ with ι ↦ ι·min(a², b²)/k², i.e. ι/4 for balanced sums;
CP(K, a) for α, β gives for α⊕β only the weaker p ≤ e^{ak} p_{id_{k/2}}(N/(4K)) ≈ e^{ak} p_{id_k}(N/K)^{1/4}.
Iterating over the ⊕-tree of a separable pattern loses a factor 4 per level, so this is useful only for bounded
depth (e.g. π = α ⊕ β with two halves for which CP* is known).

### 2.3 The relabelling identity (PROVED; reduces every π to a constrained LIS)

**Proposition 2.4.** For every ρ ∈ S_N: Π ↦ ρ∘Π preserves the uniform law, and a copy of id_k in Π at positions I
with value set V becomes, in ρ∘Π, a copy of the pattern ρ|_V at the same positions. Therefore, for every ρ,
      p_π(N) ≤ Pr( Π_N has no increasing k-subsequence whose value set V satisfies ρ|_V ≅ π ),
with equality when the right-hand side is minimised over ρ … in fact with equality for every ρ:
π ⊂ ρ∘Π ⟺ ∃ an increasing subsequence of Π with ρ|_V ≅ π, and ρ∘Π is uniform, so the two sides are equal.
So **p_π(N) = Pr(constrained LIS_ρ,π (Π_N) < k) for every ρ ∈ S_N** — the comparison with the identity is exactly the
question of how much a value-set constraint of "density" |𝒱_π(ρ)|/C(N,k) ≈ 1/k! costs the LIS lower tail.
Examples: ρ = reversal of value blocks of size s turns (21)^h into "an increasing subsequence with ≥ 2 points in
each of h prescribed value strips"; ρ = the tilted grid relabelling turns (12⋯r)^h into an increasing subsequence
with one point in each cell of an r×h grid of value strips × ??? — no: only values are relabelled, positions are not,
so grids are not reachable this way (see §4). The identity is the cheapest instance (no constraint).
