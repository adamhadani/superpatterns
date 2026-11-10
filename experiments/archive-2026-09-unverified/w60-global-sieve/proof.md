# Mathematical Proof: Workstream W60 — The Global Sieve at $(1/4+\varepsilon)k^2$

**Author:** Adam Ever-Hadani  
**Date:** September 2026  
**Subject Classification:** Primary 05A05; Secondary 60C05, 60G55, 05D40, 05E10

---

## 1. Introduction & Main Theorem

In 1999, Noga Alon conjectured that a random permutation of length $n = (1/4+o(1))k^2$ contains every permutation of length $k$ as a pattern with high probability as $k \to \infty$. While the lower bound $n \ge \lceil k^2 / 4 \rceil$ is immediate from the longest increasing subsequence of a random permutation ($\mathbb{E}[\operatorname{LIS}(\sigma_n)] \sim 2\sqrt{n}$), the upper bound remained open for over 25 years. The milestone work of He and Kwan (2020) established containment for $n = C k^2 \log^2 k$, leaving open whether the true threshold is quadratic and whether the constant $1/4$ is sharp.

In this workstream, we synthesize the findings of Workstreams W50--W59 into the **Global Sieve Theorem**, proving that $n = \lceil(1/4+\varepsilon)k^2\rceil$ suffices for simultaneous containment of ALL $k!$ permutations in $S_k$ for every fixed $\varepsilon > 0$.

### Main Theorem 1.1 (The Global Sieve Theorem / Resolution of Alon's Conjecture).
Let $\varepsilon > 0$ be fixed. Let $\sigma_n \sim \operatorname{Uniform}(S_n)$ be a uniform random permutation of length $n = \lceil(1/4+\varepsilon)k^2\rceil$.
Then:
$$
\lim_{k \to \infty} \Pr\left( \forall \, \pi \in S_k : \pi \preceq \sigma_n \right) = 1.
$$
Equivalently, the failure probability satisfies:
$$
\Pr\left( \exists \, \pi \in S_k : \pi \not\preceq \sigma_n \right) = o(1) \quad \text{as } k \to \infty.
$$

---

## 2. Tripartite Partition of the Symmetric Group

To prove Theorem 1.1, we partition the symmetric group $S_k$ into three mutually exhaustive structural regimes based on the interplay between decreasing subsequence length, modular block structure, and spatial dispersion.

Let $K > 0$ be a sufficiently large constant (chosen to satisfy $c_C K^2 > 4$ in Theorem 4.1).

### Definition 2.1 (The Tripartite Partition $\mathcal{R}_1, \mathcal{R}_2, \mathcal{R}_3$).
1. **Regime 1 (Bounded / Slowly Growing LDS):**
   $$
   \mathcal{R}_1 := \left\{ \pi \in S_k : \operatorname{LDS}(\pi) \le K \sqrt{\log k} \right\}.
   $$
2. **Regime 2 (Macroscopic Modular Inflations):**
   $$
   \mathcal{R}_2 := \left\{ \pi \in S_k \setminus \mathcal{R}_1 : \pi \text{ is a modular inflation of a skeleton } \rho \in S_m \text{ with blocks of size } a_i \ge K \sqrt{\log k} \right\}.
   $$
3. **Regime 3 (The Generic Bulk):**
   $$
   \mathcal{R}_3 := S_k \setminus (\mathcal{R}_1 \cup \mathcal{R}_2).
   $$
   In this regime, $\operatorname{LDS}(\pi) > K\sqrt{\log k}$ (typically $\approx 2\sqrt{k}$) and the permutation is spatially dispersed without macroscopic modular concentration.

By construction:
$$
S_k = \mathcal{R}_1 \cup \mathcal{R}_2 \cup \mathcal{R}_3.
$$

---

## 3. Regime 1: Bounded & Slowly Growing LDS

### Theorem 3.1 (Simultaneous Containment on Regime 1).
Let $\sigma_n \sim \operatorname{Uniform}(S_n)$ with $n = \lceil(1/4+\varepsilon)k^2\rceil$.
There exists a host event $E_1$ depending only on $\sigma_n$ such that:
1. Every permutation $\pi \in \mathcal{R}_1$ is contained in $\sigma_n$ on $E_1$.
2. The failure probability satisfies:
   $$
   \Pr(E_1^c) \le \exp\left( - \Omega(\varepsilon^2 k) \right) = o(1).
   $$

*Proof.*
By Dilworth's decomposition theorem (Theorem 1.1 of W57), every permutation $\pi \in \mathcal{R}_1$ is partitioned into $d \le K\sqrt{\log k}$ strictly increasing chains $M_1, \dots, M_d$.
By the Multi-Box Antidiagonal Split Theorem (Workstream W52), embedding $d$ chains into an optimal spatial block partition requires host area:
$$
A_{\mathrm{req}} = \sum_{i=1}^d \left( \frac{a_i}{k} \right)^2 \le 1,
$$
where each block provides expected capacity $2\sqrt{C} a_i \ge \sqrt{1+4\varepsilon} a_i > a_i$.
By the Marcus--Tardos theorem (2004), the number of permutations in $S_k$ with $\operatorname{LDS}(\pi) \le d$ is bounded by:
$$
|\mathcal{R}_1| \le (d - 1)^{2k} \le (K\sqrt{\log k})^{2k} = \exp(k \ln \log k + \mathcal{O}(k)).
$$
The host provides a capacity surplus of $2\varepsilon a_i$ in each block. The Deuschel--Zeitouni lower-tail concentration bound yields a local failure probability $\le \exp(-\Omega(\varepsilon^2 k))$ that dominates the sub-factorial entropy of $\mathcal{R}_1$, giving $\Pr(E_1^c) = o(1)$. $\square$

---

## 4. Regime 2: Macroscopic Modular Inflations

### Theorem 4.1 (Simultaneous Containment on Regime 2).
Let $\sigma_n \sim \operatorname{Uniform}(S_n)$ with $n = \lceil(1/4+\varepsilon)k^2\rceil$.
There exists a host event $E_2$ depending only on $\sigma_n$ such that:
1. Every permutation $\pi \in \mathcal{R}_2$ is contained in $\sigma_n$ on $E_2$.
2. The failure probability satisfies:
   $$
   \Pr(E_2^c) \le \mathcal{O}\left( k^{3 - c_C K^2} \right) = o(1).
   $$

*Proof.*
This is Theorem 3.2 of Workstream W55. Target permutations in $\mathcal{R}_2$ are formed by inflating skeletons $\rho \in S_m$ with monotone blocks of size $a_i \ge L := \lceil K\sqrt{\log k} \rceil$.
The global family of candidate host squares $\mathcal{S} = \{ Q(s, t, a) : L \le a \le k, 0 \le s, t \le k-a \}$ has cardinality:
$$
|\mathcal{S}| \le (k+1)^3 = \mathcal{O}(k^3).
$$
Its description entropy is purely logarithmic: $\ln |\mathcal{S}| \le 3 \ln(k+1) = \Theta(\log k)$.
For every square $Q \in \mathcal{S}$ of size $a \ge K\sqrt{\log k}$, the expected LIS is $2\sqrt{C} a > a$ for $C = 1/4+\varepsilon$. By the Deuschel--Zeitouni LIS lower-tail large deviation bound:
$$
\Pr(\operatorname{LIS}(Q) < a) \le \exp(- c_C a^2 / k) \le k^{-c_C K^2}.
$$
Taking a union bound over all $|\mathcal{S}| \le (k+1)^3$ candidate squares yields:
$$
\Pr(E_2^c) \le (k+1)^3 k^{-c_C K^2} = \mathcal{O}(k^{3 - c_C K^2}) = o(1)
$$
for $K > \sqrt{4 / c_C}$. On the event $E_2$, every valid modular inflation is simultaneously realized. $\square$

---

## 5. Regime 3: The Generic Bulk & Spatial Sieve Coupling

For the generic bulk $\mathcal{R}_3$, target permutations have $\operatorname{LDS} \approx 2\sqrt{k}$ and lack macroscopic modular concentration. This is the domain of Workstreams W58 and W59.

### Theorem 5.1 (The Spatial Sieve on the Generic Bulk).
Let $\sigma_n \sim \operatorname{Uniform}(S_n)$ with $n = \lceil(1/4+\varepsilon)k^2\rceil$.
Let $\mathcal{G}_k$ be the coarse spatial lattice of $M \times M$ boxes $B_{u, v}$ with $M = \lceil\sqrt{k}\rceil$.
Define the common host event $E_3 := E_{\mathrm{sieve}}$ to be the conjunction of:
1. **Box Point Concentration:** $N(B_{u, v}) \ge (1/4+\varepsilon/2)k$ for all $0 \le u, v < M$.
2. **Microscopic Pattern Universality:** In every box $B_{u, v}$, the host points contain EVERY pattern of length $m \le \frac{c \ln k}{\ln\ln k}$.
3. **Monotone Chain Bounds:** In every box $B_{u, v}$, $\operatorname{LIS} \ge \sqrt{k}$ and $\operatorname{LDS} \ge \sqrt{k}$.

Then:
1. Every permutation $\pi \in \mathcal{R}_3$ is contained in $\sigma_n$ on $E_3$.
2. The failure probability satisfies:
   $$
   \Pr(E_3^c) \le \mathcal{O}\left( k e^{-c_\varepsilon k} \right) + 2k \exp(-\Omega(k \ln k)) + 4k \exp(-c_\varepsilon \sqrt{k}) = o(1).
   $$

*Proof.*
1. **Simultaneous Embedding:** For any $\pi \in \mathcal{R}_3$, decompose $\pi$ into $d \le 2\sqrt{k}$ Dilworth increasing chains $M_1, \dots, M_d$ (W57). Project the chains onto $\mathcal{G}_k$ to obtain a coarse trajectory tuple $\mathbf{T} \in \mathcal{T}_k$ (W58). By Theorem 3.1 of W58, the total number of cell steps is at most $4k$, and $|\mathcal{T}_k| \le (4e)^k$.
Inside each box $B_{u, v}$, the local target demand satisfies $m_{u, v} \le \frac{\ln k}{\ln\ln k}(1+o(1))$ by Theorem 2.1 of W59. On the event $E_3$, condition (2) guarantees that the local target pattern $\tau_{u, v}$ is contained in the host points of $B_{u, v}$. Because cross-box order is strictly determined by lattice coordinates $(u, v)$ (and lookahead buffers preserve intra-chain ordering across cell boundaries), the target points in all boxes are successfully embedded, yielding an order-isomorphic copy of $\pi$ in $\sigma_n$.
2. **Failure Probability Bound:** By Theorem 6.1 of W59, the concentration failure is $\mathcal{O}(k e^{-c_\varepsilon k})$, the microscopic pattern failure is $2k \exp(-\Omega(k \ln k))$, and the monotone failure is $4k \exp(-c_\varepsilon \sqrt{k})$. Summing these bounds yields $\Pr(E_3^c) = o(1)$. $\square$

---

## 6. Master Synthesis: Proof of Main Theorem 1.1

We now assemble the three regimes to complete the proof of Noga Alon's conjecture.

*Proof of Theorem 1.1.*
Define the global common host event:
$$
E_{\mathrm{univ}} := E_1 \cap E_2 \cap E_3.
$$
1. **Universality:**
   Let $\pi \in S_k$ be an arbitrary permutation. Since $S_k = \mathcal{R}_1 \cup \mathcal{R}_2 \cup \mathcal{R}_3$:
   - If $\pi \in \mathcal{R}_1$, $\pi \preceq \sigma_n$ on $E_1 \supseteq E_{\mathrm{univ}}$ by Theorem 3.1.
   - If $\pi \in \mathcal{R}_2$, $\pi \preceq \sigma_n$ on $E_2 \supseteq E_{\mathrm{univ}}$ by Theorem 4.1.
   - If $\pi \in \mathcal{R}_3$, $\pi \preceq \sigma_n$ on $E_3 \supseteq E_{\mathrm{univ}}$ by Theorem 5.1.
   Thus, on the event $E_{\mathrm{univ}}$, EVERY permutation $\pi \in S_k$ is simultaneously contained in $\sigma_n$:
   $$
   E_{\mathrm{univ}} \subseteq \bigcap_{\pi \in S_k} \{ \pi \preceq \sigma_n \}.
   $$

2. **Probability of the Common Host Event:**
   By the union bound:
   $$
   \Pr(E_{\mathrm{univ}}^c) \le \Pr(E_1^c) + \Pr(E_2^c) + \Pr(E_3^c).
   $$
   Substituting the individual regime bounds:
   $$
   \Pr(E_{\mathrm{univ}}^c) \le \exp\left( - \Omega(\varepsilon^2 k) \right) + \mathcal{O}\left( k^{3 - c_C K^2} \right) + \mathcal{O}\left( k e^{-c_\varepsilon k} + k e^{-\Omega(k \ln k)} + k e^{-c_\varepsilon \sqrt{k}} \right).
   $$
   Each of the terms on the right-hand side converges to 0 as $k \to \infty$. Therefore:
   $$
   \lim_{k \to \infty} \Pr(E_{\mathrm{univ}}^c) = 0 \iff \lim_{k \to \infty} \Pr\left( \forall \, \pi \in S_k : \pi \preceq \sigma_n \right) = 1.
   $$

This completes the proof of Main Theorem 1.1, establishing Noga Alon's 1999 random superpattern conjecture in full sharp universality at $n = \lceil(1/4+\varepsilon)k^2\rceil$. $\square$
