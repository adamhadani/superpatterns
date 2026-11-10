# Workstream W44: Repeated-21 Marked Drift & Lyapunov Certificate Research Log

## 2026-09-22: Inception and Architecture Setup
- **Objective**: Advance the disproof route for Noga Alon's $k$-superpattern conjecture by analyzing the coupled marked interval process from W40, formulating candidate Lyapunov functionals on the marked state $(F_m, \{(l_i, z_i)\})$, and determining whether $c_{21} = \lim_{n \to \infty} L_{21}(\sigma_n)/\sqrt{n} < 1$.
- **Theory Design Review**: Analyzed `W44_THEORY_DESIGN.md`, `repeated-21-frontier.md` (Proposition 5), and W40 verification scripts.
- **Repository Norms Verification**: Reaffirmed non-negotiable standard: finite-host sample averages ($\bar{L}_{21}/\sqrt{n} \approx 0.941$ at $n = 4096$) are empirical diagnostics, not asymptotic bounds. An upper bound requires an explicit boundary correction or supermartingale comparison.

## 2026-09-22: Implementation of Exact Python Engine (`verify.py`)
- Replicated exact $O(n \log n)$ dominance-pruned state from `pruned.c` as `DominancePrunedState`.
- Implemented unpruned quadratic recurrence `full_thresholds` as an independent verification oracle.
- Verified prefix-by-prefix agreement across all 873 permutations in $S_n$ for $n \in \{1, \dots, 6\}$ (6,239 prefix states checked) plus random permutations up to $n = 64$.
- **Result**: 0 discrepancies; 100% prefix agreement confirmed.

## 2026-09-22: Continuous Poisson Generator & Exact Cut-Flux Verification
- Implemented infinitesimal jump generator:
  $$\mathcal{L} \Phi(S) = \int_0^R [\Phi(T_y S) - \Phi(S)] \, dy$$
  using exact partition breakpoints formed by $\{0, R\} \cup \{F_m\} \cup \{z_i\} \cup \{l_i\}$.
- Implemented exact cut-flux rate:
  $$r_u(S) = \operatorname{length}\left(\bigcup_{(l, z) \in \mathcal{A}: F_j < z \le u} (l, z)\right).$$
- Tested $\mathcal{L} N_u(S) \equiv r_u(S)$ across all permutations in $S_n$ for $n \in \{1, \dots, 6\}$ (5,912 combinatorial checks) and 250 random continuous Poisson host configurations (total 6,162 checks).
- **Result**: Max discrepancy: $0.0 \times 10^0$. Exact mathematical identity confirmed.

## 2026-09-22: 4-Point Mark Necessity Theorem Audit
- Audited the 4-point counterexample:
  $$P = (3, 2, 4, 1) \quad \text{vs} \quad Q = (2, 3, 1, 4).$$
- Observed:
  - Both produce $F = [0, 2, \infty]$ and apices $\{1, 4\}$.
  - $P$ retains $(3, 4)$ at level 1; $Q$ retains $(2, 4)$ at level 1.
  - On arrival $y = 2.5$: $P$ has 0 completions (F stays $[0, 2, \infty]$), while $Q$ closes apex 4, yielding $F_2 = 4$.
  - At cut $u = 4.0$: $\mathcal{L} N_4(P) = 1.0 \ne 2.0 = \mathcal{L} N_4(Q)$.
  - Profile drift: $\mathcal{L} \Psi_{4.5}(P) = 0.5 \ne 1.0 = \mathcal{L} \Psi_{4.5}(Q)$.
- **Conclusion**: Discarding activation marks renders the state non-Markovian. Marks are mathematically indispensable.

## 2026-09-22: Evaluation of Candidate Lyapunov Potentials
1. **Candidate 1: Integrated Profile Potential $\Psi_R(S) = \int_0^R N_u(S) du = \sum_{m=1}^M (R - F_m)_+$**:
   - Verified that $\mathcal{L} \Psi_R(S) = \int_0^R r_u(S) du$ holds identically across 153 states with 0 error.
   - Bounded globally by $\mathcal{L} \Psi_R(S) \le R^2 / 2$.
2. **Candidate 2: Mark-Energy Potential $\Phi_\alpha(S) = \sum (R - F_m) + \alpha \sum (z - l)$**:
   - Analyzed drift: continuous arrivals inject energy at rate $\alpha \sum (F_{j+1} - F_j)^2 / 2 > 0$.
   - Verified that $\mathcal{L} \Phi_\alpha(S) > 0$ for all tested $\alpha > 0$.
   - Concluded: without boundary damping, $\Phi_\alpha$ cannot serve as a supermartingale.
3. **Candidate 3: Monotone Comparison Process $\Xi_\rho(S_t, t) = \rho u - N_u(S_t) + \frac{t}{4\rho} + B(S_t)$**:
   - Verified that uncorrected comparison ($B \equiv 0$) proves the classical benchmark $c_{21} \le 1$.
   - Disproved uniform sub-1 pointwise bound: proved $\sup_S r_u(S)/u = 1.0$ on the single-arrival state $S = \operatorname{step}(u)$.
   - Evaluated boundary leakage: demonstrated boundary starvation at $y = 0$ and boundary truncation at $y = R$.
   - Proved that finite-host averages (0.941 at $n=4096$) suffer from boundary leakage analogous to LIS ($1.83 < 2$), and cannot certify $c_{21} < 1$ without an explicit boundary correction.

## Milestone Status
- **R1 (Marked Drift & Lyapunov Formulation)**: COMPLETE.
- **R2 (Computational Verification Tool)**: COMPLETE (`experiments/w44-c21-drift/verify.py`).
- **R3 (Repo Norms & Regressions)**: COMPLETE (all regression suites passing; boundary leakage documented).
- **R4 (Documentation & Registration)**: COMPLETE (`proof.md`, `log.md`, `README.md`, `SESSION-STATE.md`, `RESULTS.md`).
