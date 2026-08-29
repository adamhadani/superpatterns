# W17 — c_21 lower bound via renewal ("sweep") rules (log)

Date 2026-08-29.  Directory work/w17-hammersley/.  Files: rules.c (Monte Carlo of sweep rules, from the first
W17 attempt; reused), enum3.c (exact first-occurrence enumeration for a pattern tau; reused), square_series.py
(exact series for the square rule), tau_bounds.py (general tau), enum_*.out, proof.md.

## 0. Outcome in one line
Rigorous, closed form: c_21 >= 2 / sum_{n>=1} Gamma(n+3/2) n(3n+7) / (2(n+2) n! (n+1)!) = 0.78660  (square-sweep
first-descent rule), and the simpler strip rule gives c_21 >= sqrt(2/(e(4-e))) = 0.75765.  Monte Carlo (not rigorous)
for l_p sweeps: 0.803 at p = 1.5.  Previous rigorous bound: 0.598 (W12 grid).  Window now 0.787 <= c_21 <= 1.140.

## 1. Why the planned "boxes along a geodesic" route was dropped
The route in the task statement (boxes U_i along a maximal chain, p* from the stationary Hammersley process) needs
the joint law of consecutive gaps along the geodesic.  What Cator-Groeneboom give is the law of the stationary
process on space-time lines and of the second-class particle, not the joint law of (g_i, h_{i+1}) along the
point-to-point geodesic; the Burke property gives exponential marginals for gaps along a horizontal or vertical
LINE, not along the geodesic.  Without that joint law one gets only the crude bound of W12 log S1 (0.28).  Instead the
sketch left by the first W17 agent in rules.c (renewal rules with i.i.d. increments) turned out to be both rigorous
and strong; it is the Hammersley-1972 lower-bound argument for the LIS (greedy l_1 sweep: LIS >= sqrt(8/pi) sqrt N),
adapted to descent pairs, and it does not need any geodesic information.

## 2. Renewal rules (details in proof.md)
Unit-intensity Poisson process on the quadrant; sweep a growing region c + sB (B open, down-closed); stop at the
first arrival that completes a copy of tau; corner := coordinatewise max of the copy; next step from the corner.
Because the new point is on the boundary of sB and the corner dominates it, the quadrant above-right of the corner
is disjoint from the swept region, so the increments (dx, dy) are i.i.d. and c_tau >= 2/E[dx+dy]  (Theorem A).

Strip rule (B = strip of height h, first descent, a = lowest earlier point above the new point b):
  E dx = e/h,  E dy = h (4-e)/2  (exact, elementary: first non-record of i.i.d. uniforms + order statistics).
  min_h: E cost = sqrt(2e(4-e)) = 2.63972, c_21 >= 0.75765.  MC check (rules.c, rule 0, h = 1.458, 2e6 samples):
  E dx 1.86384 (e/h = 1.86436), E dy 0.93398 (0.6409 h = 0.93437).

Square rule (B = unit square; first descent; partner = chain point with least coordinate above the new point):
  Given the stopping radius r and N = n earlier points, those n points are i.i.d. uniform in (0,r)^2 conditioned
  to form an increasing chain (prob 1/n!), so their sorted x's and sorted y's are INDEPENDENT uniform order
  statistics; the new boundary point (w,r) or (r,w) has uniform w.  This gives the exact series
     E cost = sum_{n>=1} E[r_{n+1}] (1/n!) (1/(n+1)) sum_{k=0}^{n-1} (1 + (k+2)/(n+2)),  E r_{n+1} = Gamma(n+3/2)/n!
            = sum_{n>=1} Gamma(n+3/2) n (3n+7) / (2 (n+2) n! (n+1)!) = 2.54256871456...
  Checks: sum_n P(N=n) = sum n/(n+1)! = 1; E(#points) = e (MC 2.7184); MC of the rule (2e7 samples, rules.c rule 1):
  E cost 2.54276 +- 0.00022.  Terms: 1.10778, 0.90007, 0.38772, 0.11511, 0.02618, 0.00483, 0.00075, 0.00010, ...;
  T_{n+1}/T_n <= 0.11 for n >= 9 so the tail after n = 10 is < 2e-7.
  => c_21 >= 2/2.5425687 = 0.786606.

Other rules (MC only, rules.c): l_1 sweep 2.5064 (0.798); l_1.5 sweep 2.4902 +- 0.0009 (0.8031); l_2 2.4943; l_3 2.5102;
square with threshold "accept iff cost <= theta r": theta >= 2 is identical to first descent, theta = 1.8 worse
(2.5885), theta = 1.6 worse (2.7087); strip with growing threshold (rule 3): worse than plain strip.  So among the
rules tried, the first-descent rule with an l_p sweep, p ~ 1.5, is the best: c_21 >= 0.803 (MC-certified only).

## 3. General tau (tau_bounds.py; enum3 to m = 11 for all 17 classes of S_3 ∪ S_4 and their inverses)
Square rule (a) / strip rule (b), rigorous (tails: exact |Av_m| via Catalan / Gessel / Bona, verified against the
enumeration for m <= 11; 1324-class via block bound):
  S_3: 123: 0.5384/0.5243, 132: 0.5354/0.5214, 231: 0.5516/0.5390.   (W12 grid: 0.389; conjecture 2/3)
  S_4: 1234: 0.4035/0.3963, 1243: 0.4020, 1324: 0.3853*, 1342: 0.4100, 1432: 0.4017, 2143: 0.4020, 2341: 0.4127,
       2413: 0.4105, 2431: 0.4115, 3412: 0.4126, 3421: 0.4114, 4231: 0.3932*, 4321: 0.4035.  (W12: 0.30; conjecture 1/2)
  E n_tau (expected number of uniform points until tau appears) = sum_m |Av_m(tau)|/m!: 5.0907 (j=3), 8.0865 (1234 class),
  8.0360 (1342 class), >= 9.0587 (1324 class, truncated).
The square rule beats the strip rule for every tau by 2-3 %.

## 4. Numerics for the obstruction
* floor.py: E[min over ALL descent pairs in the quadrant of x_b + y_a] = 2.3861 +- 0.0019 => no renewal rule (even a
  clairvoyant one) can give more than 0.838.  Best causal rule found: l_1.5 sweep, 2.4884 +- 0.0002 (0.8037).
* boxes.c (task item 3): along a patience-sorting LIS path in Poisson(N) (N = 10^4, 10^5): LIS/sqrt N = 1.91, 1.97;
  fraction of nonempty boxes U_i = (x_{i-1},x_i) x (y_i,y_{i+1}): 0.149, 0.153; greedy stacked selection (indices
  with gap >= 2): 0.132, 0.135 of L, i.e. L_21/sqrt N >= 0.252, 0.265 — far below the renewal bound, as predicted by
  the gap size 1/(2 sqrt N) along a maximal chain (mean N*area = 1/4).  Not pursued further (would need the joint law
  of consecutive gaps along the point-to-point geodesic, which Cator-Groeneboom do not provide).

## 5. Not done / ideas
* Exact evaluation of the l_1 (triangle) sweep: needs the law of n uniform points in a triangle conditioned to form
  a chain (no product structure); polytope integrals are exact for each n but the tail P(chain of n in triangle) has
  no usable closed form.  Gain would be 0.787 -> 0.798 (l_1) or 0.803 (l_1.5, non-polytope).
* Markov (non-renewal) rules: allow the next sweep to depend on the previous configuration, e.g. two-step lookahead
  choosing among several available descent pairs; the LLN still applies to a positive-recurrent Markov chain of
  increments.  This is the only way past the 0.838 floor within "local" constructions; the numerics of W10
  (L_21/sqrt N -> 1) say the global optimum uses far more than local information.
Time spent ≈ 2 h.
