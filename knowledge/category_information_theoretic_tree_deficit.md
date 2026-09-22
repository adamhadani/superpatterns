# Category: Information-Theoretic Tree Deficit

Type: failed_approach_category
Pattern: A dyadic chaining tree of description entropy $O(\varepsilon^2 k)$ or $O(k)$ cannot embed $S_k$, because Shannon source coding requires $\log_2(k!) = \Theta(k \log k)$ bits to represent an arbitrary permutation, leaving the tree covering less than a $2^{-\Omega(k \log k)}$ fraction of targets.
Count: 13

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_L00_N02 | Claimed a tree with entropy $O(\varepsilon^2 k)$ covers all $k!$ permutations; provides $< 0.1$ bits at $k=1000, \varepsilon=0.01$ vs 8529.4 bits required, covering $< 2^{-8500}$ of $S_k$. |
| 2 | explorer_L00_N04 | Conflated single-interval entropy with total tree entropy by omitting factor $2^j$, undercounting actual tree entropy $\Theta(k \log k)$ by over $100\times$. |
| 3 | explorer_L00_N10 | Claimed coarse configurations are bounded by $(2^{j^*})!$, whereas in reality interval images disperse across bins giving $(2^{j^*})^k = \exp(\Theta(k \log(1/\varepsilon)))$. |
| 4 | explorer_L00_N12 | Assumed description entropy $O(k)$ suffices to cover $S_k$, whereas Shannon source coding requires $\Theta(k \log k)$ bits, leaving an exponential information deficit. |
| 5 | explorer_L00_N16 | Tree description entropy $O(k)$ bits cannot encode $k! = \exp(\Theta(k \log k))$ permutations; individual sparse paths cannot induce super-exponentially many distinct patterns. |
| 6 | explorer_L00_N20 | Coarse trajectory space of size $C_0(\varepsilon)$ forces each coarse path to be shared by $k!/C_0(\varepsilon) = \exp(\Theta(k \log k))$ distinct permutations, leaving fine-scale permutations uncertified. |
| 7 | explorer_L00_N21 | Claimed dyadic tree profile with $\le 3$ choices per node can describe at most $e^{O(k)}$ permutations, omitting $99.99999\%$ of $S_k$ targets. |
| 8 | explorer_L00_N23 | Exact dyadic tree value-split telescoping product $\prod_{j=0}^{\log_2 k - 1} \binom{2k/2^j}{k/2^j}^{2^j/2} = k!$, proving tree entropy is $\Theta(k \log k)$ bits, not $O(k)$. |
| 9 | explorer_L00_N24 | Chaining tree with description entropy $O(k)$ bits cannot certify $k! = \exp(\Theta(k \log k))$ permutations, failing to cover all but a negligible fraction of targets. |
| 10 | explorer_L00_N27 | Dyadic trajectory tree with $O(k)$ description entropy violates Shannon entropy bound $\log_2(k!) = \Theta(k \log k)$ by a factor of $\log k$. |
| 11 | explorer_L00_N28 | Dyadic bounding box trees distinguish all $k!$ permutations (combinatorially enumerated on $S_7, S_8$), proving tree entropy is $\Theta(k \log k)$ bits, not $O(k)$. |
| 12 | explorer_L00_N30 | Inverted scale dependence in tree entropy ($2^{-j} k$ instead of $2^j$), claiming all $k$ permutation values are specified in $O(1)$ bits vs Shannon $\Theta(k \log k)$. |
| 13 | explorer_L00_N31 | Fixed point set induces only one permutation, so $e^{O(k)}$ paths cannot certify $k!$ targets, leaving an exponential information deficit. |
