# W38 bounded diagnostic — 10 September 2026

Every subset and canonical overlap is enumerated within each sampled host. Uncertainty is over hosts: paired 2000-resample bootstrap intervals preserve covariance. These are numerical confidence intervals, not rigorous probability bounds. The C column is the actual integer-host N/k²; rounding can merge requested grid points.

| k | N | C | hosts | EY | R (95% interval) | diagonal | D (95% interval) | containment |
|---|---|---|---|---|---|---|---|---|
| 6 | 7 | 0.1944 | 1000 | 0.00735 | 136.08 (134.40–137.83) | 136.08 | 0.00 (0.00–0.00) | 0.0073 |
| 6 | 9 | 0.2500 | 1000 | 0.05202 | 20.21 (19.78–20.65) | 19.22 | 0.98 (0.89–1.08) | 0.0507 |
| 6 | 10 | 0.2778 | 1000 | 0.09947 | 11.13 (10.89–11.38) | 10.05 | 1.07 (1.00–1.15) | 0.0944 |
| 6 | 14 | 0.3889 | 1000 | 0.53194 | 2.89 (2.84–2.94) | 1.88 | 1.01 (0.99–1.03) | 0.4123 |
| 8 | 14 | 0.2188 | 400 | 0.02126 | 52.27 (50.43–54.23) | 47.04 | 5.23 (4.79–5.75) | 0.0201 |
| 8 | 16 | 0.2500 | 400 | 0.06053 | 20.32 (19.53–21.14) | 16.52 | 3.79 (3.53–4.07) | 0.0543 |
| 8 | 17 | 0.2656 | 400 | 0.09637 | 13.63 (13.15–14.15) | 10.38 | 3.25 (3.09–3.43) | 0.0832 |
| 8 | 19 | 0.2969 | 400 | 0.20278 | 7.38 (7.14–7.64) | 4.93 | 2.45 (2.34–2.56) | 0.1618 |
| 8 | 25 | 0.3906 | 400 | 0.96931 | 2.59 (2.53–2.65) | 1.03 | 1.56 (1.52–1.59) | 0.5314 |
| 10 | 25 | 0.2500 | 64 | 0.07461 | 20.35 (18.91–22.01) | 13.40 | 6.94 (6.25–7.71) | 0.0595 |

Full overlap terms (including observed zeros) and the four fixed-target diagnostics are in `out/review-20260910/summary.json`. An observed zero is not an asymptotic zero; Overlap k−1 and geometrically impossible bins are exact zeros; other zero observations need uncertainty bounds. Fixed-target ratios with insufficient hits are reported without a bootstrap interval. Containment intervals use the Wilson formula, including zero-hit cases.

Reproduce: `python3 run_diagnostic.py`, then run `analyze_diagnostic.py` with NumPy. The runner preserves existing host files. `verify_diagnostic.py` checks the enumeration against an independently written Python implementation on small hosts.
