import Superpatterns.Certificates
import Superpatterns.TheoremA
import Superpatterns.Numeric
import Superpatterns.Witness
import Superpatterns.BlockSplit
import Superpatterns.ErdosSzekeres
import Superpatterns.Interleaving
import Superpatterns.Lattice

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
#print axioms FinProb.cluster_sieve_le
#print axioms FinProb.Pr_pos_le_mean_div_cluster
#print axioms uniform_cluster_sieve
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
-- W58/W61 (Lattice)
#print axioms coord_diff_le
#print axioms monotone_path_cells_le
#print axioms single_chain_traversal_le
#print axioms total_chain_steps_bound
#print axioms coarse_trajectory_entropy_bound
#print axioms coarse_spatial_entropy_bits
-- W66 (Theorem 3.1: Backward Chain Monotonicity)
#print axioms backward_chain_monotonicity
#print axioms backward_chain_strict_monotonicity
-- W72 (Streamline Buffer Reservation)
#print axioms bundle_width_ge_one
#print axioms bundle_width_ge_two
#print axioms bundle_total_width_le
#print axioms bundle_tracks_disjoint
-- W73 (Forward Descent Chain Strict Increasing Invariant)
#print axioms forward_descent_chain_strict_increasing
-- W74 (Master Sieve Bound)
#print axioms uniform_superpattern_failure_le_sum
#print axioms uniform_mean_missing_le_card_mul_max
#print axioms uniform_master_sieve_bound
-- W75 (Discrete Macroscopic Grid Concentration & Sieve Domination)
#print axioms FinProb.Pr_exists_le
#print axioms FinProb.macro_grid_failure_le
#print axioms uniform_discrete_macro_sieve_bound
-- W76 (Multi-Chain Discrete Grid Embedding & Super-Factorial Domination)
#print axioms card_perms
#print axioms card_perms_le_pow
#print axioms uniform_master_sieve_pow_bound
#print axioms FinProb.Pr_or_le
#print axioms FinProb.multichain_grid_failure_le
#print axioms uniform_multichain_discrete_sieve_bound

end Superpatterns
