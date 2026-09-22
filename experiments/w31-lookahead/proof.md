# W31 — value-aware x-lookahead: a threshold below ½·k² for a uniformly random pattern

Date 2026-08-29.  Tags PROVED / NUMERICAL (certified) / NUMERICAL (Monte Carlo) / HEURISTIC.  Numerics: results.md;
chronology and dead ends: log.md.  Notation as in experiments/w29-random-threshold/proof.md ([W29]) and
experiments/w19-general-greedy/proof.md ([W19]): Π_N is a Poisson process of intensity N = Ck² on [0,1]²;
π ∈ S_k acts on 0-indexed positions and values; k = mh; strips I_j = [jh, (j+1)h), S_j = [0,1) × [jh/k, (j+1)h/k);
extended processes Π^{(j)} ([W19] §0) are independent Poisson processes of intensity N on ℝ²; [W19] Lemma 1.2
(sequential fresh searches) is used verbatim.  Scaled strip coordinates x' = kx, y' = ky − jh: in these
coordinates Π^{(j)} is a Poisson process of intensity C.

**Reviewed result (2026-09-10).** For uniform independent π∈S_k and a
host of length ceil(Ck²), containment holds with probability 1−o(1) for
every C>0.4649. The finite-strip reduction below, with the minor corrections
recorded here, combines with the directed MPFR supersolution certificate in
[certification.md](certification.md). The certificate uses h=512 and the
exact margin ε=1/64; it verifies V̄_512/512²<0.4649. The older `dp_cert.py`
roundoff multiplier was not an interval proof. The Bellman optimality claim
in §4 is restricted to nonanticipating future target ranks. Its limiting
constant near 0.4623 is numerical, not a certified universal barrier.
Altschuler–Dubroff–Tikhomirov (arXiv:2608.19050) already obtain a typical
target constant below 1/2; the quantitative comparison is recorded in the
current result ledger.

## 1. The rule R(h, ε, V̄) (definition)

Fix h ≥ 2, a margin ε ∈ (0, ½) and numbers V̄_0 = 0 ≤ V̄_1 ≤ ⋯ ≤ V̄_{h−1} (the *potentials*; in §3 they are
certified upper bounds on the rule's own cost-to-go, but the reduction of §2 holds for any nonnegative numbers).
State: a global clock a ≥ 0 (scaled x-coordinate of the last chosen point, initially 0); for every strip j the
placed values with their y'-coordinates and an *explored edge* e_j ≥ 0 (initially 0).

Step at position p with value v = π(p) ∈ I_j.  As in [W29] §1: L (resp. R) is the largest placed value of the
strip below v (resp. smallest above), y_L := y'(L) or 0, y_R := y'(R) or h, m_b := number of unplaced values
strictly between L and v (all of I_j below v if L is absent), m_a likewise above; G := y_R − y_L.  Put
   ε_b := ε·1[m_b > 0],  ε_a := ε·1[m_a > 0],  W := [y_L + ε_b G, y_R − ε_a G]  (the window),
   Φ(y) := V̄_{m_b}/(y − y_L) + V̄_{m_a}/(y_R − y)  on W  (a term with V̄_0 is omitted; Φ ≥ 0, Φ < ∞ on W),
   a_s := max(a, e_j)  (the safe clock),   A := {x' > a_s} × W,   ψ(x', y') := (x' − a_s) + Φ(y')/C.
The chosen point q is the minimiser of ψ over Π^{(j)} ∩ A (a.s. unique; exists since ψ ≥ x' − a_s and every
horizontal strip of positive height contains points of the process arbitrarily far to the right).  Put
   u := x'(q) − a_s,  X_p := x'(q) − a = (a_s − a) + u,  Φ_min := min_W Φ,
   a := x'(q),  e_j := a_s + ψ(q) − Φ_min/C,  and record y'(v) := y'(q).
A *collision* is a step with a_s > a.  In the code (validate2d.py) the rule is implemented exactly as above.

**Lemma 1.1 (state invariants; PROVED).**  (a) The chosen point lies strictly inside (y_L, y_R) a.s., hence the
placed points of a strip are y-ordered as their values at all times, and lie in the strip.  (b) Every gap
that still contains an unplaced value has height ≥ β_h := ε^{h−1} h; consequently |W| ≥ (1 − 2ε)β_h and
Φ_min ≤ Φ ≤ Φ_max := 2V̄_{h−1}/(εβ_h) on W whenever m_b + m_a ≥ 1 (Φ ≡ 0 otherwise).  (c) The explored set
Δ := {ψ ≤ ψ(q)} ∩ A of a step satisfies Δ ⊆ {x' ≤ e_j^{new}}, and e_j^{new} − x'(q) = (Φ(y'(q)) − Φ_min)/C ≤ D_h :=
Φ_max/C.  (d) e_j is nondecreasing in time and all explored sets of strip j lie in {x' ≤ e_j}.

*Proof.*  (a) W ⊆ [y_L, y_R]; the endpoints have probability 0 (the y'-coordinate of q has a density, Lemma
2.2 below).  Induction as in [W29] Thm 2.1.  (b) Induction over the steps of a strip: initially one gap of
height h.  When v is placed at y ∈ W, the lower sub-gap has height y − y_L ≥ ε_b G, which is ≥ εG if it
contains a value (m_b > 0); the upper one likewise.  A gap containing a value at any time is obtained from
the initial gap by at most h − 1 such splits, each keeping at least a fraction ε: height ≥ ε^{h−1}h.  On W,
y − y_L ≥ εG ≥ εβ_h when m_b > 0, so V̄_{m_b}/(y − y_L) ≤ V̄_{h−1}/(εβ_h); same above.  (c) On A, ψ ≤ ψ(q) forces
x' − a_s ≤ ψ(q) − Φ(y')/C ≤ ψ(q) − Φ_min/C, i.e. x' ≤ e_j^{new}; and e_j^{new} − x'(q) = ψ(q) − u − Φ_min/C =
(Φ(y'(q)) − Φ_min)/C ≤ Φ_max/C.  (d) e_j^{new} ≥ a_s ≥ e_j^{old}; (c).  ∎

## 2. The reduction for a random pattern (PROVED)

**Lemma 2.1 (freshness).**  Condition on the whole past before a step of strip j.  Then Π^{(j)} ∩ A is a
Poisson process of intensity C (scaled coordinates) on A, independent of the past.

*Proof.*  A = {x' > a_s} × W with a_s ≥ e_j, and by Lemma 1.1(d) all previously explored sets of Π^{(j)} lie in
{x' ≤ e_j}; so A is disjoint from them and [W19] Lemma 1.2 applies (the searches are minimisations of ψ over A,
ψ has sublevel sets of finite measure inside A because Φ ≥ 0).  ∎

**Lemma 2.2 (one-step law and scaling).**  Conditionally on the past, (u, y'(q)) has the law of the minimiser of
x + Φ(y)/C over a Poisson process of intensity C on (0,∞) × W; equivalently u = u''/C where (u'', y) is the
minimiser of x'' + Φ(y) over a Poisson process of intensity 1 on (0,∞) × W (substitute x'' = Cx).  This law
depends on the past only through (W, Φ), i.e. through the strip's own state (y_L, y_R, m_b, m_a) and the
potentials.  Moreover u ≤ ψ(q) ≤ u_left + Φ_max/C where u_left ~ Exp(C|W|) is the x-distance of the leftmost
point of the region; hence u ≤_st Exp(C(1−2ε)β_h) + D_h.

*Proof.*  Lemma 2.1 and the mapping theorem for the linear map x ↦ Cx.  The bound: the minimiser's score is at
most the score of the leftmost point, whose x-part is Exp(C|W|) and whose Φ-part is ≤ Φ_max/C; Lemma 1.1(b).  ∎

**Definition (strip cost).**  T_j := Σ_{p : π(p) ∈ I_j} u_p (the *fresh* part of the cost of strip j) and
E_coll := Σ_p (a_s − a)_p (the collision offsets), so that the final clock is a_k = Σ_j T_j + E_coll.

**Lemma 2.3 (independence and the mean of T_j).**  Conditionally on π, the strip costs T_1, …, T_m are
independent, T_j has a law depending only on (σ_j, C, h, ε, V̄) where σ_j is the sub-pattern of π on I_j, and
   E[T_j | π] = 𝒱_h(σ_j)/(hC),
where 𝒱_n(σ) is the expected cost (at intensity 1) of the rule on n values with sub-pattern σ in a gap of height 1.
For uniform π the σ_j are i.i.d. uniform in S_h ([W29] Lemma 3.1), so T_1, …, T_m are i.i.d. unconditionally,
with mean E T = 𝒱_h/(hC), 𝒱_h := E_σ 𝒱_h(σ), and E e^{θT} < ∞ for θ < C(1−2ε)β_h.

*Proof.*  By Lemma 2.2 the conditional density of the step's (u, y') given the past is a function of the
strip's own state only, and the strip's state evolves only through its own (y')'s and σ_j (the offsets a_s − a
do not enter u or y').  The joint density of all (u_p, y'_p) is therefore the product over p of factors
depending on strip j's own variables; grouping by strip gives independence and the dependence on σ_j only.
Mean: by the scaling of Lemma 2.2, a gap of height G with n values to place and sub-pattern σ costs, in
expectation, 𝒱_n(σ)/(GC): scale y by 1/G (the windows and the potentials Φ are scale-covariant because the
margins are relative and Φ is homogeneous of degree −1 in the heights), x'' by G (Poisson(1) is preserved,
costs divide by G), then x'' = Cx.  The MGF: Lemma 2.2 and Σ of h such terms.  ∎

**Lemma 2.4 (collisions are rare; annealed over π).**  Let J := max(⌈e²C h D_h⌉, ⌈3 ln k⌉).  Then
   E[E_coll] ≤ D_h ( J h + k^{−2} )   (expectation over π and the process).

*Proof.*  A collision at a step t of strip j needs a_t < e_j ≤ x'(q_{t'}) + D_h = a_{t'+1} + D_h where t' is the
previous step of strip j (Lemma 1.1(c)), i.e. Σ_{t' < τ < t} X_τ < D_h.  Given π, the number n_t := t − t' − 1 of
intermediate steps is deterministic.  Each X_τ ≥ u_τ ≥ u_left,τ, and conditionally on the past u_left,τ ~
Exp(C|W_τ|) ≥_st Exp(Ch) (|W_τ| ≤ h); so, by the tower property with E[e^{−θu} | past] ≤ Ch/θ (as in W20 Thm 4.2,
proof of F2), Pr(Σ X_τ < D_h | π) ≤ e^{θD_h}(Ch/θ)^{n_t} = (eChD_h/n_t)^{n_t} ≤ e^{−n_t} ≤ k^{−3} for n_t ≥ J.  Hence
E[#collisions | π] ≤ #{t : n_t < J} + k·k^{−3}, and each collision contributes ≤ D_h to E_coll.  For uniform π
and each position p and each 1 ≤ n ≤ J, Pr(π(p − n) ∈ I_{strip of π(p)}) = (h−1)/(k−1) ≤ h/k, so
E #{t : n_t < J} ≤ k · J · h/k = Jh.  ∎

**Theorem 2.1 (random pattern, lookahead rule).**  Let π be uniform in S_k, Π_{Ck²} independent of π, k = mh.
For every h ≥ 2, ε ∈ (0, ½), potentials V̄ and every C with
   C > Ω_h(ε, V̄) := 𝒱_h/h²
there are η > 0 and K such that for all k ≥ K
   Pr( π ⊄ Π_{Ck²} ) ≤ e^{−ηk} + (2 D_h (Jh + 1) ) / (δ k),   δ := 1 − 𝒱_h/(h²C) > 0,
in particular Pr(π ⊆ Π_{Ck²}) → 1 (probability over π and Π).  Consequently (a) all but a fraction o(1) of the
patterns π ∈ S_k satisfy Pr_Π(π ⊄ Π_{Ck²}) = o(1) (quenched, Markov); (b) a uniformly random σ_n ∈ S_n with
n ≥ (1+ε')Ck² contains a uniformly random π ∈ S_k with probability 1 − o(1) (coupling of [W29] Thm 3.2(b)).

*Proof.*  *Copy.*  On E := {a_k < k} every chosen point has x-coordinate a/k < 1 and lies in its strip (Lemma
1.1(a)), hence is a point of Π_N; x-order = position order (a increases strictly); y-order = value order
(different strips are ordered as their value intervals; inside a strip Lemma 1.1(a)).  So E ⊆ {π ⊆ Π_N}.
*Cost.*  a_k = Σ_j T_j + E_coll.  Pr(a_k ≥ k) ≤ Pr(Σ_j T_j ≥ (1 − δ/2)k) + Pr(E_coll ≥ δk/2).  The T_j are i.i.d.
with mean 𝒱_h/(hC) = (1−δ)h and finite MGF (Lemma 2.3), so Chernoff gives Pr(Σ_j T_j ≥ (1−δ/2)mh) ≤ e^{−ηk}
with η = (1/h) sup_θ [θ(1−δ/2)h − ln E e^{θT}] > 0.  Markov and Lemma 2.4 give Pr(E_coll ≥ δk/2) ≤
2D_h(Jh + k^{−2})/(δk).  (a), (b) exactly as in [W29] Thm 3.2.  ∎

**Padding to all k.** Fix h and set k′=h ceil(k/h). Sample a uniform
π′∈S_(k′); the standardization of its first k positions is uniform in S_k.
Containment of π′ implies containment of this prefix. For C>C₀>Ω_h,
C₀(k′)²<Ck² for all large k, so the constant margin absorbs padding and
Poisson-to-fixed-size coupling. Thus the headline is not restricted to h|k.

*Remarks.*  (i) The failure probability is only O(ln k/k) because of the crude Markov bound on the collision
cost; the Chernoff part has speed k.  (ii) D_h = 2V̄_{h−1}/(ε^h h C) is astronomically large for the h used
in §3 (ε = 0.05, h = 64: ε^{−63}), so the theorem is an asymptotic statement in k for fixed h; in the
end-to-end simulation (results.md §3) collisions cost 1–3 % of k already at m = 16–64 because the explored
extent beyond the chosen point, (Φ(y'(q)) − Φ_min)/C, is typically O(1), not D_h.  (iii) Nothing in §1–2 uses
the specific values V̄: any nonnegative potentials give a valid rule; §3 chooses them so that Ω_h is computable
and certified.

## 3. The constant: self-similar Bellman evaluation and certified upper bounds

**Lemma 3.1 (self-similarity of the cost-to-go).**  For n ≤ h let 𝒱_n := E_σ 𝒱_n(σ) be the rule's expected cost
(intensity 1) for n values with uniform sub-pattern in a unit-height gap, with the *same* potentials V̄ (the rule
in a sub-gap of height G with n values is the unit rule scaled, Lemma 2.3).  Then 𝒱_0 = 0 and, for n ≥ 1,
   𝒱_n = (1/n) Σ_{m=0}^{n−1} E[ u'' + 𝒱_m/y + 𝒱_{n−1−m}/(1 − y) ],
where (u'', y) is the minimiser of x + V̄_m/y + V̄_{n−1−m}/(1−y) over a Poisson(1) process on (0,∞) × W_{m,n−1−m},
W_{m,m'} := [ε·1[m>0], 1 − ε·1[m'>0]].

*Proof.*  The first value placed is uniform among the n, so m := m_b is uniform on {0..n−1} and m_a = n−1−m; the
sub-patterns of the two sub-gaps are independent uniform and their future costs are 𝒱_m/y and 𝒱_{n−1−m}/(1−y) by
scaling (Lemma 2.3), whatever the interleaving of their arrivals (the windows are fresh at every step and
costs add).  ∎

**Lemma 3.2 (certified upper bounds; PROVED given the numerics of dp_cert.py).**  Define, for A, B ≥ 0 and the
window W = [lo, hi] (lo = ε1[A>0], hi = 1 − ε1[B>0]),
   W_ε(A, B) := E min_{(x,y) ∈ Ψ ∩ (0,∞)×W} [x + A/y + B/(1−y)]  =  s_min + ∫_{s_min}^∞ e^{−area(s)} ds,
   s_min := min_W (A/y + B/(1−y)),  area(s) := ∫_W (s − A/y − B/(1−y))_+ dy
   = s(y₂ − y₁) − A ln(y₂/y₁) + B ln((1−y₂)/(1−y₁)),  y₁ < y₂ the roots of s y² − (s + A − B) y + A = 0 clipped to W.
W_ε is nondecreasing in A and in B.  Let V̄_0 = 0 and V̄_n ≥ (1/n) Σ_{m<n} W̄_ε(V̄_m, V̄_{n−1−m}) where W̄_ε ≥ W_ε is
any upper bound.  Then the rule R(h, ε, V̄) satisfies 𝒱_n ≤ V̄_n for all n ≤ h, hence Ω_h(ε, V̄) ≤ V̄_h/h².

*Proof.*  Formula: Pr(min > s) = Pr(no point in the sublevel set) = e^{−area(s)}; the sublevel set {y ∈ W:
A/y + B/(1−y) < s} is an interval because the function is convex.  Monotonicity: the minimum of a larger
function is larger.  Induction on n: 𝒱_n = (1/n)Σ_m E[u'' + 𝒱_m/y + 𝒱_{n−1−m}/(1−y)] ≤ (1/n)Σ_m E[u'' + V̄_m/y +
V̄_{n−1−m}/(1−y)] = (1/n)Σ_m W_ε(V̄_m, V̄_{n−1−m}) ≤ V̄_n, since (u'', y) minimises exactly x + V̄_m/y + V̄_{n−1−m}/(1−y).  ∎

**Numerical certification, corrected.** `dp_cert.py` used monotone
quadrature and an assumed relative roundoff allowance; its tables are
candidate potentials, not interval certificates. The independent checker
`certify_mpfr.c` reads the ε=0.02 table as exact binary64 candidate numbers
and checks every recurrence inequality for the rule with ε=1/64. See
[certification.md](certification.md) for the interval proof and reproduction.
All 512 inequalities pass; the last one gives

    W̄-recurrence upper = 121845.56860063219,
    V̄_512 = 121864.01799138699,
    V̄_512/512² ≤ 0.46487433620981994 < 0.4649.

The output records every candidate in hexadecimal, the upper recurrence,
and its nonnegative gap. The enclosure proves an upper bound on this rule's
cost; it does not certify an optimality constant or the large-h limit.

**Corollary 3.3.** For a uniformly random target and independent uniform
host of length ceil(Ck²), containment has probability 1−o(1) whenever
C>0.4649, by Theorem 2.1, padding, and the MPFR certificate for
R(512,1/64,V̄).

## 4. Optimality in the fresh-window model, and what the barrier now says (PROVED)

**Definition (fresh-window gap rule).**  A rule on one strip that, at each step, chooses a point of a *fresh*
Poisson process of intensity 1 on (0,∞) × (y_L, y_R) (the current gap; scaled x'' = Cx), by any measurable
function of the past, the current target value, and the process in that half-strip,
with no information about future target ranks beyond the processed prefix, and pays its x''-coordinate.  This is the
mean-field version of [W29] §4's gap-window rules with value-awareness and unlimited x-lookahead inside the gap.

**Theorem 4.1 (Bellman optimum).**  Let V_0 = 0, V_n := (1/n) Σ_{m=0}^{n−1} W_0(V_m, V_{n−1−m}) (ε = 0, the full
gap as window).  Then for every fresh-window gap rule and uniform σ ∈ S_h the expected strip cost (intensity 1,
unit height) is ≥ V_h, with equality for the rule with potentials V and no margin.  Hence in the fresh-window
model the best threshold constant obtainable from value strips of height h is exactly Ω*_h := V_h/h²
(cost at intensity C in a strip of height h: V_h/(hC), and success needs m·V_h/(hC) < k = mh).

*Proof.*  Finite-horizon Markov decision problem with state = (the gaps with their heights G_i and unplaced
counts n_i), Σ n_i = n_rem.  Claim: the optimal cost-to-go is Σ_i V_{n_i}/G_i.  Induction on n_rem.  The next
value is uniform among the unplaced ones, so it lies in gap i with probability n_i/n_rem and then has a uniform
rank m ∈ {0..n_i−1} inside it.  Given (i, m), the controller sees a fresh Poisson field on (0,∞) × (gap i) and
chooses a point (x, y); by the induction hypothesis the cost-to-go afterwards is Σ_{i'≠i} V_{n_{i'}}/G_{i'} +
V_m/(y − y_L) + V_{n_i−1−m}/(y_R − y).  The expected total is minimised by choosing, pointwise, the point
minimising x + V_m/(y − y_L) + V_{n_i−1−m}/(y_R − y) (any other measurable selection has a larger score on every
realisation), and the expectation of that minimum is W_0(V_m, V_{n_i−1−m})/G_i by scaling.  Averaging over m
gives V_{n_i}/G_i, which proves the claim.  The initial state (one gap of height 1, n values) gives V_n.  ∎

**Values (dp.py; NUMERICAL, uncertified Gauss–Legendre, but the old monotone-quadrature estimates at ε = 0 agree to
3·10^{−4}).**  V_1 = 1, V_2 = 3 (exact), V_h/h² = 0.6628 (3), 0.6175 (4), 0.5455 (8), 0.5067 (16), 0.4985 (20),
0.4857 (32), 0.4745 (64), 0.4686 (128), 0.4662 (256), 0.4632 (1000), 0.4627 (2000); the successive differences
halve with each doubling of h (V_h/h² ≈ Ω*_∞ + 0.84/h), so Ω*_∞ = lim V_h/h² ≈ 0.4623 (HEURISTIC extrapolation).
The dip below ½ starts at h = 20.

**Corollary 4.2 (value-awareness can beat one half).** The certified
h=512 margin rule has cost below .4649, so the value-blind one-half barrier
does not extend to value-aware rules. The smaller-h crossings and the limit
near .4623 in the preceding table are numerical. Bellman optimality applies
to the nonanticipating fresh-window model of §4 only.

**Remark 4.3 (the free-shaping bound is not ¼).**  The argument of log.md §1 — at time t the value lands in gap
j with probability p_j = n_j/(h−t+1), and Σ_j p_j/G_j ≥ (Σ_j √p_j)²/h — gives a lower bound on E Σ_t 1/G_t
for *any* gap rule, value-aware or not; numerically (freeshape_lb.py) it is 0.189 (h = 16), 0.160 (64), 0.153
(256), 0.151 (1024): far below ¼, so this counting argument cannot show that gap rules are capped at ¼.  The
real obstruction is the cost of shaping the gaps, which Theorem 4.1 accounts for exactly.

## 5. Current summary

The positive result is typical-target containment at every C>.4649, from
the corrected reduction and the directed MPFR certificate at ε=1/64.
The mean-cost Bellman optimum for nonanticipating fresh-window rules is
characterized analytically; its limiting numerical value is unproved.
The result improves the .49967+ε typical-target benchmark deduced from
Altschuler–Dubroff–Tikhomirov, but is not the first result below one half.
See the current ledger for precise quantifiers and priority limitations.
