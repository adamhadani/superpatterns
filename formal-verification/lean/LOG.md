# Lean formalisation log — superpatterns

Date: 2026-08-29.  Machine: macOS (Darwin 25.6), 12 cores, 64 GB.

## Toolchain / versions

* elan 4.2.4; Lean `leanprover/lean4:v4.33.1` (downloaded on first `lake update`).
* Mathlib tag `v4.33.1` (`lakefile.toml`: `rev = "v4.33.1"`), prebuilt oleans via `lake exe cache get`
  (8690 files; `lake update` incl. toolchain download 3 min 12 s, cache download+decompress ~1 min).
* Project: `formal-verification/lean/`, library `Superpatterns`, root module imports all files.

## Files

| file | content | status |
|---|---|---|
| `Superpatterns/Patterns.lean` | `OrdIso`, `Contains`, `IsSuperpattern`, `rank`/`ranks`, `OrdIso_of_ranks_eq` | proved, no sorry |
| `Superpatterns/Checker.lean` | DFS checker over `Array (Option (List ℕ))`, invariant `Good`, `checker_sound` | proved, no sorry |
| `Superpatterns/Certificates.lean` | σ7 (n=23), σ8 (n=32), σ8' (n=31), σ8'' (n=30) via `native_decide`; k=3, k=4 sanity by kernel `decide` | see D1 below |
| `Superpatterns/Encoding.lean` | abstract Lemma 1 (`card_le_sum_fiber`, `sum_image_eq_sum_div_card`, `card_fiber_le_of_injective`); concrete definitions (`Subsets`, `pos`, `posGet`, `patOf`, `patCount`, `width`, `gaps`, `W`, `offData`); position lemmas; `card_patterns_over_le` (CKS injectivity), `fiber_card_ge` (extension counting), `lemma1_concrete`; Step 2: `evenRule` (subset / non-adjacent / stable, proved), `step2_pointwise`, `patCount_le_sum_W` | proved, no sorry (since 2026-08-29, see below) |
| `Superpatterns/Tilt.lean` | `wt` (= f), `pair_sum_le` (Step 4, finite), `single_sum_le`, `Comp`/`compSum`/`Wcomp`/`box`, `tilt_bound` (Step 3) | proved, no sorry |
| `Superpatterns/TheoremA.lean` | `compSum_gaps`, `gaps_mem_box`, `gaps_injOn`, `theoremA` | proved, no sorry |
| `Superpatterns/Numeric.lean` | `constant_certificate`: λθ/e² − log θ + 1 + ½ log(1−e^{−θ}) < 0 at θ=7.37, λ=1.0003 | proved, no sorry |
| `Superpatterns/Axioms.lean` | `#print axioms` for all main theorems | — |

## Commands

```
cd superpatterns/lean
lake update && lake exe cache get      # once
lake build                             # everything; prints axioms from Axioms.lean
lake build Superpatterns.Certificates  # D1 only
```

## Build times (wall clock, this machine)

* `Patterns.lean` first build: 79 s (first `import Mathlib` load); subsequent single-file
  compiles ~15–25 s, dominated by loading Mathlib oleans.
* `native_decide` σ7 (k=7, n=23, C(23,7)=245 157 subsets): ~5 s on top of import (file: 21 s total).
* kernel `decide` k=3 (n=5): 17.8 s total file (i.e. instantaneous beyond import).
* `native_decide` k=8: n=30 (5.85M subsets) 67 s CPU / 178 s wall (machine shared with another build);
  first full `Certificates.lean` build (n=32, 31, 30 + sanity checks): 688 s wall, 281 s CPU total.
* kernel `decide` (elaborator route) fails at k=4 (max recursion depth) and times out at k=5.
* `decide +kernel` (kernel route): k=4 (n=9) instantaneous (13 s total file); k=5 (n=13):
  "(kernel) deep recursion" at default `maxRecDepth`; with `maxRecDepth 1000000` it ran for 14 min
  without finishing and was killed.  So the kernel route is practical only up to k=4 with this checker
  (it evaluates `Array.set` as a list operation and the DFS is deep); k=7 by `decide` is infeasible.
* k=7 by kernel (`decide +kernel`, `maxRecDepth 10000000`, `maxHeartbeats 0`): killed after 14 min, unfinished.
* Second full `Certificates.lean` build (final version): 11 min 56 s wall, 312 s CPU.
* Full `lake build` (all modules, everything cached): 51 s; `Axioms.lean` 28 s.

## Axiom audit (output of `lake build`, from `Axioms.lean`)

* `checker_sound`, `sp3_example`, `sp4_example`, `card_le_sum_fiber`, `card_fiber_le_of_injective`,
  `pair_sum_le`, `tilt_bound`, `compSum_gaps`, `gaps_mem_box`, `gaps_injOn`, `constant_certificate`:
  `[propext, Classical.choice, Quot.sound]`.
* `σ7_superpattern`, `σ8_superpattern`, `σ8'_superpattern`, `σ8''_superpattern`:
  `[propext, Classical.choice, Quot.sound, <name>._native.native_decide.ax_1_1]`
  (Lean 4.33 records each `native_decide` as its own axiom instead of `Lean.ofReduceBool`).
* `lemma1_concrete`, `patCount_le_sum_W`, `theoremA`: `[propext, Classical.choice, Quot.sound]`
  (was `[propext, sorryAx, Classical.choice, Quot.sound]` before the two sorries were removed, see below).

## What is trusted

* `native_decide` adds axiom `Lean.ofReduceBool`: it trusts the Lean compiler + runtime evaluation
  of `checker k σ`.  The *soundness* `checker_sound : checker k σ = true → IsSuperpattern k σ` is
  checked by the kernel with only `propext`, `Classical.choice`, `Quot.sound`.
* `sp3_example`, `sp4_example` use kernel `decide` only (no `ofReduceBool`).
* Kernel `decide` requires the checker to be built only from structural recursion; for this reason the
  final loop uses `List.permutations'` (structural) rather than `List.permutations`
  (well-founded recursion, which the kernel will not unfold: `decide` got stuck on it).
## Sorries (all in `Encoding.lean`) — historical, both closed 2026-08-29

1. `card_patterns_over_le` — CKS injectivity in counting form: all `T` with the same off-`I` data `q`
   yield at most `k.descFactorial |q.1|` distinct patterns.  Needs `σ.Nodup`.  Difficulty: medium-hard
   (formalising "the pattern is determined by the relative order of the known values plus the ranks at
   `I`" needs an explicit reconstruction map on rank vectors; ~200–300 lines).
2. `fiber_card_ge` — extension counting: the fibre of `offData` through `T` has at least
   `∏_{i∈I(T)} (b_i − 1)` elements (independent choices `t'_i ∈ (t_{i−1}, t_{i+1})`, non-adjacency makes
   the intervals disjoint, stability keeps `I`).  Difficulty: medium-hard (an injection from a product of
   `Ioo` intervals into `Subsets k n` and a proof that replacing `t_i` inside its interval keeps the sorted
   order of the other positions; ~200–300 lines of `Finset.sort` bookkeeping).

Everything else in the chain `patCount ≤ ∑ W ≤ x^{-(n+1)} ∑_box … ≤ x^{-(n+1)} (x/(1−x))^{k+1} (1−x^k)^m`
is proved, including the finite Step-4 identity `pair_sum_le` (as an inequality, which is all that is used).

## 2026-08-29 (later): both sorries in `Encoding.lean` closed

`Encoding.lean` now has **no `sorry`**; `lake build` passes (all modules, 8715 jobs, ~45 s wall with
Mathlib cached) and `lake env lean Superpatterns/Axioms.lean` prints

* `lemma1_concrete`, `patCount_le_sum_W`, `theoremA`: `[propext, Classical.choice, Quot.sound]`.

No `native_decide`, no new axioms, statements of `card_patterns_over_le` / `fiber_card_ge` unchanged
(so `TheoremA.lean` needed no edits).  `Encoding.lean` grew from 417 to ~835 lines.

### 1. `card_patterns_over_le` (CKS injectivity, counting form)

Helper lemmas (all in the new section "CKS injectivity: helper lemmas"):

* `vals σ T j := σ.getD (posGet T j) 0`; `valsAt_eq : valsAt σ T = (List.range k).map (vals σ T)`;
  `length_patOf`, `patOf_getD` (`(patOf σ T).getD j 0 = rank (valsAt σ T) (vals σ T j)`),
  `rank_map_range` (rank as a `Finset.card` of a filter over `range k`), `patOf_getD_eq_card`,
  `patOf_getD_lt` (ranks are `< k`).
* `posGet_injOn`, `vals_injOn` (uses `σ.Nodup` via `List.Nodup.getElem_inj_iff`), `vals_lt_iff`
  (`v j' < v j ↔ π j' < π j`, from `lt_iff_rank_lt`), `patOf_injOn`.
* `offData_eq_iff`: `offData k I T' = offData k I T ↔ I T' = I T ∧ ∀ j ∈ [1,k], j ∉ I T → t'_j = t_j`
  (via `List.map_inj_left`); used by both parts.
* `eq_of_card_filter_lt_aux`, `eq_of_card_filter_lt`: for `x, x' ∉ A`,
  `#{a ∈ A : a < x} + c = x` and `#{a ∈ A : a < x'} + c = x'` force `x = x'`
  (i.e. `x ↦ x − #{a ∈ A, a < x}` is injective off `A`).
* `patOf_eq_of_agree` (**the CKS reconstruction**): same off-`I` data + equal pattern values on `I`
  ⇒ equal patterns.  Proof: for `j ∉ I` (0-indexed `j+1 ∉ I T`),
  `π j = #{j' ∈ I : π j' < π j} + #{j' ∉ I : v j' < v j}`; the second term is determined by the
  off-`I` data, the first equals `#{a ∈ A : a < π j}` with `A = π(I)` the same set for both `T, T'`
  (`filter_image` + `card_image_of_injOn`), and `π j ∉ A`; conclude with `eq_of_card_filter_lt`.
* `exists_emb`: the map `i ↦ π(i)` is an embedding `↥(I T) ↪ Fin k`.

Main proof: `Fintype.card_le_of_injective` from the subtype of patterns over `q` into
`↥q.1 ↪ Fin k`, whose cardinality is `k.descFactorial q.1.card` by `Fintype.card_embedding_eq`.
(The first component `q.1` is `subst`-ed to `I T` after destructuring `q`.)

### 2. `fiber_card_ge` (extension counting)

Helper lemmas (section "Extension counting: helper lemmas"):

* `pos_toFinset`, `posGet_toFinset`, `toFinset_mem_Subsets`: a strictly increasing list `l` of length
  `k` with entries `< n` gives `l.toFinset ∈ Subsets k n` with `pos l.toFinset = l`
  (`List.toFinset_sort`).
* `lt_of_step`: strict monotonicity from consecutive steps.
* `replPos I₀ T g j := if j+1 ∈ I₀ then g (j+1) _ else posGet T j`,
  `replSet k I₀ T g := ((List.range k).map (replPos I₀ T g)).toFinset`;
  `replPos_step` (uses non-adjacency: the three cases `j+1 ∈ I`, `j+2 ∈ I`, neither),
  `replPos_lt_n`, `replList_pairwise`, `replSet_mem`, `posGet_replSet`,
  `posGet_replSet_of_notMem`, `posGet_replSet_of_mem`.

Main proof: `∏_{i ∈ I T} (b_i − 1) = #((I T).pi (fun i => Ioo (t_{i−1}) (t_{i+1})))` by
`Finset.card_pi` + `Nat.card_Ioo`, then `card_le_card_of_injOn (fun g => replSet k (I T) T g)`:
maps-to uses `replSet_mem`, `hstable` and `offData_eq_iff`; injectivity reads `g i` back off
`posGet (replSet …) (i − 1)`.

### Remaining sorries

None in the whole project.  The only non-standard axioms left are the per-certificate
`native_decide` axioms in `Certificates.lean` (σ7, σ8, σ8', σ8''), as before.

## 2026-08-29 (W35): witness reduction, block splitting, Erdős–Szekeres

New modules (in root and in `Axioms.lean`), all sorry-free, standard axioms only:

| file | content |
|---|---|
| `Superpatterns/Witness.lean` | `FinProb` (finite weighted probability space), `E`/`Pr`/`Eon`, count `cnt`; Prop. 15 (a) `mean_eq_E_on_pos`, `Pr_pos_le_mean`, `Pr_le_one`; (b) `sq_mean_le` (Cauchy–Schwarz), `E_sq_eq_sum`, `mean_le_max_cond`; (c) `witness_reduction`, `witness_reduction_max`; uniform model `Perms n`, `FinProb.uniform`, `missing`, `cnt_missing_pos_iff`, `witness_reduction_uniform` |
| `Superpatterns/BlockSplit.lean` | `OrdIso` equivalence, `Contains.of_sublist`, `contains_ranks_iff`, `block`/`blockStd`, `blockStd_avoids`, `ranks_perm_range` (combinatorial core of W27 Lemma 0.2; the independence/probabilistic half is not formalised) |
| `Superpatterns/ErdosSzekeres.lean` | imports `Archive.Wiedijk100Theorems.AscendingDescendingSequences` (builds from the Mathlib cache in ~5 s); `ofFn_sublist`, `OrdIso_range_of_strictMono`, `OrdIso_range_reverse_of_strictAnti`, `erdos_szekeres_contains`, `not_avoid_both`, `not_avoid_id_rev` |

Full `lake build`: 8719 jobs, 15 s wall (cached). Details: `experiments/w35-lean-witness/`.
