# Category: Entropy-Concentration Sign Inversion

Type: failed_approach_category
Pattern: Simultaneous union bound over dyadic interface trees features a fatal sign inversion because tree description entropy rate ($\kappa \ge 1.0$) is an absolute constant independent of $\varepsilon$, strictly dwarfing the $O(\varepsilon^2)$ concentration margin for all small $\varepsilon$ and causing the failure probability upper bound to diverge exponentially to $+\infty$.
Count: 31

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_L00_N00 | Tree description entropy $C_{\mathrm{ent}} k$ ($C_{\mathrm{ent}} \ge 1.0$) overwhelms concentration $c_0 \varepsilon^2 k$, causing union bound exponent $C_{\mathrm{ent}} - c_0 \varepsilon^2 > 0$ to diverge as $\exp(+0.9975 k)$ at $\varepsilon=0.05$. |
| 2 | explorer_L00_N07 | Tree entropy $\kappa_{\mathrm{tree}} k \ge 2.77 k$ exceeds concentration margin $c_2 \varepsilon^2 k$, causing net exponent $\kappa_{\mathrm{tree}} - c_2 \varepsilon^2 > 0$ to diverge to $+\infty$ for all $\varepsilon \le 0.25$. |
| 3 | explorer_L00_N08 | Wrong-sign exponent in union bound: $C_{\mathrm{tree}} - c_{\mathrm{tail}}\varepsilon^2 > 0$ with $C_{\mathrm{tree}} \ge 8.789$, yielding diverging probability bound $\ge \exp(8.7 k)$ for small $\varepsilon$. |
| 4 | explorer_L00_N09 | Dyadic tree entropy rate $\kappa_{\mathrm{chain}} \ge 1.0$ overwhelms concentration $c_1 \varepsilon^2 \le 0.005$, making net union bound exponent positive for all $\varepsilon \le 0.22$. |
| 5 | explorer_L00_N11 | Tree entropy exponent strictly exceeds concentration margin ($\kappa \ge 1.386$ vs $c\varepsilon^2$), leading to divergence of union bound for any $\varepsilon < 2.75$. |
| 6 | explorer_L00_N13 | Actual tree entropy rate $\ge 2\ln 2 \approx 1.386$ strictly exceeds Poisson tail concentration rate $c_1 \varepsilon^2$, forcing union bound divergence. |
| 7 | explorer_L00_N14 | Union bound diverges exponentially because tree state space size $\ge 2^k$ dominates Poisson deviation exponent $c\varepsilon^2 k$. |
| 8 | explorer_L00_N15 | Dyadic profile entropy $\kappa_{\mathrm{dyadic}} k$ ($> 1.0$) overwhelms concentration $c_1 \varepsilon^2 k$, causing union bound probability to diverge exponentially to $+\infty$. |
| 9 | explorer_L00_N16 | Simultaneous concentration exponent $(4\kappa_{\mathrm{tree}} - c_2\varepsilon^2)k \ge +5.52 k > 0$ has wrong sign, causing union bound to diverge exponentially to $+\infty$. |
| 10 | explorer_L00_N17 | Net exponent $(8\ln\Delta - c_0\varepsilon^2)k \ge +5.525 k > 0$ for all $\varepsilon \le 0.1$, exploding exponentially as $\exp(+\Theta(k))$. |
| 11 | explorer_L00_N18 | Dyadic tree description entropy $\kappa_{\mathrm{chain}} \ge 11.56$ dwarfs tail decay rate $c_{\mathrm{tail}}\varepsilon^2$, giving positive net exponent $\ge +11.54$ that explodes to $+\infty$. |
| 12 | explorer_L00_N19 | Union bound net exponent rate $\kappa_{\mathrm{tree}} - c_{\mathrm{tal}}\varepsilon^2 = +7.5488 > 0$ at $\varepsilon=0.05$, requiring unphysical $\varepsilon > 3.88$ to achieve negative exponent. |
| 13 | explorer_L00_N21 | Union bound exponent rate $\kappa - c_2\varepsilon^2$ is strictly positive for all small $\varepsilon$, causing simultaneous failure probability to diverge to $+\infty$. |
| 14 | explorer_L00_N22 | Dyadic profile description entropy rate $\kappa \ln 2 > 0$ strictly exceeds $(1/25)\varepsilon^2$, diverging as $\exp(+0.6927 k) \to +\infty$ at $\varepsilon=0.10$. |
| 15 | explorer_L00_N25 | Union bound net exponent $\kappa - c_1\varepsilon^2 > 0$ strictly positive for all $\varepsilon < \sqrt{\kappa/c_1}$, diverging to $+\infty$. |
| 16 | explorer_L00_N26 | Net exponent rate $\kappa - c\varepsilon^2 \ge +2.77 > 0$ for all $\varepsilon \le 0.05$ ($c\varepsilon^2 \le 0.00025$), causing exponential divergence of simultaneous failure bound. |
| 17 | explorer_L00_N27 | Dividing global deviation by single-block variance creates spurious $2^{j/2}$ factor; true global concentration $O(\varepsilon^2 k 2^{-j/2}) \to 0$ while branching entropy is $\kappa k$, causing divergence. |
| 18 | explorer_L00_N29 | Dyadic tree description entropy $\kappa_{\mathrm{dyadic}} \approx 2.08$ strictly exceeds $c\varepsilon^2$ for all $\varepsilon \le 4.07$, causing simultaneous failure probability to diverge to $+\infty$. |
| 19 | explore_merger_L01_N06 | Claimed coarse configurations are bounded by $(2^{j^*})! = O_\varepsilon(1)$, whereas unstructured permutations disperse across vertical bins yielding $(2^{j^*})^k$ configurations whose entropy rate ($+4.85$) overwhelms concentration by $15,000\times$, exploding the union bound. |
| 20 | explore_merger_L01_N07 | Claimed coarse-conditioned concentration with $N_0(\varepsilon) \le (2^{j^*})! = O_\varepsilon(1)$, but generic permutations disperse across $\Omega(1/\varepsilon^2)$ vertical bins yielding $(2^{j^*})^k$ configurations with entropy rate $+8.31$ to $+13.86$ that explodes the simultaneous union bound to $+\infty$. |
| 21 | explore_merger_L01_N13 | Mesoscopic truncation at scale $L$ still requires residual lookahead paths across $\delta k$ points, whose description entropy rate $\kappa_{\mathrm{tree}}\delta$ strictly exceeds concentration margin $c\varepsilon^2$ for small $\varepsilon$, causing simultaneous failure bound to explode as $\exp(+\Omega(k))$. |
| 22 | strategy_L02_N04 | Coarse permutation configuration entropy rate (+10.4 nats) dwarfs Poisson concentration margin (+0.001 nats), causing exponential union bound divergence. |
| 23 | strategy_L02_N07 | Coarse vertical bin configuration branching factor $(2^{j^*})^k = 8^{100} \approx 2 \times 10^{90}$ creates an entropy deficit of 208 nats, inverting union bound. |
| 24 | strategy_L03_N02 | Conditioning on coarse profiles assigns $k$ elements across $2^{j^*}$ vertical bins, generating an entropy rate of $j^* \ln 2 \approx 10.40$ nats/element that dwarfs Poisson concentration ($0.00125$ nats/elem) and causes the union bound to explode as $\exp(+10.40k) \to +\infty$. |
| 25 | strategy_L03_N03 | Dyadic host boxes event $E_{\mathrm{boxes}}$ only controls macroscopic point counts; fine-scale permutations in $S_{a_{\min}}$ have description entropy rate $\ln(a_{\min}!)/a_{\min} \in [5.18, 7.48]$ nats/element, exceeding Poisson concentration by $1036\times$ to $149,000\times$, exploding the simultaneous union bound as $\exp(+5.86k) \to +\infty$. |
| 26 | strategy_r2_L03_N00 | Backup Route 1 structured map scaffolding at $C = 2.5$ fails because catalog entropy $21 k \ln\ln k$ exceeds linear Poisson concentration margin by $+40,567.9$ nats at $k=1000$, causing catastrophic union bound divergence. |
| 27 | strategy_r2_L03_N02 | Structured periodic class $\mathcal{S}_{\mathrm{periodic}}$ embedding fails because structured map catalog entropy $21 k \ln\ln k$ exceeds Poisson concentration by $+40,584$ nats at $k=1000$. |
| 28 | strategy_r2_L03_N03 | Embedding structured periodic exceptions $\mathcal{S}_{\mathrm{periodic}}$ at $C = 1/4+\varepsilon$ fails because catalog entropy $21 k \ln\ln k$ diverges by $+40,581.4$ nats against linear concentration margin. |
| 29 | N17 (Level 0) | Dyadic tree union bound exponent rate $C_H - c_0 arepsilon^2$ has wrong sign (strictly positive $+0.4958$ for small $arepsilon$), diverging exponentially to $+\infty$ |
| 30 | N24 (Level 0) | Dyadic box certificate asserts single-box Chernoff bound $2\exp(-4/3) \le \exp(-c\varepsilon^2 k)$, manufacturing an exponential decay in $k$ from a constant (~4.55% failure per box) |
| 31 | N31 (Level 0) | Mesoscopic scaffold at scale $M = \Theta(\varepsilon\sqrt{k})$ ($2 \times 2$ grid at $k=1000$) captures only 1.386 nats of coarse entropy vs $\ln(1000!) = 5912.13$ nats, leaving a microscopic deficit of $+5910.74$ nats that explodes under union bound |
