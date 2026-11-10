import Superpatterns.Witness

/-!
# Block flip: machine-checked small instances of W90 Theorem 1

(and containment facts about the permutation `3416725` planted in W91 Lemma 2.3; that lemma
itself is not formalised).

For patterns `α`, `β` (possibly empty) the *block-flip theorem* (W90, Theorem 1; the transversal
case `k = 2` of Jelínek–Karpilovskij) says that for every `n`

  `#{σ ∈ S_n : σ ⊇ α ⊕ 21 ⊕ β} ≤ #{σ ∈ S_n : σ ⊇ α ⊕ 12 ⊕ β}`.

**The general theorem is NOT proved in this file.**  It is only *stated* (`BlockFlipStatement`),
and finitely many instances are certified by exhaustive enumeration of `S_n`.  A feasibility
assessment for the general proof is in `BLOCKFLIP-PLAN.md`.

## Contents

1. `containsB σ π : Bool`, a backtracking containment test, with a **complete** correctness proof
   `containsB_iff : containsB σ π = true ↔ Contains σ π` (soundness *and* completeness, so it also
   certifies avoidance).  It yields a `Decidable (Contains σ π)` instance.
2. `numContaining n π`, the number of permutations of `{1,…,n}` (as lists) that contain `π`,
   defined without reference to any algorithm (`Nat.card` of a subtype), and
   `numContaining_eq : numContaining n π = countB (List.range' 1 n) π`, where `countB` is an
   executable count over `List.permutations'`.  `card_Perms_contains` is the same statement for the
   project's `Perms n` (`Witness.lean`, permutations of `{0,…,n-1}`).
3. `dsum α β` (notation `α ⊕ₚ β`), the direct sum of patterns, with `dsum_perm`, `dsum_lt`,
   `dsum_assoc`.
4. Certificates (see the table in `README.md`): the two explicit permutations, the counts for
   `1234` / `1324` on `S_7`, `S_8`, `S_9`, block-flip instances as exact counts over all of `S_n`
   (`n = 7, 8, 9`) for `(α, β) ∈ {(1,1), (12,1), (1,12), (21,1), (12,12), (21,21)}`, and the
   inequality for all `|α|, |β| ≤ 2`, `n ≤ 8`.

## What is certified, and what is trusted

* **Kernel only** (`decide +kernel`; standard axioms `propext`, `Classical.choice`, `Quot.sound`,
  no compiler trust): parts 1–3; the facts about the two explicit permutations
  (`perm3416725_*`, `perm145278369_*`); every count with `n ≤ 7` (`count_*_7`, `blockFlip_*_7`);
  and the counts of `1234` and `1324` on `S_8` (`count_1234_8`, `count_1324_8`,
  `blockFlip_1_1_8`).  So both differences for `1234`/`1324`, `1` on `S_7` and `26` on `S_8`, are
  kernel-checked.
* **`native_decide`**: the other counts with `n = 8`, all counts with `n = 9` (`count_*_9`,
  `blockFlip_*_9`) and the sweep `blockFlipAt_of_le_2_of_le_8`.  Each use evaluates one closed
  Boolean statement and trusts the Lean compiler and the IR interpreter/runtime (one axiom
  `<theorem>._native.native_decide.ax_…` per use, the same trust assumption as
  `Certificates.lean`).  The reduction from the mathematical statement to that Boolean
  statement (`numContaining_eq`, `blockFlipAt_of_sweepB`) is kernel-checked.
* Kernel evaluation succeeds for every `n = 8` count (replace `native_decide` by
  `decide +kernel`), at about 21 s and 5.5 GB of memory per count on the development machine;
  it is used only for `1234`/`1324` to keep the build light.  At `n = 9` it was abandoned (more
  than 22 GB after 80 s).
* All statements are in terms of the mathematical predicate `Contains` (`Patterns.lean`) through
  `numContaining`; none is merely a statement about the Boolean checker.
* Host permutations are lists that are rearrangements of `[1, …, n]` (`List.range' 1 n`), patterns
  are written 1-based as well; `Contains` only depends on the relative order.
-/

namespace Superpatterns

/-! ## 1. A verified containment test -/

/-- A list of pairs `(host value, pattern value)` is *order-consistent*: the first coordinates
compare exactly like the second coordinates, for every two members of the list. -/
def IsoPairs (l : List (ℕ × ℕ)) : Prop :=
  ∀ a ∈ l, ∀ b ∈ l, (a.1 < b.1 ↔ a.2 < b.2)

theorem IsoPairs.of_subset {l m : List (ℕ × ℕ)} (hs : ∀ a ∈ l, a ∈ m) (h : IsoPairs m) :
    IsoPairs l :=
  fun a ha b hb => h a (hs a ha) b (hs b hb)

/-- Can the pair `(x, p)` be added to the order-consistent list `acc`? -/
def compat (acc : List (ℕ × ℕ)) (x p : ℕ) : Bool :=
  acc.all fun b =>
    (decide (b.1 < x) == decide (b.2 < p)) && (decide (x < b.1) == decide (p < b.2))

theorem isoPairs_cons {acc : List (ℕ × ℕ)} {x p : ℕ} :
    IsoPairs ((x, p) :: acc) ↔ compat acc x p = true ∧ IsoPairs acc := by
  constructor
  · intro h
    refine ⟨?_, h.of_subset fun a ha => List.mem_cons_of_mem _ ha⟩
    simp only [compat, List.all_eq_true, Bool.and_eq_true, beq_iff_eq, decide_eq_decide]
    intro b hb
    exact ⟨h b (List.mem_cons_of_mem _ hb) (x, p) List.mem_cons_self,
      h (x, p) List.mem_cons_self b (List.mem_cons_of_mem _ hb)⟩
  · rintro ⟨hc, h⟩ a ha b hb
    simp only [compat, List.all_eq_true, Bool.and_eq_true, beq_iff_eq, decide_eq_decide] at hc
    rcases List.mem_cons.1 ha with rfl | ha <;> rcases List.mem_cons.1 hb with rfl | hb
    · simp
    · exact (hc b hb).2
    · exact (hc a ha).1
    · exact h a ha b hb

/-- Backtracking search: `search xs ps acc` decides whether the remaining pattern entries `ps`
can be matched, in order, to a subsequence of the remaining host entries `xs`, consistently with
the pairs `acc` matched so far.  Structural recursion on `xs` (so the kernel can evaluate it). -/
def search : List ℕ → List ℕ → List (ℕ × ℕ) → Bool
  | _, [], _ => true
  | [], _ :: _, _ => false
  | x :: xs, p :: ps, acc =>
    (compat acc x p && search xs ps ((x, p) :: acc)) || search xs (p :: ps) acc

/-- Specification of `search`. -/
theorem search_iff : ∀ (xs ps : List ℕ) (acc : List (ℕ × ℕ)), IsoPairs acc →
    (search xs ps acc = true ↔
      ∃ τ : List ℕ, τ.Sublist xs ∧ τ.length = ps.length ∧ IsoPairs (τ.zip ps ++ acc)) := by
  intro xs
  induction xs with
  | nil =>
    intro ps acc hacc
    cases ps with
    | nil => simpa [search] using hacc
    | cons p ps => simp [search]
  | cons x xs ih =>
    intro ps acc hacc
    cases ps with
    | nil =>
      simp only [search, true_iff]
      exact ⟨[], List.nil_sublist _, rfl, by simpa using hacc⟩
    | cons p ps =>
      simp only [search, Bool.or_eq_true, Bool.and_eq_true]
      constructor
      · rintro (⟨hc, hs⟩ | hs)
        · have hacc' : IsoPairs ((x, p) :: acc) := isoPairs_cons.2 ⟨hc, hacc⟩
          obtain ⟨τ, hτ, hlen, hiso⟩ := (ih ps _ hacc').1 hs
          refine ⟨x :: τ, hτ.cons_cons x, by simp [hlen], hiso.of_subset ?_⟩
          intro a ha
          simp only [List.zip_cons_cons, List.cons_append, List.mem_cons, List.mem_append] at ha ⊢
          tauto
        · obtain ⟨τ, hτ, hlen, hiso⟩ := (ih (p :: ps) acc hacc).1 hs
          exact ⟨τ, hτ.cons x, hlen, hiso⟩
      · rintro ⟨τ, hτ, hlen, hiso⟩
        rcases List.sublist_cons_iff.1 hτ with h | ⟨r, rfl, h⟩
        · exact Or.inr ((ih (p :: ps) acc hacc).2 ⟨τ, h, hlen, hiso⟩)
        · have hiso' : IsoPairs (r.zip ps ++ (x, p) :: acc) := by
            refine hiso.of_subset ?_
            intro a ha
            simp only [List.zip_cons_cons, List.cons_append, List.mem_cons, List.mem_append]
              at ha ⊢
            tauto
          have hacc' : IsoPairs ((x, p) :: acc) :=
            hiso'.of_subset fun a ha => List.mem_append_right _ ha
          exact Or.inl ⟨(isoPairs_cons.1 hacc').1,
            (ih ps _ hacc').2 ⟨r, h, by simpa using hlen, hiso'⟩⟩

/-- `OrdIso` (index-based, `Patterns.lean`) in terms of the zipped list of pairs. -/
theorem ordIso_iff_isoPairs {τ π : List ℕ} :
    OrdIso τ π ↔ τ.length = π.length ∧ IsoPairs (τ.zip π) := by
  constructor
  · rintro ⟨hlen, h⟩
    refine ⟨hlen, ?_⟩
    intro a ha b hb
    obtain ⟨i, hi, rfl⟩ := List.mem_iff_getElem.1 ha
    obtain ⟨j, hj, rfl⟩ := List.mem_iff_getElem.1 hb
    simp only [List.length_zip] at hi hj
    simp only [List.getElem_zip]
    exact h i j (by omega) (by omega)
  · rintro ⟨hlen, h⟩
    refine ⟨hlen, fun i j hi hj => ?_⟩
    have hi' : i < (τ.zip π).length := by simp only [List.length_zip]; omega
    have hj' : j < (τ.zip π).length := by simp only [List.length_zip]; omega
    have := h _ (List.getElem_mem hi') _ (List.getElem_mem hj')
    simpa only [List.getElem_zip] using this

/-- The executable containment test. -/
def containsB (σ π : List ℕ) : Bool := search σ π []

/-- **Correctness of the containment test** (soundness and completeness) with respect to the
project's `Contains`.  No hypothesis on `σ`, `π` (they need not be permutations). -/
theorem containsB_iff (σ π : List ℕ) : containsB σ π = true ↔ Contains σ π := by
  unfold containsB Contains
  rw [search_iff σ π [] (by intro a ha; simp at ha)]
  simp only [List.append_nil]
  constructor
  · rintro ⟨τ, hτ, hlen, h⟩
    exact ⟨τ, hτ, ordIso_iff_isoPairs.2 ⟨hlen, h⟩⟩
  · rintro ⟨τ, hτ, h⟩
    obtain ⟨hlen, h⟩ := ordIso_iff_isoPairs.1 h
    exact ⟨τ, hτ, hlen, h⟩

/-- Pattern containment is decidable, via the verified test `containsB`. -/
instance instDecidableContains (σ π : List ℕ) : Decidable (Contains σ π) :=
  decidable_of_iff _ (containsB_iff σ π)

/-! ## 2. Counting permutations that contain a pattern -/

/-- Executable count: the number of arrangements of `base` (enumerated by
`List.permutations'`) on which the containment test succeeds. -/
def countB (base π : List ℕ) : ℕ := base.permutations'.countP (containsB · π)

/-- The number of rearrangements of a duplicate-free list `base` that contain `π` equals the
executable count. -/
theorem card_perm_contains (base π : List ℕ) (hb : base.Nodup) :
    Nat.card {σ : List ℕ // σ.Perm base ∧ Contains σ π} = countB base π := by
  have hnd : (base.permutations'.filter (containsB · π)).Nodup :=
    ((List.permutations_perm_permutations' base).nodup_iff.1
      (List.nodup_permutations base hb)).filter _
  have e : {σ : List ℕ // σ.Perm base ∧ Contains σ π} ≃
      {σ // σ ∈ (base.permutations'.filter (containsB · π)).toFinset} :=
    Equiv.subtypeEquivRight (fun σ => by simp [containsB_iff])
  rw [Nat.card_congr e, Nat.card_eq_fintype_card, Fintype.card_coe,
    List.toFinset_card_of_nodup hnd, countB, List.countP_eq_length_filter]

/-- `numContaining n π = #{σ ∈ S_n : σ contains π}`, where `S_n` is the set of lists that are
rearrangements of `[1, 2, …, n]` (one-line notation).  The definition mentions no algorithm. -/
noncomputable def numContaining (n : ℕ) (π : List ℕ) : ℕ :=
  Nat.card {σ : List ℕ // σ.Perm (List.range' 1 n) ∧ Contains σ π}

/-- Reduction of the mathematical count to the executable one (kernel-checked). -/
theorem numContaining_eq (n : ℕ) (π : List ℕ) :
    numContaining n π = countB (List.range' 1 n) π :=
  card_perm_contains _ _ List.nodup_range'

/-- The same reduction for the project's `Perms n` (permutations of `{0,…,n-1}`,
`Witness.lean`). -/
theorem card_Perms_contains (n : ℕ) (π : List ℕ) :
    Nat.card {σ : Perms n // Contains σ.1 π} = countB (List.range n) π := by
  rw [← card_perm_contains _ _ List.nodup_range]
  exact Nat.card_congr (Equiv.subtypeSubtypeEquivSubtypeInter
    (fun σ : List ℕ => σ.Perm (List.range n)) (fun σ => Contains σ π))

/-! ## 3. Direct sums of patterns -/

/-- Direct sum of patterns in one-line notation: `α ⊕ β` is `α` followed by `β` shifted up by
`|α|`.  This is the usual direct sum when `α` is a permutation of `{1,…,a}` (or of `{0,…,a-1}`)
and `β` is a permutation written in the same convention; see `dsum_perm` and `dsum_lt`. -/
def dsum (α β : List ℕ) : List ℕ := α ++ β.map (· + α.length)

@[inherit_doc] infixr:65 " ⊕ₚ " => dsum

@[simp] theorem length_dsum (α β : List ℕ) : (α ⊕ₚ β).length = α.length + β.length := by
  simp [dsum]

@[simp] theorem nil_dsum (β : List ℕ) : [] ⊕ₚ β = β := by simp [dsum]

@[simp] theorem dsum_nil (α : List ℕ) : α ⊕ₚ [] = α := by simp [dsum]

theorem dsum_assoc (α β γ : List ℕ) : (α ⊕ₚ β) ⊕ₚ γ = α ⊕ₚ (β ⊕ₚ γ) := by
  simp [dsum, Nat.add_comm]

/-- In `α ⊕ₚ β` every entry of the `α`-part is smaller than every entry of the (shifted)
`β`-part, as soon as the entries of `α` are `≤ |α|` and those of `β` are `≥ 1`. -/
theorem dsum_lt {α β : List ℕ} (hα : ∀ x ∈ α, x ≤ α.length) (hβ : ∀ y ∈ β, 1 ≤ y)
    {x y : ℕ} (hx : x ∈ α) (hy : y ∈ β.map (· + α.length)) : x < y := by
  obtain ⟨z, hz, rfl⟩ := List.mem_map.1 hy
  have := hα x hx
  have := hβ z hz
  omega

/-- The direct sum of a permutation of `{1,…,a}` and a permutation of `{1,…,b}` is a
permutation of `{1,…,a+b}`. -/
theorem dsum_perm {α β : List ℕ} {a b : ℕ} (hα : α.Perm (List.range' 1 a))
    (hβ : β.Perm (List.range' 1 b)) : (α ⊕ₚ β).Perm (List.range' 1 (a + b)) := by
  have ha : α.length = a := by simpa using hα.length_eq
  have h2 : (β.map (· + α.length)).Perm (List.range' (1 + a) b) := by
    have := hβ.map (a + ·)
    rw [List.map_add_range'] at this
    rw [ha, Nat.add_comm 1 a]
    simpa [Nat.add_comm] using this
  rw [← List.range'_append_1]
  exact hα.append h2

/-! ## 4. Certificates

### (a) Two explicit permutations (kernel-checked, standard axioms only)

`3 4 1 6 7 2 5` is the planted pattern `π₀` of W91 §2 (Burstein–Pantone's `3416725`): it contains
`1234` and avoids `1324`.  `1 4 5 2 7 8 3 6 9 = 1 ⊕ 3416725 ⊕ 1` contains `123456` and avoids
`124356 = 12 ⊕ 21 ⊕ 12`. -/

theorem perm3416725_mem : [3, 4, 1, 6, 7, 2, 5].Perm (List.range' 1 7) := by decide

theorem perm3416725_contains_1234 : Contains [3, 4, 1, 6, 7, 2, 5] [1, 2, 3, 4] := by
  decide +kernel

theorem perm3416725_avoids_1324 : ¬ Contains [3, 4, 1, 6, 7, 2, 5] [1, 3, 2, 4] := by
  decide +kernel

theorem perm145278369_mem : [1, 4, 5, 2, 7, 8, 3, 6, 9].Perm (List.range' 1 9) := by decide

theorem perm145278369_contains_123456 :
    Contains [1, 4, 5, 2, 7, 8, 3, 6, 9] [1, 2, 3, 4, 5, 6] := by
  decide +kernel

theorem perm145278369_avoids_124356 :
    ¬ Contains [1, 4, 5, 2, 7, 8, 3, 6, 9] [1, 2, 4, 3, 5, 6] := by
  decide +kernel

/-- `1 4 5 2 7 8 3 6 9 = 1 ⊕ 3416725 ⊕ 1`, and `1 4 5 2 7 8 3 6 = 1 ⊕ 3416725` is the second
planted order type `π₁` of W91 §2. -/
theorem perm145278369_eq_dsum :
    [1] ⊕ₚ [3, 4, 1, 6, 7, 2, 5] ⊕ₚ [1] = [1, 4, 5, 2, 7, 8, 3, 6, 9] ∧
      [1] ⊕ₚ [3, 4, 1, 6, 7, 2, 5] = [1, 4, 5, 2, 7, 8, 3, 6] := by
  decide

/-- The patterns of the block-flip instances below, written out. -/
theorem dsum_examples :
    [1] ⊕ₚ [1, 2] ⊕ₚ [1] = [1, 2, 3, 4] ∧ [1] ⊕ₚ [2, 1] ⊕ₚ [1] = [1, 3, 2, 4] ∧
    [1, 2] ⊕ₚ [1, 2] ⊕ₚ [1, 2] = [1, 2, 3, 4, 5, 6] ∧
    [1, 2] ⊕ₚ [2, 1] ⊕ₚ [1, 2] = [1, 2, 4, 3, 5, 6] ∧
    [2, 1] ⊕ₚ [1, 2] ⊕ₚ [2, 1] = [2, 1, 3, 4, 6, 5] ∧
    [2, 1] ⊕ₚ [2, 1] ⊕ₚ [2, 1] = [2, 1, 4, 3, 6, 5] := by
  decide

/-! ### (b), (c) Exact counts over all of `S_n`

`count_π_n : numContaining n π = N` says that exactly `N` of the `n!` permutations of
`{1,…,n}` contain `π`.  Reference values were computed beforehand by an independent brute-force
program (Python, different algorithm); Lean re-derives each of them. -/

/-! #### `n = 7`: kernel (`decide +kernel`), no compiler trust -/

theorem count_1234_7 : numContaining 7 [1, 2, 3, 4] = 2279 := by
  rw [numContaining_eq]; decide +kernel
theorem count_1324_7 : numContaining 7 [1, 3, 2, 4] = 2278 := by
  rw [numContaining_eq]; decide +kernel
theorem count_12345_7 : numContaining 7 [1, 2, 3, 4, 5] = 458 := by
  rw [numContaining_eq]; decide +kernel
theorem count_12435_7 : numContaining 7 [1, 2, 4, 3, 5] = 458 := by
  rw [numContaining_eq]; decide +kernel
theorem count_13245_7 : numContaining 7 [1, 3, 2, 4, 5] = 458 := by
  rw [numContaining_eq]; decide +kernel
theorem count_21345_7 : numContaining 7 [2, 1, 3, 4, 5] = 458 := by
  rw [numContaining_eq]; decide +kernel
theorem count_21435_7 : numContaining 7 [2, 1, 4, 3, 5] = 458 := by
  rw [numContaining_eq]; decide +kernel
theorem count_123456_7 : numContaining 7 [1, 2, 3, 4, 5, 6] = 37 := by
  rw [numContaining_eq]; decide +kernel
theorem count_124356_7 : numContaining 7 [1, 2, 4, 3, 5, 6] = 37 := by
  rw [numContaining_eq]; decide +kernel
theorem count_213465_7 : numContaining 7 [2, 1, 3, 4, 6, 5] = 37 := by
  rw [numContaining_eq]; decide +kernel
theorem count_214365_7 : numContaining 7 [2, 1, 4, 3, 6, 5] = 37 := by
  rw [numContaining_eq]; decide +kernel

/-! #### `n = 8`: `native_decide` (trusts the Lean compiler and runtime), except `1234` and `1324`,
which are kernel-checked (about 21 s and 5.5 GB of memory each) -/

theorem count_1234_8 : numContaining 8 [1, 2, 3, 4] = 24553 := by
  rw [numContaining_eq]; decide +kernel
theorem count_1324_8 : numContaining 8 [1, 3, 2, 4] = 24527 := by
  rw [numContaining_eq]; decide +kernel
theorem count_12345_8 : numContaining 8 [1, 2, 3, 4, 5] = 6996 := by
  rw [numContaining_eq]; native_decide
theorem count_12435_8 : numContaining 8 [1, 2, 4, 3, 5] = 6995 := by
  rw [numContaining_eq]; native_decide
theorem count_13245_8 : numContaining 8 [1, 3, 2, 4, 5] = 6995 := by
  rw [numContaining_eq]; native_decide
theorem count_21345_8 : numContaining 8 [2, 1, 3, 4, 5] = 6996 := by
  rw [numContaining_eq]; native_decide
theorem count_21435_8 : numContaining 8 [2, 1, 4, 3, 5] = 6995 := by
  rw [numContaining_eq]; native_decide
theorem count_123456_8 : numContaining 8 [1, 2, 3, 4, 5, 6] = 891 := by
  rw [numContaining_eq]; native_decide
theorem count_124356_8 : numContaining 8 [1, 2, 4, 3, 5, 6] = 891 := by
  rw [numContaining_eq]; native_decide
theorem count_213465_8 : numContaining 8 [2, 1, 3, 4, 6, 5] = 891 := by
  rw [numContaining_eq]; native_decide
theorem count_214365_8 : numContaining 8 [2, 1, 4, 3, 6, 5] = 891 := by
  rw [numContaining_eq]; native_decide

/-! #### `n = 9`: `native_decide` (trusts the Lean compiler and runtime) -/

theorem count_1234_9 : numContaining 9 [1, 2, 3, 4] = 268521 := by
  rw [numContaining_eq]; native_decide
theorem count_1324_9 : numContaining 9 [1, 3, 2, 4] = 268104 := by
  rw [numContaining_eq]; native_decide
theorem count_12345_9 : numContaining 9 [1, 2, 3, 4, 5] = 101072 := by
  rw [numContaining_eq]; native_decide
theorem count_12435_9 : numContaining 9 [1, 2, 4, 3, 5] = 101027 := by
  rw [numContaining_eq]; native_decide
theorem count_13245_9 : numContaining 9 [1, 3, 2, 4, 5] = 101027 := by
  rw [numContaining_eq]; native_decide
theorem count_21345_9 : numContaining 9 [2, 1, 3, 4, 5] = 101072 := by
  rw [numContaining_eq]; native_decide
theorem count_21435_9 : numContaining 9 [2, 1, 4, 3, 5] = 101027 := by
  rw [numContaining_eq]; native_decide
theorem count_123456_9 : numContaining 9 [1, 2, 3, 4, 5, 6] = 18043 := by
  rw [numContaining_eq]; native_decide
theorem count_124356_9 : numContaining 9 [1, 2, 4, 3, 5, 6] = 18042 := by
  rw [numContaining_eq]; native_decide
theorem count_213465_9 : numContaining 9 [2, 1, 3, 4, 6, 5] = 18043 := by
  rw [numContaining_eq]; native_decide
theorem count_214365_9 : numContaining 9 [2, 1, 4, 3, 6, 5] = 18042 := by
  rw [numContaining_eq]; native_decide

/-! ### (b) `1234` versus `1324` -/

/-- `#{σ ∈ S_n ⊇ 1234} = #{σ ∈ S_n ⊇ 1324}` for `n ≤ 6` (kernel-checked). -/
theorem count_1234_eq_count_1324_of_le_6 (n : ℕ) (hn : n ≤ 6) :
    numContaining n [1, 2, 3, 4] = numContaining n [1, 3, 2, 4] := by
  rw [numContaining_eq, numContaining_eq]
  interval_cases n <;> decide +kernel

/-- `#{σ ∈ S_7 ⊇ 1234} − #{σ ∈ S_7 ⊇ 1324} = 2279 − 2278 = 1`, i.e.
`|Av_7(1324)| − |Av_7(1234)| = 1` (kernel-checked). -/
theorem count_1234_sub_count_1324_7 :
    numContaining 7 [1, 2, 3, 4] = numContaining 7 [1, 3, 2, 4] + 1 := by
  rw [count_1234_7, count_1324_7]

/-- `#{σ ∈ S_8 ⊇ 1234} − #{σ ∈ S_8 ⊇ 1324} = 24553 − 24527 = 26`, i.e.
`|Av_8(1324)| − |Av_8(1234)| = 15793 − 15767 = 26` (kernel-checked). -/
theorem count_1234_sub_count_1324_8 :
    numContaining 8 [1, 2, 3, 4] = numContaining 8 [1, 3, 2, 4] + 26 := by
  rw [count_1234_8, count_1324_8]

/-- `#{σ ∈ S_9 ⊇ 1234} − #{σ ∈ S_9 ⊇ 1324} = 268521 − 268104 = 417` (`native_decide`). -/
theorem count_1234_sub_count_1324_9 :
    numContaining 9 [1, 2, 3, 4] = numContaining 9 [1, 3, 2, 4] + 417 := by
  rw [count_1234_9, count_1324_9]

/-! ### `123456` versus `124356 = 12 ⊕ 21 ⊕ 12` -/

/-- `#{σ ∈ S_n ⊇ 123456} = #{σ ∈ S_n ⊇ 124356}` for `n ≤ 8` (kernel-checked for `n ≤ 7`,
`native_decide` for `n = 8`). -/
theorem count_123456_eq_count_124356_of_le_8 (n : ℕ) (hn : n ≤ 8) :
    numContaining n [1, 2, 3, 4, 5, 6] = numContaining n [1, 2, 4, 3, 5, 6] := by
  obtain h | rfl | rfl : n ≤ 6 ∨ n = 7 ∨ n = 8 := by omega
  · rw [numContaining_eq, numContaining_eq]
    interval_cases n <;> decide +kernel
  · rw [count_123456_7, count_124356_7]
  · rw [count_123456_8, count_124356_8]

/-- `#{σ ∈ S_9 ⊇ 123456} − #{σ ∈ S_9 ⊇ 124356} = 18043 − 18042 = 1`: the first discrepancy
(`native_decide`; a witness is `1 4 5 2 7 8 3 6 9`, see `perm145278369_avoids_124356`). -/
theorem count_123456_sub_count_124356_9 :
    numContaining 9 [1, 2, 3, 4, 5, 6] = numContaining 9 [1, 2, 4, 3, 5, 6] + 1 := by
  rw [count_123456_9, count_124356_9]

/-! ### (c), (d) Block-flip instances, phrased through `⊕ₚ`

`blockFlip_α_β_n` gives the two exact counts, `blockFlipAt_α_β_n` the resulting inequality.
The instances with `n = 7`, and `blockFlip_1_1_8`, rest on kernel-checked counts only; the
other instances with `n = 8` and all instances with `n = 9` rest on `native_decide` counts. -/

/-- The block-flip inequality for one triple `(n, α, β)`:
`#{σ ∈ S_n ⊇ α ⊕ 21 ⊕ β} ≤ #{σ ∈ S_n ⊇ α ⊕ 12 ⊕ β}`. -/
def BlockFlipAt (n : ℕ) (α β : List ℕ) : Prop :=
  numContaining n (α ⊕ₚ [2, 1] ⊕ₚ β) ≤ numContaining n (α ⊕ₚ [1, 2] ⊕ₚ β)

/-- The **statement** of the block-flip theorem (W90, Theorem 1).  It is *not* proved in this
project; only the instances below are.  See `BLOCKFLIP-PLAN.md`. -/
def BlockFlipStatement : Prop :=
  ∀ (a b n : ℕ) (α β : List ℕ), α.Perm (List.range' 1 a) → β.Perm (List.range' 1 b) →
    BlockFlipAt n α β

theorem BlockFlipAt.of_counts {n : ℕ} {α β : List ℕ} {A B : ℕ}
    (h : numContaining n (α ⊕ₚ [2, 1] ⊕ₚ β) = A ∧ numContaining n (α ⊕ₚ [1, 2] ⊕ₚ β) = B)
    (hAB : A ≤ B) : BlockFlipAt n α β := by
  unfold BlockFlipAt
  rw [h.1, h.2]
  exact hAB

/-- `(α, β) = (1, 1)`, `n = 7`: `1324` is contained in 2278 permutations, `1234` in 2279
(difference 1). -/
theorem blockFlip_1_1_7 :
    numContaining 7 ([1] ⊕ₚ [2, 1] ⊕ₚ [1]) = 2278 ∧
      numContaining 7 ([1] ⊕ₚ [1, 2] ⊕ₚ [1]) = 2279 :=
  ⟨count_1324_7, count_1234_7⟩

theorem blockFlipAt_1_1_7 : BlockFlipAt 7 [1] [1] :=
  .of_counts blockFlip_1_1_7 (by decide)

/-- `(α, β) = (1, 1)`, `n = 8`: `1324` is contained in 24527 permutations, `1234` in 24553
(difference 26). -/
theorem blockFlip_1_1_8 :
    numContaining 8 ([1] ⊕ₚ [2, 1] ⊕ₚ [1]) = 24527 ∧
      numContaining 8 ([1] ⊕ₚ [1, 2] ⊕ₚ [1]) = 24553 :=
  ⟨count_1324_8, count_1234_8⟩

theorem blockFlipAt_1_1_8 : BlockFlipAt 8 [1] [1] :=
  .of_counts blockFlip_1_1_8 (by decide)

/-- `(α, β) = (1, 1)`, `n = 9`: `1324` is contained in 268104 permutations, `1234` in 268521
(difference 417). -/
theorem blockFlip_1_1_9 :
    numContaining 9 ([1] ⊕ₚ [2, 1] ⊕ₚ [1]) = 268104 ∧
      numContaining 9 ([1] ⊕ₚ [1, 2] ⊕ₚ [1]) = 268521 :=
  ⟨count_1324_9, count_1234_9⟩

theorem blockFlipAt_1_1_9 : BlockFlipAt 9 [1] [1] :=
  .of_counts blockFlip_1_1_9 (by decide)

/-- `(α, β) = (12, 1)`, `n = 7`: `12435` is contained in 458 permutations, `12345` in 458
(difference 0). -/
theorem blockFlip_12_1_7 :
    numContaining 7 ([1, 2] ⊕ₚ [2, 1] ⊕ₚ [1]) = 458 ∧
      numContaining 7 ([1, 2] ⊕ₚ [1, 2] ⊕ₚ [1]) = 458 :=
  ⟨count_12435_7, count_12345_7⟩

theorem blockFlipAt_12_1_7 : BlockFlipAt 7 [1, 2] [1] :=
  .of_counts blockFlip_12_1_7 (by decide)

/-- `(α, β) = (12, 1)`, `n = 8`: `12435` is contained in 6995 permutations, `12345` in 6996
(difference 1). -/
theorem blockFlip_12_1_8 :
    numContaining 8 ([1, 2] ⊕ₚ [2, 1] ⊕ₚ [1]) = 6995 ∧
      numContaining 8 ([1, 2] ⊕ₚ [1, 2] ⊕ₚ [1]) = 6996 :=
  ⟨count_12435_8, count_12345_8⟩

theorem blockFlipAt_12_1_8 : BlockFlipAt 8 [1, 2] [1] :=
  .of_counts blockFlip_12_1_8 (by decide)

/-- `(α, β) = (12, 1)`, `n = 9`: `12435` is contained in 101027 permutations, `12345` in 101072
(difference 45). -/
theorem blockFlip_12_1_9 :
    numContaining 9 ([1, 2] ⊕ₚ [2, 1] ⊕ₚ [1]) = 101027 ∧
      numContaining 9 ([1, 2] ⊕ₚ [1, 2] ⊕ₚ [1]) = 101072 :=
  ⟨count_12435_9, count_12345_9⟩

theorem blockFlipAt_12_1_9 : BlockFlipAt 9 [1, 2] [1] :=
  .of_counts blockFlip_12_1_9 (by decide)

/-- `(α, β) = (1, 12)`, `n = 7`: `13245` is contained in 458 permutations, `12345` in 458
(difference 0). -/
theorem blockFlip_1_12_7 :
    numContaining 7 ([1] ⊕ₚ [2, 1] ⊕ₚ [1, 2]) = 458 ∧
      numContaining 7 ([1] ⊕ₚ [1, 2] ⊕ₚ [1, 2]) = 458 :=
  ⟨count_13245_7, count_12345_7⟩

theorem blockFlipAt_1_12_7 : BlockFlipAt 7 [1] [1, 2] :=
  .of_counts blockFlip_1_12_7 (by decide)

/-- `(α, β) = (1, 12)`, `n = 8`: `13245` is contained in 6995 permutations, `12345` in 6996
(difference 1). -/
theorem blockFlip_1_12_8 :
    numContaining 8 ([1] ⊕ₚ [2, 1] ⊕ₚ [1, 2]) = 6995 ∧
      numContaining 8 ([1] ⊕ₚ [1, 2] ⊕ₚ [1, 2]) = 6996 :=
  ⟨count_13245_8, count_12345_8⟩

theorem blockFlipAt_1_12_8 : BlockFlipAt 8 [1] [1, 2] :=
  .of_counts blockFlip_1_12_8 (by decide)

/-- `(α, β) = (1, 12)`, `n = 9`: `13245` is contained in 101027 permutations, `12345` in 101072
(difference 45). -/
theorem blockFlip_1_12_9 :
    numContaining 9 ([1] ⊕ₚ [2, 1] ⊕ₚ [1, 2]) = 101027 ∧
      numContaining 9 ([1] ⊕ₚ [1, 2] ⊕ₚ [1, 2]) = 101072 :=
  ⟨count_13245_9, count_12345_9⟩

theorem blockFlipAt_1_12_9 : BlockFlipAt 9 [1] [1, 2] :=
  .of_counts blockFlip_1_12_9 (by decide)

/-- `(α, β) = (21, 1)`, `n = 7`: `21435` is contained in 458 permutations, `21345` in 458
(difference 0). -/
theorem blockFlip_21_1_7 :
    numContaining 7 ([2, 1] ⊕ₚ [2, 1] ⊕ₚ [1]) = 458 ∧
      numContaining 7 ([2, 1] ⊕ₚ [1, 2] ⊕ₚ [1]) = 458 :=
  ⟨count_21435_7, count_21345_7⟩

theorem blockFlipAt_21_1_7 : BlockFlipAt 7 [2, 1] [1] :=
  .of_counts blockFlip_21_1_7 (by decide)

/-- `(α, β) = (21, 1)`, `n = 8`: `21435` is contained in 6995 permutations, `21345` in 6996
(difference 1). -/
theorem blockFlip_21_1_8 :
    numContaining 8 ([2, 1] ⊕ₚ [2, 1] ⊕ₚ [1]) = 6995 ∧
      numContaining 8 ([2, 1] ⊕ₚ [1, 2] ⊕ₚ [1]) = 6996 :=
  ⟨count_21435_8, count_21345_8⟩

theorem blockFlipAt_21_1_8 : BlockFlipAt 8 [2, 1] [1] :=
  .of_counts blockFlip_21_1_8 (by decide)

/-- `(α, β) = (21, 1)`, `n = 9`: `21435` is contained in 101027 permutations, `21345` in 101072
(difference 45). -/
theorem blockFlip_21_1_9 :
    numContaining 9 ([2, 1] ⊕ₚ [2, 1] ⊕ₚ [1]) = 101027 ∧
      numContaining 9 ([2, 1] ⊕ₚ [1, 2] ⊕ₚ [1]) = 101072 :=
  ⟨count_21435_9, count_21345_9⟩

theorem blockFlipAt_21_1_9 : BlockFlipAt 9 [2, 1] [1] :=
  .of_counts blockFlip_21_1_9 (by decide)

/-- `(α, β) = (12, 12)`, `n = 7`: `124356` is contained in 37 permutations, `123456` in 37
(difference 0). -/
theorem blockFlip_12_12_7 :
    numContaining 7 ([1, 2] ⊕ₚ [2, 1] ⊕ₚ [1, 2]) = 37 ∧
      numContaining 7 ([1, 2] ⊕ₚ [1, 2] ⊕ₚ [1, 2]) = 37 :=
  ⟨count_124356_7, count_123456_7⟩

theorem blockFlipAt_12_12_7 : BlockFlipAt 7 [1, 2] [1, 2] :=
  .of_counts blockFlip_12_12_7 (by decide)

/-- `(α, β) = (12, 12)`, `n = 8`: `124356` is contained in 891 permutations, `123456` in 891
(difference 0). -/
theorem blockFlip_12_12_8 :
    numContaining 8 ([1, 2] ⊕ₚ [2, 1] ⊕ₚ [1, 2]) = 891 ∧
      numContaining 8 ([1, 2] ⊕ₚ [1, 2] ⊕ₚ [1, 2]) = 891 :=
  ⟨count_124356_8, count_123456_8⟩

theorem blockFlipAt_12_12_8 : BlockFlipAt 8 [1, 2] [1, 2] :=
  .of_counts blockFlip_12_12_8 (by decide)

/-- `(α, β) = (12, 12)`, `n = 9`: `124356` is contained in 18042 permutations, `123456` in 18043
(difference 1). -/
theorem blockFlip_12_12_9 :
    numContaining 9 ([1, 2] ⊕ₚ [2, 1] ⊕ₚ [1, 2]) = 18042 ∧
      numContaining 9 ([1, 2] ⊕ₚ [1, 2] ⊕ₚ [1, 2]) = 18043 :=
  ⟨count_124356_9, count_123456_9⟩

theorem blockFlipAt_12_12_9 : BlockFlipAt 9 [1, 2] [1, 2] :=
  .of_counts blockFlip_12_12_9 (by decide)

/-- `(α, β) = (21, 21)`, `n = 7`: `214365` is contained in 37 permutations, `213465` in 37
(difference 0). -/
theorem blockFlip_21_21_7 :
    numContaining 7 ([2, 1] ⊕ₚ [2, 1] ⊕ₚ [2, 1]) = 37 ∧
      numContaining 7 ([2, 1] ⊕ₚ [1, 2] ⊕ₚ [2, 1]) = 37 :=
  ⟨count_214365_7, count_213465_7⟩

theorem blockFlipAt_21_21_7 : BlockFlipAt 7 [2, 1] [2, 1] :=
  .of_counts blockFlip_21_21_7 (by decide)

/-- `(α, β) = (21, 21)`, `n = 8`: `214365` is contained in 891 permutations, `213465` in 891
(difference 0). -/
theorem blockFlip_21_21_8 :
    numContaining 8 ([2, 1] ⊕ₚ [2, 1] ⊕ₚ [2, 1]) = 891 ∧
      numContaining 8 ([2, 1] ⊕ₚ [1, 2] ⊕ₚ [2, 1]) = 891 :=
  ⟨count_214365_8, count_213465_8⟩

theorem blockFlipAt_21_21_8 : BlockFlipAt 8 [2, 1] [2, 1] :=
  .of_counts blockFlip_21_21_8 (by decide)

/-- `(α, β) = (21, 21)`, `n = 9`: `214365` is contained in 18042 permutations, `213465` in 18043
(difference 1). -/
theorem blockFlip_21_21_9 :
    numContaining 9 ([2, 1] ⊕ₚ [2, 1] ⊕ₚ [2, 1]) = 18042 ∧
      numContaining 9 ([2, 1] ⊕ₚ [1, 2] ⊕ₚ [2, 1]) = 18043 :=
  ⟨count_214365_9, count_213465_9⟩

theorem blockFlipAt_21_21_9 : BlockFlipAt 9 [2, 1] [2, 1] :=
  .of_counts blockFlip_21_21_9 (by decide)

/-! ### A bounded sweep over all small `(α, β)` -/

/-- Boolean form of "the block-flip inequality holds for all permutations `α`, `β` of size
`≤ m` and all `n ≤ N`". -/
def sweepB (m N : ℕ) : Bool :=
  (List.range (m + 1)).all fun a => (List.range (m + 1)).all fun b =>
    (List.range' 1 a).permutations'.all fun α => (List.range' 1 b).permutations'.all fun β =>
      (List.range (N + 1)).all fun n =>
        decide (countB (List.range' 1 n) (α ⊕ₚ [2, 1] ⊕ₚ β) ≤
          countB (List.range' 1 n) (α ⊕ₚ [1, 2] ⊕ₚ β))

/-- Soundness of the sweep (kernel-checked). -/
theorem blockFlipAt_of_sweepB {m N : ℕ} (h : sweepB m N = true) {a b n : ℕ} (ha : a ≤ m)
    (hb : b ≤ m) (hn : n ≤ N) {α β : List ℕ} (hα : α.Perm (List.range' 1 a))
    (hβ : β.Perm (List.range' 1 b)) : BlockFlipAt n α β := by
  simp only [sweepB, List.all_eq_true, List.mem_range, List.mem_permutations',
    decide_eq_true_eq] at h
  have := h a (by omega) b (by omega) α hα β hβ n (by omega)
  simpa only [BlockFlipAt, numContaining_eq] using this

/-- **Block flip for all `α, β` of size at most 2 and all `n ≤ 8`** (16 pairs `(α, β)`, including
the empty pattern, e.g. `(∅, 1)`: `213` vs `123`, and `(12, 21)`, `(21, 12)`).  Proved by
`native_decide` on `sweepB 2 8`. -/
theorem blockFlipAt_of_le_2_of_le_8 {a b n : ℕ} (ha : a ≤ 2) (hb : b ≤ 2) (hn : n ≤ 8)
    {α β : List ℕ} (hα : α.Perm (List.range' 1 a)) (hβ : β.Perm (List.range' 1 b)) :
    BlockFlipAt n α β :=
  blockFlipAt_of_sweepB (by native_decide) ha hb hn hα hβ

end Superpatterns
