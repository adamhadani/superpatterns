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
