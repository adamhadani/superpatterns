import Mathlib
import Superpatterns.Patterns

/-!
# The witness (second-moment) reduction — W28 Theorem 1.1 / paper Proposition 15

## Formalisation choice

A *finite probability space* is a `Fintype Ω` with a weight function `p : Ω → ℝ`, `p ≥ 0`,
`∑ p = 1` (`FinProb`).  Expectation is the weighted sum `E f = ∑ ω, p ω * f ω`; the probability of
an event `B : Ω → Prop` is `Pr B = E 1_B`; `E[f ; B] = E (1_B f)`.  This is the simplest faithful
model: every statement of Prop. 15 is an identity/inequality between finite sums, and the uniform
law on `S_n` (the only case used in the project) is an instance with `Ω = {σ : List ℕ // σ ~ range n}`
and `p = 1/n!`.  Conditional expectations are stated *without division*, as
"`E[M ; B] ≤ c · Pr B`" (i.e. `E[M | B] ≤ c` whenever `Pr B > 0`, and vacuous otherwise); a divided
form `condE` with the `max` over the witness values is derived in `witness_reduction_max`.

Given a finite family of events `A π` (`π : ι`, `ι` a `Fintype`) let `M ω = #{π | ω ∈ A π}` and
`μ = E M`.  Proved (all sorry-free):

* (a) `mean_eq_E_on_pos`: `μ = E[M ; M > 0]`; `Pr_pos_le_mean`: `Pr(M>0) ≤ μ` (`R ≥ 1`);
  `Pr_le_one`: `Pr(M>0) ≤ 1` (`R ≥ μ`); `mean_eq_sum_Pr`: `μ = ∑ π, Pr(A π)`.
* (b) `sq_mean_le`: `μ² ≤ E[M²] · Pr(M>0)` (Cauchy–Schwarz);
  `E_sq_eq_sum`: `E[M²] = ∑ π, E[M ; A π]`;
  `mean_le_max_cond`: if `E[M ; A π] ≤ Λ · Pr(A π)` for all `π` then `μ ≤ Λ · Pr(M>0)`
  (i.e. `R ≤ max_π Λ_π`).
* (c) `witness_reduction`: for any `W : Ω → 𝒲` (`𝒲` a `Fintype`), if `E[M ; W = w, M>0] ≤ c · Pr(W = w, M>0)`
  for every `w` then `μ ≤ c · Pr(M>0)`; `witness_reduction_max`: `μ ≤ (max_w E[M | W = w, M>0]) · Pr(M>0)`.
-/

namespace Superpatterns

open Finset

/-- A finite probability space: nonnegative weights on a finite type summing to `1`. -/
structure FinProb (Ω : Type*) [Fintype Ω] where
  p : Ω → ℝ
  nonneg : ∀ ω, 0 ≤ p ω
  sum_one : ∑ ω, p ω = 1

namespace FinProb

variable {Ω : Type*} [Fintype Ω] (P : FinProb Ω)

open Classical in
/-- Expectation. -/
noncomputable def E (f : Ω → ℝ) : ℝ := ∑ ω, P.p ω * f ω

open Classical in
/-- Indicator of an event. -/
noncomputable def ind (B : Ω → Prop) (ω : Ω) : ℝ := if B ω then 1 else 0

/-- Probability of an event. -/
noncomputable def Pr (B : Ω → Prop) : ℝ := P.E (ind B)

/-- `E[f ; B] = E[f 1_B]`. -/
noncomputable def Eon (f : Ω → ℝ) (B : Ω → Prop) : ℝ := P.E (fun ω => ind B ω * f ω)

theorem E_add (f g : Ω → ℝ) : P.E (fun ω => f ω + g ω) = P.E f + P.E g := by
  simp [E, mul_add, sum_add_distrib]

theorem E_sum {κ : Type*} (s : Finset κ) (f : κ → Ω → ℝ) :
    P.E (fun ω => ∑ j ∈ s, f j ω) = ∑ j ∈ s, P.E (f j) := by
  simp only [E, mul_sum]
  exact sum_comm

theorem E_mono {f g : Ω → ℝ} (h : ∀ ω, f ω ≤ g ω) : P.E f ≤ P.E g :=
  sum_le_sum fun ω _ => mul_le_mul_of_nonneg_left (h ω) (P.nonneg ω)

theorem E_nonneg {f : Ω → ℝ} (h : ∀ ω, 0 ≤ f ω) : 0 ≤ P.E f :=
  sum_nonneg fun ω _ => mul_nonneg (P.nonneg ω) (h ω)

theorem E_const_mul (c : ℝ) (f : Ω → ℝ) : P.E (fun ω => c * f ω) = c * P.E f := by
  simp [E, mul_sum, mul_left_comm]

theorem E_congr {f g : Ω → ℝ} (h : ∀ ω, f ω = g ω) : P.E f = P.E g := by
  simp [E, h]

omit [Fintype Ω] in
theorem ind_nonneg (B : Ω → Prop) (ω : Ω) : 0 ≤ ind B ω := by
  unfold ind; split_ifs <;> norm_num

omit [Fintype Ω] in
theorem ind_le_one (B : Ω → Prop) (ω : Ω) : ind B ω ≤ 1 := by
  unfold ind; split_ifs <;> norm_num

theorem Pr_nonneg (B : Ω → Prop) : 0 ≤ P.Pr B := P.E_nonneg (ind_nonneg B)

theorem Pr_le_one (B : Ω → Prop) : P.Pr B ≤ 1 := by
  have : P.E (fun _ => (1 : ℝ)) = 1 := by simp [E, P.sum_one]
  rw [← this]
  exact P.E_mono (ind_le_one B)

/-- If `Pr B = 0` then `E[f ; B] = 0` for every `f`. -/
theorem Eon_eq_zero_of_Pr_eq_zero {B : Ω → Prop} (h : P.Pr B = 0) (f : Ω → ℝ) :
    P.Eon f B = 0 := by
  classical
  have hz : ∀ ω, P.p ω * ind B ω = 0 := by
    have := (sum_eq_zero_iff_of_nonneg (fun ω _ => mul_nonneg (P.nonneg ω) (ind_nonneg B ω))).1 h
    exact fun ω => this ω (mem_univ ω)
  unfold Eon E
  refine sum_eq_zero fun ω _ => ?_
  rw [← mul_assoc, hz ω, zero_mul]

/-! ### The count `M` and its mean -/

variable {ι : Type*} [Fintype ι] (A : ι → Ω → Prop)

/-- `M ω = #{π | A π ω}` (as a real number). -/
noncomputable def cnt (ω : Ω) : ℝ := ∑ π, ind (A π) ω

omit [Fintype Ω] in
theorem cnt_nonneg (ω : Ω) : 0 ≤ cnt A ω := sum_nonneg fun π _ => ind_nonneg (A π) ω

omit [Fintype Ω] in
theorem cnt_pos_iff (ω : Ω) : 0 < cnt A ω ↔ ∃ π, A π ω := by
  classical
  constructor
  · intro h
    by_contra hne
    simp only [not_exists] at hne
    have : cnt A ω = 0 := sum_eq_zero fun π _ => by simp [ind, hne π]
    linarith
  · rintro ⟨π, hπ⟩
    refine lt_of_lt_of_le ?_ (single_le_sum (fun π' _ => ind_nonneg (A π') ω) (mem_univ π))
    simp [ind, hπ]

omit [Fintype Ω] in
/-- `M ≥ 1` on `{M > 0}`. -/
theorem one_le_cnt_of_pos {ω : Ω} (h : 0 < cnt A ω) : 1 ≤ cnt A ω := by
  classical
  obtain ⟨π, hπ⟩ := (cnt_pos_iff A ω).1 h
  refine le_trans ?_ (single_le_sum (fun π' _ => ind_nonneg (A π') ω) (mem_univ π))
  simp [ind, hπ]

/-- (a) `μ = E[M ; M > 0]`. -/
theorem mean_eq_E_on_pos : P.E (cnt A) = P.Eon (cnt A) (fun ω => 0 < cnt A ω) := by
  classical
  refine P.E_congr fun ω => ?_
  unfold ind
  split_ifs with h
  · ring
  · have := cnt_nonneg A ω
    have : cnt A ω = 0 := by linarith
    simp [this]

/-- (a) `Pr(M > 0) ≤ μ`, i.e. `R = μ / Pr(M>0) ≥ 1`. -/
theorem Pr_pos_le_mean : P.Pr (fun ω => 0 < cnt A ω) ≤ P.E (cnt A) := by
  classical
  refine P.E_mono fun ω => ?_
  unfold ind
  split_ifs with h
  · exact one_le_cnt_of_pos A h
  · exact cnt_nonneg A ω

/-- (a) `μ = ∑ π, Pr(A π)` (linearity). -/
theorem mean_eq_sum_Pr : P.E (cnt A) = ∑ π, P.Pr (A π) := by
  unfold cnt Pr
  exact P.E_sum univ (fun π => ind (A π))

/-! ### (b) Second moment -/

/-- Cauchy–Schwarz / Paley–Zygmund at level 0: `μ² ≤ E[M²] · Pr(M > 0)`. -/
theorem sq_mean_le :
    (P.E (cnt A)) ^ 2 ≤ P.E (fun ω => cnt A ω ^ 2) * P.Pr (fun ω => 0 < cnt A ω) := by
  classical
  unfold Pr E
  refine sum_sq_le_sum_mul_sum_of_sq_le_mul univ
    (fun ω _ => mul_nonneg (P.nonneg ω) (sq_nonneg _))
    (fun ω _ => mul_nonneg (P.nonneg ω) (ind_nonneg _ ω)) fun ω _ => ?_
  unfold ind
  split_ifs with h
  · nlinarith [P.nonneg ω, sq_nonneg (P.p ω), sq_nonneg (cnt A ω)]
  · have := cnt_nonneg A ω
    have : cnt A ω = 0 := by linarith
    simp [this]

/-- `E[M²] = ∑ π, E[M ; A π]`. -/
theorem E_sq_eq_sum : P.E (fun ω => cnt A ω ^ 2) = ∑ π, P.Eon (cnt A) (A π) := by
  unfold Eon
  rw [← P.E_sum]
  refine P.E_congr fun ω => ?_
  simp only [← sum_mul]
  unfold cnt
  ring

/-- (b) `R ≤ max_π Λ_π`: if `E[M ; A π] ≤ Λ · Pr(A π)` for every `π` (i.e. `Λ_π ≤ Λ`), then
`μ ≤ Λ · Pr(M > 0)`. -/
theorem mean_le_max_cond {Λ : ℝ} (hΛ : ∀ π, P.Eon (cnt A) (A π) ≤ Λ * P.Pr (A π)) :
    P.E (cnt A) ≤ Λ * P.Pr (fun ω => 0 < cnt A ω) := by
  have h1 := P.sq_mean_le A
  have h2 : P.E (fun ω => cnt A ω ^ 2) ≤ Λ * P.E (cnt A) := by
    rw [P.E_sq_eq_sum, P.mean_eq_sum_Pr, mul_sum]
    exact sum_le_sum fun π _ => hΛ π
  have hμ : 0 ≤ P.E (cnt A) := P.E_nonneg (cnt_nonneg A)
  have hPr : 0 ≤ P.Pr (fun ω => 0 < cnt A ω) := P.Pr_nonneg _
  rcases hμ.eq_or_lt with h0 | hpos
  · -- μ = 0 forces Pr(M>0) = 0
    have := P.Pr_pos_le_mean A
    rw [← h0] at this ⊢
    have : P.Pr (fun ω => 0 < cnt A ω) = 0 := le_antisymm this hPr
    rw [this, mul_zero]
  · have h3 : P.E (cnt A) ^ 2 ≤ Λ * P.E (cnt A) * P.Pr (fun ω => 0 < cnt A ω) :=
      h1.trans (mul_le_mul_of_nonneg_right h2 hPr)
    nlinarith

/-! ### (c) The witness form -/

/-- (c) **Witness reduction** (undivided form). For any witness map `W : Ω → 𝒲` and any `c` with
`E[M ; W = w, M > 0] ≤ c · Pr(W = w, M > 0)` for every `w` (i.e. `E[M | W = w] ≤ c` on
`{M > 0}`), we have `μ ≤ c · Pr(M > 0)`, i.e. `R ≤ c`. -/
theorem witness_reduction {𝒲 : Type*} [Fintype 𝒲] (W : Ω → 𝒲) {c : ℝ}
    (hc : ∀ w, P.Eon (cnt A) (fun ω => W ω = w ∧ 0 < cnt A ω) ≤
      c * P.Pr (fun ω => W ω = w ∧ 0 < cnt A ω)) :
    P.E (cnt A) ≤ c * P.Pr (fun ω => 0 < cnt A ω) := by
  classical
  -- decompose `μ = ∑_w E[M ; W = w, M>0]` and `Pr(M>0) = ∑_w Pr(W = w, M>0)`
  have hμ : P.E (cnt A) = ∑ w, P.Eon (cnt A) (fun ω => W ω = w ∧ 0 < cnt A ω) := by
    unfold Eon
    rw [← P.E_sum]
    refine P.E_congr fun ω => ?_
    simp only [← sum_mul]
    unfold ind
    by_cases h : 0 < cnt A ω
    · simp [h]
    · have := cnt_nonneg A ω
      have : cnt A ω = 0 := by linarith
      simp [this]
  have hPr : P.Pr (fun ω => 0 < cnt A ω) = ∑ w, P.Pr (fun ω => W ω = w ∧ 0 < cnt A ω) := by
    unfold Pr
    rw [← P.E_sum]
    refine P.E_congr fun ω => ?_
    unfold ind
    by_cases h : 0 < cnt A ω <;> simp [h]
  rw [hμ, hPr, mul_sum]
  exact sum_le_sum fun w _ => hc w

/-- Conditional expectation `E[M | W = w, M > 0]` (with the convention `0/0 = 0`). -/
noncomputable def condE {𝒲 : Type*} (W : Ω → 𝒲) (w : 𝒲) : ℝ :=
  P.Eon (cnt A) (fun ω => W ω = w ∧ 0 < cnt A ω) / P.Pr (fun ω => W ω = w ∧ 0 < cnt A ω)

/-- (c) **Witness reduction** (divided form): `μ ≤ (max_w E[M | W = w]) · Pr(M > 0)`. -/
theorem witness_reduction_max {𝒲 : Type*} [Fintype 𝒲] [Nonempty 𝒲] (W : Ω → 𝒲) :
    P.E (cnt A) ≤ (univ.sup' univ_nonempty (P.condE A W)) * P.Pr (fun ω => 0 < cnt A ω) := by
  refine P.witness_reduction A W fun w => ?_
  have hle : P.condE A W w ≤ univ.sup' univ_nonempty (P.condE A W) :=
    le_sup' (P.condE A W) (mem_univ w)
  have hPr := P.Pr_nonneg (fun ω => W ω = w ∧ 0 < cnt A ω)
  rcases hPr.eq_or_lt with h0 | hpos
  · rw [P.Eon_eq_zero_of_Pr_eq_zero h0.symm, ← h0, mul_zero]
  · calc P.Eon (cnt A) (fun ω => W ω = w ∧ 0 < cnt A ω)
        = P.condE A W w * P.Pr (fun ω => W ω = w ∧ 0 < cnt A ω) := by
          unfold condE; rw [div_mul_cancel₀ _ hpos.ne']
      _ ≤ _ := mul_le_mul_of_nonneg_right hle hPr

end FinProb

/-! ### The uniform model on `S_n` and the missing-pattern count -/

/-- Permutations of `{0,…,n-1}` as lists. -/
abbrev Perms (n : ℕ) := {σ : List ℕ // σ.Perm (List.range n)}

instance (n : ℕ) : Fintype (Perms n) :=
  Fintype.subtype (List.permutations (List.range n)).toFinset
    (fun σ => by simp [List.mem_permutations])

instance (n : ℕ) : Nonempty (Perms n) := ⟨⟨List.range n, List.Perm.refl _⟩⟩

/-- The uniform law on a nonempty finite type. -/
noncomputable def FinProb.uniform (Ω : Type*) [Fintype Ω] [Nonempty Ω] : FinProb Ω where
  p := fun _ => (Fintype.card Ω : ℝ)⁻¹
  nonneg := fun _ => by positivity
  sum_one := by
    simp only [sum_const, card_univ, nsmul_eq_mul]
    exact mul_inv_cancel₀ (by exact_mod_cast Fintype.card_ne_zero)

/-- The event `A_π = {σ : π ⊄ σ}`, indexed by `π ∈ S_k`. -/
def missing (n k : ℕ) (π : Perms k) (σ : Perms n) : Prop := ¬ Contains σ.1 π.1

/-- `M(σ) > 0` iff `σ` is not a `k`-superpattern. -/
theorem cnt_missing_pos_iff (n k : ℕ) (σ : Perms n) :
    0 < FinProb.cnt (missing n k) σ ↔ ¬ IsSuperpattern k σ.1 := by
  rw [FinProb.cnt_pos_iff]
  constructor
  · rintro ⟨π, hπ⟩ hsup
    exact hπ (hsup π.1 π.2)
  · intro h
    simp only [IsSuperpattern, not_forall] at h
    obtain ⟨π, hπ, hc⟩ := h
    exact ⟨⟨π, hπ⟩, hc⟩

/-- Prop. 15(c) in the uniform model: for `σ_n` uniform on `S_n`, `M` the number of missing
`k`-patterns, and any witness `W`, `μ ≤ (max_w E[M | W = w, M>0]) · Pr(σ_n is not a k-superpattern)`. -/
theorem witness_reduction_uniform (n k : ℕ) {𝒲 : Type*} [Fintype 𝒲] [Nonempty 𝒲]
    (W : Perms n → 𝒲) :
    (FinProb.uniform (Perms n)).E (FinProb.cnt (missing n k)) ≤
      (univ.sup' univ_nonempty ((FinProb.uniform (Perms n)).condE (missing n k) W)) *
        (FinProb.uniform (Perms n)).Pr (fun σ => ¬ IsSuperpattern k σ.1) := by
  have := (FinProb.uniform (Perms n)).witness_reduction_max (missing n k) W
  convert this using 3
  ext σ
  exact (cnt_missing_pos_iff n k σ).symm

end Superpatterns
