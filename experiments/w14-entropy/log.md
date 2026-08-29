# W14 — entropy lemma (E) for structured interleavings — log (reconstructed by the coordinator, 2026-08-29)

Goal: prove (E): #{π ∈ 𝓛_r with ≤ j mutually good shifts} ≤ e^{(29j−1)k}, which with W13's mechanism would close gap G1.

Outcome (see proof.md, verified by the coordinator):
- NEGATIVE: (E) is FALSE. For two runs whose value intervals are near-translates by Δ, the Δ-shift chain has length ≈ run
  length for EVERY interleaving word (v ↦ v−Δ is monotone on both runs), so L_Δ carries no information about the word;
  for r ≥ e^75 at least e^{61k} patterns in 𝓛_r have only two mutually good shifts.
- POSITIVE: Prop 3 — the unconditional range of Theorem 5 extends to r ≤ e^57.
- Side result: periodic words via π^{-1} (same difficulty).
Dead end: any chain-based entropy count over interleavings; the chain statistic is blind to the interleaving word.
The agent was killed by a rate limit before writing this log; proof.md is complete.
