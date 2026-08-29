# W24 — how loose is the union bound for random superpatterns?  (numerics, k = 5..9)

Date: 2026-08-29.  Question: W22 review §A item 2.  Tools/rerun: README.md.  Chronology: log.md.  Raw dumps: out/.

## 0. Setup and notation

σ_n uniform in S_n; M = #{π ∈ S_k : π ⊄ σ_n}; A_π = {π ⊄ σ_n}.  Then

    Pr(M > 0) = E[M] / E[M | M > 0],      R(n,k) := E[M | M > 0] = E[M] / Pr(M > 0) ≥ 1,

and ln R is exactly the additive error (in the exponent) of the union bound Pr(∃π ⊄ σ_n) ≤ Σ_π Pr(A_π) = E[M].
All A_π are decreasing events in the point set, so (Harris) the A_π are pairwise positively correlated and R ≥ 1.
Two readings of the same number: (i) R is the mean number of missing patterns of a random *non*-superpattern;
(ii) k!/R is the "effective number of independent absence events".

Estimators (analyze.py): R̂ = mean of M over the samples with M > 0; ln R̂ with a bootstrap SE (200 resamples).
Because M | M > 0 is heavy-tailed (see the histograms) R̂ is dominated by rare σ with huge M when Pr(M>0) is small;
the tables therefore also give the median, q10/q90/q99, the geometric mean of M | M>0, and "R w/o max" (R̂ with the
single largest sample removed).  t(k) = the n at which Pr(M>0) = 1/2 (interpolated), so R(t(k),k) = 2·E[M] there.

Sampler: mslack.c = the w5-random checker (exact set of contained k-patterns of each σ, bitset over k! codes, pruned
DFS), verified against a naive Python enumeration of all C(n,k) subsets on the *sets* of missing patterns (0 mismatches
on 43 permutations, k = 5,6,7).  Pattern codes are the w5 mixed-radix codes (patlib.py decodes them).
Samples per point: k=5: 20000–40000; k=6: 4000–30000; k=7: 3000–20000; k=8: 2000–10000; k=9: 300–3000 (1.5–2.5 s/σ).

## 1. Verdict (short)

1. **At the threshold n = t(k) the union bound is loose by a factor R = e^{Θ(k)} with a small constant, not
   e^{k ln k − O(k)}.**  Measured ln R(t(k), k) = 1.34, 1.93, 2.59, 3.26, 3.87 for k = 5,…,9.  Best fits over k = 5..9:

       ln R = 0.640·k − 1.88            (rms residual 0.018)
       ln R = 0.319·ln k! − 0.16        (rms 0.036)      ln R / ln k! = 0.28, 0.29, 0.30, 0.31, 0.30  (flat)
       ln R = 0.218·k ln k − 0.40       (rms 0.027)
       ln R = 3.35·√k − 6.2             (rms 0.048; and the increment per unit √k keeps *growing*: 2.8, 3.4, 3.7, 3.6)

   Five points over k = 5..9 cannot separate Θ(k) from Θ(k ln k) (the per-step increments Δ ln R = 0.60, 0.66, 0.67,
   0.61 are flat, which favours linear in k), but they exclude O(√k) with the observed constants and they exclude
   ln R = k ln k − O(k): the fraction of ln k! that the aggregation "gives back" is a flat ≈ 0.30, not → 1.
   Equivalently: **the effective number of independent absence events at the threshold is k!/R ≈ (k!)^{0.70}**;
   the per-pattern failure exponent that a union-bound proof must supply is ≈ 0.7·ln k! ≈ 0.7·k ln k, so a per-pattern
   speed of order k ln k is *not* removed by correlation — only its constant improves (by ≈ 30% in this range).

2. **The slack shrinks rapidly above the threshold.**  At fixed n = k² (Pr(M>0) ≈ 10⁻² … 10⁻³), ln R = 0.41, 0.42,
   0.48, 0.23 for k = 5..8 — essentially constant and ≤ 0.5; at fixed Pr(M>0) = 0.1: ln R = 0.67, 1.11, 1.41, 1.66,
   (2.8 for k=9, noisy, tail-dominated); at Pr(M>0) = 0.02: 0.37, 0.61, 0.97, 1.37, (2.2).  In the tail the growth
   per unit k is ≈ 0.25–0.45 (vs 0.64 at t(k)), i.e. deeper in the tail a random non-superpattern misses fewer
   patterns and the union bound is *closer* to tight.  Since the conjecture concerns the regime Pr(M>0) → 0, this is
   the relevant regime, and there the union bound loses at most e^{≈0.4k}.

3. **Mechanism.**  A failing σ misses a few *clusters* of patterns that are connected by adjacent transpositions
   (positions or values).  At t(k) the missing set has on average 1.6, 2.1, 3.4, 5.4, 9.6 components (k=5..9) and
   the largest component holds 83%, 77%, 68%, 62%, 55% of M.  Correspondingly the pairwise ratio
   ρ(π,π') = Pr(A_π∧A_π')/(Pr A_π Pr A_π') at t(k) is
   - adjacent transposition: 14, 58, 159, 601, 1095  (ln ρ ≈ 1.1k − 2.8),
   - dihedral image (reverse/complement/inverse…): 3.8, 9.2, 20, 47, 115  (ln ρ ≈ 0.85k − 2.9),
   - uniformly random pair: 4.1, 8.2, 12, 24, 29 ≈ E[M²]/E[M]²  (ln ρ ≈ 0.5k − 1).
   Pairwise correlations grow exponentially in k, much faster than R itself: R is *not* driven by the pairwise
   terms of a Bonferroni/Janson expansion (Δ/μ ≫ 1 here), but by the small number of clusters a typical failure has.
   Note the exception: π and its reverse (or complement) have ρ = 0 exactly once n ≥ (k−1)²+1 (Erdős–Szekeres: σ_n
   contains 12…k or k…1), e.g. id vs k…1: 0 co-misses in 40000 (k=5, n=19; independence would predict 15.6).
   So in the fixed-n model the A_π are NOT all pairwise positively correlated (Harris applies to the Poissonized
   point process, not to uniform σ_n); R ≥ 1 of course still holds.

4. **Which patterns are missing.**  Only mildly structured.  At t(k) the miss-weighted mean of LIS, LDS, #runs is
   within 1–3% of the S_k average; max(LIS,LDS) is shifted up by ≈ 0.05–0.27; the clearest signal is decomposability:
   ⊕- or ⊖-decomposable patterns are over-represented by ≈ 1.3–1.5× and (⊕,⊖)-indecomposable ones under-represented
   (k=9, n=60: 0.26 of misses vs 0.51 of S_9; k=8, n=48: 0.31 vs 0.44).  The most-missed individual patterns are the
   W5 §1.5 "monotone with small stairs" layered patterns (12354678, 21435876, 14325768, 85673412, …; identity
   ≈ 3× average at k=8), but they carry a small share of the total: at k=9, n=60, 362880 distinct patterns
   appear among the misses and the top-12 together are < 2% of them.  Deeper in the tail the missing set becomes
   more structured (k=8, n=55: indecomposable 0.17 vs 0.44; monotone-runs=2 patterns 6× enriched).

## 2. Distribution of M — headline numbers

(Full tables with quantiles, histograms of ln M, bootstrap SEs: §A.)  At n = t(k):

| k | t(k) | Pr(M>0) at nearest n | E[M] | R = E[M∣M>0] | ln R | median M∣M>0 | q90 | q99 | geometric mean M∣M>0 | E[M²]/E[M]² |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 19.1 | .511 (n=19) | 1.97 | 3.86 | 1.35 | 2 | 9 | 22 | 2.5 | 4.5 |
| 6 | 27.3 | .545 (n=27) | 4.11 | 7.55 | 2.02 | 3 | 19 | 63 | 3.7 | 6.9 |
| 7 | 36.8 | .482 (n=37) | 6.13 | 12.7 | 2.54 | 4 | 29 | 143 | 4.6 | 12.7 |
| 8 | 47.5 | .450 (n=48) | 10.2 | 22.6 | 3.12 | 5 | 49 | 308 | 5.8 | 24 |
| 9 | 59.1 | .423 (n=60) | 16.2 | 38.3 | 3.65 | 6 | 88 | 563 | 7.5 | 28 |

M | M>0 is heavy-tailed: the median is 2–6 while the mean is 4–38, the q99 is ≈ 15× the mean, and the histogram of
ln M is roughly geometric (each ln-unit bin holds ≈ 0.4–0.6× the previous one).  So R is a *mean* driven by the
upper tail: the *typical* non-superpattern misses only a handful of patterns (geometric mean 2.5 → 7.5), and
ln(geometric mean) grows only ≈ 0.27 per unit k.  Whichever statistic one prefers, none grows like k ln k.

Dependence on n at fixed k (k = 8): ln R = 6.6, 5.5, 4.3, 3.7, 3.1, 2.6, 2.0, 1.2, 1.4, 0.45, 0 at
n = 38, 41, 44, 46, 48, 50, 52, 55, 58, 62, 66 (Pr(M>0) from .9995 down to 2.5·10⁻⁴).  Roughly ln R falls by ≈ 0.25
per unit n, i.e. R ≈ exp(−(n − n₀)/4) near the threshold, until R ≈ 1 at n ≈ k² where the (rare) failures miss
a single pattern (or a single small cluster).

Interpolated ln R at fixed n/k² (§B): at 0.65k²: 2.2, 3.2, 4.3, 5.3, 6.4 (Δ ≈ 1.0 per k — but this is *below*
threshold, Pr(M>0) ≈ 0.9, where E[M] itself is what is large); at 0.75k² (≈ threshold): 1.4, 2.0, 2.6, 3.1, 3.4;
at 0.85k²: 0.9, 1.2, 1.5, 1.4, 2.4; at 1.0k²: 0.41, 0.42, 0.48, 0.23, —.  Fixed n/k² mixes regimes because
t(k)/k² drifts (0.76 → 0.73); the fixed-Pr(M>0) comparison in the verdict is the meaningful one.

## 3. Caveats

- Small k (5–9): all "growth laws" are 5-point fits over a factor 1.8 in k.  Θ(k) vs Θ(k ln k) is not separable;
  what is robust is (i) exponential-in-k growth of R at threshold with rate ≈ 0.6–0.65, (ii) ln R/ln k! flat at
  0.3, (iii) fast decay of R with n above threshold.
- Tail estimates: for Pr(M>0) ≲ 0.03 the number of failure events is 40–250 (k ≤ 8) and 11–53 (k = 9), and E[M]
  is then dominated by one or two σ with large M (k=9, n=68: one σ with M = 539 among 53 events doubles R; see the
  "R w/o max" column).  k = 9 tail values carry ±0.4–0.7 in ln R.
- k = 9 has 300–3000 samples per point (1.5–2.5 s per σ on the loaded machine); k = 9 threshold points pool 2–3 seeds.
- Fixed-n uniform σ_n, not the Poissonized point process; the difference is O(1/√n) in the location of the
  threshold and affects R only through the Erdős–Szekeres-type exact exclusions noted above.
- Pairwise ratios for specific pairs (identity and its neighbours) rest on 5–30 co-miss events; the pooled
  ρ over all pairs of a type (the numbers quoted) rest on 10³–10⁵ co-misses.
- The clusters were defined by adjacent transpositions of positions *or* values; other "one-step" moves (e.g.
  moving one entry) would merge clusters further and lower the component counts.

## 4. Consequence for the aggregation problem

Writing p̄(n) for the mean per-pattern absence probability, Pr(σ_n not a k-superpattern) = k!·p̄(n)/R(n,k).
At the threshold, R ≈ (k!)^{0.3}, so t(k) is the n at which p̄(n) ≈ (k!)^{−0.7}: a proof by summing per-pattern
bounds must still show absence probabilities of order exp(−0.7·k ln k), and the reward for a proof that captures the
correlation exactly is a constant factor ≈ 0.7 in the exponent, i.e. a constant factor in n if the per-pattern
exponent is linear in n/k (single-thread type bounds, exponent ∝ n/k, need n ≈ 0.7·k² ln k instead of k² ln k).
Above the threshold (the regime of the conjecture) R → e^{O(0.4k)} ≪ k!, so in that regime the union bound is
essentially tight to within e^{O(k)} — consistent with W22's "R = e^{O(√k)} ⇒ speed k ln k unavoidable" reading
up to replacing √k by a small multiple of k, which does not change the conclusion.  The data give no support to the
scenario "ln R ≈ k ln k − O(k)".



## A. Task 1 — full tables

### Task 1: distribution of M = #missing k-patterns (pooled over seeds)
Columns: samples; Pr(M>0) (#events); E[M]; R=E[M|M>0]; ln R (± bootstrap SE); median, q10, q90, q99 of M|M>0; max M; geometric mean of M|M>0; E[M²]/E[M]².

#### k = 5  (k! = 120, k² = 25)
| n | n/k² | samples | Pr(M>0) | #M>0 | E[M] | R | ln R | med | q10 | q90 | q99 | max | R w/o max | geo | E[M²]/E[M]² |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | 0.60 | 20000 | 0.9832 | 19664 | 14.7 | 14.95 | 2.705±0.006 | 12 | 3 | 31 | 53 | 94 | 14.9 | 10.6 | 1.65 |
| 16 | 0.64 | 20000 | 0.9280 | 18560 | 9.415 | 10.15 | 2.317±0.007 | 7 | 2 | 23 | 44 | 73 | 10.1 | 6.64 | 1.98 |
| 17 | 0.68 | 20000 | 0.8256 | 16511 | 5.82 | 7.05 | 1.953±0.008 | 5 | 1 | 16 | 35 | 87 | 7.05 | 4.42 | 2.51 |
| 18 | 0.72 | 20000 | 0.6704 | 13409 | 3.395 | 5.063 | 1.622±0.010 | 3 | 1 | 12 | 26 | 52 | 5.06 | 3.23 | 3.25 |
| 19 | 0.76 | 40000 | 0.5105 | 20421 | 1.972 | 3.863 | 1.352±0.008 | 2 | 1 | 9 | 22 | 52 | 3.86 | 2.53 | 4.45 |
| 20 | 0.80 | 40000 | 0.3517 | 14067 | 1.063 | 3.023 | 1.106±0.010 | 2 | 1 | 7 | 18 | 47 | 3.02 | 2.08 | 6.49 |
| 21 | 0.84 | 40000 | 0.2281 | 9122 | 0.5672 | 2.487 | 0.911±0.012 | 1 | 1 | 5 | 14 | 37 | 2.48 | 1.8 | 9.57 |
| 22 | 0.88 | 40000 | 0.1368 | 5473 | 0.2997 | 2.191 | 0.784±0.015 | 1 | 1 | 5 | 12 | 28 | 2.19 | 1.64 | 15.6 |
| 24 | 0.96 | 40000 | 0.0438 | 1752 | 0.0725 | 1.655 | 0.504±0.020 | 1 | 1 | 3 | 7 | 13 | 1.65 | 1.38 | 38.7 |
| 26 | 1.04 | 40000 | 0.0109 | 435 | 0.01503 | 1.382 | 0.323±0.037 | 1 | 1 | 2 | 7 | 10 | 1.36 | 1.22 | 144 |
| 28 | 1.12 | 40000 | 0.0025 | 99 | 0.0029 | 1.172 | 0.158±0.040 | 1 | 1 | 2 | 3 | 3 | 1.15 | 1.11 | 470 |
| 32 | 1.28 | 40000 | 0.0001 | 2 | 5e-05 | 1 | 0.000±0.000 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2e+04 |

#### k = 6  (k! = 720, k² = 36)
| n | n/k² | samples | Pr(M>0) | #M>0 | E[M] | R | ln R | med | q10 | q90 | q99 | max | R w/o max | geo | E[M²]/E[M]² |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 22 | 0.61 | 4000 | 0.9890 | 3956 | 43.31 | 43.8 | 3.780±0.015 | 30 | 6 | 100 | 202 | 343 | 43.7 | 26.7 | 2.01 |
| 24 | 0.67 | 4000 | 0.8955 | 3582 | 17.85 | 19.93 | 2.992±0.020 | 11 | 2 | 51 | 122 | 284 | 19.9 | 9.8 | 2.95 |
| 26 | 0.72 | 4000 | 0.6800 | 2720 | 7.033 | 10.34 | 2.336±0.026 | 5 | 1 | 26 | 73 | 217 | 10.3 | 5.05 | 4.81 |
| 27 | 0.75 | 4000 | 0.5450 | 2180 | 4.113 | 7.546 | 2.021±0.033 | 3 | 1 | 19 | 63 | 149 | 7.48 | 3.67 | 6.91 |
| 28 | 0.78 | 30000 | 0.4144 | 12432 | 2.407 | 5.808 | 1.759±0.015 | 3 | 1 | 14 | 48 | 166 | 5.8 | 3.05 | 8.66 |
| 30 | 0.83 | 6000 | 0.2015 | 1209 | 0.7425 | 3.685 | 1.304±0.043 | 2 | 1 | 9 | 27 | 66 | 3.63 | 2.19 | 15.9 |
| 32 | 0.89 | 6000 | 0.0813 | 488 | 0.2375 | 2.92 | 1.072±0.063 | 1 | 1 | 6 | 24 | 29 | 2.87 | 1.89 | 34.7 |
| 34 | 0.94 | 10000 | 0.0251 | 251 | 0.0504 | 2.008 | 0.697±0.089 | 1 | 1 | 4 | 8 | 48 | 1.82 | 1.52 | 143 |
| 36 | 1.00 | 10000 | 0.0085 | 85 | 0.013 | 1.529 | 0.425±0.107 | 1 | 1 | 2 | 14 | 14 | 1.38 | 1.25 | 263 |
| 38 | 1.06 | 10000 | 0.0022 | 22 | 0.0038 | 1.727 | 0.547±0.228 | 1 | 1 | 3 | 10 | 10 | 1.33 | 1.35 | 1.01e+03 |
| 40 | 1.11 | 20000 | 0.0006 | 11 | 0.00065 | 1.182 | 0.167±0.108 | 1 | 1 | 2 | 2 | 2 | 1.1 | 1.13 | 2.01e+03 |
| 44 | 1.22 | 20000 | 0.0000 | 0 | 0 | nan | nan±nan | nan | nan | nan | nan | 0 | nan | nan | nan |
| 47 | 1.31 | 20000 | 0.0000 | 0 | 0 | nan | nan±nan | nan | nan | nan | nan | 0 | nan | nan | nan |

#### k = 7  (k! = 5040, k² = 49)
| n | n/k² | samples | Pr(M>0) | #M>0 | E[M] | R | ln R | med | q10 | q90 | q99 | max | R w/o max | geo | E[M²]/E[M]² |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 29 | 0.59 | 3000 | 0.9967 | 2990 | 200.7 | 201.4 | 5.305±0.020 | 131 | 24 | 471 | 1009 | 2862 | 200 | 115 | 2.16 |
| 31 | 0.63 | 3000 | 0.9783 | 2935 | 95.01 | 97.12 | 4.576±0.023 | 49 | 6 | 235 | 662 | 1556 | 96.6 | 42.9 | 3.08 |
| 33 | 0.67 | 3000 | 0.8963 | 2689 | 44.99 | 50.19 | 3.916±0.037 | 18 | 2 | 131 | 447 | 1854 | 49.5 | 17.5 | 4.78 |
| 35 | 0.71 | 3000 | 0.7047 | 2114 | 16.42 | 23.3 | 3.149±0.047 | 8 | 1 | 56 | 258 | 1095 | 22.8 | 8.11 | 8.2 |
| 36 | 0.73 | 3000 | 0.6010 | 1803 | 10.59 | 17.62 | 2.869±0.041 | 6 | 1 | 44 | 159 | 501 | 17.4 | 6.32 | 8.24 |
| 37 | 0.76 | 20000 | 0.4820 | 9640 | 6.125 | 12.71 | 2.542±0.022 | 4 | 1 | 29 | 143 | 549 | 12.7 | 4.62 | 12.7 |
| 38 | 0.78 | 3000 | 0.3633 | 1090 | 3.656 | 10.06 | 2.309±0.062 | 3 | 1 | 22 | 132 | 263 | 9.83 | 3.85 | 16.9 |
| 40 | 0.82 | 3000 | 0.1827 | 548 | 1.283 | 7.026 | 1.950±0.100 | 2 | 1 | 13 | 94 | 210 | 6.65 | 2.92 | 36.3 |
| 42 | 0.86 | 6000 | 0.0898 | 539 | 0.3438 | 3.827 | 1.342±0.083 | 2 | 1 | 8 | 38 | 80 | 3.69 | 2.1 | 51.3 |
| 44 | 0.90 | 10000 | 0.0310 | 310 | 0.0863 | 2.784 | 1.024±0.107 | 1 | 1 | 6 | 17 | 74 | 2.55 | 1.77 | 143 |
| 46 | 0.94 | 10000 | 0.0128 | 128 | 0.0325 | 2.539 | 0.932±0.115 | 1 | 1 | 5 | 21 | 25 | 2.36 | 1.71 | 221 |
| 48 | 0.98 | 10000 | 0.0046 | 46 | 0.0087 | 1.891 | 0.637±0.132 | 1 | 1 | 3 | 10 | 10 | 1.71 | 1.5 | 416 |
| 52 | 1.06 | 10000 | 0.0003 | 3 | 0.0003 | 1 | 0.000±0.000 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3.33e+03 |
| 56 | 1.14 | 10000 | 0.0000 | 0 | 0 | nan | nan±nan | nan | nan | nan | nan | 0 | nan | nan | nan |
| 60 | 1.22 | 10000 | 0.0000 | 0 | 0 | nan | nan±nan | nan | nan | nan | nan | 0 | nan | nan | nan |
| 64 | 1.31 | 10000 | 0.0000 | 0 | 0 | nan | nan±nan | nan | nan | nan | nan | 0 | nan | nan | nan |

#### k = 8  (k! = 40320, k² = 64)
| n | n/k² | samples | Pr(M>0) | #M>0 | E[M] | R | ln R | med | q10 | q90 | q99 | max | R w/o max | geo | E[M²]/E[M]² |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 38 | 0.59 | 2000 | 0.9995 | 1999 | 747.5 | 747.8 | 6.617±0.030 | 404 | 54 | 1780 | 5345 | 9721 | 743 | 345 | 2.93 |
| 41 | 0.64 | 2000 | 0.9755 | 1951 | 247.3 | 253.5 | 5.535±0.040 | 92 | 6 | 631 | 2273 | 5755 | 251 | 75.6 | 4.51 |
| 44 | 0.69 | 2000 | 0.8405 | 1681 | 59.96 | 71.34 | 4.267±0.055 | 18 | 2 | 189 | 815 | 2113 | 70.1 | 17.6 | 6.82 |
| 46 | 0.72 | 6000 | 0.6470 | 3882 | 25.46 | 39.35 | 3.672±0.045 | 8 | 1 | 93 | 477 | 2742 | 38.7 | 9.52 | 14.7 |
| 48 | 0.75 | 12000 | 0.4497 | 5397 | 10.18 | 22.63 | 3.119±0.041 | 5 | 1 | 49 | 308 | 1942 | 22.3 | 5.84 | 24.1 |
| 50 | 0.78 | 6000 | 0.2590 | 1554 | 3.597 | 13.89 | 2.631±0.088 | 3 | 1 | 30 | 156 | 995 | 13.3 | 4.13 | 48.1 |
| 52 | 0.81 | 2000 | 0.1475 | 295 | 1.111 | 7.536 | 2.020±0.175 | 2 | 1 | 12 | 166 | 259 | 6.68 | 2.73 | 72.3 |
| 55 | 0.86 | 4000 | 0.0437 | 175 | 0.15 | 3.429 | 1.232±0.103 | 2 | 1 | 9 | 23 | 25 | 3.3 | 2.02 | 68.1 |
| 58 | 0.91 | 4000 | 0.0095 | 38 | 0.0395 | 4.158 | 1.425±0.342 | 1 | 1 | 7 | 49 | 49 | 2.95 | 1.95 | 565 |
| 62 | 0.97 | 4000 | 0.0018 | 7 | 0.00275 | 1.571 | 0.452±0.197 | 1 | 1 | 3 | 3 | 3 | 1.33 | 1.43 | 694 |
| 66 | 1.03 | 4000 | 0.0003 | 1 | 0.00025 | 1 | 0.000±0.000 | 1 | 1 | 1 | 1 | 1 | nan | 1 | 4e+03 |
| 70 | 1.09 | 6000 | 0.0000 | 0 | 0 | nan | nan±nan | nan | nan | nan | nan | 0 | nan | nan | nan |
| 76 | 1.19 | 6000 | 0.0000 | 0 | 0 | nan | nan±nan | nan | nan | nan | nan | 0 | nan | nan | nan |
| 83 | 1.30 | 6000 | 0.0000 | 0 | 0 | nan | nan±nan | nan | nan | nan | nan | 0 | nan | nan | nan |

#### k = 9  (k! = 362880, k² = 81)
| n | n/k² | samples | Pr(M>0) | #M>0 | E[M] | R | ln R | med | q10 | q90 | q99 | max | R w/o max | geo | E[M²]/E[M]² |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 49 | 0.60 | 300 | 1.0000 | 300 | 1865 | 1865 | 7.531±nan | 653 | 65 | 4667 | 18730 | 43143 | 1.73e+03 | 591 | 5.11 |
| 52 | 0.64 | 300 | 0.9800 | 294 | 757.8 | 773.3 | 6.651±0.156 | 167 | 9 | 1919 | 7707 | 23829 | 695 | 154 | 7.43 |
| 55 | 0.68 | 600 | 0.8500 | 510 | 164.1 | 193.1 | 5.263±0.119 | 36 | 2 | 417 | 2606 | 4729 | 184 | 32.9 | 8.99 |
| 58 | 0.72 | 1200 | 0.6033 | 724 | 39.05 | 64.72 | 4.170±0.156 | 9 | 1 | 106 | 950 | 5857 | 56.7 | 10.4 | 31.9 |
| 60 | 0.74 | 2000 | 0.4230 | 846 | 16.22 | 38.34 | 3.647±0.113 | 6 | 1 | 88 | 563 | 2222 | 35.8 | 7.51 | 27.9 |
| 62 | 0.77 | 2000 | 0.2545 | 509 | 5.613 | 22.06 | 3.094±0.181 | 3 | 1 | 44 | 303 | 1399 | 19.3 | 5.01 | 61.3 |
| 64 | 0.79 | 1000 | 0.1330 | 133 | 2.226 | 16.74 | 2.818±0.384 | 3 | 1 | 20 | 251 | 831 | 10.6 | 3.65 | 168 |
| 68 | 0.84 | 2000 | 0.0265 | 53 | 0.432 | 16.3 | 2.791±0.689 | 2 | 1 | 15 | 539 | 539 | 6.25 | 3.07 | 805 |
| 72 | 0.89 | 1500 | 0.0073 | 11 | 0.02 | 2.727 | 1.003±0.358 | 1 | 1 | 4 | 12 | 12 | 1.8 | 1.83 | 317 |

### Histograms of ln M given M>0 (bins of width 1 in ln M; counts)
k=5 n=15: [0,1):1523 [1,2):4702 [2,3):8418 [3,4):4855 [4,5):166
k=5 n=16: [0,1):3357 [1,2):6075 [2,3):6805 [3,4):2277 [4,5):46
k=5 n=17: [0,1):5145 [1,2):5994 [2,3):4369 [3,4):994 [4,5):9
k=5 n=18: [0,1):5739 [1,2):4903 [2,3):2417 [3,4):350
k=5 n=19: [0,1):10946 [1,2):6754 [2,3):2448 [3,4):273
k=5 n=20: [0,1):8945 [1,2):3967 [2,3):1088 [3,4):67
k=5 n=21: [0,1):6472 [1,2):2179 [2,3):445 [3,4):26
k=5 n=22: [0,1):4177 [1,2):1094 [2,3):193 [3,4):9
k=5 n=24: [0,1):1496 [1,2):239 [2,3):17
k=5 n=26: [0,1):397 [1,2):35 [2,3):3
k=5 n=28: [0,1):95 [1,2):4
k=5 n=32: [0,1):2
k=6 n=22: [0,1):125 [1,2):378 [2,3):945 [3,4):1423 [4,5):948 [5,6):137
k=6 n=24: [0,1):583 [1,2):889 [2,3):1009 [3,4):789 [4,5):298 [5,6):14
k=6 n=26: [0,1):856 [1,2):844 [2,3):634 [3,4):327 [4,5):55 [5,6):4
k=6 n=27: [0,1):922 [1,2):679 [2,3):386 [3,4):162 [4,5):30 [5,6):1
k=6 n=28: [0,1):6097 [1,2):3735 [2,3):1937 [3,4):573 [4,5):88 [5,6):2
k=6 n=30: [0,1):762 [1,2):298 [2,3):124 [3,4):24 [4,5):1
k=6 n=32: [0,1):336 [1,2):117 [2,3):27 [3,4):8
k=6 n=34: [0,1):206 [1,2):41 [2,3):3 [3,4):1
k=6 n=36: [0,1):77 [1,2):6 [2,3):2
k=6 n=38: [0,1):19 [1,2):2 [2,3):1
k=6 n=40: [0,1):11
k=7 n=29: [0,1):23 [1,2):51 [2,3):168 [3,4):490 [4,5):888 [5,6):976 [6,7):375 [7,8):19
k=7 n=31: [0,1):104 [1,2):241 [2,3):489 [3,4):719 [4,5):789 [5,6):479 [6,7):110 [7,8):4
k=7 n=33: [0,1):339 [1,2):469 [2,3):598 [3,4):604 [4,5):463 [5,6):180 [6,7):35 [7,8):1
k=7 n=35: [0,1):516 [1,2):529 [2,3):460 [3,4):389 [4,5):175 [5,6):40 [6,7):5
k=7 n=36: [0,1):540 [1,2):466 [2,3):417 [3,4):237 [4,5):116 [5,6):26 [6,7):1
k=7 n=37: [0,1):3717 [1,2):2682 [2,3):1831 [3,4):929 [4,5):390 [5,6):86 [6,7):5
k=7 n=38: [0,1):474 [1,2):321 [2,3):174 [3,4):83 [4,5):28 [5,6):10
k=7 n=40: [0,1):284 [1,2):156 [2,3):73 [3,4):22 [4,5):12 [5,6):1
k=7 n=42: [0,1):356 [1,2):126 [2,3):42 [3,4):12 [4,5):3
k=7 n=44: [0,1):226 [1,2):63 [2,3):18 [3,4):2 [4,5):1
k=7 n=46: [0,1):95 [1,2):25 [2,3):6 [3,4):2
k=7 n=48: [0,1):37 [1,2):7 [2,3):2
k=7 n=52: [0,1):3
k=8 n=38: [0,1):3 [1,2):14 [2,3):49 [3,4):135 [4,5):306 [5,6):492 [6,7):579 [7,8):344 [8,9):72 [9,10):5
k=8 n=41: [0,1):89 [1,2):128 [2,3):223 [3,4):326 [4,5):440 [5,6):400 [6,7):249 [7,8):89 [8,9):7
k=8 n=44: [0,1):270 [1,2):310 [2,3):321 [3,4):311 [4,5):256 [5,6):148 [6,7):58 [7,8):7
k=8 n=46: [0,1):931 [1,2):930 [2,3):806 [3,4):593 [4,5):395 [5,6):166 [6,7):54 [7,8):7
k=8 n=48: [0,1):1888 [1,2):1382 [2,3):995 [3,4):644 [4,5):338 [5,6):120 [6,7):27 [7,8):3
k=8 n=50: [0,1):696 [1,2):372 [2,3):260 [3,4):140 [4,5):69 [5,6):14 [6,7):3
k=8 n=52: [0,1):161 [1,2):80 [2,3):36 [3,4):11 [4,5):4 [5,6):3
k=8 n=55: [0,1):121 [1,2):34 [2,3):15 [3,4):5
k=8 n=58: [0,1):26 [1,2):9 [2,3):1 [3,4):2
k=8 n=62: [0,1):6 [1,2):1
k=8 n=66: [0,1):1
k=9 n=49: [0,1):1 [1,2):3 [2,3):6 [3,4):19 [4,5):29 [5,6):62 [6,7):68 [7,8):63 [8,9):37 [9,10):11 [10,11):1
k=9 n=52: [0,1):7 [1,2):18 [2,3):24 [3,4):40 [4,5):49 [5,6):58 [6,7):46 [7,8):33 [8,9):17 [9,10):1 [10,11):1
k=9 n=55: [0,1):60 [1,2):72 [2,3):79 [3,4):87 [4,5):92 [5,6):63 [6,7):33 [7,8):21 [8,9):3
k=9 n=58: [0,1):180 [1,2):158 [2,3):134 [3,4):129 [4,5):66 [5,6):33 [6,7):18 [7,8):5 [8,9):1
k=9 n=60: [0,1):258 [1,2):214 [2,3):155 [3,4):101 [4,5):71 [5,6):33 [6,7):12 [7,8):2
k=9 n=62: [0,1):206 [1,2):117 [2,3):96 [3,4):48 [4,5):29 [5,6):10 [6,7):2 [7,8):1
k=9 n=64: [0,1):65 [1,2):30 [2,3):26 [3,4):7 [4,5):2 [5,6):2 [6,7):1
k=9 n=68: [0,1):29 [1,2):12 [2,3):9 [3,4):1 [4,5):1 [6,7):1
k=9 n=72: [0,1):8 [1,2):2 [2,3):1


## B. Task 2 — fits (machine output)

### Task 2: ln R vs k at fixed n/k² and at n = t(k) (Pr(M>0)=1/2)
| k | t(k) (interp.) | ln R at t(k) | ln E[M] at t(k) | ln R @0.65k² | @0.75k² | @0.85k² | @1.0k² | @1.2k² | n,lnR @P=.9 | @P=.1 | @P=.02 | k ln k | k | √k |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 19.1 | 1.335 | 0.638 | 2.23 | 1.42 | 0.88 | 0.41 | 0.08 | 16.3,2.22 | 22.8,0.67 | 25.4,0.37 | 8.05 | 5 | 2.24 |
| 6 | 27.3 | 1.931 | 1.229 | 3.23 | 2.02 | 1.23 | 0.42 | nan | 23.9,3.03 | 31.7,1.11 | 34.6,0.61 | 10.75 | 6 | 2.45 |
| 7 | 36.8 | 2.592 | 1.895 | 4.30 | 2.62 | 1.45 | 0.48 | nan | 32.9,3.95 | 41.8,1.41 | 45.2,0.97 | 13.62 | 7 | 2.65 |
| 8 | 47.5 | 3.260 | 2.554 | 5.28 | 3.12 | 1.39 | 0.23 | nan | 42.7,4.83 | 53.4,1.66 | 57.1,1.37 | 16.64 | 8 | 2.83 |
| 9 | 59.1 | 3.870 | 3.161 | 6.35 | 3.44 | 2.41 | nan | nan | 53.8,5.80 | 65.2,2.81 | 69.4,2.18 | 19.78 | 9 | 3.00 |

Growth diagnostics (successive k):
- ln R at t(k): k5→6: Δ=+0.596, d lnR/d ln k=3.27, ratio to Δ(k ln k)=0.220, to Δk=0.596, to Δ√k=2.791; k6→7: Δ=+0.661, d lnR/d ln k=4.29, ratio to Δ(k ln k)=0.230, to Δk=0.661, to Δ√k=3.367; k7→8: Δ=+0.668, d lnR/d ln k=5.01, ratio to Δ(k ln k)=0.222, to Δk=0.668, to Δ√k=3.659; k8→9: Δ=+0.610, d lnR/d ln k=5.18, ratio to Δ(k ln k)=0.194, to Δk=0.610, to Δ√k=3.555
- ln R at 0.75k²: k5→6: Δ=+0.602, d lnR/d ln k=3.30, ratio to Δ(k ln k)=0.223, to Δk=0.602, to Δ√k=2.820; k6→7: Δ=+0.603, d lnR/d ln k=3.91, ratio to Δ(k ln k)=0.210, to Δk=0.603, to Δ√k=3.071; k7→8: Δ=+0.495, d lnR/d ln k=3.71, ratio to Δ(k ln k)=0.164, to Δk=0.495, to Δ√k=2.711; k8→9: Δ=+0.320, d lnR/d ln k=2.72, ratio to Δ(k ln k)=0.102, to Δk=0.320, to Δ√k=1.865
- ln R at 1.0k²: k5→6: Δ=+0.011, d lnR/d ln k=0.06, ratio to Δ(k ln k)=0.004, to Δk=0.011, to Δ√k=0.053; k6→7: Δ=+0.053, d lnR/d ln k=0.34, ratio to Δ(k ln k)=0.018, to Δk=0.053, to Δ√k=0.270; k7→8: Δ=-0.252, d lnR/d ln k=-1.89, ratio to Δ(k ln k)=-0.084, to Δk=-0.252, to Δ√k=-1.379
- ln R at P=.1: k5→6: Δ=+0.435, d lnR/d ln k=2.38, ratio to Δ(k ln k)=0.161, to Δk=0.435, to Δ√k=2.036; k6→7: Δ=+0.301, d lnR/d ln k=1.95, ratio to Δ(k ln k)=0.105, to Δk=0.301, to Δ√k=1.534; k7→8: Δ=+0.250, d lnR/d ln k=1.88, ratio to Δ(k ln k)=0.083, to Δk=0.250, to Δ√k=1.371; k8→9: Δ=+1.150, d lnR/d ln k=9.77, ratio to Δ(k ln k)=0.366, to Δk=1.150, to Δ√k=6.705
- ln R at P=.02: k5→6: Δ=+0.240, d lnR/d ln k=1.32, ratio to Δ(k ln k)=0.089, to Δk=0.240, to Δ√k=1.125; k6→7: Δ=+0.355, d lnR/d ln k=2.30, ratio to Δ(k ln k)=0.124, to Δk=0.355, to Δ√k=1.807; k7→8: Δ=+0.398, d lnR/d ln k=2.98, ratio to Δ(k ln k)=0.132, to Δk=0.398, to Δ√k=2.177; k8→9: Δ=+0.819, d lnR/d ln k=6.95, ratio to Δ(k ln k)=0.261, to Δk=0.819, to Δ√k=4.774


## C. Task 3 — pairwise correlations at n ≈ t(k) and in the tail (selected points; all points in analysis.txt)


### Task 3: pairwise correlation ratios  ρ(π,π') = Pr(A_π ∧ A_π') / (Pr A_π · Pr A_π')
Pooled estimators over all pairs of the given type: ρ_pool = (Σ_pairs #co-miss / S) / (Σ_pairs m_π m_π' / S²).
Also E[M²]/E[M]² ≈ ρ for a uniformly random pair (plus the diagonal 1/E[M] term).



**k=5, n=19** (S=40000, Pr(M>0)=0.511, E[M]=1.97, R=3.86, E[M²]/E[M]²=4.45)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 13.62 (pairs with both missed: 480, Σco-miss=71139)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 3.76 (pairs with both missed: 388, Σco-miss=15755)
- π vs 6 uniformly random π': ρ_pool = 4.09 (pairs with both missed: 695, Σco-miss=30919)
- id [miss rate 0.0203, 1.23× avg]: swap pos 1,2: ρ=10.1 (m1=810, m2=761, co=156); swap pos mid: ρ=11.8 (m1=810, m2=776, co=185); reverse: ρ=0.0 (m1=810, m2=769, co=0); complement: ρ=0.0 (m1=810, m2=769, co=0); inverse: same; rev∘comp: same
- top1=52341 [miss rate 0.0216, 1.32× avg]: swap pos 1,2: ρ=13.3 (m1=866, m2=580, co=167); swap pos mid: ρ=13.4 (m1=866, m2=669, co=194); reverse: ρ=0.6 (m1=866, m2=832, co=11); complement: ρ=0.6 (m1=866, m2=832, co=11); inverse: same; rev∘comp: same
- top2=54231 [miss rate 0.0215, 1.31× avg]: swap pos 1,2: ρ=11.2 (m1=859, m2=809, co=195); swap pos mid: ρ=14.1 (m1=859, m2=649, co=196); reverse: ρ=0.4 (m1=859, m2=776, co=6); complement: ρ=0.2 (m1=859, m2=818, co=3); inverse: ρ=11.0 (m1=859, m2=819, co=193); rev∘comp: ρ=11.0 (m1=859, m2=819, co=193)
- top3=12354 [miss rate 0.0209, 1.27× avg]: swap pos 1,2: ρ=10.1 (m1=834, m2=824, co=174); swap pos mid: ρ=12.4 (m1=834, m2=778, co=201); reverse: ρ=0.0 (m1=834, m2=751, co=0); complement: ρ=0.0 (m1=834, m2=743, co=0); inverse: same; rev∘comp: ρ=2.8 (m1=834, m2=761, co=45)


**k=6, n=28** (S=30000, Pr(M>0)=0.414, E[M]=2.41, R=5.81, E[M²]/E[M]²=8.66)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 57.76 (pairs with both missed: 3600, Σco-miss=72611)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 9.22 (pairs with both missed: 2420, Σco-miss=7764)
- π vs 6 uniformly random π': ρ_pool = 8.20 (pairs with both missed: 4305, Σco-miss=11883)
- id [miss rate 0.0047, 1.41× avg]: swap pos 1,2: ρ=45.4 (m1=141, m2=136, co=29); swap pos mid: ρ=42.8 (m1=141, m2=164, co=33); reverse: ρ=0.0 (m1=141, m2=153, co=0); complement: ρ=0.0 (m1=141, m2=153, co=0); inverse: same; rev∘comp: same
- top1=564231 [miss rate 0.0064, 1.90× avg]: swap pos 1,2: ρ=31.8 (m1=191, m2=173, co=35); swap pos mid: ρ=47.1 (m1=191, m2=120, co=36); reverse: ρ=0.0 (m1=191, m2=171, co=0); complement: ρ=0.0 (m1=191, m2=162, co=0); inverse: ρ=8.4 (m1=191, m2=149, co=8); rev∘comp: ρ=8.4 (m1=191, m2=149, co=8)
- top2=125436 [miss rate 0.0063, 1.87× avg]: swap pos 1,2: ρ=37.9 (m1=188, m2=177, co=42); swap pos mid: ρ=47.9 (m1=188, m2=110, co=33); reverse: ρ=0.0 (m1=188, m2=186, co=0); complement: ρ=0.0 (m1=188, m2=187, co=0); inverse: same; rev∘comp: ρ=10.4 (m1=188, m2=169, co=11)
- top3=652341 [miss rate 0.0062, 1.86× avg]: swap pos 1,2: ρ=33.4 (m1=187, m2=173, co=36); swap pos mid: ρ=49.0 (m1=187, m2=131, co=40); reverse: ρ=1.9 (m1=187, m2=169, co=2); complement: ρ=0.0 (m1=187, m2=188, co=0); inverse: ρ=8.6 (m1=187, m2=186, co=10); rev∘comp: ρ=8.6 (m1=187, m2=186, co=10)


**k=7, n=37** (S=20000, Pr(M>0)=0.482, E[M]=6.12, R=12.7, E[M²]/E[M]²=12.7)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 159.31 (pairs with both missed: 30240, Σco-miss=154314)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 19.80 (pairs with both missed: 17384, Σco-miss=11033)
- π vs 6 uniformly random π': ρ_pool = 12.31 (pairs with both missed: 30219, Σco-miss=10959)
- id [miss rate 0.0030, 2.47× avg]: swap pos 1,2: ρ=44.0 (m1=60, m2=53, co=7); swap pos mid: ρ=85.5 (m1=60, m2=39, co=10); reverse: ρ=0.0 (m1=60, m2=50, co=0); complement: ρ=0.0 (m1=60, m2=50, co=0); inverse: same; rev∘comp: same
- top1=7456231 [miss rate 0.0035, 2.88× avg]: swap pos 1,2: ρ=85.7 (m1=70, m2=30, co=9); swap pos mid: ρ=114.3 (m1=70, m2=35, co=14); reverse: ρ=0.0 (m1=70, m2=64, co=0); complement: ρ=0.0 (m1=70, m2=53, co=0); inverse: ρ=38.7 (m1=70, m2=59, co=8); rev∘comp: ρ=38.7 (m1=70, m2=59, co=8)
- top2=7234561 [miss rate 0.0034, 2.84× avg]: swap pos 1,2: ρ=79.7 (m1=69, m2=40, co=11); swap pos mid: ρ=106.8 (m1=69, m2=38, co=14); reverse: ρ=0.0 (m1=69, m2=62, co=0); complement: ρ=0.0 (m1=69, m2=62, co=0); inverse: same; rev∘comp: same
- top3=1543276 [miss rate 0.0034, 2.80× avg]: swap pos 1,2: ρ=102.9 (m1=68, m2=40, co=14); swap pos mid: ρ=90.0 (m1=68, m2=49, co=15); reverse: ρ=0.0 (m1=68, m2=65, co=0); complement: ρ=0.0 (m1=68, m2=54, co=0); inverse: same; rev∘comp: ρ=10.3 (m1=68, m2=57, co=2)


**k=8, n=48** (S=12000, Pr(M>0)=0.450, E[M]=10.2, R=22.6, E[M²]/E[M]²=24.1)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 601.08 (pairs with both missed: 277590, Σco-miss=166010)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 46.54 (pairs with both missed: 138452, Σco-miss=6201)
- π vs 6 uniformly random π': ρ_pool = 24.47 (pairs with both missed: 220641, Σco-miss=4523)
- id [miss rate 0.0008, 2.97× avg]: swap pos 1,2: ρ=400.0 (m1=9, m2=10, co=3); swap pos mid: ρ=166.7 (m1=9, m2=24, co=3); reverse: ρ=0.0 (m1=9, m2=8, co=0); complement: ρ=0.0 (m1=9, m2=8, co=0); inverse: same; rev∘comp: same
- top1=12354678 [miss rate 0.0020, 7.92× avg]: swap pos 1,2: ρ=227.3 (m1=24, m2=11, co=5); swap pos mid: ρ=166.7 (m1=24, m2=9, co=3); reverse: ρ=0.0 (m1=24, m2=10, co=0); complement: ρ=0.0 (m1=24, m2=10, co=0); inverse: same; rev∘comp: same
- top2=85673412 [miss rate 0.0017, 6.60× avg]: swap pos 1,2: ρ=250.0 (m1=20, m2=12, co=5); swap pos mid: ρ=240.0 (m1=20, m2=10, co=4); reverse: ρ=0.0 (m1=20, m2=13, co=0); complement: ρ=0.0 (m1=20, m2=12, co=0); inverse: ρ=0.0 (m1=20, m2=9, co=0); rev∘comp: ρ=0.0 (m1=20, m2=9, co=0)
- top3=21435876 [miss rate 0.0017, 6.60× avg]: swap pos 1,2: ρ=300.0 (m1=20, m2=8, co=4); swap pos mid: ρ=200.0 (m1=20, m2=9, co=3); reverse: ρ=0.0 (m1=20, m2=6, co=0); complement: ρ=0.0 (m1=20, m2=8, co=0); inverse: same; rev∘comp: ρ=0.0 (m1=20, m2=12, co=0)


**k=8, n=52** (S=2000, Pr(M>0)=0.147, E[M]=1.11, R=7.54, E[M²]/E[M]²=72.3)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 1238.40 (pairs with both missed: 26378, Σco-miss=2335)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 217.09 (pairs with both missed: 13811, Σco-miss=94)
- π vs 6 uniformly random π': ρ_pool = 70.66 (pairs with both missed: 12672, Σco-miss=23)


**k=8, n=55** (S=4000, Pr(M>0)=0.044, E[M]=0.15, R=3.43, E[M²]/E[M]²=68.1)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 2608.25 (pairs with both missed: 7889, Σco-miss=253)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 281.69 (pairs with both missed: 3994, Σco-miss=5)
- π vs 6 uniformly random π': ρ_pool = 97.56 (pairs with both missed: 3540, Σco-miss=1)


**k=9, n=60** (S=2000, Pr(M>0)=0.423, E[M]=16.2, R=38.3, E[M²]/E[M]²=27.9)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 1094.66 (pairs with both missed: 425571, Σco-miss=41377)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 114.67 (pairs with both missed: 197690, Σco-miss=991)
- π vs 6 uniformly random π': ρ_pool = 28.75 (pairs with both missed: 182307, Σco-miss=250)
- top1=132476598 [miss rate 0.0030, 67.13× avg]: swap pos 1,2: ρ=333.3 (m1=6, m2=1, co=1); swap pos mid: ρ=nan (m1=6, m2=0, co=0); reverse: ρ=nan (m1=6, m2=0, co=0); complement: ρ=nan (m1=6, m2=0, co=0); inverse: same; rev∘comp: ρ=0.0 (m1=6, m2=1, co=0)


**k=9, n=62** (S=2000, Pr(M>0)=0.255, E[M]=5.61, R=22.1, E[M²]/E[M]²=61.3)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 1455.73 (pairs with both missed: 158643, Σco-miss=12940)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 276.89 (pairs with both missed: 73259, Σco-miss=417)
- π vs 6 uniformly random π': ρ_pool = 58.47 (pairs with both missed: 65544, Σco-miss=63)


**k=9, n=64** (S=1000, Pr(M>0)=0.133, E[M]=2.23, R=16.7, E[M²]/E[M]²=168)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 943.19 (pairs with both missed: 32291, Σco-miss=2955)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 320.75 (pairs with both missed: 15273, Σco-miss=34)
- π vs 6 uniformly random π': ρ_pool = 171.05 (pairs with both missed: 13260, Σco-miss=13)


**k=9, n=68** (S=2000, Pr(M>0)=0.026, E[M]=0.432, R=16.3, E[M²]/E[M]²=805)
- π vs π∘(adjacent transposition), positions and values: ρ_pool = 1972.67 (pairs with both missed: 12629, Σco-miss=1155)
- π vs dihedral images (rev/comp/inv/…): ρ_pool = 916.67 (pairs with both missed: 5950, Σco-miss=22)
- π vs 6 uniformly random π': ρ_pool = 769.23 (pairs with both missed: 5172, Σco-miss=5)


## D. Task 4 — structure of the missing patterns (selected points; all points in analysis.txt)



**k=5, n=19** (S=40000, Pr(M>0)=0.511, distinct patterns ever missed: 120 of 120, total misses 78894)
| feature | missing (weighted by miss count) | population S_k |
|---|---|---|
| LIS | 2.799 | 2.792 |
| LDS | 2.797 | 2.792 |
| max(LIS,LDS) | 3.322 | 3.300 |
| #monotone runs | 2.973 | 3.000 |
| #ascending runs | 3.000 | 3.000 |
| ⊕-decomposable | 0.425 | 0.408 |
| ⊖-decomposable | 0.422 | 0.408 |
| indecomposable (neither) | 0.152 | 0.183 |
max(LIS,LDS) distribution, missing vs population: 3: 0.698 vs 0.717, 4: 0.282 vs 0.267, 5: 0.020 vs 0.017
#monotone runs distribution, missing vs population: 1: 0.020 vs 0.017, 2: 0.244 vs 0.233, 3: 0.479 vs 0.483, 4: 0.257 vs 0.267
top-12 missed patterns (miss count, ×avg): 52341 (866, 1.3×), 54231 (859, 1.3×), 12354 (834, 1.3×), 14325 (832, 1.3×), 53412 (825, 1.3×), 21354 (824, 1.3×), 53421 (819, 1.2×), 12435 (818, 1.2×), 21543 (810, 1.2×), 12345 (810, 1.2×), 45231 (809, 1.2×), 12543 (802, 1.2×)
among σ with M>0: fraction whose missing set contains an adjacent-transposition pair: 0.430; a dihedral-image pair: 0.129
cluster structure (adjacent-transposition graph on the missing set, σ with 0<M≤3000, 20421 σ): mean M=3.86, mean #components=1.61, mean fraction of M in largest component=0.831; among σ with M≥10: mean #components=1.87, mean M=15.0


**k=6, n=28** (S=30000, Pr(M>0)=0.414, distinct patterns ever missed: 720 of 720, total misses 72206)
| feature | missing (weighted by miss count) | population S_k |
|---|---|---|
| LIS | 3.146 | 3.140 |
| LDS | 3.164 | 3.140 |
| max(LIS,LDS) | 3.705 | 3.650 |
| #monotone runs | 3.618 | 3.667 |
| #ascending runs | 3.507 | 3.500 |
| ⊕-decomposable | 0.393 | 0.360 |
| ⊖-decomposable | 0.393 | 0.360 |
| indecomposable (neither) | 0.214 | 0.281 |
max(LIS,LDS) distribution, missing vs population: 3: 0.390 vs 0.425, 4: 0.519 vs 0.503, 5: 0.087 vs 0.069, 6: 0.004 vs 0.003
#monotone runs distribution, missing vs population: 1: 0.004 vs 0.003, 2: 0.096 vs 0.083, 3: 0.338 vs 0.328, 4: 0.402 vs 0.417, 5: 0.160 vs 0.169
top-12 missed patterns (miss count, ×avg): 564231 (191, 1.9×), 125436 (188, 1.9×), 652341 (187, 1.9×), 645231 (187, 1.9×), 634521 (186, 1.9×), 645321 (183, 1.8×), 432165 (183, 1.8×), 623451 (181, 1.8×), 154326 (178, 1.8×), 634512 (178, 1.8×), 143265 (177, 1.8×), 215436 (177, 1.8×)
among σ with M>0: fraction whose missing set contains an adjacent-transposition pair: 0.442; a dihedral-image pair: 0.090
cluster structure (adjacent-transposition graph on the missing set, σ with 0<M≤3000, 12432 σ): mean M=5.81, mean #components=2.11, mean fraction of M in largest component=0.769; among σ with M≥10: mean #components=3.61, mean M=21.2


**k=7, n=37** (S=20000, Pr(M>0)=0.482, distinct patterns ever missed: 5040 of 5040, total misses 122493)
| feature | missing (weighted by miss count) | population S_k |
|---|---|---|
| LIS | 3.504 | 3.465 |
| LDS | 3.475 | 3.465 |
| max(LIS,LDS) | 4.092 | 4.022 |
| #monotone runs | 4.277 | 4.333 |
| #ascending runs | 3.986 | 4.000 |
| ⊕-decomposable | 0.370 | 0.316 |
| ⊖-decomposable | 0.364 | 0.316 |
| indecomposable (neither) | 0.266 | 0.368 |
max(LIS,LDS) distribution, missing vs population: 3: 0.150 vs 0.175, 4: 0.630 vs 0.643, 5: 0.198 vs 0.167, 6: 0.021 vs 0.014, 7: 0.001 vs 0.000
#monotone runs distribution, missing vs population: 1: 0.001 vs 0.000, 2: 0.031 vs 0.025, 3: 0.177 vs 0.166, 4: 0.372 vs 0.367, 5: 0.319 vs 0.334, 6: 0.100 vs 0.108
top-12 missed patterns (miss count, ×avg): 7456231 (70, 2.9×), 7234561 (69, 2.8×), 1543276 (68, 2.8×), 7634512 (68, 2.8×), 7645231 (66, 2.7×), 2136547 (66, 2.7×), 7564231 (66, 2.7×), 6723451 (65, 2.7×), 1432576 (64, 2.6×), 1326547 (64, 2.6×), 7345621 (64, 2.6×), 7645123 (63, 2.6×)
among σ with M>0: fraction whose missing set contains an adjacent-transposition pair: 0.518; a dihedral-image pair: 0.099
cluster structure (adjacent-transposition graph on the missing set, σ with 0<M≤3000, 9640 σ): mean M=12.71, mean #components=3.43, mean fraction of M in largest component=0.681; among σ with M≥10: mean #components=6.63, mean M=36.9


**k=7, n=44** (S=10000, Pr(M>0)=0.031, distinct patterns ever missed: 765 of 5040, total misses 863)
| feature | missing (weighted by miss count) | population S_k |
|---|---|---|
| LIS | 3.629 | 3.465 |
| LDS | 3.387 | 3.465 |
| max(LIS,LDS) | 4.149 | 4.022 |
| #monotone runs | 4.167 | 4.333 |
| #ascending runs | 3.888 | 4.000 |
| ⊕-decomposable | 0.406 | 0.316 |
| ⊖-decomposable | 0.349 | 0.316 |
| indecomposable (neither) | 0.246 | 0.368 |
max(LIS,LDS) distribution, missing vs population: 3: 0.152 vs 0.175, 4: 0.578 vs 0.643, 5: 0.241 vs 0.167, 6: 0.027 vs 0.014, 7: 0.002 vs 0.000
#monotone runs distribution, missing vs population: 1: 0.002 vs 0.000, 2: 0.041 vs 0.025, 3: 0.198 vs 0.166, 4: 0.384 vs 0.367, 5: 0.298 vs 0.334, 6: 0.078 vs 0.108
top-12 missed patterns (miss count, ×avg): 2765134 (3, 17.5×), 7632145 (3, 17.5×), 3612754 (3, 17.5×), 1647325 (3, 17.5×), 5312764 (3, 17.5×), 2154763 (3, 17.5×), 6451273 (3, 17.5×), 6745312 (3, 17.5×), 1265437 (3, 17.5×), 2135476 (3, 17.5×), 7563412 (3, 17.5×), 2746135 (2, 11.7×)
among σ with M>0: fraction whose missing set contains an adjacent-transposition pair: 0.203; a dihedral-image pair: 0.016
cluster structure (adjacent-transposition graph on the missing set, σ with 0<M≤3000, 310 σ): mean M=2.78, mean #components=1.63, mean fraction of M in largest component=0.845; among σ with M≥10: mean #components=5.23, mean M=20.2


**k=8, n=48** (S=12000, Pr(M>0)=0.450, distinct patterns ever missed: 36776 of 40320, total misses 122114)
| feature | missing (weighted by miss count) | population S_k |
|---|---|---|
| LIS | 3.790 | 3.770 |
| LDS | 3.813 | 3.770 |
| max(LIS,LDS) | 4.456 | 4.350 |
| #monotone runs | 4.907 | 5.000 |
| #ascending runs | 4.503 | 4.500 |
| ⊕-decomposable | 0.340 | 0.278 |
| ⊖-decomposable | 0.352 | 0.278 |
| indecomposable (neither) | 0.309 | 0.443 |
max(LIS,LDS) distribution, missing vs population: 3: 0.036 vs 0.044, 4: 0.551 vs 0.609, 5: 0.341 vs 0.303, 6: 0.066 vs 0.042, 7: 0.006 vs 0.002, 8: 0.000 vs 0.000
#monotone runs distribution, missing vs population: 1: 0.000 vs 0.000, 2: 0.010 vs 0.006, 3: 0.083 vs 0.069, 4: 0.255 vs 0.237, 5: 0.353 vs 0.363, 6: 0.237 vs 0.256, 7: 0.061 vs 0.069
top-12 missed patterns (miss count, ×avg): 12354678 (24, 7.9×), 85673412 (20, 6.6×), 21435876 (20, 6.6×), 14325768 (20, 6.6×), 14325687 (20, 6.6×), 86752143 (19, 6.3×), 13254687 (19, 6.3×), 87345621 (18, 5.9×), 21654378 (18, 5.9×), 46587312 (18, 5.9×), 21543687 (18, 5.9×), 16543278 (17, 5.6×)
among σ with M>0: fraction whose missing set contains an adjacent-transposition pair: 0.530; a dihedral-image pair: 0.077
cluster structure (adjacent-transposition graph on the missing set, σ with 0<M≤3000, 5397 σ): mean M=22.63, mean #components=5.43, mean fraction of M in largest component=0.617; among σ with M≥10: mean #components=11.41, mean M=60.3


**k=8, n=55** (S=4000, Pr(M>0)=0.044, distinct patterns ever missed: 590 of 40320, total misses 600)
| feature | missing (weighted by miss count) | population S_k |
|---|---|---|
| LIS | 3.668 | 3.770 |
| LDS | 3.997 | 3.770 |
| max(LIS,LDS) | 4.575 | 4.350 |
| #monotone runs | 4.800 | 5.000 |
| #ascending runs | 4.648 | 4.500 |
| ⊕-decomposable | 0.343 | 0.278 |
| ⊖-decomposable | 0.485 | 0.278 |
| indecomposable (neither) | 0.172 | 0.443 |
max(LIS,LDS) distribution, missing vs population: 3: 0.028 vs 0.044, 4: 0.492 vs 0.609, 5: 0.372 vs 0.303, 6: 0.093 vs 0.042, 7: 0.015 vs 0.002, 8: 0.000 vs 0.000
#monotone runs distribution, missing vs population: 1: 0.000 vs 0.000, 2: 0.035 vs 0.006, 3: 0.075 vs 0.069, 4: 0.293 vs 0.237, 5: 0.295 vs 0.363, 6: 0.255 vs 0.256, 7: 0.047 vs 0.069
top-12 missed patterns (miss count, ×avg): 65412378 (2, 134.4×), 78325461 (2, 134.4×), 87623154 (2, 134.4×), 86273514 (2, 134.4×), 76852413 (2, 134.4×), 21453687 (2, 134.4×), 86573124 (2, 134.4×), 87132456 (2, 134.4×), 67854321 (2, 134.4×), 32546871 (2, 134.4×), 25436871 (1, 67.2×), 14286537 (1, 67.2×)
among σ with M>0: fraction whose missing set contains an adjacent-transposition pair: 0.263; a dihedral-image pair: 0.006
cluster structure (adjacent-transposition graph on the missing set, σ with 0<M≤3000, 175 σ): mean M=3.43, mean #components=2.19, mean fraction of M in largest component=0.774; among σ with M≥10: mean #components=7.69, mean M=16.9


**k=9, n=60** (S=2000, Pr(M>0)=0.423, distinct patterns ever missed: 30385 of 362880, total misses 32436)
| feature | missing (weighted by miss count) | population S_k |
|---|---|---|
| LIS | 4.117 | 4.059 |
| LDS | 4.217 | 4.059 |
| max(LIS,LDS) | 4.915 | 4.647 |
| #monotone runs | 5.543 | 5.667 |
| #ascending runs | 5.063 | 5.000 |
| ⊕-decomposable | 0.359 | 0.247 |
| ⊖-decomposable | 0.380 | 0.247 |
| indecomposable (neither) | 0.261 | 0.507 |
max(LIS,LDS) distribution, missing vs population: 3: 0.002 vs 0.005, 4: 0.310 vs 0.452, 5: 0.490 vs 0.444, 6: 0.170 vs 0.091, 7: 0.026 vs 0.008, 8: 0.002 vs 0.000, 9: 0.000 vs 0.000
#monotone runs distribution, missing vs population: 1: 0.000 vs 0.000, 2: 0.003 vs 0.001, 3: 0.033 vs 0.024, 4: 0.147 vs 0.124, 5: 0.301 vs 0.285, 6: 0.303 vs 0.331, 7: 0.179 vs 0.191, 8: 0.034 vs 0.044
top-12 missed patterns (miss count, ×avg): 132476598 (6, 67.1×), 984236571 (4, 44.8×), 421387659 (4, 44.8×), 978546123 (4, 44.8×), 895634217 (3, 33.6×), 893745162 (3, 33.6×), 892435617 (3, 33.6×), 985134627 (3, 33.6×), 314258976 (3, 33.6×), 128743659 (3, 33.6×), 154267389 (3, 33.6×), 129674583 (3, 33.6×)
among σ with M>0: fraction whose missing set contains an adjacent-transposition pair: 0.560; a dihedral-image pair: 0.063
cluster structure (adjacent-transposition graph on the missing set, σ with 0<M≤3000, 846 σ): mean M=38.34, mean #components=9.55, mean fraction of M in largest component=0.552; among σ with M≥10: mean #components=20.32, mean M=91.4


**k=9, n=64** (S=1000, Pr(M>0)=0.133, distinct patterns ever missed: 2210 of 362880, total misses 2226)
| feature | missing (weighted by miss count) | population S_k |
|---|---|---|
| LIS | 4.487 | 4.059 |
| LDS | 3.839 | 4.059 |
| max(LIS,LDS) | 4.925 | 4.647 |
| #monotone runs | 5.670 | 5.667 |
| #ascending runs | 4.705 | 5.000 |
| ⊕-decomposable | 0.542 | 0.247 |
| ⊖-decomposable | 0.188 | 0.247 |
| indecomposable (neither) | 0.270 | 0.507 |
max(LIS,LDS) distribution, missing vs population: 3: 0.001 vs 0.005, 4: 0.299 vs 0.452, 5: 0.505 vs 0.444, 6: 0.165 vs 0.091, 7: 0.029 vs 0.008, 8: 0.001 vs 0.000, 9: 0.000 vs 0.000
#monotone runs distribution, missing vs population: 1: 0.000 vs 0.000, 2: 0.002 vs 0.001, 3: 0.035 vs 0.024, 4: 0.097 vs 0.124, 5: 0.345 vs 0.285, 6: 0.236 vs 0.331, 7: 0.246 vs 0.191, 8: 0.038 vs 0.044
top-12 missed patterns (miss count, ×avg): 186723459 (2, 326.0×), 143265978 (2, 326.0×), 697823451 (2, 326.0×), 943278651 (2, 326.0×), 216975843 (2, 326.0×), 291583764 (2, 326.0×), 249685713 (2, 326.0×), 194352867 (2, 326.0×), 164532879 (2, 326.0×), 163452879 (2, 326.0×), 167342859 (2, 326.0×), 156342879 (2, 326.0×)
among σ with M>0: fraction whose missing set contains an adjacent-transposition pair: 0.391; a dihedral-image pair: 0.038
cluster structure (adjacent-transposition graph on the missing set, σ with 0<M≤3000, 133 σ): mean M=16.74, mean #components=4.60, mean fraction of M in largest component=0.661; among σ with M≥10: mean #components=13.92, mean M=73.1
