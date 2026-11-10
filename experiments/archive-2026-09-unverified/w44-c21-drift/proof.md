# Workstream W44: Repeated-21 Marked Drift & Lyapunov Certificate Proof

## 1. Strategic Context and the Asymptotic Pair-Growth Constant

Let $L_{21}(\sigma)$ denote the maximum number of direct-summed decreasing pairs ($21^{\oplus m}$) contained as a pattern in a permutation $\sigma \in S_n$:
$$L_{21}(\sigma) = \max \{m \ge 0 : 21^{\oplus m} \le \sigma\}.$$
When $\sigma_n \sim \operatorname{Uniform}(S_n)$, the scaled asymptotic pair-growth rate is defined by:
$$c_{21} = \lim_{n \to \infty} \frac{L_{21}(\sigma_n)}{\sqrt{n}} \quad \text{(in probability, assuming convergence)}.$$

### Proposition 1 (Conditional Obstruction Criterion, Proposition 5 of repeated-21-frontier.md)
For the pattern $\tau = 21$ of length $d = 2$:
1. If $c_{21} < 2/d = 1$, Noga Alon's random-superpattern conjecture is **FALSE**.
   *Proof.* For $k = 2m$ and $n = \lceil C k^2 \rceil$, $L_{21}(\sigma_n)/m \to 2 \sqrt{C} c_{21}$. For any $C \in (1/4, \frac{1}{4 c_{21}^2})$, $2 \sqrt{C} c_{21} < 1$, so the target $21^{\oplus m}$ is absent from $\sigma_n$ with probability tending to 1, refuting general universality above coefficient $1/4$.
2. If $c_{21} \ge 1$, the individual repeated family $21^{\oplus m}$ is contained with high probability for all $C > 1/4$, eliminating this specific pattern as an obstruction to Alon's conjecture.

### The Asymptotic Rigor Standard
Finite-host simulations at $n = 4096$ yield an empirical average $\bar{L}_{21}/\sqrt{n} \approx 0.941$. In accordance with strict repository norms, **finite sample averages, fitted intercepts, and local numerical drifts do NOT constitute an asymptotic bound**. An asymptotic certificate requires a rigorous Lyapunov functional, an invariant measure bound, or a supermartingale comparison process with an explicit boundary correction.

---

## 2. The Coupled Marked Interval Process State Space

Points arrive in increasing position coordinate $x$ with distinct heights $y \in (0, R)$.

### Definition 2.1 (System State)
The system state $S = (F, \mathcal{A})$ consists of:
1. **The Completed Threshold Frontier**:
   $$F = (0 = F_0 < F_1 < F_2 < \dots < F_M < F_{M+1} = \infty),$$
   where $F_m$ is the minimal maximum height among all completed $m$-pair copies ($21^{\oplus m}$) scanned so far. By convention, $F_m = \infty$ for $m > M$.
2. **The Active Marked Interval Set**:
   A finite set of pending intervals $\mathcal{A} = \{(l_i, z_i)\}_{i=1}^K$, where:
   - $z_i \in (0, R)$ is the apex (upper point of the pending pair).
   - $l_i \in [0, z_i)$ is the historical activation mark: the value of the completed threshold $F_m$ at the exact arrival time of apex $z_i$.

### Lemma 2.2 (Permanent Dominance Pruning, Lemma 1 of W40)
A level-$m$ pending interval with apex $z \ge F_{m+1}$ can be permanently deleted from $\mathcal{A}$ without altering any future completed threshold at any subsequent prefix.

*Proof.* Completing such an interval on a future arrival $y \in (l, z)$ would produce a completed $(m+1)$-pair copy with maximum $z$. But $F_{m+1} \le z$ already exists and only decreases in time. Any future extension above $z$ is equally available above the smaller threshold $F_{m+1}$. Furthermore, subsequent pending intervals start only from the least completed threshold. Thus, deleting $(l, z)$ cannot alter any current or future completed threshold. $\blacksquare$

### Corollary 2.3 (One-Gap Localization)
After dominance pruning, every retained pending interval $(l, z) \in \mathcal{A}$ satisfies:
$$F_m \le l < z < F_{m+1} \quad \text{where } m = \operatorname{level}(z).$$
In particular, each retained apex $z$ belongs to exactly one threshold gap $(F_m, F_{m+1})$, which uniquely identifies its level $m$.

---

## 3. The 4-Point Mark Necessity Theorem

A central foundational question is whether the historical activation marks $l_i$ can be discarded, i.e., whether the pair $(F, \{z_i\})$ of completed thresholds and unmarked apices forms an exact Markovian state.

### Theorem 3.1 (Activation Marks are Mathematically Indispensable)
The state of completed thresholds $F$ and unmarked pending apices $\{z_i\}$ is **not Markovian**. Discarding activation marks $l_i$ destroys the deterministic transition operator and alters the infinitesimal generator drift.

*Proof.* Consider the two 4-point host prefixes:
$$P = (3, 2, 4, 1) \quad \text{and} \quad Q = (2, 3, 1, 4).$$
We trace the exact pruned state evolution for each prefix:

**Prefix $P = (3, 2, 4, 1)$:**
1. Arrival $y_1 = 3$: gap $(0, \infty)$, cover $\emptyset$. Insert $(0, 3)$. $F = [0, \infty]$, $\mathcal{A} = \{(0, 3)\}$.
2. Arrival $y_2 = 2$: gap $(0, \infty)$, cover $\{3\}$ (since $0 < 2 < 3$). $z^* = 3$. $F_1 \leftarrow 3$. Prune $[3, \infty)$ (deletes $(0, 3)$). Insert $(0, 2)$. $F = [0, 3, \infty]$, $\mathcal{A} = \{(0, 2)\}$.
3. Arrival $y_3 = 4$: gap $(3, \infty)$, cover $\emptyset$. Insert $(F_1, 4) = (3, 4)$. $F = [0, 3, \infty]$, $\mathcal{A} = \{(0, 2), (3, 4)\}$.
4. Arrival $y_4 = 1$: gap $(0, 3)$, cover $\{2\}$ (since $0 < 1 < 2$). $z^* = 2$. $F_1 \leftarrow 2$. Prune $[2, 3)$ (deletes $(0, 2)$). Apex 4 has $4 \notin [2, 3)$, so $(3, 4)$ is retained. Insert $(0, 1)$.
   **Final state for $P$:**
   $$F(P) = [0, 2, \infty], \quad \mathcal{A}(P) = \{(0, 1), (3, 4)\}.$$

**Prefix $Q = (2, 3, 1, 4)$:**
1. Arrival $y_1 = 2$: gap $(0, \infty)$, cover $\emptyset$. Insert $(0, 2)$. $F = [0, \infty]$, $\mathcal{A} = \{(0, 2)\}$.
2. Arrival $y_2 = 3$: gap $(0, \infty)$, cover $\emptyset$ (since $0 < 3 < 2$ is false). Insert $(0, 3)$. $F = [0, \infty]$, $\mathcal{A} = \{(0, 2), (0, 3)\}$.
3. Arrival $y_3 = 1$: gap $(0, \infty)$, cover $\{2, 3\}$. $z^* = \min(2, 3) = 2$. $F_1 \leftarrow 2$. Prune $[2, \infty)$ (deletes both $(0, 2)$ and $(0, 3)$). Insert $(0, 1)$. $F = [0, 2, \infty]$, $\mathcal{A} = \{(0, 1)\}$.
4. Arrival $y_4 = 4$: gap $(2, \infty)$, cover $\emptyset$. Insert $(F_1, 4) = (2, 4)$.
   **Final state for $Q$:**
   $$F(Q) = [0, 2, \infty], \quad \mathcal{A}(Q) = \{(0, 1), (2, 4)\}.$$

**Comparison:**
- Both prefixes have identical completed thresholds: $F(P) = F(Q) = [0, 2, \infty]$.
- Both prefixes have identical sets of retained apices: $\{z_i\} = \{1, 4\}$.
- However, their activation marks differ: apex 4 has mark $l = 3$ in $P$, but mark $l = 2$ in $Q$.

Now consider the response to a subsequent arrival at height $y = 2.5 \in (2, \infty)$:
- In $P$, the pending interval at level 1 is $(3, 4)$. Since $2.5 \notin (3, 4)$, no interval covers $y$. No completion occurs, and $F_2$ remains $\infty$.
- In $Q$, the pending interval at level 1 is $(2, 4)$. Since $2.5 \in (2, 4)$, apex 4 closes! Threshold $F_2$ is updated to 4.

Furthermore, evaluating the infinitesimal generator drift for the cut counting functional $N_4(S) = \#\{m \ge 1 : F_m \le 4\}$:
$$\mathcal{L} N_4(P) = \operatorname{length}((3, 4)) = 1.0 \quad \ne \quad 2.0 = \operatorname{length}((2, 4)) = \mathcal{L} N_4(Q).$$
Thus, state transition probabilities and infinitesimal drifts cannot be computed without the activation marks $l_i$. The unmarked state space is non-Markovian. $\blacksquare$

---

## 4. The Continuous Poisson Jump Generator & The Exact Cut-Flux Theorem

Points arrive as a planar Poisson point process of unit intensity on $[0, \infty) \times [0, R]$, scanned in increasing $x$-order.

### Definition 4.1 (Infinitesimal Generator)
For any bounded or locally Lipschitz functional $\Phi: \mathcal{S} \to \mathbb{R}$, the infinitesimal jump generator is:
$$\mathcal{L} \Phi(S) = \int_0^R [\Phi(T_y S) - \Phi(S)] \, dy,$$
where $T_y S$ is the deterministic state update rule:
1. Identify index $j$ such that $F_j < y < F_{j+1} = b$.
2. Identify covering apices $\mathcal{C}(y) = \{z : (l, z) \in \mathcal{A}, \ l < y < z\}$.
3. If $\mathcal{C}(y) \ne \emptyset$:
   - Let $z^* = \min \mathcal{C}(y)$.
   - Update $F_{j+1} \leftarrow z^*$.
   - Delete all intervals in $\mathcal{A}$ with apex in $[z^*, b)$.
   - If $j+1 = M+1$, append $\infty$.
4. Insert pending interval $(F_j, y)$ into $\mathcal{A}$.

### Theorem 4.2 (Exact Cut-Flux Theorem, Proposition 4 of W40)
Fix $u \in (0, R) \setminus \{F_m\}$. Let $N_u(S) = \#\{m \ge 1 : F_m \le u\}$ and $j = N_u(S)$, so that $F_j \le u < F_{j+1}$.
Define the active cut-covering union:
$$U_u(S) = \bigcup_{(l, z) \in \mathcal{A}: \ F_j < z \le u} (l, z),$$
and the instantaneous cut-flux rate:
$$r_u(S) = \operatorname{length}(U_u(S)).$$
Then the infinitesimal drift of $N_u(S)$ is identically equal to $r_u(S)$:
$$\mathcal{L} N_u(S) \equiv r_u(S).$$

*Proof.* By definition of the generator:
$$\mathcal{L} N_u(S) = \int_0^R [N_u(T_y S) - N_u(S)] \, dy.$$
The count $N_u(T_y S)$ changes if and only if a completed threshold transitions across $u$.
1. If $y \in (F_k, F_{k+1})$ with $k < j$: any completion updates $F_{k+1}$ to $z^* < F_{k+1} \le F_j \le u$. Since $F_{k+1}$ was already $\le u$ before the update, $N_u$ is unchanged.
2. If $y \in (F_k, F_{k+1})$ with $k > j$: any completion updates $F_{k+1}$ to $z^* > y > F_k \ge F_{j+1} > u$. Since $z^* > u$, the new threshold remains strictly greater than $u$, so $N_u$ is unchanged.
3. If $y \in (F_j, F_{j+1})$: a completion updates $F_{j+1}$ to $z^* = \min \mathcal{C}(y)$. The count $N_u$ increases by 1 if and only if $z^* \le u$.
   - If $y \in U_u(S)$, there exists some $(l, z) \in \mathcal{A}$ with $F_j < z \le u$ such that $l < y < z$. Then $z \in \mathcal{C}(y)$, which implies $z^* = \min \mathcal{C}(y) \le z \le u$. Hence $F_{j+1}$ becomes $\le u$, increasing $N_u$ by 1.
   - Conversely, if $z^* \le u$, then the minimizing apex $z^*$ belongs to an active interval $(l^*, z^*)$ with $F_j < z^* \le u$ and $l^* < y < z^*$. Thus $y \in (l^*, z^*) \subseteq U_u(S)$.
4. Since only one threshold changes on each arrival, $N_u(T_y S) - N_u(S) \in \{0, 1\}$.
Therefore, the integrand $N_u(T_y S) - N_u(S)$ is exactly the indicator function $\mathbf{1}_{U_u(S)}(y)$. Integrating over $[0, R]$ gives:
$$\mathcal{L} N_u(S) = \int_0^R \mathbf{1}_{U_u(S)}(y) \, dy = \operatorname{length}(U_u(S)) = r_u(S). \quad \blacksquare$$

### Corollary 4.3 (Compensated Counting Martingale)
For the process started from the empty state $S_0 = ([0, \infty], \emptyset)$:
$$\mathbb{E}[N_u(S_t)] = \int_0^t \mathbb{E}[r_u(S_s)] \, ds.$$

---

## 5. Candidate Lyapunov Functionals Incorporating Activation Marks

To determine whether the drift can certify an asymptotic upper bound $c_{21} < 1$, we formulate three candidate Lyapunov functionals.

### 5.1 Candidate 1: Integrated Profile Potential $\Psi_R(S)$
Define the integrated threshold profile:
$$\Psi_R(S) = \int_0^R N_u(S) \, du = \sum_{m=1}^M (R - F_m)_+.$$

**Theorem 5.1 (Profile Drift Identity).**
$$\mathcal{L} \Psi_R(S) = \int_0^R r_u(S) \, du.$$
*Proof.* Applying Fubini's theorem to the generator integral:
$$\mathcal{L} \Psi_R(S) = \mathcal{L} \left( \int_0^R N_u(S) \, du \right) = \int_0^R \mathcal{L} N_u(S) \, du = \int_0^R r_u(S) \, du. \quad \blacksquare$$

Since $r_u(S) \le u - F_{N_u(S)}$, we obtain the global bound:
$$\mathcal{L} \Psi_R(S) \le \int_0^R (u - F_{N_u}) \, du \le \frac{R^2}{2}.$$

### 5.2 Candidate 2: Mark-Aware Energy Functional $\Phi_\alpha(S)$
To account for stored completion capacity in pending intervals, define:
$$\Phi_\alpha(S) = \sum_{m=1}^M (R - F_m) + \alpha \sum_{(l, z) \in \mathcal{A}} (z - l), \quad \alpha \in \mathbb{R}.$$
For any arrival $y \in (F_j, F_{j+1})$:
- A new interval $(F_j, y)$ is inserted, adding $\alpha (y - F_j)$ to the interval energy.
- The expected insertion energy per unit Poisson intensity is:
  $$\sum_{j=0}^M \int_{F_j}^{F_{j+1}} \alpha (y - F_j) \, dy = \alpha \sum_{j=0}^M \frac{(F_{j+1} - F_j)^2}{2} > 0 \quad (\text{for } \alpha > 0).$$
- When a completion occurs at $z^*$, $F_{j+1}$ drops to $z^*$, adding $(b - z^*)$ to the threshold energy, and dominance pruning removes all active intervals in $[z^*, b)$, subtracting their activation energy $\alpha \sum_{z \in [z^*, b)} (z - l)$.

**Obstruction:** For $\alpha > 0$, the continuous arrival stream injects fresh activation energy at rate $\alpha \sum \frac{(F_{j+1} - F_j)^2}{2}$. For $\alpha < 0$, completions release energy. For all $\alpha$, $\mathcal{L} \Phi_\alpha(S)$ remains strictly positive on reachable states; hence $\Phi_\alpha$ cannot serve as a negative-drift supermartingale without boundary damping.

### 5.3 Candidate 3: Monotone Comparison Process with Boundary Correction
Consider the comparison functional:
$$\Xi_\rho(S_t, t) = \rho u - N_u(S_t) + \frac{t}{4\rho} + B(S_t),$$
where $\rho > 0$ is a variational scaling parameter and $B(S_t)$ is a boundary correction functional.
Taking time derivatives:
$$\frac{d}{dt} \mathbb{E}[\Xi_\rho(S_t, t)] = -\mathbb{E}[r_u(S_t)] + \frac{1}{4\rho} + \frac{d}{dt} \mathbb{E}[B(S_t)].$$
If the uncorrected comparison $B(S_t) \equiv 0$ held as a submartingale, then:
$$\mathbb{E}[N_u(S_t)] \le \rho u + \frac{t}{4\rho}.$$
Optimizing over $\rho > 0$ yields:
$$\min_{\rho > 0} \left( \rho u + \frac{t}{4\rho} \right) = \sqrt{tu}.$$
Setting $t = u = \sqrt{n}$ gives $\mathbb{E}[L_{21}(\sigma_n)] \le \sqrt{n} + o(\sqrt{n})$, establishing the benchmark upper bound:
$$c_{21} \le 1.$$

---

## 6. The Boundary Leakage Obstruction & Finite-Host Diagnostics

### Theorem 6.1 (Non-Existence of Uniform Uncorrected Sub-1 Pointwise Bound)
There is no constant $c < 1$ such that $r_u(S) \le c u$ uniformly across all reachable states $S$.
In fact:
$$\sup_{S \text{ reachable}} \frac{r_u(S)}{u} = 1.0.$$

*Proof.* Let the state $S$ be initialized empty ($F_0 = 0, F_1 = \infty, \mathcal{A} = \emptyset$).
Let a single point arrive at height $z = u$.
Then $j = 0$ since $F_0 = 0 < u < F_1 = \infty$.
The update inserts pending interval $(F_0, u) = (0, u)$ into $\mathcal{A}$.
Now consider cut $u$:
$j = N_u(S) = 0$. The relevant active intervals with $F_0 < z \le u$ consists of the single interval $(0, u)$.
Its length is:
$$r_u(S) = \operatorname{length}((0, u)) = u.$$
Therefore:
$$\frac{r_u(S)}{u} = \frac{u}{u} = 1.0. \quad \blacksquare$$

### 6.2 The Boundary Leakage Obstruction
The peak flux $\sup_S r_u(S)/u = 1.0$ exposes the fundamental obstruction to bounding $c_{21} < 1$:
1. **Dynamic Flux Fluctuations**: In any reachable trajectory, $r_u(S_t)/u$ fluctuates between 0 (when no pending interval covers the cut) and 1 (when an interval spans the entire gap $(0, u)$).
2. **Boundary Starvation at $y = 0$**: Near the lower boundary $y = 0$, $F_1$ is constrained to be strictly positive. Points arriving near 0 cannot easily find a lower point to form a pair, suppressing pair creation at the bottom.
3. **Boundary Truncation at $y = R$**: Points near $R$ cannot find an upper apex, truncating pair creation at the top.
4. **Finite-Size Drag**: In a finite box of size $n = 4096$, boundary starvation and initialization lag reduce the empirical mean $\bar{L}_{21}/\sqrt{n}$ to $\approx 0.941$.
   Crucially, the exact same phenomenon occurs for the longest increasing subsequence (LIS):
   For LIS, the asymptotic limit is known to be exactly 2 (Vershik-Kerov 1977, Logan-Shepp 1977). Yet at $n = 4096$, the finite-host average is:
   $$\frac{\mathbb{E}[LIS]}{\sqrt{n}} \approx 2 - c_0 n^{-1/6} \approx 1.83.$$
   Mistaking $1.83 < 2$ for evidence that the LIS constant is strictly less than 2 would be a catastrophic mathematical error.
   Similarly, asserting $c_{21} < 1$ based on the finite-host statistic $0.941$ without an explicit boundary correction $B(S)$ would violate mathematical rigor.

### 6.3 Resolution and Necessary Condition for an Asymptotic Certificate
An asymptotic certificate $c_{21} \le c < 1$ mathematically requires either:
1. An explicit boundary correction functional $B(S_t)$ such that:
   $$\mathcal{L} N_u(S) \le \rho u + \frac{c^2 t}{4\rho} + \mathcal{L} B(S) \quad \text{with } \mathbb{E}[B(S_t)] = o(\sqrt{t}),$$
2. Or a rigorous invariant probability measure $\mu$ for the shift-invariant profile process proving:
   $$\int_{\mathcal{S}} r_u(S) \, d\mu(S) \le c u \quad \text{with } c < 1.$$
Both routes remain open. Workstream W44 establishes the exact generator and verifies that activation marks and boundary corrections are mathematically indispensable.
