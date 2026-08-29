import Mathlib

/-!
# Permutation patterns: basic definitions

* `OrdIso l m` : two lists of naturals of equal length are order-isomorphic
  (`l[i] < l[j] ↔ m[i] < m[j]` for all positions `i j`).
* `Contains σ π` : `σ` contains the pattern `π`, i.e. some sublist (subsequence)
  of `σ` is order-isomorphic to `π`.
* `IsSuperpattern k σ` : `σ` contains every permutation of `{0,…,k-1}` (as a list).
* `ranks l` : the rank vector of a list (the "standardisation"); two lists with equal
  rank vectors are order-isomorphic (`OrdIso_of_ranks_eq`).  This is the bridge used by the
  certificate checker in `Checker.lean`.
-/

namespace Superpatterns

/-- Two lists are order-isomorphic: same length and the same relative order at every
pair of positions. -/
def OrdIso (l m : List ℕ) : Prop :=
  ∃ h : l.length = m.length,
    ∀ i j (hi : i < l.length) (hj : j < l.length),
      (l[i] < l[j] ↔ m[i]'(h ▸ hi) < m[j]'(h ▸ hj))

/-- `σ` contains the (classical) pattern `π`: some subsequence of `σ` is order-isomorphic
to `π`. -/
def Contains (σ π : List ℕ) : Prop :=
  ∃ τ : List ℕ, τ.Sublist σ ∧ OrdIso τ π

/-- `σ` is a `k`-superpattern: it contains every permutation of `{0,…,k-1}`. -/
def IsSuperpattern (k : ℕ) (σ : List ℕ) : Prop :=
  ∀ π : List ℕ, π.Perm (List.range k) → Contains σ π

/-- Rank of a value inside a list: the number of entries strictly below it. -/
def rank (l : List ℕ) (x : ℕ) : ℕ := l.countP (fun y => decide (y < x))

/-- The rank vector (standardisation) of a list. -/
def ranks (l : List ℕ) : List ℕ := l.map (rank l)

@[simp] theorem length_ranks (l : List ℕ) : (ranks l).length = l.length := by
  simp [ranks]

theorem getElem_ranks (l : List ℕ) (i : ℕ) (hi : i < l.length) :
    (ranks l)[i]'(by simpa using hi) = rank l l[i] := by
  simp [ranks]

/-- Monotonicity of ranks. -/
theorem rank_mono (l : List ℕ) {a b : ℕ} (hab : a ≤ b) : rank l a ≤ rank l b := by
  unfold rank
  apply List.countP_mono_left
  intro x _ hx
  simp only [decide_eq_true_eq] at hx ⊢
  omega

/-- Strict monotonicity of ranks at members of the list. -/
theorem rank_lt_rank (l : List ℕ) {a b : ℕ} (ha : a ∈ l) (hab : a < b) :
    rank l a < rank l b := by
  unfold rank
  induction l with
  | nil => simp at ha
  | cons x xs ih =>
    rw [List.mem_cons] at ha
    simp only [List.countP_cons]
    rcases ha with rfl | ha
    · have h1 : rank xs a ≤ rank xs b := rank_mono xs hab.le
      unfold rank at h1
      have : ¬ (a < a) := lt_irrefl a
      simp [this, hab]
      omega
    · have := ih ha
      have h2 : (if decide (x < a) = true then 1 else 0) ≤ (if decide (x < b) = true then 1 else 0) := by
        split_ifs <;> simp_all <;> omega
      omega

/-- The key fact: the order between a member `a` of `l` and any `b` is determined by ranks. -/
theorem lt_iff_rank_lt (l : List ℕ) {a b : ℕ} (ha : a ∈ l) :
    a < b ↔ rank l a < rank l b := by
  constructor
  · exact rank_lt_rank l ha
  · intro h
    by_contra hba
    push_neg at hba
    have := rank_mono l hba
    omega

/-- Equal rank vectors imply order-isomorphism. -/
theorem OrdIso_of_ranks_eq {l m : List ℕ} (h : ranks l = ranks m) : OrdIso l m := by
  have hlen : l.length = m.length := by
    have := congrArg List.length h
    simpa using this
  refine ⟨hlen, ?_⟩
  intro i j hi hj
  have hi' : i < m.length := hlen ▸ hi
  have hj' : j < m.length := hlen ▸ hj
  have e1 : rank l l[i] = rank m m[i] := by
    have := congrArg (fun r : List ℕ => r[i]?) h
    simp only [ranks, List.getElem?_map] at this
    simp [List.getElem?_eq_getElem hi, List.getElem?_eq_getElem hi'] at this
    exact this
  have e2 : rank l l[j] = rank m m[j] := by
    have := congrArg (fun r : List ℕ => r[j]?) h
    simp only [ranks, List.getElem?_map] at this
    simp [List.getElem?_eq_getElem hj, List.getElem?_eq_getElem hj'] at this
    exact this
  rw [lt_iff_rank_lt l (List.getElem_mem hi), lt_iff_rank_lt m (List.getElem_mem hi'), e1, e2]

end Superpatterns
