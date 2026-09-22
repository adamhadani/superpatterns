# Noga Alon's Superpattern Conjecture (1999)

Type: reference
Confidence: high
Source: Problem context, Candidates 0-7 (Level 0)
Relevant to: Problem formulation, sharp constant threshold $(1/4+\varepsilon)k^2$.

## Bibliographic Info
- Authors: Noga Alon
- Title: Asymptotic threshold for universal permutations (Problem communication / Open problem)
- Year: 1999
- ArXiv/DOI: Problem posed in 1999; see also Bóna, "Combinatorics of Permutations", 2nd ed., 2012
- Theorem/Lemma Number: Superpattern Conjecture
- Verified via web search: yes

## Key Result
Conjectured that for every fixed $\varepsilon > 0$, a uniform random permutation $\sigma_n \sim \operatorname{Uniform}(S_n)$ of length:
$$n = \left\lceil \left(\frac{1}{4} + \varepsilon\right) k^2 \right\rceil$$
contains every permutation $\pi \in S_k$ as an induced sub-pattern with high probability:
$$\lim_{k \to \infty} \Pr\left(\sigma_n \text{ contains all } \pi \in S_k\right) = 1.$$

## Hypotheses / Conditions
- $\sigma_n$ chosen uniformly from $S_n$.
- $\varepsilon > 0$ arbitrary fixed constant.
- Simultaneous containment of all $k!$ patterns in $S_k$.

## How It Applies
This is the formal problem statement that all workstreams (W39 through W49) and explorer strategies are attempting to resolve.

## Caveats
Prior to current workstreams, the best general simultaneous universality upper bound was $C k^2 \log\log k$ (He & Kwan, 2020), which was improved to $C k^2$ for large unspecified constant $C \gg 1$ in W47. Closing the gap to the sharp constant $C = 1/4$ is the focus of W48/W49.
