import Superpatterns.Certificates
import Superpatterns.TheoremA
import Superpatterns.Numeric
import Superpatterns.Witness
import Superpatterns.BlockSplit
import Superpatterns.ErdosSzekeres
import Superpatterns.BlockFlip

/-!
# Axiom audit

`lake build` prints the axioms used by each main theorem.  Expected:

* certificates: `propext`, `Classical.choice`, `Quot.sound`, **`Lean.ofReduceBool`** (native_decide);
* `sp3_example`, `sp4_example`: no `Lean.ofReduceBool` (kernel `decide`);
* `theoremA`, `lemma1_concrete`, `patCount_le_sum_W`: standard axioms only (no `sorryAx`);
* `tilt_bound`, `pair_sum_le`, `card_le_sum_fiber`, `constant_certificate`, `checker_sound`:
  standard axioms only;
* W35 (`Witness.lean`, `BlockSplit.lean`, `ErdosSzekeres.lean`): standard axioms only.
* W90/W91 (`BlockFlip.lean`): standard axioms only for the checker (`containsB_iff`,
  `numContaining_eq`, `card_Perms_contains`, `dsum_perm`, `blockFlipAt_of_sweepB`), for the two
  explicit permutations, for every count with `n ≤ 7` and for `1234`/`1324` on `S_8` (kernel
  `decide`); **`native_decide`** axioms for the other counts with `n = 8`, the counts with
  `n = 9` and `blockFlipAt_of_le_2_of_le_8`.
-/

namespace Superpatterns

#print axioms checker_sound
#print axioms sp3_example
#print axioms sp4_example
#print axioms σ7_superpattern
#print axioms σ8_superpattern
#print axioms σ8'_superpattern
#print axioms σ8''_superpattern
#print axioms card_le_sum_fiber
#print axioms card_fiber_le_of_injective
#print axioms pair_sum_le
#print axioms tilt_bound
#print axioms lemma1_concrete
#print axioms patCount_le_sum_W
#print axioms compSum_gaps
#print axioms gaps_mem_box
#print axioms gaps_injOn
#print axioms theoremA
#print axioms constant_certificate
-- W35
#print axioms FinProb.Pr_pos_le_mean
#print axioms FinProb.sq_mean_le
#print axioms FinProb.E_sq_eq_sum
#print axioms FinProb.mean_le_max_cond
#print axioms FinProb.witness_reduction
#print axioms FinProb.witness_reduction_max
#print axioms witness_reduction_uniform
#print axioms contains_ranks_iff
#print axioms blockStd_avoids
#print axioms ranks_perm_range
#print axioms erdos_szekeres_contains
#print axioms not_avoid_both
-- W90/W91 block flip (`BlockFlip.lean`): checker and reductions
#print axioms containsB_iff
#print axioms numContaining_eq
#print axioms card_Perms_contains
#print axioms dsum_perm
#print axioms blockFlipAt_of_sweepB
-- explicit permutations (kernel)
#print axioms perm3416725_contains_1234
#print axioms perm3416725_avoids_1324
#print axioms perm145278369_contains_123456
#print axioms perm145278369_avoids_124356
-- 1234 vs 1324 (kernel for n ≤ 8, native_decide for n = 9); 123456 vs 124356 (kernel for n ≤ 7)
#print axioms count_1234_eq_count_1324_of_le_6
#print axioms count_1234_sub_count_1324_7
#print axioms count_1234_sub_count_1324_8
#print axioms count_1234_sub_count_1324_9
#print axioms count_123456_eq_count_124356_of_le_8
#print axioms count_123456_sub_count_124356_9
-- block-flip instances: exact counts (kernel for n = 7 and for (1,1) at n = 8; native_decide otherwise)
#print axioms blockFlip_1_1_7
#print axioms blockFlip_12_1_7
#print axioms blockFlip_1_12_7
#print axioms blockFlip_21_1_7
#print axioms blockFlip_12_12_7
#print axioms blockFlip_21_21_7
#print axioms blockFlip_1_1_8
#print axioms blockFlip_12_1_8
#print axioms blockFlip_1_12_8
#print axioms blockFlip_21_1_8
#print axioms blockFlip_12_12_8
#print axioms blockFlip_21_21_8
#print axioms blockFlip_1_1_9
#print axioms blockFlip_12_1_9
#print axioms blockFlip_1_12_9
#print axioms blockFlip_21_1_9
#print axioms blockFlip_12_12_9
#print axioms blockFlip_21_21_9
-- all |α|, |β| ≤ 2, n ≤ 8 (native_decide)
#print axioms blockFlipAt_of_le_2_of_le_8

end Superpatterns
