# W30 — results: what one empty rectangle does to the missing set

All numbers from `analysis.txt` (= `python3 analyze.py 6,27 6,28 7,37`), raw lines in `out/`. Notation (proof.md):
Q₁ = largest maximal empty rectangle of σ (area A₁ = w·h cells of [n]²), K_c(Q) = # missing patterns revived by one
phantom point at the centre slot of Q, K_any(Q₁) = revived by *some* point of Q₁, K_rand = revived by a phantom at a
uniformly random slot, K_g = revived by each of 9 phantoms on a 3×3 grid, ρ(π) = fraction of the board that revives π.
Samples: k=6 n=27 (6000 σ), k=6 n=28 (6000 σ), k=7 n=37 (700 σ; run was slowed by machine load ≈ 11, see log.md).
k=8 n=48 did not finish (≈ 1 min per σ at C(48,7) = 7·10⁷ subsets per phantom; no output within the time budget).

## 1. Attribution of M to the largest defect (task 1) — NUMERICAL

| | k=6, n=27 | k=6, n=28 | k=7, n=37 |
|---|---|---|---|
| P(M>0), E M, E[M | M>0] | 0.541, 4.04, 7.5 | 0.411, 2.43, 5.9 | 0.480, 5.68, 11.8 |
| Σ K_any(Q₁) / Σ M | 0.995 | 0.997 | 0.997 |
| Σ K_c(Q₁) / Σ M  (mean of K_c/M) | 0.736 (0.767) | 0.739 (0.785) | 0.784 (0.785) |
| Σ K_c(top-8 union) / Σ M | 0.979 | 0.980 | 0.987 |
| **Σ K_rand / Σ M  (mean of K_rand/M)** | **0.413 (0.468)** | **0.439 (0.468)** | **0.405 (0.436)** |
| 1 − μ(n+1)/μ(n) from W24 dumps (Prop. 2.1 predicts Σ K_rand/Σ M) | 0.415 | ≈ 0.45 (μ(29) not in W24; geometric mean of the n=28→30 pair) | 0.403 |
| 3×3 grid: mean K_g/ΣM over the 9 points (corners / centre) | 0.420 (0.434 / 0.390) | 0.437 (0.464 / 0.426) | 0.417 (0.414 / 0.410) |
| best of the 9 grid points / M | 0.956 | 0.972 | 0.949 |
| P(K_c(Q₁) = M), P(K_c(Q₁) = 0), P(K_rand = 0) | 0.50, 0.09, 0.30 | 0.56, 0.09, 0.34 | 0.47, 0.08, 0.33 |
| revival multiplicity of a missing π (# of the 9 grid phantoms reviving it): mean, P(=0) | 3.78, 0.006 | 3.94, 0.004 | 3.79, 0.005 |
| same, for π in events with M ≥ 30 | 3.34 | 3.54 | 3.62 |

Readings. (i) "Some point of Q₁ revives π" holds for 99.5–99.7 % of all missing patterns — vacuous (Cor. 1.3(b)).
(ii) A *random* point revives 41–44 % of the missing patterns, exactly as Prop. 2.1 predicts from the slope of μ;
the centre of the largest empty rectangle revives 74–79 %; nine fixed grid points together revive 95–97 %. So the
revival region of a typical missing pattern covers ≈ 42 % of the board (mean multiplicity 3.8/9), slightly less for
patterns in big clusters (3.3–3.6/9). The largest defect is only ≈ 1.8× better than a random location.
(iii) By M-bin (analysis.txt): K_c(Q₁)/M is flat, 0.77–0.81 at k=7 and 0.69–0.79 at k=6, for M from 1 to > 100;
K_rand/M decreases slowly (0.51 → 0.21 at k=6, 0.44 → 0.38 at k=7 for M=1 → M ≥ 30).

## 2. M and K against the size/shape of the defect (task 1) — NUMERICAL

Spearman(M, A₁) = 0.40 / 0.35 / 0.36 (k=6 n=27 / k=6 n=28 / k=7 n=37; W28 had 0.42 at k=7); Spearman(M, min(w,h)) =
0.20 / 0.18 / 0.18; Spearman(M, max(w,h)) = 0.08 / 0.07 / 0.08. The short side of Q₁ carries the signal, the long side none.

E[M | A₁/n² in bin] (k=7 rows: 560-sample snapshot; analysis.txt has the 700-sample version, same to within 15 %) versus the PROVED bound μ(n − min(w,h)) of Prop. 3.2 (μ interpolated from W24 + out/mu_small.txt):

| k, n | A₁/n² bin (quantiles 0–20–40–60–80–90–97–100 %) | P(M>0) | E M | mean min(w,h) | μ(n − min(w,h)) | ratio bound/E M |
|---|---|---|---|---|---|---|
| 6, 27 | 0.08–0.12 | 0.29 | 0.93 | 6.5 | 78 | 84 |
| | 0.12–0.125 | 0.41 | 1.7 | 7.1 | 94 | 55 |
| | 0.125–0.14 | 0.55 | 3.0 | 7.4 | 105 | 35 |
| | 0.14–0.15 | 0.60 | 3.8 | 7.8 | 122 | 32 |
| | 0.15–0.165 | 0.70 | 6.2 | 8.5 | 150 | 24 |
| | 0.165–0.18 | 0.81 | 9.5 | 9.3 | 184 | 19 |
| | 0.18–0.25 | 0.94 | 19.1 | 10.1 | 234 | 12 |
| 7, 37 | 0.08–0.10 | 0.19 | 0.6 | 8.2 | 212 | 330 |
| | 0.10–0.11 | 0.52 | 2.9 | 8.5 | 236 | 81 |
| | 0.11–0.12 | 0.42 | 3.3 | 9.3 | 310 | 95 |
| | 0.12–0.13 | 0.57 | 7.0 | 9.9 | 388 | 56 |
| | 0.13–0.14 | 0.62 | 9.1 | 10.6 | 506 | 55 |
| | 0.14–0.15 | 0.80 | 15.1 | 11.8 | 722 | 48 |
| | 0.15–0.18 | 0.91 | 24.0 | 12.4 | 855 | 36 |

E M grows by a factor 20 (k=6) / 37 (k=7) from the smallest to the largest A₁ decile; ln E M against mean min(w,h)
has slope ≈ 0.85 (k=6) / 0.85 (k=7) per unit of min(w,h), compared with the slope 0.4–0.55 of ln μ(n) per point
(the bound). The bound is loose by 12–330× but has the right functional form (exponential in the short side).
Mean A₁/n² = 0.136 (n=27), 0.116 (n=37), versus ln n/n = 0.122, 0.098: the largest empty rectangle has area ≈ n ln n
cells, so min(w,h) ≤ √(n ln n) ≈ 9.4 (n=27), 11.6 (n=37); observed mean min(w,h) = 7.6 / 9.8.

Scaling of K with the area a = A/n² and with k (per rectangle, the 8 largest maximal empty rectangles of every σ with M>0;
25 960 rectangles at k=6 n=27, 2 120 at k=7 n=37):

| a = A/n² bin | k=6 n=27: mean K_c, P(K_c>0), mean K_c/M | k=7 n=37: mean K_c, P(K_c>0), mean K_c/M |
|---|---|---|---|
| lowest 10 % (0.075–0.10 / 0.07–0.087) | 2.0, 0.83, 0.735 | 2.5, 0.79, 0.67 |
| 10–30 % | 3.2, 0.87, 0.742 | 4.5, 0.89, 0.74 |
| 30–50 % | 4.2, 0.90, 0.742 | 6.2, 0.93, 0.80 |
| 50–70 % | 5.3, 0.92, 0.764 | 8.9, 0.91, 0.75 |
| 70–90 % | 6.8, 0.94, 0.765 | 12.9, 0.94, 0.78 |
| 90–97 % | 9.1, 0.96, 0.780 | 18.6, 0.91, 0.74 |
| top 3 % (0.166–0.25 / 0.143–0.17) | 16.5, 0.98, 0.781 | 19.5, 0.96, 0.83 |
| Spearman(K_c, a) / Spearman(K_c/M, a) | 0.31 / −0.03 | 0.34 / −0.05 |
| by aspect ratio min/max ∈ [0,.2), [.2,.4), [.4,.6), [.6,.8), [.8,1]: mean K_c/M | 0.67, 0.72, 0.76, 0.78, 0.78 | 0.60, 0.71, 0.77, 0.79, 0.81 |

**Verdict on scaling.** K_c(Q) = (0.75 ± 0.05)·M for every rectangle in the top-8, independently of its area over
the whole observed range (a = 0.07–0.25) and nearly independently of its aspect ratio (elongated rectangles revive a
little less, 0.60–0.67). K grows with a only through M: E K_c ∝ E[M | a] ≈ e^{0.85·min(w,h)}. Across k the revival
fractions are the same at k = 6 and 7 (K_c/M = 0.74–0.79, K_rand/M = 0.41–0.44, grid mean 0.42), i.e. the *fraction*
of the missing set revived by a point is k-independent at these sizes; the *number* K_c inherits the growth of M:
ln(max K_c(Q₁))/k = 0.76 / 0.72 / 0.68 (k=6 n=27 / 6,28 / 7,37; max K_c = 98, 76, 113), ln(mean K_c | M>0)/k = 0.28 / 0.25 / 0.31.
No k=8 point could be obtained, so the growth ln K/k ≈ 0.3 (mean) – 0.7 (max) cannot be separated from k ln k here.

## 3. Deterministic extreme (task 2(iii)) — NUMERICAL (`witness_phantom.py`)

σ = sp(6)=17 witness, k=7: N₆ = 720 (all), N₇ = 3502/5040. One added point revives K_x = 635 = 0.88·6! missing
7-patterns at the best of the 324 slots (mean over slots 341, min 102); ln K_max/(k ln k) = 0.47. So for a rigid σ one
point can carry Θ((k−1)!) patterns; the conjecture is meaningful only for typical σ (proof.md §4).

## 4. Verdict

1. The working question "how many patterns does one empty rectangle kill" has, in the typical regime, the answer
   **K(Q) ≈ 0.75·M for every large empty Q, and ≈ 0.42·M for a random point** (Prop. 2.1 makes the latter exact in
   expectation: 1 − μ(n+1)/μ(n)). A missing pattern's revival region is ≈ 42 % of the board. So the number of patterns
   killed by a defect is not a new quantity with its own growth rate: it is a constant fraction of M, and the
   e^{O(k)} vs e^{Θ(k ln k)} question is unchanged — it is the tail of M | M>0 (W28 H4).
2. The defect statistic that matters is the **short side** min(w,h) of the largest empty rectangle (Spearman 0.2 vs
   0.08 for the long side; E M ≈ e^{0.85·min(w,h)}), consistent with the PROVED bound E[M | Q empty] ≤ μ(n − min(w,h))
   (Prop. 3.2), which is the first rigorous inequality of the "defect ⇒ missing patterns" type in the programme.
   It is loose by 12–300× and gives e^{O(k√ln k)}·μ for the typical largest defect only under the unproved uniform
   slope s(n) = O(1) (rigorously only e^{O(k ln^{3/2} k)}, Lemma 3.3).
3. The conjecture cannot be deterministic (§3: 0.88·(k−1)! patterns through one point of a minimal superpattern).
