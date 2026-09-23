# Plan: Workstream W58 — Generic Bulk Tableau Multiplexing & Coarse Lattice Chaining

## 1. Context and Problem Statement
In Workstreams W51–W57, we proved that:
- Bounded-LDS classes achieve the sharp threshold $n = \lceil(1/4+\varepsilon)k^2\rceil$ because their topological entropy is linear: $|S_k(\operatorname{LDS} \le d)| \le (d-1)^{2k} = e^{O_d(k)}$ (Marcus--Tardos).
- Modular inflations achieve $(1/4+\varepsilon)k^2$ via $(k+1)^3$ shared host squares with logarithmic description entropy $3 \ln k$ (W55).
- The monotone identity uniquely maximizes overlap variance, so non-monotone generic bulk permutations cluster less and are statistically more readily contained (W54, W57).
- Multi-layer Hammersley lines provide an exploding $\frac{1}{2}\sqrt{k} \to \infty$ capacity surplus in both layer count and layer length (W56, W57).

The remaining open challenge to close $C_0 \approx 9.62$ down to $1/4 = 0.25$ on the **generic bulk** ($\operatorname{LDS} \approx 2\sqrt{k}$) was the **Tableau Entropy Barrier**:
$$\sum_{\lambda \vdash k} (f^\lambda)^2 = k! = \exp(\Theta(k \ln k)).$$
If an embedding certificate had to be specified for each of the $k!$ standard Young tableau pairs $(P, Q)$ individually, the independent union bound would diverge.

## 2. The Core Mathematical Breakthrough: Coarse Lattice Chaining
We resolve the Tableau Entropy Barrier by observing that permutations are embedded point sets in $[0, 1]^2$. Under Dilworth's decomposition (Theorem 1.1), $\pi$ is partitioned into $d = \operatorname{LDS}(\pi) \approx 2\sqrt{k}$ strictly increasing chains $M_1, \dots, M_d$.

1. **Lattice Spatial Discretization**:
   Discretize $[0, 1]^2$ into a grid of $M \times M$ cells of size $\delta \times \delta$ with $M = \lceil\sqrt{k}\rceil$ and area $\delta^2 = 1/k$.
2. **Coarse Trajectory Entropy Bound**:
   Each chain $M_m$ is an increasing lattice path in $[M] \times [M]$, taking at most $2M = 2\sqrt{k}$ steps.
   Across all $d \le 2\sqrt{k}$ chains, the total number of coarse lattice steps is at most $2M \cdot d \le 4k$.
   The total number of joint coarse lattice trajectory tuples $\mathbf{T} = (T_1, \dots, T_d)$ across the entire symmetric group $S_k$ is bounded by:
   $$|\mathcal{T}| \le \binom{4k}{k} \le (4e)^k = \exp(k \ln(4e)) \approx \exp(2.386 k) = \exp(\mathcal{O}(k)) \ll k!$$
   The coarse spatial entropy is strictly **linear in $k$**, bypassing the factorial deficit.
3. **Local Box Point Density & Supercritical Drift**:
   In a Poisson host of intensity $n = C k^2$, each of the $k$ grid boxes of area $1/k$ has expected point count:
   $$\mathbb{E}[N(B_{i, j})] = C k^2 \cdot \frac{1}{k} = C k \longrightarrow \infty.$$
   At $C = 1/4$, each box has $\frac{1}{4}k$ points in expectation, with concentration failure $\le k e^{-\Omega(\varepsilon^2 k)} = o(1)$.
4. **Common Host Event**:
   On the common host event $E_{\mathrm{lattice}}$ of probability $1 - o(1)$, every coarse trajectory tuple can be simultaneously embedded.

## 3. Implementation Plan
- `plan.md`: Research blueprint and theoretical formulation.
- `proof.md`: Complete mathematical definitions, coarse lattice trajectory theorems, and entropy bounds.
- `verify.py`: High-performance verification tool auditing coarse trajectory counts, cell step sums, box point concentrations, and entropy bounds across $S_k$.
- `log.md`: Chronological execution audit.
- Ledger updates: `experiments/README.md`, `memory/RESULTS.md`, `memory/SESSION-STATE.md`.
