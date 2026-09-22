> **Status update, 2026-09-10.** The independent-strip theorem stands separately from its application. Use the corrected H_η grid hypothesis and simultaneous tilted-grid corollary in [proof.md](proof.md); the older H_b claim below is superseded.

# W36 — results (γ_∞ = 1 PROVED; all numbers reproducible from the listed files)

## Headline

| statement | status |
|---|---|
| γ_∞ = lim E K_n/n = 1, with n − √(2n) ≤ E K_n ≤ n + √(2n) + 1/2 for all n ≥ 1 | **PROVED** (proof.md Thm 3.3; Burke property Thm 2.3) |
| Sharpened lower half: E K_n ≥ n for *every* n (subadditivity + Thm 3.3); so C_b, C^{mix}_b ≥ 1/4 always | PROVED (Cor 3.4) |
| W34 Conjecture 5.1 (full-lookahead mean-field fixed-strip constant = 1/4 exactly) | **PROVED** (both directions) |
| C_b, C^{mix}_b → 1/4 with certified finite-b bounds | PROVED (Cor 4.0; constants.py) |
| Tilted grids (12⋯r)^h and all τ ∈ 𝒢(r,h) with (H_η), min(r,h) ≥ (ln k)³: threshold ≤ (1/4+ε)k², all ε>0 | **PROVED** (Thm 4.1 = Thm 3.3 + W34 Thm 3.4/paper Thm 18(a)) |
| FREE model ≤ the same | Fixed-strip copies are actual copies |
| Lower bound (1/4−o(1))k² for grids | **NOT proved, not claimed** — the W12 value .1925 still needs an interval certificate; grid LIS is only r+h−1, so LIS-type lower bounds do NOT apply (proof.md §5). "Exactly 1/4" holds for the mean-field fixed-strip full-lookahead model, not (yet) for the containment threshold. |

Mechanism: the backward recursion G_s(a) = min_{x_p>a}[y_p + G_{s+1}(x_p)] has an exact one-parameter
family of stationary centered boundary-increment laws: compound Poisson with jump rate ρ and i.i.d. Exp(1/ρ) jump sizes
(slope ρ²), per-strip cost exactly ρ (Exp(1/ρ) increment at every strip).  Analogue of Hammersley
sources/sinks (ρ, 1/ρ); free boundary x = slope 1 = cost 1/strip.  Proof of stationarity: the leftward
process D(a) = G_s(a) − G_{s+1}(a) is a reversible Markov jump process (detailed balance ⇔ ρθ = 1);
reversibility swaps input jumps (of G_{s+1}) and output jumps (of G_s) — a Burke theorem.

## Numbers

Approximate evaluations of the analytic upper-bound formula (constants.py → constants.out),
with W34 Monte Carlo in parentheses. These rounded displays are not outward enclosures:
C^{mix}_b upper formula ≈ 0.3504 (0.2656) at b=64; 0.2972 at 256; 0.2731 at 10³; 0.2571 at 10⁴; 0.2522 at 10⁵;
0.2507 at 10⁶ → 1/4.  (The certified bound crosses π/8 = 0.3927 at b = 64.)

Numerical cross-checks of the lemmas (not certification) (verify.py, seeds 1 and 2 → verify_seed{1,2}.out; own DP,
validated against brute force by check_small.py, 300 instances, max error 2·10⁻³ = discretisation):
* Lemma 1.1 (D ~ Exp(1/ρ)): KS ≤ 0.018 at 4000 samples (95% crit. 0.0215), ρ ∈ {0.5, 1, 2}.
* Theorem 2.3 (Burke): G′-jump rate = ρ to ±0.3%; sizes exponential mean ρ (KS ≤ 0.004 on ≥ 6·10⁴ jumps);
  gaps exponential mean 1/ρ; lag-1 correlations (sizes, gaps, size↔next gap) all |corr| ≤ 0.007.
* Corollary 2.4 (E G^ρ_1(0) = nρ): matches within 1.2 s.e. for (n,ρ) ∈ {10,50,200}×{0.7…1.5}.
* Lemma 3.1 (Lundberg): E Z = 1.22±0.03 vs 1.20 (ρ=1.5); 0.67±0.02 vs 0.667 (ρ=2).
* Theorem 3.3: E K_10 = 10.85±0.07, E K_50 = 51.99±0.22, E K_200 = 201.6±1.1, all inside
  [n−√(2n), n+√(2n)+½] = [5.5,15.0], [40.0,60.5], [180.0,220.5]; W34's high-precision E K_b (2.387, 3.489,
  4.564, 9.839, 18.09, 34.47, 67.03 for b = 2,3,4,9,17,33,65) all inside too.
  Observed E K_n − n ≈ 0.21√n; the bound allows 1.41√n (slack from the crude Lundberg step; truth likely n^{1/3}).

## Commands (venv = experiments/w12-c21/.venv/bin/python)

    cd experiments/w36-gamma-limit
    ../w12-c21/.venv/bin/python check_small.py        # DP vs brute force
    ../w12-c21/.venv/bin/python verify.py 1           # tests A–D, ~9 s
    ../w12-c21/.venv/bin/python verify.py 2
    ../w12-c21/.venv/bin/python constants.py          # certified C_b, C^mix_b table

## Current application

H_η means successive strip visits separated by at least ηr, fixed η>0.
Theorem 4.1 gives a uniform individual bound under this hypothesis; Corollary
4.2 now gives simultaneous containment of all admissible tilted-grid shapes
and their dihedral images. The old H_b hypothesis is withdrawn. Only the
independent-strip mean-cost constant is exact; no matching free-containment
lower threshold is established. See the current proof and W34/reduction.md.
