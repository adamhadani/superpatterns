import Superpatterns.Certificates
import Superpatterns.TheoremA
import Superpatterns.Numeric
import Superpatterns.Witness
import Superpatterns.BlockSplit
import Superpatterns.ErdosSzekeres
import Superpatterns.Interleaving

/-!
# Axiom audit

`lake build` prints the axioms used by each main theorem.  Expected:

* certificates: `propext`, `Classical.choice`, `Quot.sound`, **`Lean.ofReduceBool`** (native_decide);
* `sp3_example`, `sp4_example`: no `Lean.ofReduceBool` (kernel `decide`);
* `theoremA`, `lemma1_concrete`, `patCount_le_sum_W`: standard axioms only (no `sorryAx`);
* `tilt_bound`, `pair_sum_le`, `card_le_sum_fiber`, `constant_certificate`, `checker_sound`:
  standard axioms only;
* W35 (`Witness.lean`, `BlockSplit.lean`, `ErdosSzekeres.lean`): standard axioms only.
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
-- W43/W45/W46/W47
#print axioms strictly_increasing_avoids_21
#print axioms strictly_increasing_avoids_321
#print axioms two_chain_word_entropy_bound
#print axioms multichain_word_entropy_pow
#print axioms lookahead_entropy_pow
#print axioms disjoint_blocks_no_pos_overlap
#print axioms disjoint_blocks_no_val_overlap
#print axioms window_separation
#print axioms lookahead_bypass_order
#print axioms supercritical_velocity_quad
#print axioms two_blocks_len_le

end Superpatterns
