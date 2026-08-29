import Archive.Wiedijk100Theorems.AscendingDescendingSequences
import Superpatterns.BlockSplit

/-!
# Erdős–Szekeres disjointness (W28 Theorem 2.1)

For a duplicate-free list `σ` of length `n > (a-1)(b-1)`, `σ` contains the increasing pattern
`12⋯a = List.range a` or the decreasing pattern `b⋯21 = (List.range b).reverse`.

We reuse Mathlib's `Theorems100.erdos_szekeres` (from `Archive/Wiedijk100Theorems/`, which is a
declared library of the Mathlib package and builds from the cached Mathlib oleans) and connect
it to the project's `Contains` (Patterns.lean).
-/

namespace Superpatterns

open Finset

/-- `List.ofFn (σ[f ·])` for an order embedding `f` of indices is a subsequence of `σ`. -/
theorem ofFn_sublist (σ : List ℕ) {a : ℕ} (f : Fin a ↪o Fin σ.length) :
    (List.ofFn fun i => σ[f i]).Sublist σ := by
  rw [List.sublist_iff_exists_fin_orderEmbedding_get_eq]
  refine ⟨(Fin.castOrderIso (List.length_ofFn)).toOrderEmbedding.trans f, ?_⟩
  intro ix
  simp [List.getElem_ofFn]
  rfl

/-- A strictly increasing list of length `a` is order-isomorphic to `12⋯a`. -/
theorem OrdIso_range_of_strictMono {a : ℕ} (g : Fin a → ℕ) (hg : StrictMono g) :
    OrdIso (List.ofFn g) (List.range a) := by
  refine ⟨by simp, fun i j hi hj => ?_⟩
  simp only [List.length_ofFn] at hi hj
  simp only [List.getElem_ofFn, List.getElem_range]
  rw [hg.lt_iff_lt, Fin.mk_lt_mk]

/-- A strictly decreasing list of length `b` is order-isomorphic to `b⋯21`. -/
theorem OrdIso_range_reverse_of_strictAnti {b : ℕ} (g : Fin b → ℕ) (hg : StrictAnti g) :
    OrdIso (List.ofFn g) (List.range b).reverse := by
  refine ⟨by simp, fun i j hi hj => ?_⟩
  simp only [List.length_ofFn] at hi hj
  simp only [List.getElem_ofFn, List.getElem_reverse, List.length_range, List.getElem_range]
  rw [hg.lt_iff_gt, Fin.mk_lt_mk]
  omega

/-- **Erdős–Szekeres** in pattern language: a duplicate-free sequence of length `> (a-1)(b-1)`
contains `12⋯a` or `b⋯21`. -/
theorem erdos_szekeres_contains (σ : List ℕ) (hσ : σ.Nodup) {a b : ℕ}
    (hn : (a - 1) * (b - 1) < σ.length) :
    Contains σ (List.range a) ∨ Contains σ (List.range b).reverse := by
  classical
  have hinj : Function.Injective (fun i : Fin σ.length => σ[i]) := by
    intro i j h
    exact Fin.ext ((List.Nodup.getElem_inj_iff hσ).1 h)
  rw [← Fintype.card_fin σ.length] at hn
  rcases Theorems100.erdos_szekeres hn hinj with ⟨t, ht, hmono⟩ | ⟨t, ht, hanti⟩
  · obtain ⟨s, hst, hs⟩ := Finset.exists_subset_card_eq (show a ≤ t.card by omega)
    let f := s.orderEmbOfFin hs
    refine Or.inl ⟨List.ofFn fun i => σ[f i], ofFn_sublist σ f,
      OrdIso_range_of_strictMono _ fun i j hij => ?_⟩
    exact hmono (hst (s.orderEmbOfFin_mem hs i)) (hst (s.orderEmbOfFin_mem hs j))
      (f.strictMono hij)
  · obtain ⟨s, hst, hs⟩ := Finset.exists_subset_card_eq (show b ≤ t.card by omega)
    let f := s.orderEmbOfFin hs
    refine Or.inr ⟨List.ofFn fun i => σ[f i], ofFn_sublist σ f,
      OrdIso_range_reverse_of_strictAnti _ fun i j hij => ?_⟩
    exact hanti (hst (s.orderEmbOfFin_mem hs i)) (hst (s.orderEmbOfFin_mem hs j))
      (f.strictMono hij)

/-- **Disjointness (W28 Thm 2.1)**: for `n > (a-1)(b-1)` no `σ ∈ S_n` avoids both `12⋯a` and
`b⋯21`. -/
theorem not_avoid_both (σ : List ℕ) (hσ : σ.Nodup) {a b : ℕ}
    (hn : (a - 1) * (b - 1) < σ.length) :
    ¬ (¬ Contains σ (List.range a) ∧ ¬ Contains σ (List.range b).reverse) := by
  rintro ⟨h1, h2⟩
  rcases erdos_szekeres_contains σ hσ hn with h | h
  · exact h1 h
  · exact h2 h

/-- Specialisation to `S_n` with `n ≥ (k-1)² + 1`: the identity and the reverse identity of
length `k` are never simultaneously missing. -/
theorem not_avoid_id_rev {k : ℕ} (σ : List ℕ) (hσ : σ.Nodup) (hn : (k - 1) * (k - 1) < σ.length) :
    Contains σ (List.range k) ∨ Contains σ (List.range k).reverse :=
  erdos_szekeres_contains σ hσ hn

end Superpatterns
