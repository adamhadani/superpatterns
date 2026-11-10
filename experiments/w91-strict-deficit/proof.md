# W91 — Strict deficit: one transposition costs a constant, and E LIS − 2·E L₂₁ ≥ c·√n / log n

Date: 10 November 2026. Continues W90 (block-flip theorem, exact deficit identity). Every item carries its status.

| Item | Statement | Status |
|:--|:--|:--|
| Theorem A | Poisson model on [0,T]². Let Δ_p be the loss in expected longest contained prefix when the identity pattern gets one adjacent transposition at positions p+1, p+2. Then Σ_p Δ_p ≥ c_A·T: averaged over the position, one transposition costs at least a constant, uniformly in T | **Proved** (§5) |
| Theorem B | For uniform σ_n and all n ≥ n_B: E LIS(σ_n) − 2·E L₂₁(σ_n) ≥ c_B·√n/ln n | **Proved** (§6) |
| Corollary C | If n ≤ (k²/4)(1 + c′/ln k) then P(σ_n ⊇ 2 1 4 3 ⋯ k (k−1)) → 0, whereas the identity of length k is contained w.h.p. once n ≥ k²/4 + ω(k^{4/3}) | **Proved** given Talagrand's inequality and Baik–Deift–Johansson |
| c₂₁ < 1 | liminf (E LIS − 2 E L₂₁)/√n > 0, i.e. a disproof of Alon's conjecture at the sharp constant | **Proved in `proof-c21.md`** (Theorem D there) from Proposition 6.1 and a rate-of-convergence bound for E L₂₁; hypothesis (H) of §7 is not needed. Not read by a human mathematician |
| Lemmas 2.3–2.5 | deterministic gadget, injectivity, leftmost optimal copy | **Proved**; brute-force checked from the definitions (§8) |

The constants c_A, c_B are explicit and absurdly small (10⁻⁸⁰, 10⁻⁹⁴); the numerical values are ≈ 0.005 per unit
of T for Theorem A and D(n) ≈ 0.0023·√n for Theorem B (W90 §5). What is new here is that they are positive.

Prior art: none found for Theorem B or Corollary C (searches of 10 Nov 2026, `memory/priority-check.md`). The
planted configuration of §2 is the pattern 3416725 of Burstein–Pantone (arXiv:1402.3842), which is where the
unbalanced Wilf-equivalence 1234 ∼ {1324, 3416725} comes from; the resampling tool is the bivariate Mecke formula.

--------------------------------------------------------------------------------------------------
## 1. Setting

Configurations, z < w, SW(z), NE(z), U_α, S_β, inside points, board, valid fillings and D-inversions are as in
`../w90-layered-deficit/proof.md` §1. For points e < x the open rectangle is R(e,x) = {z : e < z < x}; "a NW of b"
means x_a < x_b and y_a > y_b.

**Model.** P is a Poisson process of intensity 1 on Q_T = [0,T]². Almost surely P is a configuration, and
conditionally on |P| = n its order type is uniform on S_n; so every statement of W90 about σ_n holds conditionally.
LIS(P) is the longest increasing chain and L₂₁(P) the largest m with P ⊇ 21^{⊕m}.

**Patterns.** A *block word* is a finite sequence B = (B₁,…,B_r), B_i ∈ {1, 21}. It defines the infinite pattern
Π_B = B₁ ⊕ ⋯ ⊕ B_r ⊕ 1 ⊕ 1 ⊕ ⋯ (increasing tail) and T₀ = T₀(B), the total length of B₁,…,B_r. For an infinite
pattern W, W[1..t] is the pattern of its first t entries, and

  N_W(P) = max{ t ≥ 0 : P contains W[1..t] }.

For S ⊂ ℕ let W_S = B₁ ⊕ B₂ ⊕ ⋯ with B_i = 21 for i ∈ S and B_i = 12 otherwise; W_∅ is the identity, and for
finite S with largest element i*, W_S = Π_B for a block word with T₀ = 2i*.

 (F1) W[1..t] is contained in W[1..t+1], so E N_W(P) = Σ_{t≥1} P(P ⊇ W[1..t]); N_{W_∅} = LIS.
 (F2) 2·L₂₁(P) ≤ N_{W_ℕ}(P).
 (F3) If S ⊂ S′ then P(P ⊇ W_{S′}[1..t]) ≤ P(P ⊇ W_S[1..t]) for every t. (W_S[1..t] arises from W_{S′}[1..t] by
      replacing complete blocks 21 by 12 one at a time; each replacement is Theorem 1 of W90 with suitable α, β.
      For odd t the last, incomplete block is a single point in both patterns.)

**Stage costs.** For S ⊂ ℕ and i ∈ S put α_i = W_{S∩[1,i−1]}[1..2i−2] and

  Cost_S(i) = Σ_{b≥0} [ P(P ⊇ α_i ⊕ 12 ⊕ I_b) − P(P ⊇ α_i ⊕ 21 ⊕ I_b) ] ≥ 0.

**Lemma 1.1 (telescoping).** For every S ⊂ ℕ, E LIS(P) − E N_{W_S}(P) = Σ_{i∈S} Cost_S(i). Consequently

  E LIS(P) − 2·E L₂₁(P) ≥ Σ_{i∈S} Cost_S(i)   for every S, hence for a random S independent of P in expectation.

*Proof.* By (F1), E LIS − E N_{W_S} = Σ_t [P(P ⊇ I_t) − P(P ⊇ W_S[1..t])]. Fix t and let i₁ < ⋯ < i_r be the
elements of S that are ≤ t/2 (blocks completely inside the prefix), S_m = {i₁,…,i_m}. Then W_S[1..t] = W_{S_r}[1..t]
and the difference telescopes over m; W_{S_{m−1}}[1..t] = α_{i_m} ⊕ 12 ⊕ I_{t−2i_m} and W_{S_m}[1..t] =
α_{i_m} ⊕ 21 ⊕ I_{t−2i_m}. Summing over t ≥ 2i_m, i.e. over b = t − 2i_m ≥ 0, gives Cost_S(i_m); all terms are
non-negative, so the order of summation is immaterial. The consequence follows from (F2), (F3) with S′ = ℕ and (F1). ∎

**Lemma 1.2 (weight of a lens).** Say that P has a *lens at (α, b)* if, for the pair (α, β = I_b), there are exactly
three inside points and, with X = {x₁<x₂<x₃}, Y = {y₁<y₂<y₃} their coordinates, the board is X × Y without the two
cells (x₁,y₁) ∉ U_α(O) and (x₃,y₃) ∉ S_β(O). Then

  P(P ⊇ α ⊕ 12 ⊕ I_b) − P(P ⊇ α ⊕ 21 ⊕ I_b) ≥ ⅓·P(P has a lens at (α, b)).

*Proof.* The valid fillings are 231, 312, 321 (a bijection must avoid 1 ↦ 1 and 3 ↦ 3), so F = 3. In 321 the pair
in columns 1, 2 is a D-inversion (corners (x₁,y₂) ∈ U, (x₂,y₃) ∈ S). In 231 the two inversions have corners
(x₁,y₁) ∉ U and (x₃,y₃) ∉ S; in 312 likewise. So a = 2 and (a−1)/F = ⅓. Condition on |P| = n and apply formula
(★) of W90, Theorem 1: "lens at (α, b)" is a property of (O, X, Y), hence of the fibre, so
E[(a−1)/F] ≥ ⅓·P(lens), the remaining fibres contributing non-negative terms. ∎

--------------------------------------------------------------------------------------------------
## 2. Deterministic part

Fix a block word B, Π = Π_B, T₀ = T₀(B), and a configuration P. For t ≥ 0 let

  U_t = {z ∈ ℝ² : SW(z) contains Π[1..t]}   (an up-set, decreasing in t, U_0 = ℝ²),

and for q ∈ P define the *level* ℓ(q) = 1 + max{t : q ∈ U_t} and the *height* h(q) = the largest number of points
in an increasing chain of P that starts at q (q included). N = N_Π(P).

**Lemma 2.1 (levels in the tail).**
 (a) For t ≥ T₀: z ∈ U_{t+1} iff there is q ∈ P with q < z and ℓ(q) ≥ t+1.
 (b) If ℓ(q) ≥ T₀+1 then ℓ(q) = 1 + max({T₀} ∪ {ℓ(r) : r ∈ P, r < q}). Moreover, for any q: r < q and
     ℓ(r) ≥ T₀+1 imply ℓ(q) ≥ ℓ(r)+1.
 (c) If ℓ(q) ≥ T₀+1 then ℓ(q) + h(q) − 1 ≤ N.
 (d) For b ≥ 1 and z ∈ ℝ²: NE(z) contains I_b iff some q ∈ P, q > z, has h(q) ≥ b. For q ∈ P: NE(q) ⊇ I_b iff h(q) ≥ b+1.

*Proof.* (a) For t ≥ T₀, Π[1..t+1] = Π[1..t] ⊕ 1: a copy inside SW(z) is a copy A of Π[1..t] together with a point
q, A < q < z; "A < q" says q ∈ U_t, i.e. ℓ(q) ≥ t+1. (b) Let m = max{ℓ(r) : r < q} (−∞ if there is none). The
hypothesis says q ∈ U_{T₀}. If m ≥ T₀+1, (a) with t = m−1 gives q ∈ U_m and (a) with t = m gives q ∉ U_{m+1}; if
m ≤ T₀, (a) with t = T₀ gives q ∉ U_{T₀+1}. The last assertion is (a) with t = ℓ(r)−1. (c) q ∈ U_{ℓ(q)−1} gives a copy of Π[1..ℓ(q)−1] below-left of q; with
q and a chain of h(q)−1 points above q it is a copy of Π[1..ℓ(q)+h(q)−1], because ℓ(q)−1 ≥ T₀. (d) is the
definition. ∎

**Outside conditions.** Let e < x be points of P, R = R(e,x), s ∈ {0,1}. A point r ∈ P ∖ (R ∪ {e,x}) is of
*class (a)* if r < x, of *class (b)* if r > e, of *class (c)* otherwise (a point below x and above e would be in
R, so the classes are disjoint; class (c) points lie NW or SE of the whole rectangle).

 (O1) ℓ(e) ≥ T₀+1.
 (O2) ℓ(r) ≤ ℓ(e) for every r of class (a).
 (O3) h(r) ≤ h(x) for every r of class (b).
 (O4) No r of class (c) has both ℓ(r) ≥ ℓ(e)+s+2 and h(r) ≥ h(x)+2.
 (O5) There is no e′ of class (a) with ℓ(e′) = ℓ(e), e′ NW of e and (R(e′,x) ∖ R) ∩ P = ∅.
 (O6) There is no x′ of class (b) with h(x′) = h(x), x′ NW of x and (R(e,x′) ∖ R) ∩ P = ∅.

E_s(e,x) denotes the conjunction (O1)–(O6). (O5), (O6) are tie-breaking rules needed only for Lemma 2.4.

**Lemma 2.2 (the conditions see only the outside).** The values ℓ(e), h(x) and the truth of E_s(e,x) are the same
for P and for every configuration P′ with P′ ∖ R(e,x) = P ∖ R(e,x).

*Proof.* If r ∉ R and (r < x or r = e) then no point of R lies below-left of r (such a point q would give
e < q < r < x, i.e. r ∈ R, or q < e). So SW(r) ∩ R = ∅ and ℓ(r) depends only on P ∖ R. Symmetrically h(r) depends
only on P ∖ R when r ∉ R and (r > e or r = x). A class (c) point is NW or SE of R, so both SW(r) and NE(r) avoid R.
The conditions involve only these values, the classes, and emptiness of sets disjoint from R. ∎

**Planted order types.** π₀ = 3 4 1 6 7 2 5 and π₁ = 1 4 5 2 7 8 3 6 (= 1 ⊕ π₀). "P ∩ R ≅ π_s" means that R
contains exactly 7+s points of P and that they are order-isomorphic to π_s. For π₀ name the points, from left to
right, u₁, p₁, u₂, p₂, v₁, p₃, v₂ (heights 3, 4, 1, 6, 7, 2, 5); for π₁ there is one more point a below-left of
all of them. The order relations among them are exactly

  a < everything;  u₁ < p₁, p₂, v₁, v₂;  u₂ < p₂, p₃, v₁, v₂;  p₁ < p₂, v₁, v₂;  p₂ < v₁;  p₃ < v₂.

**Lemma 2.3 (the gadget).** Let e < x in P satisfy (O1)–(O4) for some s ∈ {0,1}, and suppose P ∩ R(e,x) ≅ π_s.
Put p = ℓ(e)+s+1 and b = h(x)+1. Then P has a lens at (Π[1..p], b), and its three inside points are p₁, p₂, p₃.

*Proof.* Let Q = P ∩ R. A point of P below some q ∈ Q is in Q, or equals e, or is of class (a); a point above
q ∈ Q is in Q, or equals x, or is of class (b).

*Levels.* Every q ∈ Q is above e, so ℓ(q) ≥ ℓ(e)+1 ≥ T₀+2 by (O1) and Lemma 2.1(b), and Lemma 2.1(b) computes
ℓ(q) from the points below q. By (O2) the points below q that are not in Q have level ≤ ℓ(e), with equality for
e. Going up through Q with the relations listed above: ℓ(a) = ℓ(e)+1 (if s = 1), ℓ(u₁) = ℓ(u₂) = ℓ(e)+s+1 = p,
ℓ(p₁) = ℓ(p₃) = p+1 (below p₁ in Q: a, u₁; below p₃: a, u₂), ℓ(p₂) = p+2.

*Heights.* By (O3) the points above q ∈ Q that are not in Q have height ≤ h(x), with equality for x. Going down:
h(v₁) = h(v₂) = h(x)+1 = b, h(p₂) = h(p₃) = b+1 (above p₂ in Q: v₁; above p₃: v₂), h(p₁) = b+2.

*Inside points.* A point q ∈ P is inside for (Π[1..p], I_b) iff q ∈ U_p and NE(q) ⊇ I_b, i.e. (definition of ℓ
and Lemma 2.1(d)) iff ℓ(q) ≥ p+1 and h(q) ≥ b+1. In Q this holds for p₁, p₂, p₃ and fails for a, u₁, u₂ (level ≤ p) and v₁, v₂ (height b).
It fails for e and class (a) (level ≤ ℓ(e) < p+1), for x and class (b) (height ≤ h(x) < b+1), and for class (c)
by (O4), since p+1 = ℓ(e)+s+2 and b+1 = h(x)+2. So I = {p₁, p₂, p₃}.

*Board.* The coordinates are x₁ < x₂ < x₃ (of p₁, p₂, p₃) and y₁ < y₂ < y₃ (of p₃, p₁, p₂). By Lemma 2 of W90,
U_α(O) = U_α(P) = U_p and S_β(O) = S_β(P), so cells can be tested in P: a cell c is in U_p iff some q < c has
ℓ(q) ≥ p (Lemma 2.1(a)), and in S_β iff some q > c has h(q) ≥ b (Lemma 2.1(d)). The points of P below (x₁,y₁)
are a, e and class (a) points — not u₁ (its height is between y₁ and y₂) and not u₂ (it is to the right of x₁) —
and all have level ≤ p−1; so (x₁,y₁) ∉ U_p. The cells (x₁,y₂) > u₁ and (x₂,y₁) > u₂ are in U_p, and every other
cell dominates one of them. The points above (x₃,y₃) are x and class (b) points — not v₁ (left of x₃) and not v₂
(below y₃) — of height ≤ b−1; so (x₃,y₃) ∉ S_β. The cells (x₂,y₃) < v₁ and (x₃,y₂) < v₂ are in S_β, and every
other cell is dominated by one of them. Hence the board is X × Y minus (x₁,y₁) and (x₃,y₃). ∎

**Lemma 2.4 (injectivity).** Fix s ∈ {0,1} and p. Let 𝒢_{p,s}(P) be the set of pairs e < x of P with
ℓ(e) = p−s−1, E_s(e,x) and P ∩ R(e,x) ≅ π_s. Then (e,x) ↦ h(x)+1 is injective on 𝒢_{p,s}, and each value is a
level b at which P has a lens at (Π[1..p], b). Hence |𝒢_{p,s}(P)| ≤ #{b : P has a lens at (Π[1..p], b)}.

*Proof.* The second assertion is Lemma 2.3. Let (e,x), (e′,x′) ∈ 𝒢_{p,s} with h(x) = h(x′) = b−1. Both give a
lens at (Π[1..p], b), so both have the same inside set, and the labels agree: exactly one pair of the three
inside points is comparable (p₁ < p₂), and p₃ is the third point. Let Q = P ∩ R(e,x), Q′ = P ∩ R(e′,x′). Everything
assumed about the two pairs from here on is symmetric in them, which justifies the two exchanges below.

*Q = Q′.* From the proof of Lemma 2.3 for (e,x): the points of Q below p₂ are a, u₁, u₂, p₁, of level ≥ p−s,
and the points of P below p₂ outside Q are e and class (a) points, of level ≤ p−s−1. So
Q ∩ SW(p₂) = {q ∈ P : q < p₂, ℓ(q) ≥ p−s}, an expression that does not mention (e,x). Likewise
Q ∩ NE(p₁) = {p₂, v₁, v₂} = {q ∈ P : q > p₁, h(q) ≥ b}. Since Q = (Q ∩ SW(p₂)) ∪ (Q ∩ NE(p₁)) ∪ {p₁,p₂,p₃},
and the same holds for Q′, we get Q = Q′.

*e = e′.* Suppose not. Both have level p−s−1 ≥ T₀+1, so they are incomparable (Lemma 2.1(b)); exchanging the
two pairs if necessary, e′ is NW of e. Then e′ ∉ R(e,x), and e′ < u₁ < x (u₁ ∈ Q′ ⊂ R(e′,x′)), so e′ is of class
(a) for (e,x) with ℓ(e′) = ℓ(e). Let z ∈ P with e′ < z < x and z ∉ R(e,x). Then z ∉ Q. If z < x′ then
z ∈ P ∩ R(e′,x′) = Q′ = Q, impossible; and z ≠ x′, because x′ < x would give h(x′) > h(x). So z is of class (b)
for (e′,x′) and (O3) gives h(z) ≤ h(x′) = h(x), contradicting z < x. Hence (R(e′,x) ∖ R(e,x)) ∩ P = ∅ and e′
violates (O5) for (e,x).

*x = x′.* Suppose not; the heights are equal, so x, x′ are incomparable, and exchanging the pairs if necessary x′
is NW of x. Then x′ is of class (b) for (e,x) (it is above e′ = e and not below x), and
(R(e,x′) ∖ R(e,x)) ∩ P = Q′ ∖ R(e,x) = ∅, so x′ violates (O6) for (e,x). ∎

**Lemma 2.5 (leftmost optimal copy).** Suppose N ≥ T₀+2. For T₀+1 ≤ i ≤ N let
G_i = {q ∈ P : ℓ(q) = i, h(q) = N−i+1} and let z_i be the point of G_i with the smallest x-coordinate. Then every
G_i is non-empty and, for T₀+1 ≤ i < N: z_i < z_{i+1}, R(z_i,z_{i+1}) ∩ P = ∅, ℓ(z_i) = i, and
E_s(z_i,z_{i+1}) holds for s = 0 and s = 1.

*Proof.* Take a copy of Π[1..N] in P and let q_j be its point in position j > T₀. The first j−1 points are
below-left of q_j, so ℓ(q_j) ≥ j, and h(q_j) ≥ N−j+1; Lemma 2.1(c) forces equality, so q_j ∈ G_j. G_i is an
antichain (Lemma 2.1(b)), so z_i is its NW-most point.
Each q ∈ G_{i+1} has a predecessor in G_i: by Lemma 2.1(b) some r < q has ℓ(r) = i; then h(r) ≥ h(q)+1 = N−i+1
and Lemma 2.1(c) gives equality. Each q ∈ G_i, i < N, has a successor in G_{i+1}: some r > q has h(r) = N−i, and
ℓ(r) ≥ i+1 with equality by Lemma 2.1(c). Let w ∈ G_i be a predecessor of z_{i+1} and w′ ∈ G_{i+1} a successor of
z_i. Then x(z_i) ≤ x(w) < x(z_{i+1}) and y(z_i) < y(w′) ≤ y(z_{i+1}) (z_{i+1} is NW-most in G_{i+1}), so z_i < z_{i+1}.
A point strictly between them would have level > i and < i+1. Write e = z_i, x = z_{i+1}; h(e) = N−i+1, h(x) = N−i.
(O1) holds. (O2): r < x gives ℓ(r) ≤ i by Lemma 2.1(b) (or ℓ(r) ≤ T₀). (O3): r > e gives h(r) ≤ h(e)−1 = h(x).
(O4): ℓ(r) ≥ i+s+2 and h(r) ≥ N−i+2 would give ℓ(r)+h(r)−1 > N. (O5): such an e′ has ℓ(e′) = i and, being below
x, h(e′) ≥ N−i+1, with equality by Lemma 2.1(c); so e′ ∈ G_i lies to the left of z_i. (O6): such an x′ has
h(x′) = N−i and, being above e, ℓ(x′) ≥ i+1, with equality by Lemma 2.1(c); so x′ ∈ G_{i+1} lies to the left of
z_{i+1}. ∎

**Remark 2.6 (at most one lens level).** For fixed α there is at most one b with a lens at (α, b); hence
|𝒢_{p,s}(P)| ≤ 1. Indeed, let q be the inside point at level b with the largest x-coordinate. If h(q) ≥ b+2, some
r > q has h(r) ≥ b+1, so r ∈ S_β, and r ∈ U_α because r > q; then r is an inside point to the right of q. So
h(q) = b+1, q is not inside at any level b′ > b, and the inside set at level b′ has at most two points.

--------------------------------------------------------------------------------------------------
## 3. Resampling

**Lemma 3.1 (resampling identity).** Fix a block word B, s ∈ {0,1} and p ≥ T₀+s+2, and let m = 7+s,
g_s(A) = A^m/(m!)². Then

  E |𝒢_{p,s}(P)| = E Σ_{(e,x)} 1{ e < x, ℓ(e) = p−s−1, E_s(e,x), P ∩ R(e,x) = ∅ } · g_s(area R(e,x)),

the sum being over ordered pairs of distinct points of P.

*Proof.* By the bivariate Mecke formula (Last–Penrose, *Lectures on the Poisson process*, Thm 4.4), for measurable
f ≥ 0, E Σ_{(e,x)} f(e, x, P ∖ {e,x}) = ∫∫ E f(e, x, P) de dx. The rectangle R(e,x) is open, so it does not
contain e or x, and it lies in Q_T, so P ∩ R(e,x) is a Poisson process of total mass area R(e,x). By Lemma 2.2 the indicator of
{ℓ(e) = p−s−1, E_s(e,x)} is a function Φ(e, x, η ∖ R(e,x)) of the configuration η ∪ {e,x} outside the rectangle.
For fixed e < x, P ∩ R(e,x) and P ∖ R(e,x) are independent, P ∩ R is a Poisson process on a rectangle of area A,
and P(P ∩ R ≅ π_s) = e^{−A}(A^m/m!)·(1/m!) = e^{−A} g_s(A) (m points, one order type out of m!), while
P(P ∩ R = ∅) = e^{−A}. So both sides equal ∫∫_{e<x} E Φ(e, x, P ∖ R(e,x)) · e^{−A} g_s(A) de dx. ∎

**Lemma 3.2 (cost of a stage).** Let B be a block word, Π = Π_B, s ∈ {0,1}, p ≥ T₀+s+2, α = Π[1..p], and let
(z_i) be the leftmost optimal copy of Lemma 2.5 (defined when N = N_Π(P) ≥ T₀+2). Then

  Σ_{b≥0} [ P(P ⊇ α ⊕ 12 ⊕ I_b) − P(P ⊇ α ⊕ 21 ⊕ I_b) ] ≥ ⅓ · E[ 1{N ≥ p−s} · g_s( area R(z_{p−s−1}, z_{p−s}) ) ].

*Proof.* By Lemma 1.2 the left side is ≥ ⅓ E #{b : lens at (α, b)} ≥ ⅓ E |𝒢_{p,s}| (Lemma 2.4). By Lemma 3.1 this
equals ⅓ of an expected sum of non-negative terms over pairs; when N ≥ p−s the pair (z_{p−s−1}, z_{p−s}) is one of
them by Lemma 2.5 (i = p−s−1 ≥ T₀+1). ∎

--------------------------------------------------------------------------------------------------
## 4. First-moment lemmas

A *step* is a pair z < z′; it is *thin* if area R(z,z′) < A₁, where from now on **A₁ = 10⁻¹⁰**. A chain
z₀ < z₁ < ⋯ < z_k has k steps, with increments (w_i, h_i), and its *span* is R(z₀, z_k), of area (Σw_i)(Σh_i).

**Lemma 4.1 (long chains have few thin steps).** For k ≥ 1,

  E #{chains z₀ < ⋯ < z_k in P with at least k/2 thin steps} ≤ T² e^{2T} 2^k (2√A₁)^{k/2}.

*Proof.* By the Mecke formula the expectation is the Lebesgue measure of the set of such (z₀,…,z_k) ∈ Q_T^{k+1}.
Choose the set of ⌈k/2⌉ thin steps (≤ 2^k ways). The increments satisfy Σw_i ≤ T and Σh_i ≤ T, so the indicator of
the domain is ≤ e^{2T − Σ(w_i+h_i)}. Integrating z₀ over Q_T and each increment over (0,∞)² with weight e^{−(w+h)}
gives 1 for an unconstrained step and P(E₁E₂ < A₁) ≤ P(min(E₁,E₂) < √A₁) ≤ 2√A₁ for a thin one (E₁, E₂
independent standard exponentials). Finally (2√A₁)^{⌈k/2⌉} ≤ (2√A₁)^{k/2} because 2√A₁ < 1. ∎

**Lemma 4.2 (area budget of a window).** For k ≥ 1,

  E #{pairs z < z′ of P with area R(z,z′) ≥ 4k² and LIS(P ∩ R(z,z′)) < k} ≤ T⁴ e^{−0.069·k}.

*Proof.* By the bivariate Mecke formula the expectation is ∫∫_{z<z′} 1{area ≥ 4k²}·P(LIS(P ∩ R(z,z′)) < k) dz dz′
(the event depends only on the points in the open rectangle). Cut a rectangle of area ≥ 4k² into a 2k × 2k grid
of congruent cells, each of area ≥ 1. The 2k diagonal cells are non-empty independently with probability
≥ 1 − e^{−1} > 0.632, and points from distinct diagonal cells form a chain. By Hoeffding,
P(Bin(2k, 0.632) < k) ≤ exp(−2·(0.132)²·2k) ≤ e^{−0.069k}. The set of pairs has measure ≤ T⁴. ∎

**Lemma 4.3 (windows of bounded area have few thin steps).** For k ≥ 1 and T ≥ 2,

  E #{chains z₀ < ⋯ < z_k in P with area R(z₀,z_k) ≤ 4k² and at least k/2 thin steps} ≤ (2 log₂T + 5)·T²·3^{−k}.

*Proof.* Let W = Σw_i, H = Σh_i, M = 2k, R₀ = ⌈log₂T⌉ + 1. We have W, H ≤ T and WH ≤ M². There is an integer r
with |r| ≤ R₀ such that W ≤ M·2^r and H ≤ 2M·2^{−r}: if W/M ≥ 2^{−R₀} take r = ⌈log₂(W/M)⌉ (then
H ≤ M²/W < M·2^{1−r}, and r ≤ ⌈log₂(T/2)⌉ < R₀ since W ≤ T and M ≥ 2), otherwise take r = −R₀ (then
H ≤ T ≤ 2^{R₀}). Fix r and put a = M·2^r, b = 2M·2^{−r}, so
ab = 8k². The indicator of {W ≤ a, H ≤ b} is ≤ exp(k(1 − W/a) + k(1 − H/b)) = e^{2k} Π_i e^{−k w_i/a − k h_i/b}.
Choose the ⌈k/2⌉ thin steps (≤ 2^k ways), integrate z₀ over Q_T and each increment over (0,∞)²: an unconstrained
step gives ab/k² = 8, and a thin step gives, after the substitution w = (a/k)u, h = (b/k)u′,
8·P(E₁E₂ < A₁/8) ≤ 8·2√(A₁/8) = 8·√(A₁/2). The total for one r is at most
T²·2^k·e^{2k}·8^k·(A₁/2)^{⌈k/2⌉/2} ≤ T²·(16e²(A₁/2)^{1/4})^k, and 16e²·(5·10⁻¹¹)^{1/4} < 0.315 < 1/3. There are
2R₀ + 1 ≤ 2 log₂T + 5 values of r. ∎

**Lemma 4.4 (elementary bounds on lengths).** For T ≥ 50:
 (i) P(LIS(P) < T/2 + 1) ≤ e^{−0.02(T−1)};  (ii) P(2 L₂₁(P) < 0.06·T) ≤ e^{−10⁻⁴(T−2)};  (iii) P(LIS(P) ≥ 3T) ≤ (e/3)^{6T}.

*Proof.* (i) The ⌊T⌋ unit squares [j, j+1)² on the diagonal are non-empty independently with probability
1−e^{−1} > 0.632, and one point from each non-empty square forms a chain; Hoeffding gives
P(Bin(⌊T⌋, 0.632) ≤ 0.532⌊T⌋) ≤ e^{−0.02⌊T⌋}, and 0.532(T−1) ≥ T/2+1 for T ≥ 48. (ii) The ⌊T/2⌋ squares
[2j, 2j+2)² contain an inversion independently with probability ≥ P(exactly two points, forming an inversion)
= 4e^{−4} > 0.073, and inversions from distinct squares form a copy of 21^{⊕m}; Hoeffding gives
P(Bin(⌊T/2⌋, 0.073) ≤ 0.063⌊T/2⌋) ≤ e^{−2·10⁻⁴⌊T/2⌋}, and 0.063(T/2−1) ≥ 0.03T for T ≥ 42. (iii) The expected number
of chains of k points is T^{2k}/(k!)² ≤ (eT/k)^{2k}. ∎

--------------------------------------------------------------------------------------------------
## 5. Theorem A: one transposition costs a constant

For p ≥ 0 let W^{(p)} = I_p ⊕ 21 ⊕ 1 ⊕ 1 ⊕ ⋯ (the identity with positions p+1, p+2 exchanged) and

  Δ_p(T) = E LIS(P) − E N_{W^{(p)}}(P) = Σ_{b≥0} [ P(LIS(P) ≥ p+b+2) − P(P ⊇ I_p ⊕ 21 ⊕ I_b) ] ≥ 0

(the two patterns have the same prefixes of length ≤ p+1; use (F1) and Theorem 1 of W90).

**Theorem A.** There is T_A such that for all T ≥ T_A, Σ_{p≥0} Δ_p(T) ≥ c_A·T with c_A = 10⁻⁸⁰.

Since Δ_p ≤ E(LIS(P)−p−1)⁺, Σ_{p≥3T} Δ_p(T) ≤ E[|P|²; LIS(P) ≥ 3T] ≤ (E|P|⁴·P(LIS(P) ≥ 3T))^{1/2} → 0
(Cauchy–Schwarz and Lemma 4.4(iii)), so the average of Δ_p over 0 ≤ p < 3T is at least c_A/4 for large T:
a transposition at a uniformly random position among the first 3T costs a positive constant in expected length,
uniformly in T. (Numerically the cost is ≈ 0.0025 per transposition, W90 §5.)

*Proof.* Take the empty block word: T₀ = 0, Π is the identity, ℓ is the usual level, N = L := LIS(P), and (z_i)
is the leftmost longest chain. Lemma 3.2 with s = 0 gives, for p ≥ 2,
Δ_p ≥ ⅓ E[1{L ≥ p}·area R(z_{p−1},z_p)⁷]/(7!)². Summing over p,

  Σ_p Δ_p ≥ (1/(3·(7!)²)) · E Σ_{i=1}^{L−1} area R(z_i,z_{i+1})⁷ ≥ (A₁⁷/(3·(7!)²)) · E #{i < L : (z_i,z_{i+1}) is not thin}

(A₁ = 10⁻¹⁰). Let 𝒜 be the event that L−1 ≥ T/2 and that no chain of P with k ≥ T/2 steps has at
least k/2 thin steps. On 𝒜 the chain z₁ < ⋯ < z_L has more than (L−1)/2 ≥ T/4 non-thin steps. By Lemma 4.4(i)
and Lemma 4.1 (with e^{2T} ≤ e^{4k} and 2e⁴(2√A₁)^{1/2} < 0.489),

  P(𝒜ᶜ) ≤ e^{−0.02(T−1)} + Σ_{k≥T/2} T²·0.489^k → 0.

So for large T the expected number of non-thin steps is ≥ T/8 and Σ_p Δ_p ≥ 10⁻⁷⁰·T/(24·(7!)²) > 10⁻⁷⁹·T. ∎

--------------------------------------------------------------------------------------------------
## 6. Theorem B: the deficit of 2 1 4 3 ⋯ is at least of order √n / log n

**Theorem B.** There is n_B such that for all n ≥ n_B and uniform σ_n ∈ S_n,

  E LIS(σ_n) − 2·E L₂₁(σ_n) ≥ c_B·√n / ln n,   c_B = 10⁻⁹⁴.

**Proposition 6.1 (Poisson version).** There is T_B such that for T ≥ T_B,
E LIS(P) − 2·E L₂₁(P) ≥ 10⁻⁹⁴·T/ln T.

*Proof.* Let K = ⌈45 ln T⌉ and J = ⌊0.015·T/K⌋, and assume ln T ≥ 10, so that K ≤ 45.1·ln T.
Let ξ₁,…,ξ_J be independent and uniform on {1,…,K}, independent of P, i₀ = 0, i_j = i_{j−1} + K + ξ_j, and
S = {i₁,…,i_J}. By Lemma 1.1 (applied for each value of S and averaged),

  E LIS(P) − 2·E L₂₁(P) ≥ Σ_{j=1}^{J} E_S[ Cost_S(i_j) ].                                   (6.1)

Fix j and i₁ < ⋯ < i_{j−1}. Let Π = W_{{i₁,…,i_{j−1}}}; it is Π_B for a block word with T₀ = 2i_{j−1}. Let
N = N_Π(P) and (z_ι) its leftmost optimal copy. Cost_S(i_j) depends on S only through i₁,…,i_j, and for
i = i_{j−1}+K+ξ the pattern α_i equals Π[1..2i−2] (the blocks between i_{j−1} and i are 12). So

  E[ Cost_S(i_j) | i₁,…,i_{j−1} ] = (1/K) Σ_{i = i_{j−1}+K+1}^{i_{j−1}+2K} C(i),
  C(i) = Σ_{b≥0} [ P(P ⊇ Π[1..2i−2] ⊕ 12 ⊕ I_b) − P(P ⊇ Π[1..2i−2] ⊕ 21 ⊕ I_b) ].

For such i put p = 2i−2 ≥ T₀+2K. Lemma 3.2 with s = 0 and with s = 1 bounds C(i) below by two quantities, hence
by their average; using g_s(A) ≥ min(1,A)⁸/(8!)²,

  C(i) ≥ (1/(6·(8!)²)) Σ_{s∈{0,1}} E[ 1{N ≥ p−s} · min(1, area R(z_{p−s−1}, z_{p−s}))⁸ ].

As i runs through the K values and s through {0,1}, the index ι = p−s−1 ∈ {2i−3, 2i−4} runs exactly once through
the 2K consecutive integers ι₀, …, ι₀+2K−1, where ι₀ = 2i_{j−1}+2K−2. Therefore

  Σ_i C(i) ≥ (1/(6·(8!)²)) · E[ 1{N ≥ ι₀+2K} · Σ_{ι=ι₀}^{ι₀+2K−1} min(1, area R(z_ι,z_{ι+1}))⁸ ].          (6.2)

Let 𝒜 be the event that (a) N ≥ ι₀+2K; (b) no pair of points of P is as in Lemma 4.2 with k = 2K; (c) no chain
of P is as in Lemma 4.3 with k = 2K. On 𝒜 consider the chain z_{ι₀} < ⋯ < z_{ι₀+2K}, which has 2K steps. A chain
of P inside R(z_{ι₀}, z_{ι₀+2K}) has at most 2K−1 points, because levels increase strictly along
z_{ι₀} < (chain) < z_{ι₀+2K} (Lemma 2.1(b)) from ι₀ to ι₀+2K. So by (b) the span has area < 4(2K)², and then by
(c) fewer than K of the 2K steps are thin. Hence on 𝒜 the sum in (6.2) is at least K·A₁⁸.

Probability of 𝒜. (a): ι₀+2K ≤ 4Kj ≤ 4KJ ≤ 0.06·T (as i_{j−1} ≤ 2K(j−1)), and
P(N ≥ t) = P(P ⊇ Π[1..t]) ≥ P(P ⊇ W_ℕ[1..t]) ≥ P(2L₂₁(P) ≥ t) by (F3), (F2); so P(N < ι₀+2K) ≤ e^{−10⁻⁴(T−2)} by
Lemma 4.4(ii). (b): 2K ≥ 90 ln T, so the expectation in Lemma 4.2 is ≤ T⁴·e^{−6.2 ln T} ≤ T⁻². (c): the
expectation in Lemma 4.3 is ≤ (2 log₂T + 5)·T²·3^{−90 ln T} ≤ T⁻². Hence P(𝒜) ≥ ½ for T ≥ T_B, and

  E[ Cost_S(i_j) | i₁,…,i_{j−1} ] ≥ (1/K)·K·A₁⁸/(12·(8!)²) = A₁⁸/(12·(8!)²) > 5·10⁻⁹¹   for every j ≤ J.

Summing over j in (6.1) and using J ≥ 0.015·T/(45.1·ln T) − 1 ≥ 3·10⁻⁴·T/ln T (T large) gives
E LIS − 2 E L₂₁ ≥ 1.5·10⁻⁹⁴·T/ln T. ∎

**Lemma 6.2 (de-Poissonisation).** Let D(n) = E LIS(σ_n) − 2·E L₂₁(σ_n). Then 0 ≤ D(n) ≤ n and
|D(n+1) − D(n)| ≤ 2·E LIS(σ_{n+1})/(n+1).

*Proof.* D ≥ 0 is Corollary 2 of W90. Realise σ_{n+1} by n+1 i.i.d. uniform points and delete one of them,
chosen uniformly; the rest is distributed as σ_n. LIS decreases by at most 1, and only if the deleted point lies
on a fixed longest chain, so 0 ≤ E LIS(σ_{n+1}) − E LIS(σ_n) ≤ E LIS(σ_{n+1})/(n+1). L₂₁ decreases by at most 1,
and only if the deleted point is one of the 2L₂₁ points of a fixed optimal copy, so
0 ≤ 2 E L₂₁(σ_{n+1}) − 2 E L₂₁(σ_n) ≤ 2·E[2L₂₁(σ_{n+1})]/(n+1) ≤ 2·E LIS(σ_{n+1})/(n+1), the last step again by
Corollary 2 of W90. The two increments are non-negative, so their difference is at most the larger bound. ∎

*Proof of Theorem B.* Take T = √n, so that |P| is Poisson(n) and E D(|P|) = E LIS(P) − 2 E L₂₁(P). Since
P(LIS(σ_m) ≥ k) ≤ C(m,k)/k! ≤ (e√m/k)^{2k}, E LIS(σ_m) ≤ 3√m for large m, so |D(m+1) − D(m)| ≤ 6/√m, and for
|m − n| ≤ r = √n·ln n we get |D(m) − D(n)| ≤ 7 ln n. Since P(||P| − n| > r) ≤ 2e^{−(ln n)²/3} and D(m) ≤ m, the contribution of ||P| − n| > r to E D(|P|) is at most
(E|P|²·P(||P| − n| > r))^{1/2} = o(1), so
D(n) ≥ E D(|P|) − 7 ln n − o(1) ≥ 1.5·10⁻⁹⁴·√n/(½ ln n) − 7 ln n − o(1) ≥ 10⁻⁹⁴·√n/ln n for large n. ∎

**Corollary C (the layered pattern is strictly harder than the identity).** There is c′ > 0 such that, for even
k → ∞ and n ≤ (k²/4)(1 + c′/ln k),

  P(σ_n ⊇ 2 1 4 3 ⋯ k (k−1)) → 0,

whereas P(σ_n ⊇ 1 2 ⋯ k) → 1 as soon as n ≥ k²/4 + ω(k)·k^{4/3} with ω(k) → ∞. In particular the statement of
Alon's conjecture cannot be strengthened to n = (1+ε_k)k²/4 with ε_k = o(1/ln k).

*Proof.* E LIS(σ_n) = 2√n + O(n^{1/6}) and the fluctuations of LIS are O(n^{1/6}) (Baik–Deift–Johansson), which
gives the statement about the identity. By Theorem B and E LIS(σ_n) ≤ 2√n + O(n^{1/6}),
E L₂₁(σ_n) ≤ √n − (c_B/3)·√n/ln n for large n. L₂₁ is a function of n independent points which changes by at
most 1 when one point is changed, and L₂₁ ≥ m is certified by 2m points; Talagrand's inequality for such
functions (Alon–Spencer, *The Probabilistic Method*, 4th ed., Theorem 7.7.1) gives fluctuations of order n^{1/4} around the median,
hence also |E L₂₁ − median| = O(n^{1/4}), and in particular P(L₂₁ ≥ E L₂₁ + n^{1/3}) → 0. So
P(L₂₁(σ_n) ≥ m) → 0 whenever m ≥ √n·(1 − (c_B/4)/ln n). With m = k/2 and n = ⌊(k²/4)(1 + c′/ln k)⌋ this holds for
a suitable c′ (note that ln n = (2+o(1)) ln k); for smaller n use that P(σ_n ⊇ τ) is non-decreasing in n (delete
a uniformly chosen point of σ_{n+1}). ∎

--------------------------------------------------------------------------------------------------
## 7. Removing the logarithm directly (hypothesis (H)) — no longer needed for c₂₁ < 1

> **Update, 10 November 2026, evening.** c₂₁ < 1 is proved in `proof-c21.md` without (H): since
> c₂₁T − 200√(T ln T) ≤ E L₂₁(P_T) ≤ c₂₁T, the deficit T/ln T of Proposition 6.1 cannot be a lower-order effect.
> This section is kept because (H) is what a direct proof of a deficit ≥ c·√n with a usable constant would need.

The proof of Proposition 6.1 loses ln T in exactly one place. A stage pays a constant as soon as the 2K steps
ι₀, …, ι₀+2K−1 of the leftmost optimal copy are not almost all thin; the proof gets this from Lemmas 4.2 and 4.3,
which are first-moment bounds over *all* chains of Q_T and therefore need 2K ≥ 90 ln T to beat the T² (or T⁴)
possible locations. The transpositions are then ln T apart. Everything else works for constant K. Precisely:

**Hypothesis (H) (not proved).** There are constants K ≥ 2, a ∈ (0,1], κ > 0 such that for all large T, all
j ≤ κT/K and all i₁ < ⋯ < i_{j−1} with gaps in [K+1, 2K]: for Π = W_{{i₁,…,i_{j−1}}}, N = N_Π(P), (z_ι) the
leftmost optimal copy and ι₀ = 2i_{j−1}+2K−2,

  P( N ≥ ι₀+2K and area R(z_ι, z_{ι+1}) ≥ a for some ι₀ ≤ ι < ι₀+2K ) ≥ ½.

**Proposition 7.1 (conditional).** (H) implies E LIS(P) − 2 E L₂₁(P) ≥ κ·a⁸/(13·K²·(8!)²)·T for large T, hence
c₂₁ ≤ 1 − κa⁸/(26K²(8!)²) < 1, and Alon's conjecture fails for small ε.

*Proof.* Repeat the proof of Proposition 6.1 with these K and J = ⌊κT/K⌋ ≥ κT/K − 1: by (6.2) and (H),
Σ_i C(i) ≥ a⁸/(12·(8!)²), so each of the J transpositions costs at least a⁸/(12·K·(8!)²). The passage to σ_n
is Lemma 6.2, as in the proof of Theorem B, and c₂₁ = lim E L₂₁(σ_n)/√n = 1 − lim D(n)/(2√n). ∎

(H) concerns steps 2K−1, …, 4K−2, counted from the last transposition, of the leftmost longest chain of P in the
up-set U_{T₀}. Remarks on why the elementary argument stops here, and what is already available.

 1. *Why counting fails for constant K.* A window of 2K steps can fail in two ways: its span is very large
    (a sparse or flat window), or its span is bounded but most steps are thin (a dense cluster). For a window at
    a fixed place both have probability e^{−cK}; but such windows exist somewhere in Q_T with probability → 1,
    and the optimal copy chooses where to cross a given level. Dense clusters even attract it. For the whole
    copy the budget Σw ≤ T, Σh ≤ T controls the selection (Lemma 4.1), which is why one transposition is easy
    (Theorem A); for windows of length ≥ 90 ln T the union bound does; for a window of bounded length one needs
    to know that the copy is not far from where the environment is typical. For point-to-point last passage
    percolation such statements come from local-increment bounds obtained by comparison with the stationary
    Hammersley process (Cator–Groeneboom; Cator–Pimentel; Pimentel, *Local behaviour of Airy processes*) and from
    results on the environment seen from a geodesic. I have not checked that they cover the level function of
    a pattern with transpositions. This is estimate (E1) of `../w90-layered-deficit/strict-deficit-plan.md`.
 2. *The multiplicity bound (E2) of that plan is now a theorem for fat pairs.* By Lemma 3.1 and Remark 2.6, for
    every level t ≥ T₀+1 and s ∈ {0,1},

      E Σ_{(e,x)} 1{ e < x, ℓ(e) = t, E_s(e,x), P ∩ R(e,x) = ∅ } · area R(e,x)^{7+s} ≤ ((7+s)!)².

    So the pairs that are compatible with being a step of an optimal copy at level t, and whose rectangle has
    area ≥ a, number O(a⁻⁸) in expectation, uniformly in T, t and Π. Only thin compatible pairs are uncontrolled.
 3. *A weaker sufficient condition.* In (H) "some step has area ≥ a" can be replaced by any event on which a
    bounded planted configuration inside the span of the window produces a lens at one of the K candidate
    levels with conditional probability bounded below; the single-step version is the simplest such event.

 4. *What (H) is about (reasoned; not used in the proofs).* For a tail level i, the points of level ≤ i are the
    points of the down-set ℝ² ∖ U_i, and this set is determined by the points it contains (U_i is the strict
    up-closure of the points of level i, whose levels depend only on what lies below them). Conditionally on it,
    P ∩ U_i is a fresh Poisson process, and for a point q of level i, h(q) − 1 is the longest fresh chain above
    q. The point z_i is the leftmost point of level i that maximises h, and z_{i+1} is the first point of a
    longest fresh chain from z_i. So (H) asks that the first step of a point-to-corner geodesic of a Poisson
    process, started from the best point of an independent staircase, spans an area ≥ a with probability
    bounded below, when 2K consecutive steps are allowed.

**Dead ends recorded in log.md:** planted increasing runs longer than the window (probability cost A₁^K);
pair windows with interior copy points (ratio of planted to reference probability still vanishes as the area
tends to 0); super-additivity of stage costs in the set of transpositions (no inequality known; the data suggest
the opposite sign); a fixed number J of transpositions with long windows (total cost J·e^{−cJ}); the first
version of Proposition 6.1, with K ≈ 2 ln T and a thin threshold 1/(8 ln T), which gave √n/(ln n)¹⁰.

--------------------------------------------------------------------------------------------------
## 8. Verification

*Proofs.* §1–§6 were written and then re-derived line by line by the main session. An independent adversarial
review (a separate agent that took no part in the writing) re-derived §1–§6, including both versions of §4–§6,
and found no error; its nine "under-justified step" remarks have been incorporated above. Report:
`out/review-1.md`.

*Brute force* (`gadget_check.py`, run by `run_checks.sh`, output `out/gadget_checks.txt`). All quantities are
computed from the definitions of W90 §1 (U_α and S_β by dynamic programming over corners, validated against
subset enumeration; fibres by enumerating all fillings), not from the level formulas of §2.

| Test | What is checked | Result |
|:--|:--|:--|
| `dp 8 300 11` | the corner DP for "contains Π[1..t]" against brute-force subset search, random block words | 3645 checks, 0 mismatches |
| `canon 40 400 12` | Lemma 2.5: consecutive points of the leftmost optimal copy form a chain, have empty rectangles and satisfy (O1)–(O6), s = 0, 1; block words with 0–3 blocks 21 | 1930 pairs, 0 failures |
| `plant n …`, n = 14, 24, 36, 48 | Lemma 2.3: for random pairs satisfying (O1)–(O4) with an empty rectangle, plant π_s and recompute the fibre at (p, b) = (ℓ(e)+s+1, h(x)+1) from scratch | 7756 plantings (3982 with blocks 21 in the pattern): inside set = {p₁,p₂,p₃}, F = 3, a = 2 in all |
| same runs | Lemma 2.4: in each planted configuration list all pairs of 𝒢_{p,s} and all lens levels | 15 512 (stage, s) cases, 8474 pairs, always on distinct lens levels; in 4975 cases dropping (O5), (O6) produces extra pairs, so the tie-break is needed and sufficient |
| `tie` | explicit configuration with two anchors below one lens | exactly the north-west anchor satisfies (O5) |
| `mecke 4 40000 17`, `mecke 6 12000 18` | Lemma 3.1 with a one-point plant (Monte Carlo): E #{pairs with E₀, one point in R} against E Σ_{pairs with E₀, R empty} area | 1.6427 ± 0.0076 vs 1.6454 ± 0.0040; 3.334 ± 0.020 vs 3.307 ± 0.011 |

*Independent certificate through direct containment* (the reviewer's own code, written without reading
`gadget_check.py`; `review/lemma23_containment.py`, `review/section1_exact.py`, outputs in `review/out/`). No
fibres or level formulas are used: containment of α ⊕ 12 ⊕ I_b and α ⊕ 21 ⊕ I_b is decided by a corner dynamic
programme, cross-checked against a generic backtracking matcher (113 820 decisions, 0 mismatches).

| Test | Result |
|:--|:--|
| Lemma 2.3, 47 428 plantings (37 828 under patterns with blocks 21; 11 055 on pairs off the optimal copy) | the planted configuration contains α⊕12⊕I_b and avoids α⊕21⊕I_b in all; of the arrangements 231, 312, 321 of the lens exactly 321 contains α⊕21⊕I_b and exactly 231, 312 contain α⊕12⊕I_b, in all |
| negative control: drop (O1) / (O2) / (O3) / (O4) | the conclusion fails in 19 190 of 24 000 / 5 123 of 18 838 / 6 738 of 17 933 / 2 066 of 4 238 cases |
| Lemma 2.4, Remark 2.6 in the same configurations | \|𝒢_{p,s}\| ≤ #lens levels ≤ 1 in all |
| Lemma 2.5 | 70 144 consecutive pairs, 0 failures |
| plantings into steps of the leftmost optimal copy (the case used in Lemma 3.2) | 14 024, \|𝒢_{p,s}\| = 1 in all |
| (F3) and Lemma 1.1 on all of S₇, S₈, S₉ for ten sets S | 0 violations; stage costs sum to 0, 1, 46 as in W90 |

Smallest instance of Lemma 2.3: σ = 1 4 5 2 7 8 3 6 9 (e = 1, x = 9, the seven points between them form 3416725)
contains 123456 and avoids 124356 = I₂ ⊕ 21 ⊕ I₂; checked by hand in log.md.

*Not checked numerically:* the probabilistic assembly (Lemmas 4.1–4.4, Theorems A and B) — the events are far
too rare to sample (c_B = 10⁻⁹⁴). The numerical constants in Lemmas 4.1–4.4 and Proposition 6.1 were recomputed
(`out/constants.txt`). The stage-by-stage identity that Lemma 1.1 rests on was validated in W90
(`fibre_cost.py`: exact on S₈, S₉; 0.1564 ± 0.0008 against 0.153 ± 0.012 at n = 10⁴).

## 9. Reproduction

```sh
cd experiments/w91-strict-deficit
sh run_checks.sh                                        # about 3 minutes on 5 cores; writes out/gadget_checks.txt
python3 review/lemma23_containment.py selftest
python3 review/lemma23_containment.py plant 201 400 4 5  # also seeds 202, 203; about 7.5 minutes each
python3 review/lemma23_containment.py canon 301 3000
python3 review/lemma23_containment.py canonplant 401 300
python3 review/section1_exact.py 9                       # also 7, 8; about 4 minutes for n = 9
```
