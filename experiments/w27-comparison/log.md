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
