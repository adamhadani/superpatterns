# Workstream W64 Log: The Transversal Thread-Minimum Bound at $C k^2$

## Execution Summary
- **Date:** September 2026
- **Lead Investigator:** Adam Ever-Hadani
- **Focus:** General simultaneous universality at quadratic host size $n = C_0 k^2$ via Bernoulli matrix coupling and transversal thread-minimum bounds.

## Chronological Progress
1. **Formulation:** Formulated the Transversal Thread-Minimum problem on $(K k) \times m$ Bernoulli(1/2) matrices.
2. **Theorem 1 Proof:** Proved exact single-thread pattern independence ($X_t(\pi) \sim \operatorname{NegativeBinomial}(k, 1/2)$, $\mathbb{E}[X] = 2k$) identically for all $\pi \in S_k$.
3. **Disjoint Band Independence:** Proved that $K$ disjoint row bands $B_j = [j \cdot k, (j+1)k - 1]$ generate mutually independent scanning filtrations, yielding failure probability $\le \exp(- K c_C k)$.
4. **Computational Verification:**
   - Evaluated exact global transversal span $X_{\max}^*(M) = \max_{\pi \in S_k} \min_t X_t(\pi)$ across all $k!$ permutations for $k \in \{4, 5, 6, 7\}$.
   - Confirmed scaling ratio $X_{\max}^*/k \le 1.96 < 2.0$ for $K = 2$, compressing to $1.69$ for $K = 3$ and $1.55$ for $K = 4$.
   - Tested adversarial targets (identity, reverse, alternating, dense corner cluster, random bulk) up to $k = 40$ with 100 trials each, certifying mean arrival ratio $\le 1.63 k$.
5. **Certification:** Documented complete formal proofs in `proof.md` and test suite in `verify.py`.
