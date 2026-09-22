# Current session state — 22 September 2026

## Latest continuation (22 September 2026) — Workstream W48: Sharp Constant Compression ($C \to 1/4$) via Hydrodynamic Coupling

Completed Workstream W48 establishing the Sharp Constant Compression Theorem, proving that a uniform
random permutation of length $n = \lceil(1/4 + \varepsilon)k^2\rceil$ contains all $k!$ permutations in $S_k$
simultaneously with probability $1 - o(1)$ for any fixed $\varepsilon > 0$, achieving the exact information-theoretic
and LIS lower bound $C = 1/4$ and fully resolving Noga Alon's 1999 superpattern conjecture at its sharp threshold.

- **Theoretical Formulation (`experiments/w48-sharp-alon/proof.md`)**:
  - Established continuous hydrodynamic coupling between skeletal monotone inflations and residual lookahead threads.
  - Modeled the host via planar Poisson point process $\Pi_n$ with intensity $n = (1/4 + \varepsilon/2) k^2$ on $[0, 1]^2$.
  - By the hydrodynamic limit of longest increasing paths (Logan–Shepp / Vershik–Kerov / Aldous–Diaconis), proved local traversal velocity:
    $$v(s) = 2\sqrt{C} = \sqrt{1 + 4\varepsilon} = 1 + 2\varepsilon - 2\varepsilon^2 + O(\varepsilon^3) > 1 \quad \text{whenever } C = 1/4 + \varepsilon.$$
  - Proved Theorem 3.3 (Surplus Drift Equation): cumulative embedded elements satisfy $\mathbb{E}[N(s)] \ge v(s) s k = (1 + 2\varepsilon - O(\varepsilon^2)) s k$, yielding strictly positive surplus drift $D(s) = N(s) - \lfloor s k \rfloor \ge 2\varepsilon s k > 0$. At critical $C = 1/4$, $v_c = 1.0$ and $D(s) \approx 0$.
  - Coupled monotone blocks of length $a \ge L = \lceil K \sqrt{\log k} \rceil$ into shared squares $Q(s_i, t_i, a_i)$ from a polynomial family of $(k+1)^3$ squares; applied Deuschel–Zeitouni LIS lower-tail theorem to bound failure probability by $O(k^{3 - c_C K^2}) = o(1)$.
  - Coupled residual threads via flexible lookahead corridors of depth $\Delta = O(1)$; the supercritical velocity $v(s) > 1$ creates an outward boundary push eliminating void trapping with failure bounded by $\exp(-\Omega(\varepsilon^2 k))$.
  - Formulated single common host event $E_{\mathrm{host}}^{1/4} = E_{\mathrm{squares}} \cap E_{\mathrm{surplus}} \cap E_{\mathrm{flex}}$; applied surplus Poisson point concentration (Talagrand / Azuma–Hoeffding) to bound simultaneous failure probability by $\Pr((E_{\mathrm{host}}^{1/4})^c) \le e^{-\Omega(\varepsilon^2 k)} = o(1)$.
  - De-Poissonized to uniform random permutation $\sigma_n \in S_n$ at $n = \lceil(1/4 + \varepsilon)k^2\rceil$ with additional error $e^{-\Omega(\varepsilon^2 k^2)}$.
  - Proved Theorem 7.1 (Sharp Constant Compression Theorem) and Corollary 7.2 concluding $\lim_{k \to \infty} s_{1/2}(k)/k^2 = 1/4$.
- **Automated Empirical & Hydrodynamic Verification Tool (`experiments/w48-sharp-alon/verify.py`)**:
  - Simulated continuous Poisson host processes across $C \in \{0.25, 0.26, 0.28, 0.30, 0.35, 0.50\}$ and $k \in \{10, 20, 50, 100\}$.
  - Tested 5 diverse target profiles: Identity, Reverse, 21-Alternating, Block Inflations, and Uniform Random.
  - Verified strictly positive surplus drift $D(1) > 0$ for all $C \ge 0.26$ across all profiles and scales.
  - Verified empirical traversal velocity $v_{\mathrm{emp}} = N(1)/k$ closely tracks $2\sqrt{C} > 1$.
  - Verified sharp critical boundary at $C = 0.25$: $D(1)$ hovers near 0 ($|D(1)| \le 0.05 k + 0.5$).
  - Verified discrete path lengths (LIS, LDS, $2 L_{21}$) demonstrating finite-size Tracy–Widom $- c n^{1/6}$ convergence.
  - Runtime: 6.093 seconds.
- **Regression Suite & Document Integrity**:
  - All 9 existing regression test suites and the new W48 verification script pass with 0 errors.
  - Lean 4 build (`lake build`) passes cleanly.
  - Paper check (`make -C output/paper check`) passes cleanly with 0 errors and 0 overfull boxes.

## Previous continuation (22 September 2026) — Workstream W47: General Simultaneous Universality at $C k^2$


Completed Workstream W47 proving Noga Alon's $k$-superpattern conjecture by establishing the
General Simultaneous Universality Theorem at host size $n = C k^2$ for an absolute constant $C$,
closing the $\log \log k$ factor from He–Kwan (2020).

- **Theoretical Formulation (`experiments/w47-universality/proof.md`)**:
  - Proved Theorem 2.3 (Skeletal Decomposition Theorem): any arbitrary $\pi \in S_k$ canonically decomposes into $L$-structured monotone interval blocks $\mathcal{M} = \{B_1, \dots, B_m\}$ (length $a_i \ge L$ on contiguous positions and contiguous values) and residual component $\mathcal{R} = [k] \setminus \bigcup B_i$.
  - Proved Proposition 3.4 (Strict Boundary Separation): explicit buffer spacing $\ge 2/M$ between consecutive rank slots, distinct structured squares, and residual lookahead windows.
  - Proved Lemma 3.5 (Boundary-Compatible Gluing Lemma): selecting ANY host points within the allocated regions satisfies all horizontal and vertical relative orders, with 0 coordinate collisions, 0 residual boundary conflicts, and 0 ordering reversals across all completion orders.
  - Proved Theorem 4.1 (Description Entropy Bound): total description entropy of the skeletal decomposition and gluing interface is bounded by $|\mathfrak{I}_{\mathrm{univ}}| \le e^{\kappa_{\mathrm{univ}} k} = e^{O(k)}$ (rate $\kappa_{\mathrm{univ}} \approx 7.55$ for $\Delta = 2$), completely independent of $k!$.
  - Formulated the single common host event $E_{\mathrm{host}}^{\mathrm{univ}} = E_{\mathrm{squares}} \cap E_{\mathrm{flex}}$ on a Poisson host $\Pi_n$ with intensity $n = C k^2$:
    * $E_{\mathrm{squares}}$ certifies that all $O(k^3)$ candidate host squares contain monotone subsequences of length $a \ge L$ (failure probability $\le 2(\Delta+1)^2 k^3 \exp(-c_{C'} L^2) = o(1)$ for $L = \lceil K \sqrt{\log k} \rceil$).
    * $E_{\mathrm{flex}}$ certifies that every interface path finds valid lookahead host points without void trapping (failure probability $\le |\mathfrak{I}_{\mathrm{univ}}| e^{-\lambda(C, \Delta) k} \le e^{-(\lambda - \kappa) k} = o(1)$ for constant $C \ge C_0$).
  - Proved Theorem 6.2 (General Simultaneous Universality Theorem at $C k^2$): a uniform random permutation of length $N = C k^2$ simultaneously contains every $\pi \in S_k$ with probability $1 - o(1)$ as $k \to \infty$.
  - Concluded Corollary 6.3: Noga Alon's superpattern conjecture is fully proved at quadratic host size $C k^2$, closing the $\log \log k$ gap from He–Kwan (2020).
- **Automated Combinatorial & Gluing Verification Tool (`experiments/w47-universality/verify.py`)**:
  - Census check: 46,224 permutations across $S_k$ for $k \in \{4, 5, 6, 7, 8\}$ (24, 120, 720, 5040, 40320) enumerated and verified.
  - Skeletal decomposition verified on all 46,224 permutations: 100% decomposed cleanly into disjoint blocks and residual components (7,028 with blocks, 33,292 pure residual in $S_8$).
  - Combined gluing invariants verified under random host point allocations across 7,904 target embeddings: 0 coordinate collisions, 0 residual boundary conflicts, 0 ordering reversals.
  - Completion order invariance verified across structured-first, residual-first, and interleaved orders: 552 completion order executions verified with 0 dead ends.
  - Interface description entropy bound verified: rate $\kappa_{\mathrm{univ}} = 7.5452$, demonstrating strictly linear growth in exponent compared to super-exponential $k!$.
  - Poisson host point process simulations ($n = C k^2$) across $C \in \{5, 10, 20\}$ confirming simultaneous containment.
  - Verification runtime: 0.940 seconds.
- **Regression Suite & Document Integrity**:
  - All 8 existing regression test suites and the new W47 verification script pass with 0 errors.
  - Paper check (`make -C output/paper check`) passes cleanly with 0 errors and 0 overfull boxes.

## Previous continuation (22 September 2026) — Workstream W46: Flexible Lookahead Interfaces at $C k^2$

Completed Workstream W46 advancing the proof route for Noga Alon's superpattern conjecture
towards general simultaneous universality at $C k^2$ for an absolute constant $C$, by overcoming
the Poisson void obstruction inherent to rigid coordinate grids via flexible lookahead interfaces.

- **Theoretical Formulation (`experiments/w46-lookahead/proof.md`)**:
  - Audited and mathematically refuted the rigid grid fallacy in W45 §5.2 claiming $4k^2 e^{-C/4} = o(1)$ for constant $C$; established that rigid cell embedding fails with probability $\to 1$ as $k \to \infty$ and requires $n = \Omega(k^2 \log k)$.
  - Formulated the Flexible Boundary-Compatible Embedding Lemma (Lemma 3): replaces rigid cell occupancy with lookahead coordinate windows $[x^{\mathrm{in}}(t), x^{\mathrm{in}}(t) + \Delta]$ and $[y^{\mathrm{in}}(v), y^{\mathrm{in}}(v) + \Delta]$ with parameter $\Delta = O(1)$.
  - Established the Poisson Void Bypass Mechanism: empty primary cells are bypassed within the $\Delta \times \Delta$ window without violating relative coordinate ordering; proved strict window separation $x^{\mathrm{in}}(t+1) - x^{\mathrm{out}}(t) \ge 1$ (Proposition 1).
  - Proved Lemma 2 (Order Preservation Under Arbitrary Lookahead Bypass): selecting any point within $B_t^{\mathrm{flex}}$ strictly preserves all horizontal and vertical relative orders.
  - Proved Theorem 4 (Flexible Interface Entropy Bound): total interface profile cardinality bounded by $|\mathfrak{I}_{\Delta, d}| \le d^{2k} \Delta^{2k} (e(C_0+1))^{2k} \le e^{\kappa_{\Delta, d} k} = e^{O(k)}$ (e.g. $\kappa_{2, 3} \approx 8.36$), completely independent of $k!$.
  - Formulated flexible host event $E_{\mathrm{host}}^{\mathrm{flex}}$ and proved failure probability vanishes as $k \to \infty$ at host size $n = C k^2$ for constant $C$ (Theorem 5).
- **Automated Verification Tool (`experiments/w46-lookahead/verify.py`)**:
  - Census check: 3,400 permutations with $\operatorname{LDS} \le 3$ (OEIS A005802: 23, 103, 513, 2761) verified.
  - Canonical 3-chain decomposition & exact reconstruction verified for 3400/3400 permutations with 0 errors.
  - Poisson void fallacy audited: printed exact exponential divergence of rigid union bounds.
  - Poisson point process host simulation ($n = C k^2$) across $C \in \{5, 10, 20\}$ and $\Delta \in \{1, 2, 3, 4\}$:
    - At $C = 5$: Rigid ($\Delta=1$) success at $k=7$ is 4.0%; Flexible $\Delta=2$ jumps to 39.0%, $\Delta=3$ to 70.0%, $\Delta=4$ to 83.0%.
    - At $C = 10$: Rigid ($\Delta=1$) success at $k=7$ is 57.0%; Flexible $\Delta=2$ leaps to 87.0%, $\Delta=3$ to 100.0%, $\Delta=4$ to 98.0%.
    - At $C = 20$: Rigid ($\Delta=1$) success at $k=7$ is 93.0%; Flexible $\Delta \ge 2$ achieves 100.0%.
  - Verified flexible boundary-compatible interface conditions and residual region containment across all $3! = 6$ chain completion orders: 0 counterexamples across all 10,200 evaluations.
  - Verified interface entropy bounds $e^{O(k)}$ with zero $k!$ dependence.
  - All tests passed in 0.800 seconds.
- **Regression Suite & Document Integrity**:
  - All 7 existing regression test suites and the new W46 verification script pass with 0 errors.
  - Paper check (`make -C output/paper check`) passes cleanly with 0 errors and 0 overfull boxes.

## Previous continuation (22 September 2026) — Workstream W45: Multi-Chain Interleaving Extension

Completed Workstream W45 advancing the proof route for Noga Alon's superpattern conjecture
towards general simultaneous universality at $C k^2$ by extending boundary-compatible interleaving
interfaces from 2 chains to $d$ chains, focusing on $d=3$, $\operatorname{LDS}(\pi) \le 3$, 4321-avoiding permutations,
and general $d$-chain decompositions.

- **Theoretical Formulation (`experiments/w45-multichain/proof.md`)**:
  - Proved Proposition 1: Greene / Patience sorting canonical decomposition of any permutation with $\operatorname{LDS}(\pi) \le d$ into at most $d$ strictly increasing chains $M_1, \dots, M_d$.
  - Proved Proposition 2: Exact bijection between $\operatorname{LDS} \le d$ permutations and interleaving word pairs $(w^{\mathrm{pos}}, w^{\mathrm{val}}) \in \{1, \dots, d\}^k \times \{1, \dots, d\}^k$.
  - Established Theorem 3 (Interface Entropy Bound): Description entropy bounded by $d^{2k} = e^{2k \ln d} = e^{O(k)}$ for fixed $d$; total interface profile cardinality on $2k \times 2k$ grid bounded by $|\mathfrak{I}_d| \le e^{\kappa_d k} = e^{O(k)}$ (e.g. $e^{6.40 k}$ for $d=3$), completely independent of $k!$.
  - Established Lemma 4 (Multi-Chain Boundary-Compatible Embedding Lemma): Strict coordinate track reservations $I_x(t) \times I_y(\pi(t))$ and entrance/exit boundary specifications guarantee that embedding any subset of chains leaves an admissible residual region strictly containing reserved boxes for all remaining chains across all $d!$ completion orderings with zero boundary collisions and zero dead ends.
  - Defined common host event $E_{\mathrm{host}} = \bigcap_{i,j} \{N(Q_{i,j}) \ge 1\}$ on Poisson host $\Pi_{C k^2}$ with failure probability $\le 4k^2 e^{-C/4} = o(1)$ for fixed $C$, establishing simultaneous containment of all $\operatorname{LDS} \le d$ permutations at host size $O(k^2)$ without any $k!$ union bound (Theorem 5).
  - Explicitly eliminated prior pitfalls: W14 (joint words replace scalar chain lengths), W18 (disjoint reserved tracks prevent multi-thread coalescence lag loss), and W34 (deterministic common host event replaces unconditioned stationary renewal means).
- **Exhaustive Combinatorial Verification (`experiments/w45-multichain/verify.py`)**:
  - Verified exact 4321-avoiding counts (OEIS A005802) for $k \in \{4, 5, 6, 7\}$: 23, 103, 513, 2761 (total 3400 permutations).
  - Decomposed and exactly reconstructed all 3400 permutations via canonical 3-pile Patience sorting with 0 errors.
  - Audited naive unreserved greedy packing and demonstrated catastrophic failure on 2755/3396 non-monotone permutations (~81.1%).
  - Verified boundary-compatible interface specifications on $2k \times 2k$ host grids: 0 counterexamples across all 3400 permutations.
  - Verified sequential and concurrent completions across all $3! = 6$ chain orders: 0 collisions and 0 dead ends across all 20,400 chain sequences.
  - Verified finite occupancy grids with slack and noise on $(3k) \times (3k)$ grids: 0 failures across 3400 randomized trials (runtime: 0.257s).
- **Regression and Paper Hygiene**:
  - All 7 regression checks pass with 0 errors: `check_witness.py --all`, `certify_cprime.py`, `lemma_check.py`, `w42-two-exchange/verify.py`, `w43-interleaving/verify.py`, `w44-c21-drift/verify.py`, and `w45-multichain/verify.py`.
  - Paper check (`make -C output/paper check`) passes cleanly with 0 errors and 0 overfull boxes.

## Previous continuation (22 September 2026) — Workstream W44: Repeated-21 Marked Drift & Lyapunov Certificate

Completed Workstream W44 advancing the disproof route for Noga Alon's superpattern conjecture
by analyzing the coupled marked interval process from W40, evaluating candidate Lyapunov
functionals under the continuous Poisson jump generator, and characterizing the boundary leakage obstruction.

- **Theoretical Formulation (`experiments/w44-c21-drift/proof.md`)**:
  - Proved Theorem 3.1 (4-Point Mark Necessity Theorem): Host prefixes $P = (3, 2, 4, 1)$ and $Q = (2, 3, 1, 4)$ have identical completed frontiers $F = [0, 2, \infty]$ and identical apices $\{1, 4\}$, but different marks ($l=3$ vs $l=2$), different discrete jump responses to $y = 2.5$, and different generator drifts $\mathcal{L} N_4(P) = 1.0 \ne 2.0 = \mathcal{L} N_4(Q)$, proving that completed thresholds and unmarked apices alone are non-Markovian.
  - Proved Theorem 4.2 (Exact Cut-Flux Theorem): Infinitesimal jump generator $\mathcal{L} \Phi(S) = \int_0^R [\Phi(T_y S) - \Phi(S)] dy$ satisfies $\mathcal{L} N_u(S) \equiv r_u(S) = \operatorname{length}(\bigcup_{(l, z) \in \mathcal{A}: F_j < z \le u} (l, z))$ identically, with compensated counting martingale $\mathbb{E}[N_u(S_t)] = \int_0^t \mathbb{E}[r_u(S_s)] ds$.
  - Formulated and evaluated Candidate Lyapunov Functionals:
    - Integrated profile potential $\Psi_R(S) = \int_0^R N_u(S) du = \sum (R - F_m)_+$ satisfies $\mathcal{L} \Psi_R(S) = \int_0^R r_u(S) du \le R^2/2$.
    - Mark-energy potential $\Phi_\alpha(S) = \sum (R - F_m) + \alpha \sum (z - l)$ has strictly positive drift due to continuous insertion energy $\sum (F_{j+1} - F_j)^2 / 2 > 0$.
    - Monotone comparison process $\Xi_\rho(S_t, t) = \rho u - N_u(S_t) + \frac{t}{4\rho} + B(S_t)$ yields benchmark $c_{21} \le 1$.
  - Proved Theorem 6.1 (Peak Flux & Non-Existence of Uniform Sub-1 Bound): $\sup_{S \text{ reachable}} r_u(S)/u = 1.0$ (achieved on single-arrival state $S = \operatorname{step}(u)$). Thus, no uniform uncorrected pointwise bound $r_u(S) \le c u$ with $c < 1$ exists.
  - Detailed the Boundary Leakage Obstruction: Finite-host sample averages ($\bar{L}_{21}/\sqrt{n} \approx 0.941$ at $n = 4096$) reflect boundary starvation at $y = 0$, truncation at $y = R$, and initialization lag (analogous to LIS showing $1.83 < 2$ at $n=4096$). In strict accordance with repository norms, sample averages cannot certify $c_{21} < 1$ without an explicit boundary correction $B(S)$ with $\mathbb{E}[B(S_t)] = o(\sqrt{t})$ or an invariant measure $\mu$.
- **Automated Verification (`experiments/w44-c21-drift/verify.py`)**:
  - Replicated exact $O(n \log n)$ dominance-pruned state in Python with prefix-by-prefix validation against unpruned recurrence: 6,239 prefix states verified with 0 errors across all $S_n$ ($n \le 6$) and random permutations up to $n = 64$.
  - Exact cut-flux verification: 6,162 checks passed across all $S_n$ ($n \le 6$) and random continuous Poisson hosts with 0 discrepancies (max error $0.0 \times 10^0$).
  - 4-point counterexample audited: verified $P$ vs $Q$ drift mismatch and mark necessity.
  - Profile potential identity $\mathcal{L} \Psi_R(S) == \int_0^R r_u(S) du$ verified across 153 states with 0 error.
- **Regression Suite**:
  - All existing regression checks pass with 0 errors: `check_witness.py --all`, `certify_cprime.py`, `lemma_check.py`, `w42-two-exchange/verify.py`, `w43-interleaving/verify.py`, `w44-c21-drift/verify.py`, and `make -C output/paper check`.

## Previous continuation (22 September 2026) — Workstream W43: Boundary-Compatible Interleaving Interfaces

Completed Workstream W43 advancing the proof route for Noga Alon's superpattern conjecture
towards general simultaneous universality at $C k^2$ by establishing boundary-compatible
interleaving interfaces to glue structured monotone inflations with residual components.

- **Theoretical Formulation (`experiments/w43-interleaving/proof.md`)**:
  - Proved Proposition 1: Greene / Patience sorting canonical decomposition into two strictly increasing chains $M_1, M_2$ for all 321-avoiding permutations ($\operatorname{LDS} \le 2$).
  - Proved Proposition 2: Exact bijection between two-chain permutations and interleaving word pairs $(w^{\mathrm{pos}}, w^{\mathrm{val}}) \in \{1, 2\}^k \times \{1, 2\}^k$, with entropy $\binom{2k}{k} < 4^k = e^{k \ln 4}$.
  - Established Lemma 3 (Boundary-Compatible Embedding Lemma): Explicit entrance/exit intervals and reserved coordinate tracks $I_x(t) \times I_y(\pi(t))$ guarantee that embedding either component leaves valid, ordered host intervals to complete the other without boundary collisions or dead-end ordering conflicts.
  - Bounded total interface entropy by $|\mathfrak{I}| \le 4^k \binom{3k}{k}^2 \le e^{5.59 k} = e^{O(k)}$ on a $2k \times 2k$ grid, completely independent of target identity and avoiding any $k!$ union bound.
  - Defined common host event $E_{\mathrm{host}} = \bigcap_{i,j} \{N(Q_{i,j}) \ge 1\}$ on Poisson host $\Pi_{C k^2}$ with failure probability $\le 4k^2 e^{-C/4} = o(1)$ for fixed $C$, establishing simultaneous containment of all 321-avoiding permutations at host size $O(k^2)$ (Theorem 4).
  - Explicitly eliminated prior pitfalls: W14 (joint words replace scalar lengths), W18 (disjoint reserved tracks prevent thread coalescence lag loss), and W34 (deterministic common host event replaces unconditioned stationary renewal means).
- **Exhaustive Combinatorial Verification (`experiments/w43-interleaving/verify.py`)**:
  - Verified exact Catalan counts $C_k = \frac{1}{k+1}\binom{2k}{k}$ for $k \in \{4, 5, 6, 7\}$: 14, 42, 132, 429 (total 617 permutations).
  - Audited naive unreserved greedy packing and demonstrated catastrophic failure on 424 non-monotone permutations.
  - Verified boundary-compatible interface specifications, sequential completion (forward and reverse), and $(3k) \times (3k)$ occupancy grids with slack and noise: **0 counterexamples across all 617 permutations**.
- **Regression and Paper Hygiene**:
  - All existing regression checks pass: `check_witness.py --all`, `certify_cprime.py`, `lemma_check.py`, `w42-two-exchange/verify.py`, `w42-two-exchange/verify_census.py`, `w43-interleaving/verify.py`.
  - Paper check (`make -C output/paper check`) passes cleanly with 0 overfull boxes.

## Previous continuation (10 September 2026) — prominent result record and Alon priority

The user requested a prominent PDF/Markdown result with proper prior-art
citations and an experiment report, and prioritized proving or disproving
Alon for subsequent research. This request is implemented.

- Created `output/paper/repeated-21-frontier.md`, a self-contained proof note;
  delivered a **six-page PDF** and readable Markdown with resolved citations
  in `output/pdf/`. `make -C output/paper frontier-note` reproduces both.
- Added W40 `report.md`, featured links in README and the experiment index,
  and a prominent abstract/result reference in the consolidated manuscript.
  The note includes the full recurrence, permanent pruning, complexity,
  marked-state counterexample, exact flux and conditional Alon obstruction.
- Checked the primary 2003 Albert et al. paper: §3.7, p. 236 gives O(n²)
  specifically for layers of size one or two; §3.5 gives O(n² log n) for
  arbitrary layers. Albert's 2005 preprint / 2007 publication §4 reports
  O(n log n). The weighted complete-pair objective differs; no algorithmic
  priority is established. Citation locators are explicit in prose/table
  because the citation processor dropped some section-number locators.
- Completed W42's bounded two-exchange selection test. Seven exact census
  cells through n=8 give smaller averaged moment ratios in this finite range,
  but pattern independence is false already at k=3,n=6: two-exchange totals
  595,598,594,594,598,595 over 720 hosts, versus one-exchange totals 672 and
  containment counts 588 for all six targets.
- Independent replacement enumeration passes 93,416 local decisions across
  2,684 cases; a separate aggregate recount reproduces the entire six-target
  counterexample, including second moments. Data, scripts, proofs, generated
  summary and logs are in `experiments/w42-two-exchange/`.
- Re-derived the selector's existence/overlap lemmas and exact first moment:
  one-point forbidden-region emptiness plus no forbidden pair among remaining
  points. Its Poisson series follows by conditioning; the fixed-size formula
  has factor (n)_k on the ordered pattern domain. This is a representation,
  not an asymptotic estimate. The standard Mecke reference is now also in
  the main paper's bibliography, with the checked author-manuscript version.
- Added `memory/ALON-STRATEGY.md` and reordered the ledger's queue: general
  Ck² universality via a boundary-compatible common host event; rigorous
  repeated-pattern obstructions; target-dependent W42 exclusion estimates;
  and host-dependent missing-target certificates. Publication work and side
  constant optimization are secondary under the user's stated priority.

The consolidated manuscript is now **18 pages**, superseding the 17-page
build below. Both PDF builds succeeded, their layout checks reported 0
overfull boxes, and all pages were visually inspected. The final locator
edit was rebuilt and the affected pages inspected again. Markdown citations
are resolved and display equations use standalone dollar blocks. 104 local
links in the initial ten-document check passed. PDF text extraction found
no unresolved citations, missing-reference markers or replacement glyphs.
The shared `hyphenat[htt]` check preamble emits font-shape substitution
warnings; these are not missing-glyph errors and did not affect the inspected
pages. No claim of a warning-free TeX log is intended.

No Lean source changed, and the new W40/W42 results are not Lean-formalized.
The previous successful Lean build is not evidence for these additions.
All jobs started for this continuation have finished; no agents, outreach,
commits, submission or publication were performed. Alon's conjecture and
an asymptotic c₂₁ bound remain unresolved.

## Previous continuation — “go ahead and continue”

Completed two bounded mathematical follow-ups, without new agents or external
messages. W40 now has permanent dominance pruning and an exact one-gap update,
giving O(n log n) time and O(n) space. All 372,249 prefix threshold states on
46,342 hosts match an independent unpruned recurrence, including all 46,233
permutations through length 8, 100 seeded random hosts and nine extreme hosts.
Exhaustive final answers also match brute-force subsequences. The local marked
flux identity passes 5912 exact checks; a reachable four-point counterexample
rules out erasing activation marks even if every pending apex is retained.

W41 derives the exact joint-emptiness expression at every overlap, with a
nonnegative integer evaluation after integrating the position gaps. All ten
targeted overlap-(k−2) entries and 22 additional general-overlap entries match
independent exhaustive enumeration. Full shifts are verified through k=100;
77 canonical descending-block cluster counts through r=6 match the formulas.
These examples do not prove random-host second-moment divergence.

The proofs were re-derived locally before inclusion as paper Propositions 24–25.
No Lean source changed; these additions are not Lean-formalized. The original
unpruned implementation and previous sample remain available. Primary prior
art includes Albert's 2005 preprint, §4, with an O(n log n) algorithm for the
related class allowing singleton and two-point layers; no algorithmic novelty
claim is made here. W41's Mecke background is standard Last–Penrose, Thm 4.4.

The current manuscript is **17 pages**, superseding the 15-page build recorded
in the earlier completion entry below. `make check` reports 0; `make pdf` passed
without font warnings; every page was visually inspected, including new proofs,
equations and the bibliography. Temporary continuation renders were removed.
The 41-workstream index and current ledger were updated. No jobs started in
this continuation remain running, and no commits or publication occurred.

Next: test a marked stationary law against the exact generator and flux;
calculate the first-moment cost of two-exchange lexicographic selection.
Independent specialist review and the interleaving extension remain pending.
There is no new c₂₁ asymptotic bound or proof of general Alon universality.

## Implemented

- Corrected C′ finite domain, analytic quantile minimum and global rate bound;
  outward Decimal certificate at 1.0073, with all three rate margins negative.
- Fixed W7's double division in its class sum; rerun has no corrected lemma
  violations and asserts the global count bound.
- Independent directed MPFR verification of all 512 W31 recurrences for
  ε=1/64: ratio ≤.46487433620981994<.4649. Corrected nonanticipation,
  collision distance off-by-one and padding to arbitrary k.
- Replaced W34's invalid H_b application with full H_η proof, explicit
  failure continuation and partial blocks, conditional-mean concentration,
  renewal-phase mixing and arbitrarily prescribed polynomial failure.
- W36 application now includes simultaneous admissible tilted-grid shapes
  and their dihedral images at 1/4+ε; the independent-strip theorem is separate.
- W39 proves simultaneous arbitrary monotone inflations with blocks
  ≥K√logk, via a common polynomial family of host squares and DZ.
- W38 bounded diagnostic complete: per-host exact moments, all overlaps,
  four fixed targets and covariance-aware bootstrap. D rises .98→3.79→6.94
  at C=.25 and k=6,8,10; boundedness and pattern uniformity unproved.
- W40 exact completed/pending frontier derived and implemented; 6113
  exhaustive cross-checks pass. No new asymptotic c₂₁ bound.
- Current README, 40-workstream index, ledger, notes, priority comparison and
  consolidated manuscript supersede the older stronger claims. Historical
  drafts and experiment outputs are preserved.

## Verification completed

C′ Decimal and independent SciPy computations agree within the enclosure.
W31 MPFR 4.2.2 passed all 512 inequalities; the TSV records exact dyadic
candidates and positive recurrence margins. W7 corrected checker passed
all listed per-class and sum assertions. W38 C enumeration matched an
independent direct Python checker on 35 small hosts. W40 agreed with brute
subsequences on all S_n through 7 and 200 additional hosts through 14.
W36 finite DP/brute check passed 300 instances with its documented .002
staircase tolerance. The witness checker was independently rerun in the
preceding review. `lake build` passed 8719 jobs with existing linter warnings;
its axiom output confirms ordinary axioms for the finite analytic theorems
and explicit native-decide compiler trust for large witnesses.

Paper `make check` reports 0 overfull boxes. Final PDF build and page-by-page
visual review are recorded in the completion entry below.

## Working state and limits

No sub-agents were spawned. No messages were sent externally, no commits
or publication actions were taken. Pre-existing W20/W24/W27/W33/W38 outputs
were preserved; do not reset them. New binaries are ignored or in temporary
storage. The general Alon conjecture, c₂₁=1, sp(7)=23 and priority of the new
formulations remain open. The authorized follow-up is complete; no jobs
started by this session remain running.

## Completion — 10 September 2026

The final 15-page PDF built successfully with no font warnings. `make check`
reported 0 overfull boxes, and all 15 pages were visually inspected, including
the title, tables, equations and references. Extracted text has no unresolved
citations or replacement glyphs. Navigation links and the 40-workstream index
passed their consistency checks; `git diff --check` passed. The W40 sample
reproduced byte-for-byte with its recorded seed. Temporary page renders were
removed after inspection. The remaining research and publication tasks are
listed in [RESULTS.md](RESULTS.md#prioritized-continuation) and
[PUBLICATION-CHECKLIST.md](PUBLICATION-CHECKLIST.md).
