# W29 — numerics (all NUMERICAL; the reduction they feed is PROVED in proof.md)

Ω_h(β, w, rule) = E[Σ_{t≤h} 1/|W_t|]/h for a uniformly random sub-pattern σ ∈ S_h (strip.c; C-independent).
Threshold constant of Theorem 3.2 = Ω_h.  Rules: mode 2 = window is the whole reserve interval J_t;
mode 1 = J_t ∩ band of width w around the proportional target y_0 = y'_L + (y'_R − y'_L)(m_b+½)/(m_b+m_a+1),
widened to length β if shorter; mode 0 = same with the row-centre target v + ½ (always worse than mode 1).
Sanity: h = 2, mode 2, β = 1 gives Ω_2 = (1 + ln 2)/2 = 0.8466 exactly (first window [v, v+1], second [y, 2]
with y uniform); strip.c returns 0.8466 (4·10^5 samples).

## 1. Optimised constants (mode 1; seeds 11/23/31; sem ≤ 0.001 for h ≤ 256, ≤ 0.0005 at h = 1024)

| h | best (w, β) | Ω_h | barrier (h+1)/(2h) | no-band best (β) |
|---|---|---|---|---|
| 2 | (3, 0.8) | 0.798 | 0.750 | 0.847 (β=1) |
| 4 | (3, 0.8) | 0.676 | 0.625 | — |
| 8 | (3, 0.8) | 0.606 | 0.5625 | — |
| 16 | (3, 0.8) | 0.563 | 0.531 | 0.584 (0.9) |
| 32 | (3, 0.7) | 0.537 | 0.516 | — |
| 64 | (3, 0.7) | 0.5266 | 0.508 | 0.569 (0.9) |
| 128 | (3, 0.8) | 0.525 | 0.504 | — |
| 256 | (3.25, 0.7) | 0.5174 | 0.502 | — |
| 512 | (3, 0.8) | 0.520 | 0.501 | 0.564 (0.95) |
| 1024 | (3.25, 0.7) | 0.5154 | 0.5005 | — |
| 2048 | (3, 0.7) | 0.517 (40 samples) | 0.5002 | — |

Ω_h decreases in h and sits 0.015–0.03 above the proved barrier ½ + 1/(2h) for h ≥ 64; extrapolated limit
Ω_∞ ≈ 0.51–0.515 (HEURISTIC: strictly above ½, since the O(1)-size gaps of the last points are unequal).
Dependence on the parameters is mild: w ∈ [2.5, 4], β ∈ [0.6, 0.85] are all within 0.01 of the optimum (sweep2/3).

## 2. Chernoff exponents η (per point; Theorem 3.2 failure ≤ e^{−ηk}), rule (w, β) as in the table

| h | C | η | 
|---|---|---|
| 64 | 0.55 | 0.00071 |
| 64 | 0.60 | 0.0066 |
| 64 | 0.70 | 0.032 |
| 64 | 0.80 | 0.069 |
| 32 | 0.60 | 0.0047 |
| 16 | 0.60 | 0.0017 |
| 8 | 0.70 | 0.0087 |
| 4 | 0.80 | 0.013 |
| 2 | 0.90 | 0.0069 |

(Exponent computed from the window-MGF E Π_t (1 − θ/(C|W_t|))^{−1} on a θ-grid of 40 points in (0, Cβ).)

## 3. End-to-end 2-D validation (validate2d.py: real Poisson points, real random π, the greedy asserts a copy)

k = 400, h = 40, rule (3, 0.8), Ω_40 = 0.537, 20 repetitions each:
C = 0.5: 2/20 succeed; C = 0.55: 13/20; C = 0.6: 20/20; C = 0.7: 20/20.  (k = 200, h = 20, C = 0.65: 20/20.)
Every successful run passed the assertion "chosen points form a copy of π" (x increasing, y-ranks = π).
Consistent with the threshold Ω_40 = 0.537 and with η(0.6) ≈ 0.005–0.007 (e^{−ηk} ≈ 0.07–0.14 at k = 400).

## 4. Comparison with the ledger

| pattern class | rigorous constant | source |
|---|---|---|
| every π | 0.757 | W19 Thm 4B.3 |
| block-grid / monotone-strip π | π/8 = 0.393 | W11 Thm 4.1/4.4 |
| uniformly random π (annealed + all but e^{−ηk/2} fraction) | **0.5266 (h = 64), 0.5154 (h = 1024)** | this workstream |
| conjectured truth, random π | ≈ 0.22 | W21 |
| identity (true) | 0.25 | Hammersley/LIS |
