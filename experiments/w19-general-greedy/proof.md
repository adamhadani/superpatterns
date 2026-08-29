# W19 — the corner greedy for general patterns, and the speed of greedy embeddings

Date: 2026-08-29.  Every statement is tagged PROVED / HEURISTIC / NUMERICAL.  Numerics and dead ends: log.md.
Notation and the cited facts are those of experiments/w11-strips/proof.md (referred to as [W11]); in particular
(U,V) is the corner-increment law with density C e^{−C(u+v)²/2} on the quadrant, E U = √(π/(8C)),
Λ_C(θ) = ln E e^{θU}, c(C) = sup_{θ>0}(θ − Λ_C(θ)) > 0 iff C > π/8 ([W11] (4.1)–(4.2)).

## 0. Setting

Π_N is a Poisson process of intensity N = Ck² on [0,1]²; π ∈ S_k acts on 0-indexed positions and values.
For a set I of values, π^{-1}|_I is the position sequence of the values of I; "π^{-1} increasing on I" means
that the points of π with values in I form a chain (an increasing run in position order), "decreasing" an
anti-chain.  The *row* of value v is R_v = [0,1) × [v/k, (v+1)/k); the *strip* of a value interval
I = [v_0, v_1] is S_I = [0,1) × [v_0/k, (v_1+1)/k) (height |I|/k).

*Extended processes.*  For a family of disjoint measurable regions A_1, …, A_m ⊆ [0,1]² let
Π^{(ℓ)} := (Π_N ∩ A_ℓ) ∪ (an independent Poisson process of intensity N on ℝ² ∖ A_ℓ).  Then Π^{(1)}, …, Π^{(m)}
are independent Poisson processes of intensity N on ℝ² (as in [W11] Thm 4.1 Step 1), and a point of Π^{(ℓ)}
lying in A_ℓ is a point of Π_N.

## 1. A sequential fresh-search lemma (PROVED)

**Lemma 1.1 (one search).**  Let Π be a Poisson process of intensity N on ℝ², A ⊆ ℝ² measurable, ψ: A → [0,∞)
measurable with |{ψ < t} ∩ A| < ∞ for all t and |{ψ < t}| → ∞ as t → ∞, and let p* be the a.s. unique
minimiser of ψ on Π ∩ A (existence and uniqueness a.s. as in [W11] Lemma 4.3; uniqueness needs ψ to have
absolutely continuous distribution under Lebesgue measure on A, which holds for all ψ used below).  Put
Δ(p) := {q ∈ A : ψ(q) ≤ ψ(p)}.  For measurable g ≥ 0 on A and F ≥ 0 on configurations,
   E[ g(p*) F(Π ∩ (A ∖ Δ(p*))) ] = ∫_A g(p) e^{−N|{ψ < ψ(p)} ∩ A|} E[ F(Π ∩ (A ∖ Δ(p))) ] N dp.
That is: p* has density N e^{−N|{ψ<ψ(p)}∩A|} on A and, conditionally on p* = p, Π ∩ (A ∖ Δ(p)) is a Poisson
process of intensity N on A ∖ Δ(p); moreover Π ∩ (ℝ² ∖ A) is independent of everything.

*Proof.*  Verbatim [W11] Lemma 4.3 with the quadrant Q replaced by A and the triangle by the sublevel set:
p* is the unique p ∈ Π ∩ A with Π ∩ {ψ < ψ(p)} ∩ A = ∅; apply the Mecke equation and the independence of
Π on the disjoint sets {ψ < ψ(p)} ∩ A, A ∖ Δ(p), ℝ² ∖ A.  ∎

**Lemma 1.2 (sequential searches).**  Let Π^{(1)}, …, Π^{(m)} be independent Poisson processes of intensity N
on ℝ² and let a procedure perform searches t = 1, 2, …, T (T finite, possibly random and adapted): search t
chooses, as a measurable function of the outcomes of searches 1..t−1 (and of independent auxiliary
randomness), an index ℓ_t, a region A_t and a function ψ_t as in Lemma 1.1, and returns the minimiser p_t of
ψ_t on Π^{(ℓ_t)} ∩ A_t; its explored set is Δ_t := {q ∈ A_t : ψ_t(q) ≤ ψ_t(p_t)}.  Suppose that a.s. for all
t' < t with ℓ_{t'} = ℓ_t,  A_t ∩ Δ_{t'} = ∅.  Then, conditionally on the outcomes of searches 1..t−1,
Π^{(ℓ_t)} ∩ A_t is a Poisson process of intensity N on A_t; in particular p_t has the conditional density
N e^{−N|{ψ_t<ψ_t(p)}∩A_t|} on A_t, and any function of p_t whose conditional law under this density does not
depend on the past is independent of the past.

*Proof.*  Induction on t with the stronger hypothesis H_t: conditionally on searches 1..t−1, for each ℓ,
Π^{(ℓ)} ∩ (ℝ² ∖ ∪_{t'<t, ℓ_{t'}=ℓ} Δ_{t'}) is a Poisson process of intensity N on that set, and these are
independent over ℓ.  H_1 is the assumption.  Given H_t, search t is a search in the process
Π^{(ℓ_t)} ∩ (ℝ² ∖ ∪Δ_{t'}) (because A_t is disjoint from the explored sets), which is conditionally Poisson on a
set containing A_t; Lemma 1.1 (applied conditionally, with A = A_t, F = the indicator of any event of the
process outside A_t ∪ Δ_t) yields H_{t+1}: outside the new explored set Δ_t the process is again conditionally
Poisson, and the other processes are untouched.  ∎

All greedies below are instances of Lemma 1.2, and all "increments are i.i.d." claims follow from it: the
conditional density of p_t on A_t has the same form at every step after the affine normalisation.

## 2. Rigid rows: every pattern, threshold N = k², speed k (PROVED)

**Theorem 2.1.**  For every k ≥ 1, every π ∈ S_k and every C > 0, with N = Ck²,
   Pr(π ⊄ Π_N) ≤ Pr( Poisson(Ck) ≤ k − 1 ) ≤ exp(−k (C − 1 − ln C))    (the last for C > 1).
The bound is attained by the procedure: the row-greedy of the proof fails with probability exactly
Pr(Poisson(Ck) ≤ k−1).

*Proof.*  Use the extended processes Π^{(v)} of the rows R_v, v = 0..k−1.  Keep an x-level a (initially 0).
For p = 0, 1, …, k−1 in this order let q_p be the point of Π^{(π(p))} in the half-row A_p := {x > a} × [π(p)/k,
(π(p)+1)/k) minimising ψ_p(x,y) := x − a, put X_p := k (x(q_p) − a) and a := x(q_p).
*Increments.*  Each row's process is searched exactly once, so the disjointness hypothesis of Lemma 1.2 is
vacuous, and conditionally on the past q_p has density N e^{−N t/k} on A_p at horizontal distance t from the
corner (|{ψ_p < t} ∩ A_p| = t/k).  In the variable u = kt the density of X_p is (N/k²) e^{−(N/k²)u} = C e^{−Cu}:
X_0, …, X_{k−1} are i.i.d. Exp(C).
*Copy.*  On E := {X_0 + ⋯ + X_{k−1} < k} the chosen points have x-coordinates (X_0 + ⋯ + X_p)/k ∈ (0,1), so
they lie in [0,1]² ∩ R_{π(p)} and are points of Π_N; their x-order is the position order p, and their
y-order is the order of the rows, i.e. of the values π(p).  Hence they form a copy of π and Pr(π ⊄ Π_N) ≤
Pr(E^c).  Conversely the procedure fails exactly on E^c.
*Tail.*  Σ_{p<k} X_p ≥ k iff the Poisson process of rate C on [0, k] formed by the partial sums has at most
k − 1 points in [0,k), i.e. Pr(E^c) = Pr(Poisson(Ck) ≤ k − 1); Chernoff: for C > 1,
Pr(Poisson(λ) ≤ k−1) ≤ e^{−λ} (eλ/k)^k = e^{−k(C − 1 − ln C)} with λ = Ck.  ∎

*Remarks.*  (i) This is He–Kwan's "thread" (a greedy through a 0/1 matrix) in Poisson form; nothing here is
new except the constant.  (ii) Reflection in the diagonal gives the same bound with rigid columns.  (iii) The
increments are exactly exponential, so the speed of this procedure is exactly k: the greedy exposes only ~Ck
points of the N = Ck² available, and its failure is a large deviation of k i.i.d. summands.

**Corollary 2.2 (the trivial union bound, with constant).**  A uniformly random σ ∈ S_n with
n ≥ (1 + ε) k² (ln k + ln ln k) is a k-superpattern with probability 1 − o(1), for every fixed ε > 0.

*Proof.*  Couple n i.i.d. uniform points Q with Π_N ⊆ Q where N = n/(1+ε/2) ([W11] Remark 0.3: the coupling
holds on {|Π_N| ≤ n}, and Pr(Poisson(N) > n) ≤ e^{−N h(ε/2)} with h(x) = (1+x)ln(1+x) − x > 0, which is
e^{−Ω(n)} ≪ 1/k!).  With C = N/k² = (1+ε)(ln k + ln ln k)/(1+ε/2) =: (1+ε') L, L = ln k + ln ln k, ε' > 0, Theorem
2.1 and the union bound give
   Pr(some π ⊄ Q) ≤ k!·e^{−k(C − 1 − ln C)} + k! e^{−Ω(n)} ≤ exp( k ln k − k(1+ε')L + k + k ln((1+ε')L) ) + o(1),
and k ln k − k(1+ε')(ln k + ln ln k) + k + k ln L + k ln(1+ε') = −ε' k ln k + O(k ln ln k) → −∞.  ∎

*Comment (novelty).*  He–Kwan call n = O(k² log k) "easy"; I have not seen the constant 1 stated.  Theorem 2.1
is also the per-pattern statement that every π has threshold ≤ k² in the Poisson model (rigid-slab threshold
of the identity, [W11] §4 Comment).

## 3. The corner greedy is a copy-finder for exactly the chain-strip patterns (PROVED)

Fix a partition of the values into intervals I_1 < ⋯ < I_r (any sizes) and run the strip greedy of [W11]
Thm 4.4 verbatim: x-level a (global, never reset), level b_j per strip initialised at the bottom of S_{I_j},
positions processed in order, at position p with π(p) ∈ I_j take the minimiser of (x − a) + (y − b_j) on
{x > a, y > b_j} in Π^{(j)}, update a, b_j.

**Proposition 3.1.**  Suppose the run succeeds in the sense of the theorem (every chosen point lies in its
strip and x < 1).  Then the chosen points form a copy of π if and only if π^{-1} is increasing on every I_j.
Otherwise they form a copy of the permutation π' ≠ π obtained from π by sorting, inside every strip, the
values of the strip along the positions of the strip.

*Proof.*  The x-order of the chosen points is the position order (a increases).  The y-order: points in
different strips are ordered by the strips; inside strip j, y(q) > b_j = y(previous chosen point of strip j),
so the points of strip j increase in y along the position order.  Hence the y-rank of the point chosen at
position p is (number of values in lower strips) + (rank of p among the positions of strip j) = π'(p).  The
points form a copy of π iff π' = π iff, in every strip, the values increase along the positions.  ∎

*Consequence.*  The claim "Theorem 4.1's proof goes through verbatim for every π" is FALSE: the occupancy
numbers t_{ij} are irrelevant, but the within-strip order is not.  Smallest counterexample: k = 4, π = 2 3 1 4
(1-indexed), strips {1,2}, {3,4}: strip 1 contains the values 2 (position 1) and 1 (position 3), so π^{-1} is
decreasing on it and the greedy outputs a copy of π' = 1 3 2 4.  Numerically (log.md §2) the verbatim greedy on
a uniformly random π with √k equal strips produced a non-copy in every one of 100 runs at k = 64, 100, 144.
The class for which the greedy works is exactly the unions of increasing runs on the value intervals I_j
(the class 𝓛 of [W11] §0 with the given run lengths), which contains 𝒢(r,h) (h_j = h for all j).

## 4. The mixed greedy: every pattern, with a pattern-dependent threshold in [π/8, 1] (PROVED)

For a value interval I on which π^{-1} is *decreasing* use the *upper* corner: level b_j initialised at the
top of S_I, region {x > a, y < b_j}, score (x − a) + (b_j − y).  For a single value v (a row) use the row
search of §2.

**Theorem 4.1.**  Let π ∈ S_k, C > 0, N = Ck².  Let I_1, …, I_m be a partition of the values into intervals and
J ⊆ [m] a set of indices such that for every j ∈ J, π^{-1} is monotone (increasing or decreasing) on I_j;
write h_j = |I_j| and k_J = Σ_{j∈J} h_j (values of the corner strips), α = k_J/k.  Let X_0, …, X_{k−1} be
independent with X_p ~ U if π(p) ∈ ∪_{j∈J} I_j and X_p ~ Exp(C) otherwise, and let V_1, V_2, … be i.i.d.
copies of V.  Then
   Pr(π ⊄ Π_N) ≤ Pr( X_0 + ⋯ + X_{k−1} ≥ k ) + Σ_{j∈J} Pr( V_1 + ⋯ + V_{h_j} ≥ h_j )
              ≤ exp( −k·sup_{0<θ<C} [ θ − α Λ_C(θ) − (1−α) ln(C/(C−θ)) ] ) + Σ_{j∈J} e^{−c(C) h_j}.
The first exponent is positive iff  α √(π/(8C)) + (1 − α)/C < 1.

*Proof.*  *Processes.*  Extended processes Π^{(j)} for the strips S_{I_j}, j ∈ J, and Π^{(v)} for the rows R_v of
the remaining values v ∉ ∪_J I_j; the regions are disjoint, so the processes are independent.
*Procedure.*  x-level a := 0; for j ∈ J a level b_j := bottom of S_{I_j} if π^{-1} is increasing on I_j, := top
of S_{I_j} if decreasing.  For p = 0..k−1: if π(p) = v is a row value, search A = {x > a} ∩ R_v (extended to
x > 1) for the minimiser of x − a; if π(p) ∈ I_j with j ∈ J increasing (resp. decreasing), search the quadrant
{x > a, y > b_j} (resp. {x > a, y < b_j}) in Π^{(j)} for the minimiser of (x − a) + |y − b_j|; call the point
q_p, set X_p := k(x(q_p) − a), V_p := k|y(q_p) − b_j| (corner steps only), a := x(q_p), b_j := y(q_p).
*Freshness.*  Rows: searched once each.  Corner strip j (increasing case): let the searches in Π^{(j)} be at
positions p_1 < p_2 < ⋯ with corners (a_m, b_m) and explored triangles Δ_m; for m' < m, a_m ≥ x(q_{p_{m'}}) and
b_m ≥ y(q_{p_{m'}}) (a is the x-coordinate of the most recent point, to the right of q_{p_{m'}}; b_m is the
y-coordinate of the previous point of the strip, and the strip's points increase in y), so every point of
the m-th quadrant has score_{m'} > score_{m'}(q_{p_{m'}}) and the quadrant misses Δ_{m'}.  Decreasing case:
reflect y ↦ −y.  So Lemma 1.2 applies to all searches.
*Increments.*  Conditionally on the past, by Lemma 1.2: row steps give X_p ~ Exp(C) (Theorem 2.1); corner
steps give (X_p, V_p) with the law of (U,V) ([W11] Thm 4.1 Step 3; the decreasing case is the mirror image and
has the same law).  These conditional laws do not depend on the past, so all the increments are independent
with the stated marginals.
*Copy.*  Let E := {Σ_p X_p < k} ∩ ∩_{j∈J} {Σ_{p: π(p)∈I_j} V_p < h_j}.  On E, inductively, every chosen point has
x-coordinate Σ_{p' ≤ p} X_{p'}/k < 1; a row point lies in its row R_v ∩ [0,1)²; a corner point of an increasing
strip has y = bottom + (partial sum of the strip's V)/k ∈ [bottom, bottom + h_j/k) = the strip, and similarly
for a decreasing strip.  So all chosen points are points of Π_N.  Their x-order is the position order.
Their y-order: rows and strips are ordered by value intervals; inside a corner strip the points increase
(resp. decrease) in y along the position order, which is the order of their values because π^{-1} is
increasing (resp. decreasing) on I_j.  So the y-order of the chosen points is the order of the values π(p):
they form a copy of π.  Hence Pr(π ⊄ Π_N) ≤ Pr(E^c) ≤ Pr(Σ X_p ≥ k) + Σ_{j∈J} Pr(Σ V ≥ h_j).
*Tails.*  Chernoff: Pr(Σ X_p ≥ k) ≤ inf_θ e^{−θk} (E e^{θU})^{k_J} (E e^{θ Exp(C)})^{k − k_J}, with E e^{θ Exp(C)} =
C/(C−θ) for θ < C; and Pr(Σ_{h_j} V ≥ h_j) ≤ e^{−c(C)h_j} as in [W11].  The first exponent is positive iff the
mean of X_p averaged over p is < 1, i.e. α E U + (1−α)/C < 1 (Cramér).  ∎

**Corollary 4.2 (monotone runs on value intervals, all lengths and directions).**  If π is a union of r
monotone runs on consecutive value intervals of lengths h_1, …, h_r (each run increasing or decreasing), then
for every C > π/8,  Pr(π ⊄ Π_{Ck²}) ≤ e^{−c(C)k} + Σ_j e^{−c(C)h_j}; in particular for 𝒢(r,h) this is [W11]
Thm 4.4, and for unequal lengths the threshold constant π/8 is unchanged while the speed is min_j h_j.
By reflection in the diagonal the same holds for monotone runs on consecutive *position* intervals.

**Corollary 4.3 (every pattern).**  For every π ∈ S_k and every partition into monotone value-runs as above,
Pr(π ⊄ Π_{Ck²}) → 0 as soon as C > C*(π) := the unique root of α√(π/(8C)) + (1−α)/C = 1 and min_{j∈J} h_j → ∞;
C*(π) ∈ (π/8, 1].  Taking J = ∅ recovers Theorem 2.1 (C* = 1).

*Comments.*  (i) For a uniformly random π the maximal monotone runs of π^{-1} on value intervals (the
alternating runs of the sequence π^{-1}(0), π^{-1}(1), …) have mean length 3/2, so α is small unless very
short runs are admitted, and short runs have a large per-strip failure e^{−c(C)h_j}: for random π Theorem
4.1 is effectively Theorem 2.1 (numerically confirmed, log.md §2: admitting runs of length ≥ 3 or ≥ 4 does
not improve on rigid rows at C ≤ 2).  The interpolation is useful for structured patterns only.
(ii) The bound of Theorem 4.1 is tight for the procedure: by Cramér's theorem Pr(Σ_{h} V ≥ h) ≥
e^{−(c(C)+o(1))h}, so the mixed greedy itself fails with probability ≥ e^{−(c(C)+o(1)) min_J h_j}.

## 4B. The reserve greedy: a universal threshold below k² for every pattern (PROVED reduction; NUMERICAL constant)

The corner strips of Theorem 4.1 fail with constant probability when they are short (h_j = 2, 3), which is
the typical situation: the non-overlapping segmentation of the value sequence π^{-1}(0), π^{-1}(1), … into
maximal monotone runs has runs of length ≥ 2 except possibly the last one, with mean length 2.4 for random π
(log.md §4).  Two changes make short strips useful: (i) the search is *restricted to the strip*, so a strip
never overflows and the only failure mode is the x-budget; (ii) a *reserve* of β units of height is kept for
every future point of the strip, which removes the heavy tail that (i) alone produces (log.md §3), and the
last point of a strip is taken leftmost.

**Definition (reserve rule with parameters β ∈ (0,1], λ_1, λ_2, … ≥ 0).**  Values are partitioned into
intervals I_1 < ⋯ < I_m on each of which π^{-1} is monotone, h_j = |I_j|.  State: x-level a (initially 0);
for each strip j a level b_j (initially the bottom of S_{I_j} if increasing, the top if decreasing) and a
counter m_j (initially h_j) of the points still to be placed.  At position p with π(p) ∈ I_j (increasing
case; the decreasing case is the mirror image y ↦ −y):
   ρ_j := k·(top_j − b_j) (remaining scaled height),  ρ^eff := ρ_j − β(m_j − 1);
   if m_j ≥ 2: search A = {x > a, b_j < y < b_j + ρ^eff/k} in Π^{(j)} for the minimiser of (x − a) + λ_{h_j − m_j + 1}(y − b_j);
   if m_j = 1: search A = {x > a, b_j < y < top_j} for the minimiser of x − a (leftmost);
   X_p := k(x(q) − a), V_p := k(y(q) − b_j);  a := x(q), b_j := y(q), m_j := m_j − 1.
A row (h_j = 1) is a strip with m_j = 1: the leftmost search of Theorem 2.1.

**Lemma 4B.1 (state and increments).**  (a) Every search region has scaled height ρ^eff ≥ β (for m_j ≥ 2)
resp. ρ_j ≥ β (for m_j = 1), and all chosen points lie in their strips.  (b) The regions searched in the same
process Π^{(j)} are disjoint from the previously explored sets, so Lemma 1.2 applies.  (c) Conditionally on
the past, (X_p, V_p) has the density  C·exp(−C·A_{ρ,λ}(u + λv))  on {u > 0, 0 < v < ρ}, ρ = ρ^eff, λ = the
current weight, where A_{ρ,λ}(t) = t²/(2λ) for t ≤ λρ and ρt − λρ²/2 for t ≥ λρ (for λ = 0: X_p ~ Exp(Cρ), V_p
uniform on (0,ρ), independent).  This law depends on the past only through ρ^eff of the strip of p.
(d) Conditionally on the past, X_p ≤_st λβ + Exp(Cβ) for corner steps and X_p ≤_st Exp(Cβ) for leftmost steps.

*Proof.*  (a) Induction on the steps of strip j: initially ρ_j = h_j and m_j = h_j, so ρ^eff = h_j − β(h_j−1) ≥ 1
≥ β.  A corner step chooses V_p < ρ^eff, hence the new remaining height ρ_j − V_p > β(m_j − 1), i.e. after
decrementing m_j the new ρ^eff = ρ_j − V_p − β(m_j − 1) > β·1 (and for the last point, ρ_j > β).  Since
V_p < ρ^eff ≤ ρ_j the chosen point is below the top of the strip, and above b_j ≥ bottom.  (b) For two
searches of strip j at positions p' < p with corners (a', b') and (a, b): a ≥ x(q_{p'}) and b = y of the last
point of the strip ≥ y(q_{p'}); every (x,y) in the p-search region has (x − a') + λ'(y − b') > (x(q_{p'}) − a') +
λ'(y(q_{p'}) − b') (λ' ≥ 0), so it is outside the explored sublevel set of the p'-search.  (c) Lemma 1.2 with
ψ = (x − a) + λ(y − b) on A: |{ψ < t} ∩ A| = A_{ρ,λ}(t)/k² after scaling, so the density of the minimiser in
the scaled variables (u, v) = k(x − a, y − b) is (N/k²) e^{−(N/k²)A_{ρ,λ}(u+λv)} = C e^{−C A_{ρ,λ}(u+λv)}.  (d) A
contains the sub-region A_β := {x > a, b < y < b + β/k}; the minimiser's score is ≤ the minimal score on
Π^{(j)} ∩ A_β, which is stochastically ≤ λβ + (leftmost x-distance in A_β) = λβ + Exp(Cβ)/k in scaled units, and
X_p ≤ score.  For the leftmost step the region has height ≥ β.  ∎

**Theorem 4B.2 (reduction).**  For every π ∈ S_k, every partition into monotone value intervals of lengths
h_1, …, h_m and every parameters (β, λ),
   Pr(π ⊄ Π_{Ck²}) ≤ Pr( T_1 + ⋯ + T_m ≥ k ),
where the T_j are independent and T_j has the law of the total x-increment Σ_{p: π(p)∈I_j} X_p of the h_j-step
Markov chain of Lemma 4B.1(c) started at ρ = h_j (a law L(h_j; C, β, λ) depending on nothing else).
Consequently, with M_h(θ) := E e^{θ T} for T ~ L(h; C, β, λ) (finite for θ < Cβ by Lemma 4B.1(d)),
   Pr(π ⊄ Π_{Ck²}) ≤ exp( −sup_{0<θ<Cβ} [ θk − Σ_j ln M_{h_j}(θ) ] ) ≤ exp( −k·sup_θ min_j (θ − ln M_{h_j}(θ)/h_j) ),
and the exponent is positive as soon as  E T_j < h_j for every j.

*Proof.*  *Copy.*  By Lemma 4B.1(a) every chosen point is in its strip; on {Σ_p X_p < k} all x-coordinates are
< 1, so the points belong to Π_N; the x-order is the position order and the y-order is by strips and, inside
a strip, monotone along the positions in the direction of π^{-1} on I_j (levels b_j move monotonically):
a copy of π (as in Theorem 4.1).  Hence Pr(π ⊄ Π_N) ≤ Pr(Σ_p X_p ≥ k) = Pr(Σ_j T_j ≥ k).
*Independence.*  By Lemma 4B.1(c) the joint density of the whole sequence ((X_p, V_p))_p is the product over
p of the transition densities f_{ρ^eff(p)}(X_p, V_p), where ρ^eff(p) is a function of the earlier (V_{p'})
of the *same* strip only.  Grouping the factors by strip shows that the joint law is the product over strips
of the laws of the strip chains: the T_j are independent with the stated laws.
*Chernoff.*  Markov's inequality on e^{θΣT_j} with independence; the last form uses Σ_j ln M_{h_j}(θ) ≤
Σ_j h_j·max_j (ln M_{h_j}(θ)/h_j).  Positivity: θ − ln M_h(θ)/h = θ(1 − E T/h) − O(θ²) as θ ↓ 0 since M_h is
finite on a neighbourhood of 0.  ∎

**Theorem 4B.3 (universal threshold).**  Let C_univ := inf{ C : min_{β,λ} E T/2 < 1 for T ~ L(2; C, β, λ)
and min_{β,λ} E T/3 < 1 for T ~ L(3; C, β, λ) }.  Then for every C > C_univ there is η(C) > 0 such that for
EVERY k and EVERY π ∈ S_k,
   Pr(π ⊄ Π_{Ck²}) ≤ e^{−η(C) k + O(1)},
and a uniformly random σ ∈ S_n with n ≥ (1 + ε) C_univ k² contains any fixed π ∈ S_k with probability 1 − o(1)
(coupling Π_{n/(1+ε/2)} ⊆ Q as in Corollary 2.2).
NUMERICALLY (quad_h2.py, deterministic quadrature for h = 2, cross-checked by two independent Monte Carlo codes;
mc_h3.py for h = 3):  C_univ = 0.757 (attained by h = 2 with β = 0.4, λ = 1.1; h = 3 is strictly easier:
E T/3 = 0.87 at C = 0.76), and the exponents η(0.8) ≥ 0.0014, η(0.85) ≥ 0.0058, η(0.9) ≥ 0.013, η(1) ≥ 0.035,
η(1.2) ≥ 0.096 (rigid rows: 0 for C ≤ 1, 0.018 at C = 1.2).

*Proof.*  Segment the value sequence π^{-1}(0), …, π^{-1}(k−1) into maximal monotone runs from left to right
(a run ends when the next value breaks monotonicity; the next run starts at the following value).  Every run
has length ≥ 2 except possibly the last, because any two consecutive values are monotone.  Split each run of
length h ≥ 2 into consecutive pieces of lengths 2 and 3 (possible for every h ≥ 2), which are still monotone
intervals.  Apply Theorem 4B.2 with this partition and the optimal parameters for h = 2, 3 (a single leftover
value contributes the factor M_1(θ) = C/(C−θ) = e^{O(1)}): the exponent is k·sup_θ min_{h∈{2,3}}(θ − ln M_h(θ)/h)
=: η(C)k, positive for C > C_univ.  De-Poissonisation as in Corollary 2.2.  ∎

*Comments.*  (i) Prior universal per-pattern threshold: 1 (Theorem 2.1, i.e. He–Kwan's thread bound in Poisson
form); Theorem 4B.3 lowers it to 0.757 for all of S_k — the first improvement below k² for arbitrary patterns
that I know of.  The constants are numerical (explicit low-dimensional integrals; a certified evaluation is
routine but was not done).  (ii) The exponent η(C) is tiny near the threshold and grows to ≈ Cβ-ish
speed k for large C; the union bound over S_k still needs C ≍ ln k (Corollary 2.2 is not improved in order).
(iii) Numerical validation with the independent C code (gg runs … 2 1 0.4 1.1; out_scanR2.txt): at C = 0.78,
just above C_univ, success rates 251, 269, 291, 298 out of 300 for k = 100, 200, 400, 800; at C = 0.85: 286,
297, 300 (k = 100, 200, 400); rigid rows at C = 0.9, k = 100: 17%.  Every produced copy passed the O(k²)
order-isomorphism check.  (iv) For structured π (long monotone value-runs) one keeps the long runs unsplit and
the threshold decreases towards π/8 as in Corollary 4.3.  (v) Where does the gain come from?  In a strip of two
values the first point may sit anywhere in the lower 1.6 rows (reserve 0.4) at a cost λ per unit height, and
the second is leftmost in the remaining ≥ 0.4 rows; the x-increments trade against the y-slack that rigid
rows waste.  Longer strips are better (E T/h decreases in h), so the worst case is the pattern whose value
sequence alternates in runs of exactly 2 — e.g. 2 1 4 3 6 5 … and its relatives.

## 5. Speed: a two-phase repair for chain strips, and the barrier (PROVED + HEURISTIC)

### 5.1 Two-phase repair (PROVED)

**Theorem 5.1.**  Let π be a union of r increasing runs on consecutive value intervals of lengths h_1, …, h_r
(e.g. π ∈ 𝒢(r,h)), C > 0, N = Ck², and 0 < δ < 1 with Cδ > 1.  Let T_1, T_2, … be i.i.d. with the law of
T = U + V (Pr(T > t) = e^{−Ct²/2}, E T = √(π/(2C))).  Then
   Pr(π ⊄ Π_N) ≤ Pr( T_1 + ⋯ + T_k ≥ (1−δ)k ) + Σ_j Pr( V_1 + ⋯ + V_{h_j} ≥ h_j ) · Pr( Poisson(Cδ h_j) ≤ h_j − 1 )
              ≤ e^{−c'_δ(C) k} + Σ_j exp( −h_j [ c(C) + Cδ − 1 − ln(Cδ) ] ),
where c'_δ(C) := sup_θ (θ(1−δ) − ln E e^{θT}) > 0 iff (1−δ) > √(π/(2C)).

*Proof.*  *Phase 1.*  Run the strip greedy of Corollary 4.2 (extended strip processes Π^{(j)}, global x-level
a, strip levels b_j) with one change: after choosing q_p with scaled increments (U_p, V_p) set
a := x(q_p) + (V_p + δ)/k.  Do not stop when a strip overflows.  The increments (U_p, V_p) are i.i.d. with the
law of (U,V) exactly as before (the freshness argument only used a ≥ previous x).  Call strip j *good* if
Σ_{p ∈ strip j} V_p < h_j, in which case all its phase-1 points lie in S_{I_j}.
*Phase 2.*  For each bad strip j, in increasing j, build a new chain: level b := bottom of S_{I_j}; for the
positions p of strip j in increasing order, search the open box
   B_p := ( x_p + V_p/k, x_p + (V_p + δ)/k ) × [bottom, top)  of S_{I_j}  (x_p := x(q_p))
in Π^{(j)} for the point minimising ψ(x,y) = y on B_p ∩ {y > b}; call it q'_p and set W_p := k(y(q'_p) − b),
b := y(q'_p).  Strip j is *repaired* if Σ_{p ∈ strip j} W_p < h_j.
*Freshness of phase 2.*  The phase-1 search at p explored the closed triangle Δ_p = {x > a_p, y > b_p,
(x − a_p) + (y − b_p) ≤ (U_p + V_p)/k}, which lies in the vertical band a_p < x ≤ a_p + (U_p+V_p)/k = x_p + V_p/k.
(This band extends to the RIGHT of x_p — the reason for the offset V_p in the box.)  The box B_p lies in the
band x_p + V_p/k < x < x_p + (V_p + δ)/k = a_{next}, to the right of Δ_p and of every earlier triangle of the
strip, and to the left of every later triangle (which start at x > a_{next}); boxes of different positions
are disjoint; boxes of different strips are in different processes.  Hence Lemma 1.2 applies to the phase-2
searches in the order (strip, position): conditionally on everything before, Π^{(j)} ∩ (B_p ∩ {y > b}) is
Poisson of intensity N, and |{ψ < b + t} ∩ B_p ∩ {y > b}| = δt/k, so W_p has conditional density
(Nδ/k²) e^{−(Nδ/k²) w} = Cδ e^{−Cδ w}: the W_p are i.i.d. Exp(Cδ), independent of phase 1.
*Copy.*  Take the phase-1 points of good strips and the phase-2 points of repaired strips.  x-order: for
consecutive positions p < p' the final point of p has x < x_p + (V_p + δ)/k = a used at the search of p' <
x_{p'} ≤ final x of p'.  Everything is inside [0,1)² on Σ_p (U_p + V_p + δ) < k.  y-order: strips are
separated; inside a strip the points form a chain in position order (phase 1: levels increase; phase 2: b
increases); π^{-1} is increasing on each strip.  So we have a copy of π unless some strip is bad and not
repaired.
*Probability.*  Pr(fail) ≤ Pr(Σ T_p ≥ (1−δ)k) + Σ_j Pr(strip j bad and not repaired), and conditionally on
phase 1 (and the phase-2 searches of earlier strips) the W's of strip j are i.i.d. Exp(Cδ), so
Pr(bad and not repaired) = Pr(Σ_{h_j} V ≥ h_j)·Pr(Σ_{h_j} Exp(Cδ) ≥ h_j) = Pr(Σ V ≥ h_j)·Pr(Poisson(Cδh_j) ≤ h_j−1).
Chernoff for both factors as in Theorems 2.1 and 4.1; E T = E[T] = ∫_0^∞ e^{−Ct²/2}dt = √(π/(2C)).  ∎

*Comments.*  (i) Feasible range: Cδ > 1 and 1 − δ > 1.2533/√C force C > 1/δ and δ < 1 − 1.2533/√C, i.e.
C > 6.3 (δ ≈ 0.5); then the per-strip exponent improves from c(C) to c(C) + Cδ − 1 − ln(Cδ), e.g. at C = 8,
δ = 0.5: Cδ − 1 − ln(Cδ) = 1.61, against c(8) ≈ 4 — a 40% gain in the exponent, but only in a regime where the
phase-1 strips essentially never fail (numerically, log.md §6: 0 bad strips in 400 runs at C = 8, h = 4).
The x-budget now pays for U + V + δ instead of U, so the repair is useless below C ≈ 6.3.  (ii) A first
version of this theorem placed the boxes at (x_p, x_p + δ/k) and claimed Δ_p ⊆ {x ≤ x_p}; that is false
(the triangle extends V_p/k to the right of x_p), the numerics caught it (0 of 6 bad strips repaired where
85% were predicted), and the corrected version above is what is proved.  (iii) The gain is a constant factor
in the exponent; Proposition 5.2 shows the speed cannot change.

### 5.2 Why no repair of this kind changes the speed (PROVED for the procedures; HEURISTIC for the truth)

**Proposition 5.2 (the greedies have speed exactly min(k, h)).**  (a) The strip greedy of [W11] Thm 4.4 /
Cor. 4.2 fails with probability ≥ Pr(V_1 + ⋯ + V_{h_1} ≥ h_1) ≥ e^{−(c(C)+o(1))h_1}.  (b) The two-phase
procedure of Theorem 5.1 fails with probability ≥ Pr(Σ_{h_1} V ≥ h_1)·Pr(Poisson(Cδh_1) ≤ h_1−1) ≥
e^{−(c(C) + Cδ − 1 − ln(Cδ) + o(1)) h_1} (the two factors are independent by the proof of Theorem 5.1).  (c) The row greedy of Theorem 2.1 fails with probability exactly
Pr(Poisson(Ck) ≤ k−1) ≥ e^{−k(C − 1 − ln C) − O(ln k)}.
*Proof.*  The failure events of the procedures contain the displayed events (a bad, unrepaired first strip;
Σ X ≥ k), whose probabilities are exact large deviations of i.i.d. sums (Cramér lower bound; for (b) use the
independence established in the proof of Theorem 5.1).  ∎

**Proposition 5.3 (budget barrier for column-by-column procedures) — PROVED.**  Fix a strip S of height h/k
and h disjoint "windows" W_1, …, W_h ⊂ S, W_i = (ξ_i, ξ_i + w_i/k) × S with ξ_1 < ξ_1 + w_1/k ≤ ξ_2 < ⋯, and let
Π be Poisson of intensity N = Ck² on S, independent of the windows.  Let 𝒞 be the event that there is a chain
q_1, …, q_h with q_i ∈ W_i.  Then Pr(𝒞^c) ≥ Pr( Σ_{i} E_i/(C w_i) ≥ h ) where E_i are i.i.d. Exp(1); in
particular if w_i ≤ w for all i then Pr(𝒞^c) ≥ Pr(Poisson(Cwh) ≤ h−1) ≥ e^{−h(Cw − 1 − ln(Cw)) − O(ln h)}.
*Proof.*  The "lowest point above the current level" chain is optimal: by induction, any chain q_1..q_i
through W_1..W_i has y(q_i) ≥ the level reached by the greedy after i windows (if y(q_{i−1}) ≥ level_{i−1}
then q_i is a point of W_i above level_{i−1}, hence y(q_i) ≥ level_i).  So 𝒞 holds iff the greedy chain stays
below the top, and the greedy increments k·(level_i − level_{i−1}) are independent Exp(C w_i).  ∎

*Interpretation (HEURISTIC).*  Any procedure that places the points of one strip while the x-positions of the
neighbouring strips' points are frozen (so that each point of the strip must fall into a window of width
O(1/k) between its x-neighbours in the copy) is subject to Proposition 5.3 with w_i = O(1): its failure
probability per strip is e^{−O(C h)} = e^{−O(N/(k r))}.  Every greedy in this file, every thread of He–Kwan,
and every repair that keeps the other strips fixed is of this kind.  Since the union bound over S_k at
N = Ck² needs a per-pattern failure ≤ e^{−(1+ε)k ln k}, i.e. speed strictly more than k at fixed C, **no
column-by-column procedure can prove Alon's conjecture**; and at speed k the union bound forces C ≳ ln k
(Corollary 2.2), the trivial n = k² ln k.  Any proof of speed > k must move all strips simultaneously — a
genuinely two-dimensional argument (last-passage / non-intersecting-path or LIS-lower-tail type).
By contrast the *true* fixed-strip failure probability is far smaller: [W11] Prop 3.1 and Thm 2.2 locate it
between e^{−N/r} and e^{−N/(4r²(r+1))} for the tilted grid (above an r-dependent threshold), i.e. speed
N/poly(r) ≫ speed h.  The greedy loses a factor ≍ k because it exposes only O(h) of the N/r points of a strip.

### 5.3 What the free-strip / bad-cut route would need (HEURISTIC, with the dead ends of log.md §7)

For the tilted grid a copy is an h × r array of points, x-ordered row-major and y-ordered column-major, rows
and columns being chains.  Failure in the free model requires that every such array be blocked.  A
"bad cut" argument would show that failure forces a monotone curve across the square along which the process
is sparse at scale 1/k over a length Θ(1), costing e^{−Θ(N·(1/k)·1)} = e^{−Θ(Ck)}: speed k again, unless
sparsity at scale 1/k over length 1 is not enough and a width Θ(r/k) band is needed (cost e^{−Θ(Ckr)}).  I
could not prove either implication; the obstacle is that the copy may use points at x-spacing ≫ 1/k in some
rows and ≪ 1/k in others (the free model has no rigid slabs).  The molecule/Mirsky method of [W11] §2 is the
only proved speed-N/poly(r) bound for these patterns and needs C ≳ 8(r+1) ln r.  Recorded as open.

## 6. Summary of what is proved

| statement | class | threshold (N/k²) | failure bound | speed |
|---|---|---|---|---|
| Thm 2.1 | all π ∈ S_k | 1 | Pr(Poisson(Ck) ≤ k−1) ≤ e^{−k(C−1−ln C)} | k |
| Cor 2.2 | all of S_k at once | — | uniform σ ∈ S_n, n ≥ (1+ε)k²(ln k + ln ln k), is a k-superpattern w.h.p. | — |
| Prop 3.1 | — | — | the verbatim strip greedy works iff each strip is a chain; counterexample 2314 | — |
| Thm 4.1 | all π, partition into monotone value-runs (J) + rows | C*(π) ∈ (π/8, 1] | Chernoff(x-sum) + Σ_{j∈J} e^{−c(C)h_j} | min(k, min_J h_j) |
| Thm 4B.2/4B.3 | all π ∈ S_k (reserve greedy, strips of 2–3 values) | 0.757 (NUMERICAL constant; reduction PROVED) | e^{−η(C)k}, η(0.8)≥0.0014, η(1)≥0.035 | k |
| Cor 4.2 | unions of monotone runs on value (or position) intervals, lengths h_j | π/8 | e^{−c(C)k} + Σ_j e^{−c(C)h_j} | min_j h_j |
| Thm 5.1 | same, increasing runs | needs C > 6.3 | e^{−c'_δ k} + Σ_j e^{−h_j(c(C)+Cδ−1−ln Cδ)} | min_j h_j (better constant; practically irrelevant) |
| Prop 5.2/5.3 | — | — | lower bounds: the procedures have exactly these speeds; column-by-column repairs cannot exceed speed h | — |

What remains for Alon's conjecture (n = O(k²) for all of S_k): a per-pattern bound with speed strictly more than k
at fixed C (failure ≤ e^{−(1+ε)k ln k}), which by Propositions 5.2–5.3 cannot come from any greedy or repaired
greedy of the present type.  What this workstream adds on the threshold side: every pattern has threshold
≤ 0.757k² (Thm 4B.3), unions of monotone runs on value/position intervals have threshold ≤ (π/8)k² (Cor 4.2),
and the trivial union bound holds at n = (1+o(1))k²(ln k + ln ln k) (Cor 2.2).
