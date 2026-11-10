# Lean 4 Formal Verification for Superpatterns

This directory contains formal verification proofs in **Lean 4** accompanying the research on permutation superpatterns and Noga Alon's random-superpattern conjecture by **Adam Ever-Hadani**.

## Build and Verification Instructions

Requirements: Lean 4 (version specified in `lean-toolchain`).

```sh
cd formal-verification/lean
lake build
```

## Structure of Formal Proofs

| Module | Contents and Status |
|---|---|
| `Superpatterns/Patterns.lean` | Core permutation pattern definitions: `Contains`, `IsSuperpattern`, `OrdIso`, standardisation (`ranks`), monotonicity. |
| `Superpatterns/Checker.lean` | Verified algorithmic substring checker; proof that `checker_sound` certifies superpatterns. |
| `Superpatterns/Certificates.lean` | Exact short superpattern witnesses ($\sigma_7 \in S_{23}$, $\sigma_8, \sigma_8', \sigma_8'' \in S_{30}$); evaluation using `native_decide`. |
| `Superpatterns/Encoding.lean` | Formalization of the stable encoding framework, gap coordinate systems, and index fibers. |
| `Superpatterns/Tilt.lean` | Exponential tilting lemmas and geometric series representations. |
| `Superpatterns/TheoremA.lean` | Formal proof of **Theorem A** bounding pattern counts via the exponential tilt. |
| `Superpatterns/Numeric.lean` | Rational certificate proving negativity of the asymptotic exponent at $\lambda = 1.0003$. |
| `Superpatterns/Witness.lean` | Probability measures on finite permutation sets, Cauchy–Schwarz for moments, and witness reductions. |
| `Superpatterns/BlockSplit.lean` | Block standardisation and pattern avoidance preservation. |
| `Superpatterns/ErdosSzekeres.lean` | Formal connection from Mathlib's Erdős–Szekeres theorem to pattern containment and reverse avoidance. |
| `Superpatterns/BlockFlip.lean` | Verified containment test (`containsB_iff`), direct sums of patterns, and exhaustively checked instances of the block-flip inequality (W90 Theorem 1) for n ≤ 9. The general theorem is only stated, not proved; see the section below and `BLOCKFLIP-PLAN.md`. |
| `Superpatterns/Axioms.lean` | Automated axiom audit module. Every theorem prints its exact axiom dependencies. |

## Axiom Policy

- All mathematical theorems in `TheoremA.lean`, `ErdosSzekeres.lean`, `BlockSplit.lean`, `Numeric.lean`, and `Witness.lean` depend **only on standard foundational axioms**:
  - `propext` (Propositional Extensionality)
  - `Quot.sound` (Quotient Soundness)
  - `Classical.choice` (Axiom of Choice)
- Zero `sorry`s exist across the entire project.
- The large computational witness evaluations in `Certificates.lean` use `Lean.ofReduceBool` (`native_decide`) for finite kernel execution, which is explicitly separated and audited.
- `BlockFlip.lean` uses `native_decide` for its counts over S_8 (except 1234 and 1324) and S_9 and for one bounded sweep; its other certificates are evaluated by the kernel (table below).

## Block-flip instances (`Superpatterns/BlockFlip.lean`, W90/W91)

The block-flip theorem (W90 Theorem 1) says #{σ ∈ S_n ⊇ α⊕21⊕β} ≤ #{σ ∈ S_n ⊇ α⊕12⊕β} for all patterns α, β and all n.
**The general theorem is not formalised.** The module states it (`BlockFlipStatement`) and certifies finitely many
instances by exhaustive enumeration of S_n; `BLOCKFLIP-PLAN.md` assesses what a full formalisation would take.

| Item | Lean name | Checked by |
|:--|:--|:--|
| Containment test, sound and complete: `containsB σ π = true ↔ Contains σ π`; `Decidable (Contains σ π)` | `containsB_iff` | kernel |
| #{σ ∈ S_n ⊇ π} (`numContaining`, a `Nat.card`) equals the executable count; same for `Perms n` | `numContaining_eq`, `card_Perms_contains` | kernel |
| Direct sum `α ⊕ₚ β` of patterns; it maps permutations to permutations | `dsum`, `dsum_perm`, `dsum_lt`, `dsum_assoc` | kernel |
| 3 4 1 6 7 2 5 contains 1234 and avoids 1324; 1 4 5 2 7 8 3 6 9 contains 123456 and avoids 124356 | `perm3416725_*`, `perm145278369_*` | kernel |
| 1234 vs 1324: equal counts for n ≤ 6; 2279 vs 2278 on S_7 (difference 1); 24553 vs 24527 on S_8 (difference 26) | `count_1234_eq_count_1324_of_le_6`, `count_1234_sub_count_1324_7`, `count_1234_sub_count_1324_8` | kernel |
| 1234 vs 1324 on S_9: 268521 vs 268104 (difference 417) | `count_1234_sub_count_1324_9` | `native_decide` |
| 123456 vs 124356: equal counts for n ≤ 8; 18043 vs 18042 on S_9 (difference 1) | `count_123456_eq_count_124356_of_le_8`, `count_123456_sub_count_124356_9` | kernel (n ≤ 7), `native_decide` (n = 8, 9) |
| Exact counts of both sides for (α, β) ∈ {(1,1), (12,1), (1,12), (21,1), (12,12), (21,21)}, n = 7, 8, 9 | `blockFlip_α_β_n`, `blockFlipAt_α_β_n` | kernel (n = 7, and (1,1) at n = 8), `native_decide` (other n = 8, n = 9) |
| The inequality for all α, β of size ≤ 2 (16 pairs, empty pattern included) and all n ≤ 8 | `blockFlipAt_of_le_2_of_le_8` | `native_decide` |

Differences found (12-version minus 21-version): (1,1): 1, 26, 417 at n = 7, 8, 9; (12,1), (1,12), (21,1): 0, 1, 45;
(12,12), (21,21): 0, 0, 1.

Trust assumptions. "Kernel" means `decide +kernel`: the statement is evaluated by the Lean kernel and depends only
on `propext`, `Classical.choice`, `Quot.sound`. `native_decide` additionally trusts the Lean compiler and runtime
for the evaluation of one closed Boolean statement (the same assumption as `Certificates.lean`); the reduction of
the mathematical statement to that Boolean statement is kernel-checked. All certificates are stated with the
mathematical predicate `Contains`, not with the Boolean checker. S_n is the set of lists that are rearrangements of
`[1, …, n]`. Reference values were first computed by an independent brute-force program and then re-derived by Lean.
Kernel evaluation succeeds for every n = 8 count (about 21 s and 5.5 GB of memory each) but is used only for
1234 and 1324, to keep the build light; at n = 9 it was abandoned (more than 22 GB of memory after 80 s).
