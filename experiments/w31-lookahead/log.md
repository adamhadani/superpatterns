# W31 — x-lookahead / value-aware gap rules for a random pattern: chronology and dead ends

Date 2026-08-29.  Goal: rigorous threshold < ½·k² for a uniformly random π ∈ S_k (beating W29's Ω_64 = 0.527).

## 1. Analysis of the ½ barrier (19:50)

W29 Thm 4.1: a value-blind gap-window rule pays ≥ t/h for the t-th point of a strip because σ_t falls in a
uniformly random one of the t gaps and Σ_j 1/G_j ≥ t²/h.  With a VALUE-AWARE rule the gap containing σ_t is
not uniform: at time t the t gaps hold n_1..n_t unplaced values (Σ n_j = h−t+1) and σ_t is in gap j with
probability p_j = n_j/(h−t+1).  Then min_G Σ_j p_j/G_j s.t. Σ G_j = h equals (Σ_j √p_j)²/h ≤ t/h, with strict
inequality whenever the n_j are unequal — so value-awareness CAN beat ½ in principle (route 4, negative
direction: the barrier is only for value-blind rules).  The shaping of the gaps costs x, however, so the
achievable constant is a control problem.

## 2. Key observation: the fresh-window problem is self-similar (20:00)

In the mean-field regime (h fixed, m = k/h → ∞, as in W20 Thm 4.2) every visit of a strip sees a fresh
Poisson half-strip.  Then the cost-to-go of a state is a SUM over the current gaps: a gap of height G holding
n unplaced values costs V_n/G, where V_n is the optimal cost of n values in a unit-height gap (scale y by 1/G,
x by G: Poisson(1) is preserved and x-cost divides by G).  The order in which the n values of a gap arrive is
uniform and independent of everything else.  Hence the Bellman recursion is one-dimensional:
   V_0 = 0,  V_n = (1/n) Σ_{m=0}^{n−1} W(V_m, V_{n−1−m}),
   W(A,B) = E min_{(x,y)∈Ψ} [x + A/y + B/(1−y)],  Ψ Poisson(1) on (0,∞)×(0,1),
and W has the closed form smin + ∫_{smin}^∞ exp(−area(s)) ds with area(s) = s(y₂−y₁) − A ln(y₂/y₁) +
B ln((1−y₂)/(1−y₁)), y₁,₂ the roots of s y² − (s+A−B) y + A = 0, smin = (√A+√B)².  Sanity: W(0,0) = 1,
W(1,0) = 3 (both exact by hand; dp.py agrees to 1e-9).  The strip's threshold constant is Ω_h = V_h/h².

dp.py, first run (n ≤ 40): V_n/n² = 1, 0.75, 0.6628, 0.6175, …, 0.4985 (n = 20), 0.4872 (30), 0.4813 (40).
V_2/4 = 0.75 = the blind barrier exactly (value-awareness is useless at h = 2); below the blind barrier from
n = 3 on; BELOW ½ from n = 20.  Running n ≤ 2000 to see the limit (heuristic guess π/8 = 0.3927 from the
(Σ√p)² computation with exponential spacings; see proof.md §4).

## 3. Plan for the rigorous part

(a) Reduction theorem (proof.md §2): random π, k = mh, strips of h values, count-indexed potential rules with
    an x-window of length L and the "safe clock" a_safe := max(a, right edge of the strip's explored sets) so
    that W19 Lemma 1.2 applies verbatim; the collisions (a_safe > a) are rare because the clock moves by Θ(m)
    between visits and cost O(ln² k)·L in total (annealed over π).  Chernoff needs a light tail; the DP-optimal
    rule has tiny gaps with positive probability, so the theorem is stated for rules with relative margins
    (windows [y_L + ε_b G, y_R − ε_a G], ε depending on counts only) — still self-similar — and the constant of
    such a rule is computed by the same quadrature.  Numerically the margins cost almost nothing (results.md).
(b) Lower bound (proof.md §4): in the fresh-window model V_h/h² is the exact optimum over ALL gap rules
    (value-aware, any lookahead inside the current gap's half-strip).  So Ω_h^* := V_h/h² is both what the
    method achieves and what it cannot beat.

## 4. Results (20:00–20:20)

- dp.py to n = 2000: V_n/n² = 0.4985 (20), 0.4745 (64), 0.4686 (128), 0.4640 (512), 0.4627 (2000); differences
  halve per doubling ⇒ limit ≈ 0.4623.  NOT π/8: the (Σ√p)² heuristic ignores the cost of shaping the gaps
  (freeshape_lb.py gives that bound as ≈ 0.15, useless — recorded in proof.md Remark 4.3).
- dp_cert.py (rectangle-rule upper bounds, monotone in s): ε = 0.05: 0.47646 (64), 0.47159 (128); ε = 0.02:
  0.46801 (160), 0.46487 (512).  Margins cost < 0.002.
- validate2d.py, first version, FAILED (0/3 at C = 0.6, extra cost 218 of k = 256): the explored edge was set to
  a_s + ψ(q) (using Φ ≥ 0), i.e. ≈ Φ_min/C ≈ 100 units beyond the chosen point, so every revisit collided.
  Fix: the sublevel set {ψ ≤ ψ(q)} ends at x'(q) + (Φ(y'(q)) − Φ_min)/C (proof.md Lemma 1.1(c)); observed extent
  ≈ 0.4 per collision.  After the fix: success 10/10 at C = 0.50 for h = 64, 128 (k = 2048), 0/10 at 0.46,
  3/10 at 0.48; mean cost/k matches Ω_h(ε)/C + collision cost to 1 % (results.md §3).

## 5. Dead ends / routes not taken (with reasons)

- Route (1) x-lookahead WITHOUT value-awareness: pointless — [W29] Thm 4.1's bound uses only X_t ≥ Exp(C·gap),
  which any in-gap choice satisfies; lookahead helps only through the value-aware potential.
- Lookahead OUTSIDE the current gap (peeking at the half-strips of the other gaps): would break the
  fresh-search structure of [W19] Lemma 1.2 (the peeked region is explored and must be excised from later
  searches); by Thm 4.1 the in-gap class is capped at ≈ 0.4623, so this is the only remaining greedy lever.
  Not attempted (time).
- Route (2) position blocks × value strips: for a random π the cells of an m×m block grid hold hypergeometric
  counts (mean 1), not one point each, and the within-strip order is random, so the corner greedy of W11 Thm 10
  does not apply (W19 Prop 3.1 already shows it needs chains).  Position strips give the same problem
  transposed; using both directions at once is the FREE-model optimisation W20 §4.4 could not analyse.  Not
  pursued.
- Route (3) subadditivity for random π: no natural monotone composition (a random pattern of size 2k does not
  decompose into two random patterns of size k on separated regions of the square); the cost of a strip is
  self-similar only in the mean-field model, where Thm 4.1 already gives the exact constant.  Not pursued.
- Route (4), proving the ½ barrier for value-aware rules: FALSE (Cor 4.2) — settled in the other direction.
- Chernoff with the DP-optimal (ε = 0) potentials: the MGF of a strip's cost is infinite (a gap of height g
  containing a value costs an Exp(g)-like amount and Pr(g < θ) > 0), so a margin ε > 0 is kept for the
  theorem; it costs < 0.002 in the constant.
- Failure speed: only O(ln k / k) because collisions are handled by Markov; a windowed variant with
  L = Θ(ln m) as in W20 Thm 4.2 would restore e^{−ηk} (not written out).

Total: reduction PROVED, constant 0.4649 certified (h = 512, ε = 0.02); the class cap 0.4623 is the new barrier.
