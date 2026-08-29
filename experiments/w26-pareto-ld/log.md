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

## 3. Theorem written (proof.md §1), dead ends §2, r strips §3
- exact tg rates from out/tg_r2.txt (k=12): C=.4 .0116, .5 .027, .6 .047, .7 .071, .8 .092 (5/2e5); C≥1 unmeasurable (0/2e5). Larger-k runs at C=.5,.6 (k=32,40) running.
- alt.c rates (relaxation) C=.8: k=16 .0105, k=24 .0077, k=32 .0064 — decreasing in k (TW-type drift like the identity), unlike the true r=2 rate which is k-stable.
- exact_bound.py: exact finite-N evaluation of (1.2) running (python O(N^2 log k), slow).
r= 2 C_0(r)= 27.6 rho at 2C_0, 10C_0: 0.1896 0.4596 cap 0.6931
r= 3 C_0(r)= 98.5 rho at 2C_0, 10C_0: 0.1143 0.2725 cap 0.4055
r= 4 C_0(r)= 239.4 rho at 2C_0, 10C_0: 0.0821 0.1944 cap 0.2877
r= 6 C_0(r)= 827.1 rho at 2C_0, 10C_0: 0.0525 0.1237 cap 0.1823
r= 8 C_0(r)= 1982.8 rho at 2C_0, 10C_0: 0.0386 0.0908 cap 0.1335
- rate_r.py: C_0(r) = 27.6, 98.5, 239, 827, 1983 for r = 2,3,4,6,8 (≈ 3.5 r³); fixed proof.md §3.1 accordingly.
- exact_bound.c: exact finite-N value of (1.2). k=10, C=30: −lnB/N = 0.106 (asymptotic ρ(30) = .026): the crude (2k)^m(2ek/m)^m step is loose at finite k; grid of (k,C) running → out/exact_bound.txt.

## 4. Final numerics
- tg r=2 k=32 (10^6 reps): C=.5: 2 absences → P=2e-6, −lnP/N = 13.1/512 = .0256 (k=12: .027, k=24: .0255 in W23): k-stable ✓ (speed N). C=.6: 0/10^6 (rate > .0225). k=40 run killed (unfinished, unneeded).
- exact_bound grid (out/exact_bound.txt): finite-k threshold of (1.2) ≈ 20 (k=10) → 24 (k=40) → 27.6.
- FINAL: Thm 1.1 proved; C_0 = 27.6 (asymptotic), speed N, rate → ln 2. Not pushed to 0.25: obstruction = relaxation threshold 9/16 + dropped witness/stacking constraints (proof.md §2.3).
