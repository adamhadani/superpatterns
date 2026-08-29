# W15 — dihedral images and the hard family 𝓕 — log (reconstructed by the coordinator, 2026-08-29)

Goal: cover gap G2 (large-LDS chains) by applying Theorems 5/8 to the 8 dihedral images of π; decide whether they cover S_k.

Outcome (see proof.md, verified by the coordinator):
- POSITIVE: Theorem 8 extends to mixed-direction runs via the dihedral images (Thm in proof.md §3).
- NEGATIVE (main): the family 𝓕(r,h,ε) = tilted grids with each row perturbed on ≤ εr entries (|𝓕| ≥ e^{(1/32)k ln k})
  has L_Δ ≥ k/16 for every Δ ≤ 0.7k in ALL 8 dihedral images ⇒ no chain-based hypothesis can cover S_k.
- NUMERICAL (later shown misleading by W18): unconditioned simulations suggested threads overlap only when the element
  lag is ≲ 3√k; W18 proved the conditioned loss is linear in the lag, so the "lag lemma" route is closed.
- Follow-up: W11 Thm 4.1 (paper Thm 10) shows every member of 𝓕 individually has threshold ≤ (π/8)k²: 𝓕 defeats the
  method, not the statement.
The agent was killed by a rate limit before writing this log; proof.md is complete.
