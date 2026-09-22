# Limit Shape and Asymptotics of the Longest Increasing Subsequence

Type: reference
Confidence: high
Source: Candidates 0, 1, 2, 3, 4, 5, 6, 7 (Level 0)
Relevant to: LIS asymptotics, hydrodynamic traversal velocity $2\sqrt{C}$, information-theoretic barrier $C = 1/4$.

## Bibliographic Info
- Authors: B. F. Logan, L. A. Shepp; A. M. Vershik, S. V. Kerov
- Title: A variational problem for random Young tableaux (Logan & Shepp) / Asymptotics of the Plancherel measure of the symmetric group and the limiting form of Young tableaux (Vershik & Kerov)
- Year: 1977
- ArXiv/DOI: Adv. Math. 26 (1977), no. 2, 206-222; Soviet Math. Dokl. 18 (1977), 527-531
- Theorem/Lemma Number: Main Limit Theorem
- Verified via web search: yes

## Key Result
For a uniform random permutation $\sigma_n \in S_n$, the length of the longest increasing subsequence satisfies:
$$\lim_{n \to \infty} \frac{\operatorname{LIS}(\sigma_n)}{\sqrt{n}} = 2 \quad \text{almost surely and in probability}.$$
Equivalently, in a Poisson point process of intensity $\mu$ on a unit square, the maximal directed increasing path length scales as $2\sqrt{\mu}$.

## Hypotheses / Conditions
- Uniform random permutation model on $S_n$ or homogeneous planar Poisson point process.
- Strictly applies to increasing (monotone) paths.

## How It Applies
1. Sets the sharp information-theoretic lower bound $n \ge (1/4 - o(1))k^2$ for $k$-superpatterns, because containing $\operatorname{id}_k$ requires $\operatorname{LIS}(\sigma_n) \ge k$, whence $2\sqrt{n} \ge k \implies n \ge k^2/4$.
2. Governs the hydrodynamic limit velocity $v = 2\sqrt{C}$ in Poisson hosts.

## Caveats
Applies exclusively to monotone subsequences (increasing or decreasing). Does not provide traversal velocity for non-monotone target permutation trajectories.
