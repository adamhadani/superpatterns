# Infinitesimal LIS Capacity Integration Violates Point Conservation

Type: observation
Confidence: high
Source: Candidates 0, 1, 3, 4, 7 (Level 0 falsers); Aggregators strategy_L01_N04, strategy_L01_N05, strategy_L01_N08 (Round 2 Level 1)
Relevant to: Hydrodynamic limits, Poisson directed paths, traversal velocity models.

## Statement
Integrating the asymptotic LIS traversal formula $dN(s) = 2\sqrt{d\mu}$ across infinitesimal boxes of area $dA = (ds)^2$ violates point conservation $\operatorname{LIS}(S) \le |S|$. In a diagonal corridor of $k$ boxes of size $(1/k) \times (1/k)$ at Poisson intensity $n_0 = (1/4+\varepsilon/2)k^2$, the total expected number of host points is $(1/4+\varepsilon/2)k \approx 0.27 k$, yet the integral $\int 2\sqrt{d\mu} = \sqrt{1+2\varepsilon} k \approx 1.05 k$ predicts an LIS capacity nearly $4\times$ larger than the total points present.

## Evidence
1. Point conservation identity: For any point configuration $S \subset [0, 1]^2$, the length of any increasing subsequence is bounded by the total number of points: $\operatorname{LIS}(S) \le |S|$.
2. Direct calculation: In $k$ diagonal boxes of dimensions $1/k \times 1/k$, total expected Poisson points is $\sum_{i=1}^k \mathbb{E}[|\Pi_{n_0} \cap B_i|] = k \cdot (n_0 / k^2) = (1/4+\varepsilon/2)k$. For $\varepsilon = 0.05$, this is $0.275 k$.
3. The claimed hydrodynamic rate $2\sqrt{d\mu} = \sqrt{1+2\varepsilon} k = 1.049 k$ exceeds the total number of points by $1.049 / 0.275 = 3.81\times$.
4. Multi-Chain Point Conservation Violation (Round 2 Level 1 Aggregators L01_N04, L01_N05, L01_N08): Decomposing $\pi$ into $d = 2\sqrt{k}$ Dilworth chains and claiming each chain independently achieves LIS velocity $2\sqrt{C} > 1$ requires $d \cdot \sqrt{k} \cdot 2\sqrt{C} = 4\sqrt{C} k$ points from the Poisson point process (or $O(k^{3/2})$ points across parallel corridors), whereas total Poisson intensity on $[0, 1]^2$ is only $(1/4+\varepsilon)k^2$ points, of which each of the $d$ diagonal corridors receives at most $(1/4+\varepsilon)k / d$ points. Simultaneously running $d$ chains at full LIS velocity violates global point conservation $\sum_{i=1}^d \operatorname{LIS}(C_i) \le |\Pi| = O(k)$.

## Implications
The Logan--Shepp / Vershik--Kerov limit $\operatorname{LIS} \sim 2\sqrt{\mu}$ is strictly an asymptotic macroscopic phenomenon as $\mu \to \infty$. It cannot be applied infinitesimally or locally to small boxes where $\mu \to 0$, because as $\mu \to 0$, $2\sqrt{\mu} / \mu = 2/\sqrt{\mu} \to \infty$. Traversal through narrow corridors requires large host intensity or macroscopic corridor widths.

## Caveats
Macroscopic boxes with $\mu = \Omega(k)$ or $\mu \to \infty$ do achieve the $2\sqrt{\mu}$ asymptotic limit; the breakdown occurs when subdividing into microscopic cells.
