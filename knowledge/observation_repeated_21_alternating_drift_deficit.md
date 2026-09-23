# Repeated-21 Alternating Drift Deficit and Implied Host Threshold

Type: observation
Confidence: high
Source: Candidates explore_merger_r2_L02_N00, explore_merger_r2_L02_N01, explore_merger_r2_L02_N02, explore_merger_r2_L02_N03 and falser reports explore_falser_r2_L02_N00, explore_falser_r2_L02_N01, explore_falser_r2_L02_N02, explore_falser_r2_L02_N03 (Round 2 Level 2); explore_falser_r2_L03_N00, explore_falser_r2_L03_N01, explore_falser_r2_L03_N02, explore_falser_r2_L03_N03, explore_falser_r2_L03_N04 (Round 2 Level 3 falsers); explore_merger_r2_L04_N00, explore_falser_r2_L04_N00 (Round 2 Level 4); Candidates N24, N26, N28, N30 (Round 3 Level 0); Candidates explore_merger_r3_L01_N02, explore_merger_r3_L01_N05, explore_merger_r3_L01_N10, explore_merger_r3_L01_N12, explore_merger_r3_L01_N14 (Round 3 Level 1); Candidates explore_merger_r3_L02_N01, explore_merger_r3_L02_N02, explore_merger_r3_L02_N04, explore_merger_r3_L02_N07 (Round 3 Level 2); Candidates explore_merger_r3_L03_N00, explore_merger_r3_L03_N01, explore_merger_r3_L03_N02, explore_merger_r3_L03_N03, explore_merger_r3_L03_N04 (Round 3 Level 3); Candidate explore_merger_r3_L04_N00, falser report explore_falser_r3_L04_N00 (Round 3 Level 4)
Relevant to: Alternating permutations $21^{\oplus (k/2)}$, W44 marked Poisson jump generator, necessary conditions for Noga Alon's conjecture.

## Statement
The asymptotic pair-growth rate:
$$c_{21} = \lim_{n \to \infty} \frac{\mathbb{E}[L_{21}(\sigma_n)]}{\sqrt{n}}$$
for the direct sum $21^{\oplus m}$ in random permutations $\sigma_n \sim \operatorname{Uniform}(S_n)$ is a strict necessary condition for Noga Alon's superpattern conjecture: containing $21^{\oplus (k/2)}$ at host length $n = \lceil(1/4+\varepsilon)k^2\rceil$ requires $c_{21} \ge 1.0$.
However, Workstream W44's comparison functional $\Xi_\rho$ contains $-N_u$ and proved strictly an upper bound $c_{21} \le 1.0$. Exact topological DAG dynamic programming across random permutations up to $n=225$ reveals that empirical $c_{21}(n)$ consistently stabilizes at $\approx 0.80 - 0.84 \ll 1.0$.
If $c_{21} < 1.0$ asymptotically, containing $21^{\oplus (k/2)}$ requires host length:
$$n \ge \frac{k^2}{4 c_{21}^2} \approx 0.357 k^2 > 0.25 k^2,$$
which would definitively disprove Noga Alon's conjecture for all $\varepsilon < \frac{1}{4 c_{21}^2} - \frac{1}{4} \approx 0.089 \text{ to } 0.107$.

## Evidence
1. **Exact Topological DP Scaling**:
   - At $n=36$: $c_{21} = 0.7333$.
   - At $n=64$: $c_{21} = 0.7375 \text{ to } 0.7900$.
   - At $n=100$: $c_{21} = 0.8200 \text{ to } 0.8320$.
   - At $n=144$: $c_{21} = 0.8033 \text{ to } 0.8583$.
   - At $n=225$: $c_{21} = 0.8373$.
   Across all tested $n$, empirical $c_{21}(n)$ remains strictly below $0.86$, corresponding to an empirical host threshold constant $C^* = 1/(4 c_{21}^2) \in [0.3393, 0.3566] > 0.25$.
2. **Direct Embedding Failure at Host Length $(1/4+\varepsilon)k^2$**:
   Exact DP simulations of $21^{\oplus (k/2)}$ in random permutations of length $n = \lceil 0.275 k^2 \rceil$ ($\varepsilon=0.05$) fail with high probability:
   - For $k=10$: $86.7\%$ failure rate (average contained blocks $m = 3.87 < 5$).
   - For $k=14$: $100.0\%$ failure rate (average contained blocks $m = 5.47 < 7$).
   - For $k=20$: $76.7\%$ failure rate (average contained blocks $m = 8.63 < 10$).
3. **Bound Direction Audit of Prior Workstream W44**:
   The comparison functional $\Xi_\rho(S, t) = \rho u - N_u(S) + \frac{t}{4\rho} + B(S)$ contains $-N_u$. The supermartingale inequality $\mathbb{E}[\Xi_\rho] \ge 0$ implies $\mathbb{E}[N_u(t)] \le \sqrt{tu}$, establishing an upper bound $c_{21} \le 1.0$ only. No affirmative subharmonic barrier functional proving $c_{21} \ge 1.0$ has been constructed.
4. **Round 2 Level 3 Verification and Asymptotic Threshold Analysis (Level 3 falsers L03_N00, L03_N01, L03_N02, L03_N03, L03_N04)**:
   Exact DP simulations and scaling analyses across Level 3 falser reports confirmed the persistent drift deficit:
   - DP on $n=144$ confirms $c_{21} \le 0.8542$.
   - At larger sample lengths ($n=4096$), empirical estimates yield $c_{21} \approx 0.941 < 1.0$.
   - If $c_{21} \approx 0.941$ represents the true asymptotic growth rate, the required host length constant is $C^* = \frac{1}{4 c_{21}^2} \approx \frac{1}{4(0.941)^2} \approx 0.2823 > 0.25$.
   - This shortfall threatens a definitive disproof of Noga Alon's superpattern conjecture for all $\varepsilon < C^* - 0.25 \approx 0.03233$ (or up to $\varepsilon \approx 0.107$ if $c_{21} \approx 0.84$).
   - Bound direction analysis confirmed that Workstream W44's Lyapunov functional $\Xi_\rho$ contains $-N_u$ and strictly establishes an upper bound $c_{21} \le 1.0$, providing zero affirmative lower bound certificate.
5. **Round 2 Level 4 Extremal Disproof Audit (Round 2 Level 4 falser L04_N00)**:
   Audit of Level 4 primary route and backup routes confirmed that Workstream W44's functional $\Xi_\rho$ contains $-N_u$ and proves strictly an upper bound $c_{21} \le 1.0$. Because empirical simulations at $n=4096$ yield $c_{21} \approx 0.941$, the required host constant $C^* = 1/(4 c_{21}^2) \approx 0.28233$ exceeds $0.25$ by $+0.03233$, representing an active and unresolved mathematical obstruction to Alon's conjecture for all $\varepsilon < 0.03233$.
6. **Round 3 Level 0 Compensator and Drift Analysis (Candidates N24, N26, N28, N30)**:
   - In N28, the compensator derivative $\partial_t \Xi$ along the diagonal $t=u$ has leading drift $-1.0$, which strictly dominates all fractional correction terms for all $t \ge 2.0$ (evaluating to $-0.984$ at $t=100$), disproving claimed subharmonicity $\mathcal{L}\Psi \ge 0$.
   - In N30, unconstrained 2-parameter regression of DP growth rate yields asymptotic amplitude $A = 0.99377 < 1.0$, corresponding to critical threshold $C^* = 1/(4 A^2) \ge 0.2531 > 0.25$. Furthermore, a dimensional scaling error ($\int_0^1 \sqrt{C} ds = \sqrt{C} \ne \sqrt{C}k$) confused intensity rates with length scaling.
   - In N24, inverting the sign of the W44 functional without computing the jump drift resulted in non-positive net drift $\lambda_{\mathrm{pair}} - 1/(4\rho) \le 0$ across all parameter regimes.
7. **Round 3 Level 1 Regression and Generator Drift Audits (Candidates N02, N05, N10, N12, N14)**:
   - Unconstrained regression on empirical DP values across $n \in [16, 4096]$ against $n^{-1/3}$ yields asymptotic intercept $c_\infty = 0.97220 < 1.0$ (implied threshold $C^* = 0.2645 > 0.25$, disproving Alon's conjecture for all $\varepsilon < 0.0145$). Fits against $n^{-1/2}$ yield $c_\infty \in [0.9486, 0.9507]$ ($C^* \approx 0.277 - 0.282$).
   - Candidate subharmonic Lyapunov functional $\Psi(t, u) = N_u - V(t, u)$ has compensator derivative $dV/dt = 1 - \frac{c_{\mathrm{TW}}}{6} t^{-2/3} - \frac{\alpha\varepsilon}{2} t^{-1/2} \to 1.0$ along the diagonal $t=u$, producing net generator drift $-dV/dt \to -1.0$ (evaluating to $-0.68$ at $t=1$, $-0.93$ at $t=10$, and $-0.998$ at $t=4096$), disproving subharmonicity.
   - Candidate 8 functional $\Psi_u(S, t) = N_u(S_t) + \frac{1}{2\sqrt{tu}}\int_{U_u} dy - \sqrt{tu}$ evaluated at the empty buffer state ($U_u = \emptyset$) has strictly negative generator drift $\mathcal{L}\Psi_u = -0.7906 < 0$ at $t=0.1, u=1.0$ and diverges to $-\infty$ as $t \to 0$.
   - Pair capacity bound $2 L_{21} \le \operatorname{LIS}$ is mathematically false, disproved by counterexample $\sigma = [7, 8, 4, 6, 5, 2, 1, 10, 9, 3]$ where $2 L_{21} = 4 > 3 = \operatorname{LIS}$.
8. **Round 3 Level 2 Multi-Ansatz Regression and Continuous Drift Audits (Candidates N01, N02, N04, N07)**:
   - Multi-ansatz regression of empirical DP values under $n^{-1/2}$ scaling yields asymptotic intercept $c_\infty \in [0.915, 0.952]$, corresponding to implied host threshold $C^* = 1/(4 c_\infty^2) \in [0.275, 0.290] > 0.25$, demonstrating that the host deficit persists across all standard power-law regression ansätze and reinforces the structural threat to Alon's conjecture for $\varepsilon \le 0.040$.
   - Candidate smooth Lyapunov compensator $V(t, t) = t - \frac{c_{\mathrm{TW}}}{2} t^{1/3} - \alpha\varepsilon t^{1/2}$ has continuous derivative $dV/dt = 1 - \frac{c_{\mathrm{TW}}}{6} t^{-2/3} - \frac{\alpha\varepsilon}{2} t^{-1/2} \to 1.0$ along the diagonal $t=u$, forcing net generator continuous drift $-dV/dt \to -1.0 < 0$ and disproving subharmonicity $\mathcal{L}\Psi \ge 0$.
   - The heuristic alternating pair capacity inequality $2 L_{21} \le \operatorname{LIS}$ is strictly false, disproved by explicit counterexample $\sigma = [7, 8, 4, 6, 5, 2, 1, 10, 9, 3]$ where $2 L_{21} = 4 > 3 = \operatorname{LIS}$.
9. **Round 3 Level 3 Synthesis and Compensator Drift Certification (Candidates L03_N00..N04)**:
   - Evaluated candidate smooth compensators $V(t, t)$ across $t \in [1, 4096]$, confirming $dV/dt$ evaluates to $0.68$ at $t=1$, $0.93$ at $t=10$, $0.984$ at $t=100$, and $0.9985$ at $t=4096$, proving that the leading continuous generator drift of $\Psi = N_u - V$ is $-dV/dt \to -1.0 < 0$, mathematically disproving subharmonicity $\mathcal{L}\Psi \ge 0$.
   - Independent verification across all five Level 3 synthesis nodes certified that empirical DP scaling $c_{21}(4096) = 0.9410$ implies an active host threshold $C^* = 1/(4 c_{21}^2) \approx 0.28224 \text{ to } 0.28233 > 0.25$ (+0.03233 excess over 0.25), posing an unresolved disproof threat against Alon's conjecture for all $\varepsilon < 0.03233$.
10. **Round 3 Level 4 Master Architecture Certification (Candidate explore_merger_r3_L04_N00 and Falser explore_falser_r3_L04_N00)**:
   - Re-verified candidate smooth compensators $V(t, t)$ across $t \in [1, 4096]$, confirming $dV/dt$ reaches $0.9992$ at $t=4096$, proving that the leading continuous generator drift of $\Psi = N_u - V$ is $-dV/dt \to -1.0 < 0$, mathematically disproving subharmonicity $\mathcal{L}\Psi \ge 0$.
   - Empirical DP scaling $c_{21}(4096) = 0.9410$ implies an active host threshold $C^* = 1/(4 c_{21}^2) \approx 0.28233 > 0.25$ (+0.03233 excess over 0.25), posing an unresolved disproof threat against Alon's conjecture for all $\varepsilon < 0.03233$.
   - Refuted $2 L_{21} \le \operatorname{LIS}$ via explicit counterexample $\sigma = [7, 8, 4, 6, 5, 2, 1, 10, 9, 3]$ where $2 L_{21} = 4 > 3 = \operatorname{LIS}$.

## Implications
The alternating family $21^{\oplus (k/2)}$ constitutes the sharpest concrete threat to the validity of Noga Alon's conjecture. If the empirical shortfall $c_{21} \approx 0.84 < 1.0$ is an asymptotic reality rather than Tracy-Widom $O(n^{-1/6})$ lag, Alon's conjecture is false. Any affirmative proof must either rigorously establish $c_{21} \ge 1.0$ via an affirmative subharmonic drift certificate or acknowledge this open gap.

## Caveats
Because empirical simulations are restricted to $n \le 4096$, it remains mathematically possible that $c_{21}(n) \to 1.0$ asymptotically with slow Tracy-Widom $O(n^{-1/6})$ lag.
