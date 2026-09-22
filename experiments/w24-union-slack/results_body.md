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
   ≈ 3× average at k=8), but they carry a small share of the total: at k=9, n=60, about 30000 distinct patterns
   (8% of S_9) appear among the ≈ 32000 misses of 2000 samples, and the top-12 together are < 0.2% of them.  Deeper in the tail the missing set becomes
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
