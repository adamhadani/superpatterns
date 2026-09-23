# Sharp LIS Information-Theoretic Lower Bound for Superpatterns

Type: theorem
Confidence: high
Source: Candidates 0, 1, 2, 3, 4, 5, 6, 7 (Level 0); explore_merger_r3_L04_N00, explore_falser_r3_L04_N00 (Round 3 Level 4)
Relevant to: Establishing the sharpness of the $C = 1/4$ constant in Noga Alon's superpattern conjecture.

## Statement
Let $\sigma_n \sim \operatorname{Uniform}(S_n)$ be a uniform random permutation of length $n$. For any fixed constant $C < 1/4$, if $n = \lfloor C k^2 \rfloor$, then:
$$\lim_{k \to \infty} \Pr\left(\sigma_n \text{ contains } \operatorname{id}_k\right) = 0.$$
Consequently, no host length $n < (1/4 - o(1))k^2$ can be a $k$-superpattern with non-vanishing probability, making $C = 1/4$ the sharp information-theoretic threshold.

## Proof
Every $k$-superpattern $\sigma \in S_n$ must contain the identity permutation $\operatorname{id}_k = (1, 2, \dots, k)$ as an induced sub-pattern.
An induced copy of $\operatorname{id}_k$ in $\sigma_n$ corresponds to an increasing subsequence of length $k$.
Therefore, containing $\operatorname{id}_k$ implies $\operatorname{LIS}(\sigma_n) \ge k$.
By the Logan--Shepp (1977) and Vershik--Kerov (1977) limit shape theorem:
$$\frac{\operatorname{LIS}(\sigma_n)}{\sqrt{n}} \xrightarrow{n \to \infty} 2 \quad \text{almost surely and in probability}.$$
If $n = \lfloor C k^2 \rfloor$ with $C < 1/4$, then:
$$\frac{\operatorname{LIS}(\sigma_n)}{k} = \frac{\operatorname{LIS}(\sigma_n)}{\sqrt{n}} \cdot \frac{\sqrt{n}}{k} \xrightarrow{k \to \infty} 2 \sqrt{C} < 2 \sqrt{\frac{1}{4}} = 1.0 \quad \text{a.s.}$$
Thus, $\Pr(\operatorname{LIS}(\sigma_n) \ge k) = \Pr(\operatorname{LIS}(\sigma_n)/k \ge 1) \to 0$ as $k \to \infty$.

## Hypotheses / Conditions
- Uniform distribution over $S_n$.
- Asymptotic regime $k \to \infty$, $n = C k^2$.
- $C < 1/4$ fixed.

## How It Applies
This establishes the necessity of host length $n \ge (1/4 - o(1))k^2$ for any superpattern construction, proving that proving universality at $n = \lceil(1/4+\varepsilon)k^2\rceil$ achieves the exact optimal constant.

## Caveats
This is a lower bound only (necessary condition). Proving sufficiency requires showing that all other $(k!-1)$ permutations are simultaneously contained at $(1/4+\varepsilon)k^2$.
