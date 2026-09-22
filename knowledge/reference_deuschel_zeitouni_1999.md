# Lower Tail Large Deviations for the Longest Increasing Subsequence

Type: reference
Confidence: high
Source: Candidates 0, 1, 2, 3, 4, 6, 7 (Level 0)
Relevant to: Shared host squares, concentration of monotone path capacity, lower tail bounds.

## Bibliographic Info
- Authors: Jean-Dominique Deuschel, Ofer Zeitouni
- Title: On the large deviations of the longest increasing subsequence of random permutations
- Year: 1999
- ArXiv/DOI: J. Funct. Anal. 165 (1999), no. 2, 246-273
- Theorem/Lemma Number: Theorem 1 (Lower tail large deviations)
- Verified via web search: yes

## Key Result
For a Poisson point process $\Pi_\mu$ of intensity $\mu$ on $[0, 1]^2$, for any $\delta \in (0, 1)$, the probability that the longest increasing subsequence has length below $(1-\delta) 2\sqrt{\mu}$ satisfies:
$$\Pr\left(\operatorname{LIS}(\Pi_\mu) \le (1-\delta) 2\sqrt{\mu}\right) \le \exp\left( - c(\delta) \mu \right),$$
where $c(\delta) > 0$ depends only on $\delta$, exhibiting quadratic-in-$\sqrt{\mu}$ (i.e. linear in $\mu$) decay in the lower tail.

## Hypotheses / Conditions
- Homogeneous planar Poisson point process on a rectangle.
- $\delta > 0$ fixed deviation below the hydrodynamic limit $2\sqrt{\mu}$.

## How It Applies
Used to certify that all $O(k^3)$ shared candidate squares of side length $a \ge K\sqrt{\log k}$ contain increasing and decreasing subsequences of length $a$ simultaneously with failure probability $O(k^3) \exp(-c_C K^2 \log k) = o(1)$.

## Caveats
Applies only to sufficiently large blocks ($a \ge K\sqrt{\log k}$). Vacuous for microscopic blocks ($a = O(1)$), where large deviation decay is insufficient to overcome union bounds.
