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
    (h1 : x1_in ≤ x1_out) (hsep : x1_out < x2_in) (h2 : x2_in ≤ x2_out)
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

end Superpatterns
