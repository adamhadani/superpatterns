# W32 — information outside the current gap: chronology and dead ends

Date 2026-08-29, start 20:20.  Goal: a rigorous threshold below 0.46·k² for a uniformly random π ∈ S_k by
using information outside the current gap, or a proof that sequential rules cannot get there.

## 1. First analysis (20:20–20:40): out-of-gap information is STALE before it can be used

W31 Thm 4.1 caps every in-gap rule at V_h/h² → 0.4623 in the fresh-window model.  Idea (1) of the brief is to
look at the half-strips of the OTHER gaps of the strip when placing v, because they are searched later by the
same rule.  Key question: is what we see now still to the right of the clock when that gap is next visited?

Scaled units (x' = kx, y' = ky; intensity C; the copy must fit in x' < k).  At time t of a strip of height h
(t points placed), the gaps have height ≈ h/t and hold ≈ (h−t)/t values each; the whole construction advances
the clock by ≈ 1 per step on average (k steps in x' ∈ [0,k]).  A gap holding n_i unplaced values out of the
k' remaining ones is next visited after ≈ k'/n_i steps; with n_i ≈ k'/(mt) this is ≈ m·t steps, i.e. a clock
advance ≈ m·t·(typical step) — while the search in the gap sees points at x'-distance ≈ t/(Ch) (the leftmost
point of a gap of height h/t).  Ratio: (t/(Ch)) / (m t) = 1/(Chm) = 1/(Ck) → 0 for EVERY h, m with hm = k.
So, for k → ∞, the points visible in the other gaps at the time of a step are to the LEFT of the clock when
those gaps are next visited, unless the rule looks ahead by x'-distance L that is comparable with the
revisit advance.  With lookahead L, the informed steps are those with revisit advance < L: at time t the
advance is ≈ t²/(Ck)·(m/m)… (single strip h = k: revisit after t steps of ≈ t/(Ck) each = t²/(Ck)), so the
informed steps are t ≲ √(CkL), whose total cost is Σ_{t ≤ √(CkL)} t/(Ck) ≈ L/2 out of ≈ k/(2C): a fraction
≈ CL/k.  Conclusion (heuristic, to be tested numerically): out-of-gap information is worth O(L/k) of the
cost; only lookahead L = Θ(k) — i.e. seeing a constant fraction of the whole square — can beat the in-gap cap.

Same for idea (2) (windows crossing strip boundaries): the gap of v becomes the gap between the nearest placed
values overall (h = k, one strip) — still an in-gap rule, still capped by V_k/k² → 0.4623.  Idea (3)
(processing order): with a single monotone clock the only realisable orders are position order and (by
symmetry) value order; a two-sided scan (clocks from both ends) still places every value inside its gap with
a fresh window, and the strip's Bellman recursion is unchanged (the arrival order of the values of a gap is
still uniform).  So all three constructive ideas reduce to the in-gap Bellman problem in the mean-field
limit.  Decision: (a) prove the extension of W31 Thm 4.1 to rules using the whole fresh strip and all strips
(proof.md §1–2); (b) make the staleness rigorous where possible (safe-clock rules exactly, general rules under
the mean-field hypothesis); (c) test numerically with a single strip h = k (no artificial partition at all),
exact excision instead of the safe clock, and measure the "informable" cost share as a function of L/k.

## 2. Numerics plan (20:40)

single_strip.py: one strip of height h = k, the W31 rule with potentials V_n (dp_V.txt of W31, ε = 0 Bellman
values), search from the true clock a (no safe clock — rigorous because the explored sublevel sets contain no
unused points, see proof.md §1); record per step the clock advance since the gap was created and the
step cost, to compute the cost share of steps whose gap was created less than L clock-units ago.

## 3. Results as they came in (20:25–20:45)

- single_strip.py, k = 256..2000, single strip: implied constant 0.456–0.476, i.e. the mean-field V_k/k² within
  noise (results.md §1); m = 1..16 strips at k = 1024: all within ± 0.01 of V_h/h² (§2).  The partition and the
  safe clock are irrelevant; the rigorous version of "search from the true clock" is [W19] Lemma 1.2 with the
  explored sublevel sets excised (they contain no unused points), see proof.md §1.
- Staleness measured (§3 of results.md): the cost share informable by lookahead L is a function of L/k only
  (≈ 1.2 (L/k)^{0.7}), much larger than my first estimate CL/k (log §1) because gaps holding many values are
  revisited quickly, but still → 0 for L = o(k).  Conclusion unchanged.
- THE THEOREM (proof.md Thm 2.1): while formalising the staleness argument I realised it is not needed: the
  Bellman lower bound of W31 Thm 4.1 only uses that the chosen point is a point of a conditionally Poisson process
  on a subset of the gap's half-strip — the hypothesis of the fresh-search lemma itself.  Information outside
  A_p enters the conditioning but not the bound, because the cost-to-go Ψ = Σ V_{n_i}/(CG_i) is a deterministic
  function of the gaps.  So every rule proved by the programme's own tool is capped at V_k/(Ck).  Non-anticipation
  in π is the one hypothesis beyond (F); Thm 2.2 shows it costs 4·10^{−5} (bst.py).
- Two-sided scan (twosided.py) — the only realisable non-position order with one clock per end.  First runs at
  k = 256 suggested a gain of 0.02; at k = 512/1024 with matched seeds the gain is within noise (0.464 vs 0.461),
  and the rule fails at C = 0.45.  zdiag.py explains why: the candidate not taken persists with an upward-biased
  score change (E Z ≈ +0.9), so "min of two mean-zero draws" does not apply; my first write-up claimed
  "two-sided is never worse" by that argument — WRONG, corrected to Obs. 3.1 (only the two-sided *optimum* is
  trivially ≤ one-sided).
- Lanes (lanes.py; r blocks of positions with fixed x-budgets k/r, 2r candidates): r = 2, 4 no gain; r ≥ 8
  fails (a block's consumption exceeds its budget).  Dead end.
- Anticipating cap (bst.py): V(σ) depends on σ only through its binary search tree; exact over all Catalan(n)
  shapes for n ≤ 11: V^{ant}_n/V_n = 0.99996; quantised to n = 60: 0.99994.  Knowing the future order is worthless
  because W(A,B) is almost linear over the spread of V(T).

## 4. Dead ends (with reasons)

1. Joint choice using the other gaps' half-strips (brief idea 1): worthless — Thm 2.1; quantitatively, what is
   seen is stale by the next visit unless lookahead is Θ(k) (results.md §3).
2. Windows crossing strip boundaries / no partition (idea 2): covered by Thm 2.1 (gap = overall gap); the gain
   over W31's h = 512 is at most V_512/512² − lim = 0.0026 and is not visible numerically.
3. Processing orders (idea 3): with a single monotone clock only position order (or value order by symmetry)
   is realisable; two clocks (both ends) give the two-sided rule — no gain; r lanes — fail for r ≥ 8.  Orders that
   place a position between two placed neighbours need a point in a bounded rectangle (no "leftmost" cost
   structure; that is the CSP, not a sequential rule).
4. Rigorous failure-whp in Thm 2.1(b) for arbitrary rules: the Bellman inequality makes a_p + Ψ_p a submartingale
   but gives no lower-tail control (Ψ can drop by V_n/(CG) at one step for tiny gaps); stated under a weak-law
   hypothesis, as [W29] Thm 4.1.
5. Rigorous constant for the two-sided rule: would need a concentration argument for coupled strips; skipped
   because the gain is nil.

Total time ≈ 35 min of the 2 h budget; stopped because the question is settled negatively (all three
constructive ideas are inside the class capped by Thm 2.1, and the class boundary — re-using seen points, or
several candidate copies — is where the numerics show no gain either).
