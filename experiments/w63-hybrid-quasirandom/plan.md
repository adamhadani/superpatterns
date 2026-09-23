# Workstream W63: Hybrid Structured/Quasirandom Decomposition & Thread Decoupling

## Objective
Investigate whether extracting macroscopic structured blocks first (via polynomial shared squares) leaves a residual permutation $\mathcal{Q}$ whose thread-synchronization set $F(\mathcal{Q})$ is so small that multi-threaded scanning succeeds at $m = \mathcal{O}(k)$ columns (i.e. quadratic host length $n = C k^2$), eliminating the $\log\log k$ factor from He and Kwan (2020).

## Background: The He–Kwan Mechanism
In He and Kwan (2020), a uniform random permutation $\sigma \in S_n$ is coupled to a $(2k) \times m$ matrix $M$ with independent Bernoulli(1/2) entries, where $m = n/(4k)$.
- For a target permutation $\pi \in S_k$, a thread $t \in [k]$ greedily scans rows $t+1, \dots, t+k$ from left to right.
- Two threads $t$ and $t + \Delta$ synchronize if $\pi$ has a large $\Delta$-shift:
  $$L_\Delta(\pi) = \operatorname{LIS}\big( i \mapsto \pi^{-1}(\pi(i) + \Delta) \big).$$
- He and Kwan required $T = \log^2 k$ threads to beat the $k!$ union bound ($e^{-(k/2)\log^2 k} \ll 1/k!$).
- Avoiding pairwise differences in the bad set $F = \{\Delta : L_\Delta(\pi) \ge \varepsilon k\}$ forced $q = |F| = \log^5 k$.
- Bounding the structured maps $\mathcal{Z}_k$ with $(q, b)$-shift-systems gave $|\mathcal{Z}_k| \le e^{21 k \log\log k}$, which forced matrix width $m = \Theta(k \log\log k)$ and $n = \Theta(k^2 \log\log k)$.

## The Hybrid Approach
1. **Extraction of Structured Blocks:**
   Extract all monotone blocks of size $a_i \ge L = K\sqrt{\log k}$ into $\mathcal{M}$.
   These blocks are embedded into the polynomial shared host squares family $\mathcal{S}$ ($|\mathcal{S}| \le (k+1)^3$), requiring zero exponential description entropy.
2. **Residual Quasirandom Permutation:**
   Let $\mathcal{Q} = [k] \setminus \mathcal{M}$.
   How does extracting $\mathcal{M}$ affect the shift lengths $L_\Delta(\pi, \mathcal{Q})$?
   Does $\mathcal{Q}$ have strictly bounded shifts without requiring $q = \log^5 k$?
3. **Decoupled Common Host Events:**
   Can the scanning event be formulated on a common host event that does not require $T = \log^2 k$ threads to depend on $\pi$?
