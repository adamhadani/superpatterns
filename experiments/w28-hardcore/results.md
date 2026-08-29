# W28 — results: hard-core / cluster structure of the missing set (k = 6, 7; k = 8, 9 for tails)

All numbers from the W24 dumps (`../w24-union-slack/out/k{K}_n{N}_s11.txt`), scripts in this directory
(`hardcore.py`, `hardest.py`, `bigM.py`, `tail.py`), raw tables in `out/`. Notation as in proof.md:
p_π = Pr(π ⊄ σ_n), μ = Σ p_π = E M, Δ = E M(M−1), R = μ/Pr(M>0) = E[M|M>0], Λ_π = E[M | π ⊄ σ_n].

## Table 1 (Task 1) — law of M vs Janson / Bonferroni / second moment   (`out/k6.txt`, `out/k7.txt`)

k = 6 (t(6) ≈ 28):

| n | n/k² | Pr(M=0) | μ | Δ/μ | ln Pr(M=0)/(−μ) | Bonf. order 2: μ−E C(M,2) | order 3 | μ²/E M² | R | E M²/μ | max_π Λ_π |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 22 | 0.61 | 0.011 | 43.3 | 86 | 0.104 | −1820 | 7.9e4 | 0.498 | 43.8 | 87 | 121 |
| 24 | 0.67 | 0.105 | 17.9 | 51.7 | 0.127 | −444 | 1.3e4 | 0.338 | 19.9 | 52.7 | 87 |
| 26 | 0.72 | 0.320 | 7.03 | 32.8 | 0.162 | −108 | 2630 | 0.208 | 10.3 | 33.8 | 61 |
| 28 | 0.78 | 0.586 | 2.41 | 19.8 | 0.222 | −21.5 | 351 | 0.116 | 5.81 | 20.8 | 37 |
| 30 | 0.83 | 0.799 | 0.74 | 10.8 | 0.303 | −3.3 | 30.9 | 0.063 | 3.68 | 11.8 | (66, few ev.) |
| 32 | 0.89 | 0.919 | 0.24 | 7.2 | 0.357 | −0.62 | 3.7 | 0.029 | 2.92 | 8.2 | — |
| 36 | 1.00 | 0.992 | 0.013 | 2.4 | 0.657 | −0.003 | 0.04 | 0.004 | 1.53 | 3.4 | — |
| 40 | 1.11 | 0.9994 | 0.0007 | 0.3 | 0.846 | 0.0006 | 0.0006 | 0.0005 | 1.18 | 1.3 | — |

k = 7 (t(7) = 37):

| n | n/k² | Pr(M=0) | μ | Δ/μ | ln Pr(M=0)/(−μ) | Bonf. 2 | Bonf. 3 | μ²/E M² | R | E M²/μ | max_π Λ_π (≥20 ev.) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 29 | 0.59 | 0.003 | 201 | 433 | 0.028 | −4.3e4 | 1.1e7 | 0.462 | 201 | 434 | 658 |
| 33 | 0.67 | 0.104 | 45.0 | 214 | 0.050 | −4770 | 8.6e5 | 0.209 | 50.2 | 215 | 439 |
| 35 | 0.71 | 0.295 | 16.4 | 134 | 0.074 | −1080 | 1.5e5 | 0.122 | 23.3 | 135 | 158 (97 π) |
| 37 | 0.76 | 0.518 | 6.13 | 76.7 | 0.107 | −229 | 1.5e4 | 0.079 | 12.7 | 77.7 | 173 |
| 40 | 0.82 | 0.817 | 1.28 | 45.5 | 0.157 | −27.9 | 1050 | 0.028 | 7.03 | 46.5 | — |
| 44 | 0.90 | 0.969 | 0.086 | 11.3 | 0.365 | −0.40 | 6.9 | 0.007 | 2.78 | 12.3 | — |
| 48 | 0.98 | 0.995 | 0.0087 | 2.6 | 0.530 | −0.003 | 0.019 | 0.002 | 1.89 | 3.6 | — |
| 52 | 1.06 | 0.9997 | 0.0003 | 0 | 1.000 | 0.0003 | 0.0003 | 0.0003 | 1.0 | 1.0 | — |

Readings. (i) Pr(M=0) sits far ABOVE e^{−μ}: ln Pr(M=0)/(−μ) = 0.22 (k=6) and 0.11 (k=7) at t(k), rising to 1 only
where μ ≪ 1 (n ≥ 1.05k²); as a function of n/k² it decreases with k at fixed n/k² (0.16 vs 0.05 at n/k² = 0.67–0.72).
(ii) Janson e^{−μ+Δ/2} > 1 at every n with μ > 0.001 (Δ/μ ≫ 2); Bonferroni order 2 is negative and order 3 exceeds 1
for all n ≤ 0.9k² — the sieve is useless (heavy-tailed M). (iii) The second-moment bound Pr(M>0) ≥ μ²/E M² is the only
classical bound that is nontrivial: it gives R ≤ E M²/μ, i.e. ln R ≤ 3.0 / 4.35 / 5.5 / 6.1 (k=6..9 at t(k)) vs actual
1.76 / 2.54 / 3.1 / 3.65 (`out/` of tail.py). Both grow roughly linearly in k over this range.

## Table 2 (Task 2) — no hard core   (`out/k6_n28_hardest.txt`, `out/k7_n37_hardest.txt`, Task-2 blocks of `out/k*.txt`)

| | k=6, n=28 | k=7, n=37 | uniform |
|---|---|---|---|
| range of p_π / mean p_π (patterns with ≥20 events) | 0.45 – 1.90 | 0.82 – 2.88 | 1 |
| share of μ from top 1 % / top 10 % of patterns | 0.018 / 0.158 | 0.024 / 0.179 | 0.01 / 0.10 |
| p_id / max_π p_π | 0.74 | 0.86 | — |
| E_p[LIS], E_p[LDS] (p-weighted) | 3.15, 3.16 | 3.50, 3.48 | 3.14 (k=6), 3.47 (k=7) |
| E_p[max(LIS,LDS)] | 3.71 | 4.09 | 3.65 / 4.02 |
| E_p[#monotone runs] | 3.62 | 4.28 | 3.67 / 4.33 |
| E_p[adjacent-transposition distance to nearer of id, rev] | 5.10 | 7.42 | 5.33 / 7.80 |
| share of μ from max(LIS,LDS) ≥ k−1 | 0.091 | 0.022 | 0.072 / 0.015 |
| share of μ from max(LIS,LDS) ≥ k−2 | 0.61 | 0.22 | 0.575 / 0.182 |
| mean (max/min p) within a dihedral class | 1.28 | 1.52 | 1 |
| p_π by class max(LIS,LDS) = k, k−1, k−2, … (relative to mean) | 1.47, 1.25, 1.03, 0.92 | 2.26, 1.48, 1.18, 0.98, 0.86 | 1 |

Hardest patterns (k=7, n=37, ≈ 2.5–2.9× mean): 7456231, 7234561, 1543276, 7634512, 7564231, 2136547, 6723451, 1432576 —
layered / co-layered ("monotone with reversed blocks"), NOT the identity. Easiest (0.82×): generic, e.g. 5641273, 4352716.
Verdict: μ is spread over all of S_k within a factor ≈ 4; near-monotone patterns are only marginally harder
(class k−1: 1.25–1.5× mean). There is no hard core in the sense "a small set of patterns carries E M".

## Table 3 — conditional structure given M>0   (`out/k*.txt` Task-2 cluster block; `out/*_bigM.txt`; `out/*_hardest.txt` null block)

Clustering vs null (random subsets of S_k of the same size), n = t(k):

| | k=6 actual | k=6 null | k=7 actual | k=7 null |
|---|---|---|---|---|
| # components under adjacent transpositions | 3.2 | 5.4 | 5.8 | 11.2 |
| # components under one-point moves (share a (k−1)-child) | 1.19 | 2.5 | 1.37 | 5.5 |
| largest one-point component / M | 0.94 | 0.69 | 0.92 | 0.51 |
| greedy # of (k−1)-patterns covering the missing set | 2.1 | 3.8 | 3.6 | 8.0 |
| same four numbers, events with M ≥ 10 | 8.0 / 1.10 / 0.99 / 5.1 | 18 / 3.8 / 0.70 / 10.6 | 13.9 / 1.41 / 0.96 / 7.9 | 30.5 / 12 / 0.30 / 20 |

P(cover = 1 | M>0) = 0.51 (k=6), 0.37 (k=7) with E[M | cover=1] = 1.5–1.6; E[M | cover ≥ 2] = 10 / 19.

Anatomy by size of M (k=7, n=37; `out/k7_n37_bigM.txt`): share of Σ M (= share of R), fully-missing (k−1)-patterns,
fraction of the missing set inside their up-sets, mean max(LIS,LDS) of the missing patterns, greedy cover / M:

| M | #events | share of R | # fully missing τ ∈ S_6 | frac. of M explained | mean max(LIS,LDS) | cover/M |
|---|---|---|---|---|---|---|
| 1 | 2421 | 0.020 | 0 | 0 | 4.29 | 1 |
| 2–3 | 2122 | 0.041 | 0 | 0 | 4.22 | 0.66 |
| 4–9 | 2358 | 0.114 | 0 | 0 | 4.19 | 0.50 |
| 10–29 | 1787 | 0.243 | 0 | 0 | 4.14 | 0.35 |
| 30–99 | 773 | 0.329 | 0.03 | 0.014 | 4.08 | 0.24 |
| 100–299 | 165 | 0.210 | 0.46 | 0.093 | 4.00 | 0.16 |
| ≥ 300 | 14 | 0.044 | 3.9 | 0.32 | 4.06 | 0.12 |

Verdict: the missing set given M>0 is ONE diffuse connected cluster in the one-point-move graph, it is not the
up-set of missing (k−1)-patterns (the hierarchical "one (k−1)-pattern fails and drags its k² extensions" model is
refuted: fully missing children explain < 1 % of M for M < 100), and the large clusters consist of MORE generic
patterns than the singletons. "One hard region fails, dragging its neighbours" is right in the weak sense (one
component; hard patterns fail alone: corr(p_π, Λ_π) = −0.75 / −0.43) and wrong in the strong sense (no (k−1)-pattern
or monotone core is the region; each covering (k−1)-pattern loses only 3–9 of its 37 extensions).

## Table 4 — Λ_π = E[M | π ⊄ σ_n] and the tail of M | M>0 at t(k)   (`out/k*.txt` Task 3(ii) block; `tail.py`)

| k | n | ln R | ln(E M²/μ) | max_π Λ_π (≥20 ev.) | median Λ_π | Λ_id | corr(p_π, Λ_π) |
|---|---|---|---|---|---|---|---|
| 6 | 28 | 1.76 | 3.04 | 37 | 21 | 11.7 | −0.75 |
| 7 | 37 | 2.54 | 4.35 | 173 | 73 | 52 | −0.43 |
| 8 | 48 | 3.11 | 5.46 | — | — | — | — |
| 9 | 60 | 3.65 | 6.11 | — | — | — | — |

Tail P(M ≥ m | M>0), m = 2, 4, 8, …, 1024 and the share of Σ M from M ≥ 256:
- k=6: .67 .41 .21 .08 .02 .005 0 … ; share 0
- k=7: .75 .53 .34 .19 .09 .04 .012 .002 0 … ; share 0.07
- k=8: .77 .57 .39 .25 .14 .08 .036 .015 .004 0 ; share 0.29
- k=9: .80 .61 .44 .31 .20 .12 .066 .034 .012 .002 ; share 0.48 (max M = 2222 of 362880)
Local tail exponent −log₂[P(M≥2m)/P(M≥m)] at k=9: 0.4, 0.5, 0.5, 0.6, 0.7, 0.9, 1.0, 1.5, 2.6 — heavier than 1/m
up to m ≈ 300–500 ≈ e^{0.7k}, then steepening. R is made in the far tail and the share of the far tail grows with k.

## Table 5 — what makes M large: local defects of σ, not small LIS   (`msigma.c`, `defect.py`; `out/k7_n37_defect.txt`)

New independent sample (seed 21, k=7, n=37, 6000 σ; σ itself dumped). Per σ: area (in grid cells of the n×n board)
of the largest empty axis-parallel rectangle in the point set {(i, σ_i)}; minimum point count over a 3×3 and a 4×4
grid of cells; LIS, LDS. Grouped by M:

| M | #σ | mean largest empty rectangle (cells of 37²) | q90 | mean min count, 3×3 cells | P(some 3×3 cell empty) | mean min count, 4×4 | P(some 4×4 cell empty) | mean LIS | mean LDS |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3008 | 149 | 180 | 2.32 | 0.005 | 0.60 | 0.41 | 9.37 | 9.39 |
| 1–3 | 1406 | 160 | 192 | 2.12 | 0.011 | 0.42 | 0.58 | 9.47 | 9.56 |
| 4–9 | 714 | 167 | 198 | 1.98 | 0.021 | 0.32 | 0.69 | 9.63 | 9.55 |
| 10–29 | 589 | 175 | 210 | 1.84 | 0.039 | 0.23 | 0.77 | 9.73 | 9.75 |
| 30–99 | 237 | 185 | 220 | 1.59 | 0.110 | 0.19 | 0.81 | 9.90 | 9.80 |
| ≥ 100 | 46 | 200 | 236 | 1.04 | 0.283 | 0.02 | 0.98 | 10.15 | 10.30 |

Spearman correlation with M (all σ / given M>0): largest empty rectangle +0.42 / +0.32; min 3×3 count −0.26 / −0.21;
min 4×4 count −0.29 / −0.20; LIS +0.11 / +0.11; LDS +0.09 / +0.06.

Verdict: the size of the missing set is governed by *emptiness at scale ≈ n/4* (largest empty rectangle, empty
4×4 cells): 98 % of the σ with M ≥ 100 have an empty 4×4 cell (41 % for M = 0), and the largest empty rectangle grows
monotonically with M. LIS/LDS are essentially uncorrelated with M (slightly positive: more "monotone" σ miss
more, the opposite of the small-LIS mechanism). This confirms H5 of proof.md: the e^{Θ(k)} clusters are produced by
local defects, and the combinatorial step for a proof is to count the patterns killed by one empty rectangle of
area ≍ 1/k² … 1/√k (the data cannot fix the scale exponent at k = 7).

## Verdict
1. Classical sieve/Janson machinery is void here (Table 1). The only classical bound that survives is the second
   moment, which gives the *witness criterion* of proof.md Thm 1.1: R ≤ Σ_π p_π Λ_π/μ ≤ max_π Λ_π, escaping the W22
   Δ ≥ μ²/C cap because it needs no correlation inequality. Numerically ln(EM²/μ) ≈ 1.05k − 3 (k=6..9), so the
   criterion H(a) holds with a ≈ 1 in the observed range, and R ≤ e^{O(k)} ⇒ threshold constant = first-moment constant
   (Cor. 1.2). NUMERICAL only: k=6..9 cannot separate 0.7k from 0.23·k ln k.
2. The reason R is small is NOT a hard core of patterns (Table 2) — p_π is flat within ×4 — but the *locality of
   the failure mechanism*: given M>0 the missing patterns form one diffuse cluster of generic patterns (Table 3).
   Hard (layered) patterns are missed alone; generic patterns are missed in bulk when σ has a defect.
3. What a proof of R ≤ e^{O(k)} needs (proof.md §4, H4–H5): a large-deviation bound P(M ≥ m | M>0) ≤ m^{−1−δ} for
   m ≥ e^{O(k)} — "missing e^{ω(k)} patterns costs e^{−ω(k)} more than missing one". The monotone mechanism (small
   LIS) cannot produce M ≥ e^{Θ(k)} cheaply (heuristic H5) and is uncorrelated with M in the data (Table 5); the
   relevant σ-defects are empty rectangles (Table 5: Spearman(M, largest empty rectangle) = +0.4, 98 % of the M ≥ 100 events
   have an empty cell of a 4×4 grid). Bounding the number of patterns killed by one such defect by e^{O(k)} is the
   open combinatorial step.
4. Erdős–Szekeres makes id/rev co-missing impossible for n ≥ (k−1)²+1 (exact explanation of the W24 observation);
   it is worth a factor 2 only (proof.md §2).
