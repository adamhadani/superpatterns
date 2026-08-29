import Mathlib

/-!
# Steps 3–4 of Theorem A: the Chernoff tilt and the closed form `E_x f(a+a') = 1 − x^k`

Everything here is finite: sums range over boxes `[1,N]^{k+1}` (which is all Theorem A needs,
since the compositions of `n+1` into `k+1` positive parts lie in `[1,n+1]^{k+1}`), so no `tsum`
is used.

* `wt k s = f(s) = min(1, k/(s−1))` written as `if s ≤ k+1 then 1 else k/(s−1)`.
* `pair_sum_le` (Step 4, truncated):
  `∑_{a,a'∈[1,N]} x^{a+a'} f(a+a') ≤ (x/(1−x))² (1 − x^k)`.
* `tilt_bound` (Step 3): the sum over the box of `x^{Σa} W(a)` factorises and is bounded by
  `(x/(1−x))^{2m+2} (1 − x^k)^m`, where `k = 2m+1`.
-/

open Finset

namespace Superpatterns

/-- `f(s) = min(1, k/(s−1))`. -/
noncomputable def wt (k s : ℕ) : ℝ := if s ≤ k + 1 then 1 else (k : ℝ) / ((s : ℝ) - 1)

theorem wt_nonneg (k s : ℕ) : 0 ≤ wt k s := by
  unfold wt
  split_ifs with h
  · exact zero_le_one
  · apply div_nonneg (Nat.cast_nonneg k)
    have : (k : ℝ) + 2 ≤ s := by exact_mod_cast (by omega : k + 2 ≤ s)
    linarith

/-- `(s−1)·f(s) ≤ min(s−1, k)` for `s ≥ 1`. -/
theorem wt_mul_le (k : ℕ) {s : ℕ} (hs : 1 ≤ s) :
    ((s : ℝ) - 1) * wt k s ≤ ((min (s - 1) k : ℕ) : ℝ) := by
  unfold wt
  split_ifs with h
  · have : min (s - 1) k = s - 1 := by omega
    rw [this, Nat.cast_sub hs]
    simp
  · have : min (s - 1) k = k := by omega
    rw [this]
    have hs1 : ((s : ℝ) - 1) ≠ 0 := by
      have : (k : ℝ) + 2 ≤ s := by exact_mod_cast (by omega : k + 2 ≤ s)
      linarith
    rw [mul_div_cancel₀ _ hs1]

/-- The fibre `{(a,a') ∈ [1,N]² : a + a' = s}` has at most `s − 1` elements. -/
theorem card_fiber_le (N s : ℕ) :
    ((Icc 1 N ×ˢ Icc 1 N).filter (fun p : ℕ × ℕ => p.1 + p.2 = s)).card ≤ s - 1 := by
  have := Finset.card_le_card_of_injOn (s := (Icc 1 N ×ˢ Icc 1 N).filter
      (fun p : ℕ × ℕ => p.1 + p.2 = s)) (t := Icc 1 (s - 1)) (fun p => p.1) ?_ ?_
  · simpa using this
  · intro p hp
    simp only [coe_filter, mem_product, mem_Icc, Set.mem_ofPred_eq] at hp
    simp only [coe_Icc, Set.mem_Icc]
    omega
  · intro p hp q hq hpq
    simp only [coe_filter, mem_product, mem_Icc, Set.mem_ofPred_eq] at hp hq
    simp only at hpq
    exact Prod.ext hpq (by omega)

/-- `min(s−1, k) = #{1 ≤ i ≤ k : i + 1 ≤ s}`. -/
theorem min_eq_sum_indicator (s k : ℕ) :
    ((min (s - 1) k : ℕ) : ℝ) = ∑ i ∈ Ico 1 (k + 1), if i + 1 ≤ s then (1 : ℝ) else 0 := by
  rw [sum_boole]
  norm_cast
  have : (Ico 1 (k + 1)).filter (fun i => i + 1 ≤ s) = Ico 1 (min (s - 1) k + 1) := by
    ext i
    simp only [mem_filter, mem_Ico]
    omega
  rw [this, Nat.card_Ico]
  omega

/-- **Step 4 (finite version).**
`∑_{a,a' ∈ [1,N]} x^{a+a'} f(a+a') ≤ (x/(1−x))² (1 − x^k)`. -/
theorem pair_sum_le (k N : ℕ) {x : ℝ} (hx0 : 0 ≤ x) (hx1 : x < 1) :
    ∑ p ∈ Icc 1 N ×ˢ Icc 1 N, x ^ (p.1 + p.2) * wt k (p.1 + p.2) ≤
      (x / (1 - x)) ^ 2 * (1 - x ^ k) := by
  set S := Icc 1 N ×ˢ Icc 1 N with hS
  have hmaps : ∀ p ∈ S, p.1 + p.2 ∈ Icc 2 (2 * N) := by
    intro p hp
    simp only [hS, mem_product, mem_Icc] at hp ⊢
    omega
  rw [← sum_fiberwise_of_maps_to hmaps]
  have hx1' : x ≠ 1 := hx1.ne
  have h1x : (1 - x) ≠ 0 := sub_ne_zero.2 hx1'.symm
  have hx1'' : (x - 1) ≠ 0 := sub_ne_zero.2 hx1'
  calc ∑ s ∈ Icc 2 (2 * N), ∑ p ∈ S with p.1 + p.2 = s, x ^ (p.1 + p.2) * wt k (p.1 + p.2)
      = ∑ s ∈ Icc 2 (2 * N), ∑ p ∈ S with p.1 + p.2 = s, x ^ s * wt k s := by
        apply sum_congr rfl
        intro s _
        apply sum_congr rfl
        intro p hp
        simp only [mem_filter] at hp
        rw [hp.2]
    _ = ∑ s ∈ Icc 2 (2 * N),
          ((S.filter (fun p : ℕ × ℕ => p.1 + p.2 = s)).card : ℝ) * (x ^ s * wt k s) := by
        apply sum_congr rfl
        intro s _
        rw [sum_const, nsmul_eq_mul]
    _ ≤ ∑ s ∈ Icc 2 (2 * N), ((s : ℝ) - 1) * (x ^ s * wt k s) := by
        apply sum_le_sum
        intro s hs
        have hs2 : 2 ≤ s := (mem_Icc.1 hs).1
        apply mul_le_mul_of_nonneg_right _ (mul_nonneg (pow_nonneg hx0 s) (wt_nonneg k s))
        calc (((S.filter (fun p : ℕ × ℕ => p.1 + p.2 = s)).card : ℕ) : ℝ)
            ≤ ((s - 1 : ℕ) : ℝ) := by exact_mod_cast card_fiber_le N s
          _ = (s : ℝ) - 1 := by rw [Nat.cast_sub (by omega)]; simp
    _ ≤ ∑ s ∈ Icc 2 (2 * N), ((min (s - 1) k : ℕ) : ℝ) * x ^ s := by
        apply sum_le_sum
        intro s hs
        have hs2 : 2 ≤ s := (mem_Icc.1 hs).1
        have := wt_mul_le k (s := s) (by omega)
        calc ((s : ℝ) - 1) * (x ^ s * wt k s) = (((s : ℝ) - 1) * wt k s) * x ^ s := by ring
          _ ≤ _ := mul_le_mul_of_nonneg_right this (pow_nonneg hx0 s)
    _ = ∑ s ∈ Icc 2 (2 * N), ∑ i ∈ Ico 1 (k + 1), (if i + 1 ≤ s then x ^ s else 0) := by
        apply sum_congr rfl
        intro s _
        rw [min_eq_sum_indicator s k, sum_mul]
        apply sum_congr rfl
        intro i _
        split_ifs <;> simp
    _ = ∑ i ∈ Ico 1 (k + 1), ∑ s ∈ Icc 2 (2 * N), (if i + 1 ≤ s then x ^ s else 0) := sum_comm
    _ ≤ ∑ i ∈ Ico 1 (k + 1), x ^ (i + 1) / (1 - x) := by
        apply sum_le_sum
        intro i _
        rw [← sum_filter]
        calc ∑ s ∈ (Icc 2 (2 * N)).filter (fun s => i + 1 ≤ s), x ^ s
            ≤ ∑ s ∈ Ico (i + 1) (2 * N + 1), x ^ s := by
              apply sum_le_sum_of_subset_of_nonneg
              · intro s hs
                simp only [mem_filter, mem_Icc, mem_Ico] at hs ⊢
                omega
              · intro s _ _
                exact pow_nonneg hx0 s
          _ ≤ x ^ (i + 1) / (1 - x) := geom_sum_Ico_le_of_lt_one hx0 hx1
    _ = (x / (1 - x)) ^ 2 * (1 - x ^ k) := by
        rw [sum_Ico_eq_sum_range]
        simp only [Nat.add_sub_cancel]
        rw [← sum_div, div_pow]
        have : ∑ j ∈ range k, x ^ (1 + j + 1) = x ^ 2 * ∑ j ∈ range k, x ^ j := by
          rw [mul_sum]
          apply sum_congr rfl
          intro j _
          ring
        rw [this, geom_sum_eq hx1']
        field_simp
        ring

/-- `∑_{a ∈ [1,N]} x^a ≤ x/(1−x)`. -/
theorem single_sum_le (N : ℕ) {x : ℝ} (hx0 : 0 ≤ x) (hx1 : x < 1) :
    ∑ a ∈ Icc 1 N, x ^ a ≤ x / (1 - x) := by
  calc ∑ a ∈ Icc 1 N, x ^ a ≤ ∑ a ∈ Ico 1 (N + 1), x ^ a := by
        apply sum_le_sum_of_subset_of_nonneg
        · intro a ha
          simp only [mem_Icc, mem_Ico] at ha ⊢
          omega
        · intro a _ _
          exact pow_nonneg hx0 a
    _ ≤ x ^ 1 / (1 - x) := geom_sum_Ico_le_of_lt_one hx0 hx1
    _ = x / (1 - x) := by rw [pow_one]

/-! ### Compositions and the weight `W` -/

/-- A "composition" in block form: `(a_0, a_k, ((a_1,a_2), (a_3,a_4), …, (a_{k-2},a_{k-1})))`
with `k = 2m+1`. -/
abbrev Comp (m : ℕ) := ℕ × ℕ × (Fin m → ℕ × ℕ)

/-- Sum of all parts. -/
def compSum {m : ℕ} (a : Comp m) : ℕ := a.1 + a.2.1 + ∑ j, ((a.2.2 j).1 + (a.2.2 j).2)

/-- `W(a) = ∏_j f(a_{2j−1} + a_{2j})`. -/
noncomputable def Wcomp (k : ℕ) {m : ℕ} (a : Comp m) : ℝ :=
  ∏ j : Fin m, wt k ((a.2.2 j).1 + (a.2.2 j).2)

theorem Wcomp_nonneg (k : ℕ) {m : ℕ} (a : Comp m) : 0 ≤ Wcomp k a :=
  prod_nonneg (fun j _ => wt_nonneg k _)

/-- The box `[1,N]^{k+1}` in block form. -/
def box (m N : ℕ) : Finset (Comp m) :=
  Icc 1 N ×ˢ (Icc 1 N ×ˢ Fintype.piFinset (fun _ : Fin m => Icc 1 N ×ˢ Icc 1 N))

/-- **Step 3.** The tilted sum over the box factorises and is bounded by
`(x/(1−x))^{2m+2} (1 − x^k)^m`. -/
theorem tilt_bound (k m N : ℕ) {x : ℝ} (hx0 : 0 ≤ x) (hx1 : x < 1) :
    ∑ a ∈ box m N, x ^ compSum a * Wcomp k a ≤
      (x / (1 - x)) ^ (2 * m + 2) * (1 - x ^ k) ^ m := by
  have hfac : ∑ a ∈ box m N, x ^ compSum a * Wcomp k a =
      (∑ a ∈ Icc 1 N, x ^ a) * (∑ a ∈ Icc 1 N, x ^ a) *
        ∏ _j : Fin m, ∑ p ∈ Icc 1 N ×ˢ Icc 1 N, x ^ (p.1 + p.2) * wt k (p.1 + p.2) := by
    rw [prod_univ_sum]
    unfold box
    simp only [sum_product]
    conv_rhs => rw [sum_mul_sum, sum_mul]
    apply sum_congr rfl
    intro a0 _
    rw [sum_mul]
    apply sum_congr rfl
    intro ak _
    rw [mul_sum]
    apply sum_congr rfl
    intro p _
    unfold compSum Wcomp
    simp only
    rw [pow_add, pow_add, ← prod_pow_eq_pow_sum, prod_mul_distrib]
    ring
  rw [hfac]
  have hq : 0 ≤ x / (1 - x) := div_nonneg hx0 (by linarith)
  have hxk : 0 ≤ 1 - x ^ k := by
    have := pow_le_one₀ hx0 hx1.le (n := k)
    linarith
  have h1 := single_sum_le N hx0 hx1
  have h1nn : 0 ≤ ∑ a ∈ Icc 1 N, x ^ a := sum_nonneg (fun a _ => pow_nonneg hx0 a)
  have hpair : ∏ _j : Fin m, ∑ p ∈ Icc 1 N ×ˢ Icc 1 N, x ^ (p.1 + p.2) * wt k (p.1 + p.2) ≤
      ((x / (1 - x)) ^ 2 * (1 - x ^ k)) ^ m := by
    rw [← Fin.prod_const m]
    apply prod_le_prod
    · intro j _
      exact sum_nonneg (fun p _ => mul_nonneg (pow_nonneg hx0 _) (wt_nonneg k _))
    · intro j _
      exact pair_sum_le k N hx0 hx1
  have hpnn : 0 ≤ ∏ _j : Fin m, ∑ p ∈ Icc 1 N ×ˢ Icc 1 N, x ^ (p.1 + p.2) * wt k (p.1 + p.2) :=
    prod_nonneg (fun j _ => sum_nonneg (fun p _ => mul_nonneg (pow_nonneg hx0 _) (wt_nonneg k _)))
  calc (∑ a ∈ Icc 1 N, x ^ a) * (∑ a ∈ Icc 1 N, x ^ a) *
        ∏ _j : Fin m, ∑ p ∈ Icc 1 N ×ˢ Icc 1 N, x ^ (p.1 + p.2) * wt k (p.1 + p.2)
      ≤ (x / (1 - x)) * (x / (1 - x)) * ((x / (1 - x)) ^ 2 * (1 - x ^ k)) ^ m := by
        apply mul_le_mul (mul_le_mul h1 h1 h1nn hq) hpair hpnn (mul_nonneg hq hq)
    _ = (x / (1 - x)) ^ (2 * m + 2) * (1 - x ^ k) ^ m := by
        rw [pow_add, pow_mul, mul_pow]
        ring

end Superpatterns
