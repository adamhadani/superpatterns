# W27 log — comparison principle

- 2026-08-29 18:00:28 start. Created dir.
- Read ledger, W21 results, W22 §B.2, W16 §4, paper §Random. Key reframing (see proof.md §0): Alon needs only a
  UNIFORM positive speed-N rate, Pr(π⊄Π_{Ck²}) ≤ e^{-ιk²} for all π (any ι>0), which CP(K) implies; block-splitting
  gives only speed N/k² (constant exponent), so the whole content of CP is the tail rate.
- Known exact fact to keep in mind: Av_7(1324)=2762 > Av_7(1234)=2761, so CP(1) is FALSE already at k=4, n=7 (=0.44k²);
  L(1324)≈11.6>9 so the ratio grows like (1.29)^n in the SW regime. Need CP(K>1) or a k→∞ formulation.
- Plan: (A) exact Av_n(π) by generating tree (insert new max, prune) for all π up to dihedral symmetry, n as far as
  feasible; (B) SMC "growth" estimator: Pr(π⊄σ_{n+1})/Pr(π⊄σ_n) = E_{σ~unif avoiders}[#safe insertion slots]/(n+1),
  population Monte Carlo with resampling -> deep tail (validate vs LIS hook-length counts); (C) direct sampling with
  contain_bc for k=7 (all 5040 on the same σ).
- avoid.c (own DFS) validated: Av_n(1324/1234/1342) = OEIS for n≤8; SMC vs exact LIS tail (hook-length, lis_exact.py):
  identity k=4 pop 20000 agrees to <1% in log down to 1e-6. avoid2.c uses the contain_bc solver core (bc_core.h) with a
  virtual-insertion dominance table; DFS dominates the cost for non-identity patterns (avoiders are adversarial inputs).
- SMC variance warning: k=7 pattern 4163725 at n=70: pop 500 gives ln p = -37.8, pop 2000 gives -35.5 (log-bias at
  small pop). Deep-tail values need pop ≥ 1e4 or several seeds; the all-class scans use small pop and n ≲ k².
- Launched: smc4/smc4b (pop 1e5, n≤24, seeds 1,2), smc5/smc5b (pop 2e4, n≤38), smc6 (pop 2000, n≤54), smc7 (pop 1000, n≤49).
- k=7 scan restarted with n≤45, pop 500 (time budget); k=6 pop 2000 n≤54 continues.
- Budget cut: k=5 pop 5000 n≤38 (single seed), k=6 pop 1000 n≤48 (first 12 classes have pop 2000, n≤54), k=7 pop 500 n≤45. smc4b (seed 2) has 3 classes only.
- THEORY: Theorem 2.1 (PROVED): coarse-grain into g×g cells; a ⊕-sum of h blocks of size ≤ b is contained whenever
  the good cells (cells that are b-superpatterns) contain a strict 2-D chain of length h; Mirsky ⇒ #good ≤ (h−1)(2g−1)
  otherwise; NA + Chernoff ⇒ p_π(N) ≤ e^{−ιN} for N ≥ mΛ²k². New speed-N class incl. (21)^{k/2} and all layered with
  bounded layers. Thm 2.5: same for grid patterns 𝒢(r,h) (rigid rows) — speed N but rate 1/(r² ln r): same r² loss as
  W23 (honest assessment in proof.md). First draft of 2.5 overclaimed k²/ln k exponent; corrected (waste factor r and
  r cells per element).
- Dead ends recorded: Greene/RSK does not characterise (21)^h containment (3412 vs 2143 same shape (2,2);
  (h+1..2h)(1..h) has shape (h,h) and avoids (21)^2); tight-gadget posets for (12)^h have huge antichains (whole
  strips) so Mirsky-cover counting explodes; the relabelling identity (Prop 2.4) is exact but the constrained family
  has density 1/k!, i.e. it restates the union-bound entropy.
- Queued deep/ targeted runs (after k=5 scan): k=6,7,8 identity vs 1⊕dec⊕1 vs layered (21)^h vs grids (12)^h,(1234)^2.
