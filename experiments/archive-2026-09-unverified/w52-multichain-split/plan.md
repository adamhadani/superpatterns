# Workstream W52 Plan: Multi-Chain Optimal Splittings & the $(d+1)d\dots 1$-Avoiding Sharp Threshold ($d \ge 3$)

## 1. Context & Motivation

In Workstream W51, we proved that for all 321-avoiding permutations ($S_k(321)$, corresponding to $\operatorname{LDS}(\pi) \le 2$), the sharp containment threshold in a random permutation host $\sigma_n$ is:
$$C^* = \frac{1}{4} = 0.25000 \quad \text{identically.}$$

Every permutation $\pi \in S_k$ can be canonically partitioned into $d = \operatorname{LDS}(\pi)$ increasing chains $M_1, M_2, \dots, M_d$ via Greene's theorem / Dilworth's theorem (or equivalently, Patience Sorting).
- For $d = 1$: $\pi = \operatorname{id}_k$, classical LIS threshold is $C^* = 1/4$ (Logan--Shepp / Vershik--Kerov).
- For $d = 2$: $S_k(321)$, $C^* = 1/4$ proved in W51 via the Two-Box Optimal Split Theorem and Riffle Shuffle surplus.
- For $d \ge 3$: $S_k((d+1)d\dots 1)$ (permutations avoiding the decreasing pattern of length $d+1$).

Workstream W52 generalizes the optimal spatial split geometry and capacity analysis from $d=2$ to general $d \ge 3$.

---

## 2. Mathematical Architecture

### 2.1 The $d$-Box Antidiagonal Optimal Split Theorem
Consider the worst-case structural configuration: the $d$-chain skew sum:
$$\pi = M_1 \ominus M_2 \ominus \dots \ominus M_d,$$
where each $M_i$ is an increasing chain of length $a_i \ge 1$ with $\sum_{i=1}^d a_i = k$.
Let $\alpha_i = a_i / k \in (0, 1)$ with $\sum_{i=1}^d \alpha_i = 1$.

We allocate $d$ pairwise disjoint bounding boxes $B_1, \dots, B_d \subset [0, 1]^2$ along the antidiagonal:
$$B_i = [X_{i-1}, X_i] \times [Y_i, Y_{i-1}],$$
where:
$$X_0 = 0, \quad X_i = \sum_{j=1}^i \alpha_j, \quad Y_d = 0, \quad Y_i = 1 - \sum_{j=1}^i \alpha_j = \sum_{j=i+1}^d \alpha_j, \quad Y_0 = 1.$$
Notice that:
$$\operatorname{Width}(B_i) = X_i - X_{i-1} = \alpha_i = \frac{a_i}{k},$$
$$\operatorname{Height}(B_i) = Y_{i-1} - Y_i = \alpha_i = \frac{a_i}{k}.$$

Each box $B_i$ is a square of side length $\alpha_i$, with exact area:
$$\operatorname{Area}(B_i) = \alpha_i^2 = \left(\frac{a_i}{k}\right)^2.$$
Notice that the sum of areas is:
$$\sum_{i=1}^d \operatorname{Area}(B_i) = \sum_{i=1}^d \alpha_i^2 \le \left(\sum_{i=1}^d \alpha_i\right)^2 = 1.0.$$

### 2.2 Expected LIS Capacity and Universal $C^* = 1/4$ Invariant
In a Poisson host of intensity $n = C k^2$, the expected point count in box $B_i$ is:
$$\lambda_i = n \operatorname{Area}(B_i) = C k^2 \alpha_i^2 = C a_i^2.$$
By the Vershik--Kerov / Logan--Shepp theorem, the expected LIS capacity in box $B_i$ is:
$$\mathbb{E}[\operatorname{LIS}(B_i)] = 2 \sqrt{\lambda_i} = 2 \sqrt{C a_i^2} = 2 \sqrt{C} a_i.$$

To simultaneously embed every chain $M_i$ (of length $a_i$), we require:
$$\mathbb{E}[\operatorname{LIS}(B_i)] > a_i \iff 2 \sqrt{C} a_i > a_i \iff 2 \sqrt{C} > 1 \iff C > \frac{1}{4} = 0.25000.$$
**Crucial Invariant**: The condition $2\sqrt{C} > 1$ is completely independent of the chain length $a_i$, independent of the partition $(\alpha_1, \dots, \alpha_d)$, and **independent of the chain count $d$**!

### 2.3 Topological Entropy: The Marcus--Tardos / Stanley--Wilf Theorem
Unlike the generic symmetric group $S_k$ where $|S_k| = k!$ has factorial entropy $\ln(k!) = \Theta(k \ln k)$, the class of permutations avoiding $(d+1)d\dots 1$ has **linear topological entropy**:
$$|S_k((d+1)d\dots 1)| \le (d-1)^{2k} = \exp(2 k \ln(d-1)) = \exp(\mathcal{O}_d(k)).$$
For $d = 3$ (4321-avoiding permutations), by Gessel's exact formula:
$$|S_k(4321)| = \frac{1}{(k+1)^2 (k+2)} \sum_{j=0}^k \binom{2j}{j} \binom{k+1}{j} \binom{k+2}{j+1} \approx \frac{9^k}{\operatorname{poly}(k)}.$$
Topological entropy rate:
$$h_{4321} = \lim_{k \to \infty} \frac{\ln |S_k(4321)|}{k} = \ln 9 \approx 2.1972 \text{ nats/point}.$$
Because the entropy is strictly linear $\mathcal{O}(k)$, the Shannon factorial deficit is **completely absent** for any fixed $d$!

---

## 3. Workstream Deliverables

1. **Automated Verification Harness (`verify.py`)**:
   - **Part 1**: Exhaustive Combinatorial Census of $S_k(4321)$ for $k \in \{4, 5, 6, 7\}$, matching Gessel's formula (counts: $23, 103, 513, 2761$), testing Patience sorting decomposition into $\le 3$ chains.
   - **Part 2**: $d$-Box Antidiagonal Split Geometry verification across 3-partitions $(a, b, c)$ with $a+b+c = 100$, confirming exact area formulas and capacity surplus $2\sqrt{C} > 1$ for all partitions.
   - **Part 3**: Multi-Chain Extremal Families (skew sums, 3-way generalized riffle shuffles, alternating zigzag) evaluating surplus drift across scales $k \in \{30, 60, 120, 240\}$.
   - **Part 4**: Empirical Containment of all 23 permutations in $S_4(4321)$ on random host permutations at intensities $C \in \{0.35, 0.50, 0.75, 1.00\}$.
   - **Part 5**: Entropy Deficit vs Concentration Analysis for $d=3, 4, 5$, certifying $|\mathcal{H}| \le e^{\mathcal{O}(\varepsilon^2 k)} = o(1)$ simultaneous common host bounds.
2. **Mathematical Proofs (`proof.md`)**:
   - $d$-Box Optimal Antidiagonal Split Theorem.
   - Multi-Chain Generalized Riffle Surplus Theorem.
   - Bounded-LDS Linear Entropy Theorem.
   - Discharge of multi-chain debt towards `[GAP: OBLIGATION_01]`.
3. **Audit Trail (`log.md`)**: Complete chronological audit log.
4. **Repository Ledger Updates**: `experiments/README.md`, `memory/RESULTS.md`, `memory/SESSION-STATE.md`.
