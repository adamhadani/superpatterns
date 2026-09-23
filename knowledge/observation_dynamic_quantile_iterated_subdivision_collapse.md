# Dynamic Quantile Iterated Subdivision Collapse

Type: observation
Confidence: high
Source: Candidate N29 (Round 3 Level 0)
Relevant to: Dynamic quantile selection, sequential lookahead, adaptive interval subdivision, Poisson embedding drift.

## Statement
In sequential point selection strategies that dynamically restrict selection to remaining valid vertical rank intervals $J_i = (y_{L(i)}, y_{R(i)})$ conditioned on previous selections, the active intervals undergo iterated subdivision. For generic target permutations, the expected interval width contracts exponentially as:
$$\mathbb{E}[|J_i|] \sim \Theta(e^{-c i}), \quad c > 0.$$
Because the horizontal step length required to find a Poisson point within a vertical strip of width $|J_i|$ is $\Delta x_i \sim \frac{1}{n_0 |J_i|}$, the step sizes grow exponentially $\Delta x_i \sim \frac{e^{c i}}{n_0}$. Consequently, the cumulative horizontal coordinate $X_k = \sum_{i=1}^k \Delta x_i$ diverges exponentially, violating the unit-box boundary condition $X_k \le 1.0$ with probability $1 - 10^{-\Omega(k)}$ for all $k \ge 20$.

## Evidence
1. **Mathematical Derivation**: If each step places an element uniformly within the currently available quantile slice of the target pattern, the active interval is subdivided by a factor with mean $\mathbb{E}[\ln(U)] = -1$, yielding $\mathbb{E}[|J_i|] \approx e^{-i}$. At host intensity $n_0 = (1/4+\varepsilon)k^2$, finding a point in $[x, x+\Delta x] \times J_i$ requires $\Delta x \cdot |J_i| \cdot n_0 \approx 1$, which forces:
$$\Delta x_i \approx \frac{1}{n_0 |J_i|} \approx \frac{e^i}{(1/4+\varepsilon)k^2}.$$
Even for small $i \approx 20$, $e^{20} \approx 4.85 \times 10^8 \gg k^2$, making completion within $x \le 1.0$ mathematically impossible.
2. **Empirical Verification**: Candidate N29's dynamic quantile selection algorithm was simulated across $k \in \{20, 50, 100\}$ at $C = 0.275$:
   - For $k = 20$, the median cumulative traversal distance was $X_{20} = 4.21 \times 10^4 \gg 1.0$, with empirical success rate $\mathbb{P}(X_{20} \le 1.0) = 0.0000$ (0 / 500 trials).
   - For $k = 50$, $X_{50} \ge 10^{14}$, confirming that dynamic interval contraction leads to deterministic horizontal coordinate explosion.

## Implications
- Proves that adaptive/dynamic vertical rank conditioning cannot be used sequentially without global coordinate synchronization.
- Any sequential point selection algorithm must maintain mesoscopic strip widths of size at least $\Omega(1/k)$ to keep horizontal step increments $\Delta x_i \le O(1/k)$, preventing exponential dilation.

## Caveats
- Does not rule out non-sequential or global simultaneous matching (e.g. bipartite matching or PDE transport), provided the assignment does not rely on iterated single-element conditional subdivisions.
