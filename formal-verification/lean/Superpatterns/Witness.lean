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
`μ = E M`.  Proved (all complete, no placeholders):

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

/-- (Cluster Sieve Inequality, undivided form) If on `{M > 0}` we have `R ≤ M ω`, then
`R · Pr(M > 0) ≤ E[M]`. -/
theorem cluster_sieve_le {R : ℝ}
    (hR : ∀ ω, 0 < cnt A ω → R ≤ cnt A ω) :
    R * P.Pr (fun ω => 0 < cnt A ω) ≤ P.E (cnt A) := by
  classical
  unfold Pr
  rw [← P.E_const_mul]
  refine P.E_mono fun ω => ?_
  unfold ind
  split_ifs with h
  · exact (mul_one R).symm ▸ hR ω h
  · have h0 : cnt A ω = 0 := by
      have := cnt_nonneg A ω
      linarith
    rw [mul_zero, h0]

/-- (Cluster Sieve Inequality, divided form) If `0 < R` and on `{M > 0}` we have `R ≤ M ω`, then
`Pr(M > 0) ≤ (1 / R) · E[M]`. -/
theorem Pr_pos_le_mean_div_cluster {R : ℝ} (hRpos : 0 < R)
    (hR : ∀ ω, 0 < cnt A ω → R ≤ cnt A ω) :
    P.Pr (fun ω => 0 < cnt A ω) ≤ (1 / R) * P.E (cnt A) := by
  have h := P.cluster_sieve_le A hR
  have hRinv : 0 ≤ R⁻¹ := le_of_lt (inv_pos.2 hRpos)
  have h2 := mul_le_mul_of_nonneg_left h hRinv
  rw [← mul_assoc, inv_mul_cancel₀ hRpos.ne', one_mul] at h2
  rw [one_div]
  exact h2

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

/-- Cluster sieve in the uniform model on `S_n`: If every non-superpattern misses at least `R` patterns,
then `Pr(σ_n is not a k-superpattern) ≤ (1 / R) · E[M]`. -/
theorem uniform_cluster_sieve (n k : ℕ) {R : ℝ} (hRpos : 0 < R)
    (hR : ∀ σ : Perms n, ¬ IsSuperpattern k σ.1 → R ≤ FinProb.cnt (missing n k) σ) :
    (FinProb.uniform (Perms n)).Pr (fun σ => ¬ IsSuperpattern k σ.1) ≤
      (1 / R) * (FinProb.uniform (Perms n)).E (FinProb.cnt (missing n k)) := by
  have h := (FinProb.uniform (Perms n)).Pr_pos_le_mean_div_cluster (missing n k) hRpos (fun σ hpos => by
    have hnot := (cnt_missing_pos_iff n k σ).1 hpos
    exact hR σ hnot)
  convert h using 2
  ext σ
  exact (cnt_missing_pos_iff n k σ).symm

/-- Master Sieve Bound: Superpattern failure probability is bounded by expected missing count. -/
theorem uniform_superpattern_failure_le_sum (n k : ℕ) :
    (FinProb.uniform (Perms n)).Pr (fun σ => ¬ IsSuperpattern k σ.1) ≤
      (FinProb.uniform (Perms n)).E (FinProb.cnt (missing n k)) := by
  have h := (FinProb.uniform (Perms n)).Pr_pos_le_mean (missing n k)
  convert h using 2
  ext σ
  exact (cnt_missing_pos_iff n k σ).symm

/-- Expected missing pattern count is bounded by k! * P_max whenever every pattern avoidance
    probability is bounded by P_max. -/
theorem uniform_mean_missing_le_card_mul_max (n k : ℕ) (P_max : ℝ)
    (hP : ∀ π : Perms k, (FinProb.uniform (Perms n)).Pr (missing n k π) ≤ P_max) :
    (FinProb.uniform (Perms n)).E (FinProb.cnt (missing n k)) ≤ (Fintype.card (Perms k) : ℝ) * P_max := by
  have hsum : (FinProb.uniform (Perms n)).E (FinProb.cnt (missing n k)) =
      ∑ π : Perms k, (FinProb.uniform (Perms n)).Pr (missing n k π) := by
    exact (FinProb.uniform (Perms n)).mean_eq_sum_Pr (missing n k)
  rw [hsum]
  have hcard : (∑ _π : Perms k, P_max) = (Fintype.card (Perms k) : ℝ) * P_max := by
    simp [Finset.sum_const, nsmul_eq_mul]
  rw [← hcard]
  exact Finset.sum_le_sum (fun π _ => hP π)

/-- Master Sharp Sieve Bound (Workstream W74):
    The probability that a uniform random permutation σ_n is not a k-superpattern
    is bounded by k! * P_max whenever every pattern avoidance probability is bounded by P_max. -/
theorem uniform_master_sieve_bound (n k : ℕ) (P_max : ℝ)
    (hP : ∀ π : Perms k, (FinProb.uniform (Perms n)).Pr (missing n k π) ≤ P_max) :
    (FinProb.uniform (Perms n)).Pr (fun σ => ¬ IsSuperpattern k σ.1) ≤
      (Fintype.card (Perms k) : ℝ) * P_max := by
  have h1 := uniform_superpattern_failure_le_sum n k
  have h2 := uniform_mean_missing_le_card_mul_max n k P_max hP
  exact le_trans h1 h2

/-- Cardinality of Perms n is n! (Workstream W76). -/
theorem card_perms (n : ℕ) : Fintype.card (Perms n) = n.factorial := by
  have H : ∀ σ : List ℕ, σ ∈ (List.permutations (List.range n)).toFinset ↔ σ.Perm (List.range n) := by
    intro σ
    simp [List.mem_permutations]
  have hcard := Fintype.card_of_subtype (List.permutations (List.range n)).toFinset H
  rw [hcard]
  rw [List.toFinset_card_of_nodup]
  · rw [List.length_permutations]
    simp
  · exact List.nodup_permutations _ List.nodup_range

/-- Factorial bound: |Perms n| ≤ n^n (Workstream W76). -/
theorem card_perms_le_pow (n : ℕ) : (Fintype.card (Perms n) : ℝ) ≤ (n : ℝ) ^ n := by
  rw [card_perms n]
  exact_mod_cast Nat.factorial_le_pow n

/-- Super-Factorial Domination: superpattern failure probability is bounded by k^k * P_max (Workstream W76). -/
theorem uniform_master_sieve_pow_bound (n k : ℕ) (P_max : ℝ) (hPmax : 0 ≤ P_max)
    (hP : ∀ π : Perms k, (FinProb.uniform (Perms n)).Pr (missing n k π) ≤ P_max) :
    (FinProb.uniform (Perms n)).Pr (fun σ => ¬ IsSuperpattern k σ.1) ≤
      (k : ℝ) ^ k * P_max := by
  have h1 := uniform_master_sieve_bound n k P_max hP
  have h2 := mul_le_mul_of_nonneg_right (card_perms_le_pow k) hPmax
  exact le_trans h1 h2

/-- Union bound for two events in a FinProb space (Workstream W76). -/
theorem FinProb.Pr_or_le {Ω : Type*} [Fintype Ω] (P : FinProb Ω) (A B : Ω → Prop) :
    P.Pr (fun ω => A ω ∨ B ω) ≤ P.Pr A + P.Pr B := by
  have hsum : P.Pr A + P.Pr B = P.E (fun ω => ind A ω + ind B ω) := by
    unfold Pr
    rw [P.E_add]
  rw [hsum]
  unfold Pr
  refine P.E_mono (fun ω => ?_)
  unfold ind
  by_cases hA : A ω <;> by_cases hB : B ω
  · have : (fun ω => A ω ∨ B ω) ω := Or.inl hA
    rw [if_pos this, if_pos hA, if_pos hB]
    linarith
  · have : (fun ω => A ω ∨ B ω) ω := Or.inl hA
    rw [if_pos this, if_pos hA, if_neg hB]
    linarith
  · have : (fun ω => A ω ∨ B ω) ω := Or.inr hB
    rw [if_pos this, if_neg hA, if_pos hB]
    linarith
  · have : ¬(fun ω => A ω ∨ B ω) ω := by
      intro h; cases h with | inl ha => exact hA ha | inr hb => exact hB hb
    rw [if_neg this, if_neg hA, if_neg hB]
    linarith

/-- Finite union bound for families of events in a FinProb space. -/
theorem FinProb.Pr_exists_le {Ω ι : Type*} [Fintype Ω] [Fintype ι] (P : FinProb Ω)
    (B : ι → Ω → Prop) :
    P.Pr (fun ω => ∃ i, B i ω) ≤ ∑ i, P.Pr (B i) := by
  have hpos : P.Pr (fun ω => 0 < FinProb.cnt B ω) ≤ P.E (FinProb.cnt B) := P.Pr_pos_le_mean B
  have hmean : P.E (FinProb.cnt B) = ∑ i, P.Pr (B i) := P.mean_eq_sum_Pr B
  rw [hmean] at hpos
  convert hpos using 2
  ext ω
  exact (FinProb.cnt_pos_iff B ω).symm

/-- Macroscopic Grid Regularity Union Bound (Workstream W75):
    For an M x M grid, the probability that any cell fails is bounded by M^2 * P_box. -/
theorem FinProb.macro_grid_failure_le {Ω : Type*} [Fintype Ω] (P : FinProb Ω)
    (M : ℕ) (B : Fin M × Fin M → Ω → Prop) (P_box : ℝ)
    (hB : ∀ cell, P.Pr (B cell) ≤ P_box) :
    P.Pr (fun ω => ∃ cell, B cell ω) ≤ (M : ℝ)^2 * P_box := by
  have h := P.Pr_exists_le B
  have hsum : (∑ cell, P.Pr (B cell)) ≤ ∑ _cell : Fin M × Fin M, P_box :=
    Finset.sum_le_sum (fun cell _ => hB cell)
  have hcard : (∑ _cell : Fin M × Fin M, P_box) = (Fintype.card (Fin M × Fin M) : ℝ) * P_box := by
    simp [Finset.sum_const, nsmul_eq_mul]
  have hM2 : (Fintype.card (Fin M × Fin M) : ℝ) = (M : ℝ)^2 := by
    simp [Fintype.card_prod]
    ring
  rw [hM2] at hcard
  exact le_trans h (le_trans hsum (le_of_eq hcard))

/-- Workstream W75: Discrete Macroscopic Grid Sieve Domination.
    If each target permutation avoidance is bounded by a macroscopic grid failure bound
    (M^2 * P_box + P_embed), then the superpattern failure probability is bounded
    by k! * (M^2 * P_box + P_embed). -/
theorem uniform_discrete_macro_sieve_bound (n k M : ℕ) (P_box P_embed : ℝ)
    (hP : ∀ π : Perms k, (FinProb.uniform (Perms n)).Pr (missing n k π) ≤ (M : ℝ)^2 * P_box + P_embed) :
    (FinProb.uniform (Perms n)).Pr (fun σ => ¬ IsSuperpattern k σ.1) ≤
      (Fintype.card (Perms k) : ℝ) * ((M : ℝ)^2 * P_box + P_embed) := by
  exact uniform_master_sieve_bound n k ((M : ℝ)^2 * P_box + P_embed) hP

/-- Multi-Chain Discrete Grid Union Bound (Workstream W76):
    The failure probability over an M x M grid with d chains across macroscopic cells,
    intra-cell chain capacities, and boundary tracks is bounded by
    M^2 * P_macro + M^2 * d * P_chain + M * d * P_track. -/
theorem FinProb.multichain_grid_failure_le {Ω : Type*} [Fintype Ω] (P : FinProb Ω)
    (M d : ℕ)
    (B_macro : Fin M × Fin M → Ω → Prop)
    (B_chain : (Fin M × Fin M) × Fin d → Ω → Prop)
    (B_track : Fin M × Fin d → Ω → Prop)
    (P_macro P_chain P_track : ℝ)
    (h_macro : ∀ c, P.Pr (B_macro c) ≤ P_macro)
    (h_chain : ∀ ca, P.Pr (B_chain ca) ≤ P_chain)
    (h_track : ∀ ma, P.Pr (B_track ma) ≤ P_track) :
    P.Pr (fun ω => (∃ c, B_macro c ω) ∨ (∃ ca, B_chain ca ω) ∨ (∃ ma, B_track ma ω)) ≤
      (M : ℝ)^2 * P_macro + (M : ℝ)^2 * (d : ℝ) * P_chain + (M : ℝ) * (d : ℝ) * P_track := by
  have h_or1 := P.Pr_or_le (fun ω => ∃ c, B_macro c ω)
    (fun ω => (∃ ca, B_chain ca ω) ∨ (∃ ma, B_track ma ω))
  have h_or2 := P.Pr_or_le (fun ω => ∃ ca, B_chain ca ω) (fun ω => ∃ ma, B_track ma ω)
  have h_macro_bound : P.Pr (fun ω => ∃ c, B_macro c ω) ≤ (M : ℝ)^2 * P_macro :=
    P.macro_grid_failure_le M B_macro P_macro h_macro
  have h_chain_exists := P.Pr_exists_le B_chain
  have h_chain_sum : (∑ ca, P.Pr (B_chain ca)) ≤ ∑ _ca : (Fin M × Fin M) × Fin d, P_chain :=
    Finset.sum_le_sum (fun ca _ => h_chain ca)
  have h_chain_card : (∑ _ca : (Fin M × Fin M) × Fin d, P_chain) =
      (Fintype.card ((Fin M × Fin M) × Fin d) : ℝ) * P_chain := by
    simp [Finset.sum_const, nsmul_eq_mul]
  have h_chain_dim : (Fintype.card ((Fin M × Fin M) × Fin d) : ℝ) = (M : ℝ)^2 * (d : ℝ) := by
    simp only [Fintype.card_prod, Fintype.card_fin]
    push_cast
    ring
  rw [h_chain_dim] at h_chain_card
  have h_chain_bound : P.Pr (fun ω => ∃ ca, B_chain ca ω) ≤ (M : ℝ)^2 * (d : ℝ) * P_chain :=
    le_trans h_chain_exists (le_trans h_chain_sum (le_of_eq h_chain_card))
  have h_track_exists := P.Pr_exists_le B_track
  have h_track_sum : (∑ ma, P.Pr (B_track ma)) ≤ ∑ _ma : Fin M × Fin d, P_track :=
    Finset.sum_le_sum (fun ma _ => h_track ma)
  have h_track_card : (∑ _ma : Fin M × Fin d, P_track) =
      (Fintype.card (Fin M × Fin d) : ℝ) * P_track := by
    simp [Finset.sum_const, nsmul_eq_mul]
  have h_track_dim : (Fintype.card (Fin M × Fin d) : ℝ) = (M : ℝ) * (d : ℝ) := by
    simp only [Fintype.card_prod, Fintype.card_fin]
    push_cast
    ring
  rw [h_track_dim] at h_track_card
  have h_track_bound : P.Pr (fun ω => ∃ ma, B_track ma ω) ≤ (M : ℝ) * (d : ℝ) * P_track :=
    le_trans h_track_exists (le_trans h_track_sum (le_of_eq h_track_card))
  linarith [h_or1, h_or2, h_macro_bound, h_chain_bound, h_track_bound]

/-- Workstream W76: Multi-Chain Discrete Grid Sieve Domination.
    If each target permutation avoidance is bounded by the multi-chain grid failure bound
    (M^2 * P_macro + M^2 * d * P_chain + M * d * P_track), then the superpattern failure
    probability is bounded by k! * (M^2 * P_macro + M^2 * d * P_chain + M * d * P_track). -/
theorem uniform_multichain_discrete_sieve_bound (n k M d : ℕ) (P_macro P_chain P_track : ℝ)
    (hP : ∀ π : Perms k, (FinProb.uniform (Perms n)).Pr (missing n k π) ≤
      (M : ℝ)^2 * P_macro + (M : ℝ)^2 * (d : ℝ) * P_chain + (M : ℝ) * (d : ℝ) * P_track) :
    (FinProb.uniform (Perms n)).Pr (fun σ => ¬ IsSuperpattern k σ.1) ≤
      (Fintype.card (Perms k) : ℝ) *
        ((M : ℝ)^2 * P_macro + (M : ℝ)^2 * (d : ℝ) * P_chain + (M : ℝ) * (d : ℝ) * P_track) := by
  exact uniform_master_sieve_bound n k _ hP

end Superpatterns
