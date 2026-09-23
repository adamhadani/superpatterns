# Category: Poset Greene Capacity Cross-Chain Blocking

Type: failed_approach_category
Pattern: Greene's theorem multi-chain capacity and RSK tableau row sums $\sum_{i=1}^m \lambda_i \ge k$ control only total unconstrained point volume in disjoint increasing chains along parallel diagonal paths, providing zero control over the $\Theta(k^2)$ pairwise cross-chain order relations (inversions and descents); greedy topological poset embedding suffers 100% coordinate deadlocks from quadrant bounding-box starvation, while enforcing cross-chain order via rank buffers re-incurs fatal discrete buffer penalties $P_{\mathrm{disc}} \ge 0.5k$.
Count: 9

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_r2_L00_N23 | Greene--Plancherel row sums $\Lambda_m \ge k$ measure only unlabeled point cardinality along parallel diagonal paths, failing to guarantee cross-chain inversions; greedy topological poset sorting suffers 100% coordinate deadlocks (0% success across 100 trials for $k \ge 20$ even at $C=4.0$), and macro-grids have $\operatorname{LDS} \le M^2$, failing to embed generic targets. |
| 2 | explorer_r2_L00_N24 | Greene's theorem capacity dominance does not imply permutation pattern containment because it controls only unconstrained chain point volume; in exhaustive tests, 38% of shape-[3, 3] permutations fail to contain shape-[2, 2] targets despite strict row dominance, and enforcing cross-chain order requires discrete rank-slot buffers ($P_{\mathrm{disc}} \ge 0.5k$). |
| 3 | strategy_L01_N04 | Dilworth chain decomposition ($d = 2\sqrt{k}$) cannot achieve LIS velocity $2\sqrt{C} > 1$ without violating point conservation (demands $4\sqrt{C}k^{3/2} \gg k$ points); consecutive elements transition between chains $>88\%$ of the time, collapsing parallel execution to sequential 1D arrivals. |
| 4 | strategy_L01_N05 | Running $d = 2\sqrt{k}$ Dilworth chains at LIS velocity $2\sqrt{C}$ demands $O(k^{3/2})$ points from an $O(k)$ Poisson budget; decreasing permutations $\pi_{\mathrm{rev}}$ have $\operatorname{LDS} = k$, requiring $k$ chains of size 1 and collapsing velocity to 0. |
| 5 | strategy_L01_N08 | Dilworth chain decomposition violates Poisson point conservation ($2\sqrt{k} \times \sqrt{k} = k$ points with 0 margin), while $92\%$ cross-chain transitions force sequential serialized delays. |
| 6 | strategy_L01_N11 | Target elements transition between Dilworth chains in $>89\%$ of consecutive steps, serializing arrivals and destroying parallel LIS speedup. |
| 7 | strategy_L01_N12 | Greene's theorem multi-chain sums control only diagonal point counts, providing zero control over $\Theta(k^2)$ pairwise cross-chain order relations. |
| 8 | N28 (Level 0) | Backup Route 1 proposes higher Hammersley lines $m \ge 1$ for interleaved chains, which generate virtual/chimeric coordinates with 0% physical existence in $\Pi_{n_0}$ |
| 9 | N31 (Level 0) | Dilworth chain non-crossing corridors strictly forbid value interleaving; for permutations with interleaved values ($21^{\oplus (k/2)}$ or $\pi = (1, 3, \dots, 2, 4, \dots)$ with 124,750 cross-inversions), non-crossing corridors are geometrically impossible |
