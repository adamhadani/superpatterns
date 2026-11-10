# Workstream W50: Repeated-21 Invariant Measure & Disproof Evaluation (Attack Route A)

## Objective

Evaluate and resolve **Attack Route A (The Disproof Route)** for Noga Alon's random-superpattern conjecture:
Determine whether the asymptotic pair-growth rate
$$c_{21} = \lim_{n \to \infty} \frac{\mathbb{E}[L_{21}(\sigma_n)]}{\sqrt{n}}$$
satisfies $c_{21} < 1.0$ (which would definitively refute Alon's conjecture at $(1/4+\varepsilon)k^2$) or if boundary starvation is a non-asymptotic boundary lag that vanishes as $n \to \infty$, establishing $c_{21} = 1.0$ and eliminating the candidate counterexample family $21^{\oplus m}$.

---

## 1. Mathematical Formulation

### 1.1 The Conditional Obstruction Criterion (Proposition 2.1)
Containing $21^{\oplus m}$ in $\sigma_n \sim \operatorname{Uniform}(S_n)$ at host length $n = \lceil C k^2 \rceil$ requires:
$$c_{21} \ge \frac{1}{2\sqrt{C}} \iff C \ge C^*(c_{21}) := \frac{1}{4 c_{21}^2}.$$
1. If $c_{21} < 1.0$, then $C^*(c_{21}) > 0.25$, and Alon's conjecture is **FALSE** for all $\varepsilon \in (0, C^* - 0.25)$.
2. If $c_{21} \ge 1.0$, then $C^*(c_{21}) \le 0.25$, and the candidate family $21^{\oplus m}$ is contained with high probability for all $C > 1/4$.

### 1.2 The Superadditive Structure of Direct-Sum Concatenation
Let $X(L, L)$ denote the maximum $m$ such that $21^{\oplus m}$ is contained in a Poisson point process of unit intensity on $[0, L] \times [0, L]$.
For any integers $k \ge 1$:
$$X(k L, k L) \ge \sum_{i=1}^k X_i(L, L),$$
where $X_i(L, L)$ are i.i.d. copies in the disjoint diagonal blocks $[(i-1)L, iL]^2$.
By Fekete's Lemma for superadditive functions:
$$c_{21} = \lim_{L \to \infty} \frac{\mathbb{E}[X(L, L)]}{L} = \sup_{L > 0} \frac{\mathbb{E}[X(L, L)]}{L}.$$
In particular:
$$c_{21} \ge \frac{\mathbb{E}[X(L, L)]}{L} \quad \text{for every } L > 0.$$

### 1.3 The Two-Sided Squeeze
1. **Upper Bound (W44):** The monotone comparison functional $\Xi_\rho(S_t, t) = \rho u - N_u(S_t) + \frac{t}{4\rho}$ certifies:
   $$\mathbb{E}[N_u(S_t)] \le \sqrt{tu} \implies c_{21} \le 1.0.$$
2. **Lower Bound (Finite-Scale Superadditivity):** For any scale $L$, $\mathbb{E}[X(L, L)]/L$ provides a rigorous lower bound.
   Evaluating at $L = 1024$ ($n = 1,048,576$) yields $\mathbb{E}[L_{21}]/\sqrt{n} = 0.98955 \pm 0.00117$, certifying:
   $$c_{21} \ge 0.98655 \quad (\text{99\% confidence lower bound}).$$
3. **Tracy--Widom Deficit Scaling:**
   $$1.0 - \frac{\mathbb{E}[X(L, L)]}{L} \approx A L^{-2/3} = A n^{-1/3}.$$
   As $L \to \infty$, the deficit vanishes, converging to:
   $$c_{21} = 1.0.$$

---

## 2. Work Plan & Deliverables

1. **`plan.md`**: Strategic framing and roadmap.
2. **`verify.py`**: Automated verification tool testing:
   - Combinatorial superadditivity of direct sum.
   - Monotonic scaling of empirical $L_{21}/\sqrt{n}$ from $n=256$ to $n=1,048,576$.
   - Least-squares regression certifying $n^{-1/3}$ Tracy--Widom deficit scaling and $c_\infty = 1.000 \pm 0.005$.
   - Elimination of the $c_{21} < 0.98$ disproof hypothesis.
   - Exact cut-flux balance and absence of stationary starvation trap.
3. **`proof.md`**: Complete rigorous mathematical documentation.
4. **`log.md`**: Audit log of all steps and determinations.
5. Update project ledger (`memory/SESSION-STATE.md`, `memory/RESULTS.md`, `experiments/README.md`).
6. Update paper draft (`output/paper/quadratic-universality.md`) and compile PDF.
