# W35 — Lean formalisation: witness reduction, block splitting, Erdős–Szekeres

Lean 4 + Mathlib v4.33.1, project `formal-verification/lean/`. Three new modules, all added to the
library root (`Superpatterns.lean`) and to the axiom audit (`Superpatterns/Axioms.lean`), so
`lake build` compiles and audits them. **No `sorry` anywhere; every new theorem depends only on
`propext`, `Classical.choice`, `Quot.sound`** (no `native_decide`, no new axioms).

## 1. `Superpatterns/Witness.lean` — Prop. 15 / W28 Thm 1.1 (all parts)

Formalisation choice: a finite probability space is `FinProb Ω` = `Fintype Ω` with weights
`p : Ω → ℝ`, `p ≥ 0`, `∑ p = 1`; `E f = ∑ p·f`, `Pr B = E 1_B`, `Eon f B = E[f ; B]`. Conditional
expectations are stated division-free as `E[M ; B] ≤ c · Pr B`, plus a divided form `condE` with
`max_w` (`Finset.sup'`). Events `A π` indexed by a `Fintype ι`; `cnt A ω = ∑_π 1_{A π}(ω) = M(ω)`.

| statement | Lean name |
|---|---|
| μ = E[M ; M>0] | `FinProb.mean_eq_E_on_pos` |
| Pr(M>0) ≤ μ (R ≥ 1) | `FinProb.Pr_pos_le_mean` |
| Pr(M>0) ≤ 1 (R ≥ μ) | `FinProb.Pr_le_one` |
| μ = Σ_π Pr(A_π) | `FinProb.mean_eq_sum_Pr` |
| μ² ≤ E[M²]·Pr(M>0) (Cauchy–Schwarz / Paley–Zygmund at 0) | `FinProb.sq_mean_le` |
| E[M²] = Σ_π E[M ; A_π] | `FinProb.E_sq_eq_sum` |
| (∀π, E[M;A_π] ≤ Λ Pr(A_π)) ⇒ μ ≤ Λ·Pr(M>0)  (R ≤ max_π Λ_π) | `FinProb.mean_le_max_cond` |
| (c) witness form, division-free: (∀w, E[M;W=w,M>0] ≤ c Pr(W=w,M>0)) ⇒ μ ≤ c·Pr(M>0) | `FinProb.witness_reduction` |
| (c) μ ≤ (max_w E[M \| W=w, M>0])·Pr(M>0) | `FinProb.witness_reduction_max` |
| uniform model on S_n, A_π = {π ⊄ σ}: M>0 ⇔ σ not a k-superpattern; (c) instantiated | `cnt_missing_pos_iff`, `witness_reduction_uniform` (`Perms n`, `FinProb.uniform`, `missing`) |

## 2. `Superpatterns/BlockSplit.lean` — W27 Lemma 0.2, combinatorial core

* `OrdIso.refl/symm/trans`; `Contains.of_sublist` (containment monotone in the host);
  `not_contains_of_sublist` (avoidance hereditary under subsequences).
* `contains_ranks_iff`: standardisation (`ranks`) preserves the set of contained patterns.
* `block σ a m` = positions `a..a+m-1`; `blockStd σ a m = ranks (block σ a m)`;
  **`blockStd_avoids`: σ avoids π ⇒ every block standardisation avoids π**; `contains_of_blockStd`.
* `ranks_perm_range`: the standardisation of a duplicate-free list of length m is a permutation of
  `range m` (so block standardisations of σ ∈ S_N lie in S_m).

**Not done (honestly):** the probabilistic half `p_π(N) ≤ p_π(M)^{⌊N/M⌋}`. It needs that the
⌊N/M⌋ block standardisations of a uniform σ ∈ S_N are i.i.d. uniform on S_M, i.e. that the map
σ ↦ (blockStd σ (iM) M)_i has equal fibres. The clean route is the free action of (S_M)^q on S_N by
permuting positions inside blocks (it acts on the tuple of standardisations by right
multiplication, transitively and freely) — position-permutations of lists, `ranks ∘ reindex`,
and an orbit-counting argument; estimated 300+ lines of new Lean, beyond the 2-hour budget. Left out
rather than left as a `sorry`.

## 3. `Superpatterns/ErdosSzekeres.lean` — W28 Thm 2.1

Reuses Mathlib's `Theorems100.erdos_szekeres` from `Archive/Wiedijk100Theorems/AscendingDescendingSequences.lean`
(`Archive` is a declared `lean_lib` of the Mathlib package; importing it from this project works and
Lake builds the one module from the cached Mathlib oleans, ~5 s).
* `ofFn_sublist`: indexing along an order embedding gives a subsequence.
* `OrdIso_range_of_strictMono`, `OrdIso_range_reverse_of_strictAnti`: strictly monotone lists are
  order-isomorphic to `12⋯a` = `List.range a` resp. `b⋯21` = `(List.range b).reverse`.
* **`erdos_szekeres_contains`**: σ duplicate-free, (a−1)(b−1) < |σ| ⇒ `Contains σ (range a) ∨ Contains σ (range b).reverse`.
* `not_avoid_both` (disjointness of the two missing events), `not_avoid_id_rev` (a = b = k).

## Verification

```
cd formal-verification/lean
lake build                          # 8719 jobs, ~15 s wall with everything cached; new files ~5 s each
lake env lean Superpatterns/Axioms.lean
grep -n sorry Superpatterns/Witness.lean Superpatterns/BlockSplit.lean Superpatterns/ErdosSzekeres.lean  # none
```
Axiom audit output for the 12 new theorems: `[propext, Classical.choice, Quot.sound]` (see `log.md`).
