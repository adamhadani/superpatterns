# W35 log (2026-08-29)

1. Read `formal-verification/lean/LOG.md`, `Patterns.lean` (definitions `OrdIso`, `Contains`,
   `IsSuperpattern`, `rank`, `ranks`, `lt_iff_rank_lt`), the sources (W28 proof.md Thm 1.1 / Thm 2.1,
   W27 proof.md Lemma 0.2, paper Prop. 15).
2. Checked Mathlib for Erdős–Szekeres: only in `Archive/Wiedijk100Theorems/AscendingDescendingSequences.lean`
   (`Theorems100.erdos_szekeres`, statement over a `Fintype` linear order with injective `f`).
   Test import from the project: Lake built the module in 4.4 s from cached oleans. Reused it.
3. `BlockSplit.lean` written; first compile: 3 name errors (`List.length_eq_countP_add_countP`
   implicit args, `List.nodup_range` is not a function in this Mathlib); fixed, compiles.
4. `ErdosSzekeres.lean`: subsequence built as `List.ofFn (σ[f ·])` for `f = Finset.orderEmbOfFin`
   of a card-`a` subset of the monotone set; sublist via
   `List.sublist_iff_exists_fin_orderEmbedding_get_eq`. Fixes: `rfl` after simp for the
   `Fin.cast` goal; `StrictAnti.lt_iff_gt` (not `lt_iff_lt`). Compiles.
5. `Witness.lean`: `FinProb` structure, `E/ind/Pr/Eon`, `cnt`; Cauchy–Schwarz via
   `Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul` with `r = p·M`, `f = p·M²`, `g = p·1_{M>0}`
   (no square roots needed). Compiled first time modulo linter warnings (`omit [Fintype Ω]`,
   `push_neg` deprecation). Added the uniform-model section (`Perms n` Fintype via
   `List.permutations`, `FinProb.uniform`, `missing`, `cnt_missing_pos_iff`,
   `witness_reduction_uniform`).
6. Wired the three modules into `Superpatterns.lean` and `Axioms.lean`. Full `lake build`:
   8719 jobs, "Build completed successfully", 15 s wall (≈175 % CPU briefly).
7. Axiom audit (`lake env lean Superpatterns/Axioms.lean`), new entries — all
   `[propext, Classical.choice, Quot.sound]`:
   `FinProb.Pr_pos_le_mean`, `FinProb.sq_mean_le`, `FinProb.E_sq_eq_sum`, `FinProb.mean_le_max_cond`,
   `FinProb.witness_reduction`, `FinProb.witness_reduction_max`, `witness_reduction_uniform`,
   `contains_ranks_iff`, `blockStd_avoids`, `ranks_perm_range`, `erdos_szekeres_contains`,
   `not_avoid_both`. Pre-existing entries unchanged (certificates still carry their `native_decide`
   axioms).
8. Not done: probabilistic block splitting `p_π(N) ≤ p_π(M)^{⌊N/M⌋}` (see README for what is needed).
   No sorries introduced. Nothing committed.
