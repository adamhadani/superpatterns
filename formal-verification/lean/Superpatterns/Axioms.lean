import Superpatterns.Certificates
import Superpatterns.TheoremA
import Superpatterns.Numeric

/-!
# Axiom audit

`lake build` prints the axioms used by each main theorem.  Expected:

* certificates: `propext`, `Classical.choice`, `Quot.sound`, **`Lean.ofReduceBool`** (native_decide);
* `sp3_example`, `sp4_example`: no `Lean.ofReduceBool` (kernel `decide`);
* `theoremA`, `lemma1_concrete`, `patCount_le_sum_W`: standard axioms only (no `sorryAx`);
* `tilt_bound`, `pair_sum_le`, `card_le_sum_fiber`, `constant_certificate`, `checker_sound`:
  standard axioms only.
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

end Superpatterns
