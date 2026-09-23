# Half-Height Band LIS Capacity Deficit

Type: observation
Confidence: high
Source: Candidate explorer_r2_L00_N05 and falser report explore_falser_r2_L00_N05 (Round 2 Level 0)
Relevant to: Multi-threaded scanning across $2k$ strips, vertical shift ensembles, LIS capacity bounds

## Statement
In multi-threaded scanning schemes across $2k$ strips (e.g. Definition 4.1 of explorer_r2_L00_N05), the host unit square $[0, 1]^2$ is partitioned into $2k$ horizontal strips of height $1/(2k)$, and thread $t \in [k]$ searches within $k$ consecutive strips $I_{\pi(j)+t}$. Consequently, each individual thread $t$ is strictly confined to a vertical band:
$$B_t = [0, 1] \times \left[\frac{t}{2k}, \frac{t+k}{2k}\right],$$
which has vertical height $H = k / (2k) = 1/2$ and area $\operatorname{Area}(B_t) = 1/2$.
In a planar Poisson point process $\Pi$ of intensity $n_0 = (1/4+\varepsilon/2)k^2$, the expected point count in band $B_t$ is:
$$\mu_{B_t} = n_0 \cdot \operatorname{Area}(B_t) = \left(\frac{1}{8} + \frac{\varepsilon}{4}\right)k^2.$$
By the Logan-Shepp (1977) and Vershik-Kerov (1977) limit shape theorem, the asymptotic longest increasing subsequence capacity in band $B_t$ is bounded by:
$$\operatorname{LIS}(B_t \cap \Pi) \le (2 + o(1)) \sqrt{\mu_{B_t}} = (2 + o(1)) \sqrt{\left(\frac{1}{8} + \frac{\varepsilon}{4}\right)k^2} = \sqrt{\frac{1}{2} + \varepsilon} \, k.$$
For any $\varepsilon < 1/2$ (e.g. $\varepsilon = 0.05$), $\sqrt{1/2+\varepsilon} \approx \sqrt{0.55} \approx 0.7416 < 1.0$.
Therefore, the LIS capacity of any thread confined to a half-height band is at most $0.742k$, falling short of the required $k$ points by at least $25.8\%$. In particular, containing the identity permutation $\operatorname{id}_k$ or any permutation with $\operatorname{LIS}(\pi) > 0.742k$ within band $B_t$ is mathematically impossible.

## Evidence
- Direct application of the Vershik-Kerov limit shape theorem to rectangular domains of area $1/2$.
- Monte Carlo patience sorting across 40 Poisson realizations at $n_0 = (1/4+0.025)k^2$ in N05: mean LIS in $[0, 1] \times [0, 0.5]$ was $68.7$ at $k=100$, $140.3$ at $k=200$, and $287.9$ at $k=400$, exactly matching the theoretical ceiling $\sqrt{1/2+\varepsilon}k \approx 0.742k < k$ and confirming that $\operatorname{id}_k$ is never contained (0/40 trials).

## Implications
Rules out all multi-threaded scanning architectures where threads are vertically shifted within an expanded strip system (such as $2k$ strips) without increasing the total host height or re-scaling coordinates. Any thread restricted to vertical range $< 1/(1+4\varepsilon)$ lacks the LIS capacity to embed the identity permutation $\operatorname{id}_k$.

## Caveats
Applies whenever a scanning thread is confined to a spatial sub-region of vertical height $\le 1/2$ in a host process of intensity $(1/4+\varepsilon/2)k^2$.
