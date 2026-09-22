# Category: LIS Velocity Non-Monotone Mismatch

Type: failed_approach_category
Pattern: Treating the Logan-Shepp / Vershik-Kerov LIS traversal velocity $v(s) = 2\sqrt{C} > 1$ as fungible point-acquisition capacity for arbitrary non-monotone permutations is a fatal category error and violates point conservation.
Count: 25

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_L00_N00 | LIS paths embed strictly monotone identity permutations; arbitrary target permutations contain microscopic descents and oscillations that cannot be traversed by increasing paths. |
| 2 | explorer_L00_N03 | Infinitesimal box LIS capacity integration $dN(s) = 2\sqrt{d\mu}$ violates point conservation $\operatorname{LIS}(S) \le |S|$ by predicting $3.8\times$ more points than exist in the entire corridor. |
| 3 | explorer_L00_N08 | Category error applying LIS velocity $2\sqrt{C}$ to non-monotone permutations; increasing paths cannot capture arbitrary permutations without losing $\ge 50\%$ length. |
| 4 | explorer_L00_N09 | LIS velocity $v = 2\sqrt{c} > 1$ applies only to increasing subsequences, whereas general permutations contain descents and oscillations that cannot be embedded along monotone paths. |
| 5 | explorer_L00_N11 | Assumed Logan-Shepp / Vershik-Kerov LIS velocity applies to general dyadic blocks, ignoring that target permutation blocks have microscopic descents. |
| 6 | explorer_L00_N12 | Assumed diagonal boxes have LIS capacity exceeding block size, but diagonal boxes are $77\%$ empty (mean points $\le 0.26$), yielding near-zero capacity. |
| 7 | explorer_L00_N13 | Monotone LIS capacity captures only $2\sqrt{L} \ll L$ points on non-monotone permutation blocks, leading to a $100\%$ capacity deficit as block size $L \to \infty$. |
| 8 | explorer_L00_N14 | LIS velocity applied to arbitrary non-monotone permutations; local descents break chain path monotonicity. |
| 9 | explorer_L00_N15 | LIS velocity $2\sqrt{c} > 1$ cannot be integrated across non-monotone dyadic intervals without violating order preservation. |
| 10 | explorer_L00_N16 | Vershik-Kerov LIS velocity $2\sqrt{C} > 1$ applied to arbitrary non-monotone permutations; local jumps require non-monotone paths. |
| 11 | explorer_L00_N17 | Assumed LIS limit shape velocity $2\sqrt{C}$ allows arbitrary non-monotone traversal; directed paths cannot embed descents without deficit. |
| 12 | explorer_L00_N18 | Equated LIS traversal velocity $v(s) = 2\sqrt{C}$ with embedding capacity; only 0.69% of permutations in $S_8$ have monotone dyadic blocks. |
| 13 | explorer_L00_N19 | Hydrodynamic traversal rate $2\sqrt{C}$ applies only to monotone increasing paths, whereas generic target permutations require non-monotone choices. |
| 14 | explorer_L00_N20 | Monotone increasing paths in $[0, 1]^2$ cannot embed permutations with inversions, which by Greene's theorem require $\approx 2\sqrt{k}$ coupled chains. |
| 15 | explorer_L00_N21 | Applied Logan-Shepp LIS limit to microscopic non-monotone blocks where basic cells have mean count $\approx 0.028$ and void probability $> 78\%$. |
| 16 | explorer_L00_N22 | Evaluated traversal capacity along arbitrary target trajectories using monotone LIS formula, omitting permutation ranks entirely. |
| 17 | explorer_L00_N23 | Generic permutations on dyadic blocks have LIS $2\sqrt{k_j} \ll k_j$, so directed monotone paths capture only a vanishing fraction of target elements. |
| 18 | explorer_L00_N24 | Logan-Shepp / Vershik-Kerov LIS traversal rate $2\sqrt{C}$ applied to arbitrary non-monotone permutations; local descents break chain path monotonicity. |
| 19 | explorer_L00_N25 | LIS limit shape velocity conflated with non-monotone embedding capacity; monotone paths capture only a vanishing fraction of generic permutation blocks. |
| 20 | explorer_L00_N26 | 2D LIS limit treated as 1D differential form $dN = 2\sqrt{d\mu}$, predicting 107 points in corridor containing only 28.5 points (violates point conservation). |
| 21 | explorer_L00_N27 | Monotone LIS velocity applied across dyadic blocks of general permutations; monotone paths fail to capture microscopic descents. |
| 22 | explorer_L00_N28 | LIS velocity along diagonal $ds \times ds$ invalid for non-monotone targets where box heights do not shrink; concavity of $\sqrt{\cdot}$ artificially inflated capacity in simulation. |
| 23 | explorer_L00_N29 | Logan-Shepp / Vershik-Kerov LIS limit velocity applied to non-monotone permutations with microscopic oscillations. |
| 24 | explorer_L00_N30 | Hydrodynamic LIS velocity conflated with non-monotone permutation embedding, ignoring that monotone chains cannot traverse reversals. |
| 25 | explorer_L00_N31 | Directed LIS traversal velocity applied to non-monotone permutations with $\Theta(k)$ descents, where monotone paths capture only $2\sqrt{k} \ll k$ points. |
