# W26 — Pareto-front / level-set certificates for the two-strip pattern (12)^h (r = 2)

Files: proof.md (all statements tagged), log.md (chronological, dead ends), alt.c (alternating-LIS 2D DP,
Fenwick), exact_bound.c (exact finite-N evaluation of the certificate sum (1.2)), rate.py / rate_r.py
(asymptotic rate functions and thresholds), tg (= W20 tg.c, exact fixed-strip DP), out/ (raw numerics).

Result (proof.md Thm 1.1, PROVED): for N iid uniform points cut into two rigid strips (equivalently the iid
2-colour model),
   Pr((12)^h ⊄_fix) ≤ 2^{−N} Σ_m C(N,m) Σ_{n ⊨ m, 2(k−1) parts} m!/Π(n_j!)²  ≤ exp(−ρ(C)N + O(k ln N)),
ρ(C) = ln 2 − sup_β [H(β) + β ln(4e/(βC))] > 0 iff C > 27.63; ρ ↑ ln 2 (the exact cap of the model).
Speed N, rate k-independent, transfers to free containment for free.  Finite-k values of the exact sum are
better than ρ (see §4).  Previous best for r = 2 (W23 Thm 2.1): threshold ≈ 51, speed N/12.

Mechanism: "alternating-chain relaxation" — an increasing chain with alternating colours is a copy of (12)^h.
Its level function is a 2D DP; the minimal elements of the level classes (generators) are antichains (rigid,
1/n!), every other point is confined to slab intersections of total area ≤ 1 over both colours (probability
≤ 1/2 each).  This is the mixed rigid/empty-region certificate the task asked for.

Where it stops: the relaxation's own threshold is ≈ 9/16 (alt-LIS ≈ (4/3)√N numerically) vs ≈ 0.25 for the
true pattern; the certificate drops the witness and stacking constraints, which is what moves 9/16 to 27.6.
The exact 3D Pareto-front evolution cannot be encoded on any grid (e^{Θ(k³)} states, proof.md §2.2).
r strips: same theorem with cap ln(r/(r−1)) ≈ 1/r and C_0(r) ≈ 3.5 r³.  Nothing for the union bound over S_k.
