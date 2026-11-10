# Workstream W68: Quasirandom Permuton Conditioning & Deterministic Bulk Embedding at $C^* = 1/4$

**Author:** Adam Ever-Hadani  
**Date:** September 2026  
**Objective:** Resolve the generic bulk factorial deficit ($k! \approx \exp(k \ln k)$ vs 1D failure $\exp(-\Omega(\varepsilon^2 k))$) at the sharp threshold $C^* = 1/4 = 0.25000$ via 2D macroscopic permuton regularity and missing-pattern cluster sieving.

---

## 1. Problem Formulation & The Fundamental Gap

In W66 and W67, the investigation of Noga Alon's conjecture at $C^* = 1/4$ reached the following precise mathematical juncture:
1. For any individual target permutation $\pi \in S_k$, $\Pr(\pi \le \sigma_n) \ge 1 - \exp(-\Omega(\varepsilon^2 k))$ at $n = \lceil(1/4+\varepsilon)k^2\rceil$.
2. For the monotone identity $\operatorname{id}_k$, the avoidance probability decays quadratically as $P_0(\operatorname{id}_k) \sim \tau_0 \exp(-\frac{4}{3}\varepsilon^3 k^2) \ll 1/k!$.
3. For structured classes (bounded LDS, modular inflations), simultaneous universality at $C^* = 1/4$ is unconditionally proved with failure $o(1)$.
4. The remaining open barrier is simultaneous universality on the generic bulk ($d \approx 2\sqrt{k}$, $k! \approx \exp(k \ln k)$ targets): a naive sum $\sum_{\pi} P_0(\pi)$ of 1D failure rates diverges because $\exp(k \ln k - c \varepsilon^2 k) \to +\infty$.

---

## 2. Research Strategy for W68

We attack this barrier through two complementary, rigorous mathematical channels:

### Channel A: Macroscopic Permuton Regularity & VC Quadratic Sieve
- Partition $[0, 1]^2$ into a grid of $M \times M$ macroscopic boxes $B_{u, v}$ with $M = \mathcal{O}(1)$.
- By Chernoff concentration, the probability that any macroscopic box has point count deviating from its expectation $n/M^2 = (1/4+\varepsilon)k^2 / M^2$ by more than $\delta$ decays as:
  $$\Pr(E_{\mathrm{reg}}^c) \le M^2 \exp\left( - c_\delta (1/4+\varepsilon) k^2 / M^2 \right) = \exp\left( - \Omega(k^2) \right) \ll \frac{1}{k!}.$$
- Conditioning on $E_{\mathrm{reg}}$, the host possesses deterministic uniform spatial transport across macroscopic coordinates.

### Channel B: The Missing-Pattern Cluster Sieve
- Let $M(\sigma_n) = \sum_{\pi \in S_k} \mathbf{1}_{\pi \not\le \sigma_n}$ be the total count of missing patterns.
- The simultaneous failure probability satisfies:
  $$\Pr(M > 0) = \frac{\mathbb{E}[M]}{\mathbb{E}[M \mid M > 0]}.$$
- If a host $\sigma_n$ fails to be universal, it is typically in a globally degraded state (such as a macroscopic void or global LIS collapse), which simultaneously eliminates a large fraction of all patterns ($R = \mathbb{E}[M \mid M > 0] = \Omega(k!)$).
- When $R \ge \delta k!$, the simultaneous failure probability is bounded by:
  $$\Pr(M > 0) \le \frac{1}{\delta} \bar{P}_0,$$
  where $\bar{P}_0 = \frac{1}{k!} \sum_{\pi} P_0(\pi)$ is the average avoidance probability of a typical pattern, completely canceling the factorial deficit!

---

## 3. Computational Implementation Plan (`verify.py`)

1. **Part 1: Macroscopic Permuton Concentration**:
   Verify empirical concentration of point counts in macroscopic boxes $B_{u, v}$ for $n = (1/4+\varepsilon)k^2$ and verify the quadratic rate $\exp(-\Omega(k^2))$.
2. **Part 2: Missing Pattern Cluster Size & Sieve Ratio**:
   Exhaustively enumerate all missing patterns $M(\sigma_n)$ for small $k$ ($k=4, 5$) over thousands of random hosts $\sigma_n$ at various intensities $C$. Measure the cluster size distribution, the conditional expectation $\mathbb{E}[M \mid M > 0]$, and the sieve ratio $R / k!$.
3. **Part 3: Low-Discrepancy vs. Poisson Hosts**:
   Compare pattern containment between deterministic low-discrepancy sets (Hammersley, Halton, Sobol) and uniform random permutations. Verify whether low-discrepancy hosts succeed or fail on monotone vs non-monotone targets.
4. **Part 4: Quasirandom Bulk Target Embedding**:
   Test containment of typical/generic bulk permutations vs structured permutations in regular hosts.
5. **Part 5: Master Synthesis**:
   Confirm that all 5 parts pass without error.
