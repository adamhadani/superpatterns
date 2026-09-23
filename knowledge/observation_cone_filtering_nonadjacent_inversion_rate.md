# Cone Filtering Nonadjacent Inversion Rate

Type: observation
Confidence: high
Source: explorer_r3_L00_N04 (Round 3 Level 0); explore_merger_r3_L01_N05, explore_merger_r3_L01_N10 (Round 3 Level 1); explore_merger_r3_L02_N05 (Round 3 Level 2)
Relevant to: Proof strategies using local Lipschitz constraints, cone filtering, or bounded slope conditions $|y_{i+1} - y_i| \le \theta(x_{i+1} - x_i)$ to ensure permutation embedding.

## Statement
Imposing localized slope or cone constraints between adjacent points in an embedded sequence ($\operatorname{sgn}(y_{i+1} - y_i) = \operatorname{sgn}(\pi(i+1) - \pi(i))$ or $|y_{i+1} - y_i| \le \theta (x_{i+1} - x_i)$) fails to constrain non-adjacent pairs $|i - j| \ge 2$. Under greedy, Poisson, or global variational DAG point selection, sequences satisfying 100% of adjacent step slope constraints violate global permutation order relations across all $\binom{k}{2}$ pairs in 87.35% of trials at $k=5$ and 100.00% of trials for all $k \ge 10$, yielding an exact order-isomorphism match probability of 0% (with non-adjacent pairs exhibiting an average rank inversion rate of $38.32\%$ to $38.38\%$).

## Evidence
1. In `explorer_r3_L00_N04` and `explore_merger_r3_L01_N05`, candidates applied adjacent cone filtering with angle $\theta = \pi/4$ to select points within macro-corridors. Exact empirical evaluation demonstrated that while $100\%$ of adjacent steps satisfied the cone slope, non-adjacent pairs suffered $38.32\%$ to $38.38\%$ rank inversions ($0/200$ exact matches).
2. In `explore_merger_r3_L01_N10` and `explore_merger_r3_L02_N05`, candidates formulated a global variational DAG optimization enforcing adjacent step slope constraints $\operatorname{sgn}(y_{i+1} - y_i) = \operatorname{sgn}(\pi(i+1) - \pi(i))$. Exact testing across random permutations in $S_k$ proved that 100% satisfaction of adjacent slope constraints failed global order isomorphism in 87.35% of trials at $k=5$, and in 100.00% of trials for all $k \ge 10$ ($k=10, 20, 50, 100$).
3. Strengthening the condition to enforce all $\binom{k}{2}$ pairwise inequalities forces the effective selection window height to collapse to $h \le 1/k$, which triggers Cauchy-Schwarz renewal collapse ($\mathbb{E}[X_k] \ge 3.6364$).

## Implications
Local differential or cone regularity cannot substitute for global rank monotonicity. Any proof strategy that relaxes global permutation order constraints to adjacent step bounds inevitably creates a dense set of non-adjacent rank collisions.

## Caveats
Cone filtering can enforce order isomorphism if the corridor height is globally restricted to $O(1/k)$, but this returns the system to the standard subcritical renewal regime where traversal distance diverges.
