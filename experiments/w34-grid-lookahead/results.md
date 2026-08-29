# W34 — results (all numbers reproducible from the listed files; ≤ 3 cores, scipy venv of w12)

## 1. Infinite-lookahead round constant γ_∞ (fpp.py; exact DP, validated by check_dp.py, 0 mismatches / 300)

G_1(0)/n for n independent Poisson(1) strips on [0,X]×[0,Y] (caps bias upward):

| n | X | Y | seeds → G_1(0)/n |
|---|---|---|---|
| 1000 | 1400 | 4 | 0.9994 |
| 1000 | 1400 | 8 | 1.0014 |
| 1000 | 2000 | 4 | 1.0073 |
| 2000 | 2600 | 6 | 1.0057, 1.0016, 0.9972, 1.0027, 1.0075, 1.0010 (mean 1.0026) |
| 4000 | 5000 | 6 | 1.0015, 1.0047 |
| 4000 | 5000 | 10 | 1.0048 |
| 8000 | 10000 | 6 | 1.0015, 0.9997 |

**γ_∞ = 1.000 ± 0.002, C*_∞ = γ_∞²/4 = 0.250 ± 0.001** (NUMERICAL).  Files: fpp_n2000.out, fpp_n4000.out, fpp_n8000.out.
Mean x-part and y-part per strip both ≈ 0.50 (seed-to-seed spread ±0.05: nearly flat trade-off).

## 2. Block constants (blocks.py; Monte Carlo, i.i.d. samples of the exact DP)

C_b = (E K_b/(2b))²: b=1: 0.3937 (exact π/8 = 0.3927 ✓), 2: 0.3561, 3: 0.3381, 4: 0.3254, 5: 0.3171, 8: 0.3024,
9: 0.2988, 12: 0.2918, 16: 0.2847, 17: 0.2832, 24: 0.2771, 32: 0.2738, 33: 0.2727, 64: 0.2655, 65: 0.2658,
128: 0.2607, 256: 0.2567.  Fit: C_b ≈ 1/4 + 0.105/√b.  Files: blocks_a.out, blocks_b.out, blocks_c.out,
blocks_b{2,3,4}_hp.out, blocks_pairs_{a,b}.out.

Theorem 3.4 constants C^{mix}_b = ((E K_b + E K_{b+1})/(2(2b+1)))² (proof.md §4 table):
**b=2: 0.3452, b=4: 0.3208, b=8: 0.3005, b=16: 0.2839, b=32: 0.2733, b=64: 0.2656** (+2se: 0.2666).

## 3. Headline

| statement | regime | constant | status |
|---|---|---|---|
| y-lookahead (Bellman in remaining visits × level) | any | ≥ π/8 (= W20 C_mf(h) ↓ π/8) | PROVED (by W20) — negative |
| Prop 2.1: only cross-strip x-lookahead escapes Prop 3.1 in the mean-field regime | r → ∞ | — | PROVED |
| Thm 3.4: block rule, tilted grid (12⋯r)^h and all τ with (H_b), FIXED model | min(r,h) ≥ (ln k)³ | ≤ C^{mix}_b; 0.2656 at b = 64 | PROVED reduction; constant Monte Carlo |
| Conj 5.1: full lookahead | r ≫ h ≫ 1 (mean field) | γ_∞ = 1 ⇒ 1/4 exactly | NUMERICAL (±0.001) |
| FREE model | — | ≤ min(C^fix(r,h), C^fix(h,r)); no first-order gain from budget reallocation | PROVED inequality; HEURISTIC |

Prior best for these patterns (ledger): π/8 = 0.3927 (W11 Thm 10 / Thm 4.4), with the π/8 barrier for
all fresh-quadrant rules (W20 Prop 3.1).  Improvement: 0.3927 → 0.2656 (rigorous reduction, MC constant),
→ 0.250 (numerical limit).  Consequence for W20 Conjecture 4.6 (mean-field rules optimal at fixed h,
r → ∞): FALSE for large h (proof.md §5).

## 4. Open / not done
* Certified (non-Monte-Carlo) value of E K_2 (Feynman–Kac for the running minimum; log.md §4).
* Proof that γ_∞ = 1 (Burke-type stationary solution of the recursion (2.2)?).
* General τ ∈ 𝒢(r,h) without (H_b) (strips revisited within b+1 visits every row): needs per-strip weights.
* FREE-model rule with adaptive strip boundaries (goal 3): not designed; see proof.md §6.
