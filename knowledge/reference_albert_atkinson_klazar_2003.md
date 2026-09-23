# Albert, Atkinson, and Klazar (2003) on Simple Permutations

Type: reference
Confidence: high
Source: explore_merger_L01_N00, explore_falser_L01_N00 (Level 1)
Relevant to: Canonical skeletal decomposition, monotone interval blocks, simple permutations.

## Bibliographic Info
- Authors: M. H. Albert, M. D. Atkinson, Martin Klazar
- Title: The Enumeration of Simple Permutations
- Year: 2003
- ArXiv/DOI: Journal of Integer Sequences, Vol. 6 (2003), Article 03.4.4; arXiv:math/0304387
- Theorem/Lemma Number: Theorem 1 & Theorem 4
- Verified via web search: yes

## Key Result
A permutation is simple if it contains no non-trivial interval blocks (sets of contiguous indices whose values are contiguous, of size $1 < |B| < k$). Albert, Atkinson, and Klazar prove that the number of simple permutations $s_k$ in $S_k$ satisfies:
$$\frac{s_k}{k!} = 1 - \frac{2}{k} + O\left(\frac{1}{k^2}\right) \to 1 \quad \text{as } k \to \infty.$$
Consequently, almost all permutations in $S_k$ are simple.

## Hypotheses / Conditions
Applies to uniform permutations in the symmetric group $S_k$ as $k \to \infty$.

## How It Applies
This result proves that generic target permutations have no non-trivial interval blocks of length $\ge 2$. In canonical skeletal decomposition, macroscopic monotone interval blocks $\mathcal{M}$ of length $a \ge L = \Theta(\sqrt{\log k})$ or $a \ge \Theta(1/\varepsilon)$ capture exactly 0 elements ($|\mathcal{M}| = 0$) for almost all permutations in $S_k$, proving that shared host squares embed 0% of generic target elements.

## Caveats
Permutations constructed as monotone inflations (such as in Workstream W39) are by design non-simple and have large interval blocks; the theorem proves that such structure is asymptotically absent in uniform random or generic permutations.
