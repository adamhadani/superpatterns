# The Growing LDS Threshold Sieve & Polynomial Host Squares Architecture

## Mathematical Formulation and Proofs for Workstream W55

23 September 2026. Complete mathematical formulation and rigorous theorems establishing the sharp threshold $n = \lceil(1/4+\varepsilon)k^2\rceil$ for growing-LDS permutation classes.

---

## 1. Introduction and Historical Context

In Workstream W52, we established the Bounded-LDS Sharp Threshold $C^* = 1/4$ for every fixed $d = \mathcal{O}(1)$ via $d$-box antidiagonal splittings and Marcus–Tardos linear topological entropy.
In Workstream W54, we eliminated the adversarial counterexample route across non-monotone permutations (alternating permutations, perturbed identities, Cantor fractals, and uniform random targets), proving that the monotone identity uniquely maximizes autocorrelation covariance and is the true extremal bottleneck.

In Workstream W55, we bridge the gap between fixed $d = \mathcal{O}(1)$ and growing chain counts $d = d(k) \to \infty$. We show how the **Shared Host Squares Architecture** allows the sharp $1/4$ threshold to extend to classes of super-exponential target size $m! \ge \exp(\Omega(k\sqrt{\log k}))$, completely bypassing the Shannon factorial deficit through a logarithmic host certificate family.

---

## 2. The Shared Host Squares Architecture

**Definition 2.1 (Candidate Host Squares Family).**
Let $\Pi_n$ be a Poisson point process on the unit square $[0, 1]^2$ with intensity $n = C k^2$, where $C = 1/4 + \varepsilon$.
For an integer cutoff $L \ge 2$, define the family of candidate host squares:
$$\mathcal{S} = \left\{ Q(s, t, a) = \left( \frac{s}{k}, \frac{s+a}{k} \right) \times \left( \frac{t}{k}, \frac{t+a}{k} \right) : L \le a \le k, \ 0 \le s, t \le k - a \right\}.$$

**Proposition 2.2 (Polynomial Cardinality and Logarithmic Entropy).**
*The cardinality of $\mathcal{S}$ is strictly polynomial in $k$:*
$$|\mathcal{S}| \le (k+1)^3 = \mathcal{O}(k^3).$$
*Consequently, the description entropy of the candidate host squares family is purely logarithmic:*
$$\ln |\mathcal{S}| \le 3 \ln(k+1) = \Theta(\log k).$$

*Proof.*
The length $a$ takes at most $k - L + 1 \le k$ values. For each $a$, the start coordinates $s$ and $t$ each take at most $k - a + 1 \le k + 1$ integer values.
Thus $|\mathcal{S}| \le k(k+1)^2 < (k+1)^3$. The entropy bound follows immediately by taking the natural logarithm. $\blacksquare$

---

## 3. Large Deviation Concentration and the Master Host Event

**Theorem 3.1 (Deuschel–Zeitouni Host Squares Event).**
*Let $C = 1/4 + \varepsilon$ with $\varepsilon > 0$. There exists a constant $c_C > 0$ such that for any cutoff $L \ge K\sqrt{\log k}$ with $c_C K^2 > 4$:*
*The event $E_{\mathrm{squares}}$, defined as the event that every square $Q \in \mathcal{S}$ contains both an increasing and a decreasing subsequence of length $a = k \cdot \operatorname{side}(Q)$, satisfies:*
$$\Pr(E_{\mathrm{squares}}^c) \le 2(k+1)^3 \exp(-c_C L^2) \le 2(k+1)^3 k^{-c_C K^2} = \mathcal{O}(k^{3 - c_C K^2}) = o(1).$$

*Proof.*
Each square $Q(s, t, a) \in \mathcal{S}$ has area $\operatorname{Area}(Q) = (a/k)^2$.
The expected number of Poisson points in $Q$ is:
$$\mu_Q = n \cdot \operatorname{Area}(Q) = (1/4 + \varepsilon) k^2 \cdot \frac{a^2}{k^2} = (1/4 + \varepsilon) a^2 = C a^2.$$
Because $C > 1/4$, the expected LIS and LDS in $Q$ satisfy:
$$\mathbb{E}[\operatorname{LIS}(Q)] = 2\sqrt{C} a = (1 + 2\varepsilon - \mathcal{O}(\varepsilon^2)) a > a.$$
By the classical Deuschel–Zeitouni LIS lower-tail large deviation theorem (Theorem 1, 1999):
$$\Pr\big(\operatorname{LIS}(Q) < a\big) \le \exp(-c_C a^2) \le \exp(-c_C L^2).$$
By vertical reflection symmetry, the identical bound holds for the LDS:
$$\Pr\big(\operatorname{LDS}(Q) < a\big) \le \exp(-c_C L^2).$$
Taking a union bound over all $|\mathcal{S}| \le (k+1)^3$ squares and both directions yields:
$$\Pr(E_{\mathrm{squares}}^c) \le 2(k+1)^3 \exp(-c_C L^2).$$
Substituting $L = \lceil K \sqrt{\log k} \rceil$:
$$\Pr(E_{\mathrm{squares}}^c) \le 2(k+1)^3 \exp(-c_C K^2 \log k) = 2(k+1)^3 k^{-c_C K^2} = \mathcal{O}(k^{3 - c_C K^2}).$$
Choosing $K > \sqrt{4 / c_C}$ gives $c_C K^2 > 4$, ensuring the failure probability decays as $\mathcal{O}(k^{-1}) \to 0$. $\blacksquare$

---

## 4. The Growing LDS Universality Theorem

**Theorem 4.2 (Growing LDS Simultaneous Universality).**
*Let $\mathcal{C}_{k, L}$ denote the class of all permutations $\pi \in S_k$ that admit a decomposition into monotone interval blocks $B_1, \dots, B_m$ of lengths $a_1, \dots, a_m \ge L = \lceil K \sqrt{\log k} \rceil$ summing to $k$, according to an arbitrary skeleton $\rho \in S_m$.*
*Then:*
1. *The class $\mathcal{C}_{k, L}$ contains at least $m! = (k / L)! \ge \exp(\Omega(k \sqrt{\log k}))$ permutations, exhibiting super-exponential cardinality.*
2. *Every permutation $\pi \in \mathcal{C}_{k, L}$ has $\operatorname{LDS}(\pi)$ that can grow as large as $m = \Theta(k / \sqrt{\log k}) \gg \mathcal{O}(1)$.*
3. *On the single common host event $E_{\mathrm{squares}}$, EVERY permutation $\pi \in \mathcal{C}_{k, L}$ is simultaneously contained in a uniform random permutation $\sigma_n \sim \operatorname{Uniform}(S_n)$ of length $n = \lceil(1/4+\varepsilon)k^2\rceil$ with probability $1 - o(1)$.*

*Proof.*
1. Fix any partition $a_1 + \dots + a_m = k$ with each $a_i \ge L$. For every skeleton $\rho \in S_m$, the inflation $\rho[a_1, \dots, a_m]$ produces a distinct permutation in $S_k$. The number of such skeletons is $m!$. With $m = \lfloor k / (K\sqrt{\log k}) \rfloor$, Stirling's approximation gives:
   $$\ln(m!) \sim m \ln m \sim \frac{k}{K\sqrt{\log k}} \ln\left( \frac{k}{K\sqrt{\log k}} \right) \sim \frac{k \ln k}{K\sqrt{\log k}} = \frac{1}{K} k \sqrt{\log k}.$$
   This is super-exponential in $k$.
2. Choosing $\rho = (m, m-1, \dots, 1)$ (decreasing skeleton) and decreasing blocks yields a permutation with $\operatorname{LDS}(\pi) = \sum a_i = k$, while choosing increasing blocks yields $\operatorname{LDS}(\pi) = m = \Theta(k / \sqrt{\log k})$.
3. On the event $E_{\mathrm{squares}}$, every square $Q(s_i, t_i, a_i) \in \mathcal{S}$ contains a monotone subsequence of length $a_i$ with the required direction.
   Define the start coordinates:
   $$s_i = \sum_{j < i} a_j, \quad t_i = \sum_{\rho(j) < \rho(i)} a_j.$$
   Because the position intervals $[s_i, s_i + a_i]$ are consecutive and disjoint in $[0, k]$, the horizontal projections of the squares are pairwise disjoint and correctly ordered.
   Because the value intervals $[t_i, t_i + a_i]$ are disjoint and ordered according to $\rho$, the vertical projections are pairwise disjoint and ordered according to $\rho$.
   Inside each square, the points form a monotone sequence of length $a_i$ in the direction $\operatorname{dir}(B_i)$.
   The union of these chosen points across all $m$ squares forms an exact copy of the target permutation $\pi$.
   Crucially, the event $E_{\mathrm{squares}}$ does not depend on $\rho$ or on the partition $a_1, \dots, a_m$.
   Therefore, simultaneous containment holds for ALL $\pi \in \mathcal{C}_{k, L}$ simultaneously on $E_{\mathrm{squares}}$, with failure probability $\Pr(E_{\mathrm{squares}}^c) = o(1)$. $\blacksquare$

---

## 5. Conclusions & Master Ledger Impact

1. **Extension of Sharp 1/4 from Fixed to Growing LDS**:
   The sharp threshold $C^* = 1/4 = 0.25000$ is rigorously established for all growing-LDS inflations up to $m = \Theta(k / \sqrt{\log k})$ blocks.
2. **Defeating the Shannon Factorial Deficit via Shared Host Squares**:
   Even though the target family contains super-exponentially many permutations ($m! \ge \exp(\Omega(k\sqrt{\log k}))$), the host certificate family requires only $(k+1)^3$ squares, with logarithmic description entropy $3 \ln k$.
3. **Delineation of the Remaining Open Frontier**:
   With W52 (bounded LDS, $d = \mathcal{O}(1)$), W54 (adversarial disproof elimination), and W55 (growing LDS modular inflations, $m = \Theta(k/\sqrt{\log k})$), the only permutations not yet covered at $1/4$ are those consisting predominantly of **fine-scale atomized blocks** of length $< K\sqrt{\log k}$.
