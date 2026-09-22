# Tracy-Widom Boundary Fluctuation Geometric Growth in Dyadic Decompositions

Type: observation
Confidence: high
Source: Candidates 19, 20, 22 (Level 0 falsers)
Relevant to: Multi-scale dyadic chaining, boundary penalty scaling, finite-size scaling.

## Statement
In a multi-scale dyadic decomposition of length $k$, let each dyadic interval at scale $j \in \{1, \dots, \log_2 k\}$ contain $L_j = k 2^{-j}$ target elements. Under true Tracy-Widom / KPZ boundary fluctuation scaling, the boundary lag per interface between directed Poisson path segments scales as $O(L_j^{1/3}) = O(k^{1/3} 2^{-j/3})$.
Across the $2^j$ dyadic interfaces at scale $j$, the total cumulative boundary fluctuation is:
$$\sum_{m=1}^{2^j} O(L_j^{1/3}) = 2^j \cdot O(k^{1/3} 2^{-j/3}) = O(k^{1/3} 2^{2j/3}).$$
The scale-to-scale ratio is $2^{2/3} \approx 1.5874 > 1$. Consequently, the total boundary penalty across interfaces GROWS geometrically with scale depth $j$ rather than decaying. At the finest scale $j = \lceil \log_2 k \rceil$, the penalty across all interfaces scales as $k^{1/3} (2^{\log_2 k})^{2/3} = k^{1/3} k^{2/3} = \Theta(k)$.

## Evidence
1. Mathematical deduction: In directed planar percolation and Poisson bridges, the boundary matching lag across a transverse interface of a path of length $L$ scales as $L^{1/3}$ (Baik-Deift-Johansson 1999).
2. Multiplying by the number of interfaces $2^j$ gives $2^j \cdot (k 2^{-j})^{1/3} = k^{1/3} 2^{2j/3}$.
3. Summing across all dyadic scales $j = 1, \dots, \log_2 k$:
$$\sum_{j=1}^{\log_2 k} k^{1/3} 2^{2j/3} = k^{1/3} \frac{2^{2/3}(2^{(2/3)\log_2 k} - 1)}{2^{2/3} - 1} = \Theta(k^{1/3} \cdot k^{2/3}) = \Theta(k).$$
4. Candidates claiming $P_j = O(2^{-j/2} k)$ achieved this only by erroneous algebraic substitutions (e.g. converting $k_j^{1/2}$ to $2^{-3j/2} k$, or dividing by $2^j$ twice).

## Implications
Directly eliminates the central premise of multi-scale dyadic chaining: boundary discretization penalties do not converge geometrically as $O(2^{-j/2} k)$, and fine-scale penalties cannot be suppressed below $\varepsilon k$ by choosing $j^*(\varepsilon) = \Theta(\log(1/\varepsilon))$. The cumulative boundary fluctuation across fine scales is intrinsically $\Theta(k)$, which strictly overwhelms the $2\varepsilon k$ hydrodynamic surplus whenever $\varepsilon$ is smaller than the boundary prefactor.

## Caveats
Applies whenever paths must be stitched across $2^j$ spatial boundaries. Can be bypassed if paths are macroscopic ($o(k)$ boundaries) or if embedding is accomplished without piecewise spatial partitioning (e.g., global coupling or Dilworth chain decompositions with $o(k)$ chains).
