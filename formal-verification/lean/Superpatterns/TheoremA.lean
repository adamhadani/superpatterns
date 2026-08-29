import Superpatterns.Encoding
import Superpatterns.Tilt

/-!
# Theorem A: `pat(σ) ≤ x^{−(n+1)} (x/(1−x))^{k+1} (1 − x^k)^{(k−1)/2}`

Assembled from `patCount_le_sum_W` (Steps 1–2; proved modulo the two combinatorial sorries
`card_patterns_over_le` and `fiber_card_ge` in `Encoding.lean`), the gap bijection facts about
`k`-subsets (`compSum_gaps`, `gaps_mem_box`, `gaps_injOn`, proved), and `tilt_bound`
(Steps 3–4, proved).
-/

open Finset

namespace Superpatterns

/-- The gaps of a `k`-subset sum to `n + 1`. -/
theorem compSum_gaps {k m n : ℕ} (hk : k = 2 * m + 1) {T : Finset ℕ} (hT : T ∈ Subsets k n) :
    compSum (gaps n m T) = n + 1 := by
  unfold compSum gaps
  simp only
  -- telescoping: ∑_{j<m} (p_{2j+2} − p_{2j}) = p_{2m} − p_0
  have htel : ∀ M, M ≤ m →
      ∑ j : Fin M, ((posGet T (2 * j + 1) - posGet T (2 * j)) +
        (posGet T (2 * j + 2) - posGet T (2 * j + 1))) = posGet T (2 * M) - posGet T 0 := by
    intro M
    induction M with
    | zero => simp
    | succ M ih =>
      intro hM
      rw [Fin.sum_univ_castSucc]
      simp only [Fin.coe_castSucc, Fin.val_last]
      rw [ih (by omega)]
      have h1 := posGet_lt_posGet hT (i := 2 * M) (j := 2 * M + 1) (by omega) (by omega)
      have h2 := posGet_lt_posGet hT (i := 2 * M + 1) (j := 2 * M + 2) (by omega) (by omega)
      have h0 : posGet T 0 ≤ posGet T (2 * M) := by
        rcases Nat.eq_zero_or_pos M with h | h
        · subst h; simp
        · exact (posGet_lt_posGet hT (i := 0) (j := 2 * M) (by omega) (by omega)).le
      rw [show 2 * (M + 1) = 2 * M + 2 by ring]
      omega
  rw [htel m le_rfl]
  have h0 : posGet T 0 ≤ posGet T (2 * m) := by
    rcases Nat.eq_zero_or_pos m with h | h
    · subst h; simp
    · exact (posGet_lt_posGet hT (i := 0) (j := 2 * m) (by omega) (by omega)).le
  have hn := posGet_lt_n hT (i := 2 * m) (by omega)
  omega

/-- The gaps of a `k`-subset lie in the box `[1, n+1]^{k+1}`. -/
theorem gaps_mem_box {k m n : ℕ} (hk : k = 2 * m + 1) {T : Finset ℕ} (hT : T ∈ Subsets k n) :
    gaps n m T ∈ box m (n + 1) := by
  unfold box gaps
  simp only [mem_product, mem_Icc, Fintype.mem_piFinset]
  have hn := posGet_lt_n hT (i := 2 * m) (by omega)
  have h0 := posGet_lt_n hT (i := 0) (by omega)
  refine ⟨⟨by omega, by omega⟩, ⟨by omega, by omega⟩, ?_⟩
  intro j
  have h1 := posGet_lt_posGet hT (i := 2 * j) (j := 2 * j + 1) (by omega) (by omega)
  have h2 := posGet_lt_posGet hT (i := 2 * j + 1) (j := 2 * j + 2) (by omega) (by omega)
  have h3 := posGet_lt_n hT (i := 2 * j + 2) (by omega)
  exact ⟨⟨by omega, by omega⟩, ⟨by omega, by omega⟩⟩

/-- Two `k`-subsets with the same gaps are equal. -/
theorem gaps_injOn {k m n : ℕ} (hk : k = 2 * m + 1) :
    Set.InjOn (gaps n m) (Subsets k n : Set (Finset ℕ)) := by
  intro T hT T' hT' h
  have hT : T ∈ Subsets k n := hT
  have hT' : T' ∈ Subsets k n := hT'
  unfold gaps at h
  simp only [Prod.mk.injEq] at h
  obtain ⟨h0, -, hfun⟩ := h
  have hpair : ∀ j : Fin m,
      posGet T (2 * j + 1) - posGet T (2 * j) = posGet T' (2 * j + 1) - posGet T' (2 * j) ∧
      posGet T (2 * j + 2) - posGet T (2 * j + 1) =
        posGet T' (2 * j + 2) - posGet T' (2 * j + 1) := by
    intro j
    have := congrFun hfun j
    simpa only [Prod.mk.injEq] using this
  have hall : ∀ i, i ≤ 2 * m → posGet T i = posGet T' i := by
    intro i
    induction i with
    | zero => intro _; omega
    | succ i ih =>
      intro hi
      have hi' := ih (by omega)
      rcases Nat.even_or_odd i with ⟨j, hj⟩ | ⟨j, hj⟩
      · have hjm : j < m := by omega
        obtain ⟨h1, -⟩ := hpair ⟨j, hjm⟩
        simp only [Fin.val_mk] at h1
        have hlt := posGet_lt_posGet hT (i := 2 * j) (j := 2 * j + 1) (by omega) (by omega)
        have hlt' := posGet_lt_posGet hT' (i := 2 * j) (j := 2 * j + 1) (by omega) (by omega)
        rw [show i + 1 = 2 * j + 1 by omega]
        rw [show i = 2 * j by omega] at hi'
        omega
      · have hjm : j < m := by omega
        obtain ⟨-, h2⟩ := hpair ⟨j, hjm⟩
        simp only [Fin.val_mk] at h2
        have hlt := posGet_lt_posGet hT (i := 2 * j + 1) (j := 2 * j + 2) (by omega) (by omega)
        have hlt' := posGet_lt_posGet hT' (i := 2 * j + 1) (j := 2 * j + 2) (by omega) (by omega)
        rw [show i + 1 = 2 * j + 2 by omega]
        rw [show i = 2 * j + 1 by omega] at hi'
        omega
  have hlen := length_pos_of_mem hT
  have hlen' := length_pos_of_mem hT'
  have hpos : pos T = pos T' := by
    apply List.ext_getElem (by omega)
    intro i h1 h2
    rw [← posGet_eq_getElem h1, ← posGet_eq_getElem h2]
    exact hall i (by omega)
  have e1 : (pos T).toFinset = T := by unfold pos; exact Finset.sort_toFinset T _
  have e2 : (pos T').toFinset = T' := by unfold pos; exact Finset.sort_toFinset T' _
  rw [← e1, ← e2, hpos]

/-- **Theorem A.** For every `σ`, odd `k = 2m+1` and `x ∈ (0,1)`,
`pat(σ) ≤ x^{−(n+1)} (x/(1−x))^{k+1} (1 − x^k)^m`, where `n = |σ|`. -/
theorem theoremA (σ : List ℕ) (hσ : σ.Nodup) (k m : ℕ) (hk : k = 2 * m + 1) {x : ℝ}
    (hx0 : 0 < x) (hx1 : x < 1) :
    (patCount k σ : ℝ) ≤
      (x ^ (σ.length + 1))⁻¹ * (x / (1 - x)) ^ (k + 1) * (1 - x ^ k) ^ m := by
  set n := σ.length with hn
  have hxn : x ^ (n + 1) ≠ 0 := pow_ne_zero _ hx0.ne'
  have hinv : 0 ≤ (x ^ (n + 1))⁻¹ := inv_nonneg.2 (pow_nonneg hx0.le _)
  calc (patCount k σ : ℝ)
      ≤ ∑ T ∈ Subsets k n, W k m n T := patCount_le_sum_W σ hσ k m hk
    _ = (x ^ (n + 1))⁻¹ *
          ∑ T ∈ Subsets k n, x ^ compSum (gaps n m T) * Wcomp k (gaps n m T) := by
        rw [mul_sum]
        apply sum_congr rfl
        intro T hT
        rw [compSum_gaps hk hT]
        unfold W
        field_simp
    _ = (x ^ (n + 1))⁻¹ *
          ∑ a ∈ (Subsets k n).image (gaps n m), x ^ compSum a * Wcomp k a := by
        rw [sum_image (gaps_injOn hk)]
    _ ≤ (x ^ (n + 1))⁻¹ * ∑ a ∈ box m (n + 1), x ^ compSum a * Wcomp k a := by
        apply mul_le_mul_of_nonneg_left _ hinv
        apply sum_le_sum_of_subset_of_nonneg
        · intro a ha
          obtain ⟨T, hT, rfl⟩ := mem_image.1 ha
          exact gaps_mem_box hk hT
        · intro a _ _
          exact mul_nonneg (pow_nonneg hx0.le _) (Wcomp_nonneg k a)
    _ ≤ (x ^ (n + 1))⁻¹ * ((x / (1 - x)) ^ (2 * m + 2) * (1 - x ^ k) ^ m) :=
        mul_le_mul_of_nonneg_left (tilt_bound k m (n + 1) hx0.le hx1) hinv
    _ = (x ^ (n + 1))⁻¹ * (x / (1 - x)) ^ (k + 1) * (1 - x ^ k) ^ m := by
        subst hk
        ring

end Superpatterns
