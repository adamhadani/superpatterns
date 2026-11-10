# Workstream W65: Multi-Layer Hammersley Interleaving & Sharp Constant Verification at $C^* = 1/4$

## Prime Directive
Maintain strict focus on the **sharp threshold value $C^* = 1/4 = 0.25000$** for Noga Alon's 1999 conjecture.
Either:
1. Prove that every permutation $\pi \in S_k$ is simultaneously contained in a random permutation of length $n = \lceil(1/4+\varepsilon)k^2\rceil$ with probability $1 - o(1)$, OR
2. Explicitly identify and prove a genuine counterexample family $\pi_k \in S_k$ requiring $C > 1/4$, thereby refuting Alon's conjecture at $1/4$.

## Core Questions for W65

### 1. Empirical Threshold Audit of Candidate Extremal Families
Evaluate the empirical containment constant $C_{\min}(\pi)$ across candidate extremal families:
- **Monotone Identity:** $\operatorname{LIS} = k, \operatorname{LDS} = 1$ ($C_{\min} = 0.25000$).
- **Erdős–Szekeres Block-Reversal:** $\operatorname{LIS} = \sqrt{k}, \operatorname{LDS} = \sqrt{k}$.
- **Alternating Zig-Zag:** $\operatorname{LIS} \approx \sqrt{2k}, \operatorname{LDS} \approx \sqrt{2k}$.
- **Cantor / Fractal Permutations:** Self-similar non-monotone words.
- **Generic Random Bulk:** $\pi \sim \operatorname{Uniform}(S_k)$.

Does ANY candidate family exhibit an empirical threshold $C_{\min} > 0.25000$ as $k \to \infty$?

### 2. Multi-Layer Hammersley Hydrodynamics at $C = 1/4$
- Each host layer $\mathcal{L}_m$ contains $\sim 2\sqrt{C} k = k$ points at $C = 1/4$.
- Target chains $M_m$ require at most $\mu_m \le 2\sqrt{k}$ points.
- Available point surplus in each layer is $\ge \frac{1}{2}\sqrt{k} \to \infty$.
- Can the points of $M_m$ be selected from $\mathcal{L}_m$ such that inter-layer horizontal and vertical order relations are preserved?

### 3. Obstruction vs Universality Analysis
- If an obstruction exists: identify the exact geometric or topological bottleneck (e.g. crossing numbers, layer winding, or density deficit).
- If universality holds: formulate the continuous multi-layer coupling that proves simultaneous containment at $C = 1/4 + \varepsilon$.
