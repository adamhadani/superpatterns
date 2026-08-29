# W29 — random-pattern threshold: chronology and dead ends

## 2026-08-29 19:10 start
Read NOTES.md, W21 results, W19 proof (rigid rows Thm 2.1, mixed greedy 4.1, reserve greedy 4B), W11 §4 (corner
greedy, Thm 4.1/4.4), W20 §3 (fresh-quadrant barrier π/8), W27 outline.

Chosen route (idea 2 generalised): W19's reserve greedy works only on strips on which π^{-1} is monotone.
Observation: the monotonicity is NOT needed if the window for the next point of a strip is the *gap* between the
already-placed points of the strip whose values are the nearest below and above (minus a reserve β per unplaced
value in the gap), and the search is "leftmost in the window" (λ = 0), for which the disjointness hypothesis of
W19 Lemma 1.2 is trivial (explored sets are {a' < x ≤ x(q')} × window', later regions have x > a ≥ x(q')).
With the leftmost rule the y-coordinate is uniform in the window independently of C, so the window sequence
(W_i) is a C-independent process driven only by the strip sub-pattern σ ∈ S_h and the uniform draws, and
E[total x-cost] = (1/C) E Σ_i 1/W_i.  For a uniformly random π ∈ S_k the sub-patterns of k/h consecutive value
strips are i.i.d. uniform in S_h (patterns of π^{-1} on disjoint index blocks), so the per-strip costs are i.i.d.
and the annealed threshold constant is Ω_h := min over rule parameters of E[Σ_{i≤h} 1/W_i]/h.
To keep gaps regular a *band* of width w around a target (absolute row target v+1/2, or proportional position in
the gap) is intersected with the reserve interval; fallback to the reserve interval if the intersection is short.

Ideas not pursued (reasons):
- (1) He–Kwan quasirandom argument with optimised constants: their bound is 20k² via thread overlaps; W9/W13
  already refined it and are stuck at 72k²/800k² — nowhere near 0.757, let alone 1/4.
- (3) second moment of canonical copies for random π: W12/W16 machinery gives c_21-type constants for *absence*
  (lower bounds on threshold), and Janson-type exponents are capped at C/2 (W22); a second moment cannot give a
  containment threshold below the first-moment constant anyway, and the first-moment constant e^{-2}... is the
  trivial k²/e²-scale bound, not a containment proof. Not a route to an upper bound.
- (4) lower bounds: W12's universal absence (k > 2.279√N ⇒ threshold ≥ 0.1925k²) is a first-moment bound and is
  already pattern-independent; improving it for random π needs the variance, out of scope in 2h. Recorded.

## 19:15–19:40 implementation and numerics
- strip.c (y-only chain; C-independent): smoke test reproduces rigid rows (w ≤ 1 ⇒ Ω = 1) and the exact value
  Ω_2 = (1+ln 2)/2 = 0.8466 for the no-band rule, β = 1.
- sweep1/2/3: the row-centre target (mode 0) is always worse than the proportional target (mode 1); no band
  (mode 2) gives 0.564–0.58; the optimum is w ≈ 3–3.25, β ≈ 0.7–0.8, flat within 0.01 over w ∈ [2.5,4], β ∈ [0.6,0.85].
  Ω_h: 0.798, 0.676, 0.606, 0.563, 0.537, 0.527, 0.525, 0.517, 0.520, 0.515, 0.517 (h = 2,4,…,1024, 2048).
- Barrier found and PROVED (proof.md Thm 4.1): for any gap-window rule E T ≥ (h+1)/(2C), because the t-th point
  of a strip enters a uniformly random one of the t current gaps (independence of relative ranks) and by AM–HM
  E 1/G ≥ t/h.  This explains why the numbers stall at ≈ 0.51–0.52: this greedy family cannot go below ½.
- validate2d.py (real 2-D Poisson points, real π, asserts a copy): k = 400, h = 40: 2/20, 13/20, 20/20, 20/20 at
  C = 0.5, 0.55, 0.6, 0.7 — matches Ω_40 = 0.537 and the Chernoff exponents.

## Dead ends / why not < 1/4
- Two-sided score x + λ|y − y_0| (diamond search) instead of leftmost: the explored diamonds of earlier searches
  overlap later windows (disjointness of W19 Lemma 1.2 fails); fixing it by restarting x beyond the explored
  diamond costs exactly the y-deviation, and for wide windows the diamond's E score ½√(πλ/C) is far worse than
  the leftmost's 1/(CW) → no gain; dropped without numerics.
- Absolute row targets (mode 0): worse than proportional targets at every (h, w, β) (sweep3).
- One strip h = k (no fixed strips): would give Ω_∞ but the concentration of Σ 1/W_t over π needs a separate
  argument (the sum is not a bounded-difference function of the insertion ranks); fixed h with i.i.d. strips is
  rigorous and loses only 0.01 (Ω_64 vs Ω_1024).
- The ½ barrier (Thm 4.1) is intrinsic to "windows inside the current value gap": the cost of the t-th point is
  ≥ t/h. Beating it needs a rule that uses the process ahead in x (choose among candidate points by what they
  leave for later values), i.e. lookahead/non-greedy; and 1/4 for random π (W21 numerics say ≈ 0.22) is, as for
  the identity, a Hammersley-type (non-greedy) constant.  Both recorded as open.

## Final state (19:45): proof.md complete (Thm 2.1, 3.2 PROVED; Ω_h NUMERICAL; Thm 4.1 PROVED), results.md, README.md.
