# CLAUDE.md — working rules for this repository

Research repo on k-superpatterns (bounds on sp(k), constructions, Alon's random-superpattern conjecture).
Start by reading `memory/SESSION-STATE.md` (live state, open gaps, running workstreams), then
`memory/NOTES.md` (literature + results), then the paper `output/paper/superpatterns-notes.md`.

## Layout

- `output/paper/` — the paper (Markdown → pandoc → xelatex). Build: `make pdf`; lint: `make check` must print `0`.
  Formatting rules live in the skill `.claude/skills/paper-formatting/SKILL.md` — use it for every paper edit.
- `formal-verification/lean/` — Lean 4 / Mathlib project (`lake build` must pass; never leave `sorry`s in
  committed files; `Superpatterns/Axioms.lean` prints the axiom footprint).
- `experiments/wN-*/` — one folder per workstream: tools, raw outputs, `log.md` (chronology incl. dead ends),
  `proof.md` (statements + complete proofs). New workstreams get the next number and an entry in `experiments/README.md`.
- `memory/` — notes that persist across sessions. Keep `SESSION-STATE.md` current (agents, gaps, what is verified).
- `references/` — bibliography pointers only; do not commit third-party PDFs.

## Non-negotiable norms

1. **Verify before folding in.** Every theorem claimed by an agent is re-derived line by line by the main
   session; every numerical certificate is recomputed independently (ideally with separately written code);
   combinatorial lemmas are brute-forced per class where feasible. Only then does it enter the paper.
   Record the verification in `memory/SESSION-STATE.md`.
2. **Novelty check.** Before calling anything new, check it against `memory/NOTES.md`, `memory/priority-check.md`
   and the cited literature; state the prior best and the improvement magnitude in the paper's summary table.
3. **Dead ends are results.** Record failed approaches with the reason they fail, in the workstream `log.md`
   and (when instructive) in the paper.
4. **Reproducibility.** Every number in the paper points to the file/command that produced it. Digit strings,
   witnesses and certificates are stored verbatim in `experiments/` and, where possible, in Lean.
5. **Paper hygiene.** Citations via `references.bib` (`[@Key]`), section refs via `\S\ref{sec:...}`; run
   `make check` after every edit; render pages with `pdftoppm` and look before declaring done.

## Agents / workstreams

Poll workstreams by reading their files (`log.md`, `proof.md`, output tails), not transcripts. Kill stale
CPU-heavy searches (`uptime` load should stay below the core count); see the machine-hygiene notes in
`memory/SESSION-STATE.md`.

## Commits

Run `pre-commit install` once; hooks block large files, private keys and secrets. CI builds the Lean project,
builds/lints the paper, and scans for secrets. Do not commit `.lake/`, virtualenvs, compiled binaries or
third-party papers.
