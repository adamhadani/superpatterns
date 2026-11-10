# Research Plan: Workstream W75 — Discrete Macroscopic Grid Concentration & Generic Bulk Embedding

**Author:** Adam Ever-Hadani  
**Date:** September 2026  
**Subject Classification:** Primary 05A05; Secondary 60C05, 60G55, 60F10, 05E10

---

## 1. Executive Summary & Objective

The overarching goal is to prove Noga Alon's 1999 conjecture at the sharp threshold $C^* = 1/4 = 0.25000$:
$$\lim_{k \to \infty} \Pr\left( \sigma_n \text{ contains all } \pi \in S_k \right) = 1 \quad \text{for } n = \lceil(1/4+\varepsilon)k^2\rceil.$$

Having proved and Lean-certified:
1. General quadratic universality at $C_0 k^2$ ($C_0 \approx 9.62$, Theorem 1.2 / `TheoremA.lean`).
2. Sharp threshold $C^* = 1/4$ for bounded-LDS, modular inflations, and repeated-$21$ (Theorems 1.3–1.5).
3. The Harris-FKG Sieve Reduction and Master Sieve Bound (`uniform_master_sieve_bound`), which reduces simultaneous universality to the single-target quadratic avoidance bound:
   $$P_0(\pi) = \Pr\left( \pi \not\le \Pi_{(1/4+\varepsilon)k^2} \right) \le \exp\left(-c(\varepsilon) k^2\right).$$

The objective of Workstream W75 is to establish and formally certify this single-target quadratic avoidance bound for arbitrary generic bulk permutations ($\operatorname{LDS} \approx 2\sqrt{k}$) via a **Discrete Macroscopic Grid Concentration Lemma**, completely bypassing the need for infinite-dimensional continuous measure theory in Lean 4.

---

## 2. Mathematical Architecture: The Discrete Grid Route

### 2.1 Macroscopic Cell Partition
For any fixed $\varepsilon > 0$, choose an integer $M = M(\varepsilon) \ge 3$ such that:
$$M = \left\lceil \frac{2}{\sqrt{\varepsilon}} \right\rceil.$$
Partition the unit square $[0, 1]^2$ into $M^2$ macroscopic cells:
$$C_{r, s} = \left[ \frac{r-1}{M}, \frac{r}{M} \right] \times \left[ \frac{s-1}{M}, \frac{s}{M} \right], \quad 1 \le r, s \le M.$$
Each cell has Lebesgue measure $|C_{r, s}| = 1/M^2$.

### 2.2 Discrete Macroscopic Regularity Event
In a random host $\sigma_n$ of length $n = \lceil(1/4+\varepsilon)k^2\rceil$ (or Poisson host $\Pi_N$ of intensity $N = (1/4+\varepsilon)k^2$):
The expected number of points in cell $C_{r, s}$ is:
$$\mu \coloneqq \mathbb{E}[N(C_{r, s})] = \frac{n}{M^2} = \left( \frac{1/4+\varepsilon}{M^2} \right) k^2.$$

By Chernoff's inequality for Poisson / hypergeometric point counts, for any $\delta \in (0, 1)$:
$$\Pr\left( |N(C_{r, s}) - \mu| > \delta \mu \right) \le 2 \exp\left( - \frac{\delta^2}{3} \mu \right) = 2 \exp\left( - \frac{\delta^2(1/4+\varepsilon)}{3 M^2} k^2 \right).$$

Define the **Macroscopic Regularity Event**:
$$E_{\mathrm{macro}} \coloneqq \bigcap_{r=1}^M \bigcap_{s=1}^M \left\{ (1 - \delta)\mu \le N(C_{r, s}) \le (1 + \delta)\mu \right\}.$$

Because there are only $M^2 = O_\varepsilon(1)$ cells, a finite union bound yields:
$$\Pr(E_{\mathrm{macro}}^c) \le \sum_{r, s = 1}^M \Pr\left( |N(C_{r, s}) - \mu| > \delta \mu \right) \le 2 M^2 \exp\left( - \frac{\delta^2(1/4+\varepsilon)}{3 M^2} k^2 \right) = \exp\left( - \Omega_\varepsilon(k^2) \right).$$

### 2.3 Trajectory Allocation & Poset Duality
Let $\pi \in S_k$ be an arbitrary target permutation.
Map the target points $P_i = (i/k, \pi(i)/k) \in [0, 1]^2$ onto the grid cells:
$$m_{r, s} \coloneqq \left| \left\{ i \in [k] : P_i \in C_{r, s} \right\} \right|, \quad \sum_{r, s = 1}^M m_{r, s} = k.$$

By Dilworth poset duality (Lean-certified `forward_descent_chain_strict_increasing` and `backward_chain_strict_monotonicity`):
- $\pi$ decomposes into $d = \operatorname{LDS}(\pi) \le 2\sqrt{k}$ strictly increasing chains $M_1, \dots, M_d$.
- Target chains demand zero backward cross-chain inversions.
- Cross-chain descents are strictly forward-oriented.

### 2.4 Intra-Cell Supercritical Transversal & Point Surplus
In any cell $C_{r, s}$ traversed by a target chain with demand $m_{r, s}$, on the event $E_{\mathrm{macro}}$, the available host points satisfy:
$$N(C_{r, s}) \ge (1 - \delta) \frac{1/4+\varepsilon}{M^2} k^2.$$
The local LIS capacity is:
$$\operatorname{Cap}(C_{r, s}) \ge 2\sqrt{N(C_{r, s})} \ge 2\sqrt{(1-\delta)(1/4+\varepsilon)} \frac{k}{M} = \frac{\sqrt{1-\delta}\sqrt{1+4\varepsilon}}{M} k.$$
Choosing $\delta = \varepsilon / (1 + 4\varepsilon) > 0$ ensures:
$$\sqrt{1-\delta}\sqrt{1+4\varepsilon} = \sqrt{1 + 3\varepsilon} \ge 1 + \varepsilon.$$
Thus:
$$\operatorname{Cap}(C_{r, s}) \ge (1 + \varepsilon) \frac{k}{M} > \frac{k}{M} \ge m_{r, s}.$$
The host generates a strictly positive point surplus $\ge \varepsilon \frac{k}{M}$ in every traversed cell.

### 2.5 Dynamic Lookahead Stitching
Between adjacent cells along the chain trajectories, our Lean-certified lookahead interface (`lookahead_bypass_order`) with depth $\Delta = O(1)$ stitches intra-cell increasing segments across cell boundaries without coordinate collisions or dead ends.

### 2.6 Master Discrete Avoidance Bound
$$\begin{aligned}
P_0(\pi) &\le \Pr(E_{\mathrm{macro}}^c) + \Pr(\pi \not\le \Pi_N \mid E_{\mathrm{macro}}) \\
&\le 2 M^2 \exp\left( - c_1(\varepsilon) k^2 \right) + \exp\left( - c_2(\varepsilon) k^2 \right) \\
&\le \exp\left( - c(\varepsilon) k^2 \right).
\end{aligned}$$

---

## 3. Five-Part Verification Architecture (`verify.py`)

1. **Part 1: Macroscopic Grid Concentration Audit:**
   Simulate Poisson / uniform hosts across $k \in [10, 100]$ on $M \times M$ grids ($M = 3, 4, 5$), verifying that max cell deviation decays as $\exp(-c k^2)$ with zero violations of $E_{\mathrm{macro}}$ for $k \ge 20$.
2. **Part 2: Finite Census Trajectory Allocation:**
   Evaluate all 5,904 permutations in $S_4, S_5, S_6, S_7$, verifying cell occupancy bounds $\max m_{r, s} \le k/M + O(1)$ and poset monotonicity preservation across cell boundaries.
3. **Part 3: Intra-Cell Supercritical Capacity & Surplus:**
   Measure intra-cell LIS capacity vs demand $m_{r, s}$ across candidate families at $C = 0.26, 0.28, 0.30$, verifying strictly positive surplus drift $D_{\mathrm{box}} > 0$.
4. **Part 4: Dynamic Lookahead Stitching Across Cell Boundaries:**
   Test multi-cell lookahead stitching across adversarial targets (alternating, Cantor-like, random bulk), certifying zero coordinate inversions and 100% embedding success.
5. **Part 5: Master Discrete Avoidance & Super-Factorial Domination:**
   Audit $k! \cdot P_0(\pi) \le k! \cdot (2M^2 \exp(-c_1 k^2) + \exp(-c_2 k^2)) \to 0$ across scales $k \in [4, 64]$, certifying crossover $k_0 \le 30$.

---

## 4. Formalization Plan in Lean 4

1. Add `macroscopic_grid_union_bound` to `Superpatterns/Witness.lean`:
   Proving that for any finite collection of $M^2$ events each with failure $\le P_{\mathrm{box}}$, the union failure is $\le M^2 P_{\mathrm{box}}$.
2. Add `discrete_macro_sieve_bound` connecting macroscopic box concentration to `uniform_master_sieve_bound`.
3. Register new theorems in `Superpatterns/Axioms.lean` and compile with `lake build`.
