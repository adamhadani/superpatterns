# Workstream W64: The Transversal Thread-Minimum Bound at $C k^2$

## Objective
Establish a rigorous upper bound on the global transversal span:
$$X_{\max}^*(M) := \max_{\pi \in S_k} \min_{0 \le t \le k} X_t(\pi)$$
in a $(2k) \times m$ Bernoulli(1/2) matrix $M$, proving that $X_{\max}^*(M) \le C_0 k$ with probability $1 - o(1)$ for an absolute constant $C_0 > 0$.

By the He–Kwan Bernoulli matrix coupling lemma (Lemma 2.2), this directly establishes that a uniform random permutation of length:
$$n = 4 k m = 4 C_0 k^2$$
is $k$-universal across all $k!$ permutations simultaneously, closing the $\log\log k$ factor from He and Kwan (2020) and resolving Noga Alon's 1999 conjecture at quadratic host length.

## Mathematical Formulation

### 1. The Matrix Coupling
Let $M$ be a $(2k) \times m$ matrix with independent $\operatorname{Bernoulli}(1/2)$ entries.
By He and Kwan (2020, Lemma 2.2), a uniform random permutation $\sigma \in S_n$ ($n = 4km$) can be coupled with $M$ such that:
$$M \text{ contains } \pi \implies \pi \preceq \sigma.$$

### 2. Thread Scanning & Arrival Times
For any $\pi \in S_k$ and any offset $t \in [0, k]$:
- Thread $t$ scans rows $t + \pi(1), \dots, t + \pi(k)$ greedily from left to right.
- $X_t(\pi)$ is the column index where the search completes.
- In Workstream W63, Theorem 1 proved that for ANY target $\pi \in S_k$ and any thread $t$:
  $$X_t(\pi) \sim \operatorname{NegativeBinomial}(k, 1/2), \quad \mathbb{E}[X_t(\pi)] = 2k, \quad \operatorname{Var}(X_t(\pi)) = 2k.$$

### 3. The Thread Minimum and Transversal Span
Define:
- Target minimum cost: $X^*(\pi) := \min_{0 \le t \le k} X_t(\pi)$.
- Global transversal span: $X_{\max}^*(M) := \max_{\pi \in S_k} X^*(\pi)$.

### 4. Key Mathematical Goals
1. **Empirical Distribution of $X_{\max}^*(M)$:**
   Exhaustively compute $X_{\max}^*(M)$ for $k \in \{4, 5, 6, 7\}$ across all $k!$ permutations to establish the exact distribution and scale factor $\mu_k = \mathbb{E}[X_{\max}^*] / k$.
2. **Disjoint Thread Independence:**
   Analyze the $K$ mutually disjoint row bands $B_j = [j \cdot k, (j+1)k - 1]$ to quantify the probability that all $K$ independent threads fail.
3. **Column Slicing and Universal Words:**
   Partition the columns of $M$ into blocks $W_1, \dots, W_\ell$ of width $C$. Connect the transversal span to the covering of symbol permutations by the column vectors $V_c \in \{0, 1\}^{2k}$.
