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
| `Superpatterns/Interleaving.lean` | Formal proofs for multi-chain decompositions, avoidance of 21 and 321 for increasing sequences, multi-chain word entropy power identities, collision-free coordinate intervals for disjoint monotone blocks, window separation, lookahead dynamic bypass order preservation, and supercritical velocity algebraic inequalities. |
| `Superpatterns/Axioms.lean` | Automated axiom audit module. Every theorem prints its exact axiom dependencies. |

## Axiom Policy

- All mathematical theorems in `Superpatterns/Interleaving.lean`, `TheoremA.lean`, `ErdosSzekeres.lean`, `BlockSplit.lean`, `Numeric.lean`, and `Witness.lean` depend **only on standard foundational axioms**:
  - `propext` (Propositional Extensionality)
  - `Quot.sound` (Quotient Soundness)
  - `Classical.choice` (Axiom of Choice)
- Zero `sorry`s exist across the entire project.
- The large computational witness evaluations in `Certificates.lean` use `Lean.ofReduceBool` (`native_decide`) for finite kernel execution, which is explicitly separated and audited.
