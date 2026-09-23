# Poisson Void Starvation in Rigid Rank-Slot Cells

Type: observation
Confidence: high
Source: Candidates L02_N00, L02_N02, L02_N04, L02_N06 (Level 2 falsers)
Relevant to: Residual element embedding, private Cartesian boxes, lookahead windows, rank-slot isolation.

## Statement
In a planar Poisson point process with intensity $\lambda = (1/4+\varepsilon)k^2$, any strategy that restricts the embedding of $m = \Theta(k)$ target elements (such as residual elements $\mathcal{R}$ or discrete rank slots) to private Cartesian cells $B_i = I_i \times J_i$ of area $\operatorname{Area}(B_i) \le 1/k^2$ suffers fatal Poisson void starvation. Each individual box has expected point count $\mu_i = \lambda \operatorname{Area}(B_i) \le 1/4 + \varepsilon$, and therefore is completely empty (a Poisson void) with probability $\mathbb{P}(N(B_i) = 0) = \exp(-\mu_i) \ge e^{-0.25 - \varepsilon} \approx 0.7788$. Across $m$ independent boxes, the probability that all $m$ boxes are non-empty is at most $(1 - e^{-0.25-\varepsilon})^m \le (0.2212)^m \le 10^{-0.655 m}$, which is $\le 10^{-65.5}$ at $k=100$ (and $\le 10^{-655}$ at $k=1000$).

## Evidence
1. Poisson distribution exact evaluation: For independent cell $B_i$ with area $1/k^2$ and intensity $\lambda = (1/4+\varepsilon)k^2$, $\mu_i = 1/4+\varepsilon$. At $\varepsilon = 0.05$, $\mu_i = 0.30$, and $\mathbb{P}(N(B_i) \ge 1) = 1 - e^{-0.30} \approx 0.2592$.
2. Joint non-emptiness calculation:
   - For $k=100$, $(0.2592)^{100} \approx 8.7 \times 10^{-60}$.
   - For $k=1000$, $(0.2592)^{1000} \approx 10^{-587}$.
   - At $\varepsilon = 0.00$, $(1 - e^{-0.25})^{100} = (0.2212)^{100} \approx 2.9 \times 10^{-66}$.
3. Universal across strategies: Tested across L02_N00 (rigid rank-slot cells), L02_N02 (private cell reservation), L02_N04 (residual box allocation), and L02_N06 (coordinate boxes of area $1/k^2$). In all cases, requiring point presence in deterministic or decoupled microscopic cells of area $O(1/k^2)$ fails almost surely.

## Implications
Any proof route attempting to embed un-gluable residual elements $\mathcal{R}$ by assigning them to deterministic, private, or weakly-coupled spatial cells of scale $1/k \times 1/k$ is mathematically dead. Host points cannot be localized to microscopic boxes of area $1/k^2$ without macroscopic spatial pooling or shared search regions.

## Caveats
This starvation applies specifically to rigid boxes of area $\le O(1/k^2)$. It does not apply to macroscopic search windows of area $s^2 \gg (\log k)/k^2$, where the expected count $\mu \gg \log k$ guarantees non-emptiness with high probability.
