# Category: Discrete Buffer Integer Granularity

Type: failed_approach_category
Pattern: Continuous buffer scaling yields unphysical fractional host points ($< 1$) per interface, whereas discrete rank-slot separation requires $\ge 1$ integer host point per interface, incurring an $\Omega(2^j)$ penalty at scale $j$ and $\Omega(k)$ across fine scales, overwhelming $2\varepsilon k$ surplus.
Count: 24

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_L00_N04 | Buffer separation $\Delta \ge 1$ across $2^j$ interfaces incurs $\ge 2^j \Delta$ penalty, yielding fine-scale loss $\ge k/2$ that strictly exceeds $2\varepsilon k$ surplus for all $\varepsilon < 1/4$. |
| 2 | explorer_L00_N00 | Claimed fractional buffer $\delta_J = O(k^{-1/2})$ per interface violates integer point capacity, while discrete rank separation requires $\ge 1$ point, forcing fine penalty $\Omega(k)$. |
| 3 | explorer_L00_N08 | Unphysical fractional buffer $\delta_j \to 0$ vs discrete requirement of $\ge 1$ point per interface; integer points require penalty $\ge 2^J \ge k$, wiping out surplus. |
| 4 | explorer_L00_N09 | Discrete atomicity violation: continuous buffer $\delta_j < 1/k$ is physically impossible in discrete permutations where each point occupies integer coordinates. |
| 5 | explorer_L00_N10 | Claimed buffer loss $O(2^{-3j/2}k)$, but discrete integer rank buffer forces $\sum 2^j \Delta = \Theta(k)$, exceeding $2\varepsilon k$ surplus by $\ge 50\times$. |
| 6 | explorer_L00_N12 | Fractional rank buffer $\delta_J = O(k^{-1/2}) < 1$ slot vs discrete requirement $\ge 1$ slot per interface, forcing fine-scale loss $\ge k/2$. |
| 7 | explorer_L00_N13 | Discrete buffer $\Delta 2^j = \Omega(2^j)$ yields total fine penalty $\ge 3k$ points, exceeding $2\varepsilon k$ surplus by $\ge 150\times$. |
| 8 | explorer_L00_N14 | Conflated Poisson standard deviation $O(2^{-j/2}k)$ with deterministic discrete rank buffer requirement $\Omega(2^j)$. |
| 9 | explorer_L00_N15 | Fractional buffer $\delta_J < 1$ slot violates integer point granularity; enforcing $\ge 1$ slot per interface forces penalty $\ge 2^J = \Theta(k)$. |
| 10 | explorer_L00_N16 | Lookahead rank boxes of area $\Theta(1/k^2)$ suffer from independent Poisson voids, with joint occupancy probability $\le \exp(-3.5k) \to 0$. |
| 11 | explorer_L00_N18 | Fractional buffer loss $C_{\mathrm{disc}}/\sqrt{k} \to 0$ violates discrete rank integrality; reserving $\ge 1$ point per interface forces $\Omega(k)$ penalty, wiping out surplus. |
| 12 | explorer_L00_N19 | Buffer scaling assumes fractional point loss $1/\sqrt{k} < 1$, but discrete rank buffers require $\ge 1$ integer point, forcing fine-scale penalty $P_J \ge k$. |
| 13 | explorer_L00_N20 | Boundary fluctuation scaling under Tracy-Widom grows as $k^{1/3} 2^{2j/3}$ rather than decaying, accumulating to $\Theta(k)$; discrete buffers require $\ge ck$ points. |
| 14 | explorer_L00_N21 | Buffer width scaling $\delta_j = C_1 2^{-3j/2} \ge 2/M$ requires $C_1 = \Omega(\sqrt{k})$, forcing $\delta_1 > 1$; discrete boundary slots sum to $\sum 2^j = 2k-2$, wiping out surplus. |
| 15 | explorer_L00_N22 | Per-interface penalty $p_j = O(2^{-3j/2} k) \to 0$ violates discrete rank integrality; reserving $\ge 1$ slot per interface requires $\ge 2k$ points. |
| 16 | explorer_L00_N23 | Wrong-sided bound $2^{-j/4} \le 2^{-j/2}$ in penalty derivation; expected points in fine buffers decay to $\Theta(k^{-1/2}) \to 0$, causing Poisson void starvation. |
| 17 | explorer_L00_N24 | Buffer width $\delta_J = c_0 k^{-3/2}$ yields $k \delta_J \approx k^{-1/2} < 1$ slot, violating discrete rank integrality and leaving buffer boxes 100% empty. |
| 18 | explorer_L00_N25 | Continuous boundary penalties assume fractional point loss, but discrete rank-slot separation requires $\ge 1$ point per interface, incurring $\ge k$ fine penalty. |
| 19 | explorer_L00_N26 | 100 disjoint rank boxes of size $1/k^2$ are 75% empty under Poisson intensity $(1/4+3\varepsilon/4)k^2$; discrete buffers require integer points, wiping out surplus. |
| 20 | explorer_L00_N27 | Rank-slot buffer spacing $2/(3k)$ across $k$ interfaces consumes $2/3$ (66.7%) of the unit interval, leaving negative net drift $-0.57$ at $\varepsilon=0.05$. |
| 21 | explorer_L00_N28 | Fractional buffer scaling violates discrete rank integrality; boundary penalty proof fabricated with undefined variable and trivial collision check. |
| 22 | explorer_L00_N29 | Inverted algebraic step dividing by $h_{j,m}$ causes actual discrete boundary loss to scale as $\Omega(2^{+j/2} k)$, diverging exponentially by $1024\times$ at $j=10$. |
| 23 | explorer_L00_N30 | Fractional buffer width $O(k^{-1/2})$ violates discrete integer rank slots; reserving $\ge 1$ slot per interface requires $\ge k$ points, exceeding $O(\varepsilon k)$ surplus. |
| 24 | explorer_L00_N31 | Discrete rank-slot buffer separation requires $\ge 1$ cell per interface, forcing penalty $\ge k$ on $k$ singletons and leaving negative net drift $D_{\mathrm{net}} \le (2\varepsilon - 1)k < 0$ for all $\varepsilon < 0.5$. |
