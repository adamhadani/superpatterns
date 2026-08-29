# W31 — numerics

All constants are C-independent (intensity-1 normalisation, proof.md Lemma 2.2) and reproducible with the
commands in README.md.  Machine: ≤ 3 cores used; total CPU ≈ 15 min.

## 1. Bellman values V_n (dp.py, ε = 0, Gauss–Legendre; uncertified) and certified upper bounds (dp_cert.py)

Ω*_n = V_n/n² is the optimum over all fresh-window gap rules (proof.md Thm 4.1); V̄_n/n² (ε) is the certified
upper bound for the margin rule R(n, ε, V̄) (proof.md Lemma 3.2), valid as a threshold constant by Thm 2.1.

| n | V_n/n² (ε=0, dp.py) | V̄_n/n² certified, ε=0 | ε=0.02 | ε=0.05 | blind barrier (n+1)/(2n) |
|---|---|---|---|---|---|
| 1 | 1 (exact) | 1.000000 | 1.000000 | 1.000000 | 1 |
| 2 | 0.75 (exact, V_2 = 3) | 0.750000 | 0.750000 | 0.750000 | 0.75 |
| 3 | 0.662838 | 0.663 | 0.663 | 0.663 | 0.666667 |
| 4 | 0.617506 | | | | 0.625 |
| 8 | 0.545687 | 0.5459 | | | 0.5625 |
| 16 | 0.506714 | 0.506981 | 0.506981 | 0.507145 | 0.53125 |
| 20 | 0.498483 | | | | 0.525 |
| 32 | 0.485716 | 0.486000 | 0.486008 | 0.486762 | 0.515625 |
| 64 | 0.474526 | 0.474834 | 0.474913 | 0.476456 | 0.507813 |
| 128 | 0.468628 | 0.468964 | 0.469167 | 0.471585 | 0.503906 |
| 160 | 0.467411 | 0.467756 | 0.468005 | 0.470716 | 0.503125 |
| 256 | 0.465552 | | 0.466271 | | 0.501953 |
| 512 | 0.463961 | | 0.464874 | | 0.500977 |
| 1000 | 0.463164 | | | | 0.5005 |
| 2000 | 0.462745 | | | | 0.50025 |

Files: dp_V.txt (n ≤ 2000), dp_cert_eps0.txt, dp_cert_eps0.05.txt (n ≤ 160), dp_cert_eps0.02.txt (n ≤ 512).
The certified bounds exceed the Gauss–Legendre values by 3·10^{−4} relative at ε = 0 (rectangle rule with
40 000 panels; the 1 + 10^{−9} rounding slack is negligible).  Differences V_{2n}/(2n)² − V_n/n²:
−0.0074 (50→100), −0.0039 (100→200), −0.0020 (200→400), −0.00104 (400→800), −0.00052 (800→1600): ∝ 1/n, so
lim Ω*_n ≈ 0.462745 − 0.84/2000 ≈ 0.4623 (HEURISTIC).  Crossing of ½: n = 20 (0.49848; n = 19: 0.50023).
Margin cost: ε = 0.02 adds ≤ 0.0002 at n = 64, ≤ 0.0010 at n = 512; ε = 0.05 adds 0.0016 at n = 64.

Sanity checks: W(0,0) = 1 and W(1,0) = 3 reproduced to 10^{−9} by both codes (hand computation in proof.md §3).

## 2. Free-shaping lower bound (freeshape_lb.py; Monte Carlo, 2000 patterns; HEURISTIC use only)

LB_h = (1/h²) Σ_t E[(Σ_j √p_{t,j})²]: 0.18895 (h = 16), 0.15983 (64), 0.15321 (256), 0.15110 (1024, 200
patterns).  Far below ¼: the counting argument of [W29] Thm 4.1 cannot cap value-aware gap rules at ¼; the
true cap of the class is the Bellman value ≈ 0.4623 (Thm 4.1).

## 3. End-to-end validation on a real Poisson process and a real random π (validate2d.py; Monte Carlo)

Rule R(h, 0.05, V̄) exactly as in proof.md §1 (safe clock, explored edges), N ~ Poisson(Ck²) uniform points,
π uniform in S_k, k = mh; "success" = all k chosen points have x < 1 AND the chosen points were checked to
form a copy of π (y-order = value order, sampled pairs).  10 runs per line; seeds 5/7/11.

| h | m | k | C | Ω_h(0.05) | success | mean a_k/k (finished runs) | collisions / run | collision cost / k |
|---|---|---|---|---|---|---|---|---|
| 32 | 64 | 2048 | 0.48 | 0.4868 | 2/10 | 0.985 | 31 | 0.009 |
| 32 | 64 | 2048 | 0.50 | | 9/10 | 0.974 | 31 | 0.007 |
| 32 | 64 | 2048 | 0.52 | | 10/10 | 0.943 | 35 | 0.008 |
| 32 | 64 | 2048 | 0.55 | | 10/10 | 0.883 | 33 | 0.007 |
| 64 | 32 | 2048 | 0.46 | 0.4765 | 0/10 | — | 62 | 0.014 |
| 64 | 32 | 2048 | 0.48 | | 3/10 | 0.989 | 63 | 0.015 |
| 64 | 32 | 2048 | 0.50 | | 10/10 | 0.965 | 62 | 0.014 |
| 64 | 32 | 2048 | 0.52 | | 10/10 | 0.933 | 61 | 0.013 |
| 64 | 32 | 2048 | 0.55 | | 10/10 | 0.879 | 61 | 0.013 |
| 128 | 16 | 2048 | 0.46 | 0.4716 | 0/10 | — | 118 | 0.028 |
| 128 | 16 | 2048 | 0.48 | | 3/10 | 0.986 | 125 | 0.030 |
| 128 | 16 | 2048 | 0.50 | | 10/10 | 0.969 | 123 | 0.027 |
| 128 | 16 | 2048 | 0.52 | | 10/10 | 0.925 | 123 | 0.025 |

Consistency with the theory: predicted mean a_k/k = Ω_h(ε)/C + (collision cost)/k, e.g. h = 64, C = 0.55:
0.4765/0.55 + 0.013 = 0.879 (observed 0.879); C = 0.52: 0.916 + 0.013 = 0.929 (observed 0.933); h = 128,
C = 0.52: 0.907 + 0.025 = 0.932 (observed 0.925).  The empirical transition sits at C ≈ 0.49 for all three
(h, m) pairs at k = 2048, i.e. ≈ Ω_h + collision cost + finite-m fluctuation of the strip sum (m = 16–64 strips);
all three effects vanish as m → ∞ (Thm 2.1).  At k = 2048 the success probability at C = 0.50 is already
0.9–1.0 for every h, against W29's rule which needed C ≈ 0.55–0.6 for the same success (W29 results.md:
13/20 at 0.55, 2/20 at 0.5 with k = 400).

Collisions: ≈ h per run (one per strip, mostly the first revisit after a strip's first point), costing 1–3 %
of k; the theoretical bound D_h of proof.md is astronomically larger than the observed explored extents
(Φ(y'(q)) − Φ_min)/C ≈ 0.4 per collision, because the rule almost never chooses points near the window edges.
