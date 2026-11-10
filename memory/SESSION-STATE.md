# Current session state — 10 November 2026

Read this first, then [AUDIT-2026-11-10.md](AUDIT-2026-11-10.md), [ALON-STRATEGY.md](ALON-STRATEGY.md) §0,
`experiments/w90-layered-deficit/proof.md` and `experiments/w91-strict-deficit/proof.md`. The previous version of this file (22–27 September) is archived at
`archive/SESSION-STATE-2026-09-27-superseded.md`; its verdicts were not supported by the proofs.

## Verdict

* **Claimed on 10 Nov 2026 (evening), not externally verified: c₂₁ < 1, so Alon's conjecture is false for small
  fixed ε** (W91 part 2, `experiments/w91-strict-deficit/proof-c21.md`: Lemma R, Theorem D, Corollary E). The
  argument: ℓ(T) = E L₂₁(P_T) is superadditive and satisfies ℓ(2T) ≤ 2ℓ(T) + 45√(T ln T) (cut an optimal copy at the
  antidiagonal; Talagrand), hence c₂₁T − 200√(T ln T) ≤ ℓ(T) ≤ c₂₁T; Proposition 6.1 of W91 gives
  2ℓ(T) ≤ 2T − 10⁻⁹⁴T/ln T; so c₂₁ < 1. Written and reviewed by AI only — say "claimed", not "established".
* **Background (morning): Alon's conjecture was not proved here, and the evidence pointed the other way.** For the pattern
  21^{⊕k/2} = 2 1 4 3 … the limiting constant c₂₁ satisfies c₂₁ ≤ 1 (**proved**, W90 Corollary 2) and, numerically,
  c₂₁ = 0.99887 ± 0.00002 (paired simulation, n = 10³…10⁸; the deficit E⌊LIS/2⌋ − E L₂₁ grows like 0.00113·√n).
  If c₂₁ < 1, a random permutation of length (1+ε)k²/4 with ε < 0.0023 does not contain that pattern, so the sharp
  conjecture fails. Layers of size 3, 4, 5, 6 show deficits 0.0050, 0.0075, 0.0095, 0.0105 (D/√n); sizes 8–16 show 0.012–0.017.
* **New, proved (W91, 10 Nov, afternoon): E LIS(σ_n) − 2·E L₂₁(σ_n) ≥ c·√n/ln n** for large n (c = 10⁻⁹⁴). Hence
  2 1 4 3 ⋯ of length k is w.h.p. not contained for n ≤ (k²/4)(1 + c′/ln k), while the identity is contained at
  k²/4 + ω(k^{4/3}): the identity is not the hardest pattern. Also: one adjacent transposition, averaged over its
  position, costs a positive constant (Poisson model). By itself this is not c₂₁ < 1; part 2 supplies the step.
* Still **open**: an effective version (deficit ≥ c√n with a usable constant), i.e. removing the ln n directly.
  W91 §7 reduces it to hypothesis (H): a window of boundedly many consecutive steps of the leftmost optimal copy,
  at a prescribed level, contains a step whose rectangle has area ≥ a with probability ≥ ½.
* Universality at C·k² for all patterns (removing He–Kwan's log log k) is untouched here. A preprint of Oct 2026
  (Chen–Wang, arXiv:2610.13530, unrefereed, AI-found proof per its abstract) announces 32k²; not read, not verified
  here. It is consistent with c₂₁ < 1.

## Verified in this session (norm 1)

| Item | How it was verified |
|:--|:--|
| Theorem 1 (W90): #(⊇ α⊕21⊕β) ≤ #(⊇ α⊕12⊕β), exact fibre formula | Proof written and re-derived by the main session; `verify_fibers.py` recomputes U, S, fibres and boards from the definitions for 7 choices of (α, β), all σ ∈ S_n, n ≤ 8 (n = 9 for (21, 21)); reproduces \|Av₈(1324)\| − \|Av₈(1234)\| = 26 |
| L₂₁ ≤_st ⌊LIS/2⌋, c₂₁ ≤ 1 | Corollary of Theorem 1; exhaustive counts on S_n, n ≤ 12 (`exact_dist.c`): equal for n ≤ 8, deficits 1, 66, 2565(+2), 77232(+213) for n = 9…12 |
| Smallest defect: 3 points, 3×3 board minus two opposite corners, weight 1/3 | `skew_boards.py` (all boards for N ≤ 5); the single extra avoider of 214365 at n = 9 is one such fibre |
| Deficit ∝ √n | `l21_paired.c`: 1 290 950 paired samples; algorithm validated against an O(n³) DP (180 000 permutations) and against the exhaustive counts; independent cross-check with W40 `pruned.c`, numpy PCG64 and Python LIS: 0 disagreements on 81 240 permutations and the same deficit |
| Exact fibre formula stage by stage | `fibre_cost.py`: equals Σ(LIS − N) exactly on S₈ (1) and S₉ (46); at n = 10⁴, flips 1…63, 120 000 permutations: 0.15641 ± 0.00083 vs 0.153 ± 0.012 measured directly on the same permutations |
| Audit findings in AUDIT-2026-11-10.md §3 | Two reviewers; every cited line re-read by the main session |
| W91 Lemmas 2.3–2.5 (planted 3416725 gives the 3-point lens; at most one planted pair per stage; leftmost optimal copy satisfies the outside conditions) | Proofs re-derived twice by the main session; `gadget_check.py` from the W90 definitions: 7756 plantings (3982 under patterns with 21-blocks), 15 512 injectivity cases, 1930 copy pairs, 0 failures; independently written `review/lemma23_containment.py` (direct containment, no fibres): 47 428 plantings, 70 144 copy pairs, 0 failures, negative controls fail as they should |
| W91 Lemma 3.1 (resampling identity) | Mecke formula; Monte Carlo with a one-point plant (1.6427 ± 0.0076 vs 1.6454 ± 0.0040; 3.334 ± 0.020 vs 3.307 ± 0.011); exact at leading order for the 7-point plant (1/(9!)² both sides) and, by the reviewer, for a pattern with a 21-block (1/(11!)²) |
| W91 part 2: Lemma C, Lemma R, Corollary R′, Theorem D (c₂₁ < 1), Corollary E | Written and re-derived by the main session; Talagrand's inequality checked against Alon–Spencer 4th ed. Thm 7.7.1 and the Mecke equation against Last–Penrose Thm 4.4 (user's copies); independent adversarial review `out/review-2.md` (holds; one false auxiliary sentence "2Y_n ≤ LIS pointwise" and five cosmetic points, all corrected; no circularity; Prop. 6.1 re-read, nothing found); reviewer's numerics `review2/`: ℓ(2T) − 2ℓ(T) ≈ 0.65·T^{1/3} for T = 10…400, cutting inequality 3300/3300 |
| W91 Theorems A, B, Corollary C (probabilistic assembly, §4–§6) | Written proof only (constants 10⁻⁸⁰, 10⁻⁹⁴ cannot be sampled); re-derived line by line by the main session and by an independent adversarial reviewer (`out/review-1.md`: no error; nine under-justified steps, all incorporated); constants recomputed (`out/constants.txt`); (F3) and Lemma 1.1 exact on S₇–S₉ |

Not verified / not claimed: a deficit of order √n (numerical only; proved order is √n/ln n); W91 has not been read
by a human specialist; the inequality for layers of size ≥ 3
(Jelínek–Karpilovskij conjecture; data consistent); priority of Theorem 1 (it is the k = 2 transversal case of
Jelínek–Karpilovskij 2021 / Burstein–Pantone 2015 in pattern language — no novelty claimed for it).

## Open gaps, in priority order

0. **Get W91 (both parts) read by a human specialist** before anything is announced or pushed as a result. The
   chain is: W90 Theorem 1 → W91 Lemmas 1.1–3.2 → Proposition 6.1 → `proof-c21.md`. A single error anywhere in
   Proposition 6.1 would void Theorem D; the rate lemma is classical.
1. **Effective constant (remove the ln n from W91 Theorem B).** No longer needed for c₂₁ < 1. State after W91: transpositions placed at random,
   K ≈ 45 ln T blocks apart, each cost a constant, because one leftmost optimal copy serves a whole window of
   candidate positions and windows of ≥ 90 ln T steps are good everywhere by first-moment bounds. For constant K
   one needs hypothesis (H) of `experiments/w91-strict-deficit/proof.md` §7: it is a statement about the first
   steps of a point-to-corner geodesic of a fresh Poisson process started from the best point of an independent
   staircase (the front). Expected tools: local increments via the stationary Hammersley process
   (Cator–Groeneboom, Cator–Pimentel) or results on the environment seen from a geodesic — not checked. The old
   estimate (E2) is now a theorem for fat pairs (§7, remark 2). Untried ideas are in W91 `log.md` §10 (arbitrary
   reference content / moats; near-optimal anchors). W90's `strict-deficit-plan.md` is superseded by W91.
2. Size-≥3 blocks: prove P(⊇ α⊕J_d⊕β) ≤ P(⊇ α⊕I_d⊕β) (transversal case of the JK conjecture).
3. Which layered pattern is hardest? D/√n is still increasing at layer size 16 (0.012, 0.0135, 0.014, 0.017 for
   sizes 8, 10, 12, 16 at n = 10⁵); the large-layer limit should be a KPZ-scale constant times d^{−2/3}. A faster
   algorithm is needed beyond size 16.
4. Universality at C·k²: no progress here; W9/W13/W15 remain this repository's state. See Chen–Wang,
   arXiv:2610.13530 (32k² announced). Reading it against W9 Theorem 8 would be a useful independent check.

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

## Added on 10 November 2026 (afternoon): W91

* `experiments/w91-strict-deficit/`: `proof.md` (Theorems A, B, Corollary C, hypothesis (H)), `log.md` (chronology,
  dead ends, verification, untried ideas), `gadget_check.py` + `run_checks.sh` + `out/`, the reviewer's report
  `out/review-1.md` and independent code `review/`.
* Paper: new §6.3 "A strict deficit" (Theorems 29, 31, Corollary 30, Lemmas 32, 33), abstract, summary table,
  verification bullet, `Talagrand95` in `references.bib`. `make check` prints 0; pages 2, 15–18 inspected (24 pages).
* README, experiments/README, RESULTS, NOTES, ALON-STRATEGY §0, priority-check and PUBLICATION-CHECKLIST updated.
* Evening: `proof-c21.md`, `out/review-2.md`, `review2/` (reviewer's code and raw outputs); paper §6.3 extended
  with Lemma 34, Theorem 35, Corollary 36 and a caution paragraph (25 pages, `make check` 0, pages 18–19 inspected);
  `Alexander94`, `Rhee95`, `AlonSpencer16` added to `references.bib`.
* Not committed at the time of writing unless `git log` shows a W91 commit. Nothing pushed; the public GitHub
  README still shows the withdrawn September claims.

## Added on 10 November 2026 (night): referee package

* `output/paper/layered-refutation.md` → `output/pdf/layered-refutation.pdf` (`make -C output/paper refutation-note`):
  13-page self-contained note with only the disproof chain, one planted pattern (3416725), deficit
  T/(ln T)² (enough for Theorem 1), dependency list, verification table. **This is the file to give a referee.**
* `experiments/w91-strict-deficit/out/citation-audit.md`: every citation checked against primary sources;
  corrections applied (block-flip attribution: Jelínek thesis / Burstein–Pantone, not Jelínek–Karpilovskij;
  Chen–Wang preprint cited; Arratia Conjecture 3 and He–Kwan Conjecture 5.3 added; Alexander vs
  Lember–Matzinger–Torres for the rate lemma).
* Cold reads of the note: `out/review-3-note.md` (first version: no error, 14 small gaps, notation) and
  `out/review-4-note.md` (rewritten version: no error; one wrong cross-reference and remaining symbol clashes,
  all fixed). The last notation/wording pass after review 4 has not been re-read by a reviewer.
* Note rewritten after review 3: section-based numbering, cleaned notation, simplified tie-breaks (O5), (O6)
  (re-derived; `gadget_check.py strict`: 1922 copy pairs, 2365 plantings, 4730 uniqueness cases), two-sided
  threshold (Corollary 1.3), AI declaration after the abstract, concluding remarks, verification appendix. 17 pages.
* `related-work.md`: comparison with He–Kwan and Chen–Wang (opposite directions; bracket (1+ε₀)/4 ≤ C* ≤ 32).
* Lean: `formal-verification/lean/Superpatterns/BlockFlip.lean` — containment checker proved sound and complete
  (`containsB_iff`), direct sums, the two explicit permutations, exact counts on S₇, S₈, S₉ for six (α, β)
  (1234 vs 1324: differences 1, 26, 417; 123456 vs 124356: 0, 0, 1), and the inequality for all α, β of size ≤ 2,
  n ≤ 8. Kernel-only for n = 7 and for 1234/1324 at n = 8; `native_decide` otherwise. `lake build`: 8720 jobs,
  0 errors, no `sorry` (re-run by the main session). The counts agree with the known |Av_n(1234)|, |Av_n(1324)|.
  `BLOCKFLIP-PLAN.md`: full formalisation of Theorem 1 ≈ 1500–2200 lines; the Poisson part is out of reach.
* The notes paper §6.3 now states the results and points to the note (24 pages, `make check` 0).

## Jobs

Nothing is running. All W90 batches finished on 10 Nov; tables are in `experiments/w90-layered-deficit/out/`
(`l21_table.txt`, `family_table.txt`, `hybrid_table.txt`) and are regenerated by `aggregate.py`,
`aggregate_family.py`, `aggregate_hybrid.py`. The proof attempt for the strict inequality is recorded in
`experiments/w90-layered-deficit/strict-deficit-plan.md` (plan only; one lemma missing).

## Machine hygiene

12 cores, 64 GB. Keep `uptime` load below 12: other projects and Spotlight were using 3–5 cores during this
session, so run at most 5–6 workers. Each n = 10⁸ worker needs ≈ 0.8 GB. Compiled binaries live in the session
scratch directory, not in the repo.
