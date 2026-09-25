# Original User Request

## 2026-09-22T16:05:58Z

Use a very large team of agents.

Advance the proof route for Noga Alon's $k$-superpattern conjecture towards general simultaneous universality at $C k^2$ for an absolute constant $C$, by launching Workstream W45: Multi-Chain Interleaving Extension, generalizing W43's boundary-compatible interface mechanism from 2 chains to $d$ chains ($d \ge 3$, focusing on $\operatorname{LDS} \le 3$ and general $d$-chain decompositions).

Working directory: `/Users/adamhadani/Development/math-proofs/superpatterns`
Integrity mode: development

Reference material:
- [experiments/w43-interleaving/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w43-interleaving/proof.md)
- [experiments/w43-interleaving/log.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w43-interleaving/log.md)
- [experiments/w39-shared-squares/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w39-shared-squares/proof.md)
- [output/paper/repeated-21-frontier.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/paper/repeated-21-frontier.md)
- [memory/ALON-STRATEGY.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/memory/ALON-STRATEGY.md)
- [CLAUDE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/CLAUDE.md)
- He–Kwan (2020), "Universality of random permutations", arXiv:1911.12878

## Requirements

### R1. Multi-Chain Boundary-Compatible Embedding Theory
Formulate a general $d$-chain boundary-compatible embedding lemma that establishes coordinate track reservations $I_x(t) \times I_y(\pi(t))$ and entrance/exit boundary specifications for permutations partitioned into $d$ strictly increasing chains $M_1, \dots, M_d$ ($\operatorname{LDS}(\pi) \le d$, including 4321-avoiding permutations for $d=3$). Quantify the interface entropy for fixed $d$ and evaluate the common host event $E_{\mathrm{host}}$ on a Poisson host $\Pi_{C k^2}$ guaranteeing simultaneous containment without a $k!$ union bound.

### R2. Exhaustive Combinatorial Verification
Implement an automated combinatorial verification tool (e.g. in `experiments/w45-multichain/verify.py`) to systematically enumerate permutations with $\operatorname{LDS} \le 3$ in $S_k$ (for $k \in \{4, 5, 6, 7\}$) using Greene / Patience sorting with 3 piles, testing that the multi-chain coordinate reservation guarantees 0 boundary collisions and 0 ordering dead ends on discrete host grids across all valid interleavings.

### R3. Non-Negotiable Repo Norms & No Regressions
Strictly adhere to repo norms in `CLAUDE.md`: no unverified claims, no heuristic limits treated as proved theorems, no hidden $k!$ union bounds. Ensure 0 regressions across all existing test suites:
- `python3 experiments/witnesses/check_witness.py --all`
- `python3 experiments/w25-asymptopia-review/certify_cprime.py`
- `python3 experiments/w7-slots/lemma_check.py`
- `python3 experiments/w42-two-exchange/verify.py`
- `python3 experiments/w43-interleaving/verify.py`
- `python3 experiments/w44-c21-drift/verify.py`
- `make -C output/paper check`

### R4. Complete Research Documentation
Record formal mathematical statements, multi-chain decompositions, and complete proofs in `experiments/w45-multichain/proof.md`, maintain an audit trail in `experiments/w45-multichain/log.md`, register W45 in `experiments/README.md`, and update `memory/SESSION-STATE.md` and `memory/RESULTS.md`.

## Acceptance Criteria

### Automated Combinatorial & Mathematical Verification
- [ ] Multi-chain boundary-compatible embedding lemma is formulated with explicit coordinate tracks and entropy quantification for $d$ chains.
- [ ] Automated verification script verifies 0 counterexamples across all permutations with $\operatorname{LDS} \le 3$ for $k \in \{4, 5, 6, 7\}$ on host occupancy grids.
- [ ] All 7 regression checks pass with 0 failures:
  - `check_witness.py --all`
  - `certify_cprime.py`
  - `lemma_check.py`
  - `w42-two-exchange/verify.py`
  - `w43-interleaving/verify.py`
  - `w44-c21-drift/verify.py`
  - `w45-multichain/verify.py`
- [ ] LaTeX documents and technical notes compile with 0 errors and 0 overfull boxes (`make -C output/paper check` passes).
- [ ] `memory/SESSION-STATE.md` and `memory/RESULTS.md` are updated to document findings and the bridge to general $C k^2$ universality.

## 2026-09-22T16:18:17Z

Use a very large team of agents.

Advance the proof route for Noga Alon's $k$-superpattern conjecture towards general simultaneous universality at $C k^2$ for an absolute constant $C$, by launching Workstream W46: Flexible Lookahead Interfaces at $C k^2$, overcoming the Poisson void obstruction in rigid coordinate grids.

Working directory: `/Users/adamhadani/Development/math-proofs/superpatterns`
Integrity mode: development

Reference material:
- [experiments/w45-multichain/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w45-multichain/proof.md)
- [experiments/w43-interleaving/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w43-interleaving/proof.md)
- [experiments/w39-shared-squares/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w39-shared-squares/proof.md)
- [experiments/w34-grid-lookahead/reduction.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w34-grid-lookahead/reduction.md)
- [experiments/w36-gamma-limit/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w36-gamma-limit/proof.md)
- [CLAUDE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/CLAUDE.md)
- He–Kwan (2020), "Universality of random permutations", arXiv:1911.12878

## Requirements

### R1. Flexible Interface with Lookahead & Poisson Void Resolution
Formulate a Flexible Boundary-Compatible Embedding Lemma with lookahead parameter $\Delta = O(1)$ that replaces rigid cell occupancy with flexible window traversal: target points $(t, \pi(t))$ are allocated horizontal/vertical coordinate windows $[x^{\mathrm{in}}(t), x^{\mathrm{in}}(t) + \Delta]$ and $[y^{\mathrm{in}}(v), y^{\mathrm{in}}(v) + \Delta]$ such that an empty cell in a Poisson host with constant intensity $C$ is bypassed without violating relative coordinate ordering. Prove that the failure probability of the flexible host event $E_{\mathrm{host}}^{\mathrm{flex}}$ vanishes as $k \to \infty$ at host size $n = C k^2$ for an absolute constant $C$, with total interface entropy bounded by $e^{O(k)}$.

### R2. Empirical & Discrete Combinatorial Verification Tool
Implement an automated verification tool in `experiments/w46-lookahead/verify.py` that simulates Poisson hosts of size $n = C k^2$ across varying constants $C \in \{5, 10, 20\}$ and lookahead depths $\Delta \in \{1, 2, 3, 4\}$. Systematically evaluate the empirical success probability of embedding 4321-avoiding permutations ($\operatorname{LDS} \le 3$, 3,400 permutations) under flexible lookahead versus rigid grid embedding, demonstrating that lookahead $\Delta \ge 2$ eliminates void failures and achieves probability $1 - o(1)$ at constant $C$.

### R3. Non-Negotiable Repo Norms & No Regressions
Strictly respect repo norms in `CLAUDE.md`: do not mistake $4k^2 e^{-C/4}$ for $o(1)$ at constant $C$; treat Poisson void cells rigorously. Ensure 0 regressions across all 7 existing regression test suites (`check_witness.py`, `certify_cprime.py`, `lemma_check.py`, `w42-two-exchange/verify.py`, `w43-interleaving/verify.py`, `w44-c21-drift/verify.py`, `w45-multichain/verify.py`) and paper check (`make -C output/paper check`).

### R4. Complete Research Documentation
Record formal mathematical statements, window definitions, and complete proofs in `experiments/w46-lookahead/proof.md`, maintain an audit trail in `experiments/w46-lookahead/log.md`, register W46 in `experiments/README.md`, and update `memory/SESSION-STATE.md` and `memory/RESULTS.md`.

## Acceptance Criteria

### Automated Combinatorial & Mathematical Verification
- [ ] Formulate the Flexible Boundary-Compatible Embedding Lemma with explicit lookahead parameter $\Delta = O(1)$ and bounded interface entropy $e^{O(k)}$.
- [ ] Prove that the flexible host event $E_{\mathrm{host}}^{\mathrm{flex}}$ achieves probability $1 - o(1)$ at host size $n = C k^2$ for constant $C$.
- [ ] Automated verification script verifies empirical success of flexible embedding vs rigid embedding across all 3,400 permutations in $S_k$ with $\operatorname{LDS} \le 3$ ($k \in \{4, 5, 6, 7\}$).
- [ ] All existing regression checks pass with 0 failures:
  - `check_witness.py --all`
  - `certify_cprime.py`
  - `lemma_check.py`
  - `w42-two-exchange/verify.py`
  - `w43-interleaving/verify.py`
  - `w44-c21-drift/verify.py`
  - `w45-multichain/verify.py`
- [ ] LaTeX documents and technical notes compile with 0 errors and 0 overfull boxes (`make -C output/paper check` passes).
- [ ] `memory/SESSION-STATE.md` and `memory/RESULTS.md` are updated.

## 2026-09-22T16:34:18Z

Use a very large team of agents.

Advance the proof route for Noga Alon's $k$-superpattern conjecture by launching Workstream W47: General Simultaneous Universality at $C k^2$, proving that a random permutation of length $n = C k^2$ simultaneously contains every $\pi \in S_k$ with probability tending to 1 for an absolute constant $C$, closing the $\log \log k$ factor from He–Kwan (2020).

Working directory: `/Users/adamhadani/Development/math-proofs/superpatterns`
Integrity mode: development

Reference material:
- [experiments/w46-lookahead/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w46-lookahead/proof.md)
- [experiments/w45-multichain/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w45-multichain/proof.md)
- [experiments/w39-shared-squares/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w39-shared-squares/proof.md)
- [experiments/w34-grid-lookahead/reduction.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w34-grid-lookahead/reduction.md)
- [CLAUDE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/CLAUDE.md)
- He–Kwan (2020), "Universality of random permutations", arXiv:1911.12878

## Requirements

### R1. General Simultaneous Universality Theorem at $C k^2$
Formulate and prove the General Simultaneous Universality Theorem at $C k^2$: establish a skeletal decomposition theorem partitioning any arbitrary $\pi \in S_k$ into structured monotone blocks (handled via W39 shared squares) and residual quasirandom components (handled via W46 flexible lookahead interfaces). Prove that the interface gluing preserves boundary coordinate ordering without dead ends, with total description entropy bounded by $e^{O(k)}$ on a single common host event $E_{\mathrm{host}}^{\mathrm{univ}}$ of probability $1 - o(1)$ at host size $n = C k^2$ for an absolute constant $C$.

### R2. Automated Combinatorial & Gluing Verification Tool
Implement an automated verification tool in `experiments/w47-universality/verify.py` that systematically tests the combined gluing of structured inflations and flexible lookahead threads across arbitrary permutations in $S_k$ for $k \in \{4, 5, 6, 7, 8\}$, verifying that no target permutation experiences coordinate ordering collisions or residual boundary conflicts.

### R3. Non-Negotiable Repo Norms & No Regressions
Strictly respect repo norms in `CLAUDE.md`: no hidden $k!$ union bounds, no unproved heuristic limits, and exact boundary compatibility. Ensure 0 regressions across all 8 existing regression test suites (`check_witness.py`, `certify_cprime.py`, `lemma_check.py`, `w42-two-exchange/verify.py`, `w43-interleaving/verify.py`, `w44-c21-drift/verify.py`, `w45-multichain/verify.py`, `w46-lookahead/verify.py`) and paper check (`make -C output/paper check`).

### R4. Complete Research Documentation
Record formal mathematical statements, skeletal decomposition definitions, and complete proofs in `experiments/w47-universality/proof.md`, maintain an audit trail in `experiments/w47-universality/log.md`, register W47 in `experiments/README.md`, and update `memory/SESSION-STATE.md` and `memory/RESULTS.md`.

## Acceptance Criteria

### Automated Combinatorial & Mathematical Verification
- [ ] General Simultaneous Universality Theorem at $C k^2$ is fully proved in `proof.md` with explicit skeletal gluing and $e^{O(k)}$ host entropy bound.
- [ ] Automated verification script verifies zero boundary collisions and complete embedding success across arbitrary permutations in $S_k$ ($k \in \{4, 5, 6, 7, 8\}$).
- [ ] All 8 existing regression checks pass with 0 failures:
  - `check_witness.py --all`
  - `certify_cprime.py`
  - `lemma_check.py`
  - `w42-two-exchange/verify.py`
  - `w43-interleaving/verify.py`
  - `w44-c21-drift/verify.py`
  - `w45-multichain/verify.py`
  - `w46-lookahead/verify.py`
- [ ] LaTeX documents and technical notes compile with 0 errors and 0 overfull boxes (`make -C output/paper check` passes).
- [ ] `memory/SESSION-STATE.md` and `memory/RESULTS.md` are updated to document the $C k^2$ general universality theorem.

## 2026-09-22T16:54:28Z

Use a very large team of agents.

Advance the proof route for Noga Alon's $k$-superpattern conjecture towards the full sharp threshold $n = \lceil(1/4+\varepsilon)k^2\rceil$ by launching Workstream W48: Sharp Constant Compression ($C \to 1/4$) via Hydrodynamic Coupling.

Working directory: `/Users/adamhadani/Development/math-proofs/superpatterns`
Integrity mode: development

Reference material:
- [experiments/w47-universality/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w47-universality/proof.md)
- [experiments/w46-lookahead/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w46-lookahead/proof.md)
- [experiments/w39-shared-squares/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w39-shared-squares/proof.md)
- [experiments/w36-gamma-limit/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w36-gamma-limit/proof.md)
- [experiments/w34-grid-lookahead/reduction.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w34-grid-lookahead/reduction.md)
- [output/paper/repeated-21-frontier.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/paper/repeated-21-frontier.md)
- [CLAUDE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/CLAUDE.md)
- He–Kwan (2020), "Universality of random permutations", arXiv:1911.12878

## Requirements

### R1. Hydrodynamic Traversal Theory & Sharp $1/4$ Constant Compression
Formulate and prove the Sharp Constant Compression Theorem: establish a continuous hydrodynamic coupling between the skeletal monotone inflations (which achieve $(1/4+\varepsilon)k^2$ via W39 shared squares and Deuschel–Zeitouni LIS lower tails) and the residual lookahead threads. Prove that allocating host density according to the target trajectory density profile yields a local traversal rate $v(s) = 2\sqrt{C} \ge \sqrt{1 + 4\varepsilon} = 1 + 2\varepsilon - O(\varepsilon^2) > 1$ whenever $C = 1/4 + \varepsilon$. Prove that surplus Poisson point concentration bounds the simultaneous failure probability over all interface paths by $e^{-\Omega(\varepsilon^2 k)} = o(1)$ on a single common host event $E_{\mathrm{host}}^{1/4}$.

### R2. Automated Empirical & Hydrodynamic Verification Tool
Implement an automated verification tool in `experiments/w48-sharp-alon/verify.py` that simulates continuous Poisson host processes at intensities $C \in \{0.26, 0.28, 0.30, 0.35, 0.50\}$ across diverse target profiles in $S_k$ ($k \in \{10, 20, 50, 100\}$). Systematically measure the surplus drift $D(s) = N(s) - \lfloor s k \rfloor$ along the optimal hydrodynamic paths, verifying that the empirical surplus drift remains strictly positive and bounded away from zero for all $C \ge 1/4 + \varepsilon$.

### R3. Non-Negotiable Repo Norms & No Regressions
Strictly adhere to repo norms in `CLAUDE.md`: no heuristic limits treated as proved thresholds, no hidden $k!$ union bounds, and explicit hydrodynamic drift bounds. Ensure 0 regressions across all 9 existing regression test suites (`check_witness.py`, `certify_cprime.py`, `lemma_check.py`, `w42-two-exchange/verify.py`, `w43-interleaving/verify.py`, `w44-c21-drift/verify.py`, `w45-multichain/verify.py`, `w46-lookahead/verify.py`, `w47-universality/verify.py`), Lean 4 build (`lake build`), and paper check (`make -C output/paper check`).

### R4. Complete Research Documentation
Record formal mathematical statements, hydrodynamic trajectory equations, surplus drift bounds, and complete proofs in `experiments/w48-sharp-alon/proof.md`, maintain an audit trail in `experiments/w48-sharp-alon/log.md`, register W48 in `experiments/README.md`, and update `memory/SESSION-STATE.md` and `memory/RESULTS.md`.

## Acceptance Criteria

### Automated Combinatorial & Mathematical Verification
- [ ] Sharp Constant Compression Theorem is proved in `proof.md`, establishing the surplus traversal velocity $2\sqrt{C} > 1$ at $C = 1/4 + \varepsilon$ with $e^{-\Omega(\varepsilon^2 k)}$ surplus concentration.
- [ ] Automated verification script verifies strictly positive surplus drift across continuous Poisson host simulations for $C > 0.25$ on targets up to $k=100$.
- [ ] All 9 existing regression checks pass with 0 failures:
  - `check_witness.py --all`
  - `certify_cprime.py`
  - `lemma_check.py`
  - `w42-two-exchange/verify.py`
  - `w43-interleaving/verify.py`
  - `w44-c21-drift/verify.py`
  - `w45-multichain/verify.py`
  - `w46-lookahead/verify.py`
  - `w47-universality/verify.py`
  - `w48-sharp-alon/verify.py`
- [ ] Lean 4 project builds cleanly (`lake build`).
- [ ] LaTeX documents and technical notes compile with 0 errors and 0 overfull boxes (`make -C output/paper check` passes).
- [ ] `memory/SESSION-STATE.md` and `memory/RESULTS.md` are updated to document the full resolution of Noga Alon's conjecture.

## 2026-09-22T18:01:13Z

Use a very large team of agents.

Advance the proof of Noga Alon's $k$-superpattern conjecture by launching Workstream W49: Multi-Scale Dyadic Chaining for Arbitrary Targets at $(1/4+\varepsilon)k^2$, closing the remaining gap between the continuous hydrodynamic traversal rate ($v(s) = 2\sqrt{C} > 1$) and discrete interface lookahead bypass across microscopic blocks to prove the sharp threshold $n = \lceil(1/4+\varepsilon)k^2\rceil$ for all $k!$ permutations simultaneously.

Working directory: `/Users/adamhadani/Development/math-proofs/superpatterns`
Integrity mode: development

Reference material:
- [output/pdf/quadratic-universality.pdf](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/pdf/quadratic-universality.pdf)
- [output/paper/quadratic-universality.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/paper/quadratic-universality.md)
- [experiments/w48-sharp-alon/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w48-sharp-alon/proof.md)
- [experiments/w47-universality/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w47-universality/proof.md)
- [experiments/w46-lookahead/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w46-lookahead/proof.md)
- [experiments/w39-shared-squares/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w39-shared-squares/proof.md)
- [CLAUDE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/CLAUDE.md)
- He–Kwan (2020), "Universality of random permutations", arXiv:1911.12878

## Requirements

### R1. Multi-Scale Dyadic Chaining Theorem
Formulate and prove the Multi-Scale Dyadic Chaining Theorem: decompose any arbitrary target permutation $\pi \in S_k$ across dyadic spatial scales $j \in \{1, \dots, \lceil\log_2 k\rceil\}$. Prove that the macroscopic hydrodynamic surplus drift $D(s) \ge 2\varepsilon s k$ generated by coarse-scale trajectory tracking dominates the cumulative discrete boundary discretization penalty $\sum_{j=1}^{\lceil\log_2 k\rceil} O(2^{-j/2} k) = O(k)$ from fine-scale lookahead bypass. Show that the simultaneous failure probability over all $k!$ interface paths decays as $e^{-\Omega(\varepsilon^2 k)} = o(1)$ on a single common host event $E_{\mathrm{host}}^{1/4}$ at host size $n = \lceil(1/4+\varepsilon)k^2\rceil$ for every fixed $\varepsilon > 0$.

### R2. Automated Empirical Chaining & Boundary Verification Tool
Implement an automated verification tool in `experiments/w49-multiscale-chaining/verify.py` that simulates continuous Poisson host processes at intensities $C \in \{0.26, 0.28, 0.30\}$ across worst-case adversarial fine-block permutations (including rapid oscillations, Cantor-like fractals, and high-frequency alternating words in $S_k$ for $k \in \{20, 50, 100, 200\}$). Systematically verify that the cumulative multi-scale surplus remains strictly positive at all scales and that zero interface collisions occur across all test instances.

### R3. Non-Negotiable Repo Norms & No Regressions
Strictly adhere to repo norms in `CLAUDE.md`: no heuristic limits treated as proved thresholds, no hidden $k!$ union bounds, and explicit dyadic chaining convergence bounds. Ensure 0 regressions across all 10 existing regression test suites (`check_witness.py`, `certify_cprime.py`, `lemma_check.py`, `w42-two-exchange/verify.py`, `w43-interleaving/verify.py`, `w44-c21-drift/verify.py`, `w45-multichain/verify.py`, `w46-lookahead/verify.py`, `w47-universality/verify.py`, `w48-sharp-alon/verify.py`), Lean 4 build (`lake build`), and paper check (`make -C output/paper check`).

### R4. Complete Research Documentation & Paper Update
Record formal mathematical statements, dyadic decomposition equations, chaining bounds, and complete proofs in `experiments/w49-multiscale-chaining/proof.md`, maintain an audit trail in `experiments/w49-multiscale-chaining/log.md`, register W49 in `experiments/README.md`, update `memory/SESSION-STATE.md` and `memory/RESULTS.md`, and update `output/paper/quadratic-universality.md` and `superpatterns-notes.md` with the full resolution of Noga Alon's conjecture at $(1/4+\varepsilon)k^2$.

## Acceptance Criteria

### Automated Combinatorial & Mathematical Verification
- [ ] Multi-Scale Dyadic Chaining Theorem is proved in `proof.md`, showing coarse-scale surplus $\ge 2\varepsilon k$ absorbs fine-scale lookahead penalty $\sum_j O(2^{-j/2} k)$ to yield simultaneous failure probability $e^{-\Omega(\varepsilon^2 k)} = o(1)$ at $n = \lceil(1/4+\varepsilon)k^2\rceil$.
- [ ] Automated verification script verifies strictly positive surplus across dyadic scales on adversarial fine-block permutations up to $k=200$ with zero boundary collisions.
- [ ] All 10 existing regression checks pass with 0 failures:
  - `check_witness.py --all`
  - `certify_cprime.py`
  - `lemma_check.py`
  - `w42-two-exchange/verify.py`
  - `w43-interleaving/verify.py`
  - `w44-c21-drift/verify.py`
  - `w45-multichain/verify.py`
  - `w46-lookahead/verify.py`
  - `w47-universality/verify.py`
  - `w48-sharp-alon/verify.py`
- [ ] Lean 4 project builds cleanly (`lake build`).
- [ ] LaTeX documents and technical notes compile with 0 errors and 0 overfull boxes (`make -C output/paper check` passes).
- [ ] `memory/SESSION-STATE.md`, `memory/RESULTS.md`, and paper manuscripts are updated to document the unconditional resolution of Noga Alon's conjecture for all permutations in $S_k$.

## 2026-09-25T08:06:17Z

Use a very large team of agents.

Execute Workstream W80: Large-Scale Adversarial Red-Team Audit for Full-Generality Sharp Superpattern Universality on the paper "Simultaneous Universality of Random Permutations at Quadratic Host Size" and its accompanying Lean 4 formalization.

Working directory: `/Users/adamhadani/Development/math-proofs/superpatterns`
Integrity mode: development

Reference material:
- [output/paper/quadratic-universality.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/paper/quadratic-universality.md)
- [output/arxiv/main.tex](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/arxiv/main.tex)
- [output/arxiv/main.pdf](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/arxiv/main.pdf)
- [formal-verification/lean/Superpatterns/](file:///Users/adamhadani/Development/math-proofs/superpatterns/formal-verification/lean/Superpatterns/)
- [memory/SESSION-STATE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/memory/SESSION-STATE.md)
- [memory/RESULTS.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/memory/RESULTS.md)
- [CLAUDE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/CLAUDE.md)

## Requirements

### R1. Adversarial Claim-vs-Proof Cross-Audit
Perform a rigorous, adversarial cross-check between what the paper claims to prove vs. what is mathematically established:
1. Distinguish precisely between:
   (a) Unconditional simultaneous universality at quadratic host length C_0 k^2 (C_0 approx 9.62, Theorem 1.2 / Lean theoremA),
   (b) Unconditional sharp threshold C* = 1/4 for structured classes (Theorems 1.3–1.5),
   (c) Full-generality sharp threshold C* = 1/4 for arbitrary generic bulk permutations in S_k,
   (d) Machine-checked Lean 4 theorems vs. pen-and-paper functional-analytic proofs.
2. Flag any sentence, abstract claim, or theorem statement where the scope might be construed as conflating (a), (b), and (c), or where asymptotic constants/dependencies are underspecified.

### R2. Stress-Testing the Generic Bulk Reduction Chain
Attack each link in the generic bulk proof chain (n = ceil((1/4 + eps) k^2)):
1. Poset Decomposition: Can adversarial permutations generate Dilworth chain structures that evade Greene's shape bound or violate forward descent preservation?
2. Macroscopic Grid Concentration (M x M): Verify that Hoeffding bounds hold uniformly over all M^2 cells simultaneously and that cell vacancy probability does not accumulate across chains.
3. Cross-Cell Boundary Buffer Allocation: Test whether the track reservation w = 1/(d M) guarantees collision-free traversal under all corner cases (e.g. chains entering and exiting adjacent cell boundaries in dense configurations).
4. Continuum Variational LDP & Euler-Lagrange Minimality: Rigorously scrutinize Theorem 7.23 (Rate Minimality I(rho*_bulk) >= I(rho*_id) = c(eps) > 0). Could a non-monotone target profile permit a localized depletion of measure with rate strictly less than c(eps)?
5. Master Sieve Domination: Verify that the finite-scale crossover k_0(eps) where k! exp(-c(eps) k^2) < 1 is well-defined and has no hidden k-dependent prefactors in the exponent.

### R3. Lean 4 Formalization Alignment & Axiom Scrutiny
1. Audit every theorem in formal-verification/lean/Superpatterns/ referenced in the paper:
   - Verify that theorem names, hypotheses, and conclusions in the LaTeX text match the Lean definitions byte-for-byte.
   - Check the axiom dependency of every theorem (#print axioms), confirming that no unproved assumptions or unintentional circularities exist.
   - Catalog exactly which steps of the proof pipeline are fully verified in Lean 4 vs. which rely on pen-and-paper functional analysis (e.g., continuum measure LDP).

### R4. Actionable Backlog & Delegation Blueprint
Synthesize all findings into a prioritized, concrete action backlog:
- Categorize each flagged item: [CRITICAL GAP], [EXPOSITION MISALIGNMENT], [LEAN EXPANSION CANDIDATE], or [POLISH/HARDENING].
- Provide concrete specification prompts for any item requiring resolution, ready to be immediately delegated to Gemini 3.1 Pro subagents.

## Acceptance Criteria

### Automated Combinatorial & Mathematical Verification
- [ ] Deliverable experiments/w80-redteam-audit/adversarial_audit_report.md is authored, comprehensive, and catalogs all findings across R1–R4.
- [ ] Every theorem statement in output/arxiv/main.tex and output/paper/quadratic-universality.md has an explicit, verified status badge (Proved Unconditional / Proved Sharp for Class / Machine-Checked Lean 4 / Variational Reduction).
- [ ] All 13 core regression test suites pass with 0 errors (check_witness.py, certify_cprime.py, w76-multichain-grid/verify.py, w77-variational-ldp/verify.py, w78-greene-poset/verify.py, etc.).
- [ ] Lean 4 build compiles with 0 errors, 0 warnings, and 0 sorrys (lake build).
- [ ] output/arxiv/main.pdf compiles with 0 overfull boxes.


## 2026-09-25T10:36:24Z

Use a very large team of agents.

Execute Workstream W85: Post-Synthesis Adversarial Red-Team Audit & Stress-Testing on the finalized proof of Noga Alon's 1999 random superpattern conjecture at the sharp threshold $C^* = 1/4 = 0.25000$ in full generality, as presented in the paper "Simultaneous Universality of Random Permutations at Quadratic Host Size" and its accompanying Lean 4 formalization.

Working directory: `/Users/adamhadani/Development/math-proofs/superpatterns`
Integrity mode: development

Reference material:
- [output/paper/quadratic-universality.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/paper/quadratic-universality.md)
- [output/arxiv/main.tex](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/arxiv/main.tex)
- [output/arxiv/main.pdf](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/arxiv/main.pdf)
- [formal-verification/lean/Superpatterns/](file:///Users/adamhadani/Development/math-proofs/superpatterns/formal-verification/lean/Superpatterns/)
- [experiments/w84-track-buffers/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w84-track-buffers/proof.md)
- [experiments/w83-permuton-bundles/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w83-permuton-bundles/proof.md)
- [experiments/w80-redteam-audit/adversarial_audit_report.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w80-redteam-audit/adversarial_audit_report.md)
- [memory/SESSION-STATE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/memory/SESSION-STATE.md)
- [memory/RESULTS.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/memory/RESULTS.md)
- [CLAUDE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/CLAUDE.md)

## Requirements

### R1. Adversarial Stress-Testing of the Permuton Bundle & Track Buffer Architecture
Scrutinize and attempt to break the newly synthesized W83–W84 Generic Bulk architecture:
1. **Adversarial Permutation Attack**: Systematically test candidate counterexamples against the Coordinate Track Buffer box allocation $B_i = I_{r(i), p(i)} \times J_{c(i), q(i)}$:
   - High-frequency alternating permutations (e.g. $2, 1, 4, 3, 6, 5, \dots$).
   - Reverse identity ($\pi(i) = k - 1 - i$).
   - Cantor-like fractal permutations and recursive block structures.
   - Dense multi-point cells where $m_{r, s} = \Omega(\sqrt{k})$.
   Verify whether track buffer separation strictly prevents coordinate inversions and track collisions under all possible adverse geometries.
2. **Macroscopic Corridor Network Rate Lower Bound**:
   Rigorously scrutinize the continuous large deviation rate lower bound $I(\rho_T) \ge c(\varepsilon) > 0$ for coarse trajectory matrices $T \in \mathcal{T}_k$:
   - Verify that $\operatorname{Area}(T) \ge 1/4$ holds uniformly for all admissible target trajectories.
   - Check whether any singular measure concentration could deplete capacity along target paths while keeping $I(\rho) < c(\varepsilon)$.
3. **Master Sieve Convergence & Crossover Rigor**:
   Evaluate the two-term master sieve bound:
   $$
   \Pr(\exists \pi \in S_k : \pi \not\le \Pi_n) \le |\mathcal{T}_k| \exp(-c(\varepsilon) k^2) + M^2 \exp(-\Omega(k \ln k)).
   $$
   Verify that the crossover scale $k_0(\varepsilon)$ is strictly finite and that no polynomial prefactors or dimension factors overturn the asymptotic decay for any $\varepsilon > 0$.

### R2. Lean 4 Machine-Certification Audit
Perform an exhaustive verification of the formal Lean 4 codebase:
1. Audit all 3 newly added theorems in `Superpatterns/Interleaving.lean`:
   - `intra_row_track_separation`
   - `cross_row_track_separation`
   - `track_buffer_order_fidelity`
   Confirm that they prove the exact mathematical assertions needed for coordinate order preservation without hidden premises or trivialized hypotheses.
2. Audit `#print axioms` across all declarations in `Superpatterns/Axioms.lean`, verifying zero custom axioms and zero `sorry`s.
3. Verify that `lake build` executes cleanly with 0 warnings across all jobs.

### R3. Manuscript Coherence & Journal Submission Readiness Audit
1. Audit `output/arxiv/main.tex` and `output/paper/quadratic-universality.md`:
   - Verify that Section 1, Section 7.5, and Section 7.6 are fully harmonized.
   - Confirm that theorem statements, equations, and cross-references match the formalized mathematics.
   - Verify that all literature citations (He–Kwan 2020, Altschuler–Dubroff–Tikhomirov 2026, Marcus–Tardos 2004, Deuschel–Zeitouni 1999) are accurate and fully integrated.
2. Verify that `output/arxiv/main.pdf` compiles cleanly with **EXACTLY 0 overfull boxes**.

### R4. Complete Audit Deliverables & Ledger Update
1. Create deliverable `experiments/w85-redteam-audit/adversarial_audit_report.md` documenting:
   - Comprehensive findings on each requirement.
   - Edge case stress test results.
   - Formal verification matrix.
   - Final readiness verdict for submission to *Annals of Mathematics*.
2. Implement automated stress-test script `experiments/w85-redteam-audit/verify.py` executing the adversarial permutation battery.
3. Update `memory/SESSION-STATE.md`, `memory/RESULTS.md`, and `experiments/README.md`.

## Acceptance Criteria

### Automated Combinatorial & Mathematical Verification
- [ ] Deliverable `experiments/w85-redteam-audit/adversarial_audit_report.md` is authored, comprehensive, and catalogs all findings across R1–R4.
- [ ] Automated stress-test script `experiments/w85-redteam-audit/verify.py` passes all edge case checks with exit code 0.
- [ ] All existing regression test suites pass with 0 errors:
  - `python3 experiments/witnesses/check_witness.py --all`
  - `python3 experiments/w25-asymptopia-review/certify_cprime.py`
  - `python3 experiments/w83-permuton-bundles/verify.py`
  - `python3 experiments/w84-track-buffers/verify.py`
  - `python3 experiments/w85-redteam-audit/verify.py`
- [ ] Lean 4 formalization compiles with 0 errors, 0 warnings, and 0 `sorry`s (`lake build`).
- [ ] `output/arxiv/main.pdf` compiles with 0 errors and EXACTLY 0 overfull boxes.
- [ ] `memory/SESSION-STATE.md` and `memory/RESULTS.md` are updated.

## 2026-09-25T11:55:45Z

Use a very large team of agents.

Execute Workstream W86: Multi-Scale Dynamic Lookahead Corridor Traversal & Fractal Gap Resolution at the sharp threshold $C^* = 1/4$ for Noga Alon's 1999 random superpattern conjecture.

Working directory: `/Users/adamhadani/Development/math-proofs/superpatterns`
Integrity mode: development

Reference material:
- [output/paper/quadratic-universality.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/paper/quadratic-universality.md)
- [output/arxiv/main.tex](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/arxiv/main.tex)
- [experiments/w85-redteam-audit/adversarial_audit_report.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w85-redteam-audit/adversarial_audit_report.md)
- [experiments/w84-track-buffers/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w84-track-buffers/proof.md)
- [experiments/w83-permuton-bundles/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w83-permuton-bundles/proof.md)
- [formal-verification/lean/Superpatterns/Interleaving.lean](file:///Users/adamhadani/Development/math-proofs/superpatterns/formal-verification/lean/Superpatterns/Interleaving.lean)
- [CLAUDE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/CLAUDE.md)

## Requirements

### R1. Dynamic Multi-Scale Lookahead Corridor Traversal Theory
Formulate and prove the Dynamic Multi-Scale Lookahead Corridor Traversal Lemma:
1. Replace static independent box occupancy ($B_i = I_{r, p} \times J_{c, q}$, where $\operatorname{Area}(B_i) \approx 1/k^2$ causes $67\%$ vacancy failure) with dynamic corridor traversal along the macroscopic trajectory $T$ of area $\operatorname{Area}(T) \ge 0.25$.
2. Define adaptive lookahead windows $W_t(\Delta)$ of depth $\Delta = \mathcal{O}(1)$ that bypass empty $1/k^2$ cells while preserving the Lean-certified Coordinate Track Buffer ordering ($X_i < X_j \iff i < j$ and $Y_i < Y_j \iff \pi(i) < \pi(j)$).
3. Prove that the supercritical point accumulation velocity $v(s) = 2\sqrt{C} = \sqrt{1+4\varepsilon} > 1$ generates cumulative surplus along the corridor that absorbs local lookahead bypasses, bounding the failure probability of dynamic corridor traversal by $\exp(-\Omega(\varepsilon^2 k))$ uniformly across all bundles $T \in \mathcal{T}_k$.

### R2. Resolution of the Cantor Fractal Permutation Gap
Resolve the structural gap identified in the W85 audit for low-footprint, growing-LDS permutations:
1. Analyze self-similar and fractal permutation families (such as recursive block inflations of $[1, 3, 0, 2]$) where corridor area shrinks $\operatorname{Area}(T) \sim k^{D/2 - 1} \to 0$ yet $\operatorname{LDS}(\pi) \sim \sqrt{k}$ without large monotone blocks.
2. Prove the Self-Similar Entropy Bound: show that permutations visiting $S = |T| = o(k)$ cells possess strictly sub-factorial description entropy:
   $$
   |\mathcal{F}_k| \le \exp\left( \mathcal{O}(k) \right) \ll k!.
   $$
3. Conclude that for all such fractal targets, the linear avoidance exponent $\exp(-\Omega(\varepsilon^2 k))$ strictly dominates their target entropy, closing the tripartite sieve without requiring macroscopic 2D area $\ge 0.25$.

### R3. Automated Empirical & Combinatorial Verification Suite
Implement an automated verification tool in `experiments/w86-dynamic-corridor/verify.py` testing:
1. Dynamic lookahead corridor simulation on Poisson hosts at $n = (1/4+\varepsilon)k^2$ across generic bulk targets ($k \in \{20, 50, 100, 200\}$), verifying $100\%$ containment success with 0 order inversions.
2. Fractal permutation census: test recursive Cantor permutations up to $k=256$, verifying that dyadic chaining achieves $100\%$ containment at $C = 1/4 + \varepsilon$.
3. Comprehensive regression check verifying zero regressions across all existing test suites.

### R4. Complete Research Documentation & Lean Alignment
1. Author `experiments/w86-dynamic-corridor/proof.md` containing complete mathematical proofs.
2. Author `experiments/w86-dynamic-corridor/log.md` detailing the research log.
3. Register W86 in `experiments/README.md`, `memory/SESSION-STATE.md`, and `memory/RESULTS.md`.
4. Ensure all Lean 4 formalizations compile cleanly with `lake build` (0 sorrys, 0 warnings).

## Acceptance Criteria

### Automated Combinatorial & Mathematical Verification
- [ ] Dynamic Multi-Scale Lookahead Corridor Traversal Lemma is proved with rigorous surplus bounds absorbing $1/k^2$ box vacancies.
- [ ] Fractal Permutation Entropy Bound is proved, establishing that all $\operatorname{Area}(T) = o(k)$ targets have entropy $\le \exp(\mathcal{O}(k))$, closing the Footprint Sieve Dichotomy.
- [ ] Automated verification script `experiments/w86-dynamic-corridor/verify.py` passes all parts with exit code 0.
- [ ] All existing regression test suites pass with 0 errors:
  - `python3 experiments/witnesses/check_witness.py --all`
  - `python3 experiments/w25-asymptopia-review/certify_cprime.py`
  - `python3 experiments/w83-permuton-bundles/verify.py`
  - `python3 experiments/w84-track-buffers/verify.py`
  - `python3 experiments/w85-redteam-audit/verify.py`
  - `python3 experiments/w86-dynamic-corridor/verify.py`
- [ ] Lean 4 project builds cleanly with 0 errors, 0 warnings, and 0 `sorry`s (`lake build`).
- [ ] Paper manuscripts `output/arxiv/main.tex` and `output/paper/quadratic-universality.md` compile with 0 errors and EXACTLY 0 overfull boxes.

## 2026-09-25T14:00:47Z

Use a very large team of agents.

Advance the proof of Noga Alon's 1999 random superpattern conjecture at the sharp threshold $C^* = 1/4$ toward full generality for all permutations in $S_k$ by launching Workstream W87: Uniform Chaining & Coupled 2D Percolation on Permuton Trajectories at $C^* = 1/4$.

Working directory: `/Users/adamhadani/Development/math-proofs/superpatterns`
Integrity mode: development

Reference material:
- [output/paper/quadratic-universality.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/paper/quadratic-universality.md)
- [output/arxiv/main.tex](file:///Users/adamhadani/Development/math-proofs/superpatterns/output/arxiv/main.tex)
- [experiments/w86-dynamic-corridor/verify.py](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w86-dynamic-corridor/verify.py)
- [experiments/w85-redteam-audit/adversarial_audit_report.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w85-redteam-audit/adversarial_audit_report.md)
- [experiments/w84-track-buffers/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w84-track-buffers/proof.md)
- [experiments/w83-permuton-bundles/proof.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/experiments/w83-permuton-bundles/proof.md)
- [formal-verification/lean/Superpatterns/Interleaving.lean](file:///Users/adamhadani/Development/math-proofs/superpatterns/formal-verification/lean/Superpatterns/Interleaving.lean)
- [formal-verification/lean/Superpatterns/Lattice.lean](file:///Users/adamhadani/Development/math-proofs/superpatterns/formal-verification/lean/Superpatterns/Lattice.lean)
- [CLAUDE.md](file:///Users/adamhadani/Development/math-proofs/superpatterns/CLAUDE.md)
- He–Kwan (2020), "Universality of random permutations", arXiv:1911.12878

## Requirements

### R1. Uniform Empirical Process Chaining over Permuton Trajectories
Develop a uniform empirical process and chaining bound for 2D Poisson host point accumulations across all $(4e)^k$ coarse corridor trajectories in $\mathcal{T}_k$:
1. Formulate the collection of corridor indicator functionals $\{f_T : T \in \mathcal{T}_k\}$ as an empirical process over a single 2D Poisson host process $\Pi_n$ of intensity $n = (1/4+\varepsilon)k^2$.
2. Establish a bracketing entropy / generic chaining bound showing that because trajectories heavily overlap in $[0, 1]^2$, the supremum of empirical process deviations is sub-linear:
   $$
   \mathbb{E}\left[ \sup_{T \in \mathcal{T}_k} \left| N(T) - \mathbb{E}[N(T)] \right| \right] = \mathcal{O}(\sqrt{k \ln(4e)}) = \mathcal{O}(\sqrt{k}) \ll \varepsilon k.
   $$
3. Conclude that on a single common host event $E_{\mathrm{host}}^{\mathrm{chain}}$ of probability $1 - o(1)$, EVERY corridor $T \in \mathcal{T}_k$ simultaneously exhibits supercritical point accumulation density, replacing the divergent naive union bound $|\mathcal{T}_k| \exp(-\gamma k) \to +\infty$ with a unified concentration bound.

### R2. Coupled 2D Percolation & Microscopic Lookahead Bypass
Resolve the 2D Box Capacity Paradox ($\mathbb{E}[N(B_i)] \approx 0.40$, void rate $>80\%$) through dependent corridor percolation:
1. Construct a coupled directed percolation model along each corridor $T$, proving that empty $1/k^2$ micro-boxes form subcritical finite clusters that are bypassed by adaptive lookahead windows $W_t(\Delta)$ of bounded expected depth $\mathbb{E}[\Delta] = \mathcal{O}(1)$.
2. Prove that the supercritical point flux ($v = 2\sqrt{1/4+\varepsilon} > 1$) guarantees that point deficit along any bypassed void cluster is absorbed with exponentially decaying boundary overshoot probability.
3. Prove that the Lean-certified Coordinate Track Buffer ordering ($X_i < X_j \iff i < j$ and $Y_i < Y_j \iff \pi(i) < \pi(j)$) is preserved under the percolating bypass paths with zero coordinate inversions.

### R3. Automated Empirical & Combinatorial Verification Suite
Implement an automated verification tool in `experiments/w87-uniform-chaining/verify.py` testing:
1. Empirical process fluctuation test: measure $\sup_{T \in \mathcal{T}_k} |N(T) - \mathbb{E}[N(T)]|$ across Poisson host simulations for $k \in \{20, 50, 100, 200\}$ at intensity $C = 1/4 + \varepsilon$, verifying $\mathcal{O}(\sqrt{k})$ scaling.
2. Coupled percolation simulation: evaluate lookahead bypass depth distributions and verify that void cluster lengths decay exponentially with 0 order inversions across generic bulk targets.
3. Master sieve convergence: verify the unified non-containment probability decays to zero.
4. Comprehensive regression run verifying 0 regressions across all existing suites (`check_witness.py --all`, `certify_cprime.py`, `w83`, `w84`, `w85`, `w86`).

### R4. Complete Research Documentation & Lean Alignment
1. Author `experiments/w87-uniform-chaining/proof.md` detailing the mathematical proofs.
2. Author `experiments/w87-uniform-chaining/log.md` recording the investigation audit trail.
3. Register W87 in `experiments/README.md`, `memory/SESSION-STATE.md`, and `memory/RESULTS.md`.
4. Check that all Lean 4 formalizations compile cleanly with `lake build` (0 sorrys, 0 warnings).

## Acceptance Criteria

### Automated Combinatorial & Mathematical Verification
- [ ] Uniform Empirical Process Chaining Theorem is proved in `proof.md`, establishing $\sup_{T \in \mathcal{T}_k} |N(T) - \mathbb{E}[N(T)]| = \mathcal{O}(\sqrt{k})$ and proving simultaneous supercritical flux across all $|\mathcal{T}_k| \le (4e)^k$ corridors on a single host event of probability $1 - o(1)$.
- [ ] Coupled 2D Percolation Bypass Lemma is proved, establishing that lookahead windows bypass micro-box vacancies with zero coordinate inversions and geometrically decaying bypass length.
- [ ] Automated verification script `experiments/w87-uniform-chaining/verify.py` passes all parts with exit code 0.
- [ ] All existing regression test suites pass with 0 errors:
  - `python3 experiments/witnesses/check_witness.py --all`
  - `python3 experiments/w25-asymptopia-review/certify_cprime.py`
  - `python3 experiments/w83-permuton-bundles/verify.py`
  - `python3 experiments/w84-track-buffers/verify.py`
  - `python3 experiments/w85-redteam-audit/verify.py`
  - `python3 experiments/w86-dynamic-corridor/verify.py`
- [ ] Lean 4 project builds cleanly with 0 errors, 0 warnings, and 0 `sorry`s (`lake build`).
- [ ] LaTeX and Pandoc manuscripts compile with 0 errors and EXACTLY 0 overfull boxes.
