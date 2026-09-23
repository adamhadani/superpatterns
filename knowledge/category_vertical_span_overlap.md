# Category: Vertical Span Overlap

Type: failed_approach_category
Pattern: Vertical range spans across dyadic intervals overlap globally ($\sum_{m=1}^{2^j} h_{j,m} = \Theta(2^j)$), refuting the disjointness assumption $\sum h_{j,m} \le 1$ and causing discretization penalties to grow to $\Theta(k^{3/2})$ or $\Theta(k \log k)$ instead of decaying geometrically.
Count: 21

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_L00_N01 | Falsely claimed $\sum h_{j,m} \le 1$ to manufacture $P_j = O(2^{-j/2} k)$; vertical spans sum to $\Theta(2^j)$, making penalties grow exponentially in $j$. |
| 2 | explorer_L00_N06 | Conflated distinct point values with disjoint vertical intervals; actual sum $\sum h_{j,m} = \Theta(2^j)$ causes cumulative penalty $\Theta(k^{3/2})$, exceeding surplus by $3000\times$. |
| 3 | explorer_L00_N07 | Claimed vertical span bound $\sum h_{j,m} \le 2$ violated by up to $77\times$ on alternating/random permutations, causing total penalty $\Theta(k \log k)$. |
| 4 | explorer_L00_N09 | Bounded variation fallacy $\sum h_{j,m} \le 2$ refuted by empirical verification of $\sum h_{j,m} = \Theta(2^j)$, making cumulative penalties diverge as $\Theta(k \log k)$. |
| 5 | explorer_L00_N10 | Assumed $1/2$-Hölder regularity bounds vertical displacements, but discrete permutation paths have unconstrained vertical dispersion across dyadic boxes. |
| 6 | explorer_L00_N11 | Assumed non-monotone interfaces scale as $O(2^{j/2})$ with Haar energy $2^{-2j}$; true active interfaces are $\Theta(2^j)$ with Haar energy $\Theta(2^{-j})$, giving $\Theta(k \log k)$ total penalty. |
| 7 | explorer_L00_N15 | Overlapping vertical ranges across dyadic intervals destroy Poisson increment independence and invalidate union bound conditioning. |
| 8 | explorer_L00_N17 | Assumed Haar wavelet bounds imply box heights decay as $2^{-j/2}$; for alternating/random permutations average height remains $\Theta(1)$ and sum of heights scales as $\Theta(2^j)$. |
| 9 | explorer_L00_N25 | Theorem 5.1 penalty formula $0.5 C_0 k$ has zero geometric decay, while actual Haar $L^1$ variation $\sum |\Delta y| = \Theta(2^j)$ reaches 169.15 on random permutations (claimed bound 32). |
| 10 | explorer_L00_N27 | Vertical span of dyadic permutation blocks is $(1-o(1))k$, refuting the claimed decay to $k 2^{-j}$ and causing fine discretization loss to overwhelm surplus. |
| 11 | explorer_L00_N28 | Box height remains $\Theta(1)$ on non-monotone permutations with aspect ratio $h/w$ reaching $16.0$, violating diagonal box $ds \times ds$ scaling. |
| 12 | strategy_L03_N02 | Collective buffer amortization between horizontal clusters of size $b = \Omega(1/\varepsilon)$ fails because generic permutations have $96.4\%$ to $98.5\%$ vertical span overlap and $0.00\%$ disjoint pairs ($0/18200$), making inter-cluster vertical rank buffering impossible. |
| 13 | strategy_L03_N03 | Horizontal dyadic bisection down to scale $j_{\mathrm{stop}}$ fails to prevent vertical rank collisions for generic targets, whose vertical spans exceed $0.998$ across horizontal intervals, leaving target elements globally interleaved across $[0, 1]$ with zero vertical separation. |
| 14 | explorer_r2_L00_N04 | Assuming mesoscopic blocks of length $L = \Theta(1/\varepsilon)$ fit into boxes of height $L/k$ and area $L^2/k^2$ fails because generic permutation blocks have vertical span exceeding $0.976$ ($12.2\times$ larger than $L/k$), creating total vertical overlap across all $M$ blocks. |
| 15 | explorer_r3_L00_N06 | Adjacent permutation blocks of size $b=160$ exhibit $99.82\%$ vertical span overlap and 11,196 cross-inversions, refuting the assumption that mesoscopic blocks can be separated by vertical buffers. |
| 16 | explorer_r3_L00_N08 | Dilworth chain ribbons have 79.1% to 91.2% overlapping vertical spans in generic permutations, forcing horizontal serialization with renewal collapse $\mathbb{E}[X_k] \ge 3.6364$. |
| 17 | N20 (Level 0) | Dropped $\sqrt{k}$ factor in boundary penalty: $n_0 \cdot \delta_j = (C k^2) \cdot O(2^{-j/2} k^{-1/2}) = O(2^{-j/2} k^{3/2})$, exceeding gross surplus by $\Theta(\sqrt{k})$ (31.6x) |
| 18 | N20 (Level 0) | Total 2D dyadic grid line perimeter $\Theta(2^j)$ requires coordinate separation buffers consuming $\Theta(2^j k)$ points, exploding exponentially with scale $j$ |
| 19 | explore_merger_r3_L01_N02 | Target elements in horizontal blocks of width $w = 2/(\varepsilon k)$ have mean vertical span $0.9522$ ($95.2\%$ of $[0, 1]$, $23.8\times$ box height), with $0/1000$ blocks localized within height $w$, causing vertical interleaving across slabs. |
| 20 | explore_merger_r3_L01_N08 | In generic permutations of length $k=1000$, adjacent blocks of size $b=160$ exhibit $99.02\%$ vertical span overlap and $12,880.9$ cross-inversions per pair ($50.32\%$ inverted), causing topological front advancement to suffer $100\%$ renewal collapse (mean horizontal span $2.9 \times 10^5 \gg 1.0$). |
| 21 | explore_merger_r3_L01_N15 | Dyadic vertical spans on generic permutations sum to $\sum_{m=1}^{2^j} h_{j,m} = \Theta(2^j) \gg 1$ rather than $O(1)$, refuting vertical disjointness across dyadic spatial boxes and destroying non-crossing multi-scale chaining. |
