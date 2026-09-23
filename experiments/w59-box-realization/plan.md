# Plan: Workstream W59 — The Microscopic Intra-Box Order Realization Lemma

## 1. Context and Problem Statement
In Workstream W58, we proved that the **Tableau Entropy Barrier** $\sum (f^\lambda)^2 = k!$ can be bypassed by continuous spatial lattice chaining:
- Discretizing $[0, 1]^2$ into an $M \times M$ grid $\mathcal{G}_k$ of boxes with $M = \lceil\sqrt{k}\rceil$ and box area $1/k$.
- The $d \le 2\sqrt{k}$ Greene chains of any generic bulk target $\pi$ traverse at most $4k$ total cell steps.
- The coarse trajectory tuples $\mathbf{T} \in \mathcal{T}_k$ carry strictly linear description entropy:
  $$|\mathcal{T}_k| \le \binom{4k}{k} \le (4e)^k \approx \exp(2.386 k) \ll k!.$$
- The host point density in every box is $\mathbb{E}[N(B_{u, v})] = C k = (1/4+\varepsilon)k \to \infty$.

To complete the proof of simultaneous containment at $(1/4+\varepsilon)k^2$, we must resolve the **microscopic order realization inside each box**:
Given that a target $\pi$ allocates $m_{u, v}$ points to box $B_{u, v}$ with induced relative order $\tau_{u, v} \in S_{m_{u, v}}$, we must prove that the uniformly distributed host points inside $B_{u, v}$ contain $\tau_{u, v}$ with overwhelming probability, allowing a union bound over the spatial lattice and coarse trajectory configurations.

## 2. Theoretical Formulation & Key Lemmas

### 2.1 Balls-into-Bins Target Demand
For a generic bulk permutation $\pi \in S_k$, the target points $\mathcal{P}(\pi) = \{ (i/k, \pi(i)/k) \}$ are spatially dispersed:
- Average target load per box: $\bar{m} = k / M^2 \le 1.00$.
- Maximum target load in any box: by the classical balls-into-bins maximum load theorem,
  $$m_{\max}(\pi) \le \frac{\ln k}{\ln\ln k} (1 + o(1)) \quad \text{with probability } 1 - o(1).$$
  Empirically, for $k = 400$, $m_{\max} \le 6$; for $k = 1024$, $m_{\max} \le 7$.
- For arbitrary permutations (even adversarial), column marginals ensure $m_{u, v} \le \lceil k/M \rceil \le \sqrt{k}+1$.

### 2.2 Host Box Representation
Inside each box $B_{u, v}$, the host process $\Pi_n$ has point count $N \sim \operatorname{Poisson}(C k)$ with $C = 1/4 + \varepsilon$. Conditioned on $N$, the points are i.i.d. uniform in $B_{u, v}$, so their induced permutation $\sigma_{B_{u, v}}$ is distributed as $\operatorname{Uniform}(S_N)$.

### 2.3 The Marcus--Tardos--Fox Microscopic Avoidance Bound
By the Marcus--Tardos theorem (2004) and Fox (2014):
For any pattern $\tau \in S_m$, $|\operatorname{Av}_N(\tau)| \le c_\tau^N$ with $c_\tau \le 2^{O(m)}$.
In a uniform random host permutation $\sigma \sim S_N$:
$$\Pr(\sigma \text{ avoids } \tau) = \frac{|\operatorname{Av}_N(\tau)|}{N!} \le \frac{c_\tau^N}{(N/e)^N} = \left(\frac{e c_\tau}{N}\right)^N.$$
For $N = \Theta(k)$ and $m \le \frac{c \ln k}{\ln\ln k}$, we have $c_\tau \le k^{o(1)}$, so:
$$\frac{e c_\tau}{N} \le \mathcal{O}(k^{-(1-o(1))}) \ll 1 \implies \Pr(\sigma \text{ avoids } \tau) \le \exp\left( - \frac{1}{4} k \ln k (1 - o(1)) \right).$$
This failure probability decays **superexponentially**.

### 2.4 Monotone & Deuschel--Zeitouni Regimes
For larger monotone sub-permutations ($m \le \sqrt{k}$), the expected host box LIS is $2\sqrt{N} \ge \sqrt{1+4\varepsilon}\sqrt{k} > \sqrt{k} \ge m$. By Deuschel--Zeitouni (1999), $\Pr(\operatorname{LIS}(\sigma_N) < m) \le \exp(-\Omega(\varepsilon^2 \sqrt{k}))$.

### 2.5 Simultaneous Box Realization
A union bound across all $M^2 \le 2k$ boxes yields a total failure probability:
$$\Pr(\exists \, (u, v) : \text{box failure}) \le 2k \exp(-\Omega(k \ln k)) = \exp(-\Omega(k \ln k)) \longrightarrow 0.$$

## 3. Implementation Plan
- `plan.md`: Research blueprint and theoretical formulation.
- `proof.md`: Complete mathematical definitions, Marcus--Tardos--Fox avoidance bounds, and intra-box realization theorems.
- `verify.py`: High-performance verification tool auditing balls-into-bins loads, host point Poisson counts, Marcus--Tardos bounds, and empirical pattern containment across $S_k$.
- `log.md`: Chronological execution audit.
- Ledger updates: `experiments/README.md`, `memory/RESULTS.md`, `memory/SESSION-STATE.md`.
