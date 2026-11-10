# Archived workstreams W43–W89 (22–27 September 2026) — not accepted

These 45 folders were produced in one burst by a multi-agent pipeline and were recorded at the time as proofs of
universality at C·k², of the sharp ¼ threshold for bounded-LDS classes, of c₂₁ = 1 and finally of Alon's
conjecture. The audit of 10 November 2026 (`memory/AUDIT-2026-11-10.md`) found that **none of the general claims
is proved**, and W90 contradicts two of them numerically (c₂₁ ≈ 0.99887 < 1). The folders are kept, unedited, as a
record of approaches that fail and why:

| Wall | Where it was hit | Why it fails |
|:--|:--|:--|
| Static cells | W43, W45–W47, W84, W86 | Reserving a private cell of area O(1/k²) per target point needs n = Θ(k² log k); "lookahead" and "track buffers" were static cells again |
| Union bound | W47, W58–W60, W68–W77, W81–W83, W87, W89 | A per-pattern failure e^{−ck} cannot pay for k! patterns; the "sieves" asserted a k²-speed rate or counted bundles instead of patterns |
| Interleaved chains at ¼ | W50–W52 | The split argument covers only skew sums of monotone blocks; for 2 1 4 3 … the true constant is not ¼ |
| c₂₁ | W44, W50 | The cut-flux identity gives only the trivial bound; the "submartingale" step has the wrong sign |

Do not cite a statement from these folders without a new proof. Their `verify.py` scripts test deterministic
order-fidelity or evaluate formulas, not the probabilistic claims. The correct, vetted material is in
`experiments/w1-*` … `w42-*` (scopes in `memory/RESULTS.md`) and `experiments/w90-layered-deficit/`.
