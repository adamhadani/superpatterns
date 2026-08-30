# W37 log (chronological; includes dead ends)

2026-08-30
- Read W27 (proof.md/results.md, coordinator's verification note: SMC excesses biased at k≥5 deep n; exact
  facts only). Decision: all numerics here EXACT (no SMC), via a new all-patterns-at-once counter.
- allpat.c written: DFS over prefixes of σ; for each j ≤ 7 maintains all j-subsets as (value-bitmask, Lehmer
  index) with O(1) extension via precomputed table; first-occurrence stamping counts each containing σ once
  with multiplicity (#completions); Klein 4-group fundamental domain on (σ(1), σ(n)) gives a 4× saving.
  Validated: n=8 full enumeration reproduces Av_8(1234)=15767, Av_8(1324)=15793, Av_8(1342)=15485, Catalan
  for k=3. n=9,10 symmetric reconstruction reproduces OEIS k=4 values and the W27 coordinator's brute-force
  values Av_9(12345)=261808, Av_9(14325)=261863, Av_10(123456)=3291590, 132546=3291715, 154326=3291662,
  143256=3291666. (My initial "expected" Av_9(12345)=206098 was a WRONG memory of OEIS A047889 — computed
  value matches the coordinator's independent av9.c; recorded to avoid re-confusion.)
- Timings (12 cores): n=10: 0.4s; n=11: 5s; n=12: 81s; n=13: launched in background (~25 min est).
- proof.md: Lemma 1 (strip-rearrangement reformulation, both directions, cut-at-point care via midpoint cuts),
  Lemma 2 (fixed-cut law π-independent, exact Exp-gap formula, greedy optimality by exchange), Lemma 3
  (de-Poissonization), Lemma 4 (defect cost, elementary, no Stanley–Wilf needed), Lemma 5 (p_{id_a}(M) ≤
  e^{−M+2(a−1)√M} via RSK column words — simpler and for our purposes stronger than the W23 certificate),
  Theorem 6/Corollary 7 (corner-defect comparison; covers 1⊕dec_{k−2}⊕1, the empirically hardest pattern),
  Theorem 8 (defect-sum box bound), Theorem 9 (Alon window (1/4+δ)k² restricted to ⊕/⊖-sums of long monotone
  runs + sparse small defects; conditional on DZ lower tail; unconditional variant at (16+δ)k² via Lemma 5).

Dead ends / negative findings (details in proof.md §5):
- FKG/Harris on {E_c}: gives lower bounds on p_π (wrong direction). No Slepian analogue for indicator families
  with exchangeable marginals; "less correlated ⇒ larger sup" is not a theorem and must saturate to equality at
  k=3 and at every BWX pair, which kills naive strict-monotonicity couplings.
- Pathwise bubble-step merging (swap two adjacent strips, show sup over cuts can only drop): FALSE pointwise —
  1324→1234 is a bubble step with the strict reverse inequality for all n ≥ 7 (exact). Only the windowed rate
  version can hold.
- Middle defects (id_a ⊕ τ ⊕ id_b, a ≍ b ≍ k/2): thinning+chain-window argument fails because a usable window
  rectangle must have area Ω(1) for a speed-k² certificate (window-area problem) ⇒ Θ(k) skipped chain points ⇒
  constant-factor N loss. Box splitting gives min(a,b)²/k² rate loss — enough for ω(k ln k) at (1/4+δ)k² when
  min(a,b) ≫ √(k ln k) (this became Theorem 9's run-length condition), not enough for the clean rate form.
- Early plan to use per-pattern DFS (W27 avoid.c) for the all-pattern tables scrapped: the all-at-once counter
  is far cheaper for k = 6, 7, where almost every σ_n (n ≤ 13) avoids any given pattern so the generating-tree
  prune saves nothing; avoid.c retained only for k = 4/5 extensions to n = 14+.
