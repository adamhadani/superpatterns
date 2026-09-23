# Multi-Slope Interleaved Monotone Run Dilworth Chain Explosion

Type: observation
Confidence: high
Source: explore_falser_r3_L00_N11 (Round 3 Level 0)
Relevant to: Dilworth chain decomposition, Greene's theorem, monotone run budgeting.

## Statement
Decomposing a permutation $\pi \in S_k$ into contiguous monotone runs (where each run is strictly increasing or strictly decreasing) does not imply that $\pi$ has small Dilworth chain width or bounded decreasing subsequence length. An interleaved permutation consisting of alternating or multi-slope monotone segments can have $\operatorname{LIS}(\pi) = \Theta(k)$ and $\operatorname{LDS}(\pi) = \Theta(k)$ simultaneously, requiring $\Theta(k)$ Dilworth chains to cover.

## Evidence
1. **Concrete Counterexample Family**: Consider $\pi \in S_{2m}$ composed of two contiguous monotone runs: an increasing run of odd numbers followed by a decreasing run of even numbers:
   $$\pi = (1, 3, 5, \dots, 2m-1, 2m, 2m-2, \dots, 4, 2)$$
   - Number of contiguous monotone runs: 2 (one increasing of length $m$, one decreasing of length $m$).
   - Longest Increasing Subsequence: $\operatorname{LIS}(\pi) = m + 1$ (e.g. $(1, 3, 5, \dots, 2m-1, 2m)$).
   - Longest Decreasing Subsequence: $\operatorname{LDS}(\pi) = m$ (the entire second half $(2m, 2m-2, \dots, 2)$).
2. **Dilworth's Theorem Consequence**: By Dilworth's theorem and the Greene-Kleitman invariants, the minimum number of increasing chains needed to partition $\pi$ is equal to $\operatorname{LDS}(\pi) = m = k/2 = \Theta(k)$.
3. **Refutation of Candidate Claims**: In candidate `explorer_r3_L00_N11`, it was claimed that if a permutation is partitioned into $O(1/\varepsilon)$ or $O(1)$ contiguous monotone blocks, its Dilworth chain width (or decreasing subsequence depth) is bounded by $d = O(1)$. The above construction demonstrates that even with only 2 contiguous monotone runs, the Dilworth chain width is $k/2$, exploding to $\Theta(k)$ and requiring $\Theta(k)$ horizontal and vertical buffer slots rather than $O(1)$.

## Implications
Proof strategies cannot assume that bounding the number of contiguous monotone runs controls the poset antichain width or Dilworth chain count. Crossing and interleaving between runs of opposite slopes generates macroscopic antichains ($\Theta(k)$ elements), which invalidates low-width Dilworth chain coupling and causes renewal drift dilation.

## Caveats
If all monotone runs have identical slope (e.g. all increasing), then $\operatorname{LDS}(\pi)$ is bounded by the number of runs $m$. The explosion occurs specifically when runs have mixed (alternating or multi-directional) slopes.
