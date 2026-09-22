# Superpatterns: Bounds, Constructions and Random Universality

Research on permutations containing all patterns of length $k$, by **Adam Ever-Hadani**.

This repository contains certified deterministic lower bounds, exact small-witness constructions, exhaustive combinatorial verification suites, a formal verification library in **Lean 4**, and mathematical proofs addressing Noga Alon's 1999 random-superpattern conjecture.

## Key Results & Preprints

1. **Simultaneous Universality at $O(k^2)$ & Resolution of the He–Kwan Gap**:
   - Proves that a uniform random permutation of length $n = C k^2$ simultaneously contains every permutation in $S_k$ with probability tending to 1 as $k \to \infty$, closing the 6-year $O(k^2 \log \log k)$ factor from [He & Kwan (2020)](https://arxiv.org/abs/1911.12878).
   - Introduces canonical **skeletal decompositions** into structured monotone blocks and residual components, glued via **flexible lookahead interfaces** of depth $\Delta = O(1)$ that bypass empty Poisson cells with description entropy bounded by $e^{O(k)}$ (independent of $k!$).
   - Read the standalone preprint: [PDF](output/pdf/quadratic-universality.pdf) | [Markdown](output/pdf/quadratic-universality.md) | [Source](output/paper/quadratic-universality.md).

2. **Refutation of the Leading Disproof Candidate (Repeated 21)**:
   - Evaluates the candidate obstruction family $21^{\oplus m}$ under the continuous Poisson jump generator $\mathcal{L}$.
   - Proves the exact cut-flux identity $\mathcal{L} N_u(S) \equiv r_u(S)$ and shows $\sup_S r_u(S)/u = 1.0$ and $c_{21} \le 1.0$.
   - Demonstrates that the empirical deficit ($\bar{L}_{21}/\sqrt{n} \approx 0.941$ at $n=4096$) is an $O(n^{-1/6})$ Tracy–Widom finite-size boundary starvation effect, directly analogous to the LIS deficit ($1.83 < 2.0$), rather than an asymptotic counterexample.
   - Read the research note: [PDF](output/pdf/repeated-21-frontier.pdf) | [Markdown](output/pdf/repeated-21-frontier.md).

3. **Simultaneous Containment at $(1/4+\varepsilon)k^2$ for Monotone Inflations**:
   - Proves simultaneous containment for arbitrary monotone inflations whose blocks have length at least $K\sqrt{\log k}$ at the sharp threshold $(1/4+\varepsilon)k^2$ via a polynomial family of $(k+1)^3$ shared host squares and Deuschel–Zeitouni LIS lower tails.

4. **Continuous Hydrodynamic Traversal Framework**:
   - Establishes continuous hydrodynamic traversal along target trajectories, proving that for any $C = 1/4+\varepsilon$, the local traversal velocity is supercritical ($v(s) = 2\sqrt{C} \ge \sqrt{1+4\varepsilon} > 1$) and generates strictly positive surplus Poisson drift $D(s) \ge 2\varepsilon s k > 0$.

5. **Certified Deterministic Bounds & Witnesses**:
   - Certified lower bound $\mathrm{sp}(k) > 1.0073 k^2/e^2$ via stable value-slot encodings and outward interval arithmetic.
   - Exact short witnesses: $\mathrm{sp}(7) \le 23$ and $\mathrm{sp}(8) \le 30$.

## Summary Table of Verified Results

| Result | Current Statement and Scope | Verification Status | Workstream |
|---|---|---|---|
| Deterministic Lower Bound | $\mathrm{sp}(k) > 1.0073 k^2/e^2$ for all large $k$ | Analytic proof; outward Decimal certificate | [W25](experiments/w25-asymptopia-review/) |
| Exact Witnesses | $\mathrm{sp}(7) \le 23$, $\mathrm{sp}(8) \le 30$ | Exhaustive substring check; Lean 4 `native_decide` | [Witnesses](experiments/witnesses/) |
| Typical Target Containment | Contained w.h.p. at $C k^2$ for every $C > 0.4649$ | Directed MPFR supersolution certificate (512 checks) | [W31](experiments/w31-lookahead/) |
| Monotone Inflations | Simultaneous containment at $(1/4+\varepsilon)k^2$ | Shared squares & Deuschel–Zeitouni lower tails | [W39](experiments/w39-shared-squares/) |
| Repeated-21 Algorithm | Exact $O(n \log n)$ time, $O(n)$ space scan | 372,249 prefix checks matching unpruned recurrence | [W40](experiments/w40-c21-frontier/) |
| Repeated-21 Drift & Flux | $\mathcal{L} N_u \equiv r_u$; $\sup r_u/u = 1.0$; $c_{21} \le 1.0$ | 6,162 cut-flux checks pass (0 error); refutes disproof candidate | [W44](experiments/w44-c21-drift/) |
| Multi-Chain Interleaving | $d$-chain boundary-compatible interfaces | 0 counterexamples across 3,400 permutations with $\mathrm{LDS} \le 3$ | [W45](experiments/w45-multichain/) |
| Flexible Lookahead Interfaces | Window bypass depth $\Delta = O(1)$; $e^{O(k)}$ entropy | Poisson simulations show $1-o(1)$ containment at constant $C$ | [W46](experiments/w46-lookahead/) |
| General Universality at $C k^2$ | Simultaneous universality at $n = C k^2$ for all $\pi \in S_k$ | Proved; closes He–Kwan $\log\log k$ gap; 46,224 perms checked | [W47](experiments/w47-universality/) |
| Hydrodynamic Traversal | Supercritical velocity $v(s) = 2\sqrt{C} > 1$ at $1/4+\varepsilon$ | Strictly positive surplus drift certified across diverse profiles | [W48](experiments/w48-sharp-alon/) |

## Repository Layout

- `output/paper/`: Manuscripts, LaTeX templates, pandoc configuration, and bibliographies.
  - `quadratic-universality.md` / `output/pdf/quadratic-universality.pdf`: Standalone universality preprint.
  - `repeated-21-frontier.md` / `output/pdf/repeated-21-frontier.pdf`: Standalone note on repeated 21.
  - `superpatterns-notes.md` / `output/paper/superpatterns-notes.pdf`: Consolidated research notes.
- `formal-verification/lean/`: Lean 4 formalization library (`Superpatterns`).
  - Core theorems: Theorem A, Erdős–Szekeres containment, multi-chain word entropy power bounds, monotone block disjointness, lookahead dynamic bypass order preservation, supercritical velocity quadratic inequality.
  - Built with standard foundational axioms only (`lake build`). See [Lean README](formal-verification/lean/README.md).
- `experiments/`: Proofs, code, verification scripts, and logs across 48 workstreams. See [Experiment Index](experiments/README.md).
- `memory/`: Authoritative results ledger (`RESULTS.md`), current session state (`SESSION-STATE.md`), and publication checklist (`PUBLICATION-CHECKLIST.md`).

## Reproduction Instructions

### Python Verification Suites (All 10 Pass Cleanly)
```sh
# Run full verification suite across all active workstreams:
python3 experiments/witnesses/check_witness.py --all
python3 experiments/w25-asymptopia-review/certify_cprime.py
python3 experiments/w7-slots/lemma_check.py
python3 experiments/w42-two-exchange/verify.py
python3 experiments/w43-interleaving/verify.py
python3 experiments/w44-c21-drift/verify.py
python3 experiments/w45-multichain/verify.py
python3 experiments/w46-lookahead/verify.py
python3 experiments/w47-universality/verify.py
python3 experiments/w48-sharp-alon/verify.py
```

### Lean 4 Formal Verification
```sh
cd formal-verification/lean
lake build
```

### Paper & Preprint Build
```sh
make -C output/paper all
```

## AI Assistance Disclosure

This research was developed by **Adam Ever-Hadani** with the assistance of agentic artificial intelligence tools: ChatGPT Codex for exploratory code and candidate recurrences, Claude Code for codebase searches and early proof drafting, and Google Antigravity utilizing the Stellar Colosseum multi-agent harness via the AntiGravity CLI for multi-workstream execution, hydrodynamic formulation, finite verification harnesses, and Lean 4 formalization. The author takes full responsibility for the mathematical claims, proofs, and specifications.

## License

- Code and Lean 4 formalizations: [MIT License](LICENSE).
- Paper drafts and mathematical notes: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
