# W27 results — Pr(π ⊄ σ_n) across all patterns, deep tail, versus the identity

Method: SMC growth estimator (avoid2.c; ratio Pr(⊄ at n+1)/Pr(⊄ at n) = E_{σ ~ uniform π-avoider of length n}
[#safe insertion slots for a new maximum]/(n+1), population Monte Carlo with systematic resampling; the solver core is
W21's contain_bc). Validation: exact Av_n(π) for n ≤ 8 (OEIS values reproduced for 1234/1324/1342), exact LIS tails
(hook-length sums, lis_exact.py): identity k=4 pop 1e5 gives ln p = −13.914 at n = 24 vs exact −13.958; the three
non-identity members of the identity's Wilf class at k = 4 (1243, 1432, 2143) land within 0.04 of it at n = 24.
Noise ≈ ±0.04 in ln p at the deepest n for pop 1e5 (k=4), larger for the small-population scans (see per-k notes).
Numbers are ln p_π(n); "excess" = ln p_π(n) − ln p_id(n) (> 0 means π is HARDER to contain than the identity).

## k = 4 (all 7 dihedral classes, n = 1…24, pop 1e5, two seeds)

| n | n/k² | ln p_id | 1324 | 1243 | 1432 | 2143 | 1342 | 2413 |
|---|---|---|---|---|---|---|---|---|
| 8 | 0.50 | -0.936 | +0.001 | -0.002 | -0.003 | -0.005 | -0.021 | -0.022 |
| 10 | 0.62 | -1.818 | +0.005 | -0.004 | -0.003 | -0.011 | -0.059 | -0.061 |
| 12 | 0.75 | -2.953 | +0.017 | -0.010 | -0.005 | -0.019 | -0.118 | -0.121 |
| 14 | 0.88 | -4.315 | +0.035 | -0.018 | -0.010 | -0.027 | -0.192 | -0.202 |
| 16 | 1.00 | -5.886 | +0.066 | -0.026 | -0.014 | -0.029 | -0.283 | -0.294 |
| 18 | 1.12 | -7.647 | +0.110 | -0.032 | -0.015 | -0.030 | -0.386 | -0.402 |
| 20 | 1.25 | -9.582 | +0.160 | -0.032 | -0.021 | -0.033 | -0.504 | -0.521 |
| 22 | 1.38 | -11.673 | +0.218 | -0.031 | -0.028 | -0.039 | -0.630 | -0.648 |
| 24 | 1.50 | -13.914 | +0.289 | -0.025 | -0.038 | -0.044 | -0.764 | -0.781 |

Reading: at k = 4 exactly one class, 1324, is harder than the identity, from n ≈ 7 on (exact: Av_7(1324) = 2762 >
2761), with excess growing roughly linearly in n (slope ≈ 0.02/point at n = 24, far below the Stanley–Wilf
asymptote ln(11.60/9) = 0.254/point). 1243, 1432, 2143 are Wilf-equivalent to 1234 (excess = 0 exactly; the
observed ±0.04 is the SMC noise). 1342 and 2413 (Wilf class of growth 8) are much easier: excess −0.76 at n = 24.
