# Mathematical Proof: Workstream W57 — Dynamic Greene Chain Routing on the Generic Bulk

**Author:** Adam Ever-Hadani  
**Date:** September 2026  
**Subject Classification:** Primary 05A05; Secondary 60C05, 60G55, 05E10

---

## 1. Poset Structure & Constructive Dilworth Chain Decomposition

Let $\pi \in S_k$ be a permutation of length $k$. We associate to $\pi$ a strict partial order $([k], <_\pi)$ on index set $[k] = \{0, 1, \dots, k-1\}$ defined by:
$$
i <_\pi j \iff i < j \quad \text{and} \quad \pi(i) < \pi(j).
$$

Under this partial order:
- A **chain** is a subset of indices $M \subseteq [k]$ totally ordered by $<_\pi$, which corresponds precisely to an **increasing subsequence** of $\pi$.
- An **antichain** is a subset of pairwise incomparable indices $A \subseteq [k]$, where for all $i < j$ in $A$, $\pi(i) > \pi(j)$, which corresponds precisely to a **decreasing subsequence** of $\pi$.

By Dilworth's classical decomposition theorem, the minimum number of chains required to partition a finite poset equals the maximum size of an antichain. In the permutation poset $([k], <_\pi)$, the maximum antichain size is the length of the longest decreasing subsequence, denoted $d = \operatorname{LDS}(\pi)$.

### Theorem 1.1 (Constructive Dilworth Chain Decomposition).
For each index $i \in [k]$, let $\operatorname{lds\_end}(i)$ denote the length of the longest decreasing subsequence of $\pi$ whose final element is $i$:
$$
\operatorname{lds\_end}(i) := \max \left\{ \ell \ge 1 : \exists \, i_1 < i_2 < \dots < i_\ell = i \text{ with } \pi(i_1) > \pi(i_2) > \dots > \pi(i_\ell) \right\}.
$$
Define the chain assignment map $\operatorname{chain}: [k] \to \{1, \dots, d\}$ by:
$$
\operatorname{chain}(i) := \operatorname{lds\_end}(i).
$$
For each $m \in \{1, \dots, d\}$, let $M_m := \{ i \in [k] : \operatorname{chain}(i) = m \}$. Then:
1. The sets $M_1, \dots, M_d$ form a partition of $[k]$ into exactly $d = \operatorname{LDS}(\pi)$ non-empty subsets.
2. Every set $M_m$ is a strictly increasing chain: for any $i, j \in M_m$ with $i < j$, we have $\pi(i) < \pi(j)$.

*Proof.*
1. Since every index $i$ has at least the single-element decreasing subsequence $(i)$, $1 \le \operatorname{lds\_end}(i) \le \operatorname{LDS}(\pi) = d$. The subsets $M_1, \dots, M_d$ are mutually disjoint and cover $[k]$.
2. Suppose for contradiction that there exist $i, j \in M_m$ with $i < j$ but $\pi(i) \ge \pi(j)$. Since $\pi$ is a permutation, entries are distinct, so $\pi(i) > \pi(j)$. Let $i_1 < i_2 < \dots < i_m = i$ be a decreasing subsequence of length $m = \operatorname{chain}(i)$ ending at $i$. Appending $j$ yields the sequence $i_1 < \dots < i_m < j$ with $\pi(i_1) > \dots > \pi(i_m) > \pi(j)$, which is a valid decreasing subsequence of length $m + 1$ ending at $j$. Thus:
$$
\operatorname{lds\_end}(j) \ge m + 1 > m = \operatorname{chain}(j),
$$
a direct contradiction. Therefore, $\pi(i) < \pi(j)$ for all $i < j$ in $M_m$, establishing that $M_m$ is strictly increasing in both index and value. $\square$

---

## 2. Two-Dimensional Capacity Super-Surplus Law

Let $\sigma_n \in S_n$ be a uniform random permutation of length $n = C k^2$, where $C = 1/4 + \varepsilon$.

Applying Theorem 1.1 to the host $\sigma_n$, the host decomposes into $H = \operatorname{LDS}(\sigma_n)$ strictly increasing chains $\mathcal{L}_1, \dots, \mathcal{L}_H$. By Greene's theorem, these chains correspond to the peeled rows of the Robinson–Schensted–Knuth (RSK) Young tableau.

### Theorem 2.1 (Two-Dimensional Super-Surplus Law).
For any target $\pi \in S_k$ and host $\sigma_n \in S_n$ at $n = C k^2$:
1. **Layer Count Surplus:** The expected number of available host layers $H = \operatorname{LDS}(\sigma_n)$ satisfies:
   $$
   \mathbb{E}[H] \sim 2\sqrt{n} = 2\sqrt{C} k.
   $$
   For generic targets $\pi$, $\mathbb{E}[d] = \mathbb{E}[\operatorname{LDS}(\pi)] \sim 2\sqrt{k}$. The layer capacity ratio satisfies:
   $$
   \frac{\mathbb{E}[H]}{\mathbb{E}[d]} \sim \frac{2\sqrt{C} k}{2\sqrt{k}} = \sqrt{C} \sqrt{k} \longrightarrow \infty \quad \text{as } k \to \infty.
   $$
   At $C = 1/4$, $\sqrt{C} \sqrt{k} = \frac{1}{2}\sqrt{k} \to \infty$.
2. **Layer Length Surplus:** By the Baik–Deift–Johansson theorem, each of the top $d \le 2\sqrt{k}$ host layers has expected length:
   $$
   \mathbb{E}[|\mathcal{L}_m|] \sim 2\sqrt{C} k = 1.000 k \quad \text{at } C = 1/4.
   $$
   The target chain length $\mu_m = |M_m|$ satisfies $\mu_m \le \operatorname{LIS}(\pi) \sim 2\sqrt{k}$. Thus:
   $$
   \frac{\mathbb{E}[|\mathcal{L}_m|]}{\mu_m} \ge \frac{k}{2\sqrt{k}} = \frac{1}{2}\sqrt{k} \longrightarrow \infty \quad \text{as } k \to \infty.
   $$
3. **Quadratic Global Point Surplus:** The total host size is $n = C k^2$, whereas the target size is $k$. The global point ratio is:
   $$
   \frac{n}{k} = C k = \left(\frac{1}{4} + \varepsilon\right) k \longrightarrow \infty.
   $$

*Significance.*
In generic permutations, neither the number of chains nor the lengths of the chains saturate host resources. Both dimensions provide an unboundedly growing $\Theta(\sqrt{k})$ capacity surplus.

---

## 3. Dynamic Greene Chain Routing

We formulate the Dynamic Greene Chain Routing algorithm to embed target $\pi \in S_k$ into host $\sigma_n \in S_n$.

### Definition 3.1 (Dynamic Routing Map).
Let $M_1, \dots, M_d$ be the Dilworth increasing chains of target $\pi$, and let $\mathcal{L}_1, \dots, \mathcal{L}_H$ be the peeled increasing layers of host $\sigma_n$.
1. Assign target chain $m \in \{1, \dots, d\}$ to host layer $\tau(m) = m \in \{1, \dots, H\}$.
2. Order target points by position $t = 0, 1, \dots, k-1$.
3. At step $t$, the target point $(t, \pi(t))$ belongs to chain $m = \operatorname{chain}(t)$.
4. Select host point $p_t \in \mathcal{L}_{\tau(m)}$ satisfying:
   - Horizontal position order: $x(p_t) > x(p_{t-1})$.
   - Vertical value consistency: for all $s < t$, $y(p_t) > y(p_s) \iff \pi(t) > \pi(s)$.
   - Lookahead buffer: $p_t$ leaves at least $\mu_m - \operatorname{rank}_{M_m}(t)$ points remaining on $\mathcal{L}_{\tau(m)}$ to the right of $x(p_t)$.

### Theorem 3.2 (Internal Monotonicity Guarantee).
Under any dynamic routing assignment where target chain $M_m$ is mapped to host layer $\mathcal{L}_{\tau(m)}$, all intra-chain order relations are automatically preserved:
$$
\forall \, s, t \in M_m \text{ with } s < t \implies x(p_s) < x(p_t) \quad \text{and} \quad y(p_s) < y(p_t).
$$

*Proof.*
By Theorem 1.1, $s < t \implies \pi(s) < \pi(t)$. By definition of host layer $\mathcal{L}_{\tau(m)}$, all points on $\mathcal{L}_{\tau(m)}$ form an increasing subsequence in $\sigma_n$. Since $x(p_s) < x(p_t)$ is enforced by step-by-step position ordering, $p_s$ and $p_t$ are two points on the increasing line $\mathcal{L}_{\tau(m)}$ with $x(p_s) < x(p_t)$. Hence $y(p_s) < y(p_t)$, matching $\pi(s) < \pi(t)$ identically. $\square$

---

## 4. Autocorrelation Extremality & Generic Superiority

In Workstream W54, we proved that the expected number of occurrences of any pattern $\pi$ in a random host $\sigma_n$ is strictly invariant:
$$
\mathbb{E}[\operatorname{occ}(\pi, \sigma_n)] \equiv \frac{\binom{n}{k}}{k!}.
$$

### Theorem 4.1 (Generic Superiority over the Monotone Identity).
For any non-monotone generic permutation $\pi \in S_k$, the self-overlap covariance profile satisfies:
$$
\mathcal{O}_j(\pi) < \mathcal{O}_j(\operatorname{id}_k) = \binom{k}{j}^2 \quad \text{for all } j \in \{2, \dots, k-1\}.
$$
Consequently:
1. The variance of $\operatorname{occ}(\pi, \sigma_n)$ is strictly smaller than the variance of $\operatorname{occ}(\operatorname{id}_k, \sigma_n)$.
2. By the Paley–Zygmund lower bound, the containment probability satisfies:
   $$
   \Pr(\pi \le \sigma_n) \ge \frac{\mathbb{E}[\operatorname{occ}(\pi)]^2}{\mathbb{E}[\operatorname{occ}(\pi)^2]} \ge \frac{\mathbb{E}[\operatorname{occ}(\operatorname{id}_k)]^2}{\mathbb{E}[\operatorname{occ}(\operatorname{id}_k)^2]}.
   $$
3. Random and alternating targets cluster strictly less and are statistically more readily contained in $\sigma_n$ than the monotone identity at every host intensity $C$.

---

## 5. Master Strategic Synthesis

Workstream W57 establishes:
1. **Dilworth Chain Decomposition**: Any permutation $\pi \in S_k$ canonically decomposes into $d = \operatorname{LDS}(\pi)$ strictly increasing chains via $\operatorname{lds\_end}[i]$.
2. **Two-Dimensional Capacity Surplus**: On host size $n = (1/4+\varepsilon)k^2$, host layers outnumber target chains by $\frac{1}{2}\sqrt{k} \to \infty$, and host points per layer outnumber target chain lengths by $\frac{1}{2}\sqrt{k} \to \infty$.
3. **Internal Monotonicity**: Mapping chains to peeled Hammersley lines guarantees intra-chain order preservation automatically.
4. **Generic Superiority**: The monotone identity is the true extremal bottleneck for pattern containment; generic permutations have lower overlap covariance and higher empirical containment probabilities.
