# Category: Vertical Span Overlap

Type: failed_approach_category
Pattern: Vertical range spans across dyadic intervals overlap globally ($\sum_{m=1}^{2^j} h_{j,m} = \Theta(2^j)$), refuting the disjointness assumption $\sum h_{j,m} \le 1$ and causing discretization penalties to grow to $\Theta(k^{3/2})$ or $\Theta(k \log k)$ instead of decaying geometrically.
Count: 11

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
