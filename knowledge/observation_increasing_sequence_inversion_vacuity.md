# Inversion Vacuity on Increasing Sequences and Alternating Capacity Disproof

Type: observation
Confidence: high
Source: Candidates N16, N17, N19, N20, N22 (Round 3 Level 0)
Relevant to: Workstream W44, alternating pattern embeddings ($21^{\oplus m}$), hydrodynamic LIS limits, pair growth rate $c_{21}$.

## Statement
In any strictly increasing sequence $x_1 < x_2 < \dots < x_m$ and $y_1 < y_2 < \dots < y_m$ (such as an optimal LIS path in a Poisson point process or random permutation), the number of consecutive descents/inversions ($y_i > y_{i+1}$) is **identically zero**. Consequently, attempts to derive the alternating pair growth rate $c_{21} = 1.0$ by asserting that consecutive steps along an optimal LIS trajectory form descents with probability $1/2$ (or that $\mathbb{E}[L_{21}] = \frac{1}{2}\mathbb{E}[\operatorname{LIS}]$) are mathematically vacuous.

Furthermore, the alternating capacity bound $2 L_{21}(\sigma) \le \operatorname{LIS}(\sigma)$ is mathematically false for general permutations: there exist finite permutations where the alternating pair length exceeds half the LIS.

## Evidence
1. **Identically Zero Inversions on LIS Paths**:
   By definition of an increasing subsequence, every pair $(i, j)$ with $i < j$ satisfies $\pi(i) < \pi(j)$. There are zero inversions $(y_i > y_j)$ among elements selected by any increasing path. Postulating that 21-pairs can be sampled from an LIS at rate $1/2$ per step conflates an unconditioned random walk with a conditioned monotonically increasing path.
2. **Counterexample to $2 L_{21} \le \operatorname{LIS}$**:
   At $n=10$, consider the permutation:
   $$\sigma = [7, 8, 4, 6, 5, 2, 1, 10, 9, 3].$$
   - The alternating pattern $21^{\oplus 2}$ (length 4) can be embedded as $(7, 4)$ and $(10, 3)$ or $(6, 5)$ and $(10, 9)$, giving $L_{21}(\sigma) = 2$ ($2 L_{21} = 4$).
   - The longest increasing subsequence of $\sigma$ has length $\operatorname{LIS}(\sigma) = 3$ (e.g. $[4, 6, 10]$ or $[4, 5, 10]$ or $[7, 8, 10]$).
   - Thus, $2 L_{21}(\sigma) = 4 > 3 = \operatorname{LIS}(\sigma)$, directly disproving the inequality $2m \le \operatorname{LIS}$.
3. **Non-Monotonicity of Empirical DP Ratio**:
   Exact dynamic programming on random permutations shows that the ratio $\mathbb{E}[L_{21}(n)] / \sqrt{n}$ does not converge monotonically from above to 1.0. Empirical evaluations show non-monotonic fluctuations (e.g. $0.915$ at $n=64$ vs $0.9187$ at $n=36$) and persistent asymptotic stabilization near $c_{21} \approx 0.84 - 0.941 < 1.0$.

## Implications
The pair-growth rate $c_{21}$ cannot be inherited, derived, or halved from Baik-Deift-Johansson (1999) or Vershik-Kerov / Logan-Shepp theorems for LIS. Monotone paths and alternating paths have fundamentally opposing sign structures: increasing paths enforce strictly positive velocity $\dot{y} > 0$, while $21^{\oplus m}$ enforces microscopic downward jumps $\Delta y < 0$ interleaved with macroscopic upward steps.

## Caveats
The empirical shortfall $c_{21} < 1.0$ remains an active numerical barrier for $n \le 4096$, though an asymptotic convergence $c_{21} \to 1.0$ with slow Tracy-Widom lag cannot be ruled out purely by finite computations.
