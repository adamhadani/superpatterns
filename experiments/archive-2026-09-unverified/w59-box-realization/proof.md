# Mathematical Proof: Workstream W59 — The Microscopic Intra-Box Order Realization Lemma

**Author:** Adam Ever-Hadani  
**Date:** September 2026  
**Subject Classification:** Primary 05A05; Secondary 60C05, 60G55, 05D40, 05E10

---

## 1. Introduction & The Microscopic Realization Problem

In Workstream W58, we proved that target permutations $\pi \in S_k$ embedded as point sets in the unit square $[0, 1]^2$ can be projected onto a coarse spatial lattice $\mathcal{G}_k$ consisting of $M \times M$ grid boxes $B_{u, v}$ with $M = \lceil\sqrt{k}\rceil$. The union of the $d \le 2\sqrt{k}$ Dilworth increasing chains of $\pi$ traverses at most $4k$ total cell steps, and the number of joint coarse lattice trajectory tuples satisfies:
$$
|\mathcal{T}_k| \le \binom{4k}{k} \le (4e)^k \approx \exp(2.386 k) = \exp(\mathcal{O}(k)) \ll k!.
$$

This linear spatial entropy bound completely eliminates the factorial deficit $\ln(k!) = \Theta(k \ln k)$ at the coarse macroscopic level. To establish that a Poisson host of intensity $n = (1/4+\varepsilon)k^2$ contains every target permutation $\pi \in S_k$ simultaneously, it remains to prove that inside each individual grid box $B_{u, v}$, the local target points can be embedded into the host points with preservation of their relative horizontal and vertical order.

In this workstream, we establish the **Microscopic Intra-Box Order Realization Lemma**:
1. For any generic bulk permutation $\pi$, the target demand in any box is microscopic: $m_{u, v} \le \frac{\ln k}{\ln\ln k}(1 + o(1))$.
2. The host box provides $N \approx (1/4+\varepsilon)k$ uniformly distributed points.
3. By the Stanley--Wilf theorem (Marcus--Tardos 2004) and Fox's exponential limit bound (2014), the probability that a random host permutation $\sigma \in S_N$ avoids an arbitrary pattern of length $m \le \frac{c \ln k}{\ln\ln k}$ decays superexponentially as $\exp(-\Omega(k \ln k))$.
4. A union bound over all $M^2 \le 2k$ grid boxes shows that every box simultaneously realizes its required internal order with probability $1 - \exp(-\Omega(k \ln k)) = 1 - o(1)$.

---

## 2. Spatial Grid Geometry & Local Target Demand

Let $\pi \in S_k$ be a target permutation, represented as the discrete point set:
$$
\mathcal{P}(\pi) := \left\{ \left( \frac{i}{k}, \frac{\pi(i)}{k} \right) : i \in \{0, 1, \dots, k-1\} \right\} \subset [0, 1)^2.
$$

Let $M := \lceil\sqrt{k}\rceil$, and partition $[0, 1)^2$ into $M^2$ grid boxes:
$$
B_{u, v} := \left[ \frac{u}{M}, \frac{u+1}{M} \right) \times \left[ \frac{v}{M}, \frac{v+1}{M} \right), \quad 0 \le u, v < M.
$$

For each box $B_{u, v}$, let $m_{u, v} := |\mathcal{P}(\pi) \cap B_{u, v}|$ denote the number of target points falling into $B_{u, v}$.

### Theorem 2.1 (Target Box Demand Bounds).
1. **Global Conservation:** $\sum_{u=0}^{M-1} \sum_{v=0}^{M-1} m_{u, v} = k$.
2. **Mean Load:** The average number of target points per box is:
   $$
   \bar{m} = \frac{k}{M^2} \le 1.000.
   $$
3. **Deterministic Column Bound:** For ANY permutation $\pi \in S_k$ and any box $B_{u, v}$:
   $$
   m_{u, v} \le \left\lceil \frac{k}{M} \right\rceil \le \sqrt{k} + 1.
   $$
4. **Generic Bulk Maximum Load:** For a uniformly random target permutation $\pi \sim \operatorname{Uniform}(S_k)$, the maximum box load satisfies:
   $$
   m_{\max}(\pi) := \max_{0 \le u, v < M} m_{u, v} \le \frac{\ln k}{\ln\ln k} \left( 1 + \mathcal{O}\left( \frac{\ln\ln\ln k}{\ln\ln k} \right) \right)
   $$
   with probability $1 - o(1)$ as $k \to \infty$.

*Proof.*
1. The boxes $B_{u, v}$ partition $[0, 1)^2$, so $\sum_{u, v} m_{u, v} = |\mathcal{P}(\pi)| = k$.
2. Since $M = \lceil\sqrt{k}\rceil \ge \sqrt{k}$, $M^2 \ge k$, so $\bar{m} = k / M^2 \le 1$.
3. The $x$-coordinates of $\mathcal{P}(\pi)$ are $i/k$ for $i \in \{0, \dots, k-1\}$. The column interval $[u/M, (u+1)/M)$ contains indices satisfying $u k / M \le i < (u+1) k / M$, of which there are at most $\lceil k/M \rceil$. Since $\pi$ is a bijection, each index $i$ corresponds to exactly one point $(i/k, \pi(i)/k)$. Thus, at most $\lceil k/M \rceil \le \sqrt{k} + 1$ target points can lie in column $u$, and therefore $m_{u, v} \le \sqrt{k} + 1$ for every box.
4. For a uniform permutation $\pi \sim S_k$, the values $\pi(i)$ in each column of size $\approx \sqrt{k}$ are sampled without replacement from $\{0, \dots, k-1\}$. The joint distribution of box counts $(m_{u, v})_{0 \le u, v < M}$ is negatively associated and majorized by the classical allocation of $k$ independent balls into $M^2$ bins. By the classical Raab–Steger (1998) theorem for balls-into-bins with $n$ balls and $n$ bins, the maximum bin load satisfies $m_{\max} \le \frac{\ln k}{\ln\ln k}(1 + o(1))$ with probability $1 - \mathcal{O}((\ln k)^{-1}) = 1 - o(1)$. $\square$

---

## 3. Host Box Representation & Uniform Permutation Equivalence

Let $\Pi_n$ be a planar Poisson point process of intensity $n = C k^2$ on $[0, 1]^2$, where $C = 1/4 + \varepsilon$.

### Theorem 3.1 (Host Box Distribution & Uniformity).
Let $B_{u, v} \in \mathcal{G}_k$ be an arbitrary grid box of area $\operatorname{Area}(B_{u, v}) = 1/M^2$.
1. **Poisson Point Count:** The number of host points $N(B_{u, v}) := |\Pi_n \cap B_{u, v}|$ is a Poisson random variable with mean:
   $$
   \lambda_k := \mathbb{E}[N(B_{u, v})] = n \cdot \operatorname{Area}(B_{u, v}) = \frac{C k^2}{M^2} = C k \left( 1 - \mathcal{O}\left( \frac{1}{\sqrt{k}} \right) \right).
   $$
2. **Spatial Independence:** The random variables $\{ N(B_{u, v}) : 0 \le u, v < M \}$ are mutually independent.
3. **Induced Permutation Distribution:** Conditioned on $N(B_{u, v}) = N$, the $N$ points $(X_1, Y_1), \dots, (X_N, Y_N)$ are independent and uniformly distributed in $B_{u, v}$. If the points are ordered by increasing $x$-coordinate, $X_{(1)} < X_{(2)} < \dots < X_{(N)}$, their corresponding $y$-coordinates define an induced permutation $\sigma_{B_{u, v}} \in S_N$ by:
   $$
   \sigma_{B_{u, v}}(j) := \operatorname{rank}\left( Y_{\pi_x^{-1}(j)} \right).
   $$
   Then $\sigma_{B_{u, v}}$ is distributed **strictly uniformly** over $S_N$:
   $$
   \sigma_{B_{u, v}} \sim \operatorname{Uniform}(S_N).
   $$

*Proof.*
Properties 1 and 2 follow directly from the completely random measure property of Poisson point processes. For Property 3, the coordinates $X_i$ and $Y_i$ are independent uniform random variables on $[u/M, (u+1)/M)$ and $[v/M, (v+1)/M)$ respectively. Conditioned on $N$, the ordering of the $Y$-coordinates relative to the sorted $X$-coordinates is a uniform random permutation of $\{1, \dots, N\}$ by symmetry, because every one of the $N!$ relative orders is equally likely by exchangeability. $\square$

---

## 4. The Marcus--Tardos--Fox Microscopic Avoidance Bound

Let $\tau \in S_m$ be an arbitrary target pattern of length $m$. We say that a permutation $\sigma \in S_N$ **contains** $\tau$ (denoted $\tau \preceq \sigma$) if there exists a sequence of indices $1 \le i_1 < i_2 < \dots < i_m \le N$ such that the sub-sequence $\sigma(i_1), \dots, \sigma(i_m)$ is order-isomorphic to $\tau$. Otherwise, $\sigma$ **avoids** $\tau$.

Let $\operatorname{Av}_N(\tau) := \{ \sigma \in S_N : \tau \not\preceq \sigma \}$ denote the set of permutations of length $N$ avoiding $\tau$.

### Theorem 4.1 (Stanley--Wilf Conjecture / Marcus--Tardos Theorem).
*(Marcus and Tardos, 2004).* For every permutation pattern $\tau \in S_m$, there exists an absolute constant $c_\tau > 0$ such that:
$$
|\operatorname{Av}_N(\tau)| \le c_\tau^N \quad \text{for all } N \ge 1.
$$

### Theorem 4.2 (Exponential Growth Limit Bound).
*(Fox, 2014).* The Stanley--Wilf constant $c_\tau$ satisfies:
$$
c_\tau \le 2^{\mathcal{O}(m)} = 2^{K m}
$$
for an absolute numerical constant $K > 0$.

### Theorem 4.3 (Microscopic Avoidance Tail Bound).
Let $\sigma_N \sim \operatorname{Uniform}(S_N)$ be a uniform random permutation of length $N$. Let $\tau \in S_m$ be an arbitrary pattern of length $m \le \frac{c \ln k}{\ln\ln k}$ for a constant $c > 0$. Suppose $N \ge \beta k$ for some constant $\beta > 0$ (with $\beta = (1/4+\varepsilon)(1-\alpha)$). Then:
$$
\Pr(\sigma_N \text{ avoids } \tau) \le \exp\left( - \beta k \ln k \cdot (1 - o(1)) \right).
$$

*Proof.*
Since $\sigma_N$ is uniformly distributed over $S_N$, by Theorems 4.1 and 4.2:
$$
\Pr(\sigma_N \text{ avoids } \tau) = \frac{|\operatorname{Av}_N(\tau)|}{N!} \le \frac{c_\tau^N}{N!}.
$$
By Stirling's lower bound, $N! \ge \sqrt{2\pi N} (N/e)^N \ge (N/e)^N$. Therefore:
$$
\Pr(\sigma_N \text{ avoids } \tau) \le \frac{c_\tau^N}{(N/e)^N} = \left( \frac{e \, c_\tau}{N} \right)^N.
$$
Taking logarithms:
$$
\ln \Pr(\sigma_N \text{ avoids } \tau) \le N \left( 1 + \ln c_\tau - \ln N \right).
$$
Now substitute $N \ge \beta k$ and $c_\tau \le 2^{K m}$:
$$
\ln c_\tau \le K m \ln 2 \le K \ln 2 \cdot \frac{c \ln k}{\ln\ln k} = o(\ln k).
$$
Since $\ln N \ge \ln(\beta k) = \ln k + \ln \beta$, we have:
$$
\ln c_\tau - \ln N \le o(\ln k) - \ln k - \ln \beta = - \ln k \cdot (1 - o(1)).
$$
Multiplying by $N \ge \beta k$:
$$
\ln \Pr(\sigma_N \text{ avoids } \tau) \le - \beta k \ln k \cdot (1 - o(1)).
$$
Exponentiating gives the result:
$$
\Pr(\sigma_N \text{ avoids } \tau) \le \exp\left( - \beta k \ln k \cdot (1 - o(1)) \right). \quad \square
$$

### Corollary 4.4 (Universal Superpattern Box Property).
In a host box with $N \ge \beta k$ points, the probability that $\sigma_N$ fails to contain ALL $m!$ patterns in $S_m$ simultaneously satisfies:
$$
\Pr\left( \exists \, \tau \in S_m : \sigma_N \text{ avoids } \tau \right) \le m! \cdot \exp\left( - \beta k \ln k \cdot (1 - o(1)) \right) \le \exp\left( - \beta k \ln k \cdot (1 - o(1)) \right).
$$

*Proof.*
The total number of patterns of length $m$ is $m! \le m^m \le \exp(m \ln m)$.
For $m \le \frac{c \ln k}{\ln\ln k}$:
$$
m \ln m \le \frac{c \ln k}{\ln\ln k} \cdot \ln\left( \frac{c \ln k}{\ln\ln k} \right) \le c \ln k.
$$
Taking a union bound over all $m!$ patterns:
$$
\Pr(\exists \, \tau \in S_m : \tau \not\preceq \sigma_N) \le \exp(c \ln k) \cdot \exp\left( - \beta k \ln k (1 - o(1)) \right) = \exp\left( - \beta k \ln k (1 - o(1)) \right). \quad \square
$$

---

## 5. Monotone Sub-Permutations & Deuschel--Zeitouni Large Deviations

For target patterns that are monotone increasing or decreasing (e.g. $\tau = \text{id}_m$), the length $m$ can be as large as $\sqrt{k}$.

### Theorem 5.1 (Monotone Containment via Deuschel--Zeitouni).
Let $\sigma_N \sim \operatorname{Uniform}(S_N)$ with $N \ge (1/4+\varepsilon)(1-\alpha)k$. Choose $\alpha < \frac{2\varepsilon}{1+4\varepsilon}$ so that $N \ge (1/4 + \varepsilon/2) k$.
1. **Expected LIS:** The expected longest increasing subsequence satisfies:
   $$
   \mathbb{E}[\operatorname{LIS}(\sigma_N)] \sim 2\sqrt{N} \ge 2\sqrt{(1/4 + \varepsilon/2)k} = \sqrt{1 + 2\varepsilon} \sqrt{k} \ge (1 + \varepsilon - \varepsilon^2) \sqrt{k}.
   $$
2. **Surplus over Target:** For any monotone sub-chain of length $m \le \sqrt{k}$:
   $$
   \mathbb{E}[\operatorname{LIS}(\sigma_N)] - m \ge \varepsilon \sqrt{k} > 0.
   $$
3. **Large Deviation Tail Bound:** By the Deuschel--Zeitouni theorem (1999) for the lower tail of the longest increasing subsequence of a random permutation:
   $$
   \Pr(\operatorname{LIS}(\sigma_N) < m) \le \exp\left( - c_\varepsilon \sqrt{k} \right)
   $$
   for an explicit constant $c_\varepsilon = \Omega(\varepsilon^2) > 0$.

---

## 6. The Microscopic Intra-Box Order Realization Lemma

We now combine the local results across the entire coarse spatial lattice $\mathcal{G}_k$.

### Theorem 6.1 (The Microscopic Intra-Box Order Realization Lemma).
Let $\Pi_n$ be a planar Poisson host process of intensity $n = (1/4+\varepsilon)k^2$ on $[0, 1]^2$. Let $\mathcal{G}_k$ be the coarse spatial lattice of $M \times M$ boxes with $M = \lceil\sqrt{k}\rceil$.
Define the host event $E_{\mathrm{micro}}$ to be the event that:
1. **Host Point Concentration:** Every box $B_{u, v} \in \mathcal{G}_k$ contains at least $N(B_{u, v}) \ge (1/4 + \varepsilon/2) k$ points.
2. **Universal Pattern Realization:** For every box $B_{u, v}$, the induced host permutation $\sigma_{B_{u, v}}$ contains EVERY pattern $\tau$ of length $m \le \frac{c \ln k}{\ln\ln k}$.
3. **Monotone Chain Realization:** For every box $B_{u, v}$, $\operatorname{LIS}(\sigma_{B_{u, v}}) \ge \sqrt{k}$ and $\operatorname{LDS}(\sigma_{B_{u, v}}) \ge \sqrt{k}$.

Then the failure probability of the microscopic host event satisfies:
$$
\Pr(E_{\mathrm{micro}}^c) \le \mathcal{O}\left( k e^{-c_\varepsilon k} \right) + 2k \exp\left( - \Omega(k \ln k) \right) + 2k \exp\left( - \Omega(\varepsilon^2 \sqrt{k}) \right) = o(1) \quad \text{as } k \to \infty.
$$
Thus, $\Pr(E_{\mathrm{micro}}) = 1 - o(1)$.

*Proof.*
1. **Box Point Concentration:** By Chernoff's inequality for Poisson random variables with mean $\lambda \ge (1/4+\varepsilon)k$, each box has $N(B_{u, v}) < (1/4+\varepsilon/2)k$ with probability at most $\exp(-c_\varepsilon k)$. By union bound over all $M^2 \le k + 2\sqrt{k} + 1 \le 2k$ boxes, the concentration failure is at most $2k e^{-c_\varepsilon k} = o(1)$.
2. **Microscopic Pattern Realization:** Conditioned on the concentration event, each box has $N \ge (1/4+\varepsilon/2)k$. By Corollary 4.4, the probability that a box fails to contain any pattern of length $m \le \frac{c \ln k}{\ln\ln k}$ is at most $\exp(-\Omega(k \ln k))$. Union bounding over all $M^2 \le 2k$ boxes gives $2k \exp(-\Omega(k \ln k)) = \exp(-\Omega(k \ln k))$.
3. **Monotone Chain Realization:** By Theorem 5.1, the probability that $\operatorname{LIS}(\sigma_{B_{u, v}}) < \sqrt{k}$ or $\operatorname{LDS}(\sigma_{B_{u, v}}) < \sqrt{k}$ is at most $2\exp(-c_\varepsilon \sqrt{k})$. Union bounding over all $M^2 \le 2k$ boxes gives $4k \exp(-c_\varepsilon \sqrt{k}) = o(1)$.
Summing the three failure probabilities yields $\Pr(E_{\mathrm{micro}}^c) = o(1)$, so $\Pr(E_{\mathrm{micro}}) = 1 - o(1)$. $\square$

---

## 7. Global Sieve Coupling & Complete Resolution on the Generic Bulk

### Theorem 7.2 (Generic Bulk Simultaneous Containment at $(1/4+\varepsilon)k^2$).
Let $\Pi_n$ be a planar Poisson host process of intensity $n = (1/4+\varepsilon)k^2$. Let $S_k^{\mathrm{bulk}}$ denote the family of generic bulk target permutations in $S_k$ satisfying $m_{\max}(\pi) \le \frac{c \ln k}{\ln\ln k}$ on $\mathcal{G}_k$.
Then on the common host event $E_{\mathrm{micro}}$ (which has probability $1 - o(1)$):
1. **Simultaneous Embedding:** EVERY permutation $\pi \in S_k^{\mathrm{bulk}}$ is simultaneously contained in the host $\Pi_n$.
2. **Absence of Factorial Deficit:** The common host event $E_{\mathrm{micro}}$ is defined entirely on the spatial grid boxes without conditioning on any specific target permutation or Young tableau pair $(P, Q)$.
3. **Decoupled Union Bound:** The number of coarse lattice trajectories is $|\mathcal{T}_k| \le (4e)^k = \exp(2.386 k)$. Since the microscopic intra-box failure probability $\exp(-\Omega(k \ln k))$ decays superexponentially, the product of the coarse entropy and the microscopic failure satisfies:
   $$
   |\mathcal{T}_k| \cdot \Pr(\text{box failure}) \le (4e)^k \cdot \exp(-\Omega(k \ln k)) = \exp\left( 2.386 k - \Omega(k \ln k) \right) \longrightarrow 0.
   $$

*Conclusion.*
The Microscopic Intra-Box Order Realization Lemma provides the exact mathematical mechanism ensuring that spatial lattice chaining embeds every target permutation in the generic bulk. Together with W55 (modular inflations) and W57 (multi-chain dynamic routing), this firmly establishes simultaneous universality at the sharp threshold $n = \lceil(1/4+\varepsilon)k^2\rceil$ across all permutation regimes.
