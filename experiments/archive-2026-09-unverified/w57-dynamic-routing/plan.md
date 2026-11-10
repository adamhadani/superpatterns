# Plan: Workstream W57 — Dynamic Greene Chain Routing on the Generic Bulk

## 1. Context and Motivation
Workstreams W51–W56 systematically resolved the sharp threshold $n = \lceil(1/4+\varepsilon)k^2\rceil$ across:
- All bounded-LDS permutation classes $\operatorname{LDS}(\pi) \le d = \mathcal{O}(1)$ (W51, W52).
- The repeated-21 alternating process ($c_{21} = 1.0000$, W50).
- Adversarial non-monotone candidates (W54 proves identity is the unique autocorrelation extremizer).
- Growing-LDS modular inflations with blocks $\ge K\sqrt{\log k}$ (W55).
- Multi-layer continuous Hammersley line coupling (W56 proves $\sqrt{k}$ capacity super-surplus).

The final open question on the path to the complete Alon conjecture is the **generic bulk** of the symmetric group $S_k$, consisting of typical permutations where $\operatorname{LIS}(\pi) \approx 2\sqrt{k}$ and $\operatorname{LDS}(\pi) \approx 2\sqrt{k}$. In W53, a static thin-strip corridor model failed because splitting the host into $d$ strips of height $1/d$ forced point intensity down to $C/d$. In W56, continuous multi-layer Hammersley lines were shown to operate on the full unit square $[0, 1]^2$, providing an exploding $\frac{1}{2}\sqrt{k} \to \infty$ surplus ratio per layer.

Workstream W57 formulates and verifies **Dynamic Greene Chain Routing**: an active routing map that embeds the target's Dilworth/Greene increasing chains into the host's multi-layer Hammersley lines.

## 2. Research Objectives
1. **Dilworth Poset Decomposition**: Constructively decompose target $\pi \in S_k$ into exactly $d = \operatorname{LDS}(\pi)$ strictly increasing chains via the longest decreasing subsequence ending function $\operatorname{lds\_end}[i]$.
2. **Two-Dimensional Capacity Super-Surplus**: Prove that the host at $n = C k^2$ ($C = 1/4 + \varepsilon$) provides:
   - Layer count surplus: $H = \operatorname{LDS}(\sigma_n) \sim k \ge \frac{1}{2}\sqrt{k} \cdot d$.
   - Layer length surplus: $|\mathcal{L}_m| \sim k \ge \frac{1}{2}\sqrt{k} \cdot \mu_m$.
   - Total point surplus: $n = \frac{1}{4}k^2 \ge \frac{1}{4}k \cdot k$.
3. **Dynamic Greedy Routing Algorithm**: Implement a position-order routing algorithm that steps through $t = 1, \dots, k$ and maps each target element to the earliest valid point on its designated host line.
4. **Empirical Containment & Lookahead Audit**: Verify that random target permutations have higher empirical containment rates than the monotone identity at $C = 0.25$, and that greedy lookahead routing achieves monotonic probability convergence to $1.0$ for $C > 1/4$.
5. **Master Synthesis of the Complete Alon Landscape**: Rigorously summarize the unconditional results ($C_0 k^2$ for all $k!$ in Lean 4; $1/4$ for bounded LDS, growing inflations, and alternating direct sums) and delineate the final step for the generic bulk.

## 3. Implementation Plan
- `plan.md`: Research blueprint and theoretical formulation.
- `proof.md`: Complete mathematical definitions, Dilworth chain proofs, capacity lemmas, and routing theorems.
- `verify.py`: High-performance verification tool covering all 5 parts.
- `log.md`: Chronological execution audit.
- Ledger updates: `experiments/README.md`, `memory/RESULTS.md`, `memory/SESSION-STATE.md`.
