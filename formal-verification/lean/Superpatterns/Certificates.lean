import Superpatterns.Checker

/-!
# Certificates: `sp(7) ≤ 23` and `sp(8) ≤ 30` (also the length-31 and length-32 witnesses)

The witnesses below are checked by running the verified checker (`Checker.lean`) through
`native_decide`.  `native_decide` trusts the Lean compiler and the runtime (it adds the axiom
`Lean.ofReduceBool`); everything else is checked by the kernel.  Small cases are also checked
by the kernel itself (`decide +kernel`) as a sanity test of the checker.
-/

namespace Superpatterns

/-- Witness for `sp(7) ≤ 23`. -/
def σ7 : List ℕ :=
  [7, 20, 13, 10, 2, 18, 23, 4, 12, 16, 8, 5, 19, 15, 1, 9, 22, 14, 6, 17, 11, 3, 21]

/-- Witness for `sp(8) ≤ 32`. -/
def σ8 : List ℕ :=
  [13, 26, 3, 31, 11, 16, 23, 8, 20, 12, 30, 6, 18, 27, 7, 1, 21, 29, 15, 4, 9, 22, 32, 19, 2,
   14, 24, 10, 28, 5, 17, 25]

/-- Witness for `sp(8) ≤ 31`. -/
def σ8' : List ℕ :=
  [25, 21, 11, 4, 27, 8, 17, 19, 1, 13, 31, 5, 23, 16, 26, 10, 6, 29, 15, 20, 28, 3, 9, 14, 24,
   2, 12, 30, 18, 7, 22]

theorem σ7_length : σ7.length = 23 := by decide
theorem σ7_perm : σ7.Perm (List.range' 1 23) := by decide
theorem σ8_length : σ8.length = 32 := by decide
theorem σ8_perm : σ8.Perm (List.range' 1 32) := by decide
/-- Witness for `sp(8) ≤ 30` (headline `k = 8` witness). -/
def σ8'' : List ℕ :=
  [13, 4, 25, 18, 8, 30, 12, 22, 1, 28, 19, 10, 6, 14, 24, 27, 3, 16, 21, 11, 5, 20, 29, 15, 7,
   23, 2, 17, 26, 9]

theorem σ8'_length : σ8'.length = 31 := by decide
theorem σ8'_perm : σ8'.Perm (List.range' 1 31) := by decide
theorem σ8''_length : σ8''.length = 30 := by decide
theorem σ8''_perm : σ8''.Perm (List.range' 1 30) := by decide

/-- Sanity checks evaluated by the kernel (`decide`). -/
theorem sp3_example : IsSuperpattern 3 [2, 5, 3, 1, 4] := checker_sound (by decide +kernel)
theorem sp4_example : IsSuperpattern 4 [5, 1, 9, 4, 7, 2, 6, 8, 3] := checker_sound (by decide +kernel)

/-- `sp(7) ≤ 23`. -/
theorem σ7_superpattern : IsSuperpattern 7 σ7 := checker_sound (by native_decide)

/-- `sp(8) ≤ 32`. -/
theorem σ8_superpattern : IsSuperpattern 8 σ8 := checker_sound (by native_decide)

/-- `sp(8) ≤ 31`. -/
theorem σ8'_superpattern : IsSuperpattern 8 σ8' := checker_sound (by native_decide)

/-- `sp(8) ≤ 30`. -/
theorem σ8''_superpattern : IsSuperpattern 8 σ8'' := checker_sound (by native_decide)

end Superpatterns
