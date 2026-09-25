import Mathlib
import Superpatterns.Patterns
import Superpatterns.ErdosSzekeres

open Finset

namespace Superpatterns

/-- A chain is an increasing subsequence. -/
def IsChain (σ : List ℕ) (indices : Finset (Fin σ.length)) : Prop :=
  ∀ i ∈ indices, ∀ j ∈ indices, i < j → σ[i] < σ[j]

/-- A list of disjoint chains. -/
def DisjointChains (σ : List ℕ) (chains : List (Finset (Fin σ.length))) : Prop :=
  (∀ c ∈ chains, IsChain σ c) ∧
  (∀ i j (hi : i < chains.length) (hj : j < chains.length), i ≠ j → Disjoint (chains[i]'hi) (chains[j]'hj))

/-- Union of a list of chains. -/
def chainUnion {σ : List ℕ} (chains : List (Finset (Fin σ.length))) : Finset (Fin σ.length) :=
  chains.foldl (· ∪ ·) ∅

def Is_m_ChainUnion (σ : List ℕ) (m : ℕ) (u : Finset (Fin σ.length)) : Prop :=
  ∃ chains : List (Finset (Fin σ.length)), chains.length ≤ m ∧ DisjointChains σ chains ∧ chainUnion chains = u

noncomputable def c_m (σ : List ℕ) (m : ℕ) : ℕ :=
  sSup {k | ∃ u : Finset (Fin σ.length), Is_m_ChainUnion σ m u ∧ u.card = k}

noncomputable def LIS (σ : List ℕ) : ℕ :=
  sSup {k | ∃ c : Finset (Fin σ.length), IsChain σ c ∧ c.card = k}

def IsAntichain (σ : List ℕ) (indices : Finset (Fin σ.length)) : Prop :=
  ∀ i ∈ indices, ∀ j ∈ indices, i < j → σ[i] > σ[j]

noncomputable def LDS (σ : List ℕ) : ℕ :=
  sSup {k | ∃ c : Finset (Fin σ.length), IsAntichain σ c ∧ c.card = k}

axiom c_1_eq_LIS (σ : List ℕ) : c_m σ 1 = LIS σ

axiom c_m_le_c_m_add_one (σ : List ℕ) (m : ℕ) : c_m σ m ≤ c_m σ (m + 1)
axiom c_m_le_card (σ : List ℕ) (m : ℕ) : c_m σ m ≤ σ.length

axiom c_m_eq_card_of_ge_LDS (σ : List ℕ) (m : ℕ) : LDS σ ≤ m → c_m σ m = σ.length

noncomputable def greene_lambda (σ : List ℕ) (i : ℕ) : ℕ :=
  if i = 0 then 0 else c_m σ i - c_m σ (i - 1)

axiom greene_capacity_bound (σ : List ℕ) (chains : List (Finset (Fin σ.length))) (h : DisjointChains σ chains) :
  (chainUnion chains).card ≤ ∑ i ∈ Finset.range (chains.length + 1), greene_lambda σ i

axiom greene_capacity_optimal (σ : List ℕ) (m : ℕ) :
  ∃ chains : List (Finset (Fin σ.length)), chains.length = m ∧ DisjointChains σ chains ∧
  (chainUnion chains).card = ∑ i ∈ Finset.range (m + 1), greene_lambda σ i

/-
NOTE ON DEMAND REALIZABILITY:
A candidate proposition asserting that ANY demand profile satisfying `demand a ≤ greene_lambda σ a`
can be realized simultaneously by disjoint chains of lengths at least `demand a` is
MATHEMATICALLY FALSE in general.

Minimal Counterexample in S_6:
Consider σ = [1, 2, 5, 0, 3, 4] ∈ S_6.
- The longest increasing subsequence has length 4 (unique chain: [1, 2, 3, 4]). Thus c_1 = 4, λ_1 = 4.
- The maximum cardinality of a union of 2 disjoint chains is 6 = |σ| (e.g. [1, 2, 5] and [0, 3, 4]). Thus c_2 = 6, λ_2 = 2.
- The Greene shape is λ = (4, 2).
- Consider demand = (4, 2), which satisfies demand 1 ≤ λ_1 (4 ≤ 4) and demand 2 ≤ λ_2 (2 ≤ 2).
- To realize this demand, σ would need two disjoint chains of lengths 4 and 2.
- Any chain of length 4 must use [1, 2, 3, 4]. The remaining elements are {5, 0}.
- The set {5, 0} has position/value order (2:5, 3:0), which forms a descending pair and contains no increasing chain of length 2.
- Hence no two disjoint chains of lengths 4 and 2 exist in σ.

Therefore, `multichain_demand_realizability` is false and has been retracted.
Greene's theorem establishes cumulative capacity bounds (`greene_capacity_bound` and `greene_capacity_optimal`),
namely that max ∑ |C_i| = ∑ λ_i, which is sound.
-/

end Superpatterns
