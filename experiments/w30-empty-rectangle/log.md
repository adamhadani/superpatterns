# W30 log — empty rectangles vs missing patterns

- 19:25 Read NOTES.md, W28 proof/results (Thm 1.1 witness reduction, Table 5 emptiness correlation), W24 dump format
  (dumps contain M + codes only, NO σ), W27 §0 block splitting. Decision: write own sampler `erect.c` (missing set via
  the W24 bitset/DFS algorithm; all maximal empty axis-parallel rectangles by O(n^4) scan with prefix sums; for the
  top-R rectangles Q count the missing patterns revived by a phantom point at the centre slot of Q; for Q_1 also
  the "any point of Q" variant via completion cells). Load average 8.6 on 12 cores; will use ≤3 processes.
- 19:45 erect.c verified against brute force (verify.py: k=4,5,6 small n, M / rectangles / Kc / Kany / Kunion all agree).
  FIRST LOOK (k=6, n=27, 6000 σ, before restart): K_any(Q_1)/M = 0.999 — the "some point of Q_1 revives π" variant
  is nearly vacuous: the revival region Rev(π) = {x : π ⊂ σ+x} is a union of completion cells of ALL copies of the
  k children of π and covers most of the board. Centre-phantom K_c(Q_1)/M = 0.73–0.77. Needed baseline: random-location
  phantom (expected ≈ (μ(n)−μ(n+1))/μ(n) ≈ 0.3). Added: random phantom, 3×3 grid of phantoms, per-pattern histogram of
  revival multiplicity. Restarted runs (k=6: n=27,28,24; k=7: n=37,35,33; k=8: n=48 200 σ). 3 cores.
- 19:50 k=6 n=27/28 (6000 σ each) done. Headline: K_any(Q₁)/M = 0.995 (vacuous), K_c(Q₁)/M = 0.74, K_rand/M = 0.41
  = 1 − μ(28)/μ(27) (Prop. 2.1, exact identity, checked). K_c/M independent of the rectangle's area and aspect ratio.
  The short side min(w,h) of Q₁ is the predictive statistic (Spearman 0.2; long side 0.08).
- 19:55 Proved: cells characterisation (Lemma 1.2), random-point identity (Prop. 2.1), strip-deletion bound
  E[M | Q empty] ≤ μ(n − min(w,h)) (Prop. 3.2) with the one-point lemma p_π(n−1) ≤ n p_π(n) (Lemma 3.3).
  Deterministic counterexample scale: sp(6) witness + 1 point revives 0.88·6! patterns (witness_phantom.py).
- 20:05 k=7 n=37 only 560 σ (machine load 11–12 from other users; my 3 processes got ≈ 1 core). k=8 n=48: 0 lines
  (≈ 1 min/σ). results.md written from k=6 (full) + k=7 (partial). Runs killed at the end of the session to free the
  machine; to extend, rerun the commands in README.md with new seeds (analyze.py pools all seeds).

## Dead ends (with reasons)
1. "Patterns killed by Q = patterns with a copy through some point of Q" (K_any): vacuous, 99.5–99.7 % of M, because the
   revival region of a missing pattern is the union of the completion cells of ALL copies of its k children
   (e^{Θ(k)} copies), which covers most of the board. Any definition of "killed by Q" must fix the point (K_x) or
   demand Q ⊆ Rev(π); neither isolates a defect-specific mechanism (K_c/M ≈ 0.75 for every large Q).
2. Prop. 4.1, K_x ≥ N_{k−1}(σ)/k − N_k(σ): never positive (N_k ≥ N_{k−1}/k always); the deterministic lower bound
   must count patterns whose every copy uses x, which we could only do numerically.
3. Exploiting BOTH strips (Miss(σ_V) ∩ Miss(σ_H)) to improve Prop. 3.2: the two sub-permutations share the
   n − w − h points outside the cross of Q, no independence; not pursued.
4. Union bound over rectangles + Prop. 3.2 to bound the contribution of big defects to R: the gain e^{−A/n} = n^{−O(1)}
   at A ≍ n ln n is dominated by the loss e^{s·min(w,h)} = e^{Θ(k√ln k)} (proof.md Rem. (ii)); cannot reach e^{O(k)}
   without the uniform-slope statement s(n) = O(1), which is exactly the missing per-point rate control of W27.
5. k=8 numerics: too slow at C(48,7) subsets per phantom under the load; a smarter revival test (DFS over copies of
   the k children with pruning against the missing bitset) would be ≈ 100× faster — not implemented in the time.
6. Corner defects (Q at a corner of the board, killing the (k−1)! patterns with π(1)=1): heuristically only
   e^{O(k)}·μ_{k−1}, since every point of the boundary strip has a NE quadrant containing all but ≤ 2n/k points
   (a Prop. 3.2-type argument); not written up as a theorem because the corner strip is not a rectangle-with-empty-interior.
- 20:10 Runs stopped (k=7 n=37: 700 σ; empty k=8 / k=6 n=24 / k=7 n=33,35 outputs deleted). analysis.txt regenerated;
  results.md §1 updated to the 700-sample k=7 numbers (changes ≤ 0.03). Deliverables complete: README.md, log.md,
  results.md, proof.md, erect.c, verify.py, analyze.py, witness_phantom.py, out/.
