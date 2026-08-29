# W20 — the threshold constant of tilted grids: models, exact cases, the mean-field (r → ∞) theory

Date 2026-08-29.  Every statement is labelled PROVED / HEURISTIC / NUMERICAL.  Numerics, dead ends and
chronology are in log.md.  Background: W11 proof.md §4 (corner greedy, Theorems 4.1/4.4, threshold π/8),
W17 proof.md §1, §5 (renewal principle; why one-block rules cap at 0.8 of the truth).

## 0. Three models and their ordering

Π_N is a Poisson process of intensity N = Ck² on [0,1]²; k = rh; the tilted grid is π(ir+s) = sh + i
(0 ≤ i < h, 0 ≤ s < r), i.e. the periodic word (12⋯r)^h: r increasing runs ("strips", letter s ↔ value
block [sh,(s+1)h)) of length h, interleaved periodically; equivalently h increasing runs ("slabs") of length r
on position blocks.  A copy of π in a point set consists of points p_{i,s} with

  x(p_{i,s}) increasing in (i,s) lexicographically,   y(p_{i,s}) increasing in (s,i) lexicographically.   (0.1)

Three containment notions, with strips S_s = [0,1] × [s/r, (s+1)/r) and cells Z_{i,s} = [ (ir+s)/k, (ir+s+1)/k ) × S_s:

* FREE:  π ⊂ Π_N (ordinary containment; this is what "a uniformly random permutation contains π" means).
* FIXED (rigid strips, free slabs; the model of W11 Theorem 4.4 and of tg.c):  a copy with p_{i,s} ∈ S_s.
* CELL  (rigid strips and rigid x-cells of width 1/k):  a copy with p_{i,s} ∈ Z_{i,s}.

CELL ⇒ FIXED ⇒ FREE, hence for the half-probability thresholds N_{1/2}^{free} ≤ N_{1/2}^{fix} ≤ N_{1/2}^{cell}.
Write C^{model}(r,h) := N_{1/2}^{model}(r,h)/k².

**Scaled coordinates.**  In strip s put x' = kx, y' = k(y − s/r) ∈ [0,h).  Under this map Π_N ∩ S_s becomes a
Poisson process of intensity N/k² = C on [0,k] × [0,h): each strip is a Poisson process of intensity C on a
k × h rectangle; the x'-budget is k = rh for all k points together (mean 1 per point), the y'-budget is h per
strip (mean 1 per point).  All limits below are stated in these units.

## 1. Reformulations (PROVED)

**Proposition 1.1 (colour model).**  Let Ψ be a Poisson process of intensity N on [0,1]² whose points carry
i.i.d. uniform colours in {0,…,r−1}.  Then Pr(π ⊂_fix Π_N) = Pr(Ψ contains points q_0, …, q_{k−1} with
x(q_0) < ⋯ < x(q_{k−1}), colour(q_t) = t mod r, and y increasing along each colour class).

*Proof.*  The map (x,y) ↦ (x, ry − s) on S_s (s = ⌊ry⌋), with colour s, sends Π_N to a Poisson process of
intensity N on [0,1]² (mapping theorem; each strip has intensity N·(1/r) per unit area after the y-stretch by r,
and the r images are independent and superpose to intensity N) whose colours are i.i.d. uniform (colouring
theorem).  A copy with p_{i,s} ∈ S_s is exactly a sequence q_t = image of p_{⌊t/r⌋, t mod r} with the stated
properties, and conversely (within a strip the map is increasing in y).  ∎

**Proposition 1.2 (exact dynamic programme; the state of tg.c).**  Process the points of Π_N in increasing x.
For t ≤ k let F_t ⊂ ℝ^r be the set of vectors ℓ = (ℓ_0,…,ℓ_{r−1}) such that the first t letters of the word
can be embedded (FIXED notion) in the points seen so far with ℓ_s = the y-coordinate of the last point used in
strip s (ℓ_s = −∞ if none).  Then: (i) feasibility of any continuation depends on ℓ monotonically (ℓ ≤ ℓ'
coordinatewise and ℓ' feasible ⇒ ℓ feasible), so F_t can be replaced by its set of minimal elements (Pareto
front); (ii) a new point (x, y) in strip s = t mod r updates each ℓ ∈ F_t with ℓ_s < y to ℓ[s ← y] ∈ F_{t+1};
(iii) π ⊂_fix Π_N iff F_k ≠ ∅ at the end.  For FREE containment the state additionally carries the y-coordinate
f_s of the first point of each strip s ≥ 1 (the strip bottoms), with the condition that a point placed in strip
s lies above all ℓ_{s'} (s' < s) and below all f_{s'} (s' > s).  Both are implemented in tg.c (validated
against brute force on 7200 samples, W11 log §6.1).

*Proof.*  (i) If ℓ ≤ ℓ' and a continuation uses points above ℓ'_s in strip s, the same points are above ℓ_s.
(ii)–(iii) are the definitions.  For FREE: a copy is r separated chains (W11 Lemma 0.1(b)); separation of
chain s from chains s' < s is the condition "above all their points", i.e. above their tops ℓ_{s'}, and from
chains s' > s "below all their points", i.e. below their bottoms f_{s'}.  ∎

## 2. Exact constants in the degenerate directions (PROVED)

**Theorem 2.1 (CELL model: constant 1).**  In the CELL model each strip succeeds independently, with
   Pr(strip s succeeds) = Pr( Γ(h,1) < Ch ),
so Pr(π ⊂_cell Π_{Ck²}) = Pr(Γ(h,1) < Ch)^r.  Consequently C^{cell}(r,h) → 1 as h → ∞ for every r = r(h)
(and for C < 1, Pr → 0 exponentially in h; for C > 1, Pr → 1 provided r e^{−hI(C)} → 0, I(C) = C − 1 − ln C).

*Proof.*  Fix a strip.  The cells Z_{i,s}, i = 0..h−1, are disjoint, each of area 1/(kr), containing
independent Poisson(N/(kr)) = Poisson(Ch·(1/r)·…) — in scaled units, independent Poisson processes of intensity
C on [0,1) × [0,h).  A copy needs a point in every cell of the strip with increasing y'.  The lowest attainable
level after cell i is the greedy one (the state is a single number and lower is better, Proposition 1.2(i) with
r = 1 per strip), and the lowest point of cell i above the level ℓ has y' − ℓ ~ Exp(C) (the number of points of
cell i in [ℓ, ℓ + t] is Poisson(Ct)), independent of the past by the independence of the cells.  So the strip
succeeds iff E_1 + ⋯ + E_h < h for i.i.d. Exp(C), i.e. Γ(h,1) < Ch.  Strips are independent (disjoint regions).
The limits are Cramér's theorem for the Gamma law.  ∎

**Theorem 2.2 (FIXED model, h = 1: constant 1).**  For h = 1 (π = identity of length k = r, one value per
strip), Pr(π ⊂_fix Π_N) = Pr(G_1 + ⋯ + G_r ≤ |Π_N|) where G_i are i.i.d. Geometric(1/r) on {1,2,…}
(independent of |Π_N| ~ Poisson(N)).  Hence N_{1/2}^{fix}(r,1) = k² + O(k^{3/2}) and C^{fix}(r,1) → 1.

*Proof.*  By Proposition 1.1 with h = 1 the y-conditions are void: containment means that the colour word
(i.i.d. uniform letters, length |Π_N|) contains 0 1 ⋯ (r−1) as a subsequence.  The leftmost embedding is optimal
for subsequence containment, and its waiting times are i.i.d. Geometric(1/r).  Mean r², variance
r²·r(1−1/r) ≤ r³; Chebyshev gives the O(k^{3/2}).  ∎

**Proposition 2.3 (colour-word lower bound for FIXED).**  For every r, h:  if N ≤ (1 − ε) k r then
Pr(π ⊂_fix Π_N) ≤ Pr(Poisson(N) ≥ (1−ε/2)kr) + Pr(Σ_{t<k} G_t ≤ (1−ε/2)kr) → 0 (G_t i.i.d. Geometric(1/r)).
Hence C^{fix}(r,h) ≥ (1 − o(1))/h: for h ≤ 3 the FIXED constant exceeds 1/4 (h = 1: 1; h = 2: ≥ 1/2; h = 3: ≥ 1/3).

*Proof.*  Ignore the y-conditions: the colour word must contain (0 1 ⋯ r−1)^h, and the leftmost embedding
needs Σ_{t<k} G_t letters.  Chebyshev as above.  ∎

**Fact 2.4 (r = 1).**  For r = 1 all three models coincide with "LIS ≥ k", whose threshold is k²/4 (Hammersley,
Vershik–Kerov, Logan–Shepp; finite-size N_{1/2} = k²/4 + Θ(k^{5/3}) by Baik–Deift–Johansson).

*Comment.*  Thus C^{fix} runs from 1/4 (r = 1) to 1 (h = 1) along the boundary of the (r,h) quadrant; the
FIXED model is not the object of Alon's conjecture, only a device.  The FREE model has C^{free}(r,1) = 1/4
(identity) for every r (h = 1) and C^{free}(1,h) = 1/4.

## 3. The fresh-quadrant barrier π/8 (PROVED)

Write the increments of any copy, in scaled units, as u_t = x'(p_t) − x'(p_{t−1}) and v_t = y'(p_t) − y'(previous
point of the same strip) (u_0 = x'(p_0), v = y' for a strip's first point).  Every copy satisfies

   Σ_{t<k} u_t ≤ k   and   Σ_{i<h} v_{(i,s)} ≤ h for every strip s,   hence  Σ_t (u_t + v_t) ≤ 2k.        (3.1)

**Definition (fresh-quadrant strategies).**  An embedding strategy is *fresh-quadrant* if, at every step t, the
point p_t is chosen inside the quadrant Q_t = {x' > x'(p_{t−1}), y' > level of strip s_t} (possibly truncated to
y' < h) and, conditionally on the past of the construction, the strip process restricted to Q_t is a Poisson
process of intensity C.  Every corner rule of W11 Theorem 4.1/4.4 is fresh-quadrant (Lemma 4.3 there); so is any
rule that explores Q_t along the ℓ₁-sweep {u + v ≤ s} to any depth and then chooses one of the explored points
(the unexplored part stays Poisson by the same lemma), and so are all mean-field rules of §4.

**Proposition 3.1.**  For a fresh-quadrant strategy, E[u_t + v_t | past] ≥ E[min_{p ∈ Ψ ∩ Q} (u + v)] =
2√(π/(8C)) at every step (Ψ a Poisson process of intensity C on the full quadrant; truncation to y' < h only
increases the minimum).  Consequently, for C < π/8, E Σ_t (u_t+v_t) ≥ 2k√(π/(8C)) > 2k, and by (3.1) and the
weak law (the increments have uniformly Gaussian tails when the quadrant is fresh) the strategy fails with
probability → 1 as k → ∞.  In particular no fresh-quadrant strategy — whatever its lookahead inside the current
quadrant, and whatever its choice rule — proves a threshold below π/8; the triangle rule (E U = E V = √(π/(8C)))
is optimal in this class.

*Proof.*  The chosen point lies in Q_t, so u_t + v_t ≥ min_{Q_t}(u+v), and min over the points of a Poisson
process of intensity C on (a subset of) the quadrant is stochastically ≥ the minimum T over the full quadrant,
Pr(T > t) = e^{−Ct²/2}, E T = √(π/(2C)) = 2√(π/(8C)).  The rest is (3.1).  ∎

*Comment.*  This is the tilted-grid analogue of W17 Proposition 4 (renewal rules cap at 0.84 for c_{21}) and of
Hammersley's √(8/π) vs 2 for the LIS: the ratio π/8 : 1/4 = π/2 is the same 0.8 loss.  Beating π/8 requires
choosing p_t using information about the strip process *outside* Q_t — i.e. below the current level or, more
usefully, to the right of where the next visit of the strip will begin (§4.4).

## 4. The mean-field regime: h fixed, r → ∞ (PROVED upper bound, HEURISTIC identification)

In the FIXED model with h fixed and r → ∞, consecutive visits of a strip are separated by r − 1 steps of the
other strips, i.e. by an x'-distance of order r, while a single visit explores an O(1) neighbourhood of its corner.
So a strip *forgets* its previous exploration by the next visit, and any per-strip rule automatically sees a
fresh half-strip at every visit.  This makes a large class of rules rigorously analysable, and gives, for each
fixed h, an explicit constant.

### 4.1 Mean-field rules

Fix h.  A *mean-field rule* R = (c, W) consists of caps 0 < c_1 < c_2 < ⋯ < c_h = h with δ := min_m (c_m − c_{m−1})
> 0 (c_0 := 0) and potentials W_1, …, W_h: [0,h) → ℝ, each nondecreasing and bounded on [0, c_m] (ties broken by
smaller u).  The rule acts on one strip with state (m, v) (round m ∈ {1..h}, level v ∈ [0, c_{m−1}]): given a Poisson
process Ψ of intensity C on the half-strip (0,∞) × (v, c_m), it chooses the point (u, y) ∈ Ψ minimising
u + W_m(y) (a.s. exists and is unique: the sublevel sets of u + W_m are bounded because W_m is bounded on [v,c_m]),
pays u_m := u and moves to (m+1, y).  Its *mean strip cost* is μ_R(C) := E[u_1 + ⋯ + u_h] starting from (1, 0),
each round using an independent fresh Poisson process.  Note v_m := y − v ≤ c_m − c_{m−1}... in fact the level
after round m is ≤ c_m ≤ h always, so the strip's y-budget is never violated; only the x-budget Σ u can fail.

The *windowed* version R^L (L > 0) minimises over the points with u < L only and *fails* if the half-strip window
(0, L) × (v, c_m) contains no point of Ψ; Pr(fail at a round) ≤ e^{−CLδ} since c_m − v ≥ c_m − c_{m−1} ≥ δ.  Its cost
on a completed strip is ≤ hL.

**Lemma 4.1 (window limit).**  μ_{R^L}(C) := E[u_1+⋯+u_h; no failure] satisfies μ_{R^L}(C) → μ_R(C) as L → ∞,
and E[u_m^2] ≤ 2/(Cδ)² for both rules (u_m is stochastically at most Exp(Cδ), the wait for the first point of
(0,∞) × (v, c_m), whose height is ≥ δ).

*Proof.*  Let (u_left, y_left) be the leftmost point of Ψ in (0,∞) × (v, c_m); u_left ~ Exp(C(c_m − v)) is
stochastically ≤ Exp(Cδ).  The minimiser (u*, y*) satisfies u* + W_m(y*) ≤ u_left + W_m(y_left), so
u* ≤ u_left + osc_m, osc_m := sup − inf of W_m on [0, c_m] < ∞; hence E u_m² ≤ E(u_left + osc_m)² ≤ 2(2/(Cδ)² + osc_m²)
=: B_m (the stated bound 2/(Cδ)² is the case osc_m = 0; below we only use finiteness of B_m and, in Proposition 4.5,
the explicit form with W_m(y) = y).  Window limit: the windowed and unwindowed rules coincide on the event that the
unwindowed minimiser has u* < L at every round; since u* ≤ u_left + osc_m, this event has probability
≥ 1 − Σ_m Pr(u_left ≥ L − osc_m) ≥ 1 − h e^{−Cδ(L − max osc)} → 1, and the unwindowed cost is integrable (E u_m ≤
1/(Cδ) + osc_m), so dominated convergence gives μ_{R^L} → μ_R.  ∎

### 4.2 The theorem

**Theorem 4.2 (mean-field upper bound; PROVED).**  Fix h ≥ 1, a mean-field rule R = (c, W) with bounded potentials,
and C > 0 with μ_R(C) < h.  Then Pr(π_{r,h} ⊂_fix Π_{Ck²}) → 1 as r → ∞ (k = rh).  Consequently

   limsup_{r→∞} C^{fix}(r,h) ≤ C_mf(h) := inf{ C : μ_R(C) < h for some mean-field rule R }.

*Proof.*  Fix ε > 0 with μ_R(C) < h − 3ε and let L = L_r := (3 ln r)/(Cδ), so that h e^{−CLδ} = h r^{−3}, and (Lemma
4.1) μ_{R^L}(C) ≤ h − 2ε for r large.  Work in the colour model of Proposition 1.1 in scaled units: strip s is a
Poisson process Ψ_s of intensity C on [0,k] × [0,h), the r processes independent.

*The construction (coupled system).*  Process t = 0, 1, …, k−1 with s_t = t mod r and round m_t = ⌊t/r⌋ + 1.
Maintain the clock a ∈ [0, ∞) (a = 0 initially) and levels v_s (= 0 initially).  At step t, in strip s = s_t, let
R_t := (a, a + L) × (v_s, c_{m_t}) (in strip coordinates) and let O_t := ∪_{t' < t, s_{t'} = s} R_{t'} be the region
of strip s already observed.  Let Ψ^*_t := (Ψ_s ∩ (R_t ∖ O_t)) ∪ (A_t ∩ (R_t ∩ O_t)), where A_t is an independent
Poisson process of intensity C ("artificial fill").  Apply the windowed rule to Ψ^*_t: if Ψ^*_t = ∅, STOP (failure
F1); else choose (u, y) ∈ Ψ^*_t minimising u + W_{m_t}(y), set a := a + u, v_s := y.  If the chosen point belongs to
A_t (failure F2), STOP.  If all k steps complete with a ≤ k (else failure F3), the chosen points are genuine points
of Π_N, one per step, with x' increasing (each u > 0), each in its strip with y' < h, and increasing y' within a
strip: by Proposition 1.1 they form a copy of π, fixed-strip.

*Freshness.*  Let 𝔽_{t} be the σ-field generated by everything used before step t (the other strips' observations,
all A_{t'}, t' < t, and Ψ_s ∩ O_t).  R_t is 𝔽_t-measurable, and Ψ_s ∩ (R_t ∖ O_t) is the restriction of Ψ_s to an
𝔽_t-measurable set disjoint from O_t, hence (independence of a Poisson process over disjoint sets, applied
conditionally on the 𝔽_t-measurable sets) it is, conditionally on 𝔽_t, a Poisson process of intensity C on
R_t ∖ O_t, independent of 𝔽_t; A_t is independent of everything.  So Ψ^*_t is, conditionally on 𝔽_t, a Poisson
process of intensity C on the whole window R_t.  Therefore the coupled system performs, in each strip, exactly
the windowed rule R^L with fresh windows at every round, and the r strips' cost sequences (u_{(1,s)}, …, u_{(h,s)})
are i.i.d. across s (a strip's sequence is a function of its own fresh windows and its own states; the clock a
enters only as the origin of the window).

*Failure F1.*  Pr(F1) ≤ k·e^{−CLδ} = rh·r^{−3} → 0.

*Failure F2.*  F2 at step t requires R_t ∩ O_t ≠ ∅, hence a_t − a_{t'} < L for the previous visit t' = t − r of the
same strip (older visits have smaller a).  Now a_t − a_{t'} = Σ_{t'<τ<t} u_τ is a sum of r − 1 increments of r − 1
*distinct other* strips, independent (across strips) in the coupled system, each stochastically ≥ the wait for the
first point of a window of height ≤ h: Pr(u_τ ≤ x | 𝔽_τ) ≤ 1 − e^{−Chx} ≤ Chx.  Hence E[e^{−θu_τ} | 𝔽_τ] ≤ Ch/θ for
θ > 0 (E e^{−θu} = ∫_0^1 Pr(u < −ln z/θ) dz ≤ (Ch/θ)∫_0^1 (−ln z) dz = Ch/θ), and by the tower property
   Pr(Σ_{r−1} u_τ ≤ L) ≤ e^{θL} (Ch/θ)^{r−1} = (eChL/(r−1))^{r−1}   (θ = (r−1)/L),
which with L = 3 ln r/(Cδ) is ≤ (3eh ln r/(δ(r−1)))^{r−1} ≤ r^{−3} for r ≥ r_0(h,δ).  Union over the k = rh steps:
Pr(F2) ≤ h r^{−2} → 0.

*Failure F3.*  On F1^c, a_k = Σ_s cost_s with cost_s := Σ_m u_{(m,s)} i.i.d. across strips, 0 ≤ cost_s ≤ hL and
E cost_s ≤ μ_{R^L}(C) + hL·Pr(strip fails) ≤ h − 2ε + hL·h r^{−3} ≤ h − ε.  Hoeffding:
   Pr(Σ_s cost_s ≥ rh) ≤ exp(−2 r ε²/(hL)²) = exp(−2rε²C²δ²/(9h² ln² r)) → 0.
Hence Pr(π ⊄_fix Π_N) ≤ Pr(F1) + Pr(F2) + Pr(F3) → 0.  ∎

*Remarks.*  (i) The proof uses nothing about h being fixed except through the constants: for h = h(r) it works
verbatim as long as h ≤ r^{1/2−η}, provided μ_R(C) ≤ h − εh (relative slack) — the F2 bound (r^{−3} per step) and
the Hoeffding exponent 2rε²/(L)² (with cost ≤ hL, ε ↦ εh) survive.  We do not pursue this: at h → ∞ the rules of
§4.3 give π/8 anyway, which W11 Theorem 4.4 already proves for all min(r,h) → ∞.
(ii) The failure event F2 is where the mean-field picture is *proved*: previous explorations are forgotten
because the clock moves by Θ(r) between visits.  In the diagonal regime r = h = √k the same forgetting holds
(r → ∞), but the theorem's conclusion is only about mean-field rules, which (Proposition 3.1) cannot beat π/8.

### 4.3 The constants C_mf(h): Bellman recursion, h = 1, and the limit h → ∞

**Proposition 4.3 (Bellman form; PROVED for the inequality, standard for the equality).**  For C > 0 define
V_0 ≡ 0 and, for m ≥ 1 and v ∈ [0, h),
   V_m(v) := E[ min_{(u,y) ∈ Ψ ∩ (0,∞)×(v,h)} ( u + V_{m−1}(y) ) ]  =  ∫_0^∞ exp( −C ∫_v^h (σ − V_{m−1}(y))_+ dy ) dσ,
Ψ a Poisson process of intensity C.  Then (a) V_m(v) ≥ 1/(C(h−v)) for m ≥ 1 and V_m is finite, nondecreasing and
continuous on [0,h) with V_m(v) → ∞ as v → h; (b) inf_R μ_R(C) over all mean-field rules (all caps, all potentials)
is ≥ V_h(0), and (c) inf_R μ_R(C) = V_h(0) (the infimum is approached by the rules with caps c_m ↑ h and potentials
W_m = V_{h−m}, restricted to the capped half-strips).  Hence C_mf(h) = inf{C : V_h(0) < h} =: the unique root of
V_h(0; C) = h (V_h(0; C) is decreasing in C).

*Proof.*  The formula: Pr(min > σ) = Pr(no point in {u + V_{m−1}(y) < σ}) = exp(−C·area), area = ∫(σ − V)_+ dy.
(a) V_m(v) ≥ E[min u] = 1/(C(h−v)) (the minimiser of u + V_{m−1}(y), V_{m−1} ≥ 0, has u ≥ min u; the leftmost point
of a Poisson process on a half-strip of height h − v is at distance Exp(C(h−v))).  Finiteness by induction (V_{m−1}
bounded on [v, (v+h)/2] gives area(σ) ≥ ((h−v)/2)(σ − sup) for large σ).  Monotonicity and continuity in v are
clear from the formula.  (b) A mean-field rule is a policy in the finite-horizon Markov decision problem with state
(m, v), exogenous fresh half-strips and cost u; caps only restrict the action set (points with y ≤ c_m), so its
mean cost is ≥ the unrestricted optimal value, which is V_h(0) by the dynamic-programming principle (finite
horizon; at each stage the cost-to-go is u + V_{m−1}(y) and the optimal action is its minimiser, whose existence is
part (a)).  (c) The rule with caps c_m = h − (h−m)η and potentials W_m = V_{h−m} on [0,c_m] has cost → V_h(0) as
η → 0 (dominated convergence as in Lemma 4.1: it differs from the optimal unrestricted policy only when some
optimal choice has y > c_m, an event of probability → 0 as η → 0, since y* < h a.s. and the level distributions
have no atom at h).  Monotonicity in C: coupling of Poisson processes.  ∎

**Corollary 4.4 (h = 1; PROVED).**  V_1(0) = 1/(Ch), so C_mf(1) = 1, matching Theorem 2.2: the mean-field bound is
exact for h = 1.

**Proposition 4.5 (the limit h → ∞; PROVED).**  π/8 ≤ C_mf(h) for every h, and C_mf(h) → π/8 as h → ∞.

*Proof.*  Lower bound: a mean-field rule is a fresh-quadrant strategy for one strip, so by Proposition 3.1's
inequality Σ_m (u_m + v_m) ≥ Σ_m T_m with E T_m = 2√(π/(8C)) (v_m := y_m − y_{m−1}), and Σ_m v_m ≤ h; hence
μ_R(C) ≥ h(2√(π/(8C)) − 1) ≥ h for C ≤ π/8, so C_mf(h) ≥ π/8.
Upper bound: fix C > π/8, so ρ := √(π/(8C)) < 1 (ρ = E U = E V of the triangle rule of W11 (4.1)).  Take the rule
with potentials W_m(y) = y and caps c_m = h − (h−m)η, η := (1−ρ)/2 (so δ = η).  Couple the strip's rounds with the
free triangle rule: extend each fresh half-strip by an independent Poisson process above c_m; the free triangle
minimiser (Ũ_m, Ṽ_m) of u + (y − v) over the whole quadrant has the law (U,V) of W11 (4.1), i.i.d. over rounds, and
the capped rule chooses the same point unless Ṽ_m > c_m − v_{m−1}.  Let G be the event that Σ_{i≤m} Ṽ_i ≤ mρ +
h(1−ρ)/4 for all m ≤ h and that Ṽ_m ≤ M_h := h·min(3(1−ρ)/4, 1/4) for all m.  On G, inductively, the capped rule
coincides with the free rule at every round (the level v_{m−1} = Σ_{i<m} Ṽ_i ≤ (m−1)ρ + h(1−ρ)/4, and
c_m − v_{m−1} ≥ h(1−η) + m(η − ρ) − h(1−ρ)/4 ≥ M_h — split according to η < ρ or η ≥ ρ — so Ṽ_m ≤ M_h keeps the point
under the cap), hence cost = Σ Ũ_m on G.  Pr(G^c) ≤ h e^{−c h} + h e^{−CM_h²/2} =: p_h → 0 (Chernoff for the
i.i.d. Ṽ with Gaussian tails, mean ρ; and Pr(Ṽ > M) ≤ Pr(T > M) = e^{−CM²/2}).  By Lemma 4.1 with osc_m ≤ h
(W_m(y) = y on [0,c_m]), E u_m² ≤ 2(2/(Cη)² + h²), so E cost² ≤ h Σ_m E u_m² ≤ 2h²(2/(Cη)² + h²), and by
Cauchy–Schwarz
   μ_R(C) ≤ E Σ Ũ_m + E[cost; G^c] ≤ hρ + (E cost²)^{1/2} p_h^{1/2} = hρ + O(h² e^{−ch/2}) < h
for h large.  So C_mf(h) ≤ C for every C > π/8 and all large h.  ∎

*Comment.*  Together with Theorem 4.2 this recovers W11 Theorem 4.4's π/8 in the iterated limit (r → ∞, then
h → ∞), and shows the mean-field theory is exactly the "fresh-quadrant" theory, whose optimum is the triangle
rule when h → ∞ and a genuinely better, h-dependent rule for finite h.

**Numerical values (NUMERICAL; mf.py, 400–800 cells).**  C_mf(h) = 1 (h = 1, exact), 0.750, 0.655, 0.603,
0.570, 0.547, 0.530, 0.517 (h = 2..8), 0.501 (10), 0.472 (16); C_mf(h) − π/8 ≈ 0.50·h^{−2/3} (log.md §3.1).
The mean-field rule for h = 2 simulated on the real FIXED model has success probability 0.50–0.52 at C = 0.75
for r = 64 and 256 (log.md §3.2): Theorem 4.2's constant is attained at moderate r.

### 4.4 What is conjectured, and the obstruction

**Conjecture 4.6 (HEURISTIC).**  For every fixed h, lim_{r→∞} C^{fix}(r,h) exists and equals C_mf(h).  In words:
in the FIXED model with r → ∞ the optimal (non-causal) embedding gains nothing over mean-field rules.

*Heuristic.*  Between two visits of a strip the clock advances by a sum of r − 1 increments chosen in the other
strips.  A non-causal embedding could in principle tune these increments so that the clock arrives at a
pre-selected good point of the strip; but every increment is itself the choice of some strip, and a clock that is
tuned for strip s at round m fixes the choices of the strips s' < s in that round, which then cannot be tuned for
themselves.  With each strip having Θ(r) candidate points per round in its budget band and only O(1) of them
"planned", the planning cost and benefit are both O(1) per strip per round... this is exactly the trade-off that the
exact DP resolves and that we cannot resolve analytically.  The evidence for the conjecture is Theorem 2.2 (h = 1,
where it is a theorem) and the numerics of log.md §3 (h = 2, 3 with r up to 64: NUMERICAL — see there for the
status; convergence in r is slow, O(r^{−1/2}) already at h = 1).

**What this means for the 1/4 question.**  If Conjecture 4.6 holds then lim_h lim_r C^{fix}(r,h) = π/8 exactly
(Proposition 4.5): the FIXED model's constant is π/8, not 1/4, in the iterated limit, and the corner greedy of W11
is asymptotically optimal there.  The diagonal limit lim_{r=h→∞} C^{fix}(r,r) is a different quantity, sandwiched
(numerically) ≤ 0.335 at k = 64 and still decreasing (log.md §3.2), i.e. already below the iterated limit;
so either the two limits differ (the clock at r = h is far more predictable than at r ≫ h) or the diagonal
curve turns around beyond k = 64.  The 1/4 of Alon's conjecture can only come from the FREE model: the freedom the FREE model has and
the FIXED one lacks is that the copy chooses its own strip boundaries (the y-levels separating its r chains), so
the "budget h per strip" is replaced by "budget k in total, allocated by the copy".  In the colour model this
corresponds to colours that are *not* i.i.d. but chosen by the embedding — a fundamentally different (and much
richer) optimisation, which is why the FREE thresholds track the identity's (W11 log §6.2) while the FIXED ones
do not.

**Remark 4.7 (the FREE model at fixed h, and the two strip directions; PROVED inequality).**  The tilted grid
r×h and its inverse h×r are the same pattern up to the diagonal reflection, and Pr(π ⊂ Π_N) = Pr(π^{−1} ⊂ Π_N).
Hence  C^{free}(r,h) ≤ min( C^{fix}(r,h), C^{fix}(h,r) ):  the copy may use strips in either direction.  For fixed h
and r → ∞ the better direction is C^{fix}(h,r) — h rigid strips, each holding a chain of length r → ∞ — and
numerically (log.md §3) C^{fix}(2,r) → 1/4 as r → ∞.  So the mean-field constants C_mf(h) > π/8 say nothing
against the 1/4 conjecture for the FREE model at fixed h; they quantify the loss of *rigid strips in the short
direction*.  On the diagonal r = h both directions coincide and the question is genuinely open.

## 5. Summary of the constant landscape

| model | direction | constant | status |
|---|---|---|---|
| CELL | any r, h → ∞ | 1 | PROVED (Thm 2.1) |
| FIXED | h = 1, r → ∞ | 1 | PROVED (Thm 2.2) |
| FIXED | h fixed, r → ∞ | ≤ C_mf(h) (Thm 4.2); ≥ 1/h (Prop 2.3); C_mf(1)=1, C_mf(2)=0.750, C_mf(h) ↓ π/8 | PROVED bounds; = C_mf(h) is Conj. 4.6 |
| FIXED | min(r,h) → ∞ | ≤ π/8 (W11 Thm 4.4); ≥ π/8 for fresh-quadrant strategies (Prop 3.1) | PROVED; exact value open (iterated limit = π/8 under Conj. 4.6) |
| FIXED | r = 1 | 1/4 | PROVED (LIS) |
| FREE | any r, h = 1 or r = 1 | 1/4 | PROVED (LIS) |
| FIXED | r = 2, h → ∞ | ≥ 1/8 (LIS in a half-strip); numerically 0.254 at k = 256, extrapolating to ≈ 0.22–0.23 < 1/4 | open |
| FREE | r = 2 ((12)^h), h → ∞ | ≤ the FIXED value; 0.272 at k = 64, below the identity's 0.291 | open |
| FREE | r = h → ∞ | ∈ [0.1925 (W-notes universal bound, semi-rigorous) / 1/e² (first moment, rigorous), π/8]; numerically ≤ 0.335 (FIXED 8×8) | open |
