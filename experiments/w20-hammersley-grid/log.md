# W20 — exact constant for tilted grids: log

Date 2026-08-29.  Work dir experiments/w20-hammersley-grid/.  Proofs in proof.md.  Machine heavily loaded by
other jobs (load 30–110 on 12 cores during this session); all runs here are single-threaded, ≤ 4 at a time.

## 1. Orientation (what was read, what the question really is)

* W11 proof.md §4: corner greedy (triangle rule) gives threshold π/8 ≈ 0.393 for all block-grid patterns,
  free slabs / rigid strips (Theorem 4.4).  W11 log §6: exact FIXED thresholds 0.55 … 0.36 for r = h ≤ 7,
  decreasing; FREE thresholds track the identity.  W17 §5: one-block renewal rules cap at 0.8 of the truth.
* Three models: CELL ⊂ FIXED ⊂ FREE (proof.md §0).  The conjecture "threshold (1/4 + o(1))k²" is about FREE.
  FIXED is only a proof device — and it is a lossy one: at h = 1 the FIXED constant is 1 (the colour word
  0 1 ⋯ r−1 must appear in an i.i.d. r-ary word: k² letters), while the FREE constant is 1/4 (identity).
* Key reformulation (proof.md Prop 1.1): FIXED containment = an x-increasing sequence of k points in a Poisson
  process with i.i.d. uniform colours, colours cycling 0,1,…,r−1, each colour class a chain.  For r = 1 this is
  the LIS; for h = 1 it is subsequence containment of a word.

## 2. Chronology

1. 14:30 Read W11/W17/notes.  Copied tg.c (exact Pareto-front DP, validated in W11) and wrote bisect.py
   (C_{1/2} = N_{1/2}/k² by 11-step bisection, 400 samples per step; ±0.01 typical).
2. 14:40 Launched exact-DP scans: FIXED r = 2,3,4 with h up to 256/64/32 (runA.sh); FIXED small h with r up to 64
   (runC.sh); FREE r = 2 with h ≤ 32 (runD.sh); FIXED 8×8 (run88.sh, 30 s/sample at load 60).
3. 14:45–15:10 Theory: the barrier proposition (proof.md §3: every fresh-quadrant strategy needs C ≥ π/8,
   E[u+v] ≥ 2√(π/(8C))), and the mean-field regime (h fixed, r → ∞).  Realised that the clock advances by Θ(r)
   between visits of a strip while a visit explores O(1), so per-strip rules with *any* potential are rigorously
   analysable via an "artificial fill" coupling (Theorem 4.2).  Wrote the Bellman recursion (Prop 4.3) and
   mf.py to evaluate C_mf(h).
4. 15:00 Added option -iid to tg.c (i.i.d. colours instead of the balanced colouring induced by N uniform points
   with rigid strips, which has a hypergeometric finite-size effect: at h = 1, r = 32 the balanced model gives
   0.950 and the i.i.d. one 0.985, both → 1).  Launched iid scans at h = 1, 2, 3 (runE.sh).
5. mf.py bugs fixed (nan from the infinite top cell; one round too many).  Checks: V_1(0) = 1/(Ch) exactly
   (h = 1 → C_mf = 1); h = 2 at n = 200/400/800: 0.7519/0.7509/0.7505 (discretisation error ≈ +0.003 at n = 400).

## 3. Numerics

### 3.1 Mean-field constants C_mf(h) (proof.md Prop 4.3; NUMERICAL, mf.py, n = 400 cells; π/8 = 0.3927)

    h        1      2      3      4      5      6      7      8      10     12     14     16
    n=400    1.000  0.751  0.656  0.605  0.572  0.549  0.532  0.519  0.501  0.488  0.479  0.472
    n=800    1.000  0.7505 0.655  0.603  0.570  0.547  0.530  0.517
    (C_mf − π/8)·h^{2/3} = 0.57, 0.55, 0.53, 0.52, 0.515, 0.51, 0.505 (h = 2 … 8), 0.505 (h = 16):
    consistent with C_mf(h) = π/8 + (0.50 ± 0.01)·h^{−2/3} — a k^{−2/3}-type (Tracy–Widom-like) finite-h
    correction to the mean-field constant (NUMERICAL).  Discretisation error ≈ +0.002 at n = 400.

### 3.2 Exact DP thresholds C_{1/2} = N_{1/2}/k² (NUMERICAL; results.txt has the bisection traces)

FIXED (balanced colouring = rigid strips in N uniform points, tg.c default):
    h = 1:  r = 2: 0.592   4: 0.776   8: 0.860   16: 0.904   32: 0.950            → 1 (Theorem 2.2)
    h = 2:  r = 2: 0.577   4: 0.594   8: 0.610   16: 0.600   (32, 64 pending)     mean-field prediction 0.751
    r = 2:  h = 1: 0.592   2: 0.577   8: 0.379   16: 0.322   32: 0.287   64: 0.268   (128, 256 pending)
FIXED with i.i.d. colours (-iid):
    h = 1:  r = 4: 0.938   8: 0.973   16: 0.976   32: 0.985                        → 1
    h = 2:  pending
FREE, r = 2 (the pattern (12)^h = 1 (h+1) 2 (h+2) ⋯):
    h = 4: 0.391   8: 0.335   16: 0.293   24: 0.278   (32 pending)
    identity of the same k (W11 lisref): k=8: 0.404, 16: 0.350, 32: 0.311, 49: 0.298, 64: 0.291.
    So (12)^h is easier than the identity of the same length at every k tested, by 0.01–0.02.
FIXED 8×8 (diagonal, k = 64): pending (diag88.txt).

### 3.3 Reading

* h = 1 confirms Theorem 2.2 and shows the convergence in r is O(r^{−1/2}) and from below.
* h = 2 (FIXED, balanced colouring): 0.58–0.61 for r ≤ 16, vs C_mf(2) = 0.751.  Either the convergence is slow
  (as at h = 1, where r = 16 is 10 % below the limit and the relative correction is O(k^{−1/2}) with a large
  constant), or the optimal non-causal embedding genuinely beats the mean-field rules (Conjecture 4.6 false).
  The i.i.d.-colour runs at r = 32, 64 (and the balanced ones) will discriminate: if C_{1/2}(r,2) keeps rising
  towards 0.75 the conjecture stands.  [To be updated when runE finishes.]
* r = 2, h → ∞ (FIXED): 0.268 at k = 128, still falling; a fit C(k) = C_∞ + b k^{−2/3} through k = 32, 64, 128
  gives C_∞ ≈ 0.25 ± 0.01.  So plausibly lim_h C^{fix}(2,h) = 1/4, i.e. rigid strips cost nothing when there
  are only two of them and they are long.  Contrast with lim_r C^{fix}(r,2) ≥ 1/2 (Prop 2.3).
* FREE r = 2: 0.278 at k = 48, below the identity's finite-size value; consistent with a limit ≤ 1/4.

## 4. Dead ends (with reasons)

1. *Subadditivity in x for the FIXED model at fixed r.*  Concatenating x-intervals is superadditive, but the
   limit is trivial: with r fixed and x-length L → ∞ the strips are thin, and a chain of length h in a strip
   of height 1/r needs N/r ≥ h²/4, so H(L)/L → 0 (the number of periods is sublinear in the number of points
   ×length).  The right scaling has r and h growing together; no one-parameter subadditive family was found
   (stacking in y changes the merge word to a shuffle of two periodic words, not a periodic word).
2. *Lookahead within the current quadrant* (explore the m nearest points, choose the best): useless — the
   choice cannot reduce E[u+v] below E[min φ] (Prop 3.1).  Any gain must come from information outside the
   current quadrant.
3. *Planning for the next visit.*  In the mean-field regime the clock position at the next visit is uncertain by
   Θ(√r) (sum of r−1 O(1) increments) while a point is O(1) in size, so a strip cannot pre-select a point for
   its next visit; a rule that makes the clock deterministic (rigid cells) has constant 1.  This is the
   heuristic behind Conjecture 4.6 and also why we could not design a *rigorous* rule below π/8 in the
   diagonal regime: such a rule needs Θ(1)-precision control of the clock, i.e. coordination among the strips,
   which destroys the i.i.d./Markov structure that the renewal proofs need.
4. *Two-strip (12)^h construction "A = corner-greedy chain in strip 1, B = cell-greedy in the gaps of A".*
   B's y-increment in a gap of width w is Exp(Cw) with mean 1/(Cw), and the gap law has positive density at 0,
   so E[1/w] = ∞; skipping small gaps costs A extra points.  Rough optimisation gives B a y-cost per point
   ≈ 1/(2C) ≥ 1 unless C ≥ 1/2: worse than π/8.  Not pursued.
5. *Exact solvability of the 2-strip system.*  The DP state for r = 2 is a 2-dimensional Pareto front (a
   staircase), not a single level; no Hammersley-type particle description with a known hydrodynamic limit was
   found.  Numerically the r = 2 FIXED constant appears to be 1/4 (§3.3), which, if true, would say that the
   two-strip system has the *same* constant as the LIS — a statement that should have a comparison proof
   (embed a copy of (12)^h near a maximal chain?), but the joint law of gaps along the maximal chain is not
   available (cf. W17 §5).
