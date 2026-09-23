# Optimal Transport Cyclic Monotonicity Descent Barrier

Type: observation
Confidence: medium
Source: explorer_r3_L00_N05 (Round 3 Level 0)
Relevant to: Proof strategies attempting to construct permutation embeddings via Monge-Kantorovich optimal transport or gradient push-forward maps $T = \nabla \phi$.

## Statement
The quadratic Wasserstein optimal transport map $T: \mathbb{R}^d \to \mathbb{R}^d$ push-forwarding continuous density is uniquely given (by Brenier's Theorem) as the gradient of a convex potential $T = \nabla \phi$. Consequently, $T$ is cyclically monotone: for all points $x, y$, $\langle T(x) - T(y), x - y \rangle \ge 0$. In one dimension (and coordinate projections), this forces $T$ to be strictly non-decreasing, making it mathematically impossible for quadratic optimal transport to map an increasing coordinate sequence to a sequence containing coordinate descents.

## Evidence
In `explorer_r3_L00_N05`, the candidate attempted to construct host permutations via optimal transport coupling. Falser verification showed that the resulting transport map preserves coordinate orientation monotonically, yielding 0 descents ($x_i < x_j \implies T(x_i) < T(x_j)$). Generic permutations in $S_k$ have $\approx k/2$ descents, and alternating permutations have $k-1$ descents, which strictly contradicts cyclical monotonicity.

## Implications
Optimal transport with convex potentials cannot generate or match permutation descents. Strategies invoking Monge-Kantorovich transport to embed generic or alternating patterns must introduce discontinuous or non-monotone re-orderings, which destroys the regularity and energy bounds of the transport map.

## Caveats
Non-quadratic transport costs or non-optimal couplings can produce non-monotone permutations, but they forfeit Brenier's theorem and convex potential regularity, requiring explicit combinatorial control of crossings.
