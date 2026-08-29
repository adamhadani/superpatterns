# W21 — half-probability containment thresholds n_½(π), k = 12 … 40

Question.  n_½(π) = the n at which a uniform random σ_n contains π with probability 1/2.  For the identity,
n_½/k² → 1/4 (LIS, Tracy–Widom).  Does the same limit hold for random π, or is lim n_½(π)/k² strictly below 1/4
(≈ 0.23, which would make the identity NOT the asymptotically easiest pattern and κ_univ > 2)?

Method (see README.md for commands, seeds, files).  Solver `contain_bc.c` (CSP with 2-D bounds consistency, cell
counting, per-cell LIS/LDS prune); validated with 56 000 per-sample comparisons against W16's `contain_gen`
(k ≤ 12, 0 mismatches) and 1 200 per-sample comparisons against an LIS oracle for the identity (k = 20..32,
0 mismatches).  For each (k, n) all patterns are tested on the same 2000 (k ≤ 32) / 1000 (k = 36) / 600 (k = 40)
uniform permutations; n_½ from a maximum-likelihood logistic fit on the points with 0.1 < p < 0.9, 95 % CI by
parametric bootstrap; `cross` = plain linear interpolation of the 1/2-crossing (model-free check).  Identity
thresholds are also computed from the LIS with 10^5 samples per point (`lis_thr.out`).  Random patterns:
`random.seed(100+k)` + successive shuffles (r_0..r_3 are W16's rand0..3); 8 patterns for k ≤ 32, 4 for k = 36, 40.

Speed: k = 32 ≈ 0.1 s/sample/pattern near threshold, k = 36 ≈ 0.3 s, k = 40 ≈ 1.5 s (contain_mrv would have
needed ≈ 100× more at k = 20 and was hopeless at k ≥ 28).

## 1. Identity: solver vs LIS (validation of the thresholds)

| k | n_½ solver (2000/pt) | n_½ LIS (10^5/pt) | n_½/k² |
|---|---|---|---|
| 12 | 52.24 [52.12, 52.39] | 52.16 [52.13, 52.19] | .3622 |
| 16 | 88.24 [88.07, 88.46] | 88.21 [88.17, 88.25] | .3446 |
| 20 | 132.68 [132.30, 133.08] | 132.89 [132.83, 132.94] | .3322 |
| 24 | 186.35 [185.93, 186.86] | 186.22 [186.15, 186.30] | .3233 |
| 28 | 248.10 [247.42, 248.76] | 248.03 [247.92, 248.14] | .3164 |
| 32 | 318.46 [317.86, 319.16] | 318.70 [318.56, 318.85] | .3112 |
| 36 | 401.0 [394.6, 410.8] (grid ends at p = .32) | 397.86 [397.68, 398.05] | .3070 |
| 40 | — | 485.72 [485.49, 485.93] | .3036 |
| 48 | — | 686.73 [686.42, 687.06] | .2981 |

Solver and LIS agree to within the CIs at every k (W16's k = 20 value 135.6 from 120 samples was 2 % high).

## 2. Random π: per-pattern thresholds

k = 12 (4000 samples/pt, n = 38..64 step 2), k = 16 (4000, n = 66..105 step 3), k = 20 (2000, n = 100..165 step 5),
k = 24 (2000, 145..215 step 5), k = 28 (2000, 195..265 step 5), k = 32 (2000, 250..340 step 6),
k = 36 (1000, 320..376 step 8), k = 40 (600, 400..460 step 12).  Only r_0..r_3 are listed per k; the mean/sd
use all 8 (k ≤ 32).

| k | r_0 | r_1 | r_2 | r_3 | mean over random π (sd; sem) | mean/k² | id (LIS) | ratio rand/id |
|---|---|---|---|---|---|---|---|---|
| 12 | 50.30 ±.12 | 50.03 ±.11 | 50.95 ±.12 | 49.49 ±.12 | 50.00 (0.49; 0.17) | .3472 | 52.16 | .9586 |
| 16 | 82.84 ±.17 | 82.22 ±.17 | 82.24 ±.17 | 82.70 ±.17 | 82.61 (0.49; 0.17) | .3227 | 88.21 | .9364 |
| 20 | 121.54 ±.33 | 122.83 ±.36 | 123.18 ±.37 | 125.77 ±.32 | 122.79 (1.34; 0.48) | .3070 | 132.89 | .9240 |
| 24 | 169.24 ±.35 | 169.84 ±.36 | 169.26 ±.35 | 170.96 ±.36 | 169.73 (0.59; 0.21) | .2947 | 186.22 | .9114 |
| 28 | 223.89 ±.38 | 224.43 ±.39 | 223.31 ±.37 | 222.47 ±.36 | 224.22 (1.38; 0.49) | .2860 | 248.03 | .9040 |
| 32 | 287.11 ±.47 | 284.49 ±.44 | 284.62 ±.46 | 285.40 ±.46 | 284.95 (0.93; 0.33) | .2783 | 318.70 | .8941 |
| 36 | 352.52 ±.9 | 355.09 ±1.0 | 351.39 ±.9 | 352.66 ±1.0 | 352.92 (1.56; 0.78) | .2723 | 397.86 | .8870 |
| 40 | 428.19 ±1.5 | 428.18 ±1.5 | 426.08 ±1.4 | 429.23 ±1.4 | 427.92 (1.32; 0.66) | .2675 | 485.72 | .8810 |

(± = half-width of the 95 % bootstrap CI.)  The threshold of a random pattern is strongly self-averaging: the
spread across random π is 0.3–1 % of n_½ at every k, far below the identity–random gap (7–13 %).
The transition is also sharper for random π (logistic width w ≈ 0.055 n_½) than for the identity (w ≈ 0.073 n_½).

Ratio n_rand/n_id vs k (12 … 36): .959 .936 .924 .911 .904 .894 .887 **.881** — monotone decreasing, no sign
of turning towards 1.  (W16 had .95 .97 .97 .97 .94 .90 for k = 8..20 from ≤ 500 samples; the new series
supersedes it.)

## 3. Fits of the k-dependence and implied limits

Four forms were fitted to n_½(k) (means over random π, k = 12..40; bootstrap CIs from the per-k sem, floor 0.3):
A: √n = a k + b k^{1/3} (Tracy–Widom form; limit a²);  B: n = c k² + d k;  C: n = c k² + d k^{4/3};
D: n = c k² + d k^{4/3} + e k^{2/3}.  The SAME forms fitted to the exact identity series (LIS, k = 12..48,
true limit 1/4) calibrate the finite-k bias of each form.

| form | identity (true limit .2500) | random π, k = 12..40 | random π, k = 16..40 |
|---|---|---|---|
| A: a² | .2585 [.2575, .2596], b = .497, rms .19 | .2092 [.2073, .2115], b = .706, rms .50 | .2077 [.2054, .2101], rms .36 |
| B: c | .2744 [.2737, .2749], d = 1.16, rms .71 | .2295 [.2278, .2312], d = 1.54, rms .86 | .2283 [.2263, .2303], rms .66 |
| C: c | .2553 [.2543, .2562], d = .564, rms .09 | .2008 [.1982, .2035], d = .780, rms .23 | .2004 [.1974, .2034], rms .20 |
| D: c | .2558 [.2523, .2595], rms .09 | .1947 [.1848, .2056], e = −.49, rms .12 | .1943 [.1800, .2084], rms .13 |

Every form puts the random-π limit 0.04–0.06 below the value the same form returns for the identity, whose
bias is upward (+.005 … +.024); a bias-corrected reading is c_rand ≈ 0.20–0.23 (form B, the least curved
correction, gives .230 − .024 = .21; form C gives .201 − .005 = .20; form A .209 − .009 = .20).

Direct diagnostics (means over random π):

| k | 20 | 24 | 28 | 32 | 36 | 40 |
|---|---|---|---|---|---|---|
| n_½ − k²/4 | 22.8 | 25.7 | 28.2 | 29.0 | 28.9 | 27.9 |
| (n_½ − k²/4)/k | 1.14 | 1.07 | 1.01 | 0.905 | 0.803 | 0.698 |
| (n_½ − k²/4)/k^{4/3} | .420 | .372 | .332 | .285 | .243 | .204 |
| identity: (n_½ − k²/4)/k^{4/3} | .606 | .610 | .612 | .617 | .621 | .627 |

For the identity the excess over k²/4 grows like 0.6 k^{4/3} (Tracy–Widom, coefficient slowly rising towards its
limit).  For random π the excess over k²/4 has STOPPED GROWING at k ≈ 32–36 (≈ 29 permutation points) and decreases at k = 40: a limit
of 1/4 would require the finite-size correction to be positive but bounded (or to turn negative) — i.e. a
correction of the form d k − e k^{4/3} with e > 0.  Forcing c = 1/4 and fitting n − k²/4 = d k + e k^{4/3} on
k ≥ 24 indeed gives e = −0.60 (d = 2.8); with e = 0 (n = k²/4 + d k) the fit has rms 4.5 (vs 0.2–0.9 for the free forms).
With the leading constant free, a linear-in-k correction (form B) fits with c = 0.228–0.230 and every simpler
form agrees on c ∈ [0.19, 0.23].

### 3a. Log-log analysis (coordinator/W25 request): slope of log(n_½/k² − c) vs log k

If lim n_½/k² = c with a Tracy–Widom-type finite-size correction, n_½/k² − c ∝ k^{−2/3}, i.e. slope −2/3.

| series | slope at c = 1/4 (rms) | c at which slope = −2/3 | slope at c = .20 / .22 / .23 / .24 |
|---|---|---|---|
| identity, LIS, k = 12..48 (control) | −0.617 (.003) | .220 | −.37 / −.44 / −.48 / −.54 |
| identity, LIS, k = 20..40 (control) | −0.619 (.002) | .220 | −.35 / −.43 / −.48 / −.54 |
| random π mean, k = 12..40 | −1.41 (.082) | .2025 | −.65 / −.82 / −.95 / −1.13 |
| random π mean, k = 20..40 | −1.69 (.045) | .2000 | −.67 / −.87 / −1.04 / −1.28 |
| single patterns r_0..r_3, k = 20..40, c = 1/4 | −1.60, −1.65, −1.80, −1.81 (rms .02–.07) | | |

Control: the identity gives slope −0.62 at its true limit — close to −2/3 (the 7 % shortfall is the known
sub-leading term; it also makes the "c with slope −2/3" estimator biased LOW by 0.03).  Random π at c = 1/4
gives slope −1.4 to −1.8, steepening with k, with a poor fit (rms 0.05–0.08 vs 0.002–0.003 for the identity
and 0.002–0.005 for the random series at c ≈ 0.20): the random-π data are NOT compatible with a k^{−2/3}
approach to 1/4.  A TW-type approach is restored at c ≈ 0.20 (bias-corrected by the control: ≈ 0.23).
Conclusion of the re-analysis: the finite-size exponent, not just the value at k = 40, separates the two
hypotheses; the identity behaves as TW predicts, the random patterns do not approach 1/4 at that rate.

## 4. Structured patterns

| k | identity | decreasing | layered (21)^{k/2} | dec-half (k..k/2+1, then random) | tilted √k×√k grid | random r_0 |
|---|---|---|---|---|---|---|
| 20 | 132.7 ±.4 | 133.1 ±.4 | 132.8 ±.4 | 130.5 ±.4 | — | 121.5 ±.3 |
| 24 | 186.3 ±.5 | 186.0 ±.5 | 186.9 ±.5 | 184.5 ±.4 | — | 169.2 ±.4 |
| 25 | 200.9 ±.5 | 200.9 ±.5 | — | — | 180.8 ±.4 (5×5) | 182.5 ±.4 |
| 36 | 397.9 (LIS) | — | — | — | 350.4 ±.9 (6×6) | 351.8 ±.9 |

- decreasing = identity (as the reflection symmetry requires; a check of the solver's symmetry-independence).
- The layered pattern (21)^{k/2} (LIS = k/2, LDS = 2) is as hard as the identity: n_½ = 132.8 vs 132.7 at k = 20,
  186.9 vs 186.3 at k = 24 (if anything marginally harder).
- The tilted grid (LIS = LDS = √k) sits exactly with the random patterns (180.8 vs 182.5 at k = 25;
  350.4 vs 351.8 at k = 36), i.e. patterns with balanced small LIS/LDS are as easy as random ones.
- dec-half (LDS ≥ k/2) is only 1–1.6 % easier than the identity (130.5 vs 132.7 at k = 20; 184.5 vs 186.3 at
  k = 24): a monotone run of length k/2 already dominates the threshold.
So the identity and the layered patterns are the hard (n_½/k² ≈ .31–.33) family, random and grid-like patterns
the easy one (≈ .27–.28 at k = 32–36), and the gap is widening with k.

## 5. Verdict

Decided at the level a numerical experiment can decide, in favour of "strictly below 1/4":
1. n_rand/n_id decreases monotonically from .959 (k = 12) to .881 (k = 40) with sem ≲ 0.003.
2. n_rand − k²/4 has stopped growing (28.2, 29.0, 28.9, 27.9 at k = 28, 32, 36, 40 — it has started to decrease), whereas any limit of 1/4 with a
   positive TW-type correction needs it to grow like k^{4/3} (the identity's does: 0.6 k^{4/3}).
3. The log-log slope at c = 1/4 is −1.3 … −1.8 and steepening (identity control: −0.62 ≈ −2/3); the value of
   c that makes the random series TW-like is 0.20 (bias-corrected ≈ 0.23).
4. Every free-constant form gives c_rand ∈ [0.19, 0.23], 0.04–0.06 below what the same form gives for the
   identity (whose true limit is 1/4).
Best estimate: lim n_½(random π)/k² ≈ 0.22 ± 0.02 (κ_univ ≈ 1/√0.22 ≈ 2.13, > 2).

What is NOT excluded: lim = 1/4 with a correction that is positive at k ≤ 40 but eventually negative
(n = k²/4 + d k − e k^{4/3} + …, e ≈ 0.7).  No finite-k experiment can rule this out; but it would require the
random patterns' n_½ to CROSS k²/4 from above around k ≈ 60–70 and then approach k²/4 from below — under the
fitted forms that is the only escape.  To make it visible, n_½ at k = 64 (predicted 0.96 k²/4 ≈ 985 under
c = .23 vs ≥ 1024 + O(k) under c = 1/4, a 4–5 % difference, far above the ≈ 0.3 % statistical error) would be
decisive; contain_bc costs ≈ 1.5 s/sample at k = 40 and grows ≈ 5× per +4 in k, so k = 48 (≈ 15 s/sample,
≈ 1 CPU-day for 4 patterns × 500 samples × 6 n) is feasible, k = 64 is not with this solver.
