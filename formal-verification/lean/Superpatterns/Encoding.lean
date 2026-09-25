import Superpatterns.Patterns
import Superpatterns.Tilt

/-!
# Step 1 of Theorem A: stable encodings and double counting (Lemma 1)

## Abstract part (fully proved)

* `sum_image_eq_sum_div_card`: for `ψ : W → Ψ` and any `g`,
  `∑_{q ∈ ψ(S)} g q = ∑_{T ∈ S} g (ψ T) / |ψ⁻¹(ψ T) ∩ S|`  (fibre averaging).
* `card_fiber_le_of_injective`: if `φ : P → Ψ × C` is injective with first component `ψ ∘ occ`,
  the number of `p` with `ψ (occ p) = q` is at most the number of admissible second components.
* `card_le_sum_fiber` (**abstract Lemma 1**): if every `p ∈ P` has a witness `occ p ∈ S` and the
  number of `p` over a given `q = ψ (occ p)` is at most `m q`, then
  `|P| ≤ ∑_{T ∈ S} m (ψ T) / |{T' ∈ S : ψ T' = ψ T}|`.

  Lemma 1 of `proof.md` is this with `P` = patterns of `σ`, `S` = `k`-subsets, `ψ T = (I(T), (t_j)_{j ∉ I(T)})`,
  `m = k!/(k−|I|)!` (from the injection `φ(π) = (ψ, (π(i))_{i ∈ I})`), and
  `|fibre| = ∏_{i ∈ I} (b_i − 1)` (from stability and non-adjacency).

## Concrete part

`patCount`, `gaps`, `W`, `offData` (= ψ), `lemma1_concrete` (proved from the abstract lemma and the two
combinatorial facts `card_patterns_over_le` (CKS injectivity) and `fiber_card_ge`
(extension counting), both proved below), and Step 2 (`evenRule`, `patCount_le_sum_W`, proved).
-/

open Finset

namespace Superpatterns

/-! ### Abstract double counting -/

/-- Fibre averaging: `∑_{q ∈ ψ(S)} g q = ∑_{T ∈ S} g (ψ T) / |fibre of ψ T|`. -/
theorem sum_image_eq_sum_div_card {W Ψ : Type*} [DecidableEq Ψ] (S : Finset W) (ψ : W → Ψ)
    (g : Ψ → ℝ) :
    ∑ q ∈ S.image ψ, g q =
      ∑ T ∈ S, g (ψ T) / ((S.filter (fun T' => ψ T' = ψ T)).card : ℝ) := by
  rw [← sum_fiberwise_of_maps_to (t := S.image ψ) (g := ψ) (fun T hT => mem_image_of_mem ψ hT)]
  apply sum_congr rfl
  intro q hq
  have hcongr : ∀ T ∈ S.filter (fun T => ψ T = q),
      g (ψ T) / ((S.filter (fun T' => ψ T' = ψ T)).card : ℝ) =
        g q / ((S.filter (fun T' => ψ T' = q)).card : ℝ) := by
    intro T hT
    rw [(mem_filter.1 hT).2]
  rw [sum_congr rfl hcongr, sum_const, nsmul_eq_mul]
  have hne : ((S.filter (fun T' => ψ T' = q)).card : ℝ) ≠ 0 := by
    rw [Nat.cast_ne_zero, ← pos_iff_ne_zero, card_pos]
    obtain ⟨T, hT, rfl⟩ := mem_image.1 hq
    exact ⟨T, mem_filter.2 ⟨hT, rfl⟩⟩
  field_simp

/-- The injection into triples: if `φ : P → Ψ × C` is injective and `(φ p).1 = ψ (occ p)`, then
the number of `p` lying over `q` is at most the number of admissible second components. -/
theorem card_fiber_le_of_injective {P W Ψ C : Type*} [Fintype P] [DecidableEq Ψ] [DecidableEq C]
    (ψ : W → Ψ) (occ : P → W) (φ : P → Ψ × C) (hφ : Function.Injective φ)
    (hφ1 : ∀ p, (φ p).1 = ψ (occ p)) (q : Ψ) (Cq : Finset C)
    (hC : ∀ p, ψ (occ p) = q → (φ p).2 ∈ Cq) :
    (univ.filter (fun p => ψ (occ p) = q)).card ≤ Cq.card := by
  apply card_le_card_of_injOn (fun p => (φ p).2)
  · intro p hp
    simp only [coe_filter, mem_univ, true_and, Set.mem_ofPred_eq] at hp
    exact mem_coe.2 (hC p hp)
  · intro p hp p' hp' h
    simp only [coe_filter, mem_univ, true_and, Set.mem_ofPred_eq] at hp hp'
    apply hφ
    exact Prod.ext (by rw [hφ1, hφ1, hp, hp']) h

/-- **Abstract Lemma 1.** -/
theorem card_le_sum_fiber {P W Ψ : Type*} [Fintype P] [DecidableEq Ψ]
    (S : Finset W) (ψ : W → Ψ) (occ : P → W) (hocc : ∀ p, occ p ∈ S)
    (m : Ψ → ℝ)
    (hm : ∀ q ∈ S.image ψ, ((univ.filter (fun p => ψ (occ p) = q)).card : ℝ) ≤ m q) :
    (Fintype.card P : ℝ) ≤
      ∑ T ∈ S, m (ψ T) / ((S.filter (fun T' => ψ T' = ψ T)).card : ℝ) := by
  rw [← sum_image_eq_sum_div_card]
  have h1 : Fintype.card P =
      ∑ q ∈ S.image ψ, (univ.filter (fun p => ψ (occ p) = q)).card := by
    rw [← card_univ]
    exact card_eq_sum_card_fiberwise (f := fun p => ψ (occ p))
      (fun p _ => mem_coe.2 (mem_image_of_mem ψ (hocc p)))
  rw [h1]
  push_cast
  exact sum_le_sum hm

/-! ### Concrete setting: `k`-subsets of positions of `σ` -/

/-- The `k`-subsets of positions `{0,…,n−1}`. -/
def Subsets (k n : ℕ) : Finset (Finset ℕ) := (range n).powersetCard k

/-- The positions of `T` in increasing order, `t_1 < … < t_k` (0-indexed here: `pos T = [p_0,…,p_{k-1}]`
with `t_{i+1} = p_i + 1`). -/
def pos (T : Finset ℕ) : List ℕ := T.sort (· ≤ ·)

/-- `i`-th position (0-indexed). -/
def posGet (T : Finset ℕ) (i : ℕ) : ℕ := (pos T).getD i 0

/-- The values of `σ` along `T`. -/
def valsAt (σ : List ℕ) (T : Finset ℕ) : List ℕ := (pos T).map (fun i => σ.getD i 0)

/-- The pattern (rank vector) of `σ` on `T`. -/
def patOf (σ : List ℕ) (T : Finset ℕ) : List ℕ := ranks (valsAt σ T)

/-- `pat(σ)`: the number of distinct `k`-patterns contained in `σ`. -/
def patCount (k : ℕ) (σ : List ℕ) : ℕ := ((Subsets k σ.length).image (patOf σ)).card

/-! ### Facts about sorted positions of a `k`-subset -/

theorem length_pos_of_mem {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) : (pos T).length = k := by
  unfold pos
  rw [Finset.length_sort]
  exact (Finset.mem_powersetCard.1 hT).2

theorem pos_pairwise (T : Finset ℕ) : (pos T).Pairwise (· < ·) :=
  (Finset.sortedLT_sort T).pairwise

theorem posGet_lt_posGet {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) {i j : ℕ}
    (hij : i < j) (hj : j < k) : posGet T i < posGet T j := by
  have hl := length_pos_of_mem hT
  have hi' : i < (pos T).length := by omega
  have hj' : j < (pos T).length := by omega
  unfold posGet
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi',
    List.getElem?_eq_getElem hj']
  simp only [Option.getD_some]
  exact List.Pairwise.rel_get_of_lt (pos_pairwise T) (a := ⟨i, hi'⟩) (b := ⟨j, hj'⟩) hij

theorem posGet_lt_n {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) {i : ℕ} (hi : i < k) :
    posGet T i < n := by
  have hl := length_pos_of_mem hT
  have hi' : i < (pos T).length := by omega
  have hmem : (pos T)[i] ∈ T := by
    have := List.getElem_mem hi'
    unfold pos at this ⊢
    exact (Finset.mem_sort _).1 this
  have hsub := (Finset.mem_powersetCard.1 hT).1 hmem
  rw [Finset.mem_range] at hsub
  unfold posGet
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi']
  simpa using hsub

theorem posGet_eq_getElem {T : Finset ℕ} {i : ℕ} (hi : i < (pos T).length) :
    posGet T i = (pos T)[i] := by
  unfold posGet
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi]
  rfl

/-- Width `b_i(T) = t_{i+1} − t_{i−1}` (1-indexed `i`), i.e. `p_i − p_{i−2}` 0-indexed. -/
def width (T : Finset ℕ) (i : ℕ) : ℕ := posGet T i - posGet T (i - 2)

/-- The gap composition `(a_0, a_k, ((a_1,a_2),…,(a_{k−2},a_{k−1})))` of `T`, `k = 2m+1`:
`a_0 = t_1`, `a_j = t_{j+1} − t_j`, `a_k = n + 1 − t_k`. -/
def gaps (n m : ℕ) (T : Finset ℕ) : Comp m :=
  (posGet T 0 + 1, n - posGet T (2 * m),
    fun j : Fin m => (posGet T (2 * j + 1) - posGet T (2 * j), posGet T (2 * j + 2) - posGet T (2 * j + 1)))

/-- The Step-2 weight `W(T) = ∏_{i even} f(b_i(T))`; note `b_{2j} = a_{2j−1} + a_{2j}`, so this is
`Wcomp k (gaps n m T)`. -/
noncomputable def W (k m n : ℕ) (T : Finset ℕ) : ℝ := Wcomp k (gaps n m T)

/-- The "off-`I` data" `ψ(T) = (I(T), (t_j)_{j ∉ I(T)})` (1-indexed `j ∈ [1,k]`). -/
def offData (k : ℕ) (I : Finset ℕ → Finset ℕ) (T : Finset ℕ) : Finset ℕ × List ℕ :=
  (I T, (((Icc 1 k).filter (fun j => j ∉ I T)).sort (· ≤ ·)).map (fun j => posGet T (j - 1)))

/-! ### CKS injectivity: helper lemmas -/
/-- The value of `σ` at the `j`-th position of `T` (0-indexed). -/
def vals (σ : List ℕ) (T : Finset ℕ) (j : ℕ) : ℕ := σ.getD (posGet T j) 0

theorem valsAt_eq {σ : List ℕ} {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) :
    valsAt σ T = (List.range k).map (vals σ T) := by
  have hl := length_pos_of_mem hT
  apply List.ext_getElem
  · simp [valsAt, hl]
  · intro j h1 h2
    simp only [valsAt, List.getElem_map, List.getElem_range, vals]
    rw [posGet_eq_getElem]

theorem length_patOf {σ : List ℕ} {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) :
    (patOf σ T).length = k := by
  simp [patOf, valsAt_eq hT]

theorem patOf_getD {σ : List ℕ} {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) {j : ℕ}
    (hj : j < k) : (patOf σ T).getD j 0 = rank (valsAt σ T) (vals σ T j) := by
  have hl : j < (valsAt σ T).length := by simp [valsAt_eq hT, hj]
  have hl2 : j < (patOf σ T).length := by rw [length_patOf hT]; exact hj
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hl2, Option.getD_some]
  show (ranks (valsAt σ T))[j] = _
  have key : ∀ (h : j < (ranks (valsAt σ T)).length),
      (ranks (valsAt σ T))[j] = rank (valsAt σ T) (vals σ T j) := by
    intro h
    rw [getElem_ranks (valsAt σ T) j hl]
    congr 1
    rw [List.getElem_of_eq (valsAt_eq hT)]
    simp
  exact key hl2

theorem rank_map_range (k : ℕ) (v : ℕ → ℕ) (x : ℕ) :
    rank ((List.range k).map v) x = ((range k).filter (fun j => v j < x)).card := by
  unfold rank
  rw [List.countP_map, List.countP_eq_length_filter, Finset.card_def, Finset.filter_val,
    Finset.range_val, Multiset.range, Multiset.filter_coe, Multiset.coe_card]
  rfl

theorem patOf_getD_eq_card {σ : List ℕ} {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) {j : ℕ}
    (hj : j < k) :
    (patOf σ T).getD j 0 = ((range k).filter (fun j' => vals σ T j' < vals σ T j)).card := by
  rw [patOf_getD hT hj, valsAt_eq hT, rank_map_range]

theorem patOf_getD_lt {σ : List ℕ} {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) {j : ℕ}
    (hj : j < k) : (patOf σ T).getD j 0 < k := by
  rw [patOf_getD_eq_card hT hj]
  have h : (range k).filter (fun j' => vals σ T j' < vals σ T j) ⊂ range k :=
    filter_ssubset.2 ⟨j, mem_range.2 hj, lt_irrefl _⟩
  have := card_lt_card h
  rwa [card_range] at this

theorem posGet_injOn {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) {i j : ℕ} (hi : i < k)
    (hj : j < k) (h : posGet T i = posGet T j) : i = j := by
  rcases lt_trichotomy i j with hij | hij | hij
  · have := posGet_lt_posGet hT hij hj; omega
  · exact hij
  · have := posGet_lt_posGet hT hij hi; omega

theorem vals_injOn {σ : List ℕ} (hσ : σ.Nodup) {k : ℕ} {T : Finset ℕ}
    (hT : T ∈ Subsets k σ.length) {i j : ℕ} (hi : i < k) (hj : j < k)
    (h : vals σ T i = vals σ T j) : i = j := by
  apply posGet_injOn hT hi hj
  have h1 := posGet_lt_n hT hi
  have h2 := posGet_lt_n hT hj
  unfold vals at h
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_eq_getElem h1,
    List.getElem?_eq_getElem h2, Option.getD_some, Option.getD_some] at h
  exact (hσ.getElem_inj_iff).1 h

theorem vals_lt_iff {σ : List ℕ} {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) {i j : ℕ}
    (hi : i < k) (hj : j < k) :
    vals σ T i < vals σ T j ↔ (patOf σ T).getD i 0 < (patOf σ T).getD j 0 := by
  rw [patOf_getD hT hi, patOf_getD hT hj]
  apply lt_iff_rank_lt
  rw [valsAt_eq hT, List.mem_map]
  exact ⟨i, List.mem_range.2 hi, rfl⟩

theorem patOf_injOn {σ : List ℕ} (hσ : σ.Nodup) {k : ℕ} {T : Finset ℕ}
    (hT : T ∈ Subsets k σ.length) {i j : ℕ} (hi : i < k) (hj : j < k)
    (h : (patOf σ T).getD i 0 = (patOf σ T).getD j 0) : i = j := by
  apply vals_injOn hσ hT hi hj
  have h1 := vals_lt_iff (σ := σ) hT hi hj
  have h2 := vals_lt_iff (σ := σ) hT hj hi
  omega

/-- Extracting the content of `offData` equality. -/
theorem offData_eq_iff {k : ℕ} {I : Finset ℕ → Finset ℕ} {T T' : Finset ℕ} :
    offData k I T' = offData k I T ↔
      I T' = I T ∧ ∀ j, 1 ≤ j → j ≤ k → j ∉ I T → posGet T' (j - 1) = posGet T (j - 1) := by
  unfold offData
  rw [Prod.mk.injEq]
  constructor
  · rintro ⟨h1, h2⟩
    refine ⟨h1, ?_⟩
    rw [h1, List.map_inj_left] at h2
    intro j hj1 hjk hjI
    exact h2 j ((Finset.mem_sort _).2 (mem_filter.2 ⟨mem_Icc.2 ⟨hj1, hjk⟩, hjI⟩))
  · rintro ⟨h1, h2⟩
    refine ⟨h1, ?_⟩
    rw [h1, List.map_inj_left]
    intro j hj
    have := mem_filter.1 ((Finset.mem_sort _).1 hj)
    rw [mem_Icc] at this
    exact h2 j this.1.1 this.1.2 this.2

/-- Combinatorial core: `x ↦ x − #{a ∈ A : a < x}` is injective off `A`. -/
theorem eq_of_card_filter_lt_aux (A : Finset ℕ) {x x' : ℕ} (hxx' : x < x') (hx : x ∉ A) :
    (A.filter (· < x')).card ≤ (A.filter (· < x)).card + (x' - x - 1) := by
  have hsub : A.filter (· < x') ⊆ A.filter (· < x) ∪ Ioo x x' := by
    intro a ha
    rw [mem_filter] at ha
    rw [mem_union, mem_filter, mem_Ioo]
    rcases lt_trichotomy a x with h | h | h
    · exact Or.inl ⟨ha.1, h⟩
    · subst h; exact absurd ha.1 hx
    · exact Or.inr ⟨h, ha.2⟩
  calc _ ≤ (A.filter (· < x) ∪ Ioo x x').card := card_le_card hsub
    _ ≤ (A.filter (· < x)).card + (Ioo x x').card := card_union_le _ _
    _ = _ := by rw [Nat.card_Ioo]

theorem eq_of_card_filter_lt (A : Finset ℕ) {x x' c : ℕ} (hx : x ∉ A) (hx' : x' ∉ A)
    (h : (A.filter (· < x)).card + c = x) (h' : (A.filter (· < x')).card + c = x') : x = x' := by
  rcases lt_trichotomy x x' with hlt | heq | hgt
  · have := eq_of_card_filter_lt_aux A hlt hx; omega
  · exact heq
  · have := eq_of_card_filter_lt_aux A hgt hx'; omega

/-- **CKS injectivity**: two occurrences with the same off-`I` data whose patterns agree on `I`
have the same pattern. -/
theorem patOf_eq_of_agree {σ : List ℕ} (hσ : σ.Nodup) {k : ℕ} {I : Finset ℕ → Finset ℕ}
    {T T' : Finset ℕ} (hT : T ∈ Subsets k σ.length) (hT' : T' ∈ Subsets k σ.length)
    (hoff : offData k I T' = offData k I T)
    (hagree : ∀ i ∈ I T, (patOf σ T').getD (i - 1) 0 = (patOf σ T).getD (i - 1) 0) :
    patOf σ T' = patOf σ T := by
  obtain ⟨hII, hpos⟩ := offData_eq_iff.1 hoff
  set v := vals σ T with hv
  set v' := vals σ T' with hv'
  set π := fun j => (patOf σ T).getD j 0 with hπ
  set π' := fun j => (patOf σ T').getD j 0 with hπ'
  have hvv : ∀ j, j < k → j + 1 ∉ I T → v' j = v j := by
    intro j hj hjI
    have := hpos (j + 1) (by omega) (by omega) hjI
    simp only [Nat.add_sub_cancel] at this
    simp only [hv, hv', vals, this]
  have hππ : ∀ j, j < k → j + 1 ∈ I T → π' j = π j := fun j _ hjI => by
    have := hagree (j + 1) hjI
    rw [Nat.add_sub_cancel] at this
    exact this
  -- the set of ranks occupied by `I`
  set A := ((range k).filter (fun j => j + 1 ∈ I T)).image π with hA
  have hA' : ((range k).filter (fun j => j + 1 ∈ I T)).image π' = A := by
    apply image_congr
    intro j hj
    rw [coe_filter] at hj
    exact hππ j (mem_range.1 hj.1) hj.2
  -- count formula
  have count : ∀ (T₀ : Finset ℕ) (hT₀ : T₀ ∈ Subsets k σ.length) (j : ℕ), j < k → j + 1 ∉ I T →
      ((((range k).filter (fun j' => j' + 1 ∈ I T)).image (fun j => (patOf σ T₀).getD j 0)).filter
          (· < (patOf σ T₀).getD j 0)).card +
        ((range k).filter (fun j' => j' + 1 ∉ I T ∧ vals σ T₀ j' < vals σ T₀ j)).card =
        (patOf σ T₀).getD j 0 := by
    intro T₀ hT₀ j hj hjI
    rw [filter_image, card_image_of_injOn, filter_filter]
    · have hsplit := card_filter_add_card_filter_not
        (s := (range k).filter (fun j' => vals σ T₀ j' < vals σ T₀ j)) (fun j' => j' + 1 ∈ I T)
      rw [filter_filter, filter_filter] at hsplit
      have e1 : (range k).filter (fun j' => j' + 1 ∈ I T ∧ (patOf σ T₀).getD j' 0 < (patOf σ T₀).getD j 0)
          = (range k).filter (fun j' => vals σ T₀ j' < vals σ T₀ j ∧ j' + 1 ∈ I T) := by
        apply filter_congr
        intro j' hj'
        rw [mem_range] at hj'
        rw [← vals_lt_iff hT₀ hj' hj]
        exact and_comm
      have e2 : (range k).filter (fun j' => j' + 1 ∉ I T ∧ vals σ T₀ j' < vals σ T₀ j)
          = (range k).filter (fun j' => vals σ T₀ j' < vals σ T₀ j ∧ j' + 1 ∉ I T) := by
        apply filter_congr
        intro j' hj'
        exact and_comm
      rw [e1, e2, hsplit, patOf_getD_eq_card hT₀ hj]
    · intro a ha b hb hab
      simp only [mem_coe, mem_filter, mem_range] at ha hb
      exact patOf_injOn hσ hT₀ ha.1.1 hb.1.1 hab
  have hlen := length_patOf (σ := σ) hT
  have hlen' := length_patOf (σ := σ) hT'
  apply List.ext_getElem (by rw [hlen, hlen'])
  intro j hj _
  rw [hlen'] at hj
  rw [← List.getD_eq_getElem, ← List.getD_eq_getElem]
  change π' j = π j
  by_cases hjI : j + 1 ∈ I T
  · exact hππ j hj hjI
  · have c1 := count T hT j hj hjI
    have c2 := count T' hT' j hj hjI
    rw [hA'] at c2
    have hc : ((range k).filter (fun j' => j' + 1 ∉ I T ∧ vals σ T' j' < vals σ T' j)).card =
        ((range k).filter (fun j' => j' + 1 ∉ I T ∧ vals σ T j' < vals σ T j)).card := by
      congr 1
      apply filter_congr
      intro j' hj'
      rw [mem_range] at hj'
      constructor
      · rintro ⟨h1, h2⟩
        refine ⟨h1, ?_⟩
        have e1 := hvv j' hj' h1
        have e2 := hvv j hj hjI
        simp only [hv, hv'] at e1 e2
        rw [← e1, ← e2]; exact h2
      · rintro ⟨h1, h2⟩
        refine ⟨h1, ?_⟩
        have e1 := hvv j' hj' h1
        have e2 := hvv j hj hjI
        simp only [hv, hv'] at e1 e2
        rw [e1, e2]; exact h2
    rw [hc] at c2
    have hnot : ∀ (T₀ : Finset ℕ), T₀ ∈ Subsets k σ.length →
        (patOf σ T₀).getD j 0 ∉ ((range k).filter (fun j' => j' + 1 ∈ I T)).image
          (fun j => (patOf σ T₀).getD j 0) := by
      intro T₀ hT₀ hmem
      obtain ⟨i, hi, hij⟩ := mem_image.1 hmem
      rw [mem_filter, mem_range] at hi
      have := patOf_injOn hσ hT₀ hi.1 hj hij
      subst this
      exact hjI hi.2
    have h1 := hnot T hT
    have h2 := hnot T' hT'
    rw [hA'] at h2
    exact (eq_of_card_filter_lt A h1 h2 c1 c2).symm


/-- The pattern values on `I` form an injective map `I → [k]`. -/
theorem exists_emb {σ : List ℕ} (hσ : σ.Nodup) {k : ℕ} {I₀ T : Finset ℕ}
    (hT : T ∈ Subsets k σ.length) (hI : I₀ ⊆ Icc 2 (k - 1)) :
    ∃ e : ↥I₀ ↪ Fin k, ∀ i : ↥I₀, (e i : ℕ) = (patOf σ T).getD (i.1 - 1) 0 := by
  have hlt : ∀ i : ↥I₀, i.1 - 1 < k := fun i => by
    have := mem_Icc.1 (hI i.2); omega
  refine ⟨⟨fun i => ⟨(patOf σ T).getD (i.1 - 1) 0, patOf_getD_lt hT (hlt i)⟩, ?_⟩, fun i => rfl⟩
  intro i i' h
  simp only [Fin.mk.injEq] at h
  have := patOf_injOn hσ hT (hlt i) (hlt i') h
  have h2 := mem_Icc.1 (hI i.2)
  have h2' := mem_Icc.1 (hI i'.2)
  exact Subtype.ext (by omega)

/-- **CKS injectivity (counting form).**  All `T` with the same off-`I` data `q` produce at most
`k!/(k−|I|)!` distinct patterns: the pattern is determined by `q` (which fixes the relative order
of the values at positions outside `I`, via `σ`) together with the `|I|` pattern values at the
positions in `I` (an injective map `I → [k]`).  Needs `σ.Nodup` so that the ranks of the values along
`T` form a permutation. -/
theorem card_patterns_over_le (σ : List ℕ) (hσ : σ.Nodup) (k : ℕ) (I : Finset ℕ → Finset ℕ)
    (hI : ∀ T, I T ⊆ Icc 2 (k - 1)) (q : Finset ℕ × List ℕ) :
    (((Subsets k σ.length).filter (fun T => offData k I T = q)).image (patOf σ)).card ≤
      k.descFactorial q.1.card := by
  classical
  obtain ⟨I₀, L⟩ := q
  set S := (Subsets k σ.length).filter (fun T => offData k I T = (I₀, L)) with hS
  have hex : ∀ π ∈ S.image (patOf σ), ∃ e : ↥I₀ ↪ Fin k, ∀ i : ↥I₀, (e i : ℕ) = π.getD (i.1 - 1) 0 := by
    intro π hπ
    obtain ⟨T, hT, rfl⟩ := mem_image.1 hπ
    rw [hS, mem_filter] at hT
    have hI0 : I₀ = I T := by
      have := congrArg Prod.fst hT.2
      exact this.symm
    subst hI0
    exact exists_emb hσ hT.1 (hI T)
  choose e he using hex
  rw [← Fintype.card_coe]
  calc Fintype.card ↥(S.image (patOf σ)) ≤ Fintype.card (↥I₀ ↪ Fin k) := by
        apply Fintype.card_le_of_injective (fun π => e π.1 π.2)
        intro π π' h
        apply Subtype.ext
        obtain ⟨T, hT, hπ⟩ := mem_image.1 π.2
        obtain ⟨T', hT', hπ'⟩ := mem_image.1 π'.2
        rw [hS, mem_filter] at hT hT'
        rw [← hπ, ← hπ']
        apply patOf_eq_of_agree hσ hT'.1 hT.1 (by rw [hT.2, hT'.2])
        intro i hi
        have hI0 : i ∈ I₀ := by
          have := congrArg Prod.fst hT'.2
          simp only at this
          rw [← this]; exact hi
        have e1 := he π π.2 ⟨i, hI0⟩
        have e2 := he π' π'.2 ⟨i, hI0⟩
        have h' : e π.1 π.2 = e π'.1 π'.2 := h
        rw [hπ, hπ', ← e1, ← e2, h']
    _ = k.descFactorial I₀.card := by
        rw [Fintype.card_embedding_eq, Fintype.card_fin, Fintype.card_coe]

/-! ### Extension counting: helper lemmas -/
theorem pos_toFinset {l : List ℕ} (hl : l.Pairwise (· < ·)) : pos l.toFinset = l := by
  unfold pos
  exact (List.toFinset_sort (· ≤ ·) (hl.imp ne_of_lt)).2 (hl.imp le_of_lt)

theorem posGet_toFinset {l : List ℕ} (hl : l.Pairwise (· < ·)) (j : ℕ) :
    posGet l.toFinset j = l.getD j 0 := by
  unfold posGet
  rw [pos_toFinset hl]

theorem toFinset_mem_Subsets {l : List ℕ} {k n : ℕ} (hl : l.Pairwise (· < ·)) (hk : l.length = k)
    (hn : ∀ x ∈ l, x < n) : l.toFinset ∈ Subsets k n := by
  unfold Subsets
  rw [mem_powersetCard]
  refine ⟨?_, ?_⟩
  · intro x hx
    rw [List.mem_toFinset] at hx
    exact mem_range.2 (hn x hx)
  · rw [List.toFinset_card_of_nodup (hl.imp ne_of_lt), hk]

theorem lt_of_step {f : ℕ → ℕ} {k : ℕ} (hstep : ∀ j, j + 1 < k → f j < f (j + 1)) :
    ∀ i j, j < k → i < j → f i < f j := by
  intro i j hj hij
  induction j with
  | zero => omega
  | succ j ih =>
    rcases Nat.lt_succ_iff_lt_or_eq.1 hij with h | h
    · exact (ih (by omega) h).trans (hstep j hj)
    · subst h; exact hstep i hj

/-- The new position function: replace `t_i`, `i ∈ I₀` (1-indexed), by `g i`. -/
def replPos (I₀ T : Finset ℕ) (g : ∀ i, i ∈ I₀ → ℕ) (j : ℕ) : ℕ :=
  if h : j + 1 ∈ I₀ then g (j + 1) h else posGet T j

/-- The modified `k`-set. -/
def replSet (k : ℕ) (I₀ T : Finset ℕ) (g : ∀ i, i ∈ I₀ → ℕ) : Finset ℕ :=
  ((List.range k).map (replPos I₀ T g)).toFinset

section repl
variable {k n : ℕ} {I₀ T : Finset ℕ} {g : ∀ i, i ∈ I₀ → ℕ}
  (hT : T ∈ Subsets k n) (hI₀ : I₀ ⊆ Icc 2 (k - 1)) (hnonadj : ∀ i ∈ I₀, i + 1 ∉ I₀)
  (hg : ∀ i (hi : i ∈ I₀), posGet T (i - 2) < g i hi ∧ g i hi < posGet T i)
include hT hI₀ hnonadj hg

omit hI₀ in
theorem replPos_step : ∀ j, j + 1 < k → replPos I₀ T g j < replPos I₀ T g (j + 1) := by
  intro j hj
  unfold replPos
  by_cases h1 : j + 1 ∈ I₀
  · have h2 : j + 1 + 1 ∉ I₀ := hnonadj _ h1
    rw [dif_pos h1, dif_neg h2]
    exact (hg _ h1).2
  · rw [dif_neg h1]
    by_cases h2 : j + 1 + 1 ∈ I₀
    · rw [dif_pos h2]
      have := (hg _ h2).1
      rwa [show j + 1 + 1 - 2 = j by omega] at this
    · rw [dif_neg h2]
      exact posGet_lt_posGet hT (Nat.lt_succ_self j) hj

omit hnonadj in
theorem replPos_lt_n : ∀ j, j < k → replPos I₀ T g j < n := by
  intro j hj
  unfold replPos
  by_cases h1 : j + 1 ∈ I₀
  · rw [dif_pos h1]
    have := mem_Icc.1 (hI₀ h1)
    exact (hg _ h1).2.trans (posGet_lt_n hT (by omega))
  · rw [dif_neg h1]
    exact posGet_lt_n hT hj

omit hI₀ in
theorem replList_pairwise : ((List.range k).map (replPos I₀ T g)).Pairwise (· < ·) := by
  rw [List.pairwise_iff_getElem]
  intro i j hi hj hij
  simp only [List.length_map, List.length_range] at hi hj
  simp only [List.getElem_map, List.getElem_range]
  exact lt_of_step (replPos_step hT hnonadj hg) i j hj hij

theorem replSet_mem : replSet k I₀ T g ∈ Subsets k n := by
  apply toFinset_mem_Subsets (replList_pairwise hT hnonadj hg)
  · simp
  · intro x hx
    rw [List.mem_map] at hx
    obtain ⟨j, hj, rfl⟩ := hx
    exact replPos_lt_n hT hI₀ hg j (List.mem_range.1 hj)


omit hI₀ in
theorem posGet_replSet {j : ℕ} (hj : j < k) : posGet (replSet k I₀ T g) j = replPos I₀ T g j := by
  unfold replSet
  rw [posGet_toFinset (replList_pairwise hT hnonadj hg)]
  simp [hj]


omit hI₀ in
theorem posGet_replSet_of_notMem {j : ℕ} (hj1 : 1 ≤ j) (hjk : j ≤ k) (hjI : j ∉ I₀) :
    posGet (replSet k I₀ T g) (j - 1) = posGet T (j - 1) := by
  rw [posGet_replSet hT hnonadj hg (by omega)]
  unfold replPos
  rw [dif_neg (by rw [show j - 1 + 1 = j by omega]; exact hjI)]


theorem posGet_replSet_of_mem {i : ℕ} (hi : i ∈ I₀) :
    posGet (replSet k I₀ T g) (i - 1) = g i hi := by
  have := mem_Icc.1 (hI₀ hi)
  rw [posGet_replSet hT hnonadj hg (by omega)]
  unfold replPos
  have h : i - 1 + 1 ∈ I₀ := by rw [show i - 1 + 1 = i by omega]; exact hi
  rw [dif_pos h]
  congr 1
  omega

end repl

/-- **Extension counting.**  For a non-adjacent stable rule, every choice of `t'_i ∈ (t_{i−1}, t_{i+1})`
for `i ∈ I(T)` (independently) gives a `T'` with the same off-`I` data, so the fibre of `ψ` through
`T` has at least `∏_{i ∈ I(T)} (b_i − 1)` elements. -/
theorem fiber_card_ge (n k : ℕ) (I : Finset ℕ → Finset ℕ)
    (hI : ∀ T, I T ⊆ Icc 2 (k - 1))
    (hnonadj : ∀ T, ∀ i ∈ I T, i + 1 ∉ I T)
    (hstable : ∀ T T', T ∈ Subsets k n → T' ∈ Subsets k n →
      (∀ j, 1 ≤ j → j ≤ k → j ∉ I T → posGet T' (j - 1) = posGet T (j - 1)) → I T' = I T)
    (T : Finset ℕ) (hT : T ∈ Subsets k n) :
    ∏ i ∈ I T, (width T i - 1) ≤
      ((Subsets k n).filter (fun T' => offData k I T' = offData k I T)).card := by
  classical
  set t : ℕ → Finset ℕ := fun i => Ioo (posGet T (i - 2)) (posGet T i) with ht
  have hcard : ∏ i ∈ I T, (width T i - 1) = ((I T).pi t).card := by
    rw [card_pi]
    apply prod_congr rfl
    intro i _
    simp only [ht, Nat.card_Ioo, width]
  rw [hcard]
  apply card_le_card_of_injOn (fun g => replSet k (I T) T g)
  · intro g hg
    rw [mem_coe, mem_pi] at hg
    have hg' : ∀ i (hi : i ∈ I T), posGet T (i - 2) < g i hi ∧ g i hi < posGet T i :=
      fun i hi => mem_Ioo.1 (hg i hi)
    have hmem := replSet_mem hT (hI T) (hnonadj T) hg'
    rw [mem_coe, mem_filter]
    refine ⟨hmem, ?_⟩
    have hoff : ∀ j, 1 ≤ j → j ≤ k → j ∉ I T →
        posGet (replSet k (I T) T g) (j - 1) = posGet T (j - 1) :=
      fun j hj1 hjk hjI => posGet_replSet_of_notMem hT (hnonadj T) hg' hj1 hjk hjI
    exact offData_eq_iff.2 ⟨hstable T _ hT hmem hoff, hoff⟩
  · intro g hg g' hg' heq
    rw [mem_coe, mem_pi] at hg hg'
    have hg1 : ∀ i (hi : i ∈ I T), posGet T (i - 2) < g i hi ∧ g i hi < posGet T i :=
      fun i hi => mem_Ioo.1 (hg i hi)
    have hg1' : ∀ i (hi : i ∈ I T), posGet T (i - 2) < g' i hi ∧ g' i hi < posGet T i :=
      fun i hi => mem_Ioo.1 (hg' i hi)
    funext i hi
    rw [← posGet_replSet_of_mem hT (hI T) (hnonadj T) hg1 hi,
      ← posGet_replSet_of_mem hT (hI T) (hnonadj T) hg1' hi]
    simp only at heq
    rw [heq]

theorem two_le_width {k n : ℕ} {T : Finset ℕ} (hT : T ∈ Subsets k n) {i : ℕ}
    (hi : i ∈ Icc 2 (k - 1)) : 2 ≤ width T i := by
  rw [mem_Icc] at hi
  have h1 := posGet_lt_posGet hT (i := i - 2) (j := i - 1) (by omega) (by omega)
  have h2 := posGet_lt_posGet hT (i := i - 1) (j := i) (by omega) (by omega)
  unfold width
  omega

/-- **Lemma 1 (concrete form).** For a non-adjacent, stable rule `I` and `σ` without repeated
values, `pat(σ) ≤ ∑_T k!/(k−|I(T)|)! ∏_{i ∈ I(T)} 1/(b_i(T) − 1)`.
(Indices `i` are 1-indexed as in `proof.md`, `2 ≤ i ≤ k−1`.)

Proof: `card_le_sum_fiber` with `P` = the patterns of `σ`, `occ π` = a chosen occurrence,
`ψ = offData k I`, `m q = k.descFactorial |q.1|` (`card_patterns_over_le`), and the fibre lower
bound `fiber_card_ge`. -/
theorem lemma1_concrete (σ : List ℕ) (hσ : σ.Nodup) (k : ℕ) (I : Finset ℕ → Finset ℕ)
    (hI : ∀ T, I T ⊆ Icc 2 (k - 1))
    (hnonadj : ∀ T, ∀ i ∈ I T, i + 1 ∉ I T)
    (hstable : ∀ T T', T ∈ Subsets k σ.length → T' ∈ Subsets k σ.length →
      (∀ j, 1 ≤ j → j ≤ k → j ∉ I T → posGet T' (j - 1) = posGet T (j - 1)) → I T' = I T) :
    (patCount k σ : ℝ) ≤ ∑ T ∈ Subsets k σ.length,
      ((k.factorial : ℝ) / ((k - (I T).card).factorial : ℝ)) *
        ∏ i ∈ I T, (1 : ℝ) / ((width T i : ℝ) - 1) := by
  classical
  set n := σ.length with hn
  set S := Subsets k n with hS
  set ψ := offData k I with hψ
  set P := S.image (patOf σ) with hP
  have hocc_ex : ∀ π : P, ∃ T, T ∈ S ∧ patOf σ T = π := fun π => mem_image.1 π.2
  choose occ hoccS hoccP using hocc_ex
  have hm : ∀ q ∈ S.image ψ,
      ((univ.filter (fun p : P => ψ (occ p) = q)).card : ℝ) ≤ (k.descFactorial q.1.card : ℝ) := by
    intro q _
    have h1 : (univ.filter (fun p : P => ψ (occ p) = q)).card ≤
        ((S.filter (fun T => ψ T = q)).image (patOf σ)).card := by
      apply card_le_card_of_injOn (fun p : P => (p : List ℕ))
      · intro p hp
        simp only [coe_filter, mem_univ, true_and, Set.mem_ofPred_eq] at hp
        exact mem_coe.2 (mem_image.2 ⟨occ p, mem_filter.2 ⟨hoccS p, hp⟩, hoccP p⟩)
      · intro p _ p' _ h
        exact Subtype.ext h
    exact_mod_cast h1.trans (card_patterns_over_le σ hσ k I hI q)
  have main := card_le_sum_fiber S ψ occ hoccS (fun q => (k.descFactorial q.1.card : ℝ)) hm
  rw [Fintype.card_coe] at main
  unfold patCount
  refine main.trans (sum_le_sum fun T hT => ?_)
  have hfib := fiber_card_ge n k I hI hnonadj hstable T hT
  rw [← hψ, ← hS] at hfib
  have hψ1 : (ψ T).1 = I T := rfl
  have hcardI : (I T).card ≤ k := by
    have := card_le_card (hI T)
    rw [Nat.card_Icc] at this
    omega
  have hdf : (k.descFactorial (I T).card : ℝ) =
      (k.factorial : ℝ) / ((k - (I T).card).factorial : ℝ) := by
    rw [eq_div_iff (by positivity)]
    have := Nat.factorial_mul_descFactorial hcardI
    exact_mod_cast (by rw [mul_comm]; exact this)
  rw [hψ1, hdf]
  have hB : (0 : ℝ) < ∏ i ∈ I T, ((width T i : ℝ) - 1) := by
    apply prod_pos
    intro i hi
    have := two_le_width hT (hI T hi)
    have : (2 : ℝ) ≤ width T i := by exact_mod_cast this
    linarith
  have hBcast : ((∏ i ∈ I T, (width T i - 1) : ℕ) : ℝ) = ∏ i ∈ I T, ((width T i : ℝ) - 1) := by
    push_cast
    apply prod_congr rfl
    intro i hi
    have := two_le_width hT (hI T hi)
    rw [Nat.cast_sub (by omega)]
    simp
  have hfib' : ∏ i ∈ I T, ((width T i : ℝ) - 1) ≤
      ((S.filter (fun T' => ψ T' = ψ T)).card : ℝ) := by
    rw [← hBcast]
    exact_mod_cast hfib
  have hprod : ∏ i ∈ I T, (1 : ℝ) / ((width T i : ℝ) - 1) =
      1 / ∏ i ∈ I T, ((width T i : ℝ) - 1) := by
    rw [prod_div_distrib, prod_const_one]
  rw [hprod, mul_one_div]
  exact div_le_div_of_nonneg_left (by positivity) hB hfib'

/-! ### Step 2: the even rule -/

/-- The even rule `I(T) = {i even : b_i − 1 > k}` (1-indexed `i ∈ [2, k−1]`). -/
def evenRule (k : ℕ) (T : Finset ℕ) : Finset ℕ :=
  (Icc 2 (k - 1)).filter (fun i => Even i ∧ k < width T i - 1)

theorem evenRule_subset (k : ℕ) (T : Finset ℕ) : evenRule k T ⊆ Icc 2 (k - 1) :=
  filter_subset _ _

theorem odd_notMem_evenRule (k : ℕ) (T : Finset ℕ) {j : ℕ} (hj : Odd j) : j ∉ evenRule k T := by
  intro h
  simp only [evenRule, mem_filter] at h
  obtain ⟨-, he, -⟩ := h
  rw [Nat.odd_iff] at hj
  rw [Nat.even_iff] at he
  omega

theorem evenRule_nonadj (k : ℕ) (T : Finset ℕ) : ∀ i ∈ evenRule k T, i + 1 ∉ evenRule k T := by
  intro i hi
  simp only [evenRule, mem_filter] at hi
  obtain ⟨-, he, -⟩ := hi
  apply odd_notMem_evenRule
  rw [Nat.even_iff] at he
  rw [Nat.odd_iff]
  omega

/-- Stability of the even rule: it only depends on the odd (1-indexed) positions, none of which is
in `I(T)`. -/
theorem evenRule_stable (k : ℕ) (T T' : Finset ℕ)
    (h : ∀ j, 1 ≤ j → j ≤ k → j ∉ evenRule k T → posGet T' (j - 1) = posGet T (j - 1)) :
    evenRule k T' = evenRule k T := by
  unfold evenRule
  apply filter_congr
  intro i hi
  rw [mem_Icc] at hi
  have key : Even i → width T' i = width T i := by
    intro he
    rw [Nat.even_iff] at he
    have h1 := h (i + 1) (by omega) (by omega)
      (odd_notMem_evenRule k T (by rw [Nat.odd_iff]; omega))
    have h2 := h (i - 1) (by omega) (by omega)
      (odd_notMem_evenRule k T (by rw [Nat.odd_iff]; omega))
    rw [show i + 1 - 1 = i by omega] at h1
    rw [show i - 1 - 1 = i - 2 by omega] at h2
    unfold width
    rw [h1, h2]
  constructor
  · rintro ⟨he, hw⟩
    exact ⟨he, by rw [← key he]; exact hw⟩
  · rintro ⟨he, hw⟩
    exact ⟨he, by rw [key he]; exact hw⟩

/-- Pointwise Step 2: `k!/(k−|I(T)|)! ∏_{i ∈ I(T)} 1/(b_i − 1) ≤ W(T)`. -/
theorem step2_pointwise (k m n : ℕ) (hk : k = 2 * m + 1) (T : Finset ℕ) (hT : T ∈ Subsets k n) :
    ((k.factorial : ℝ) / ((k - (evenRule k T).card).factorial : ℝ)) *
        ∏ i ∈ evenRule k T, (1 : ℝ) / ((width T i : ℝ) - 1) ≤ W k m n T := by
  have hcard : (evenRule k T).card ≤ k := by
    have := card_le_card (evenRule_subset k T)
    rw [Nat.card_Icc] at this
    omega
  set I := evenRule k T with hI
  have hfact : (k.factorial : ℝ) / ((k - I.card).factorial : ℝ) ≤ (k : ℝ) ^ I.card := by
    rw [div_le_iff₀ (by positivity)]
    have h1 := Nat.factorial_mul_descFactorial hcard
    have h2 := Nat.descFactorial_le_pow k I.card
    calc (k.factorial : ℝ) = (k.descFactorial I.card : ℝ) * ((k - I.card).factorial : ℝ) := by
          rw [← h1]; push_cast; ring
      _ ≤ (k : ℝ) ^ I.card * ((k - I.card).factorial : ℝ) := by
          gcongr
          exact_mod_cast h2
  have hwidth : ∀ i ∈ I, (k : ℝ) + 2 ≤ width T i := by
    intro i hi
    simp only [hI, evenRule, mem_filter] at hi
    obtain ⟨-, -, hw⟩ := hi
    exact_mod_cast (by omega : k + 2 ≤ width T i)
  have hprodI : (k : ℝ) ^ I.card * ∏ i ∈ I, (1 : ℝ) / ((width T i : ℝ) - 1) =
      ∏ i ∈ I, wt k (width T i) := by
    rw [← prod_const, ← prod_mul_distrib]
    apply prod_congr rfl
    intro i hi
    have hw := hwidth i hi
    have hw' : k + 2 ≤ width T i := by exact_mod_cast hw
    unfold wt
    rw [if_neg (by omega)]
    have : (width T i : ℝ) - 1 ≠ 0 := by linarith
    field_simp
  have hevens : ∏ i ∈ I, wt k (width T i) =
      ∏ i ∈ (Icc 2 (k - 1)).filter Even, wt k (width T i) := by
    have : I = ((Icc 2 (k - 1)).filter Even).filter (fun i => k < width T i - 1) := by
      simp only [hI, evenRule, filter_filter]
    rw [this]
    apply prod_filter_of_ne
    intro i _ hne
    by_contra hle
    apply hne
    unfold wt
    rw [if_pos (by omega)]
  have hW : ∏ i ∈ (Icc 2 (k - 1)).filter Even, wt k (width T i) = W k m n T := by
    unfold W Wcomp gaps
    simp only
    have himg : (Icc 2 (k - 1)).filter Even =
        (univ : Finset (Fin m)).image (fun j : Fin m => 2 * (j : ℕ) + 2) := by
      ext i
      simp only [mem_filter, mem_Icc, mem_image, mem_univ, true_and]
      constructor
      · rintro ⟨⟨h2, hk1⟩, he⟩
        rw [Nat.even_iff] at he
        refine ⟨⟨i / 2 - 1, by omega⟩, ?_⟩
        simp only
        omega
      · rintro ⟨j, hj⟩
        refine ⟨⟨by omega, by omega⟩, ?_⟩
        rw [Nat.even_iff]
        omega
    rw [himg, prod_image (fun j _ j' _ h => Fin.ext (by omega))]
    apply prod_congr rfl
    intro j _
    have h1 := posGet_lt_posGet hT (i := 2 * j) (j := 2 * j + 1) (by omega) (by omega)
    have h2 := posGet_lt_posGet hT (i := 2 * j + 1) (j := 2 * j + 2) (by omega) (by omega)
    unfold width
    congr 1
    rw [show 2 * (j : ℕ) + 2 - 2 = 2 * j by omega]
    omega
  calc ((k.factorial : ℝ) / ((k - I.card).factorial : ℝ)) *
          ∏ i ∈ I, (1 : ℝ) / ((width T i : ℝ) - 1)
      ≤ (k : ℝ) ^ I.card * ∏ i ∈ I, (1 : ℝ) / ((width T i : ℝ) - 1) := by
        apply mul_le_mul_of_nonneg_right hfact
        apply prod_nonneg
        intro i hi
        have := hwidth i hi
        apply div_nonneg zero_le_one
        linarith
    _ = ∏ i ∈ I, wt k (width T i) := hprodI
    _ = ∏ i ∈ (Icc 2 (k - 1)).filter Even, wt k (width T i) := hevens
    _ = W k m n T := hW

/-- **Step 2 (the even rule).** `pat(σ) ≤ ∑_T W(T)`, `W(T) = ∏_{i even} f(b_i)`,
`f(b) = min(1, k/(b−1))`.  Derived from `lemma1_concrete` with the even rule
(non-adjacent, stable) and `k!/(k−|I|)! ≤ k^{|I|}`. -/
theorem patCount_le_sum_W (σ : List ℕ) (hσ : σ.Nodup) (k m : ℕ) (hk : k = 2 * m + 1) :
    (patCount k σ : ℝ) ≤ ∑ T ∈ Subsets k σ.length, W k m σ.length T := by
  have h := lemma1_concrete σ hσ k (evenRule k) (evenRule_subset k) (evenRule_nonadj k)
    (fun T T' _ _ hh => evenRule_stable k T T' hh)
  exact h.trans (sum_le_sum fun T hT => step2_pointwise k m σ.length hk T hT)

end Superpatterns
