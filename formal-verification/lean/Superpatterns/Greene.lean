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

axiom multichain_demand_realizability (σ : List ℕ) (d : ℕ) (demand : ℕ → ℕ)
  (h_cap : ∀ a, 1 ≤ a ∧ a ≤ d → demand a ≤ greene_lambda σ a) :
  ∃ chains : List (Finset (Fin σ.length)), ∃ hd : chains.length = d, DisjointChains σ chains ∧
  ∀ a (ha : 1 ≤ a ∧ a ≤ d), demand a ≤ (chains[a - 1]'(by omega)).card

end Superpatterns
