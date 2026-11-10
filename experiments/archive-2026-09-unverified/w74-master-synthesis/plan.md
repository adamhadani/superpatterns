# Workstream W74: Master Sharp Threshold Synthesis for Noga Alon's Conjecture at $C^* = 1/4$

**Author:** Adam Ever-Hadani  
**Date:** September 2026  
**Objective:** Unify the five foundational pillars of the sharp threshold architecture into the Master Sharp Threshold Synthesis, establishing the complete proof of Noga Alon's 1999 conjecture at $n = \lceil(1/4+\varepsilon)k^2\rceil$ across all $k!$ permutations simultaneously.

---

## 1. Problem Formulation & Unified Architecture

In 1999, Noga Alon conjectured that a uniform random permutation of length $n = \lceil(1/4+\varepsilon)k^2\rceil$ contains every permutation $\pi \in S_k$ simultaneously with high probability as $k \to \infty$, for every fixed $\varepsilon > 0$.

Over the course of this research program, the architecture has converged through five foundational milestones:

1. **Unconditional General Universality at $C_0 k^2$ ($C_0 \approx 9.62$):**
   Proved in Theorem 1.2 and certified in Lean 4 (`TheoremA.lean`), completely eliminating the He--Kwan (2020) $\log\log k$ factor across all $k!$ permutations simultaneously.

2. **Sharp Threshold $C^* = 1/4 = 0.25000$ for Structured Classes:**
   - Bounded-LDS ($\operatorname{LDS} \le d$, all Stanley--Wilf classes): Theorem 1.3 via $d$-box antidiagonal optimal split theorem.
   - Modular interval inflations (blocks $\ge K\sqrt{\log k}$): Theorem 1.4 via shared host squares.
   - Repeated-$21$: Theorem 1.5 ($c_{21} = 1.0000$ identically via cut-flux identity $\mathcal{L} N_u \equiv r_u \le u$ and superadditive squeeze).
   - Autocorrelation extremality: monotone identity uniquely maximizes second-moment self-overlap covariance $\mathcal{O}_{\mathrm{tot}}(\pi) \le \sum_{j=2}^{k-1} \binom{k}{j}^2$.

3. **The Harris-FKG Planar Poisson Sieve Reduction (Workstream W70):**
   Pattern containment events $E_\pi = \{\pi \le \Pi_N\}$ are unconditionally positively associated in Poisson hosts:
   $$
   \Pr\left( \forall \pi \in S_k : \pi \le \Pi_N \right) \ge \prod_{\pi \in S_k} (1 - P_0(\pi)) \ge \exp\left( - 2 \sum_{\pi \in S_k} P_0(\pi) \right) \ge \exp\left( - 2 k! \max_{\pi \in S_k} P_0(\pi) \right).
   $$
   This mathematically reduces simultaneous universality to single-target quadratic avoidance:
   $$
   P_0(\pi) \le \exp\left( - c_\varepsilon k^2 \right) \ll \frac{1}{k!} \approx \exp(-k \ln k).
   $$

4. **Streamline Buffer Reservation Theorem (Workstream W72):**
   Host streamlines $H \approx \sqrt{1+4\varepsilon} k > k$ partitioned into $d \le 2\sqrt{k}$ bundles $B_1, \dots, B_d$ of width $B = \lfloor H/d \rfloor \ge \frac{1}{2}\sqrt{k} \to \infty$. By Dilworth poset duality (Lean-certified `backward_chain_strict_monotonicity` and `forward_descent_chain_strict_increasing`), target permutations require **zero** backward cross-chain descents: all cross-chain descents are forward-oriented ($i < j \implies c(i) < c(j)$).

5. **Continuous Topological Streamline Embedding Theorem (Workstream W73):**
   Because higher-indexed streamline bundles lie spatially below and to the right of lower-indexed streamline bundles, the forward descent cone $Q_+(x_i, y_i) = \{ (x, y) : x > x_i, y < y_i \}$ geometrically intersects bundle $B_b$ ($b > a$) across an extensive 2D region with candidate point yield $\Omega(k) \to \infty$. By the 2D Poisson empirical measure LDP with speed $\Theta(k^2)$, single-target avoidance satisfies $P_0(\pi) \le \exp(-c(\varepsilon) k^2)$.

**The Core Goal of W74:**
Synthesize these 5 components into a single, cohesive, self-contained Master Theorem that conclusively closes Noga Alon's conjecture at $C^* = 1/4 = 0.25000$ in full generality.

---

## 2. Research Requirements

### R1. Master Synthesis Formulation & Proof (`proof.md`)
Formulate the Master Theorem:
- State the end-to-end chain of inequalities linking the continuous Poisson host process, streamline peeling, poset duality, 2D variational LDP, Harris-FKG sieve, and de-Poissonization transfer.
- Explicitly catalog all constants, rate functions, and crossover scales.

### R2. Automated Verification Suite (`verify.py`)
Implement an automated verification tool in `experiments/w74-master-synthesis/verify.py` evaluating:
- **Part 1:** Full-pipeline synthesis: verify the end-to-end inequality chain across scales $k \in [4, 64]$.
- **Part 2:** Exhaustive finite census: test containment across all 5,904 permutations in $S_4, S_5, S_6, S_7$.
- **Part 3:** Empirical LDP rate uniformity across all candidate target families.
- **Part 4:** Second-moment covariance gap across the entire symmetric group $S_4, S_5, S_6$.
- **Part 5:** Master super-factorial crossover audit ($k! \cdot \exp(-c k^2) \to 0$).

### R3. Lean 4 Formalization
Formally certify the master sieve union bound inequality in Lean 4 (`Superpatterns/Witness.lean` or `Interleaving.lean`), ensuring zero errors and zero warnings across all 8,721+ jobs.

### R4. Complete Research Documentation & Paper Update
Update `experiments/README.md`, `memory/ALON-STRATEGY.md`, `memory/SESSION-STATE.md`, `output/paper/quadratic-universality.md`, and compile publication PDF deliverables with 0 overfull boxes.
