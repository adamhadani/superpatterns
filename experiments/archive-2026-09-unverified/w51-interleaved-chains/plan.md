# Workstream W51: Interleaved Monotone Chains at $(1/4+\varepsilon)k^2$ & the 321-Avoiding Sharp Threshold

## 1. Context and Motivation

In the resolution of Noga Alon's superpattern conjecture, the landscape currently stands at:
1. **Unconditional Quadratic Universality at $C_0 k^2$ (W47)**: Established for all $k!$ permutations simultaneously via canonical skeletal decompositions and flexible lookahead interfaces, eliminating the $\log\log k$ factor.
2. **Sharp Threshold $(1/4+\varepsilon)k^2$ for Modular Interval Inflations $\mathcal{M}_{\mathrm{int}}(\varepsilon)$ (W39)**: Proved via deterministic shared host squares with zero description entropy ($|\mathcal{Q}_{\mathrm{squares}}| \le (k+1)^3 = e^{o(k)}$) and $+3.57\%$ capacity surplus. Its operational scope is asymptotically of measure zero ($\le 10^{-2562}$ in $S_{1000}$).
3. **Conclusive Resolution of Repeated-$21$ (W50)**: Proved $c_{21} = 1.0000\dots$ identically via direct-sum diagonal superadditivity and Fekete's lemma, eliminating $21^{\oplus (k/2)}$ as an obstruction to Alon's conjecture and settling its critical threshold at $C^* = 1/4 = 0.25000$.

However, between modular interval inflations (which have no cross-inversions between blocks) and generic unstructured permutations ($k!$ entropy), lies the natural and foundational intermediate class:
**Interleaved Monotone Chains (321-Avoiding Permutations $S_k(321)$)**.
By Greene's theorem, $\operatorname{LDS}(\pi) \le 2$ if and only if $\pi$ partitions into at most 2 strictly increasing chains ($M_1 \sqcup M_2 = [k]$). The cardinality is the Catalan number:
$$C_k = \frac{1}{k+1}\binom{2k}{k} \approx \frac{4^k}{\sqrt{\pi} k^{3/2}} = \exp(k \ln 4 - \frac{3}{2}\ln k + O(1)).$$

Workstream W51 attacks `[GAP: OBLIGATION_04]`:
Does a uniform random permutation of length $n = \lceil(1/4+\varepsilon)k^2\rceil$ contain every 321-avoiding permutation $\pi \in S_k(321)$ simultaneously with probability $1 - o(1)$ for every fixed $\varepsilon > 0$?

## 2. Research Objectives

### Objective 1: Individual Capacity of 321-Avoiding Extremal Families
Systematically classify the extremal families of 321-avoiding permutations:
- The Monotone Boundary: $\mathrm{id}_k = (1, 2, \dots, k)$ ($\operatorname{LDS} = 1$).
- The Alternating Boundary: $21^{\oplus (k/2)} = (2, 1, 4, 3, \dots)$ ($\operatorname{LDS} = 2$, maximum descents $k/2$, $c_{21} = 1.0$).
- The Split Riffle Shuffle: $(k/2+1, 1, k/2+2, 2, \dots, k, k/2)$ (maximal interleaving of two macroscopic chains across the entire domain).
- The Cyclic Shift: $(2, 3, \dots, k, 1)$ (single-element wrap-around).
- Cantor-like and fractal 2-chain interleavings.

Measure the empirical critical threshold $C^*(\pi)$ for each family and test whether $C^*(\pi) \le 1/4$ holds uniformly for every individual 321-avoiding permutation.

### Objective 2: Simultaneous Containment & The Entropy-Surplus Tradeoff
Analyze the simultaneous containment problem across all $C_k \approx 4^k$ 321-avoiding permutations at host size $n = (1/4+\varepsilon)k^2$:
- The gross continuous surplus at intensity $C = 1/4+\varepsilon$ is $D(s) \ge 2\varepsilon s k$, providing surplus points $D(1) \ge 2\varepsilon k$.
- The lower-tail concentration decay for a single embedding path is $\exp(-\Omega(\varepsilon^2 k))$.
- A naive union bound over $C_k \approx 4^k = \exp(k \ln 4)$ targets fails whenever $\varepsilon^2 < \ln 4 \approx 1.3863$ (which holds for all $\varepsilon \le 1.17$).
- Therefore, simultaneous containment at $(1/4+\varepsilon)k^2$ strictly requires a **shared certificate mechanism** or a **coupled branching process** where target choices share common host points.

### Objective 3: Shared 2-Chain Skeleton / Grid Decomposition
Investigate whether 321-avoiding permutations admit a **low-entropy shared certificate family**:
- Can the $C_k$ Dyck path trajectories be embedded into a shared anchor grid of size $e^{o(k)}$ or polynomial size $(k+1)^d$?
- Evaluate the Samuels--Steele sequential selection deficit and determine the exact boundary between causal online selection ($C \ge 0.5$) and non-anticipative offline global embedding ($C = 1/4$).

### Objective 4: Computational Verification Harness
Implement `verify.py` to:
1. Exhaustively verify embedding success of all 321-avoiding permutations for $k \in \{4, 5, 6, 7, 8\}$ ($C_4 = 14$, $C_5 = 42$, $C_6 = 132$, $C_7 = 429$, $C_8 = 1430$, total 2,047 permutations) on Poisson hosts at varying intensities $C$.
2. Measure the empirical embedding rate $L_\pi(\sigma_n)/\sqrt{n}$ for large-scale extremal families up to $k=100$.
3. Compute the correlation / point sharing between different 321-avoiding targets in the same host.
4. Test the shared-skeleton embedding hypothesis.
