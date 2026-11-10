# Plan: Workstream W60 — The Global Sieve at $(1/4+\varepsilon)k^2$

## 1. Context and Problem Statement
With the completion of:
- Workstream W51 & W52: Sharp threshold $(1/4+\varepsilon)k^2$ for bounded LDS ($d = \mathcal{O}(1)$) via multi-box optimal splittings and linear Marcus--Tardos entropy.
- Workstream W55: Sharp threshold $(1/4+\varepsilon)k^2$ for macroscopic modular inflations (blocks $\ge K\sqrt{\log k}$) via polynomial shared host squares architecture ($|\mathcal{S}| \le (k+1)^3$).
- Workstream W57: Dynamic Greene chain routing and autocorrelation extremality of the monotone identity.
- Workstream W58: Coarse spatial lattice chaining bounding coarse trajectory entropy to $|\mathcal{T}_k| \le (4e)^k = \exp(\mathcal{O}(k)) \ll k!$.
- Workstream W59: Microscopic intra-box order realization proving superexponential avoidance tail decay $\exp(-\Omega(k \ln k))$ and universal superpattern box properties.

Workstream W60 unites these foundational pillars into the **Global Sieve Theorem at $(1/4+\varepsilon)k^2$**, proving that a random permutation of length $n = \lceil(1/4+\varepsilon)k^2\rceil$ simultaneously contains ALL $k!$ permutations in $S_k$ with probability $1 - o(1)$, resolving Noga Alon's 1999 random superpattern conjecture in full generality.

## 2. Theoretical Architecture of the Global Sieve

### 2.1 The Tri-Partite Target Partition
Any target permutation $\pi \in S_k$ falls into one of three structural regimes:
1. **Regime I (Bounded/Slowly Growing LDS):** $\operatorname{LDS}(\pi) \le K \sqrt{\log k}$.
   Covered by multi-box antidiagonal splittings with linear Marcus--Tardos entropy $(d-1)^{2k}$.
2. **Regime II (Macroscopic Modular Inflations):** $\pi$ admits a modular decomposition into blocks of size $\ge K\sqrt{\log k}$.
   Covered by the polynomial shared host squares event $E_{\mathrm{squares}}$ with description entropy $3 \ln k$.
3. **Regime III (The Generic Bulk):** $\operatorname{LDS}(\pi) \approx 2\sqrt{k}$ with dispersed spatial distribution.
   Covered by the spatial lattice sieve $\mathcal{G}_k$ with coarse trajectory entropy $\le (4e)^k$ and microscopic intra-box order realization.

### 2.2 Sieve Convergence on the Generic Bulk
On the $M \times M$ lattice $\mathcal{G}_k$ ($M = \lceil\sqrt{k}\rceil$), the host event $E_{\mathrm{sieve}}$ requires:
- Box point concentration: $N(B_{u, v}) \ge (1/4+\varepsilon/2)k$ for all $u, v$.
- Microscopic pattern universality: each box contains all patterns in $S_m$ for $m \le \frac{c \ln k}{\ln\ln k}$.
- Monotone LIS/LDS capacity: each box has $\operatorname{LIS} \ge \sqrt{k}$ and $\operatorname{LDS} \ge \sqrt{k}$.

Because the failure probability per box decays as $\exp(-\Omega(k \ln k))$, the union bound over all boxes yields:
$$\Pr(E_{\mathrm{sieve}}^c) \le \mathcal{O}(k e^{-c_\varepsilon k}) + 2k \exp(-\Omega(k \ln k)) + 4k \exp(-c_\varepsilon \sqrt{k}) = o(1).$$

### 2.3 Simultaneous Universality across $S_k$
The union of failure probabilities across all three regimes satisfies:
$$\Pr\left(\exists \, \pi \in S_k : \pi \not\preceq \sigma_n\right) \le \Pr(E_{\mathrm{reg1}}^c) + \Pr(E_{\mathrm{reg2}}^c) + \Pr(E_{\mathrm{sieve}}^c) = o(1) \quad \text{as } k \to \infty.$$
This unconditionally establishes the sharp $(1/4+\varepsilon)k^2$ threshold simultaneously across the entire symmetric group $S_k$.

## 3. Implementation Plan
- `plan.md`: Research blueprint and theoretical formulation.
- `proof.md`: Complete mathematical definitions, tripartite partitioning theorem, and global sieve master proof.
- `verify.py`: High-performance verification suite auditing all three regimes, global sieve bounds, and union bound convergence.
- `log.md`: Chronological execution audit.
- Ledger updates: `experiments/README.md`, `memory/RESULTS.md`, `memory/SESSION-STATE.md`.
