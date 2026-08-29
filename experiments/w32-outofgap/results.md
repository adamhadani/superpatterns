# W32 — numerical results

All runs: uniformly random π ∈ S_k, Poisson process of intensity Ck² on the unit square, scaled units (x' = kx,
y' = ky), potentials V_n from ../w31-lookahead/dp_V.txt (ε = 0 Bellman values), no window margins, searches from
the true clock (no safe clock).  "Implied constant" := C · (x-consumption)/k, which for a fresh-model rule is
C-independent and equals the rule's threshold constant.  Commands: see README.md.  Statistical noise: the
per-run sd is 0.02–0.05 of k, so means over 8–10 runs carry ± 0.01 in the implied constant.

## 1. One-sided in-gap rule, no artificial partition (single strip h = k) — single_strip.py, runs_m1.out

| k | C | runs | mean cost/k (sd) | implied constant | mean-field V_k/k² |
|---|---|---|---|---|---|
| 256 | 0.5 | 10 | 0.883 (0.052) | 0.442 | 0.4656 |
| 256 | 0.6 | 10 | 0.794 (0.077) | 0.476 | 0.4656 |
| 1024 | 0.5 | 9 (1 run ran off the square) | 0.934 (0.024) | 0.467 | 0.4631 |
| 1024 | 0.6 | 10 | 0.785 (0.025) | 0.471 | 0.4631 |
| 2000 | 0.5 | 10 | 0.929 (0.028) | 0.465 | 0.4627 |
| 2000 | 0.6 | 10 | 0.760 (0.015) | 0.456 | 0.4627 |

The real process (non-fresh, single strip, exact excision) reproduces the mean-field cap V_k/k² within noise:
removing the strip partition (W31 used h ≤ 512) buys nothing beyond V_h/h² − V_k/k².

## 2. Dependence on the partition (k = 1024, C = 0.6) — runs_m.out

| m (strips) | h | implied constant | V_h/h² |
|---|---|---|---|
| 1 | 1024 | 0.471 | 0.4631 |
| 2 | 512 | 0.473 | 0.4640 |
| 4 | 256 | 0.461 | 0.4656 |
| 8 | 128 | 0.464 | 0.4686 |
| 16 | 64 | 0.475 | 0.4745 |

All within ± 0.01 of the mean-field prediction; the partition is irrelevant at this precision (Theorem 2.1
Remark (ii)).

## 3. Staleness: cost share of steps a lookahead L could inform — stale_k*_m1_C0.6.txt

D := clock advance between the creation of the current value's gap and the current step; share := Σ u over
steps with D < L divided by Σ u.

| L/k | k = 256 | k = 1024 | k = 2000 |
|---|---|---|---|
| 0.001 | 0.041 | 0.017 | 0.018 |
| 0.005 | 0.073 | 0.054 | 0.057 |
| 0.01 | 0.112 | 0.093 | 0.097 |
| 0.02 | 0.169 | 0.156 | 0.166 |
| 0.05 | 0.312 | 0.298 | 0.315 |
| 0.1 | 0.480 | 0.465 | 0.495 |
| 0.2 | 0.699 | 0.694 | 0.715 |
| 0.5 | 0.958 | 0.970 | 0.967 |

The share is a function of L/k alone (k = 1024 and 2000 agree; ≈ 1.2 (L/k)^{0.7}): a lookahead of x'-length L
= o(k) can inform a vanishing share of the cost.  By time (diag.py, k = 1024): the median revisit advance grows
from 0.0035k (t < 0.1k) to 0.25k (t > 0.9k); the lower tail (gaps with many values are revisited fast) is what
makes the share ≫ CL/k.

## 4. Several candidates: two-sided scan and lanes — twosided.py, lanes.py

| rule | k | C | runs | success | implied constant |
|---|---|---|---|---|---|
| one-sided | 512 | 0.6 | 8 | 8/8 | 0.448 (lanes r=1, seed 11) |
| one-sided | 1024 | 0.6 | 10 | 10/10 | 0.461 |
| two-sided | 256 | 0.6 | 5 | 5/5 | 0.461 (one-sided same seeds 0.481) |
| two-sided | 512 | 0.5 | 8 | 7/8 | 0.461 |
| two-sided | 512 | 0.45 | 8 | 3/8 | (0.434 over finished runs — biased) |
| two-sided | 512 | 0.4 | 8 | 0/8 | — |
| two-sided | 1024 | 0.6 | 10 | 10/10 | 0.464 |
| lanes r=2 | 512 | 0.6 | 8 | 8/8 | 0.456 |
| lanes r=4 | 512 | 0.6 | 8 | 8/8 | 0.450 |
| lanes r=4 | 1024 | 0.6 | 8 | 8/8 | 0.467 |
| lanes r=8 | 512 | 0.6 | 8 | 4/8 | 0.445 over finished |
| lanes r=16, 32 | 512 | 0.6 | 8 | 0/8 | — |

Two-sided / lane rules give no gain beyond the noise (± 0.01) at k = 1024; the two-sided rule fails at C = 0.45
and 0.40.  zdiag.py (k = 512, C = 0.6): the two candidates' score changes Z have mean +0.94 (left), +0.89 (right),
sd 1.7, E min(Z_L, Z_R) = −0.12 per step: the persisting candidate is biased upward (selection), so the minimum
of the two is not −E|Z_L − Z_R|/2 as it would be for fresh mean-zero pairs (proof.md Obs. 3.1).

## 5. Anticipating cap: E V(T) over random binary search trees — bst.py, bst.out

| n | V_n^{ant} | V_n | ratio | V_n^{ant}/n² |
|---|---|---|---|---|
| 4 | 9.880028 | 9.880089 | 0.999994 | 0.61750 |
| 8 | 34.922966 | 34.923993 | 0.999971 | 0.54567 |
| 11 | 63.499384 | 63.501861 | 0.999961 | 0.52479 |
| 20 | 199.382874 | 199.393307 | 0.999948 | 0.49846 (quantised, 40 atoms) |
| 40 | 770.057039 | 770.104276 | 0.999939 | 0.48129 (quantised) |
| 60 | 1710.945699 | 1711.056015 | 0.999936 | 0.47526 (quantised) |

n ≤ 11 exact (all Catalan(n) shapes); n > 11 with the V(T)-distribution quantised to 40 atoms, which by concavity
of W over-estimates V^{ant} slightly (the true gain for n > 11 may be a little larger than shown); the exact values
for n ≤ 11 and the smooth trend put the gain from knowing π in advance at 4–7·10^{−5}.
