# Workstream W67: The Missing-Pattern Autocorrelation Sieve & The $k^2$ Avoidance Bound

## Prime Directive
Maintain strict focus on the **sharp threshold value $C^* = 1/4 = 0.25000$** for Noga Alon's 1999 conjecture.
Audit and resolve the fundamental gap in W66 Theorem 7.1: namely, that on the generic bulk ($d \approx 2\sqrt{k}$), individual target failure probabilities of order $\exp(-\Theta(\varepsilon^2 k))$ cannot withstand a union bound over $k! \approx \exp(k \ln k)$ targets.

## Core Research Objectives

### 1. The Quadratic Avoidance Hypothesis vs Linear Renewal Fallacy
- Identify why W66 yielded $\exp(-\Theta(\varepsilon^2 k))$: because W66 analyzed a *single, 1D renewal path* along host streamlines.
- Contrast with the 2D planar Poisson host: the lower-tail Large Deviation Principle (LDP) for the longest increasing subsequence (Baik–Deift–Johansson / Deuschel–Zeitouni) operates with **speed $n = (1/4+\varepsilon)k^2$**, yielding:
  $$P_0(\operatorname{id}_k) \sim \exp\left( - \frac{4}{3} \varepsilon^3 k^2 \right) \ll \frac{1}{k!}.$$
- Determine whether $P_0(\pi) \le \exp(-\Omega(\varepsilon^3 k^2))$ holds for **all** target permutations $\pi \in S_k$, which would immediately allow a valid union bound over all $k!$ targets.

### 2. Autocorrelation Dominance & The Identity-Hardest Comparison
- For all $\pi \in S_k$, the expected count is invariant: $\mathbb{E}[\operatorname{occ}(\pi)] \equiv \binom{n}{k}/k!$.
- The self-overlap profile $\mathcal{O}_j(\pi) = \sum_{S, T} \mathbf{1}_{S \cong T \cong \pi}$ is **strictly maximized** by the monotone identity:
  $$\mathcal{O}_j(\pi) \le \mathcal{O}_j(\operatorname{id}_k) = \binom{k}{j}^2 \quad \forall j \in \{2, \dots, k-1\}.$$
- Because non-monotone patterns cluster strictly less, their occurrences are more evenly dispersed throughout the host, resulting in strictly smaller avoidance probabilities $P_0(\pi) \le P_0(\operatorname{id}_k)$.

### 3. Automated Empirical and Theoretical Verification
Implement `experiments/w67-quasirandom-regularity/verify.py`:
- Part 1: High-precision empirical measurement of $P_0(\pi)$ across candidate families ($\operatorname{id}_k$, $\operatorname{rev}_k$, alternating, Erdős–Szekeres, Cantor, and random bulk) across varying host sizes $n$.
- Part 2: Exact evaluation of the union bound sum $\mu(n, k) = \sum_{\pi \in S_k} P_0(\pi)$ vs exact simultaneous containment probability $\Pr(M = 0)$ for small $k$.
- Part 3: Overlap covariance computation and variance reduction audit across $S_k$.
- Part 4: Asymptotic tail analysis: Tracy–Widom $k^2$ rate vs $k!$ growth.
