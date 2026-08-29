# W33 — results (all numbers reproducible from files in this directory)

## 1. Per-pattern slopes s_π(n) = ln p_π(n−1) − ln p_π(n)  (SMC, generating-tree survival; out/analysis.txt)
Identity, exact (hook lengths, out/lis_k*.txt), and the k→∞ closed form ln((4C+1)²/(16C)) of proof.md §3:

| C = n/k² | k=4 | k=5 | k=6 | k=7 | k=8 | k=9 | k=10 | a+b/k fit (k=9,10) | limit formula |
|---|---|---|---|---|---|---|---|---|---|
| 0.50 | 0.337 | 0.264 | 0.239 | 0.221 | 0.214 | 0.197 | 0.193 | 0.157 | 0.118 |
| 0.75 | 0.600 | 0.486 | 0.485 | 0.449 | 0.427 | 0.412 | 0.397 | 0.255 | 0.288 |
| 1.00 | 0.813 | 0.735 | 0.674 | 0.630 | 0.612 | 0.592 | 0.576 | 0.435 | 0.446 |
| 1.50 | 1.142 | 1.075 | 1.011 | 0.955 | 0.908 | 0.876* | – | – | 0.693 |
(*k=9 at n=120: C=1.48; n = round(Ck²) throughout.)  E[S_max] = n e^{−s} → 16k²n²/(4n+k²)² (= n at C=1/4, → k² as C→∞).

All patterns (SMC, mean over seeds; SMC vs exact agreement ±0.01 at k=4, n ≤ 11):

| k | pattern (class rep.) | C=0.5 | C=0.75 | C=1 | C=1.25 | C=1.5 | I_π(1) = −ln p/n at n=k² |
|---|---|---|---|---|---|---|---|
| 4 | 1234 (=1243,1432,2143) | 0.336 | 0.600 | 0.810 | 0.993 | 1.149 | 0.369 |
| 4 | 1324 | 0.340 | 0.590 | 0.788 | 0.959 | 1.107 | 0.364 |
| 4 | 1342 (=2413) | 0.351 | 0.629 | 0.856 | 1.031 | 1.190 | 0.387 |
| 5 | 12345 | 0.271 | 0.535 | 0.744 | 0.902 | 1.096 | 0.316 |
| 5 | 13254 (min) | 0.259 | 0.527 | 0.715 | 0.846 | 0.964 | 0.310 |
| 5 | 14325 | 0.259 | 0.530 | 0.692 | 0.845 | 1.015 | 0.308 |
| 5 | 13452 (max) | 0.281 | 0.581 | 0.814 | 1.023 | 1.217 | 0.341 |
| 5 | all 23 classes: range | 0.26–0.28 | 0.52–0.58 | 0.69–0.81 | 0.85–1.02 | 0.96–1.22 | 0.31–0.34 |
| 6 | 123456 | 0.247 | 0.474 | 0.677 | 0.755 | 0.908 | 0.281 |
| 6 | 215436 (min, layered) | 0.246 | 0.440 | 0.626 | 0.799 | 0.929 | 0.263 |
| 6 | 246135 (max, generic) | 0.279 | 0.574 | 0.823 | 1.023 | – | 0.330 |
| 6 | 16 patterns: range | 0.24–0.28 | 0.44–0.57 | 0.63–0.82 | 0.76–1.02 | 0.91–1.05 | 0.26–0.33 |
| 7 | see out/analysis.txt (filled in as the runs finish) | | | | | | |

Findings (NUMERICAL): (i) at fixed (k, C) the slope varies by ≤ ±15 % over S_k — the identity is typical, slightly
below the median; layered patterns have the smallest slope, generic ones the largest; (ii) s_π(n) is increasing in n
for every pattern and every n ≥ k (log-concavity of p_π in the window); (iii) at fixed C the slope decreases in k with
O(1/k) corrections, parallel to the exact identity values, i.e. no sign of a ln k growth: the ln(n/(k−1)) upper bound
of proof.md Lemma 1.1 is far from tight; (iv) the rates I_π(1) are 0.26–0.39, decreasing in k — consistent with
p_π(k²) = e^{−Θ(k²)} with a bounded constant, i.e. with the window-averaged slope being O(1) for every π (Thm 2.3(ii)).

## 2. μ-slope s_μ(n) = ln μ(n−1) − ln μ(n) from the W24 dumps (out/mu_slopes.txt; per unit n, between the listed n)
| k | below threshold (μ ≈ 10²–10³) | at threshold (μ ≈ 1–10) | above (μ ≈ 0.1–1) |
|---|---|---|---|
| 5 | 0.45 (n 15→16) | 0.48–0.62 (16→20) | 0.63–0.71 (20→24) |
| 6 | 0.44–0.47 (22→26) | 0.54–0.59 (26→30) | 0.57–0.78 (30→34) |
| 7 | 0.37–0.50 (29→35) | 0.44–0.55 (35→40) | 0.66–0.69 (40→44) |
| 8 | 0.37–0.47 (38→46) | 0.46–0.59 (46→52) | 0.67 (52→55) |
| 9 | 0.30–0.51 (49→58) | 0.44–0.53 (58→64) | 0.41 (64→68, 53 events) |
s_μ is ≈ 0.5 at the threshold for every k = 5..9 (flat in k), increasing in n; it exceeds the identity's slope at the
same n (0.40 at k = 9, C = 0.74) because μ is a p_π(n−1)-weighted average of e^{s_π} and the late-missing patterns are
those with steeper current slope. Cross-check: W30 measured revival fraction 0.40 at k=6, n=27 = 1 − e^{−0.536·…}: 1 − μ(28)/μ(27) = 0.415 ✓.

## 3. What is proved (proof.md)
- Lemma 1.1: s_π(n) ≤ ln(n/(k−1)) for all π ∈ S_k, n > k (improves W30 Lemma 3.3 by ln(k−1)); three exact forms of the ratio.
- Thm 2.1: a uniform lower bound s_π ≥ s_0 on [ck², Ck²] implies CP* and Alon's conjecture at n = Ck² — so it is
  not a lemma but the theorem itself.
- Prop 2.2: the average μ-slope over any window of length εk² ending at t(k) is ≤ (1+o(1)) ln k/(εk) → 0 (μ ≤ k!); the
  Θ(1) slope needed by W28 Cor 1.2 can only hold on the last O(k ln k) points before the threshold, and that is all
  Cor 1.2 needs (n_1 − n_0 ≤ (ak + ln 2)/s_0).
- Thm 2.3: pointwise upper bound over the window ⟹ p_π(Ck²) ≥ ½e^{−A(C−1/6)k²}; window-averaged upper bound ⟺
  I_π(C) = O(1); for μ the window average is ≤ H_0(1/√C) + o(1) unconditionally (via p_id).
- Prop 3.3: identity slope s_id → 2 ln((4+x²)/(4x)) = ln((4C+1)²/(16C)), x = k/√n, with the LIS lower-tail rate
  H_0(x) = −1 + x²/4 + (x²/2) ln((4+x²)/(2x²)) + 2 ln((4+x²)/(4x)) — from the Poissonized Gessel determinant
  (numerical input −d ln Q/dλ = (1−y/2)², 4 digits) plus de-Poissonization; passes the x→0, TW-cubic and Regev checks.
- Prop 4.1: s_π(n) ≤ ln n − ln E[τ_α + τ'_β − 1 | Av_{n−1}(π)] (prefix/suffix hitting times of the sub-patterns left and
  right of the maximum of π): the pointwise O(1) bound reduces to "a random π-avoider needs Θ(n) points before its
  prefix contains α", which holds for the identity by Prop 3.3(v).

## 4. Consequences for W28 / W30
- HEURISTIC warning (proof.md Prop 2.5): the Θ(1) slope at the threshold is pre-asymptotic. For the identity the
  slope at the point p_id = 1/k! is 0.44, 0.22, 0.08, 0.025 at k = 10, 10², 10³, 10⁴ (exact formula), i.e. Θ((ln k/k)^{2/3});
  the same scaling is expected for the patterns carrying μ at t(k) unless their rate function has a kink at the
  threshold. Cor 1.2 of W28 then needs Λ_π ≤ e^{ak} with a = o(k^{1/3} ln^{2/3} k) rather than o(k); a = O(1)
  (the observed R = e^{0.7k}) still gives n_1 − n_0 = O(k^{5/3}) = o(k²).
- W28 Cor 1.2's "ln μ decreases by Θ(1) per unit n near the threshold": NUMERICAL yes (≈ 0.5 for k ≤ 9, flat in k),
  PROVED no; it is a scale-k statement (Prop 2.2), not a scale-k² one. W28 §4 (H5) used c' from the naive DZ rate;
  the identity's actual per-point slope at C = 3/4 is 0.29 (k→∞), 0.40–0.60 at k = 4..9.
- W30 Cor 3.4's "slope O(1) uniformly in k ⇒ e^{O(k√ln k)}": the required bound is pointwise in n; the best proved is
  ln(n/(k−1)) ≈ ln(Ck) (⇒ e^{O(k ln k · √ln k)}… i.e. the same e^{O(k ln^{3/2} k)} up to constants). The numerics
  (slopes decreasing in k at fixed C, uniform over π) support the O(1) statement with A ≈ e^{0.6} ≈ 1.8 at C ≤ 1.
