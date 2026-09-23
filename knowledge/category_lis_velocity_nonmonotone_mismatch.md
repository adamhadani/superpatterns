# Category: LIS Velocity Non-Monotone Mismatch

Type: failed_approach_category
Pattern: Treating the Logan-Shepp / Vershik-Kerov LIS traversal velocity $v(s) = 2\sqrt{C} > 1$ as fungible point-acquisition capacity for arbitrary non-monotone permutations is a fatal category error and violates point conservation.
Count: 42

## Entries
| # | Original File | One-line Summary |
|---|---------------|------------------|
| 1 | explorer_L00_N00 | LIS paths embed strictly monotone identity permutations; arbitrary target permutations contain microscopic descents and oscillations that cannot be traversed by increasing paths. |
| 2 | explorer_L00_N03 | Infinitesimal box LIS capacity integration $dN(s) = 2\sqrt{d\mu}$ violates point conservation $\operatorname{LIS}(S) \le |S|$ by predicting $3.8\times$ more points than exist in the entire corridor. |
| 3 | explorer_L00_N08 | Category error applying LIS velocity $2\sqrt{C}$ to non-monotone permutations; increasing paths cannot capture arbitrary permutations without losing $\ge 50\%$ length. |
| 4 | explorer_L00_N09 | LIS velocity $v = 2\sqrt{c} > 1$ applies only to increasing subsequences, whereas general permutations contain descents and oscillations that cannot be embedded along monotone paths. |
| 5 | explorer_L00_N11 | Assumed Logan-Shepp / Vershik-Kerov LIS velocity applies to general dyadic blocks, ignoring that target permutation blocks have microscopic descents. |
| 6 | explorer_L00_N12 | Assumed diagonal boxes have LIS capacity exceeding block size, but diagonal boxes are $77\%$ empty (mean points $\le 0.26$), yielding near-zero capacity. |
| 7 | explorer_L00_N13 | Monotone LIS capacity captures only $2\sqrt{L} \ll L$ points on non-monotone permutation blocks, leading to a $100\%$ capacity deficit as block size $L \to \infty$. |
| 8 | explorer_L00_N14 | LIS velocity applied to arbitrary non-monotone permutations; local descents break chain path monotonicity. |
| 9 | explorer_L00_N15 | LIS velocity $2\sqrt{c} > 1$ cannot be integrated across non-monotone dyadic intervals without violating order preservation. |
| 10 | explorer_L00_N16 | Vershik-Kerov LIS velocity $2\sqrt{C} > 1$ applied to arbitrary non-monotone permutations; local jumps require non-monotone paths. |
| 11 | explorer_L00_N17 | Assumed LIS limit shape velocity $2\sqrt{C}$ allows arbitrary non-monotone traversal; directed paths cannot embed descents without deficit. |
| 12 | explorer_L00_N18 | Equated LIS traversal velocity $v(s) = 2\sqrt{C}$ with embedding capacity; only 0.69% of permutations in $S_8$ have monotone dyadic blocks. |
| 13 | explorer_L00_N19 | Hydrodynamic traversal rate $2\sqrt{C}$ applies only to monotone increasing paths, whereas generic target permutations require non-monotone choices. |
| 14 | explorer_L00_N20 | Monotone increasing paths in $[0, 1]^2$ cannot embed permutations with inversions, which by Greene's theorem require $\approx 2\sqrt{k}$ coupled chains. |
| 15 | explorer_L00_N21 | Applied Logan-Shepp LIS limit to microscopic non-monotone blocks where basic cells have mean count $\approx 0.028$ and void probability $> 78\%$. |
| 16 | explorer_L00_N22 | Evaluated traversal capacity along arbitrary target trajectories using monotone LIS formula, omitting permutation ranks entirely. |
| 17 | explorer_L00_N23 | Generic permutations on dyadic blocks have LIS $2\sqrt{k_j} \ll k_j$, so directed monotone paths capture only a vanishing fraction of target elements. |
| 18 | explorer_L00_N24 | Logan-Shepp / Vershik-Kerov LIS traversal rate $2\sqrt{C}$ applied to arbitrary non-monotone permutations; local descents break chain path monotonicity. |
| 19 | explorer_L00_N25 | LIS limit shape velocity conflated with non-monotone embedding capacity; monotone paths capture only a vanishing fraction of generic permutation blocks. |
| 20 | explorer_L00_N26 | 2D LIS limit treated as 1D differential form $dN = 2\sqrt{d\mu}$, predicting 107 points in corridor containing only 28.5 points (violates point conservation). |
| 21 | explorer_L00_N27 | Monotone LIS velocity applied across dyadic blocks of general permutations; monotone paths fail to capture microscopic descents. |
| 22 | explorer_L00_N28 | LIS velocity along diagonal $ds \times ds$ invalid for non-monotone targets where box heights do not shrink; concavity of $\sqrt{\cdot}$ artificially inflated capacity in simulation. |
| 23 | explorer_L00_N29 | Logan-Shepp / Vershik-Kerov LIS limit velocity applied to non-monotone permutations with microscopic oscillations. |
| 24 | explorer_L00_N30 | Hydrodynamic LIS velocity conflated with non-monotone permutation embedding, ignoring that monotone chains cannot traverse reversals. |
| 25 | explorer_L00_N31 | Directed LIS traversal velocity applied to non-monotone permutations with $\Theta(k)$ descents, where monotone paths capture only $2\sqrt{k} \ll k$ points. |
| 26 | explore_merger_L01_N04 | Assumed directed increasing path capacity $(1+\varepsilon/2)2^{-j}k$ in coarse dyadic boxes embeds arbitrary permutations; non-monotone target blocks have LIS length $O(\sqrt{M}) \ll M$, losing 50% to 99.9% of target elements in coarse boxes. |
| 27 | strategy_L02_N01 | Uniform LIS velocity $2\sqrt{C} > 1$ applied to arbitrary non-monotone permutations violates point conservation and order preservation. |
| 28 | strategy_L02_N05 | Applying LIS velocity $2\sqrt{c} > 1$ across transverse coordinate directions violates monotone path directionality and point conservation. |
| 29 | strategy_L02_N07 | Uniform LIS embedding mechanics applied along non-monotone paths violate permutation order constraints. |
| 30 | strategy_L03_N02 | Continuous marked Poisson renewal under discrete buffering $\Delta \ge 1$ has provably subcritical effective traversal velocity $v_{\mathrm{eff}} = \frac{2}{2+\Delta}\sqrt{1+4\varepsilon} \le 0.7303 < 1.0$ at $\varepsilon=0.05$, producing net negative drift. |
| 31 | strategy_L03_N03 | Proposition 6.2 claims continuous traversal velocity $v_{21} = \sqrt{1+4\varepsilon} > 1.0$ for repeated-21, conflating peak cut-flux with actual traversal rate; in W44, empirical drift is $c_{21} \approx 0.941 < 1.0$ (leaving a capacity deficit of $-12.5$ points at $a_{\min}=960$), and under discrete buffering effective velocity collapses to $v_{\mathrm{eff}} \le 0.7303 < 1.0$. |
| 32 | explorer_r2_L00_N20 | Theorem 3.1 commits a category error by applying Logan-Shepp / Vershik-Kerov LIS velocity $v = 2\sqrt{C} > 1$ to non-monotone quasirandom permutations with $\sim k/2$ descents; when order preservation is enforced in a ribbon of width $k^{-1/2}$, the acceptance window shrinks to $O(1/k)$ and forward velocity collapses to $v_{\mathrm{eff}} \le 0.35 \ll 1.0$ (embedding only $34.8\%$ of elements, $0/20$ full successes). |
| 33 | explorer_r2_L00_N26 | Conflates 2D northeast LIS velocity ($2\sqrt{C} > 1$) with non-monotone permutations where interleaved Dilworth chains require southeast steps ($\Delta X > 0, \Delta Y < 0$) with $>95\%$ vertical span overlap, violating chain monotonicity and point conservation. |
| 34 | strategy_r2_L03_N04 | Claiming a factor-of-4 spatial velocity gain $2\sqrt{C}/C = 4.0$ from LIS for 2D spatial non-local traversal (Risky Lemma 4) fails because LIS applies strictly to northeast monotone chains; non-monotone permutations with $\approx k/2$ descents require vertical rank order preservation, forcing Cauchy-Schwarz dilation $\mathbb{E}[X_k] \ge 3.636 > 1.0$ or $12.5\%$ to $45.12\%$ rank inversions. |
| 35 | explorer_r3_L00_N00 | Logan-Shepp / Vershik-Kerov LIS velocity $2\sqrt{C} > 1$ applied to coarse non-monotone dyadic blocks with $\approx k/2$ descents, capturing only $O(\sqrt{k})$ points and violating point conservation. |
| 36 | explorer_r3_L00_N06 | Theorem 9 asserts wavefront velocity $v = 2\sqrt{C} > 1$ on generic permutations, but exact order preservation collapses greedy point selection ($\mathbb{E}[X_{100}] \approx 2.9 \times 10^5 \gg 1.0$, 0/50 trials complete in $[0, 1]$). |
| 37 | N16 (Level 0) | Monotone LIS velocity $v = 2\sqrt{C} > 1$ applied to non-monotone oscillating trajectories $\gamma_\pi(s)$ |
| 38 | N23 (Level 0) | Conflates monotone LIS capacity $2\sqrt{\mu}$ with universal pattern embedding; random point sets fail to embed $21^{\oplus 10}$ in 36.7% of trials |
| 39 | N24 (Level 0) | Applies macroscopic Logan-Shepp / Vershik-Kerov LIS velocity $v = 2\sqrt{C} > 1$ to microscopic quasirandom runs (mean length 2.50, 90% of runs length $\le 3$), where Cauchy-Schwarz forces $\mathbb{E}[X_k] \ge 3.636 > 1.0$ |
| 40 | explore_merger_r3_L01_N02 | Conflating monotone LIS capacity $2\sqrt{\mu}$ with universal subpattern capacity: Poisson point sets of size $N=140$ fail to contain alternating pattern $21^{\oplus 10}$ in $38\%$ to $53.3\%$ of trials, so simultaneous mesoscopic block containment vanishes as $(1 - 0.38)^{2^{j^*}} \to 0$. |
| 41 | explore_merger_r3_L01_N09 | Applying monotone LIS velocity $v = 2\sqrt{C} > 1$ along oscillating generic trajectories in Proposition 5.3 commits a category error: monotone paths capture only $2\sqrt{k} \ll k$ points on generic targets, while terminal blocks of size $m = \Theta(\varepsilon k)$ face 0% completion ($\mathbb{E}[X_m] \ge 4.7 \gg 1.0$). |
| 42 | explore_merger_r3_L01_N11 | Theorem 5 overclaims that $c_{21} = 1.0$ is proved via undefined 'local transversal exchange' along the LIS chain; an LIS chain contains strictly increasing coordinates and zero descents, so pairing points along LIS cannot produce $21^{\oplus m}$ without modifying the fixed Poisson host point set. |
