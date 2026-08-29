# W19 — general greedy / speed of the corner greedy — log

Date: 2026-08-29.  Machine load at start: 19 (k7n22 SAT + others); I keep my own jobs to <= 2 cores.

## 0. Reading notes (W11 §4, notes §Alon, W18)
- Thm 4.1/4.4 (corner greedy) need: strips = value intervals on which pi^{-1} is INCREASING (column chains).
  Nothing else about pi is used.  The "verbatim for every pi" claim in my brief is therefore FALSE as stated:
  with strips of h consecutive values, a general pi has, inside strip j, the pattern sigma_j in S_h (its h
  points in position order), which is a chain only for the block-grid/union-of-runs class.  Counterexample
  and exact characterisation in proof.md §2.
- W18: threads (= rigid-row greedies at integer value shifts) coalesce at cost linear in the lag; no polylog
  family of correlated greedies can give speed k ln k at m = Ck.

## 1. Analysis plan (before numerics)
(a) Baseline for ALL pi: rigid rows of height 1/k, leftmost point in the row to the right of the x-level.
    Increments k*dx are i.i.d. Exp(C) exactly (each row searched once, rows disjoint).  Pr(fail) <=
    Pr(Poisson(Ck) <= k-1).  Threshold C=1, speed k.  This is He-Kwan's thread in Poisson form.
(b) The corner greedy generalises to unions of MONOTONE runs on value intervals (up-runs: lower corner,
    down-runs: upper corner), arbitrary lengths h_j; and, mixed with (a), to every pi: each value interval
    on which pi^{-1} is monotone may be handled by the corner rule, the remaining values by rigid rows.
    Threshold interpolates between pi/8 (all mass in long runs) and 1 (random pi).  Speed: min run length.
(c) Speed.  Every scheme that places the points of a strip/column with the x-positions of the neighbouring
    columns frozen is a sum of h (near-)independent increments and fails with probability e^{-Theta(C h)};
    two-phase repair (below) gives each column an INDEPENDENT second chance (doubles the exponent) but
    cannot change the speed h.  The x-part is e^{-Theta(Ck)}.  Consequently no greedy of this type can give
    the union bound over S_k at N = O(k^2): it needs C >~ ln k, i.e. n = O(k^2 ln k) (the trivial bound).
    I will (i) prove the two-phase repair theorem, (ii) prove the barrier as a proposition about the class
    of procedures, (iii) record the dead ends for "free strips".

## 2. Numerics I: rigid rows, the false "verbatim" claim, and the mixed greedy (gg.c; out_general.txt, out_scanC.txt)
gg.c (compile: cc -O2 -o gg gg.c -lm).  All modes validate every produced copy by an O(k^2) order check
("noncopy" column); the "thm" column counts runs on which the extended-process event of the theorem held
(emulated exactly: when the restricted minimiser is found, the probability that the extended process has a
closer point outside the region is exp(-N * outside-area) and is sampled).
- rows (Thm 2.1): success 219/400 (k=64), 200/400 (k=100), 202/400 (k=144) at C=1: Pr(Poisson(k) >= k) ~ 0.5. OK.
  C=0.5: 0/400; C=2: 400/400; C=0.9,k=100: 68/400; C=1.2: 389/400 (Pr(Poisson(120)>=100)=0.97). OK.
- verbatim (equal strips of sqrt(k) values, corner rule, random pi): noncopy = 98/100, 100/100, 100/100
  (k = 64,100,144, C=1,2; at C=0.5 the run rarely completes).  The output is a copy of pi', never of pi.
- runs L=3/4 (Thm 4.1, theorem event "thm"): at C=1 the theorem event holds LESS often than rigid rows (e.g.
  k=100: thm=90 (L=3), 219 (L=4) vs rows 200) because short corner strips overflow with constant probability;
  at C=2, 341-391/400 vs rows 400/400.  So Theorem 4.1 is useless for random pi, as predicted (proof.md §4 (i)).
- BUT the PRACTICAL restricted greedy (search confined to the strip; column "success") is much better:
  k=100, C=1: 332-362/400 vs 195 rows; C=0.8: 195/400 vs 8; C=0.7: 49-84/400 vs 1.

## 3. Dead end: the restricted corner rule has heavy-tailed x-increments (check_constants.py)
Independent MC of the restricted rule (Markov chain in the remaining height rho of the strip): E[total x]/h
at C=1 is 1.18 (h=2), 1.12 (h=3), but with huge variance (C=0.8, h=4: 10.9 in one run of 200000 samples).
Reason: the last search of a strip is a leftmost search in a sliver of height rho, with x-increment Exp(C rho),
and rho has positive density at 0; so E[1/rho] = infinity and Pr(X > t) ~ a/t.  With ~k/2.4 strips the
probability that some strip alone exhausts the x-budget k is a CONSTANT, so the practical success rate
plateaus (86%, 87%, 87% at k=64,100,144, C=1) instead of tending to 1.  The "meanX/value" column of gg is
E[min(sum X, k)]/k and hides the tail.  => The restricted rule without a reserve does NOT lower the threshold.

## 4. The reserve rule (reserve_mc.py, quad_h2.py, mc_h3.py, gg runs ... beta lam)
Fix: the m-th of h points searches only up to height (top - beta*(h-m)/k) — at least beta units are reserved
for each future point — and the last point uses the leftmost rule.  Every search region then has height
>= beta, so X <=_st beta*lam + Exp(C beta) conditionally on the past: all MGFs finite, Chernoff applies.
- reserve_mc.py (independent numpy MC): mean x per value for a random pi (value-fractions by run length of
  the non-overlapping monotone segmentation of pi^{-1}: 2: 0.558, 3: 0.301, 4: 0.104, 5: 0.026, ...):
  C=0.8: 0.93 (beta=0.7, lam=0.75), 0.91 (0.5, 0.5); C=0.75: 0.97-0.99; C=0.7: >1.04.
- quad_h2.py (deterministic quadrature, 1D+2D integrals, checked against MC: 0.9651 vs 0.9660): for h=2 with
  the last point leftmost, min over (beta,lam) of E[T_2]/2 equals 1 at C = 0.757 (beta=0.4, lam=1.1);
  E[T_2]/2 = 0.947 at C=0.8, 0.891 at 0.85, 0.842 at 0.9, 0.758 at 1.0.
- gg validation (out_scanR.txt, beta=0.7, lam=0.75, corner also for the last point): success/300 for k=100,200,400:
  C=0.8: 235, 253, 276;  C=0.85: 275, 291, 297;  C=0.9: 290, 300, 300;  C=1: 300, 300, 300.  Rigid rows at
  C=0.9, k=100: 68/400.  The increase with k at fixed C=0.8, 0.85 is the signature of a threshold below 0.8.

## 5. Numerics II: universal threshold (mc_h3.py, out_h3.txt; quad_h2.py; out_scanR2.txt)
- Optimised reserve rule, last point leftmost.  E[T_h]/h (mean x-increment per value in a strip of h values):
    C=0.76: h=2 0.992 (beta=0.4, lam=1.1), h=3 0.875;  C=0.80: 0.942 / 0.832;  C=0.85: 0.890 / 0.783;
    C=0.90: 0.841 / 0.743;  C=1.00: 0.754 / 0.666.   h=3 is strictly easier than h=2; h=2 sets C_univ = 0.757.
- Chernoff exponents eta(C) = sup_theta min_{h=2,3} (theta - ln M_h(theta)/h) with (beta,lam) = (0.4,1.1) for h=2 and
  (0.35,(1,1)) for h=3, MGFs by MC (400000 samples): C=0.8: 0.0014; 0.85: 0.0058; 0.9: 0.013; 1.0: 0.035; 1.2: 0.096
  (rigid rows C-1-ln C: 0 for C<=1, 0.018 at 1.2).
- Validation with gg (independent code; beta=0.4, lam=1.1, last point leftmost; random pi; 300 reps):
    C=0.78: 251, 269, 291, 298 successes for k=100, 200, 400, 800;  C=0.80: 267, 282, 291, 299;
    C=0.85: 286, 297, 300 (k=100,200,400).  Every produced copy passed the order check.
  Compare rigid rows: C=0.9, k=100: 68/400.  Conclusion: the universal per-pattern threshold is <= 0.757 k^2
  (Thm 4B.3; reduction proved, constant numerical).

## 6. Goal 2 (speed): two-phase repair — a bug, its correction, and why it is useless (out of gg grid runs)
- First version: phase-2 boxes (x_p, x_p+delta/k) x S_j.  gg: at C=3, r=16, h=4, delta=0.5 (C delta = 1.5,
  predicted per-strip repair probability Pr(Poisson(6) >= 4) = 0.85), 0 of 6 bad strips were repaired.  Debug
  output showed phase-2 y-increments ~1.2 per row instead of 0.67: the box overlaps the phase-1 explored
  triangle, which extends V_p/k to the RIGHT of the found point.  The claim "Delta_p is left of x_p" in my
  first proof was false.  Corrected: boxes (x_p+V_p/k, x_p+(V_p+delta)/k), x-level advanced by (V_p+delta)/k.
- Corrected version costs x-budget sum(U+V+delta) < k: feasible only for C > 6.3.  gg (corrected): C=6, h=4,
  delta=0.5: xfail 249/400 (E T = 0.51 per point + 0.5 > 1... marginal), badcols 0; C=8, k=144, h=4: 398/400,
  badcols 0.  In the feasible regime no strip is ever bad, so the repair never acts.  Theorem 5.1 (corrected)
  is proved but practically empty; recorded as such.
- Speed: Prop 5.2 (exact speeds of the procedures) and Prop 5.3 (chain through frozen windows: the greedy is
  optimal, brute-force checked on 3000 random instances, check_prop53.py: 0 violations) show that any
  column-by-column scheme has speed <= O(C h) per strip.  The union bound over S_k at N = O(k^2) is out of
  reach for every greedy-type argument; n = (1+o(1)) k^2 (ln k + ln ln k) (Cor 2.2) is what they give.

## 7. Dead ends for free strips (Goal 2), with reasons
(a) Free strips with row-major processing: column j+1's first point is placed long before column j's last,
    and must be above it; no causal rule can guarantee separation without a committed boundary.
(b) Column-major processing: column 0 would have to be built with x-gaps of size ~ r/k to leave room for the
    other columns, i.e. rigid slabs by another name.
(c) Elastic strips (start columns in the middle of their strips): the overflow region of column j is the
    start region of column j+1; the budget per column is h regardless.
(d) Multiple independent chances per column (M boxes of width delta/M): exponent ~ h(C delta - M - M ln(C delta/M)),
    the same order Theta(C h) as one chance.
(e) Bad-cut / last-passage formulation: could not prove that failure of the free model forces a sparse
    monotone cut; the copy may use x-spacings >> 1/k in some rows and << 1/k in others.  Open.
(f) Janson's inequality on the number of copies: Delta/mu^2 >= const/C (pairs sharing one point), so it gives
    at best e^{-O(C)}: useless at N = Ck^2.

## 8. Verification summary
- check_prop31.py: Prop 3.1 (copy iff strips are chains; output = pi') on all pi in S_4, S_5, S_6 with several
  partitions, 5902 completed runs, 0 violations.
- check_prop53.py: Prop 5.3 greedy optimality, 3000 random instances, 0 violations.
- check_constants.py: E U = 0.6271 vs sqrt(pi/8) = 0.6267; c(C) = 0.011, 0.036, 0.109, 0.202, 0.460, 0.749, 1.922
  for C = 0.5, 0.6, 0.8, 1, 1.5, 2, 4 (W11: 0.011, 0.036, 0.109, 0.201, 0.465, 0.750, 1.92).  Cor 2.2 arithmetic checked.
- quad_h2.py vs MC: 0.9651 vs 0.9660 for E[T_2]/2 at C=0.8, beta=0.7, lam=0.75.
Files: gg.c (simulator), runall.sh/scanC.sh/scanR.sh/scanR2.sh (batches), out_*.txt (raw outputs).
Machine: all jobs niced, <= 2 processes at a time; background load from other users' jobs was 17-44.
