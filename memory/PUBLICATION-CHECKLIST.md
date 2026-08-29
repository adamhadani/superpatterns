# Publication checklist (adapted from `publishing-llm-assisted-mathematics.md`)

Status as of 2026-08-29. ☑ done · ☐ open · ◐ partial.

## Mathematical claim
- ☑ Definition of k-superpattern explicit (classical/non-consecutive containment; paper §1).
- ☑ Every new bound stated precisely with the prior best and the same conventions (summary table, paper §1).
- ☑ Results classified: explicit witnesses (sp(7), sp(8)); proofs (Thm A, C, 5, 8, 9, 10, c₂₁ bounds); exact values by SAT (f(k;k+1), rosaries); negative results.
- ☑ Witnesses printed in the paper and machine-readable in `experiments/witnesses/witnesses.txt`.

## Verification
- ☑ Two independent implementations for the superpattern witnesses: C DFS checker (`experiments/w1-search/sp.c`), the pure-Python
  brute force (`experiments/witnesses/check_witness.py`, no shared code), and additionally the Lean kernel-checked DFS
  (`formal-verification/lean/Superpatterns/Certificates.lean`, `native_decide` + proved `checker_sound`).
- ☑ Checkers pass known positives (sp(3)=5, sp(4)=9, ζ₅ (13), Arnarson's 17) and damaged negatives (`check_witness.py --test`).
- ☑ Pattern counts, subset counts, versions and SHA-256 hashes recorded (`experiments/witnesses/README.md`, paper §Verification).
- ☑ Theorem A fully formalised in Lean (axioms: propext, Classical.choice, Quot.sound).
- ◐ SAT results (f(k;k+1), rosaries, sp(4)=9, sp(5)=13 re-proofs): scripts and logs archived; DRAT proof certificates not yet emitted.
- ☑ Every theorem from a workstream re-derived by the coordinating session before entering the paper (`SESSION-STATE.md`).

## Novelty
- ☑ Literature searched under neighbouring terminology (superpatterns, universal permutations, universal/complete sequences for
  patterns, dense packing, zigzag constructions, circular superpatterns, OEIS A342474); see `priority-check.md`, `NOTES.md`.
- ☑ Citing literature of CKS21 (to 2026-08) and EV21 checked; Hunter's unpublished 15/32 claim recorded.
- ☑ Witnesses compared with prior ones under reverse/complement/inverse (the 23 and 30 are not tie-broken words over [k+1]; Arnarson's 17 is).
- ☐ Specialists in permutation patterns asked about prior art / definitional mismatch.
- ◐ Every citation opened and checked by a human (all bib entries were checked against arXiv/DOI metadata by the session; human pass pending).

## Reproducibility
- ☑ Code, witnesses, tests and one-command instructions public (this repository).
- ☐ Stable DOI (Zenodo deposit) — do at preprint time.
- ☐ Fresh-machine reproduction of the principal results (CI covers Lean and the paper build; the witness check is one command).

## Responsible AI disclosure
- ☑ Model/version, date and material uses disclosed (paper §Discovery method and AI disclosure).
- ◐ Prompts and visible outputs preserved: workstream briefs and results are in `experiments/*/log.md`; the full session transcript
  is kept locally (`~/.claude/projects/...jsonl`) and should be exported into the archive before release.
- ☑ The LLM is not an author; human author takes responsibility.
- ☐ Target journal's current AI policy checked (candidates: Electronic J. Combin., Australasian J. Combin., Discrete Math., Combinatorial Theory).

## Publication
- ☑ Manuscript leads with the mathematics; title descriptive.
- ☑ Paper explains more than the existence of witnesses (structure of witnesses, lower-bound method, random-permutation results, dead ends).
- ☐ Preprint marked as not peer-reviewed; arXiv `math.CO`.
- ☐ One journal at a time.

## Before announcing
1. Human read-through of every proof in the paper (especially Theorems C, 5, 8, 10 and the c₂₁ bounds).
2. Send the concise package (statements, witnesses, verification instructions, prior bounds) to 1–2 specialists.
3. Zenodo deposit; add DOI to README and paper.
