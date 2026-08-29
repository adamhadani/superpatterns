# Superpatterns: bounds, constructions and random-permutation thresholds

Research notes, computations and formal proofs on **k-superpatterns** — permutations that contain every
permutation of length k as a pattern — and on the closely related question of when a *random* permutation
is a k-superpattern (Alon's conjecture). The work was carried out on 2026-08-29 as an LLM-assisted
research project: a coordinating session planned attack lines, spawned parallel workstreams, and
independently re-verified every claimed result before it entered the paper.

**Paper (work in progress):** [`output/paper/superpatterns-notes.pdf`](output/paper/superpatterns-notes.pdf)
(source: [`output/paper/superpatterns-notes.md`](output/paper/superpatterns-notes.md)).

## Main results (see the paper's summary table for prior bests and improvement magnitudes)

| Result | Previously | Here |
|:--|:--|:--|
| Lower bound sp(k) ≥ (λ − o(1)) k²/e² | λ = 1.000076 (Chroman–Kwan–Singhal) | λ = 1.0003125 (Theorem A, fully Lean-verified); λ = 1.00483 (Theorem C) |
| sp(7), sp(8) upper bounds | 25, 33 (Engen–Vatter) | 23, 30 (explicit witnesses, Lean `native_decide` certificates) |
| f(k; k+1) (words over an alphabet of size k+1) | ≤ (k²+k)/2 | = (k²+k)/2 for k ≤ 5 (Hunter's Problem 3) |
| Gupta rosaries r(n), odd n | < n²/2 + n/4 − 1 | = ⌊n²/2⌋ for n ≤ 5; ≤ ⌊n²/2⌋ for n ≤ 11 |
| Layered pattern constant c₂₁ | 0.40 ≤ c₂₁ ≤ e/2 | 0.787 ≤ c₂₁ ≤ 1.140; universal absence threshold κ = 2.279 |
| Alon's conjecture (random permutation of length (1/4+ε)k² is a k-superpattern) | 2000 k² log log k (He–Kwan) | partial results: 72k² for a much larger class than He–Kwan's; (π/8)k² for all block-grid patterns (tilted grids and the family that defeats the thread method); proof that the polylog-thread framework cannot reach O(k²) |

Negative results (dead ends with proofs) are recorded alongside the positive ones — see
`experiments/*/log.md` and the paper's "what cannot work" paragraphs.

## Repository layout

| Directory | Contents |
|:--|:--|
| `output/paper/` | The paper: Markdown source, `references.bib`, pandoc defaults, CSL, Makefile (`make pdf`, `make check` = overfull-box lint, must print 0), and the built PDF |
| `formal-verification/lean/` | Lean 4 + Mathlib project: pattern containment, a verified DFS checker, `native_decide` certificates for sp(7) ≤ 23 and sp(8) ≤ 30, and the complete formalisation of Theorem A (`#print axioms` → propext, Classical.choice, Quot.sound only). `LOG.md` documents every file and its status |
| `experiments/` | One folder per workstream (`w1-search` … `w18-lag`): C/Python tools, raw outputs, `log.md` (chronology, dead ends) and `proof.md` (theorem statements with full proofs). `experiments/README.md` indexes them |
| `memory/` | Living notes: `NOTES.md` (literature state and results), `SESSION-STATE.md` (live coordination state, verification norms, open gaps), `priority-check.md` (novelty check against the literature) |
| `references/` | Bibliography pointers (`README.md`); the papers/books themselves are not redistributed |
| `.claude/skills/` | Claude Code skills used in this repo (paper formatting rules that keep the PDF clean) |

## Reproducing

```sh
# Paper
cd output/paper && make pdf && make check        # needs pandoc ≥ 3, xelatex (TeX Live), citeproc

# Lean certificates and Theorem A
cd formal-verification/lean
lake exe cache get && lake build                 # Lean v4.33.1 / Mathlib v4.33.1 via elan
lake env lean Superpatterns/Axioms.lean          # prints the axioms each theorem depends on

# Experiments: each experiments/wN-*/log.md gives the exact compile/run lines (mostly `cc -O2 x.c` and python3)
```

## Verification norm

Every theorem claimed by a workstream was re-derived line by line by the coordinating session, every
numerical certificate was recomputed independently (often by a separately written program), and
combinatorial lemmas were brute-forced per class where feasible, *before* entering the paper. One
false lemma (an early draft of the value-slot refinement) was caught this way; the corrected version
is what appears.

## Citing

See `output/paper/references.bib` for the literature and the paper's summary table for exactly what is
new relative to each reference. If you use these results, please cite the paper (preprint forthcoming)
and this repository.

## License

MIT for code and Lean sources; CC BY 4.0 for the paper and notes.
