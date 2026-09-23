# Category: Omission of Coarse Penalties

Type: failed_approach_category
Pattern: Calculating net surplus drift as $D_{\mathrm{net}}(s) = D_{\mathrm{coarse}}(s) - P_{\mathrm{fine}}(s)$ silently drops coarse-scale discretization penalties $\sum_{j \le j^*} P_j \approx 2.41 C_1 k$, which exceed the macroscopic surplus $2\varepsilon k$ by orders of magnitude.
Count: 9

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_L00_N05 | Dropped coarse-scale penalties $\sum_{j \le j^*} P_j \approx 2.41 C_1 k$; true net drift when accounting for all interfaces is $-2.40 k < 0$ at $\varepsilon=0.01$. |
| 2 | explorer_L00_N19 | Defined $D_{\mathrm{net}} = D_{\mathrm{coarse}} - P_{\mathrm{fine}}$, dropping coarse penalties $\sum_{j=1}^{j*} P_j \ge 2.37 k$; true net drift is $-2.31 k \ll 0$ at $\varepsilon=0.05$. |
| 3 | explorer_L00_N23 | Omitted coarse discretization penalties $\sum_{j=1}^{j*} P_j \approx 2.414 C_{\mathrm{pen}} k$; restoring coarse penalties yields net deficit $\approx -2.4 k < 0$ for all small $\varepsilon$. |
| 4 | explorer_L00_N30 | Omitted coarse-scale fluctuations of order $\Theta(k)$, which strictly overwhelm the $O(\varepsilon k)$ macroscopic surplus. |
| 5 | explorer_r3_L00_N00 | Net traversal drift $D_{\mathrm{net}} = D_{\mathrm{coarse}} - P_{\mathrm{fine}}$ drops coarse penalties $\sum_{j \le j^*} P_j \approx 2.38 C_1 k$, which overwhelm continuous surplus $2\varepsilon k$ by up to $116\times$ and force true net drift negative ($D_{\mathrm{net}} \le -0.175k < 0$). |
| 6 | N17 (Level 0) | Net drift calculation dropped coarse-scale boundary penalties $\sum_{j=1}^{j^*} P_j  pprox 2.414 C_1 k$, which exceed gross surplus by 24x to 120x, forcing $D_{\mathrm{net}} \le -2.31k$ |
| 7 | explore_merger_r3_L02_N00 | Summing dyadic interface buffer separations across coarse scales $j \le j^*(\varepsilon)=12$ yields 8,178 interfaces requiring 16,356 buffer points ($\Delta=2$), swamping continuous surplus ($2\varepsilon k = 100$ at $k=1000$) by $163.56\times$ and driving net drift deeply negative ($D_{\mathrm{net}} \le -162.56k < 0$). |
| 8 | explore_merger_r3_L03_N02 | Summing dyadic interface buffers across coarse scales $j \le j^*(\varepsilon) = 12$ at $\varepsilon = 0.05$ yields $\sum_{j=1}^{12}(2^j-1) = 8,178$ coarse interfaces requiring $16,356$ discrete buffer points ($\Delta=2$), swamping continuous surplus ($100$ points at $k=1000$) by $163.56\times$. |
| 9 | explore_merger_r3_L04_N00 | Coarse dyadic boundary interfaces total $\sum_{j=1}^{12}(2^j-1) = 8,178$ at $\varepsilon=0.05$, consuming $16,356$ buffer points ($\Delta=2$) which overwhelms macroscopic continuous surplus ($100$ points at $k=1000$) by $163.56\times$, precluding discrete coarse interface buffering. |
