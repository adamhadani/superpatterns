# W26 log — Pareto-front certificates for (12)^h, r=2

- start: created dir, reading NOTES.md ledger, w23/w20/w11 proofs.

## 1. Reading + first analysis
- W23: Thm 1.1 Dilworth (rate ln(C/e)); Thm 2.1 for r=2 gives speed N/12 only for C > 9r ln(3er) ≈ 51. §4: fixed r=2 rate ≈ .025 at C=.5, k-independent.
- W20 Prop 1.2: exact DP state = Pareto front of (l_0,l_1) per level t. In 3D: U_t = {(x,y_0,y_1): t letters embed} nested up-sets in [0,1]^3.
- W11 Prop 3.1 cap: Pr ≥ e^{-N/2} (Poisson) = 2^{-N} (N iid points): rate ≤ ln 2 in the iid model.
- DEAD END (entropy): coarse-graining the 3D up-sets U_t on a grid of side a/k costs 2^{O(k^2/a^2)} PER LEVEL, k levels → e^{Θ(k^3)} ≫ e^{N}. The 3D state is too rich to encode geometrically.
- DEAD END (2D staircases on grid for the alternating relaxation, see below): count 4^{2k·k/a}, boundary slack 4a → rate 1/2−2a−4ln2/(aC) > 0 only for C > 89. Grid coarse-graining is too lossy; use the points themselves as generators (Dilworth style).
- KEY IDEA: alternating-chain relaxation. An increasing chain a_1<...<a_k (2D dominance) with colours 0,1,0,1,... is a copy of (12)^h in the fixed-strip/colour model. Its level function λ(p) = longest alternating chain ending at p has a 2D DP: λ(p) = 1+max{λ(q): q<p, colour(q)≠colour(p)}, monotone within colour. Level classes are NOT antichains (same-colour comparable pairs allowed), but their minimal elements are; the non-minimal points are confined to slab intersections of total area ≤ 1 (both colours together) ⇒ each non-generator point is allowed w.p. ≤ 1/2. Certificate = (generator set M, labels (t,c)); Pr ≤ 2^{-N} Σ_m C(N,m) Σ_{comp of m into 2(k−1)} m!/Π(n!)².

## 2. Numerics batch 1 (alt.c = alternating-LIS 2D DP, Fenwick prefix-max per colour)
- rate.py: Theorem A rate rho(C)=ln2−sup_b[H(b)+b ln(4e/(bC))]: C_0 = 27.63; rho(30)=.026, rho(50)=.166, rho(100)=.31, rho(1000)=.57 → ln2.
- alt-LIS ≈ 1.33·sqrt(N) (k=64: 65.2 at N=2458): relaxation threshold C_alt ≈ 9/16 ≈ 0.56 (vs true fixed (12)^h ≈ 0.25, W20). Generator fraction (minimal elements of level classes) ≈ 0.51 → 1/2 in typical configurations.
- launched: out/tg_r2.txt (exact fixed-strip r=2, k=12..40, C=.4..1, 2e5 reps) and out/alt_rates.txt (k=16..48, C=.6..1.5).
