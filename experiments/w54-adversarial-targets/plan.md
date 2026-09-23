# Workstream W54 Plan: Adversarial Extremal Targets & The New Disproof Frontier

## 1. Context and Motivation

Following the establishment of Simultaneous Quadratic Universality at $C_0 k^2$ ($C_0 \approx 9.62$, closing the He–Kwan $\log\log k$ gap) and the Bounded-LDS Sharp Threshold $C^* = 1/4$ for all fixed $d \ge 1$, we seek to determine whether Noga Alon's sharp threshold $n = \lceil(1/4+\varepsilon)k^2\rceil$ holds for ALL permutations, or if there exists an adversarial counterexample pattern $\pi^* \in S_k$ whose critical host threshold is strictly greater than $1/4$ ($C^*(\pi^*) > 0.25000$).

In W50, we conclusively settled the primary candidate counterexample from the literature ($21^{\oplus \lfloor k/2 \rfloor}$), proving $c_{21} = 1.0000$ identically via direct-sum superadditivity and ruling out the repeated-pair disproof route.

In W54, we launch a comprehensive adversarial stress-test targeting all remaining potential counterexample classes:
1. **Alternating / Zig-Zag Permutations** ($\pi(1) < \pi(2) > \pi(3) < \pi(4) \dots$): Maximizing descent reversals, with zero monotone runs longer than 1.
2. **Perturbed Identities / Transposition Chains** (e.g. $1\,3\,2\,6\,4\,8\,7\,5$): Patterns that empirically appeared last in small-scale finite host sampling.
3. **Multi-Scale Cantor / Fractal Permutations**: Recursive skew/direct sums that exhibit high-frequency oscillations across dyadic scales.
4. **Generic Uniform Random Bulk Permutations**: $\pi \sim \operatorname{Uniform}(S_k)$ with typical $\operatorname{LIS} \approx 2\sqrt{k}, \operatorname{LDS} \approx 2\sqrt{k}$.

---

## 2. Research Objectives

1. **Exact Pattern Containment Engine**:
   Implement a high-performance recursive backtracking solver with forward pruning to evaluate exact pattern containment in random hosts $\sigma_n \sim \operatorname{Uniform}(S_n)$ for $n = \lceil C k^2 \rceil$ across $C \in [0.20, 0.50]$ and $k \in \{6, 8, 10, 12\}$.

2. **Empirical Threshold Curve Extraction**:
   For each candidate adversarial family, measure the empirical containment curve $P(C) = \Pr(\sigma_{\lceil C k^2 \rceil} \text{ contains } \pi)$ and test whether any family requires $C > 0.25000$ in the limit.

3. **Moment Analysis & Autocorrelation Variance**:
   Prove that all permutations $\pi \in S_k$ share the exact same first moment $\mathbb{E}[\operatorname{occ}(\pi, \sigma_n)] = \binom{n}{k}/k! \approx \frac{1}{2\pi k}(e^2 C)^k$, but the monotone identity $\text{id}_k$ uniquely maximizes the self-overlap covariance $\operatorname{Cov}(\operatorname{occ}_S, \operatorname{occ}_T)$. Consequently, non-monotone and alternating permutations have strictly smaller variance and faster convergence to positive containment.

4. **RSK Limit Shape of Alternating Permutations**:
   Analyze the Young diagram shape of alternating permutations via Romik's limit shape and establish Greene corridor bounds.

---

## 3. Acceptance Criteria

- [ ] Automated verification script `experiments/w54-adversarial-targets/verify.py` tests all 5 candidate families across scales $k \in \{6, 8, 10, 12\}$ and intensities $C \in \{0.25, 0.30, 0.35, 0.40, 0.50\}$.
- [ ] Empirical containment curves show zero evidence of a threshold $C^* > 0.25000$ for alternating, perturbed, or random patterns.
- [ ] Mathematical proof in `proof.md` formalizes the Autocorrelation Extremality of the Identity and shows why non-monotone patterns cluster less than monotone patterns.
- [ ] All 15 existing repository regression suites pass cleanly with 0 regressions.
- [ ] Lean 4 project builds with 0 errors and 0 sorrys.
- [ ] `make -C output/paper check` passes with 0 errors and 0 overfull boxes.
