# Category: Omission of Coarse Penalties

Type: failed_approach_category
Pattern: Calculating net surplus drift as $D_{\mathrm{net}}(s) = D_{\mathrm{coarse}}(s) - P_{\mathrm{fine}}(s)$ silently drops coarse-scale discretization penalties $\sum_{j \le j^*} P_j \approx 2.41 C_1 k$, which exceed the macroscopic surplus $2\varepsilon k$ by orders of magnitude.
Count: 4

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_L00_N05 | Dropped coarse-scale penalties $\sum_{j \le j^*} P_j \approx 2.41 C_1 k$; true net drift when accounting for all interfaces is $-2.40 k < 0$ at $\varepsilon=0.01$. |
| 2 | explorer_L00_N19 | Defined $D_{\mathrm{net}} = D_{\mathrm{coarse}} - P_{\mathrm{fine}}$, dropping coarse penalties $\sum_{j=1}^{j*} P_j \ge 2.37 k$; true net drift is $-2.31 k \ll 0$ at $\varepsilon=0.05$. |
| 3 | explorer_L00_N23 | Omitted coarse discretization penalties $\sum_{j=1}^{j*} P_j \approx 2.414 C_{\mathrm{pen}} k$; restoring coarse penalties yields net deficit $\approx -2.4 k < 0$ for all small $\varepsilon$. |
| 4 | explorer_L00_N30 | Omitted coarse-scale fluctuations of order $\Theta(k)$, which strictly overwhelm the $O(\varepsilon k)$ macroscopic surplus. |
