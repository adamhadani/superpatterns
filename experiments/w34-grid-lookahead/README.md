# W34 — grid lookahead (block-grid patterns 𝒢(r,h): from π/8 toward 1/4)

Question: can lookahead push the rigorous threshold of the tilted grids / block-grid patterns (W11 Thm 10:
(π/8)k², barrier π/8 for all fresh-quadrant rules, W20 Prop 3.1) toward 1/4?

Answer (see proof.md, results.md):
* y-lookahead (cost-to-go of a strip's remaining visits) is W20's Bellman C_mf(h) ≥ π/8: useless (§1).
* The barrier is escaped only by x-lookahead ACROSS strips (choosing where the shared clock lands, Prop 2.1).
  In the mean-field regime the x-costs telescope and a round is a first-passage problem across strips (2.1);
  its per-strip constant is numerically γ_∞ = 1.000 ± 0.002, i.e. threshold 1/4 exactly (Conj 5.1).
* Rigorous: block rule (optimal path through b consecutive fresh windows, stationary random block sizes
  {b, b+1}); Theorem 3.4: for the tilted grid (and τ with (H_b)), min(r,h) ≥ (ln k)³:
  threshold ≤ C^{mix}_b = 0.345 (b=2), 0.321 (4), 0.300 (8), 0.284 (16), 0.273 (32), 0.2656 (64) [Monte Carlo].

Files: fpp.py (exact DP for K_n / γ_∞), check_dp.py (brute-force validation), blocks.py (block constants),
*.out (raw outputs), log.md (chronology, dead ends), proof.md (statements + proofs), results.md (tables).
Run: `../w12-c21/.venv/bin/python fpp.py n X Y seed`, `... blocks.py b M [seed0]`.
