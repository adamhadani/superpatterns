import Superpatterns.Patterns

/-!
# A verified superpattern checker

`checker k σ` enumerates all `k`-element subsequences of `σ` by depth-first search, computes the
rank vector (`ranks`) of each and stores it in an array indexed by a base-`k` encoding of the
rank vector.  Finally it checks that for every permutation `π` of `{0,…,k-1}` the slot indexed by
`ranks π` holds exactly `ranks π`.

The soundness theorem `checker_sound : checker k σ = true → IsSuperpattern k σ` only needs the
invariant that *every stored rank vector is the rank vector of a genuine subsequence of `σ`*;
the indexing function plays no role in soundness (it only matters for the checker to succeed),
so no injectivity argument about the encoding is required.
-/

namespace Superpatterns

/-- The store: slot `i` holds `some r` if a subsequence with rank vector `r` has been found
and filed under index `i`. -/
abbrev Store := Array (Option (List ℕ))

/-- Base-`k` encoding of a rank vector. -/
def index (k : ℕ) (r : List ℕ) : ℕ := r.foldl (fun acc d => acc * k + d) 0

/-- File the rank vector of a subsequence `τ`. -/
def mark (k : ℕ) (st : Store) (τ : List ℕ) : Store :=
  let r := ranks τ
  let i := index k r
  if h : i < st.size then st.set i (some r) h else st

/-- Depth-first enumeration of all `need`-element subsequences of `xs` (whose length is `rem`),
with the already chosen prefix `chosen` kept in reverse order. -/
def dfs (k : ℕ) : List ℕ → ℕ → List ℕ → ℕ → Store → Store
  | _, _, chosen, 0, st => mark k st chosen.reverse
  | [], _, _, _ + 1, st => st
  | x :: xs, rem, chosen, need + 1, st =>
    let st1 := if need ≤ rem - 1 then dfs k xs (rem - 1) (x :: chosen) need st else st
    if need + 1 ≤ rem - 1 then dfs k xs (rem - 1) chosen (need + 1) st1 else st1

/-- The checker. -/
def checker (k : ℕ) (σ : List ℕ) : Bool :=
  let st := dfs k σ σ.length [] k (Array.replicate (k ^ k) none)
  (List.range k).permutations'.all fun π =>
    let r := ranks π
    decide (st.getD (index k r) none = some r)

/-- Invariant: every stored rank vector comes from a genuine subsequence of `σ`. -/
def Good (σ : List ℕ) (st : Store) : Prop :=
  ∀ i r, st.getD i none = some r → ∃ τ : List ℕ, τ.Sublist σ ∧ ranks τ = r

theorem good_replicate (σ : List ℕ) (n : ℕ) : Good σ (Array.replicate n none) := by
  intro i r hr
  rw [Array.getD_eq_getD_getElem?, Array.getElem?_replicate] at hr
  split at hr <;> simp at hr

theorem good_mark {σ : List ℕ} {st : Store} (k : ℕ) (hst : Good σ st) {τ : List ℕ}
    (hτ : τ.Sublist σ) : Good σ (mark k st τ) := by
  intro i r hr
  unfold mark at hr
  simp only at hr
  split at hr
  · rw [Array.getD_eq_getD_getElem?, Array.getElem?_set] at hr
    split at hr
    · exact ⟨τ, hτ, by simpa using hr⟩
    · exact hst i r (by rw [Array.getD_eq_getD_getElem?]; exact hr)
  · exact hst i r hr

theorem good_dfs {σ : List ℕ} (k : ℕ) :
    ∀ (xs : List ℕ) (rem : ℕ) (chosen : List ℕ) (need : ℕ) (st : Store),
      Good σ st → (∀ τ : List ℕ, τ.Sublist xs → (chosen.reverse ++ τ).Sublist σ) →
      Good σ (dfs k xs rem chosen need st) := by
  intro xs
  induction xs with
  | nil =>
    intro rem chosen need st hst hch
    cases need with
    | zero =>
      simp only [dfs]
      exact good_mark k hst (by simpa using hch [] (List.Sublist.refl _))
    | succ n => simpa [dfs] using hst
  | cons x xs ih =>
    intro rem chosen need st hst hch
    cases need with
    | zero =>
      simp only [dfs]
      exact good_mark k hst (by simpa using hch [] (List.nil_sublist _))
    | succ n =>
      simp only [dfs]
      have h1 : Good σ (if n ≤ rem - 1 then dfs k xs (rem - 1) (x :: chosen) n st else st) := by
        split
        · apply ih
          · exact hst
          · intro τ hτ
            have := hch (x :: τ) (hτ.cons_cons x)
            simpa using this
        · exact hst
      split
      · apply ih
        · exact h1
        · intro τ hτ
          exact hch τ (hτ.cons x)
      · exact h1

/-- **Soundness of the checker.** -/
theorem checker_sound {k : ℕ} {σ : List ℕ} (h : checker k σ = true) : IsSuperpattern k σ := by
  intro π hπ
  have hmem : π ∈ (List.range k).permutations' := List.mem_permutations'.2 hπ
  unfold checker at h
  simp only [List.all_eq_true, decide_eq_true_eq] at h
  have hst := h π hmem
  have hg : Good σ (dfs k σ σ.length [] k (Array.replicate (k ^ k) none)) :=
    good_dfs k σ σ.length [] k _ (good_replicate σ _) (fun τ hτ => by simpa using hτ)
  obtain ⟨τ, hτ, hr⟩ := hg _ _ hst
  exact ⟨τ, hτ, OrdIso_of_ranks_eq hr⟩

end Superpatterns
