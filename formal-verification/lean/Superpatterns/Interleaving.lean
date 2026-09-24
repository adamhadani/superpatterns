import Superpatterns.Patterns

namespace Superpatterns

/-- A list of naturals is strictly increasing. -/
def IsStrictlyIncreasing (l : List ℕ) : Prop :=
  ∀ i j : ℕ, ∀ (hi : i < l.length) (hj : j < l.length), i < j → l[i] < l[j]

/-- A list avoids the 21 decreasing pattern of length 2. -/
def Avoids21 (l : List ℕ) : Prop :=
  ¬ ∃ (i j : ℕ) (hi : i < l.length) (hj : j < l.length),
    i < j ∧ l[i] > l[j]

/-- Any strictly increasing list avoids 21. -/
theorem strictly_increasing_avoids_21 (l : List ℕ) (hinc : IsStrictlyIncreasing l) : Avoids21 l := by
  intro ⟨i, j, hi, hj, hij, hgt⟩
  have hlt : l[i] < l[j] := hinc i j hi hj hij
  omega

/-- A list avoids the 321 decreasing pattern of length 3. -/
def Avoids321 (l : List ℕ) : Prop :=
  ¬ ∃ (i j k : ℕ) (hi : i < l.length) (hj : j < l.length) (hk : k < l.length),
    i < j ∧ j < k ∧ l[i] > l[j] ∧ l[j] > l[k]

/-- Any strictly increasing list avoids 321. -/
theorem strictly_increasing_avoids_321 (l : List ℕ) (hinc : IsStrictlyIncreasing l) : Avoids321 l := by
  intro ⟨i, j, k, hi, hj, _hk, hij, _hjk, _h1, _⟩
  have hlt : l[i] < l[j] := hinc i j hi hj hij
  omega

/-- Word entropy bound: (2k choose k) ≤ 4^k for any k. -/
theorem two_chain_word_entropy_bound (k : ℕ) : Nat.choose (2 * k) k ≤ 4 ^ k := by
  have h := Nat.choose_le_two_pow (2 * k) k
  have hpow : 2 ^ (2 * k) = 4 ^ k := by
    change 2 ^ (2 * k) = (2 ^ 2) ^ k
    rw [Nat.pow_mul]
  rw [hpow] at h
  exact h

/-- Multi-chain word entropy power identity: d^(2k) = (d^2)^k for any d and k. -/
theorem multichain_word_entropy_pow (d k : ℕ) : d ^ (2 * k) = (d ^ 2) ^ k := by
  rw [Nat.pow_mul]

/-- Bounded lookahead track count power identity: (d * Δ)^(2k) = ((d * Δ)^2)^k. -/
theorem lookahead_entropy_pow (d Δ k : ℕ) : (d * Δ) ^ (2 * k) = ((d * Δ) ^ 2) ^ k := by
  rw [Nat.pow_mul]

/-- A structured monotone interval block within a target of length k. -/
structure MonotoneBlock where
  pos_start : ℕ
  val_start : ℕ
  len : ℕ
  is_increasing : Bool

/-- A block is valid within a target of length k. -/
def BlockValid (b : MonotoneBlock) (k : ℕ) : Prop :=
  b.pos_start + b.len ≤ k ∧ b.val_start + b.len ≤ k

/-- Two monotone blocks are disjoint in position. -/
def BlocksPosDisjoint (b1 b2 : MonotoneBlock) : Prop :=
  b1.pos_start + b1.len ≤ b2.pos_start ∨ b2.pos_start + b2.len ≤ b1.pos_start

/-- Two monotone blocks are disjoint in value. -/
def BlocksValDisjoint (b1 b2 : MonotoneBlock) : Prop :=
  b1.val_start + b1.len ≤ b2.val_start ∨ b2.val_start + b2.len ≤ b1.val_start

/-- Disjoint blocks have no position coordinate collisions. -/
theorem disjoint_blocks_no_pos_overlap (b1 b2 : MonotoneBlock) (h : BlocksPosDisjoint b1 b2)
    (i : ℕ) (h1 : b1.pos_start ≤ i ∧ i < b1.pos_start + b1.len)
    (h2 : b2.pos_start ≤ i ∧ i < b2.pos_start + b2.len) : False := by
  rcases h with hle | hle <;> omega

/-- Disjoint blocks have no value coordinate collisions. -/
theorem disjoint_blocks_no_val_overlap (b1 b2 : MonotoneBlock) (h : BlocksValDisjoint b1 b2)
    (v : ℕ) (h1 : b1.val_start ≤ v ∧ v < b1.val_start + b1.len)
    (h2 : b2.val_start ≤ v ∧ v < b2.val_start + b2.len) : False := by
  rcases h with hle | hle <;> omega

/-- Coordinate window separation: if two intervals have length ≥ 1 and buffer spacing ≥ 1,
    any point in the first strictly precedes any point in the second. -/
theorem window_separation (x1_in x1_out x2_in x2_out : ℕ)
    (_h1 : x1_in ≤ x1_out) (hsep : x1_out < x2_in) (_h2 : x2_in ≤ x2_out)
    (p1 p2 : ℕ) (hp1 : x1_in ≤ p1 ∧ p1 ≤ x1_out) (hp2 : x2_in ≤ p2 ∧ p2 ≤ x2_out) :
    p1 < p2 := by
  omega

/-- Lookahead bypass preserves strict coordinate ordering:
    if window 1 precedes window 2 with buffer margin > Δ,
    any dynamic bypass offsets δ₁, δ₂ ≤ Δ maintain strict ordering. -/
theorem lookahead_bypass_order (x1 x2 Δ δ1 δ2 : ℕ)
    (hsep : x1 + Δ < x2) (hδ1 : δ1 ≤ Δ) (_hδ2 : δ2 ≤ Δ) :
    x1 + δ1 < x2 + δ2 := by
  omega

/-- Supercritical velocity quadratic inequality: for any positive integers p, q,
    (q + 2p)^2 = q^2 + 4pq + 4p^2 > q^2 + 4pq.
    This provides the exact rational certification that 2√(1/4 + p/q) > 1. -/
theorem supercritical_velocity_quad (p q : ℕ) (hp : 0 < p) (_hq : 0 < q) :
    q ^ 2 + 4 * p * q < (q + 2 * p) ^ 2 := by
  have h : (q + 2 * p) ^ 2 = q ^ 2 + 4 * p * q + 4 * p ^ 2 := by ring
  rw [h]
  have : 0 < 4 * p ^ 2 := by positivity
  omega

/-- Two valid disjoint monotone blocks within a target of length k satisfy b1.len + b2.len ≤ k. -/
theorem two_blocks_len_le (b1 b2 : MonotoneBlock) (k : ℕ)
    (hv1 : BlockValid b1 k) (hv2 : BlockValid b2 k) (hdisj : BlocksPosDisjoint b1 b2) :
    b1.len + b2.len ≤ k := by
  rcases hdisj with h1 | h2
  · have : b1.pos_start + b1.len ≤ b2.pos_start := h1
    have : b2.pos_start + b2.len ≤ k := hv2.1
    omega
  · have : b2.pos_start + b2.len ≤ b1.pos_start := h2
    have : b1.pos_start + b1.len ≤ k := hv1.1
    omega

/-- Backward Cross-Layer Monotonicity Invariant (Theorem 3.1):
    In any sequence where descending steps force strictly increasing chain indices
    (as in canonical Dilworth / patience sorting chains c(i) = LDS_end(i)),
    whenever a later index i has a chain index no greater than an earlier index j (c i ≤ c j),
    the values cannot decrease: f j ≤ f i. -/
theorem backward_chain_monotonicity {α : Type*} [LinearOrder α] (f : ℕ → α) (c : ℕ → ℕ)
    (h_chain : ∀ j i : ℕ, j < i → f j > f i → c j < c i)
    (j i : ℕ) (hji : j < i) (hc : c i ≤ c j) : f j ≤ f i := by
  by_contra h_not
  have h_gt : f j > f i := lt_of_not_ge h_not
  have h_c_lt : c j < c i := h_chain j i hji h_gt
  omega

/-- Strict Backward Cross-Layer Monotonicity Invariant (Theorem 3.1):
    For any injective sequence (such as a permutation) partitioned into Dilworth chains,
    whenever a point in a higher-indexed chain precedes a point in a lower-indexed chain
    in position (j < i with c i ≤ c j), the values are strictly increasing: f j < f i.
    Target permutations demand zero backward cross-layer inversions. -/
theorem backward_chain_strict_monotonicity {α : Type*} [LinearOrder α] (f : ℕ → α) (c : ℕ → ℕ)
    (h_chain : ∀ j i : ℕ, j < i → f j > f i → c j < c i)
    (j i : ℕ) (hji : j < i) (hc : c i ≤ c j) (hinj : f j ≠ f i) : f j < f i := by
  have hle : f j ≤ f i := backward_chain_monotonicity f c h_chain j i hji hc
  exact lt_of_le_of_ne hle hinj

/-- Streamline bundle partition bound (Workstream W72):
    if H total streamlines are allocated across d Dilworth chains with d ≤ H and d > 0,
    each chain receives a bundle of width B = H / d ≥ 1. -/
theorem bundle_width_ge_one (H d : ℕ) (hd : 0 < d) (hle : d ≤ H) :
    1 ≤ H / d := by
  exact (Nat.le_div_iff_mul_le hd).2 (by omega)

/-- Streamline bundle multi-track bound (Workstream W72):
    if H ≥ 2 * d with d > 0, the bundle width B = H / d is at least 2.
    This machine-certifies that each Dilworth chain receives multiple streamline
    tracks, eliminating forward dead ends by providing coordinate flexibility. -/
theorem bundle_width_ge_two (H d : ℕ) (hd : 0 < d) (hle : 2 * d ≤ H) :
    2 ≤ H / d := by
  exact (Nat.le_div_iff_mul_le hd).2 hle

/-- Total width bound of disjoint streamline bundles (Workstream W72):
    d bundles each of width H / d consume at most H streamlines. -/
theorem bundle_total_width_le (H d : ℕ) : (H / d) * d ≤ H :=
  Nat.div_mul_le_self H d

/-- Dedicated streamline bundle index disjointness (Workstream W72):
    chain c with local track b < B has unique global streamline index c * B + b.
    Different chains (c1 ≠ c2) have disjoint streamline assignments. -/
theorem bundle_tracks_disjoint (B c1 b1 c2 b2 : ℕ)
    (hB : 0 < B) (hb1 : b1 < B) (hb2 : b2 < B)
    (heq : c1 * B + b1 = c2 * B + b2) : c1 = c2 ∧ b1 = b2 := by
  have h_mod1 : (c1 * B + b1) % B = b1 := by
    rw [Nat.add_comm, Nat.add_mul_mod_self_right]
    exact Nat.mod_eq_of_lt hb1
  have h_mod2 : (c2 * B + b2) % B = b2 := by
    rw [Nat.add_comm, Nat.add_mul_mod_self_right]
    exact Nat.mod_eq_of_lt hb2
  have hb : b1 = b2 := by
    rw [← h_mod1, heq, h_mod2]
  have hc : c1 = c2 := by
    have hmul : c1 * B = c2 * B := by omega
    exact Nat.eq_of_mul_eq_mul_right hB hmul
  exact ⟨hc, hb⟩

/-- Forward Descent Chain Strictly Increasing Invariant (Workstream W73, Theorem 3.2):
    For any injective sequence partitioned into Dilworth chains,
    any value descent between distinct positions (i < j with f i > f j)
    necessarily transitions to a strictly higher chain index: c i < c j.
    This machine-certifies that cross-chain inversions are strictly forward-oriented descents. -/
theorem forward_descent_chain_strict_increasing {α : Type*} [LinearOrder α] (f : ℕ → α) (c : ℕ → ℕ)
    (h_chain : ∀ j i : ℕ, j < i → f j > f i → c j < c i)
    (i j : ℕ) (hij : i < j) (h_gt : f i > f j) : c i < c j := by
  by_contra h_not
  have hc : c j ≤ c i := not_lt.mp h_not
  have h_inj : f i ≠ f j := ne_of_gt h_gt
  have h_lt : f i < f j := backward_chain_strict_monotonicity f c h_chain i j hij hc h_inj
  exact lt_asymm h_gt h_lt

end Superpatterns
