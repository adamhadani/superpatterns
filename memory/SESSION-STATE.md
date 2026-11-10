# Current session state — 10 November 2026

Read this first, then [AUDIT-2026-11-10.md](AUDIT-2026-11-10.md), [ALON-STRATEGY.md](ALON-STRATEGY.md) §0 and
`experiments/w90-layered-deficit/proof.md`. The previous version of this file (22–27 September) is archived at
`archive/SESSION-STATE-2026-09-27-superseded.md`; its verdicts were not supported by the proofs.

## Verdict

* **Alon's conjecture is not proved here, and the evidence now points the other way.** For the pattern
  21^{⊕k/2} = 2 1 4 3 … the limiting constant c₂₁ satisfies c₂₁ ≤ 1 (**proved**, W90 Corollary 2) and, numerically,
  c₂₁ = 0.99887 ± 0.00002 (paired simulation, n = 10³…10⁸; the deficit E⌊LIS/2⌋ − E L₂₁ grows like 0.00113·√n).
  If c₂₁ < 1, a random permutation of length (1+ε)k²/4 with ε < 0.0023 does not contain that pattern, so the sharp
  conjecture fails. Layers of size 3, 4, 5, 6 show deficits 0.0050, 0.0075, 0.0095, 0.0105 (D/√n); sizes 8–16 show 0.012–0.017.
* The rigorous disproof is **open**: it needs liminf (E⌊LIS/2⌋ − E L₂₁)/√n > 0. W90 gives an exact formula for the
  left side as a sum of non-negative local terms and identifies the smallest contributing configuration.
* Universality at C·k² for all patterns (removing He–Kwan's log log k) is **open** and untouched.

## Verified in this session (norm 1)

| Item | How it was verified |
|:--|:--|
| Theorem 1 (W90): #(⊇ α⊕21⊕β) ≤ #(⊇ α⊕12⊕β), exact fibre formula | Proof written and re-derived by the main session; `verify_fibers.py` recomputes U, S, fibres and boards from the definitions for 7 choices of (α, β), all σ ∈ S_n, n ≤ 8 (n = 9 for (21, 21)); reproduces \|Av₈(1324)\| − \|Av₈(1234)\| = 26 |
| L₂₁ ≤_st ⌊LIS/2⌋, c₂₁ ≤ 1 | Corollary of Theorem 1; exhaustive counts on S_n, n ≤ 12 (`exact_dist.c`): equal for n ≤ 8, deficits 1, 66, 2565(+2), 77232(+213) for n = 9…12 |
| Smallest defect: 3 points, 3×3 board minus two opposite corners, weight 1/3 | `skew_boards.py` (all boards for N ≤ 5); the single extra avoider of 214365 at n = 9 is one such fibre |
| Deficit ∝ √n | `l21_paired.c`: 1 290 950 paired samples; algorithm validated against an O(n³) DP (180 000 permutations) and against the exhaustive counts; independent cross-check with W40 `pruned.c`, numpy PCG64 and Python LIS: 0 disagreements on 81 240 permutations and the same deficit |
| Audit findings in AUDIT-2026-11-10.md §3 | Two reviewers; every cited line re-read by the main session |

Not verified / not claimed: strict asymptotic deficit (numerical only); the inequality for layers of size ≥ 3
(Jelínek–Karpilovskij conjecture; data consistent); priority of Theorem 1 (it is the k = 2 transversal case of
Jelínek–Karpilovskij 2021 / Burstein–Pantone 2015 in pattern language — no novelty claimed for it).

## Open gaps, in priority order

1. **Prove c₂₁ < 1.** Reduction in W90 `proof.md` §4, `log.md` §4 and `strict-deficit-plan.md`: enough to show that for a positive fraction of
   the ≍ √n flip stages, with probability bounded below, some level has (i) the 21-version failing and (ii) an
   isolated 3-point defect lens. Missing ingredient: tightness of the number of free points within O(1) levels of
   the maximum, or a softer substitute. Alternative: sparse swaps (pattern "identity with a transposition every
   2K places") plus relaxation of the Hammersley tandem between defects.
2. Size-≥3 blocks: prove P(⊇ α⊕J_d⊕β) ≤ P(⊇ α⊕I_d⊕β) (transversal case of the JK conjecture).
3. Which layered pattern is hardest? D/√n is still increasing at layer size 16 (0.012, 0.0135, 0.014, 0.017 for
   sizes 8, 10, 12, 16 at n = 10⁵); the large-layer limit should be a KPZ-scale constant times d^{−2/3}. A faster
   algorithm is needed beyond size 16.
4. Universality at C·k²: no progress; W9/W13/W15 remain the honest state.

## Clean-up done on 10 November 2026

* W43–W89 moved, unedited, to `experiments/archive-2026-09-unverified/` (README there says why each approach fails).
* Removed: `output/arxiv/` (submission bundle of the withdrawn preprint), `quadratic-universality.*`, `knowledge/`,
  `implementation_plan.md`, `ORIGINAL_REQUEST.md`. All remain in git history (last present in commit `6978364`).
* Lean: removed `Greene.lean` (six axioms), `Interleaving.lean`, `Lattice.lean`; restored `Witness.lean`,
  `Axioms.lean`, `Superpatterns.lean` to their 30 August state. `lake exe cache get && lake build` on 10 Nov:
  8719 jobs, 0 errors, 0 warnings, no `sorry`, no added axioms (the machine had no Mathlib build cache before).
* Paper `output/paper/superpatterns-notes.md` rewritten around what is proved: new §6.2 (Theorem 26, Corollary 27,
  Proposition 28, deficit table), new abstract and summary table, withdrawal note in §7. `make check` prints 0 for
  the notes and for the repeated-21 note; pages 1, 2, 14, 15 inspected.
* `README.md`, `RESULTS.md`, `NOTES.md`, `priority-check.md`, `PUBLICATION-CHECKLIST.md`, `experiments/README.md`
  rewritten or pruned to the accepted statements.

## Jobs

Nothing is running. All W90 batches finished on 10 Nov; tables are in `experiments/w90-layered-deficit/out/`
(`l21_table.txt`, `family_table.txt`, `hybrid_table.txt`) and are regenerated by `aggregate.py`,
`aggregate_family.py`, `aggregate_hybrid.py`. The proof attempt for the strict inequality is recorded in
`experiments/w90-layered-deficit/strict-deficit-plan.md` (plan only; one lemma missing).

## Machine hygiene

12 cores, 64 GB. Keep `uptime` load below 12: other projects and Spotlight were using 3–5 cores during this
session, so run at most 5–6 workers. Each n = 10⁸ worker needs ≈ 0.8 GB. Compiled binaries live in the session
scratch directory, not in the repo.
