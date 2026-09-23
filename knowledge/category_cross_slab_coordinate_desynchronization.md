# Category: Cross-Slab Coordinate Desynchronization

Type: failed_approach_category
Pattern: Decomposing a target permutation into independent sub-permutations embedded within vertical or horizontal slabs ignores the cross-slab ordering constraints, causing independent coordinate realizations to violate global order isomorphism $x_1 < x_2 < \dots < x_k$ with probability $1 - (1/\sqrt{k}!)^M \approx 1 - 10^{-1133}$.
Count: 16

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_r2_L00_N14 | Embedding target sub-permutations independently across $M = \sqrt{k}$ vertical slabs fails global horizontal order isomorphism $x_1 < x_2 < \dots < x_k$ across columns with probability $1 - (1/\sqrt{k}!)^M \approx 1 - 10^{-1133}$ at $k=1000$. |
| 2 | strategy_L01_N13 | Independent embedding in $M = \lceil\sqrt{k}\rceil$ horizontal slabs leaves points within the same column unsorted horizontally, with global sorting probability $(1/M!)^M \approx 10^{-1133}$ at $k=1000$. |
| 3 | strategy_L01_N14 | Independent slab matching across $M = \lceil\sqrt{k}\rceil$ slabs fails cross-slab horizontal and vertical order relations, requiring $\Theta(k^2)$ pairwise synchronizations and failing order isomorphism almost surely. |
| 4 | explorer_r3_L00_N01 | Alternating permutations require crossing between 2 horizontal slabs at each step; horizontal monotonicity forces the chain to stall at $0.85k$ points, failing to embed the full target. |
| 5 | explorer_r3_L00_N05 | Embedding sub-permutations within vertical slabs orders points by increasing column index, producing a permutation with 0 descents and failing to embed target permutations with $\sim k/2$ descents. |
| 6 | explorer_r3_L00_N08 | Routing interleaved runs to adjacent slabs collapses by $1/\binom{k}{k/2} \le 10^{-301}$ due to cross-slab order desynchronization. |
| 7 | N17 (Level 0) | Vertical slab stratification uncoordinated points fail global horizontal interleaving with probability $1 - 1/inom{k}{k/2} pprox 1 - 10^{-300}$ |
| 8 | N19 (Level 0) | Disjoint vertical ribbons inside domain blocks force horizontal coordinates to sort with probability $1/b! \le 1/1600! pprox 10^{-4438}$ |
| 9 | N22 (Level 0) | Intra-column horizontal coordinate desynchronization: points in vertically separated clusters within column of width $4/(arepsilon k)$ sort with probability $1/80! pprox 10^{-119}$ |
| 10 | N25 (Level 0) | Multi-track parallel diagonal ribbons $|y - x - \delta_j| \le w$ couple $x \approx y$, forcing $x_{k/2} \ge 0.925 > 0.075 \ge x_{k/2+1}$ on $\pi = (1, 3, \dots, 2, 4, \dots)$, causing an 85% macroscopic domain inversion |
| 11 | N26 (Level 0) | Coarse-cell bipartite matching: target points in different rows within the same column share horizontal interval, failing horizontal order sorting with probability $1 - 10^{-1495}$ at $k=1000$ |
| 12 | N30 (Level 0) | Laminar ribbon coordinate rule $x(C_1, r) < x(C_2, s)$ iff $r \le s$ horizontally interleaves domain positions, embedding the identity permutation $\operatorname{id}_{2m}$ rather than the interleaved target pattern |
| 13 | explore_merger_r3_L01_N05 | Sequential horizontal coordinate slabs fail on interleaved runs: achieving exact alternating order $Y_1 < Y'_1 < \dots$ across two independent slabs has probability $1/\binom{2m}{m} \le 10^{-300}$ at $k=1000$. |
| 14 | explore_merger_r3_L01_N06 | Concurrent diagonal ribbons for interleaved runs force an $85\%$ horizontal domain inversion gap ($x_{k/2} \ge 0.925 > 0.075 \ge x_{k/2+1}$), destroying domain order on $100\%$ of trials. |
| 15 | explore_merger_r3_L01_N13 | Laminar Dilworth folia ribbon coordinate rule $x(C_1, r) < x(C_2, s) \iff r \le s$ horizontally interleaves domain positions, embedding the monotonic identity permutation $\operatorname{id}_{2m}$ (zero cross-inversions) rather than the target interleaved pattern with $m(m-1)/2$ cross-inversions. |
| 16 | explore_merger_r3_L03_N03 | Embedding multi-slope interleaved monotone runs (like $\pi = (1, 3, \dots, 2m-1, 2m, 2m-2, \dots, 2)$ with $\mathrm{LIS} = m+1, \mathrm{LDS} = m$) in concurrent parallel diagonal ribbons couples physical coordinates $x \approx y$, forcing an $85\%$ horizontal domain inversion gap ($x_{k/2} \ge 0.925 > 0.075 \ge x_{k/2+1}$) that destroys pattern isomorphism on $100\%$ of runs, while independent sequential slabs fail with probability $1 - 10^{-300}$. |
