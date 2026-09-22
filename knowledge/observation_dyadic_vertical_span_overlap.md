# Dyadic Vertical Span Global Overlap on Non-Monotone Permutations

Type: observation
Confidence: high
Source: Candidates 0, 1, 2, 4, 6, 7, 9, 10, 11, 15 (Level 0 falsers)
Relevant to: Multiscale dyadic chaining, spatial decomposition, discretization penalty bounds.

## Statement
For general, alternating, or uniform random permutations $\pi \in S_k$, the vertical range spans $h_{j,m} = \max_{t/k \in I_{j,m}} \pi(t)/k - \min_{t/k \in I_{j,m}} \pi(t)/k$ on dyadic intervals $I_{j,m} = [(m-1)2^{-j}, m 2^{-j}]$ do not have disjoint projections. Instead, they satisfy:
$$\sum_{m=1}^{2^j} h_{j,m} = \Theta(2^j) \gg 1.$$
Consequently, $\sum_{m=1}^{2^j} \sqrt{h_{j,m}} = \Theta(2^j)$, and the boundary discretization penalty across scale $j$ interfaces scales as $P_j = \Theta(2^{j/2} k)$ or $\Theta(k)$ rather than decaying as $O(2^{-j/2} k)$.

## Evidence
1. Rigorous testing on $S_{4096}$: For uniform random permutations, at scale $j=1$ (2 intervals) $\sum h = 1.999$; at scale $j=6$ (64 intervals) $\sum h = 62.01$; at scale $j=10$ (1024 intervals) $\sum h = 615.27 \gg 1$.
2. For alternating permutations $\pi = (1, k, 2, k-1, \dots)$ at $k=1024$, at scale $j=8$, $\sum h_{j,m} = 128.50$, violating the claimed bound $\le 2$ by a factor of $64\times$.
3. Candidate 11 falsification proved that active Haar energy scales as $\Theta(2^{-j})$ (rather than $2^{-2j}$) across $\Theta(2^j)$ non-monotone interfaces, giving cumulative interface penalty $\sum_j \Theta(k) = \Theta(k \log k)$.
4. The only permutations where $\sum_{m=1}^{2^j} h_{j,m} \le 1$ holds are strictly monotone permutations.

## Implications
Any proof route relying on dyadic spatial partitioning to achieve geometric decay of boundary discretization penalties $P_j = O(2^{-j/2} k)$ fails for general permutations. Cumulative boundary discretization penalties sum to $\Theta(k^{3/2})$ or $\Theta(k \log k)$, massively overpowering the $2\varepsilon k$ hydrodynamic surplus.

## Caveats
Holds whenever permutations possess high-frequency non-monotone oscillations. Permutations of bounded total variation $V(\pi) = O(1)$ or structured monotone inflations can satisfy $\sum h_{j,m} = O(1)$, but such classes form a vanishingly small fraction of $S_k$.
