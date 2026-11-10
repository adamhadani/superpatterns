# Workstream W56 Plan: Multi-Layer Hammersley Coupling & Dynamic Hydrodynamic Routing

## 1. Context and Motivation

Workstream W54 proved that the monotone identity is the true extremal bottleneck for pattern containment, eliminating candidate adversarial counterexamples (alternating, perturbed, and Cantor fractals).
Workstream W55 proved that the sharp $(1/4+\varepsilon)k^2$ threshold extends to all growing-LDS modular inflations with blocks $\ge K\sqrt{\log k}$, completely bypassing the Shannon factorial deficit via the Shared Host Squares Architecture.

The remaining open challenge is the **Generic Atomized Bulk**: permutations with unbounded LDS ($d \approx 2\sqrt{k}$) whose monotone blocks are microscopic ($< K\sqrt{\log k}$).
In W53, static horizontal corridors $S_i = [0, 1] \times [y_{i-1}, y_i]$ failed on the generic bulk due to the Double Interleaving Obstruction (vertical value and horizontal position interleaving).

In Workstream W56, we attack this obstruction via **Avenue 1: Multi-Layer Hammersley Particle Hydrodynamics**.
Instead of confining chains to static thin strips of area $1/d$, we couple them to the **continuous multi-layer Hammersley lines** $\mathcal{L}_1, \dots, \mathcal{L}_d$ of the planar Poisson host, which span the FULL width and height of the unit square.

---

## 2. Mathematical Architecture

### 2.1 Multi-Layer Hammersley Process
Let $\Pi_n$ be a homogeneous Poisson process on $[0, 1]^2$ with intensity $n = C k^2$.
By the Robinson–Schensted correspondence and Greene's theorem (1974), $\Pi_n$ decomposes into multi-layer Hammersley lines $\mathcal{L}_1, \mathcal{L}_2, \dots$:
- $\mathcal{L}_1$ is the first Hammersley line (longest increasing path).
- Successive layers $\mathcal{L}_m$ are obtained by peeling off earlier layers.
- For each $m \le d = \mathcal{O}(\sqrt{k})$, the length of line $\mathcal{L}_m$ satisfies the Baik–Deift–Johansson / Aldous–Diaconis hydrodynamic limit:
  $$\mathbb{E}[|\mathcal{L}_m|] = 2\sqrt{C} k \cdot \Omega\left(\frac{m}{2\sqrt{C} k}\right) = 2\sqrt{C} k \big(1 - \mathcal{O}(m/k)\big).$$

### 2.2 The $\sqrt{k}$ Capacity Super-Surplus Law
For an atomized permutation $\pi \in S_k$ with Greene partition shape $\lambda \vdash k$:
- The target chain demand is $\lambda_i(\pi) \le \lambda_1(\pi) \approx 2\sqrt{k}$.
- The available capacity in Hammersley layer $\mathcal{L}_i$ is $|\mathcal{L}_i| \approx 2\sqrt{C} k$.
- The capacity ratio is:
  $$\frac{\operatorname{Cap}(\mathcal{L}_i)}{\lambda_i(\pi)} \ge \frac{2\sqrt{C} k}{2\sqrt{k}} = \sqrt{C} \sqrt{k} \xrightarrow{k \to \infty} \infty.$$
At $C = 1/4 = 0.25$, the capacity ratio is $\frac{1}{2}\sqrt{k} \to \infty$ ($5\times$ at $k=100$, $10\times$ at $k=400$, $50\times$ at $k=10000$).
Every Hammersley line has an exploding polynomial surplus of points.

### 2.3 Dynamic Interleaving Routing
Because each Hammersley line $\mathcal{L}_i$ spans the entire unit square $[0, 1]^2$, target points on chain $M_i$ are not confined to pre-assigned coordinate strips.
We study the dynamic routing problem of selecting a subset of points on $\mathcal{L}_1 \cup \dots \cup \mathcal{L}_d$ matching the relative ordering of $\pi$.

---

## 3. Acceptance Criteria

- [ ] Automated verification script `experiments/w56-hammersley-coupling/verify.py` implements:
  1. Multi-layer Hammersley line extraction on random hosts of intensity $n = C k^2$.
  2. Verification of the Baik–Deift–Johansson hydrodynamic row length scaling $\lambda_i \approx 2\sqrt{C} k$ for $i \le 2\sqrt{k}$.
  3. Empirical capacity surplus ratio scaling $\ge \sqrt{C} \sqrt{k}$ across scales up to $k = 10,000$.
  4. Dynamic Greene chain routing test on random permutations in $S_k$.
- [ ] Formal mathematical statements, proofs, and hydrodynamic equations recorded in `experiments/w56-hammersley-coupling/proof.md`.
- [ ] Chronological audit trail maintained in `experiments/w56-hammersley-coupling/log.md`.
- [ ] 0 regressions across all 17 existing repository test suites, Lean 4 build, and paper check.
