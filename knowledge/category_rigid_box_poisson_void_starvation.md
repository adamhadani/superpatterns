# Category: Rigid Box Poisson Void Starvation

Type: failed_approach_category
Pattern: Reserving private Cartesian boxes of area $\le 1/k^2$ fails due to Poisson void starvation ($e^{-0.25} \approx 0.7788$ void probability per box, joint non-emptiness decaying as $\le 10^{-\Theta(k)}$)
Count: 15

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | strategy_L02_N00 | Rigid Cartesian rank-slot box decomposition ($B_i = I_i \times J_i$) fails almost surely due to Poisson voids ($e^{-0.25} \approx 0.7788$ void probability per cell, joint non-emptiness $\le 10^{-65}$ at $k=100$). |
| 2 | strategy_L02_N02 | Independent private Poisson cell reservation requires $k$ non-empty boxes of area $1/k^2$, failing with probability $\ge 1 - 10^{-65}$ at $k=100$. |
| 3 | strategy_L02_N04 | Assigning residual permutation elements $\mathcal{R}$ to private spatial cells fails because each cell has expected Poisson intensity $\le 0.25$ and void probability $> 77\%$. |
| 4 | strategy_L02_N06 | Reserving rigid coordinate boxes of area $1/k^2$ for rank-slot isolation has $22.1\%$ success rate per box, yielding joint success probability $\le 10^{-65}$ across $k=100$ cells. |
| 5 | strategy_L03_N00 | Residual coordinate embedding via private rank-slot boxes of area $2/(9k^2)$ suffers $94.1\%$ vacancy rate, causing joint non-emptiness across $k$ elements to fail with probability $\ge 1 - 10^{-122.7}$ at $k=100$. |
| 6 | strategy_L03_N04 | Rank-slot grid with individual slots of area $(\Delta/((\Delta+1)k))^2$ has an $88.5\%$ cell vacancy rate in Poisson host $\Pi_{n_0}$, causing joint non-emptiness across $k$ elements to fail with probability $\ge 1 - 10^{-94}$ at $k=100$. |
| 7 | strategy_r2_L02_N00 | Attempting to compress W47 lookahead ($C_0 \approx 9.62$) to Alon's threshold $C = 0.275$ collapses cell Poisson intensity 38-fold to $\mu_{\mathrm{cell}} = 0.0306$, causing 4-cell void probability to explode from $3.74 \times 10^{-8}$ to $88.50\%$ and extinguishing lookahead branching trees. |
| 8 | strategy_r2_L02_N02 | Compressing W47 lookahead cells to $C = 0.275$ causes joint 4-cell void probability to surge to $61.33\%$, turning the lookahead search tree into a strictly subcritical branching process that extinguishes almost surely. |
| 9 | explorer_r3_L00_N02 | Fining $r \times r$ quantile sub-cells within macroscopic boxes collapses per-cell Poisson intensity to $\lambda \approx 0.044$, leaving $95.7\%$ of sub-cells empty and starving embedding paths. |
| 10 | explorer_r3_L00_N03 | Dedicated rank-slot cells of area $1/k^2$ have Poisson mean $\mu = 0.275$, leading to void probability $e^{-0.275} \approx 0.76$ and joint survival probability across $k=100$ slots bounded by $\le 10^{-61.9}$. |
| 11 | N25 (Level 0) | Universal host regularity certificate on macroscopic boxes of area $\ge \varepsilon/k$ provides zero control over single-element cells of area $1/k^2$, where Poisson intensity collapses to $\mu_{\mathrm{cell}} = 0.1222$ (88.5% empty cells) |
| 12 | N29 (Level 0) | Mesoscopic certificate scale separation: macroscopic density on $O(1/\varepsilon^2)$ boxes provides zero protection against void starvation in microscopic dynamic strips of height $1/k^2$ (which have 99.83% vacancy) |
| 13 | explore_merger_r3_L01_N08 | In Theorem 2.1, cell side length was claimed to be $2/(3k)$ across $M=3k$ cells, which spans $[0, 2]^2$ (area 4.0, a 4x geometric area scaling error); correcting cell side length to $1/(3k)$ collapses expected cell Poisson count from $\mu_{\mathrm{cell}} = 4.275$ down to $1.069$, increasing 4-cell void probability by $372,000\times$ (from $3.96 \times 10^{-8}$ to $1.39\%$). |
| 14 | explore_merger_r3_L01_N09 / N15 | At Alon's threshold $C = 0.275$, grid cells of area $4/(9k^2)$ have Poisson mean $\mu_{\mathrm{cell}} = 0.1222$ ($88.50\%$ vacant), 4-cell void probability surges to $61.33\%$ per step, and lookahead branching trees undergo $100\%$ Galton--Watson extinction with offspring mean $0.460 < 1.0$ and 100-step path survival $5.45 \times 10^{-42}$. |
| 15 | explore_merger_r3_L03_N01 | At Alon's threshold $C = 0.275$, grid cells of area $4/(9k^2)$ collapse Poisson mean 38-fold to $\mu_{\mathrm{cell}} = 0.1222$ ($88.50\%$ empty cells), surging 4-cell void probability to $61.33\%$ per step and triggering $100\%$ Galton-Watson branching tree extinction (offspring mean $0.4602 < 1.0$, 100-step path survival $5.45 \times 10^{-42}$). |
