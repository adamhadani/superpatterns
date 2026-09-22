# W34 — cross-strip lookahead for block-grid patterns: below π/8, numerically to 1/4

Date 2026-08-29.  Tags PROVED / NUMERICAL / HEURISTIC.  Background: W11 proof.md §4 (corner greedy, π/8),
W20 proof.md §3–4 (fresh-quadrant barrier Prop 3.1; mean-field theorem 4.2; Bellman C_mf(h) ↓ π/8),
W31 proof.md (windows, safe clock).  Numerics: results.md; chronology and dead ends: log.md.

**Current status (2026-09-10).** The first-passage functional and scaling
argument in §2 are unchanged. W36 now proves γ_∞=1 analytically. The original
application assumed only a fixed no-revisit window, which did not imply the
Ω(r) spacing used in the proof. The corrected hypothesis is successive
visits to the same strip separated by at least ηr, for fixed η>0. The
[complete repaired reduction](reduction.md) also controls the random
conditional means and partial boundary blocks, and gives failure ≤k^(−A)
for every fixed A>0. The resulting simultaneous tilted-grid corollary is
stated there. The Monte Carlo constants in §4 remain numerical estimates.

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

## 3. The block rule and the corrected reduction

**Theorem 3.4.** Fix b≥1, η>0, A>0 and C>C_b^mix. For π_τ∈G(r,h),
k=rh, with min(r,h)≥log³k and successive strip visits at least ηr apart,
P(π_τ not contained in Π_(Ck²) in the fixed-strip model)≤k^(−A) for all
sufficiently large k, uniformly over individual visiting sequences.

The full proof is [reduction.md](reduction.md). It uses a stationary
partition into blocks of lengths b,b+1, a safe clock, windows with
L²=(b+1)(A+3)log k/C, artificial continuation on failed blocks, renewal
reward concentration for the x budget, and exponential mixing of the
partition phase followed by conditional concentration for each y budget.
This replaces the entire original §3. The old H_b hypothesis is insufficient;
the explicit counterexample is recorded at the end of the repaired proof.

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

## 5. The infinite-lookahead constant: γ_∞=1 (proved in W36)

[W36](../w36-gamma-limit/proof.md) proves n≤E K_n≤n+√(2n)+1/2.
Consequently C_b and C_b^mix tend to 1/4. This settles the numerical
conjecture about the independent-strip mean cost. It is not a matching
lower bound for the containment threshold of a general grid pattern.

## 6. The free model

Fixed-strip containment implies free containment. W36's exact γ∞=1
settles the independent-strip mean-cost conjecture; it supplies no matching
lower bound for free containment. Small-r numerical extrapolations are not
evidence of an exact threshold in the regime where both r and h grow.

## Review note, 2026-09-10

The previous coordinator's approval of §3 missed the revisit and conditional
mean gaps. `historical-proof.md` retains that record; `reduction.md` is the
current proof. The generic weaker H_b application is withdrawn.
