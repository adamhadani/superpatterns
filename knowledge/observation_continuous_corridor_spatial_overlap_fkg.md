# Continuous 2D Corridor Spatial Overlap and FKG Thread Correlation

Type: observation
Confidence: high
Source: Candidates explore_merger_r2_L02_N02, explore_merger_r2_L02_N03 and falser reports explore_falser_r2_L02_N02, explore_falser_r2_L02_N03 (Round 2 Level 2)
Relevant to: Multi-threaded scanning, continuous 2D quantile corridors, He-Kwan shift decorrelation in continuous space.

## Statement
In continuous 2D quantile corridors of macroscopic width $w = \Omega(\varepsilon)$, shifted scanning threads $t, t'$ with center vertical shift $\Delta/k \le (\log^2 k)/k$ query overlapping spatial regions whenever $\Delta/k \le 2w$, i.e. $\Delta \le 2wk$.
For $k=1000$ and $w=0.05$, $2wk = 100 \ge T = \lceil\log_2^2(1000)\rceil = 100$, so $100\%$ of thread pairs have $100\%$ same-step spatial corridor overlap across all 1000 target elements.
This directly refutes the discrete He-Kwan rank overlap bound:
$$|T_t \cap T_{t'}| \le 3\sqrt{k}$$
(which assumed width $1/k$) by more than an order of magnitude ($1000$ steps vs $\le 94.9$). Querying practically identical Poisson points induces strong positive correlation under the Harris-FKG inequality, refuting the claimed independent product decay $\exp(-\Omega(k \log^2 k))$.

## Evidence
1. **Geometric Overlap Calculation**:
   - Thread $t$ queries vertical range $[(\pi(i) + t)/k - w, (\pi(i) + t)/k + w]$.
   - Thread $t'$ queries vertical range $[(\pi(i) + t')/k - w, (\pi(i) + t')/k + w]$.
   - The two corridors intersect at target step $i$ if and only if $|t' - t|/k \le 2w \iff |t' - t| \le 2wk$.
   - Because $t, t' \in \{1, 2, \dots, T\}$ with $T = \lceil\log_2^2 k\rceil$, the maximum shift is $T - 1 < \log_2^2 k$.
   - Whenever $2wk \ge \log_2^2 k$ (which holds for all $k \ge 72$ when $w=0.05$), every single pair of threads satisfies $|t' - t| \le 2wk$.
   - Consequently, for every step $i \in [k]$, the two corridors share a vertical stripe of width $2w - |t' - t|/k > 0$. The number of overlapping steps is identically $k$, not $\le 3\sqrt{k}$.
2. **Harris-FKG Positive Correlation**:
   The events $E_t = \{\text{thread } t \text{ fails to complete within } [0, 1]\}$ are decreasing functionals of the Poisson point configuration $\Pi_{n_0}$ on the shared corridors. By the Harris-FKG inequality:
   $$\Pr\left(\bigcap_{t=1}^T E_t\right) \ge \prod_{t=1}^T \Pr(E_t)$$
   is violated in the direction of independence: the conditional failure probability $\Pr(E_{t'} \mid E_t) \ge \Pr(E_{t'})$ increases because conditioning on failure indicates low point count in the shared corridor.
3. **Failure Inversion Compounding**:
   Because single threads in corridors of subcritical effective width fail with probability $p_{\mathrm{fail}} \approx 1.0$, the true joint failure probability satisfies $\Pr(\bigcap_{t=1}^T E_t) \ge 1 - T(1 - p_{\mathrm{fail}}) \approx 1.0$, completely refuting the claim that product multiplication yields $\exp(-\Omega(k \log^2 k))$.

## Implications
Continuous multi-scale 2D corridors cannot inherit the $O(\sqrt{k})$ shift-decorrelation of He & Kwan (2020). Expanding corridor width to $w = \Omega(\varepsilon)$ couples all scanning threads across 100% of target coordinates, eliminating multi-threaded diversity as an escape from the Shannon factorial deficit.

## Caveats
Applies to continuous corridors whose vertical width $w$ does not shrink as $O(1/k)$. If $w \le 1/k$, corridors do not overlap across steps with $|\Delta| > 1$, but arrival rates then collapse back to the subcritical 1D Cauchy-Schwarz barrier $\mathbb{E}[X_k] \ge 1/C > 1.0$.
