import Superpatterns.Patterns

/-!
# Block splitting: the combinatorial core (W27 Lemma 0.2, deterministic part)

* `OrdIso` is an equivalence relation (`OrdIso.refl`, `.symm`, `.trans`).
* `Contains.of_sublist` / `not_contains_of_sublist`: containment is hereditary under passing
  to a supersequence, i.e. avoidance is hereditary under passing to a subsequence.
* `contains_ranks_iff`: standardising a list (`ranks`) does not change which patterns it
  contains.
* `block σ a m` is the position block `σ[a], …, σ[a+m-1]`; `blockStd σ a m` its standardisation.
  `blockStd_avoids`: if `σ` avoids `π` then every block standardisation avoids `π`.
* `ranks_perm_range`: the standardisation of a duplicate-free list of length `m` is a
  permutation of `{0,…,m-1}` (so `blockStd σ a m ∈ S_m` when `σ` is a permutation).

The probabilistic part of Lemma 0.2 (`p_π(N) ≤ p_π(M)^{⌊N/M⌋}`, independence of the block
standardisations under the uniform law on `S_N`) is **not** formalised here; see the README.
-/

namespace Superpatterns

theorem OrdIso.refl (l : List ℕ) : OrdIso l l := ⟨rfl, fun _ _ _ _ => Iff.rfl⟩

theorem OrdIso.symm {l m : List ℕ} (h : OrdIso l m) : OrdIso m l := by
  obtain ⟨hlen, h⟩ := h
  refine ⟨hlen.symm, fun i j hi hj => ?_⟩
  exact (h i j (hlen ▸ hi) (hlen ▸ hj)).symm

theorem OrdIso.trans {l m n : List ℕ} (h₁ : OrdIso l m) (h₂ : OrdIso m n) : OrdIso l n := by
  obtain ⟨hlen₁, h₁⟩ := h₁
  obtain ⟨hlen₂, h₂⟩ := h₂
  refine ⟨hlen₁.trans hlen₂, fun i j hi hj => ?_⟩
  exact (h₁ i j hi hj).trans (h₂ i j (hlen₁ ▸ hi) (hlen₁ ▸ hj))

/-- Containment is monotone in the host: a pattern of a subsequence is a pattern of the
whole sequence. -/
theorem Contains.of_sublist {σ τ π : List ℕ} (h : τ.Sublist σ) (hc : Contains τ π) :
    Contains σ π :=
  let ⟨ρ, hρ, hiso⟩ := hc
  ⟨ρ, hρ.trans h, hiso⟩

/-- Avoidance is hereditary: every subsequence of a `π`-avoiding sequence avoids `π`. -/
theorem not_contains_of_sublist {σ τ π : List ℕ} (h : τ.Sublist σ) (hσ : ¬ Contains σ π) :
    ¬ Contains τ π :=
  fun hc => hσ (hc.of_sublist h)

/-- Containment is invariant under replacing the pattern by an order-isomorphic one. -/
theorem Contains.of_ordIso {σ π π' : List ℕ} (hc : Contains σ π) (h : OrdIso π π') :
    Contains σ π' :=
  let ⟨ρ, hρ, hiso⟩ := hc
  ⟨ρ, hρ, hiso.trans h⟩

/-- A list all of whose entries lie in `σ` is order-isomorphic to its image under `rank σ`. -/
theorem OrdIso_map_rank {σ τ : List ℕ} (hτ : ∀ x ∈ τ, x ∈ σ) :
    OrdIso τ (τ.map (rank σ)) := by
  refine ⟨by simp, fun i j hi hj => ?_⟩
  simp only [List.getElem_map]
  exact lt_iff_rank_lt σ (hτ _ (List.getElem_mem hi))

/-- A list is order-isomorphic to its standardisation. -/
theorem OrdIso_ranks (l : List ℕ) : OrdIso l (ranks l) :=
  OrdIso_map_rank (fun _ h => h)

/-- Standardisation does not change the set of contained patterns. -/
theorem contains_ranks_iff (σ π : List ℕ) : Contains (ranks σ) π ↔ Contains σ π := by
  constructor
  · rintro ⟨τ', hτ', hiso⟩
    obtain ⟨τ, hτ, rfl⟩ := List.sublist_map_iff.mp hτ'
    exact ⟨τ, hτ, (OrdIso_map_rank (fun _ h => hτ.subset h)).trans hiso⟩
  · rintro ⟨τ, hτ, hiso⟩
    exact ⟨τ.map (rank σ), hτ.map _, (OrdIso_map_rank (fun _ h => hτ.subset h)).symm.trans hiso⟩

/-- Standardising a subsequence of a `π`-avoiding sequence gives a `π`-avoiding sequence. -/
theorem not_contains_ranks_of_sublist {σ τ π : List ℕ} (h : τ.Sublist σ) (hσ : ¬ Contains σ π) :
    ¬ Contains (ranks τ) π := by
  rw [contains_ranks_iff]
  exact not_contains_of_sublist h hσ

/-- The position block of length `m` starting at position `a` (0-indexed). -/
def block (σ : List ℕ) (a m : ℕ) : List ℕ := (σ.drop a).take m

theorem block_sublist (σ : List ℕ) (a m : ℕ) : (block σ a m).Sublist σ :=
  (List.take_sublist _ _).trans (List.drop_sublist _ _)

theorem length_block (σ : List ℕ) (a m : ℕ) (h : a + m ≤ σ.length) :
    (block σ a m).length = m := by
  simp [block]; omega

/-- The standardisation of a position block. -/
def blockStd (σ : List ℕ) (a m : ℕ) : List ℕ := ranks (block σ a m)

/-- **Block splitting, deterministic core**: if `σ` avoids `π` then so does the standardisation of
every position block of `σ`. -/
theorem blockStd_avoids {σ π : List ℕ} (hσ : ¬ Contains σ π) (a m : ℕ) :
    ¬ Contains (blockStd σ a m) π :=
  not_contains_ranks_of_sublist (block_sublist σ a m) hσ

/-- Contrapositive form used in the union bound: `π ⊆ σ` as soon as `π` is contained in
one block standardisation. -/
theorem contains_of_blockStd {σ π : List ℕ} {a m : ℕ} (h : Contains (blockStd σ a m) π) :
    Contains σ π :=
  ((contains_ranks_iff _ _).mp h).of_sublist (block_sublist σ a m)

/-! ### Standardisation of a duplicate-free list is a permutation of `range` -/

theorem rank_lt_length {l : List ℕ} {x : ℕ} (hx : x ∈ l) : rank l x < l.length := by
  unfold rank
  have h1 := List.length_eq_countP_add_countP (fun y => decide (y < x)) (l := l)
  have h2 : 0 < l.countP (fun y => decide ¬ (decide (y < x)) = true) := by
    rw [List.countP_pos_iff]
    exact ⟨x, hx, by simp⟩
  omega

theorem ranks_nodup {l : List ℕ} (hl : l.Nodup) : (ranks l).Nodup := by
  unfold ranks
  refine List.Nodup.map_on ?_ hl
  intro x hx y hy hxy
  by_contra hne
  rcases Nat.lt_or_gt_of_ne hne with h | h
  · exact absurd hxy (rank_lt_rank l hx h).ne
  · exact absurd hxy.symm (rank_lt_rank l hy h).ne

/-- The standardisation of a duplicate-free list of length `m` is a permutation of `range m`. -/
theorem ranks_perm_range {l : List ℕ} (hl : l.Nodup) : (ranks l).Perm (List.range l.length) := by
  have hnd := ranks_nodup hl
  have hsub : ∀ x ∈ ranks l, x ∈ List.range l.length := by
    intro x hx
    obtain ⟨y, hy, rfl⟩ := List.mem_map.mp hx
    exact List.mem_range.mpr (rank_lt_length hy)
  have hcard : (ranks l).toFinset = (List.range l.length).toFinset := by
    apply Finset.eq_of_subset_of_card_le
    · intro x hx
      exact List.mem_toFinset.mpr (hsub x (List.mem_toFinset.mp hx))
    · rw [List.toFinset_card_of_nodup hnd, List.toFinset_card_of_nodup List.nodup_range]
      simp
  exact List.perm_of_nodup_nodup_toFinset_eq hnd List.nodup_range hcard

end Superpatterns
