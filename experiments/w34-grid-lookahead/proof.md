# W34 — cross-strip lookahead for block-grid patterns: below π/8, numerically to 1/4

Date 2026-08-29.  Tags PROVED / NUMERICAL / HEURISTIC.  Background: W11 proof.md §4 (corner greedy, π/8),
W20 proof.md §3–4 (fresh-quadrant barrier Prop 3.1; mean-field theorem 4.2; Bellman C_mf(h) ↓ π/8),
W31 proof.md (windows, safe clock).  Numerics: results.md; chronology and dead ends: log.md.

**Summary.**  (i) The y-lookahead Bellman recursion asked for in goal (1) is W20 Prop 4.3; its optimum
C_mf(h) ↓ π/8, so it never goes below π/8 (§1).  (ii) Prop 3.1 covers every rule that chooses the point of
the current strip from a quadrant that is still Poisson given the past; the only escape is to choose the
point of strip s *using the process of the strips visited next* (x-lookahead across strips = deciding where
the shared x-clock lands).  In the mean-field regime (r → ∞, every strip fresh at each visit) the x-costs
telescope and the optimal round is a first-passage problem across strips (§2); its constant is numerically
γ_∞ = 1.000 ± 0.002, i.e. the threshold 1/4 exactly (§5, NUMERICAL).  (iii) The rigorous version is the
*block rule*: jointly optimal path through b consecutive fresh strip windows, blocks i.i.d.  Theorem 3.4
(PROVED) gives, for the tilted grids (and every π_τ ∈ 𝒢(r,h) whose consecutive rows do not revisit a strip
within b+1 visits) with min(r,h) ≥ (ln k)³, threshold ≤ C^{mix}_b = ((E K_b + E K_{b+1})/(2(2b+1)))², where K_b is
the b-strip first-passage cost at intensity 1: C^{mix}_2 = 0.345, C^{mix}_4 = 0.321, C^{mix}_8 = 0.300, C^{mix}_32 = 0.273,
C^{mix}_64 = 0.266 (Monte Carlo, §4); the pure block constants C_b = (E K_b/(2b))² → 1/4 (NUMERICAL, ≈ 1/4 + 0.105/√b).

## 0. Setting

Π_N Poisson of intensity N = Ck² on [0,1]², k = rh, π = π_τ ∈ 𝒢(r,h) (W11 §4): h rows (slabs), r strips
S_s = [0,1] × [s/r, (s+1)/r), row i visits the strips in the order τ_i(0), …, τ_i(r−1); the FIXED model
(rigid strips, free slabs; W20 §0) asks for a copy with the entry of (row i, strip s) inside S_s.
Scaled strip coordinates x' = kx, y' = k(y − s/r) ∈ [0,h): strip s is a Poisson process of intensity C on
[0,k] × [0,h); extended process Π^{(s)} := (Π_N ∩ S_s) ∪ (independent Poisson(N) on ℝ² ∖ S_s), i.e. Poisson(C)
on the whole plane in strip coordinates, the r processes independent (W11 Thm 4.4).  A copy = one point per
(row, strip), x' increasing in the visiting order, y' increasing within a strip and < h; its cost:
u_t := x'-increment at step t, v_t := y'-increment in the strip; feasibility ⇔ Σ_t u_t ≤ k and, for every
strip, Σ_{its h visits} v ≤ h.

## 1. Goal (1): y-lookahead alone does not beat π/8 (PROVED, by reference)

The rule "at a visit, choose among the fresh points by x-increment + cost-to-go of the strip's remaining
visits as a function of the y-level reached" is a mean-field rule in the sense of W20 §4.1; the exact
cost-to-go is W20's V_m(v) (Prop 4.3, Bellman form, with the intensity C in the exponent), and the best
constant over all such rules is C_mf(h) = root of V_h(0;C) = h, which is ≥ π/8 for every h and ↓ π/8 (W20
Prop 4.5; values 1, 0.750, 0.655, …, 0.472 (h=16)).  Reason: such a rule is fresh-quadrant (W20 Prop 3.1):
whatever the cost-to-go, the chosen point lies in a quadrant that is Poisson given the past, so
E[u+v | past] ≥ 2√(π/(8C)).  Nothing to compute; recorded as a negative.

## 2. Goal (2): what a rule must use, and the first-passage reformulation

**Proposition 2.1 (scope of the barrier; PROVED).**  Let a rule choose, at every step t, the point p_t of
strip s_t from Q_t = {x' > a_t, y' > v_{s_t}} (a_t the clock).  If the conditional law of Π^{(s_t)} ∩ Q_t given
𝔽_t (everything the rule has used so far) is Poisson(C) on Q_t, then E[u_t + v_t | 𝔽_t] ≥ √(π/(2C)), and the
rule cannot succeed for C < π/8 (W20 Prop 3.1).  Conversely the hypothesis fails as soon as 𝔽_t contains
information about Π^{(s_t)} ∩ Q_t, and there are exactly two ways to acquire it:
 (a) the strip s_t was explored beyond the clock at an earlier visit (impossible in the mean-field regime
     r → ∞, where the clock moves Θ(r) between visits while a visit explores O(1): W20 Thm 4.2's F2), or
 (b) the point of an *earlier* step t' < t was chosen after looking at Π^{(s_t)} to the right of the
     candidates for p_{t'} — the clock a_t (a function of p_{t'}) is then correlated with Π^{(s_t)}.
So in the mean-field regime, x-lookahead across strips (b) is the *only* information that can beat π/8; the
y-lookahead of §1 and any in-quadrant lookahead are covered by the barrier.  ∎  (Trivial from the definitions;
stated to answer goal (2) precisely.)

**The round problem.**  Consider one round (row) in the mean-field regime: the r strips are visited once each,
in some order, and every strip's process to the right of the clock is fresh at the start of the round.  Cost
of the round with clock a at its start and levels v_s:  Σ_t u_t + λ Σ_t v_t = (x'_{last} − a) + λ Σ_s (y'_s − v_s):
*the x-costs telescope*.  Relabel the strips in visiting order 1..n (n = r) and translate y so that all levels
are 0.  With weight λ = 1:

   K_n := min { x_n + Σ_{s=1}^{n} y_s :  p_s = (x_s, y_s) ∈ Ψ_s,  0 < x_1 < x_2 < ⋯ < x_n },            (2.1)

Ψ_1, …, Ψ_n independent Poisson processes of intensity 1 on (0,∞)².  Backward recursion (PROVED, immediate):

   G_{n+1}(x) := x,   G_s(a) := min_{p ∈ Ψ_s, x_p > a} [ y_p + G_{s+1}(x_p) ],   K_n = G_1(0);            (2.2)

each G_s is a nondecreasing step function with jumps at the points of Ψ_s, so (2.2) is computed exactly by a
suffix minimum (fpp.py; validated against exhaustive enumeration, check_dp.py, 300 instances).

**Lemma 2.2 (scaling; PROVED).**  Let K_n(λ, C) be the minimum of (x_n − 0) + λ Σ y_s over n independent
Poisson processes of intensity C.  Then K_n(λ, C) =_d √(λ/C) · K_n(1,1).  Consequently, writing g_n(λ) :=
E K_n(λ, 1) = √λ · E K_n, the mean x-part X* := E x_n and the mean y-part Y* := E Σ y_s of the (a.s. unique)
minimising path at λ = 1 satisfy  X* = Y* = E K_n / 2.

*Proof.*  For a Poisson(C) process put y' = λy (intensity C/λ),
then x'' = √(C/λ)·x', y'' = √(C/λ)·y' (intensity 1); the cost x + λy = x' + y' = √(λ/C)(x'' + y'').  For the
second claim: K_n(λ) = min over finitely many candidate paths P (a.s.; only points with x < K_n(1)+1 and
y < K_n(1)+1 can matter for λ near 1) of X_P + λY_P, a concave piecewise-linear function of λ; the minimiser
at λ = 1 is a.s. unique (the costs have continuous joint laws), so ∂_λ K_n(λ)|_{λ=1} = Y_{P*} a.s., and
0 ≤ (K_n(1+δ) − K_n(1))/δ ≤ Y_{P*} ≤ K_n(1) with E K_n(1) < ∞ (K_n ≤ Σ_s T_s, T_s the corner-greedy increments,
Gaussian tails).  Dominated convergence: g_n'(1) = E Y_{P*} = Y*.  But g_n(λ) = √λ g_n(1), so Y* = g_n(1)/2, and
X* = g_n(1) − Y* = g_n(1)/2.  ∎

**Definition.**  γ_n := E K_n / n and C_n := (γ_n/2)² = (E K_n/(2n))².  γ_1 = E min(x+y) = √(π/2), C_1 = π/8.

## 3. The block rule and the reduction (PROVED)

Fix b ≥ 1 and C > 0; put L := √((b+9) ln k / C) (window length and height).  Write E K_n for the mean of
(2.1) at intensity 1 and define the *mixed* per-visit cost and constant

   γ^{mix}_b := (E K_b + E K_{b+1}) / (2b+1),      C^{mix}_b := (γ^{mix}_b / 2)²                       (3.1)

(renewal-reward: blocks of size b or b+1 with probability ½ each have mean cost (E K_b + E K_{b+1})/2 and mean
size b + ½).  Numerically C^{mix}_b lies between C_b and C_{b+1} (§4).

**The partition.**  Concatenate the rows: visit t = ir + s' is the (s'+1)-th strip of row i, t = 0..k−1.
Independently of Π_N, cut the visit sequence into consecutive *blocks* by a stationary discrete-time renewal
process with i.i.d. block sizes uniform on {b, b+1}: the block containing visit 0 has size b with probability
b/(2b+1) (size-biased) and visit 0 is at a uniform position in it; subsequent sizes are i.i.d.  Standard
fact (stationary delayed renewal process): for *every* t, the (size, position) of visit t has this same
stationary law — size b w.p. b/(2b+1), position uniform in the block — so every visit is in a size-b block at
a uniform position with probability b/(2b+1) and in a size-(b+1) block at a uniform position otherwise.
The last block may be truncated by the end of the sequence (its cost is ≤ (b+1)L, negligible).

**Hypothesis (H_b) on τ.**  Every block contains b+1 ≤ r−1 consecutive visits, so its strips are distinct
iff no strip is visited twice within any window of b+1 consecutive visits.  For the tilted grid (τ_i = id)
this holds since the visiting sequence is periodic with period r.  In general (H_b): for every i, the last b
entries of τ_i and the first b entries of τ_{i+1} are disjoint sets.  (General τ ∈ 𝒢(r,h) is discussed in
Remark (v).)

**The rule R_b.**  State: clock a ≥ 0 (scaled x' of the last chosen point; 0 initially); for every strip s its
level v_s (0 initially) and explored edge e_s (0 initially).  For a block with strips s_1, …, s_{b'} (b' ∈
{b, b+1}, distinct by (H_b), in visiting order):

 1. *Safe clock.*  a* := max(a, e_{s_1}, …, e_{s_{b'}}).  Windows R_j := (a*, a* + L) × (v_{s_j}, v_{s_j} + L) in
    strip s_j's coordinates.  Set e_{s_j} := a* + L for all j (before choosing).
 2. *Block optimisation.*  Among all paths (p_1, …, p_{b'}) with p_j ∈ Π^{(s_j)} ∩ R_j and x'(p_1) < ⋯ < x'(p_{b'}),
    choose the one minimising (x'(p_{b'}) − a*) + Σ_j (y'(p_j) − v_{s_j}) (a.s. unique).  If no path exists: STOP
    (failure F1).  Otherwise set a := x'(p_{b'}), v_{s_j} := y'(p_j).

If after all k visits a ≤ k and every strip has v_s < h, the chosen points are points of Π_N (each lies in its
strip since v_s < h, and x' ≤ k), x'-increasing in visiting order and y'-increasing within each strip: by W11
Lemma 0.1 (fixed version) / W20 Prop 1.1 they form a copy of π_τ in the FIXED model.

**Lemma 3.1 (freshness; PROVED).**  Condition on 𝔽 := the partition and everything used before the block
optimisation of a given block (all earlier choices and Π^{(s)} on all earlier windows of all strips).  Then
Π^{(s_j)} ∩ R_j, j = 1..b', are independent Poisson processes of intensity C on R_j, independent of 𝔽.

*Proof.*  All earlier windows of strip s_j lie in {x' ≤ e_{s_j}} (the edge is set to the right end of each
window and is nondecreasing), and R_j ⊂ {x' > a*} ⊂ {x' > e_{s_j}}; windows of distinct strips concern
independent processes; R_j is 𝔽-measurable.  So W19 Lemma 1.2 / W20 Thm 4.2 ("freshness") applies: the
restriction of a Poisson process to an 𝔽-measurable set disjoint from everything 𝔽 has looked at is
conditionally Poisson.  ∎

**Lemma 3.2 (block cost law; PROVED).**  Conditionally on 𝔽, the block's variables (x'(p_j) − a*, y'(p_j) −
v_{s_j})_j have the law of the minimising path of the windowed problem
   K^{L}_{b'} := min { x_{b'} + Σ_j y_j : p_j ∈ Ψ_j ∩ (0,L)², x_1 < ⋯ < x_{b'} }   (Ψ_j i.i.d. Poisson(C) on (0,L)²),
which depends on 𝔽 only through b'.  Hence, conditionally on the partition, the block costs (offsets
excluded) of all blocks are independent, with a law depending only on the block size; and for each strip s the
y-increments (v_{s,i})_{i<h} of its h visits are independent, the i-th having the law of the y-part at the
(size, position) of that visit.

*Proof.*  Lemma 3.1 and translation invariance (a*, v_{s_j} are 𝔽-measurable shifts); each block's variables
are a function of its own fresh windows; a strip's visits lie in distinct blocks under (H_b).  ∎

**Lemma 3.3 (window limit; PROVED).**  Let X^L_{b'} := E[x-part] and Y^L_{b',j} := E[y-part at position j] of
the windowed problem at intensity C and X*_{b'}, Y*_{b',j} the unwindowed ones.  Then X^L_{b'} → X*_{b'} and
Y^L_{b',j} → Y*_{b',j} as L → ∞, and the windowed problem is infeasible with probability ≤ b' e^{−CL²/b'}.

*Proof.*  On A_L := {the unwindowed minimising path has x_{b'} < L and all y_j < L} the two problems have the
same minimiser.  Pr(A_L^c) ≤ Pr(K_{b'} ≥ L) ≤ Pr(Σ_j T_j ≥ L) → 0 (T_j i.i.d. corner-greedy increments; the
corner path is feasible so K_{b'} ≤ Σ T_j; Gaussian tails).  Off A_L the windowed parts are ≤ b'L when feasible,
and L·Pr(K_{b'} ≥ L) → 0; the unwindowed parts are integrable.  Feasibility: split each window into b' vertical
sub-windows of width L/b'; if the j-th sub-window of strip j is nonempty for every j (each fails with
probability e^{−CL²/b'}) an x-ordered path exists.  ∎

**Theorem 3.4 (block-rule threshold; PROVED reduction, constant (3.1) NUMERICAL).**  Fix b ≥ 1 and
C > C^{mix}_b.  Then Pr(π_τ ⊂_fix Π_{Ck²}) → 1 uniformly over τ satisfying (H_b), as r, h → ∞ with
min(r, h) ≥ (ln k)³ (k = rh; e.g. the diagonal r = h, and the tilted grid (12⋯r)^h).  Consequently (fixed-strip
containment implies containment; W11 Remark 0.3) a uniformly random σ ∈ S_n with n ≥ 2C(1+o(1))k² contains
every such π w.h.p.

*Proof.*  By Lemma 2.2 at intensity C (scaling by √C), the unwindowed size-b' block has mean x-part
E K_{b'}/(2√C) and mean total y-part E K_{b'}/(2√C).  Per visit, under the stationary partition, the mean
x-part is [ (b/(2b+1))·E K_b/(2b) + ((b+1)/(2b+1))·E K_{b+1}/(2(b+1)) ]/√C = γ^{mix}_b/(2√C) =: ρ, and the mean
y-part of a visit at a uniform position of a size-b' block is E K_{b'}/(2b'√C), hence the mean y-increment of
any visit is also ρ.  C > C^{mix}_b means ρ < 1; fix δ > 0 with ρ + 3δ < 1, and L_0 such that for L ≥ L_0 the
windowed means (Lemma 3.3, both sizes, all positions) are within δ of the unwindowed ones; for k large L ≥ L_0.

*F1 (an infeasible block).*  ≤ k blocks, each infeasible with probability ≤ (b+1) e^{−CL²/(b+1)} = (b+1)k^{−(b+9)/(b+1)}
≤ (b+1) k^{−1−8/(b+1)} (conditionally on 𝔽, Lemma 3.1): Pr(F1) ≤ (b+1) k^{−8/(b+1)} → 0.

*F2 (offsets).*  The offset a* − a of a block is ≤ L and is nonzero only if some strip s_j has e_{s_j} > a,
i.e. the block of its previous visit started at a clock a' with a' + L > a.  Under (H_b) two visits of a strip
are separated by ≥ r − 2b visits (the strips of row i after s and of row i+1 before s; for the tilted grid
exactly r − 1), hence by ≥ (r − 2b)/(b+1) − 2 ≥ r/(2b+2) complete blocks (k large).  On F1^c each complete block
advances the clock by x'(p_{b'}) − a* ≥ x'(p_1) − a* ≥ W := min(L, the x'-distance of the first point of R_1),
and conditionally on the past W ≥_st min(L, Exp(CL)) (R_1 has height L), independently across blocks (fresh).
If the total advance over m := r/(2b+2) blocks is ≤ L then no W hit the cap, so
   Pr(advance ≤ L) ≤ Pr(Σ_m Exp(CL) ≤ L) ≤ (eCL²/m)^m = ( 2e(b+1)(b+9) ln k / r )^{r/(2b+2)}
(Chernoff as in W20 Thm 4.2, F2).  For r ≥ (ln k)³ the base is ≤ c_b/(ln k)² and the exponent ≥ (ln k)³/(2b+2),
so this is ≤ k^{−3} for k large.  Union over the k visits: Pr(some offset at a visit separated by ≥ r − 2b
visits from the previous one) ≤ k^{−2}.  So off an event of probability ≤ k^{−2} + Pr(F1), all offsets vanish.

*F3 (x-budget).*  On F1^c ∩ F2^c, a_k = Σ_{blocks} x-part.  Conditionally on the partition the x-parts are
independent, in [0, L], with mean ≤ ρ·(size) + δ·(size) by Lemma 3.3 and the computation of ρ (the partition
is stationary, so Σ_{blocks} E[x-part | partition] = Σ_t E[x-part per visit] ≤ k(ρ + δ) + (b+1)L).  Hoeffding
(≤ k blocks, range L): Pr(a_k ≥ k(ρ + 2δ)) ≤ exp(−2(kδ)²/(kL²)) = exp(−2kδ²/L²) → 0.

*F4 (y-budgets).*  Fix a strip s.  Its h increments are independent given the partition (Lemma 3.2), each in
[0, L], the i-th with conditional mean Y^L_{size,pos} ≤ Y*_{size,pos} + δ; averaging over the stationary law of
(size, pos) of visit ir + τ_i^{-1}(s) gives E[v_{s,i}] ≤ ρ + δ.  Since the partition is independent of the
Poisson processes, use Azuma on the martingale
Σ_i (v_{s,i} − E[v_{s,i} | partition]) (increments bounded by L): Pr(Σ_i v_{s,i} ≥ h(ρ + 3δ)) ≤
Pr(Σ_i E[v_{s,i}|partition] ≥ h(ρ+2δ)) + exp(−2hδ²/L²).  The first term: Σ_i E[v_{s,i}|partition] is a function
of the (size,pos) of h visits spaced by r under the renewal process; by the exponential mixing of a finite
aperiodic renewal process, the (size,pos) at visits ir + p_i, i < h, spaced by ≥ r − 2b ≫ b, are within total
variation e^{−c r} of independent stationary copies, so this is a sum of h bounded variables with mean ≤ ρ + δ
each, i.i.d. up to an error he^{−cr} in probability: Hoeffding gives ≤ exp(−2hδ²/L²) + h e^{−cr}.  Altogether
Pr(strip s overflows) ≤ 2 exp(−hδ²C/((b+9) ln k)) + h e^{−cr}; the union over r strips → 0 since h ≥ (ln k)³
≫ ln r · ln k and r ≥ (ln k)³.

On F1^c ∩ F2^c ∩ F3^c ∩ F4^c the construction succeeds, and each failure probability → 0 uniformly in τ
satisfying (H_b).  ∎

*Remarks.*  (i) b = 1 is W11's corner greedy in windowed form (K_1 = min(x+y), E K_1 = √(π/2)); C^{mix}_1 =
((√(π/2) + E K_2)/3)²/4 = 0.369 already beats π/8 because half the blocks are pairs.  (ii) The failure
probability is only polynomially small in k (F2 union bound); W11 Thm 4.4's speed min(r,h) is lost.  (iii) The
constants are means of explicit finite-dimensional functionals of ≤ b+1 Poisson processes, evaluated by Monte
Carlo (§4), not certified; for b = 2 the certification route is a Feynman–Kac equation for the running minimum
of strip 1 (log.md §4).  (iv) The regime min(r,h) ≥ (ln k)³ is crude; the theorem is about the diagonal-type
limits, where W11 Thm 4.4 gave π/8.  (v) General τ ∈ 𝒢(r,h) without (H_b): a strip revisited within b+1
visits would appear twice in a block.  Splitting such blocks produces short blocks whose y-means (e.g. the
corner greedy's √(π/8C) for a singleton) can exceed 1 at C < π/8, and a strip may be in that situation in
every row (e.g. τ_i alternating id and reverse); the fix (per-strip Lagrange weights λ_s) was not carried out.
So the theorem covers the tilted grids and all τ with (H_b), not all of 𝓕(r,h,ε); W11's π/8 remains the
bound for the rest.

## 4. The constants C_b (NUMERICAL, Monte Carlo with standard errors; blocks.py)

E K_b computed by the exact DP (2.2) on i.i.d. samples of b Poisson(1) strips on [0, 2b+12] × [0, 8]
(the caps only remove paths, so any bias is upward, i.e. conservative for C_b); M samples; standard error se.

| b | M | E K_b ± se | E K_b/b | E x-part /b | E y-part /b | C_b = (E K_b/2b)² | C_b at +2se |
|---|---|---|---|---|---|---|---|
| 1 | 20000 | 1.2550 ± 0.0046 | 1.2550 | 0.625 | 0.630 | 0.3937 (exact π/8 = 0.3927) | 0.3996 |
| 2 | 20000 | 2.3857 ± 0.0058 | 1.1928 | 0.595 | 0.598 | 0.3557 | 0.3592 |
| 3 | 20000 | 3.4754 ± 0.0067 | 1.1585 | 0.578 | 0.581 | 0.3355 | 0.3381 |
| 4 | 20000 | 4.5628 ± 0.0073 | 1.1407 | 0.572 | 0.568 | 0.3253 | 0.3274 |
| 8 | 10000 | 8.7979 ± 0.0131 | 1.0997 | 0.552 | 0.548 | 0.3024 | 0.3042 |
| 16 | 6000 | 17.076 ± 0.021 | 1.0672 | 0.534 | 0.533 | 0.2847 | 0.2862 |
| 32 | 3000 | 33.491 ± 0.038 | 1.0466 | 0.520 | 0.527 | 0.2738 | 0.2751 |
| 64 | 1500 | 65.949 ± 0.066 | 1.0305 | 0.517 | 0.514 | 0.2655 | 0.2665 |
| 128 | 600 | 130.70 ± 0.13 | 1.0211 | 0.510 | 0.511 | 0.2607 | 0.2617 |
| 256 | 200 | 259.41 ± 0.31 | 1.0133 | 0.513 | 0.500 | 0.2567 | 0.2579 |

High-precision runs (blocks_b*_hp.out): E K_2 = 2.3868 ± 0.0019 (M = 2·10⁵), E K_3 = 3.4885 ± 0.0030 (10⁵),
E K_4 = 4.5637 ± 0.0033 (10⁵); partners E K_5 = 5.6314 ± 0.0079, E K_9 = 9.8394 ± 0.0154, E K_17 = 18.092 ± 0.026,
E K_33 = 34.467 ± 0.046, E K_65 = 67.025 ± 0.091 (blocks_pairs_*.out).  Mixed constants (3.1):

| b | γ^{mix}_b = (E K_b + E K_{b+1})/(2b+1) | C^{mix}_b | C^{mix}_b at +2se |
|---|---|---|---|
| 1 | 1.2140 | 0.3685 | 0.3706 |
| 2 | 1.1751 | 0.3452 | 0.3463 |
| 3 | 1.1503 | 0.3308 | 0.3320 |
| 4 | 1.1328 | 0.3208 | 0.3225 |
| 8 | 1.0963 | 0.3005 | 0.3022 |
| 16 | 1.0657 | 0.2839 | 0.2854 |
| 32 | 1.0455 | 0.2733 | 0.2746 |
| 64 | 1.0308 | 0.2656 | 0.2666 |

The x- and y-parts are equal within noise, as Lemma 2.2 predicts.  E K_b − b ≈ 0.21√b (b = 4: 0.56, 16: 1.08,
64: 1.95, 256: 3.41), so γ_b = 1 + 0.21 b^{−1/2} and C_b ≈ 1/4 + 0.105 b^{−1/2} (NUMERICAL fit).

## 5. The infinite-lookahead constant: γ_∞ = 1, threshold 1/4 (NUMERICAL)

fpp.py evaluates G_1(0)/n for n strips (2.2) at intensity 1; this is the round cost per strip of the
*globally optimal* round (all r strips looked at), i.e. the best any rule can do in the mean-field FIXED model
with linear y-cost, and also lim_b γ_b.  Values (results.md §1): n = 1000: 0.999, 1.001, 1.007; n = 2000
(6 seeds): 1.0057, 1.0016, 0.9972, 1.0027, 1.0075, 1.0010; n = 4000: 1.0015, 1.0047, 1.0048; n = 8000: 1.0015,
0.9997.  So γ_∞ = 1.000 ± 0.002 and

   C*_∞ := γ_∞²/4 = 0.250 ± 0.001.

**Conjecture 5.1 (HEURISTIC/NUMERICAL).**  γ_∞ = 1 exactly, i.e. lim_{b→∞} C_b = 1/4: in the FIXED model with
r ≫ h ≫ 1 (and, by Theorem 3.4's regime, on the diagonal r = h → ∞) the tilted grids and all block-grid
patterns have threshold exactly 1/4·k², the value of Alon's conjecture — and W20 Conjecture 4.6 (mean-field
rules are optimal at fixed h as r → ∞) is FALSE for large h, since C_mf(h) ≥ π/8 > C_b for b ≥ 2 and every h
large enough (Theorem 3.4 needs h ≥ (ln k)³ only through the union bound; at fixed h the same block rule has
mean cost bρ per block and W20 Thm 4.2's proof applies verbatim with strip costs replaced by block costs,
giving limsup_r C^fix(r,h) ≤ C_b + O(1/h) — the y-cap loss — which is < C_mf(h) once h is large).

What is proved about γ_∞: π/8-barrier gives nothing (it is a statement about fresh quadrants); trivially
γ_∞ ≤ γ_b for every b (a block path is a feasible round path), and γ_∞ ≥ ? — no lower bound beyond the
first-moment 1/e²-type bounds of the ledger.  A natural guess for a proof of γ_∞ = 1 is a Burke-type
stationary solution of (2.2) (G_{s}(x) − x stationary in x for a suitable boundary noise), by analogy with
Hammersley's process; not attempted (log.md §5).

## 6. Goal (3): the FREE model (HEURISTIC; one PROVED inequality)

PROVED: C^{free}(r,h) ≤ min(C^{fix}(r,h), C^{fix}(h,r)) (W20 Remark 4.7), so Theorem 3.4 transfers to the FREE
model and to both strip directions; on the diagonal the two coincide.

HEURISTIC: in the FIXED model the only per-strip constraint is the y-budget h; with the block rule the
per-strip y-usage is a sum of h independent increments of mean hρ with fluctuations O(√h), so a FREE copy that
*reallocates* budget between strips (the strip boundaries are the copy's to choose) gains only at the level
of fluctuations, O(√h) per strip, i.e. a relative gain O(h^{−1/2}) → 0.  The first-order gain of the FREE model
must come from non-rigid geometry (strip boundaries that are not horizontal lines), which is outside the
sequential fresh-window framework; if Conjecture 5.1 holds there is nothing left to gain at first order for
block-grid patterns anyway (1/4 is conjecturally the truth for every pattern), while W20's numerics for
(12)^h (FIXED 0.254 at k = 256 → ≈ 0.22 extrapolated) show that at *bounded* r the non-mean-field regime
(strips explored contiguously, Hammersley-like) goes below 1/4 in the FIXED model already.  A reserve-based
adaptive-boundary rule (W29/W31 style) was not designed for lack of time; noted as open in results.md.

## Coordinator's verification note (main session, 2026-08-29 21:10)
Lemma 2.2, Lemmas 3.1–3.3 and Theorem 3.4 (F1–F4) re-derived; the stationary renewal partition argument
(every visit at a uniform block position ⇒ per-visit means ρ for x and for every strip's y) is correct.
Constants recomputed with an independent suffix-minimum first-passage code (scratchpad/w34check.py):
E K_1 = 1.254 (√(π/2) ✓), E K_2 = 2.393 ± 0.006, E K_4 = 4.574 ± 0.010, E K_16 = 17.12 ± 0.04,
E K_64 = 66.23 ± 0.15, γ_1000 ≈ 0.99–1.01 — all consistent with §4–5 within Monte-Carlo error.
One slip: the consequence sentence of Theorem 3.4 says "n ≥ 2C(1+o(1))k²"; the correct statement is
n ≥ (1+ε)Ck² (fixed containment ⇒ containment; Poisson/uniform coupling as in W19 Cor. 2.2). Folded as Theorem 18.
