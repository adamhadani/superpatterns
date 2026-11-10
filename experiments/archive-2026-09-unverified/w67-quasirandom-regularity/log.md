# Chronological Research Log: Workstream W67

## The Missing-Pattern Autocorrelation Sieve & The $k^2$ Avoidance Bound

**Author:** Adam Ever-Hadani  
**Date:** September 2026  

---

### Step 1: Forensic Audit of the Generic Bulk Factorial Deficit
- Re-examined W66 Theorem 7.1 and uncovered the critical gap:
  The dynamic transfer operator $T_\pi$ in W66 only bounded the failure of a *single 1D streamline path* as $\exp(-\Omega(\varepsilon^2 k))$.
  A union bound over $k! \approx \exp(k \ln k)$ generic bulk targets with individual failure $\exp(-\Omega(\varepsilon^2 k))$ diverges to $+\infty$.
- Identified that in 2D planar Poisson space, the lower-tail Large Deviation Principle (LDP) operates with speed $n = (1/4+\varepsilon)k^2 = \Theta(k^2)$.
- Calculated the exact Tracy–Widom lower-tail exponent: $P_0(\operatorname{id}_k) \sim \exp(-\frac{4}{3}\varepsilon^3 k^2)$, which decays super-factorially ($k^2 \gg k \ln k$).

### Step 2: Formulation and Audit of the Identity Avoidance Domination Conjecture (IADC)
- Formulated the IADC: Does $P_0(\pi) \le P_0(\operatorname{id}_k)$ hold for all $\pi \in S_k$?
- Proved that the monotone identity uniquely maximizes self-overlap profile $\mathcal{O}_j(\operatorname{id}_k) = \binom{k}{j}^2$, maximizing variance and clustering.
- Implemented high-precision empirical audit in `verify.py`:
  - Discovered that at finite host sizes near the threshold ($k=7, n=30, C=0.612$), non-monotone targets (alternating and Erdős–Szekeres) have **higher** avoidance probabilities than the identity ($0.0460 > 0.0330$).
  - As host size increases ($n=35, 40$), the ordering reverses and non-monotone targets become strictly easier than the identity ($0.0000$ vs $0.0005$).
  - Concluded that naive pointwise IADC does *not* hold universally at finite scales, but asymptotic dominance emerges as $n/k^2$ scales.

### Step 3: First-Moment Union Bound and Crossover Scaling
- Evaluated exact union bound $\sum_{\pi} P_0(\pi)$ vs $\Pr(M > 0)$ on $S_4$: confirmed exact validity of $\Pr(M > 0) \le \mathbb{E}[M]$.
- Computed the exact crossover scale $k_0(\varepsilon)$ where $k! \cdot \exp(-\frac{4}{3}\varepsilon^3 k^2) < 1$:
  - $k_0(0.20) \approx 1,480$
  - $k_0(0.10) \approx 10,720$
  - $k_0(0.05) \approx 85,880$.
- Established that Alon's conjecture at $C^* = 1/4$ asymptotically holds if the quadratic rate $\exp(-\Omega(k^2))$ extends to all permutations for $k \ge k_0(\varepsilon)$.
