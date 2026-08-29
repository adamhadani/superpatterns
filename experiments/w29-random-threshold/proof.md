# W29 — the gap-reserve greedy: a threshold below 0.757k² for a typical pattern, and a ½ barrier

Date: 2026-08-29.  Tags: PROVED / HEURISTIC / NUMERICAL.  Numerics: results.md; chronology and dead ends: log.md.
Notation is that of experiments/w19-general-greedy/proof.md ([W19]): Π_N is a Poisson process of intensity
N = Ck² on [0,1]²; π ∈ S_k acts on 0-indexed positions and values; the strip of a value interval I is
S_I = [0,1) × [min I/k, (max I+1)/k); extended processes Π^{(j)} := (Π_N ∩ S_j) ∪ (independent Poisson process of
intensity N off S_j) are independent Poisson processes of intensity N on ℝ² ([W19] §0); "search" and "explored
set" are as in [W19] Lemma 1.1–1.2 (sequential fresh searches), which is used verbatim.

Summary.  [W19]'s reserve greedy needs every value strip to be a monotone run of π^{-1}, which for a random π
forces strips of 2–3 values and gives the universal constant 0.757.  Here the strips may carry an *arbitrary*
sub-pattern: the window of the next point of a strip is the gap between the already-placed points of the strip
whose values are the nearest below and above, minus a reserve β per still-unplaced value inside the gap, and
the point taken is the leftmost one in the window.  The reduction (Theorem 2.1) holds for every π; for a
uniformly random π the strip sub-patterns are i.i.d. uniform, the per-strip costs are i.i.d., and the threshold
constant is Ω_h = E[Σ_{i≤h} 1/W_i]/h, a C-independent quantity computed by simulation: Ω_64 = 0.527, Ω_1024 = 0.515
(Theorem 3.2 + results.md).  Every rule of this type is capped at ½ (Theorem 4.1), so this route cannot reach 1/4.

## 1. The gap-reserve greedy on one strip (PROVED)

Fix a value interval I of h consecutive values, its strip S = S_I, and the *sub-pattern* σ: the h values of I
listed in the order of their positions in π (so σ is a sequence of h distinct values; only its relative order
matters).  Fix β ∈ (0,1] and a *window rule* ω (any measurable rule, see below).  Scaled coordinates in the
strip: y' = k·y − (bottom of S)·k ∈ [0,h), x' = kx.

State when the strip is visited for the t-th time (t = 1..h; the value to be placed is v = σ_t): a global
x-level a (shared by all strips: the x-coordinate of the last point chosen anywhere); the placed values
P ⊂ I with their y'-coordinates.  Let L (resp. R) be the largest placed value < v (resp. smallest placed value
> v), with y'_L := 0 if there is none below and y'_R := h if none above; m_b := #(unplaced values strictly
between L and v) = v − L − 1 (resp. v − min I if L is absent), m_a := R − v − 1 similarly.  The *reserve
interval* is
     J_t := [ y'_L + β m_b ,  y'_R − β m_a ].
The *window* W_t := ω(past) is a closed sub-interval of J_t of length |W_t| ≥ β (the rule may use the whole
past; concrete rules: results.md — "no band": W_t = J_t; "band": J_t ∩ [y_0 − w/2, y_0 + w/2] widened
symmetrically until its length is β, with y_0 the row centre v + ½ or the proportional position of v in the gap).
The point q_t is the leftmost point of Π^{(I)} in A_t := {x > a} × (W_t in unscaled coordinates); put
X_t := k(x(q_t) − a), Y_t := y'(q_t); update a := x(q_t), P := P ∪ {v}.

**Lemma 1.1 (invariant; windows have length ≥ β; points stay in the strip).**  Call a configuration
*admissible* if for every gap between consecutive placed values (or a strip boundary and a placed value) the
scaled height of the gap is ≥ β·(number of unplaced values in it).  The initial configuration (no points, one gap
of height h containing h values) is admissible since β ≤ 1.  If the configuration is admissible before step t,
then |J_t| ≥ β, so a window of length ≥ β exists, and after placing v anywhere in J_t the configuration is again
admissible.  All chosen points lie in S.

*Proof.*  The gap (L,R) containing v has height y'_R − y'_L ≥ β(m_b + m_a + 1), so |J_t| = y'_R − y'_L −
β(m_b + m_a) ≥ β.  If v is placed at y' ∈ J_t, the two new gaps have heights y' − y'_L ≥ β m_b and y'_R − y' ≥
β m_a, and they contain m_b resp. m_a unplaced values; the other gaps are unchanged.  Since J_t ⊆ [y'_L, y'_R] ⊆
[0,h], the point is in S.  ∎

**Lemma 1.2 (increments).**  Condition on the whole past of the construction (all strips) before step t of
strip I.  Then Π^{(I)} ∩ A_t is a Poisson process of intensity N on A_t; consequently X_t ~ Exp(C·|W_t|) and
Y_t is uniform on W_t, independent of each other and of the past given W_t.  In particular the law of the
sequence (W_t, Y_t)_{t ≤ h} does not depend on C, and E[X_t | past] = 1/(C|W_t|).

*Proof.*  The searches in Π^{(I)} are "leftmost in A_t", i.e. minimisers of ψ_t(x,y) = x − a on A_t, and the
explored set of step t is Δ_t = {a < x ≤ x(q_t)} × W_t.  A later search in the same process has x-level a' ≥
x(q_t) (a only increases), so A_{t'} ∩ Δ_t = ∅: the disjointness hypothesis of [W19] Lemma 1.2 holds, and that
lemma gives the conditional Poisson property.  The leftmost point of a Poisson process of intensity N on
{x > a} × W, where W has unscaled height |W_t|/k, has x − a ~ Exp(N|W_t|/k) = Exp(Ck|W_t|), i.e. in scaled
units X_t = k(x − a) ~ Exp(C|W_t|), and given x its y is uniform on W (the Poisson process restricted to a
number of points in {a < x ≤ a + s} × W is Poisson(Ns|W_t|/k) and
conditionally on the count the points are i.i.d. uniform in the rectangle, so the leftmost point's y is uniform
on W and independent of its x).  ∎

## 2. The reduction for every pattern (PROVED)

Partition the values into consecutive intervals I_1 < ⋯ < I_m with |I_j| = h_j; run the greedy of §1 on all
strips simultaneously, processing the positions p = 0, 1, …, k−1 in order and performing at position p the next
step of the strip containing π(p) (the x-level a is global).

**Theorem 2.1.**  For every π ∈ S_k, every partition, every β ∈ (0,1] and every window rule,
     Pr( π ⊄ Π_{Ck²} ) ≤ Pr( T_1 + ⋯ + T_m ≥ k ),
where T_j := Σ_{p: π(p) ∈ I_j} X_p is the total scaled x-cost of strip j, the T_j are independent, and the law
of T_j depends only on (h_j, the sub-pattern σ_j of π on I_j, C, β, ω).  Moreover E T_j = (1/C)·E Σ_{t ≤ h_j} 1/|W_t^{(j)}|,
where the window sequence has a C-independent law (Lemma 1.2), and E e^{θ T_j} ≤ (1 − θ/(Cβ))^{−h_j} < ∞ for θ < Cβ.

*Proof.*  *Copy.*  On E := {Σ_p X_p < k} every chosen point has x-coordinate Σ_{p' ≤ p} X_{p'}/k < 1 and (Lemma
1.1) lies in its strip, hence is a point of Π_N.  The x-order of the chosen points is the position order.  For
the y-order: points of different strips are ordered as their strips, i.e. as their values; inside a strip, the
point of value v was placed in J_t ⊆ (y'_L, y'_R), strictly between the points of the nearest placed values
below and above, so by induction the placed points of a strip are y-ordered as their values at every time.
Hence the y-order of the k points is the order of π(p): they form a copy of π, and Pr(π ⊄ Π_N) ≤ Pr(E^c).
*Independence.*  By Lemma 1.2 the conditional law of (X_p, Y_p) given the past is f_{W_p}(x,y) dx dy with
f_W = C|W| e^{−C|W|x}·|W|^{−1}1_{y∈W}, and W_p is a function of the earlier (Y_{p'}) of the same strip and of
σ_j only.  The joint density of ((X_p,Y_p))_p is the product over p of these factors; grouping by strip shows
that the strip chains are independent, with laws depending only on the listed data.
*Moments.*  E[X_p | past] = 1/(C|W_p|) and |W_p| ≥ β, so X_p ≤_st Exp(Cβ) given the past, whence the MGF bound;
E T_j follows by conditioning on the window sequence.  ∎

## 3. Uniformly random patterns (PROVED reduction, NUMERICAL constant)

Let k = mh and take the m strips of h consecutive values.

**Lemma 3.1.**  If π is uniform in S_k, the sub-patterns σ_1, …, σ_m (the relative orders of the position
sequences of the strips) are independent and uniform in S_h.

*Proof.*  σ_j is the standardisation of π^{-1} on the index block I_j.  π^{-1} is uniform in S_k; conditionally
on the m sets π^{-1}(I_j) the internal orders are independent uniform (the map from S_k to (ordered set
partition, m internal orders) is a bijection with uniform product image).  ∎

**Definition.**  For a window rule ω and β, let Ω_h(β, ω) := E[ Σ_{t≤h} 1/|W_t| ] / h, the expectation over a
uniform σ ∈ S_h and the uniform draws Y_t (C-independent by Lemma 1.2).  Let T = T(h; C, β, ω) be the strip
cost for uniform σ: E T = h·Ω_h/C.

**Theorem 3.2 (annealed threshold for a random pattern).**  Let π be uniform in S_k and Π_{Ck²} independent of π.
For every h, β ∈ (0,1] and window rule ω with C > Ω_h(β, ω) there is η = η(h, C, β, ω) > 0 such that
     Pr( π ⊄ Π_{Ck²} ) ≤ e^{−η k}        (probability over π and Π_N; k a multiple of h),
namely η = (1/h)·sup_{0<θ<Cβ} [ θh − ln E e^{θT} ] > 0.  Consequently:
(a) (quenched) for all but a fraction e^{−ηk/2} of the patterns π ∈ S_k, Pr_Π(π ⊄ Π_{Ck²}) ≤ e^{−ηk/2};
(b) (uniform permutations) for every ε > 0, a uniformly random σ_n ∈ S_n with n ≥ (1+ε) C k² contains a
uniformly random π ∈ S_k with probability 1 − e^{−Ω(k)} (over both).

*Proof.*  By Theorem 2.1 and Lemma 3.1, conditionally on π the T_j are independent with laws determined by σ_j,
and the σ_j are i.i.d. uniform; hence unconditionally T_1, …, T_m are i.i.d. with the law of T.  Chernoff:
Pr(Σ T_j ≥ k) ≤ inf_θ e^{−θk} (E e^{θT})^m = exp(−m·sup_θ[θh − ln E e^{θT}]); the MGF is finite for θ < Cβ
(Theorem 2.1) and θh − ln E e^{θT} = θ(h − E T) − O(θ²) > 0 for small θ > 0 because E T = hΩ_h/C < h.
(a) Markov's inequality applied to f(π) := Pr_Π(π ⊄ Π_N), E_π f ≤ e^{−ηk}.  (b) Couple n i.i.d. uniform points
Q_n with Π_N ⊆ Q_n on {|Π_N| ≤ n}, N := Ck² ≤ n/(1+ε): Pr(|Π_N| > n) ≤ e^{−N h(ε)}, h(ε) = (1+ε)ln(1+ε) − ε > 0
([W19] Cor. 2.2); a copy in Π_N is a copy in Q_n, and the pattern of Q_n is uniform in S_n.  ∎

**Numerical constant (NUMERICAL, strip.c / results.md).**  With the proportional band rule (w = 3, β = 0.7 or
0.8): Ω_16 = 0.563, Ω_32 = 0.537, Ω_64 = 0.5266 (4·10^4 samples, sem 10^{-4}), Ω_256 = 0.517, Ω_1024 = 0.515;
Ω_h decreases in h towards ≈ 0.51 and stays above the barrier ½ + 1/(2h) of §4.  Hence, for a uniformly
random π ∈ S_k,  threshold ≤ 0.527·k² (h = 64) and ≤ 0.516·k² (h = 1024), annealed and quenched, with
failure e^{−ηk}, η(C = 0.6, h = 64) = 0.0066, η(0.7) = 0.032 — against 0.757k² for arbitrary π ([W19] Thm 4B.3)
and 1/4 for the identity.  Ω_h is a Monte-Carlo estimate of a C-independent expectation of a quantity bounded
by h/β (1/|W_t| ≤ 1/β); it is not certified by quadrature (only the exact value Ω_2 = (1 + ln 2)/2 for the
no-band rule with β = 1 was checked by hand, results.md).  End-to-end validation of the whole procedure on real
Poisson points and real random π (validate2d.py): success 20/20 at C = 0.6, 13/20 at 0.55, 2/20 at 0.5
(k = 400, h = 40, Ω_40 = 0.537).

**Remark 3.3 (also valid for every π with "random-like" strips).**  Theorem 2.1 is pattern-wise; only Lemma
3.1 uses randomness.  For a fixed π the same bound holds with Ω_h replaced by max_j E[Σ_t 1/|W_t^{(j)}|]/h,
so any π whose strip sub-patterns all have cost ≤ 0.53h (e.g. every strip a tilted grid, or a random-like
permutation) has threshold ≤ 0.53k² by the same proof.  For the identity all strips are increasing runs and the
present rule is *worse* than the corner greedy (windows of the identity's strip are [y'_L + β m_b, h]:
Ω_h(identity) → 1 as β → 1 and E 1/|W| diverges as β → 0), so this rule does not compete with [W11] on
monotone strips: the two rules are complementary.

## 4. The ½ barrier for gap-window rules (PROVED)

**Definition.**  A *gap-window rule* is any strategy that, at every step t of a strip, chooses a point
q_t ∈ Π^{(I)} ∩ ({x > a} × W_t) with W_t ⊆ (y'_L, y'_R) (the gap between the nearest placed values below and
above; not necessarily respecting a reserve), W_t and the choice being measurable functions of the past and of
the process inside {x > a} × W_t, where conditionally on the past Π^{(I)} is Poisson of intensity N on
{x > a} × W_t.  (All rules of §1 are gap-window rules, for every β, ω, and so is "leftmost in the gap".)

**Theorem 4.1.**  For every gap-window rule, every h and uniform σ ∈ S_h,  E T ≥ (h+1)/(2C).  Hence no
gap-window rule has E T < h for C ≤ ½ + 1/(2h): Theorem 3.2's exponent is void for C ≤ ½, and Ω_h(β,ω) ≥
(h+1)/(2h) > ½ for every β, ω.  Moreover, if the rule keeps |W_t| ≥ β > 0, then for C < ½ the rule fails
with probability → 1 as m = k/h → ∞ (weak law for the i.i.d. T_j, whose variance is finite).

*Proof.*  Let r_t be the rank of σ_t among σ_1, …, σ_t.  For uniform σ the r_t are independent, r_t uniform on
{1, …, t} (the standard bijection S_h ↔ Π_t [t] via relative ranks).  Before step t the strip has t − 1 placed
points, which cut [0,h] into t gaps of heights G_{t,1}, …, G_{t,t} (top to bottom or bottom to top) with
Σ_j G_{t,j} = h; the gap containing σ_t is the r_t-th one.  The heights (G_{t,j})_j are a function of the past
(the positions of the first t − 1 points), and r_t is independent of the past (the past depends on σ only
through r_1, …, r_{t−1}, plus independent process randomness).  Given the past and r_t, the leftmost point of
Π^{(I)} in {x > a} × W_t has scaled x-increment Exp(C|W_t|), and X_t is at least that, so
E[X_t | past, r_t] ≥ 1/(C|W_t|) ≥ 1/(C G_{t,r_t}).  Averaging over r_t:
     E[X_t | past] ≥ (1/(Ct)) Σ_{j≤t} 1/G_{t,j} ≥ (1/(Ct))·t²/Σ_j G_{t,j} = t/(Ch)     (harmonic ≤ arithmetic mean).
Summing over t = 1..h: E T ≥ (1/(Ch)) Σ_{t≤h} t = (h+1)/(2C).  The remaining statements follow from E T < h ⇔
C > Ω_h and the weak law (T ≤_st Σ_{t≤h} Exp(Cβ) has finite variance).  ∎

*Comments.*  (i) The bound is attained only if all t gaps are equal at every step, which no rule can arrange
(a point placed to split its gap in the ratio dictated by the unplaced values on either side would need the
gap sizes to be h/t exactly); the optimised rules of results.md sit 0.015–0.03 above the barrier for h ≥ 64.  (ii) The barrier
is the analogue of the fresh-quadrant barrier π/8 of experiments/w20-hammersley-grid/proof.md Prop 3.1: there
the loss is that a corner search pays u + v ≥ min over a quadrant; here the loss is that a random pattern
visits a *uniformly random* gap, whose typical height is h/t at time t, so the t-th point of a strip costs
≥ t/h whatever the rule does.  (iii) The identity is not subject to this barrier (its gap is always the top
one, of height ≈ h − t), which is why corner rules reach π/8 for monotone strips; for a random pattern the
route to a constant below ½ — let alone below ¼ — needs a rule that looks at the strip process *outside*
the current gap (e.g. ahead in x, to choose which of several candidate points to commit to), or a genuinely
two-dimensional (non-greedy) argument.  Recorded as open.

## 5. Summary

| statement | class | threshold N/k² | failure | speed |
|---|---|---|---|---|
| Thm 2.1 | every π, any value partition | pattern-dependent (max strip cost) | Chernoff | k |
| Thm 3.2 | uniformly random π (annealed; quenched for all but e^{−ηk/2} of S_k) | Ω_64 = 0.527, Ω_1024 = 0.515 (NUMERICAL; reduction PROVED) | e^{−ηk} | k |
| Thm 4.1 | all gap-window rules | ≥ ½ + 1/(2h) (PROVED barrier) | — | — |

Novelty relative to the ledger: first rigorous per-pattern threshold below 0.757k² for a *typical* pattern
(and Remark 3.3 for any pattern with random-like strips); the identity's 1/4 is not reached, and Theorem 4.1
shows that no greedy of this type can reach it, matching the conjectured ordering (random ≈ 0.22 < identity
1/4 numerically, W21) only in the sense that the identity is *provably* not the easiest pattern for this
method — the direction opposite to the one the numerics suggest for the true thresholds.

## Coordinator's verification note (main session, 2026-08-29 19:30)
Lemmas 1.1–1.2, Theorems 2.1, 3.2 and Lemma 3.1 re-derived line by line: correct. Ω_h independently
recomputed with a separate Python implementation of the mode-1 rule (scratchpad/w29check.py): Ω_2 = 0.7988,
Ω_16 = 0.5628, Ω_64 = 0.5265 (agent: 0.798, 0.563, 0.5266). GAP in Theorem 4.1: the proof uses that r_t is
independent of the past, i.e. that the rule sees σ only through the relative ranks r_1..r_{t−1}; but the §1 rules
use the actual values (m_b, m_a, the proportional target), which reveal future ranks. Theorem 4.1 is therefore
proved only for *value-blind* (rank-measurable) gap-window rules; for the value-aware rules actually used the
barrier is respected numerically (and exactly at h = 2: the value-aware optimum over window lengths is ≈ 1.57 ≥ 1.5)
but not proved. Folded into the paper with this qualification.
