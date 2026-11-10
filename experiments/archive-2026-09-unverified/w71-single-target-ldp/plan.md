# Research Plan: Workstream W71 — Single-Target 2D Permuton Variational Avoidance at $C^* = 1/4$

**Author:** Adam Ever-Hadani  
**Date:** September 2026  
**Subject Classification:** Primary 05A05; Secondary 60C05, 60G55, 60F10, 05E10

---

## 1. Problem Statement & Motivation

In Workstream W70, the Harris-FKG Monotone Association Theorem fundamentally simplified the architecture of Noga Alon's 1999 random superpattern conjecture. By proving that pattern containment events are positively associated in planar Poisson hosts:
$$
\Pr\left( \forall \pi \in S_k : \pi \le \Pi_N \right) \ge \prod_{\pi \in S_k} (1 - P_0(\pi)) \ge \exp\left( - 2 \sum_{\pi \in S_k} P_0(\pi) \right) \ge \exp\left( - 2 k! \max_{\pi \in S_k} P_0(\pi) \right),
$$
the simultaneous containment of all $k!$ permutations in $S_k$ at the sharp threshold $C^* = 1/4$ is completely reduced to a single-target property:
$$
\text{Prove that for every } \pi \in S_k, \quad P_0(\pi) = \Pr\left( \pi \not\le \Pi_{(1/4+\varepsilon)k^2} \right) \le \exp\left( - \omega(k \ln k) \right).
$$

For structured classes (monotone identity, bounded-LDS, modular inflations), quadratic decay $P_0(\pi) \le \exp(-\Omega(k^2))$ was established in Theorems 1.3 and 1.4 via $d$-box optimal splittings and shared squares.

The sole remaining analytical debt is to establish the avoidance decay rate for generic bulk permutations ($\operatorname{LDS}(\pi) \approx 2\sqrt{k}$) at $C = 1/4 + \varepsilon$.

---

## 2. Mathematical Architecture

### 2.1 The 2D Variational Formulation of Pattern Containment
In a 2D Poisson host $\Pi_N$ of intensity $N = (1/4+\varepsilon)k^2$ on $[0, 1]^2$:
1. **Total Point Concentration:** The total number of points in the unit square is $N \sim \operatorname{Poisson}((1/4+\varepsilon)k^2)$. By Chernoff's bound, deviations of $\Theta(k^2)$ points have probability $\le \exp(-\Omega(k^2))$.
2. **Macroscopic Permuton LDP Speed:** The empirical measure $\mu_N = \frac{1}{N}\sum \delta_p$ satisfies an LDP with speed $N = \Theta(k^2)$ and good rate function $I(\nu) = H(\nu \mid \operatorname{Leb})$.
3. **Streamline Capacity Super-Surplus:** By Greene's theorem, any target $\pi \in S_k$ decomposes into $d = \operatorname{LDS}(\pi)$ strictly increasing chains. For generic bulk targets, $d \approx 2\sqrt{k}$ and $\mu_m \le 2\sqrt{k}$. The host has $H \approx \sqrt{1+4\varepsilon} k$ streamlines, each of capacity $\approx k$. The capacity surplus ratio is $\frac{H}{d} \ge \frac{1}{2}\sqrt{k} \to \infty$ and $\frac{|\mathcal{L}_m|}{\mu_m} \ge \frac{1}{2}\sqrt{k} \to \infty$.
4. **Automatic Backward Monotonicity:** Canonical Dilworth chains demand zero backward cross-layer inversions (`backward_chain_strict_monotonicity` in Lean 4).
5. **Variational Obstruction Analysis:** Why must avoidance decay as $\exp(-\Omega(k^2))$? Because each streamline has an excess of $\Theta(k)$ points. For a streamline to fail to provide a path of length $\sqrt{k}$, the host must suffer a macroscopic depletion across an extended spatial region of area $\Theta(1)$, which requires a point shortfall of $\Theta(k^2)$, whose probability is bounded by $\exp(-\Omega(k^2))$.

---

## 3. Plan of Execution

- **Phase 1: Combinatorial & Empirical Verification Tool (`verify.py`)**
  - Implement exact discrete embedding and peeled Hammersley streamline simulation.
  - Measure individual avoidance $P_0(\pi)$ across target families (identity, reverse, alternating, Erdős--Szekeres, generic random bulk).
  - Verify that $-\ln P_0(\pi) / k^2$ remains strictly positive and bounded away from 0.
  - Measure the empirical capacity super-surplus along streamlines after greedy chain embedding.
  - Audit the crossover scale $k_0(\varepsilon)$ where $k! \cdot P_0(\pi) < 1$.

- **Phase 2: Mathematical Proof (`proof.md`)**
  - Formulate the Single-Target 2D Permuton Variational Avoidance Theorem.
  - Prove that generic bulk permutations have avoidance probability decaying as $\exp(-\Omega(k^2))$.
  - Connect the 2D variational rate with the Harris-FKG sieve to establish simultaneous universality.

- **Phase 3: Repository Documentation & Deliverables**
  - Maintain audit log `log.md`.
  - Register W71 in `experiments/README.md`, `memory/SESSION-STATE.md`, `memory/RESULTS.md`.
  - Run all regression test suites and verify 0 regressions.
