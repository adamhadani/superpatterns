# Universality of Random Permutations (He & Kwan 2020)

Type: reference
Confidence: high
Source: Candidates L03_N00, L03_N01, L03_N02, L03_N03, L03_N04 (Level 3 mergers)
Relevant to: Baseline host length bounds for $k$-superpatterns, elimination of logarithmic factors, comparison with sharp threshold $(1/4+\varepsilon)k^2$.

## Bibliographic Info
- Authors: Xiaoyu He, Matthew Kwan
- Title: Universality of random permutations
- Year: 2020
- ArXiv/DOI: arXiv:2003.02327; Bulletin of the London Mathematical Society, 52(6):1117–1128, 2020
- Theorem/Lemma Number: Theorem 1.1
- Verified via web search: yes

## Key Result
For every integer $k \ge 1$, let $\sigma_n \sim \operatorname{Uniform}(S_n)$ be a uniform random permutation. If $n \ge C k^2 \log\log k$ for a sufficiently large absolute constant $C > 0$, then with probability $1 - o(1)$ as $k \to \infty$, $\sigma_n$ contains every permutation $\pi \in S_k$ as an induced sub-pattern (i.e. $\sigma_n$ is a $k$-superpattern).

## Hypotheses / Conditions
- Host permutation $\sigma_n$ is drawn uniformly at random from $S_n$.
- Length $n \ge C k^2 \log\log k$ for an absolute constant $C > 0$.
- Asymptotics as target pattern length $k \to \infty$.

## How It Applies
1. Provides the best published upper bound for Noga Alon's 1999 superpattern conjecture in the literature, improving upon Richard Arratia's 1999 bound of $O(k^2 \log^2 k)$ and chromatic/poset methods.
2. Serves as the immediate benchmark that Workstream W47 improved upon by eliminating the $\log\log k$ factor to achieve $n = C_0 k^2$ ($C_0 \approx 9.62$), which Tier 2 of the Level 3 architectures cites as their unconditional general universality baseline.
3. Quantifies the remaining gap between published literature ($O(k^2 \log\log k)$), linear-scaling universality ($C_0 k^2$), and Noga Alon's sharp constant threshold $n = \lceil(1/4+\varepsilon)k^2\rceil$.

## Caveats
The He–Kwan proof technique relies on partitioning target permutations into monotone chains via Dilworth's theorem and embedding them using dependent coordinate intervals with buffer spacing, which inherently incurs the $\log\log k$ factor to control void fluctuations in coordinate cells. It does not provide the sharp constant $C = 1/4$.
