# Workstream W55 Plan: Growing LDS Threshold Sieve & Dihedral Sieve

## 1. Context and Motivation

In Workstream W52, we established the Bounded-LDS Sharp Threshold $C^* = 1/4$ for any fixed $d = \mathcal{O}(1)$.
In Workstream W54, we eliminated the adversarial counterexample route, proving that the monotone identity is the true extremal bottleneck and confirming that non-monotone patterns cluster less and are more easily contained.

In Workstream W55, we tackle **Avenue 2: The Growing LDS Threshold Sieve ($d(k) \to \infty$)**, closing the gap between fixed $d = \mathcal{O}(1)$ and the full symmetric group $S_k$.

---

## 2. Key Mathematical Breakthroughs to Develop

### 2.1 The Dihedral Duality Theorem (Erdős–Szekeres Reduction)
Every permutation $\pi \in S_k$ satisfies $\operatorname{LIS}(\pi) \cdot \operatorname{LDS}(\pi) \ge k$ by the Erdős–Szekeres theorem.
Consequently:
$$\min\big(\operatorname{LIS}(\pi), \operatorname{LDS}(\pi)\big) \le \lfloor \sqrt{k} \rfloor.$$
Because a uniform random host $\sigma_n \sim \operatorname{Uniform}(S_n)$ is strictly invariant under all 8 operations of the dihedral symmetry group $D_4$ (reversal, complement, inverse), containing $\pi$ is probabilistically equivalent to containing its reverse $\pi^{\mathrm{rev}}$ (which swaps LIS and LDS).
Therefore, **simultaneous universality over all $k!$ permutations reduces to simultaneous universality over the half-space $\operatorname{LDS}(\pi) \le \lfloor \sqrt{k} \rfloor$**.
The maximum number of Greene chains is unconditionally compressed from $k$ down to $d_{\max} \le \sqrt{k}$.

### 2.2 The Growing LDS Capacity Scaling Law
For $d \le \sqrt{k}$, the mean chain length satisfies:
$$\bar{a} = \frac{k}{d} \ge \frac{k}{\sqrt{k}} = \sqrt{k}.$$
For macroscopic chains of length $a_i \ge \sqrt{k}$, the Deuschel–Zeitouni LIS lower-tail large deviation probability scales as:
$$\Pr\big(\operatorname{LIS}(B_i) < a_i\big) \le \exp\big(-c \varepsilon^2 a_i^2\big) \le \exp\big(-c \varepsilon^2 k\big).$$
The cumulative failure across all $d \le \sqrt{k}$ boxes satisfies:
$$\sum_{i=1}^d \Pr\big(\operatorname{LIS}(B_i) < a_i\big) \le \sqrt{k} \exp\big(-c \varepsilon^2 k\big) = o(1).$$

### 2.3 Macroscopic vs Microscopic Chain Sieve
Chains are partitioned into:
- **Macroscopic chains** ($a_i \ge K\sqrt{\log k}$): Embedded into disjoint antidiagonal quadratic boxes of area $(a_i/k)^2$, where Deuschel–Zeitouni concentration holds unconditionally.
- **Microscopic chains** ($a_i < K\sqrt{\log k}$): Total length is at most $d \cdot K\sqrt{\log k} \le K\sqrt{k\log k} = o(k)$. Embedded via full-width shared strips with $k^{1/4}$ capacity surplus.

---

## 3. Acceptance Criteria

- [ ] Automated verification script `experiments/w55-growing-lds/verify.py` verifies:
  1. Exhaustive dihedral duality across all $k!$ permutations for $k \in \{4, 5, 6, 7\}$ confirming $\min(\operatorname{LIS}, \operatorname{LDS}) \le \lfloor\sqrt{k}\rfloor$.
  2. RSK limit shape census for typical random permutations confirming $d \le 2\sqrt{k}$.
  3. Growing LDS split scaling for $d \in \{2, 3, \dots, \lfloor\sqrt{k}\rfloor\}$ across $k \in \{16, 64, 144, 256, 400\}$.
  4. Deuschel–Zeitouni quadratic tail bound $\exp(-\Omega(\varepsilon^2 k))$ dominating the growing LDS family.
- [ ] Mathematical proofs recorded in `experiments/w55-growing-lds/proof.md`.
- [ ] Chronological audit trail in `experiments/w55-growing-lds/log.md`.
- [ ] 0 regressions across all 16 existing repository test suites, Lean 4 build, and paper check.
