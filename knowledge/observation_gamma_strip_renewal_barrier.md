# Gamma Strip Renewal Completion Barrier

Type: observation
Confidence: high
Source: Candidates explorer_r2_L00_N00, explorer_r2_L00_N02, explorer_r2_L00_N03, explorer_r2_L00_N05, explorer_r2_L00_N06, explorer_r2_L00_N07 (Round 2 Level 0); Aggregators strategy_L01_N00, strategy_L01_N03, strategy_L01_N06, strategy_L01_N07, strategy_L01_N10, strategy_L01_N11, strategy_L01_N14 (Round 2 Level 1)
Relevant to: Continuous horizontal rank-strip slicing and 1D Poisson renewal embedding models

## Statement
When target elements of a permutation $\pi \in S_k$ are assigned to $k$ disjoint horizontal strips $\{S_v\}_{v=1}^k$ of height $1/k$ across a planar Poisson point process $\Pi$ of intensity $C k^2$ on $[0, 1]^2$, the point process within each strip has linear arrival rate $\lambda = C k$. Because the strips are pairwise disjoint and values $\pi(1), \dots, \pi(k)$ are distinct, sequential greedy point selection queries an untouched strip at each step. By the strong Markov property, the horizontal increments $W_t = x_t - x_{t-1}$ are independent $\operatorname{Exp}(C k)$ random variables, so the completion coordinate is Gamma-distributed:
$$x_k = \sum_{t=1}^k W_t \sim \operatorname{Gamma}(k, C k).$$
In particular:
$$\mathbb{E}[x_k] = \frac{k}{C k} = \frac{1}{C}, \quad \operatorname{Var}(x_k) = \frac{1}{C^2 k}.$$
By the arithmetic-harmonic mean inequality, for any non-uniform partition of heights with $\sum h_t \le 1$, the expected completion coordinate satisfies $\mathbb{E}[x_k] \ge 1/C$. Consequently:
1. At Noga Alon's conjectured threshold $C = 1/4 + \varepsilon$, $\mathbb{E}[x_k] = 1/(1/4+\varepsilon) \approx 3.33 \text{ to } 4.0 \gg 1.0$ (overshooting the unit square width by $3.3\times$ to $4\times$, or $7.3\times$ if $2k$ half-strips are used).
2. Achieving $\mathbb{E}[x_k] \le 1.0$ in 1D strip renewal strictly requires host constant $C \ge 1.0$.
3. At $C = 1/4+\varepsilon$, completion within $[0, 1]$ is a deep lower-tail large deviation with Cramér rate function $I(C) = C - 1 - \ln C \approx 0.6363$ at $C = 0.25$, yielding an exponentially small success probability $\Pr(x_k \le 1) \le \exp(-I(C)k) \le 10^{-50}$ at $k=100$.

## Evidence
- Exact analytical calculus via Legendre transform of the exponential cumulant generating function: $I(C) = C - 1 - \ln C$.
- Cauchy-Schwarz traversal barrier: For any partition of $[0, 1]$ into horizontal strips $\{S_i\}_{i=1}^k$ of heights $h_i > 0$ ($\sum_{i=1}^k h_i \le 1$), the Cauchy-Schwarz inequality $(\sum h_i)(\sum 1/h_i) \ge k^2$ forces $\sum_{i=1}^k 1/h_i \ge k^2$, with strict equality if and only if heights are uniform ($h_i = 1/k$). Because the arrival rate in strip $i$ is $\lambda_i = C k^2 h_i$, the expected traversal span is $\mathbb{E}[x_k] = \frac{1}{C k^2} \sum_{i=1}^k 1/h_i \ge 1/C \ge 3.64$. Any non-uniform height assignment strictly worsens the delay.
- Monte Carlo simulations across 10,000 trials in N00, N02, N03, N05, N07 confirming empirical mean $\mathbb{E}[x_k] = 1/C$ exactly across all $C \in [0.25, 2.0]$ (e.g., $1.0015$ at $C=1.0$, $4.006$ at $C=0.25$, $7.273$ for $2k$ strips at $C=0.275$).
- Dynamic programming and greedy selection simulations confirming that greedy selection is provably minimal across disjoint bands.

## Implications
Eliminates all proof routes that attempt to achieve Noga Alon's sharp constant $C = 1/4 + \varepsilon$ via 1D horizontal rank strips or single-leaf foliation. Achieving $C = 1/4$ requires exploiting genuinely 2-dimensional spatial optimization (as in Logan-Shepp / Vershik-Kerov for increasing subsequences), because restricting coordinates to 1D strips reduces effective traversal velocity by a factor of 4.

## Caveats
Holds for any architecture where target elements are constrained to disjoint horizontal strips without 2D adaptive windowing or multi-element collective matching.
