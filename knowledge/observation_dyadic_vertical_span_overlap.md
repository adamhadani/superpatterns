# Dyadic Vertical Span Global Overlap on Non-Monotone Permutations

Type: observation
Confidence: high
Source: Candidates 0, 1, 2, 4, 6, 7, 9, 10, 11, 15 (Level 0 falsers); Candidates L03_N02, L03_N03 (Level 3 falsers); Candidate N20 (Round 3 Level 0); Candidates explore_merger_r3_L01_N02, explore_merger_r3_L01_N08, explore_merger_r3_L01_N14, explore_merger_r3_L01_N15 (Round 3 Level 1)
Relevant to: Multiscale dyadic chaining, spatial decomposition, discretization penalty bounds.

## Statement
For general, alternating, or uniform random permutations $\pi \in S_k$, the vertical range spans $h_{j,m} = \max_{t/k \in I_{j,m}} \pi(t)/k - \min_{t/k \in I_{j,m}} \pi(t)/k$ on dyadic intervals $I_{j,m} = [(m-1)2^{-j}, m 2^{-j}]$ do not have disjoint projections. Instead, they satisfy:
$$\sum_{m=1}^{2^j} h_{j,m} = \Theta(2^j) \gg 1.$$
Consequently, $\sum_{m=1}^{2^j} \sqrt{h_{j,m}} = \Theta(2^j)$, and the boundary discretization penalty across scale $j$ interfaces scales as $P_j = \Theta(2^{j/2} k)$ or $\Theta(k)$ rather than decaying as $O(2^{-j/2} k)$.

## Evidence
1. Rigorous testing on $S_{4096}$: For uniform random permutations, at scale $j=1$ (2 intervals) $\sum h = 1.999$; at scale $j=6$ (64 intervals) $\sum h = 62.01$; at scale $j=10$ (1024 intervals) $\sum h = 615.27 \gg 1$.
2. For alternating permutations $\pi = (1, k, 2, k-1, \dots)$ at $k=1024$, at scale $j=8$, $\sum h_{j,m} = 128.50$, violating the claimed bound $\le 2$ by a factor of $64\times$.
3. Candidate 11 falsification proved that active Haar energy scales as $\Theta(2^{-j})$ (rather than $2^{-2j}$) across $\Theta(2^j)$ non-monotone interfaces, giving cumulative interface penalty $\sum_j \Theta(k) = \Theta(k \log k)$.
4. The only permutations where $\sum_{m=1}^{2^j} h_{j,m} \le 1$ holds are strictly monotone permutations.
5. Mesoscopic cluster and dyadic block testing (Level 3 falsers L03_N02, L03_N03): Partitioning uniform random permutations into horizontal clusters of size $b = \Omega(1/\varepsilon)$ (e.g. $b \in \{10, 20\}$) across $k \in \{100, 500, 1000\}$ yielded exactly $0.00\%$ disjoint vertical value spans (0 out of 18,200 adjacent cluster pairs tested), with average vertical span overlap between adjacent clusters of $96.4\%$ to $98.5\%$. Similarly, terminal horizontal dyadic blocks at stopping scale $j_{\mathrm{stop}}$ have individual vertical spans $h \ge 0.9948$ at $k=1000$ and $0.9982$ at $k=4000$, proving that horizontal spatial partitioning provides zero vertical rank decoupling.
6. Dyadic Grid Line Perimeter and Boundary Buffer Scaling (Candidate N20, Round 3 Level 0): In 2D dyadic decompositions, the total grid line perimeter across scale $j$ is $2(2^j - 1) = \Theta(2^j)$. Placing coordinate separation buffers of width $\delta_j \ge 1/k$ along all boundary interfaces consumes $\Theta(2^j k)$ Poisson points per scale, growing exponentially with $j$ rather than decaying. Furthermore, an algebraic exponent error in boundary penalty claims $n_0 \cdot \delta_j = (C k^2) \cdot O(2^{-j/2} k^{-1/2}) = O(2^{-j/2} k^{3/2})$, which carries an unabsorbed $\sqrt{k}$ factor exceeding the gross surplus $2\varepsilon k$ by $\Theta(\sqrt{k})$ ($31.6\times$ at $k=1000$).
7. **Round 3 Level 1 Spatial Overlap and Coarse Interface Buffer Count (Candidates N02, N08, N14, N15)**:
   - Target elements in horizontal blocks of width $w = 2/(\varepsilon k)$ have mean vertical span $0.9522$ ($95.2\%$ of $[0, 1]$, $23.8\times$ box height), with $0/1000$ blocks localized within height $w$ (N02).
   - In generic permutations of length $k=1000$, adjacent blocks of size $b=160$ exhibit $99.02\%$ vertical span overlap and $12,880.9$ cross-inversions per pair ($50.32\%$ inverted), causing renewal collapse (mean horizontal span $2.9 \times 10^5 \gg 1.0$) (N08).
   - Coarse interface count fallacy: at $\varepsilon = 0.05$ ($j^* = 12$), the $\sum_{j=1}^{12} (2^j - 1) = 8,178$ coarse interfaces require $16,356$ buffer points (with $\Delta=2$), which overwhelms the continuous surplus $2\varepsilon k = 100$ at $k=1000$ by $163.5\times$ (N14).
   - Sum of dyadic vertical spans scales as $\sum_{m=1}^{2^j} h_{j,m} = \Theta(2^j) \gg 1$, refuting vertical disjointness across dyadic spatial boxes and destroying non-crossing multi-scale chaining (N15).

## Implications
Any proof route relying on dyadic spatial partitioning to achieve geometric decay of boundary discretization penalties $P_j = O(2^{-j/2} k)$ fails for general permutations. Cumulative boundary discretization penalties sum to $\Theta(k^{3/2})$ or $\Theta(k \log k)$, massively overpowering the $2\varepsilon k$ hydrodynamic surplus.

## Caveats
Holds whenever permutations possess high-frequency non-monotone oscillations. Permutations of bounded total variation $V(\pi) = O(1)$ or structured monotone inflations can satisfy $\sum h_{j,m} = O(1)$, but such classes form a vanishingly small fraction of $S_k$.
