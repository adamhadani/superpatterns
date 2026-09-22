# Discrete Rank-Slot Integer Buffer Granularity Barrier

Type: observation
Confidence: high
Source: Candidates 0, 1, 3, 4, 7 (Level 0 falsers)
Relevant to: Lookahead buffers, discrete embedding, boundary discretization penalties.

## Statement
In any discrete coordinate embedding of permutations into planar point sets, preventing coordinate collisions and rank inversions across block boundaries requires reserving an absolute coordinate separation of at least 1 discrete rank slot and at least 1 integer host point per interface. Consequently, across $2^j$ interfaces at dyadic scale $j$, the discrete buffer penalty is at least $2^j \times 1 = 2^j$, which grows exponentially with scale $j$ and sums to $\ge k/2 = \Omega(k)$ across fine scales, strictly exceeding the hydrodynamic surplus $2\varepsilon k$ for all $\varepsilon < 1/4$.

## Evidence
1. Analytical evaluation: To ensure $x(p_t) < x(p_{t+1})$ and $y(p_{\pi^{-1}(v)}) < y(p_{\pi^{-1}(v+1)})$ deterministically, the buffer strip must not contain conflicting host points, costing at least $\Delta \ge 1$ rank slots.
2. Sum of discrete cuts: Across fine scales $j > j^*(\varepsilon)$ down to $J = \lceil\log_2 k\rceil$, the number of fine-scale cuts is $\sum_{j=j^*+1}^J 2^{j-1} = k - 2^{j^*}$. For $k \ge 2^{j^*+1}$, this is at least $k/2$.
3. Net drift deficit: $D_{\mathrm{net}} \le 2\varepsilon k - k/2 = (2\varepsilon - 1/2)k < 0$ for all $\varepsilon < 1/4$.

## Implications
Attempts to model discrete boundary penalties as continuously decaying fractions $\delta_j = O(2^{-j/2}/k)$ violate integer point reality at fine scales where $k \delta_J = O(k^{-1/2}) \ll 1$. Discrete lookahead cannot decouple microscopic blocks without paying $\Omega(k)$ buffer losses.

## Caveats
Continuous hydrodynamic coupling avoids integer buffer penalties only when blocks are macroscopic ($a \gg 1$), where buffer spacing $O(1)$ is negligible compared to block capacity $2\sqrt{a}$.
