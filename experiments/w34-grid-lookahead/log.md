# W34 — grid lookahead: log (chronological, with dead ends)

Date 2026-08-29.

## 0. Reading (W11 §4, W20, W31) and the key reformulation

* Goal (1) — "1-D Bellman in (remaining visits, y-level)" — is EXACTLY W20 Prop 4.3 (V_m(v)); its optimum
  C_mf(h) ↓ π/8 (W20 Prop 4.5).  So y-lookahead alone (cost-to-go over the strip's remaining visits) does NOT
  go below π/8 for h → ∞.  Nothing new to compute there; recorded as a negative in results.md.
* Goal (2) — Prop 3.1's hypothesis is "the point is chosen inside a quadrant on which the strip process is
  still Poisson(C) given the past".  A rule that, when choosing the point of strip s, also looks at strip
  s+1's process near the candidate x-positions, makes the quadrant of strip s+1 at the next step NOT fresh
  (it is conditioned on the previous choice).  That is the only escape: the clock is a shared resource and
  the copy should choose where it lands.  In the mean-field regime (r → ∞, each strip fresh at each round)
  the x-costs telescope: cost of a round = (x_last − a) + Σ_s (y_s − v_s).  With linear y-cost (h → ∞) the
  optimal round is a FIRST-PASSAGE problem across strips:
      G_s(a) = min_{p ∈ strip s, x_p > a} [ y_p + G_{s+1}(x_p) ],   G_{n+1}(x) = x,
  and the constant is γ_∞ := lim G_1(0)/n at intensity 1.  By scaling (x,y ↦ √C·(x,y); weight λ on y is
  a y-rescaling) the threshold of the FIXED model attainable by this class is  C* = γ²/4  (corner greedy:
  γ_0 = √(π/2) = 1.2533 ⇒ π/8 ✓).  Finite lookahead depth d gives γ_d ≥ γ_∞.
* Plan: (A) exact backward DP for γ_∞ (numpy); (B) forward Monte Carlo for depth d = 1,2,3,5 windowed rules;
  (C) rigorous reduction theorem (fresh windows, safe clock, F1/F2/F3 failures as in W20 Thm 4.2) for the
  depth-d windowed rule in the regime r → ∞, h ≥ ln² r (includes the diagonal r = h); (D) FREE model.

## 1. Exact DP for γ_∞ (fpp.py) — γ_∞(1) = 1.000 ± 0.002  (NUMERICAL)

fpp.py: backward recursion G_s(a) = min_{x_p>a}[y_p + G_{s+1}(x_p)], G_{n+1}(x) = x, each strip Poisson(1) on
[0,X]×[0,Y] (caps only remove paths ⇒ upward bias; Y = 6 vs 10 and X = 1.25n vs 2n agree within noise).
G_1(0)/n:  n=1000: 0.999, 1.001, 1.007;  n=2000 (6 seeds): 1.0057 1.0016 0.9972 1.0027 1.0075 1.0010;
n=4000: 1.0015 1.0047 1.0048;  n=8000: 1.0015 0.9997.   Mean u ≈ mean v ≈ 0.50 (flat direction: seeds give
u ∈ [0.46,0.56] with u+v ≈ 1.00 — the trade-off u ↔ v is nearly linear).  Outputs: fpp_n*.out.
Conclusion: the mean-field infinite-lookahead constant is  C*_∞ = γ_∞²/4 = 0.250 ± 0.001, i.e. numerically
EXACTLY Alon's 1/4 for tilted grids with r ≫ h ≫ 1 in the FIXED model.  Sanity: b = 1 block must give
√(π/2) = 1.2533 (corner greedy), checked below.  Whether γ_∞ = 1 exactly is open (no proof found; see proof.md §5).

## 2. Block rule (rigorous structure): E K_b / b for b strips, blocks i.i.d.

blocks.py: E K_b by Monte Carlo of the exact DP with b strips.  b = 1 gives 1.2550 ± 0.0046 vs √(π/2) = 1.2533 ✓.
C_b = (E K_b/2b)²: 0.356 (2), 0.325 (4), 0.302 (8), 0.285 (16), 0.274 (32), 0.265 (64), 0.261 (128), 0.257 (256).
E K_b − b ≈ 0.21√b (boundary layer of the terminal cost x_b).  x-part = y-part within noise (Lemma 2.2 ✓).

## 3. Writing the reduction — a gap found and fixed

First draft cut each row into blocks with a per-row random offset.  GAP: a strip at a fixed row position
(strip 0 of the tilted grid is always first) lands in a partial block in almost every row; partial blocks
(size < b, worst case singletons = corner greedy) have y-means up to √(π/(8C)) > 1 at C < π/8, so that
strip's y-budget is NOT controlled by the position-averaged mean.  Fix: a single global partition of the
visit sequence by a stationary renewal process with i.i.d. sizes uniform{b, b+1} — every visit then has the
exact stationary (size, position) law, all blocks are full-size, and consecutive rows' boundary strips are
distinct for the tilted grid (hypothesis (H_b) in general).  Price: the constant becomes the size-mixture
C^{mix}_b (between C_b and C_{b+1}); needs E K_{b+1} too (blocks_pairs_*.out).  The F4 step uses the exponential
mixing of the renewal (size,pos) chain across visits spaced by r; a fully elementary alternative would be to
draw the block sizes of each row afresh — not done, the mixing statement is standard.

Dead end (general τ): with strips revisited within b+1 visits in every row (τ_i alternating id / reverse),
the block must be split and the short block's y-mean can exceed the budget; per-strip Lagrange weights λ_s
would fix it but were not carried out.  Theorem 3.4 therefore has hypothesis (H_b); W11's π/8 stays for the rest.

## 4. Certification route for b = 2 (not done)

Pr(K_2 > t) = E exp(−∫_0^t (t − x − m(x))_+ dx), m(x) := min{y_p : p ∈ Ψ_1, x_p < x} (running minimum of strip
1; +∞ before its first point), because a pair (p, q) costs x_q + y_p + y_q < t iff q ∈ {x > x_p, x + y < t − y_p}
and the union of these regions over p is {y < t − x − m(x)}.  m is a Markov jump process (rate m, jump to
Uniform(0,m)); F(x, m) := E[exp(−∫_x^t (t−x'−m(x'))_+ dx') | m(x) = m] solves ∂_x F = (t−x−m)_+ F − ∫_0^m
(F(x,y) − F(x,m)) dy with F(t,·) = 1 and F(x,m) = F(x, t−x) for m ≥ t − x; E K_2 = ∫_0^∞ F(0, t) dt.  A monotone
scheme (F is monotone in m and in x) would give a certified bound; ~a day's work, not attempted.

## 5. γ_∞ = 1?

No proof.  Facts: γ_∞ ≤ γ_b for all b (block paths are feasible round paths); the recursion (2.2) is a min-plus
linear map on nondecreasing functions; a stationary version (G_s(x) − x stationary in x with a suitable
boundary noise, à la Burke/Hammersley) would identify the constant.  The numerical evidence (five sizes,
eleven runs, all within 0.008 of 1, no drift in n) is strong.  Consequence if true: the FIXED model's
constant in the iterated limit r → ∞, h → ∞ is 1/4 (not π/8 as W20 Conj 4.6 would give), so the corner greedy
loses exactly the factor π/2 that Hammersley's √(8/π)-greedy loses on the LIS.

## 6. Not done
Goal (3) (FREE model with adaptive boundaries): only the inequality C^free ≤ min(C^fix(r,h), C^fix(h,r)) and
the heuristic that budget reallocation gains O(h^{−1/2}) relative (proof.md §6).  Time ran out.
