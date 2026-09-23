# Pointwise Optimality of Greedy Traversal in Fixed Strips and Lookahead Ineffectiveness

Type: observation
Confidence: high
Source: explorer_r2_L00_N25 (Level 0)
Relevant to: Greedy scanning, multi-thread lookahead, fixed horizontal rank strips, renewal traversal velocity

## Statement
When target elements $j = 1, \dots, k$ are pre-assigned to fixed horizontal rank strips $B_{t+\pi(j)} = [0, 1] \times [y_j^-, y_j^+]$, the greedy arrival sequence $g_j = \min\{x \in B_{t+\pi(j)} : x > g_{j-1}\}$ (with $g_0 = 0$) is the absolute pointwise lower bound of all valid arrival coordinates. For any sequence of valid embedding points $(x_1, \dots, x_k)$ satisfying $x_j \in B_{t+\pi(j)}$ and $x_1 < x_2 < \dots < x_k$, we have:
$$x_j \ge g_j \quad \text{for all } j \in [k].$$
In particular, $x_k \ge g_k$. Consequently, no lookahead policy of any depth $\Delta \ge 1$ within fixed strip assignments can ever achieve a smaller horizontal completion coordinate than the greedy traversal. If greedy single-thread traversal is subcritical ($\mathbb{E}[g_k] = 8/(1+4\varepsilon) \approx 6.67 \gg 1.0$), lookahead search within fixed strips cannot accelerate forward progress or prevent Poisson starvation.

## Evidence
- Mathematical proof by induction: For $j = 1$, $x_1 \ge \min\{x \in B_{t+\pi(1)} : x > 0\} = g_1$. Assuming $x_{j-1} \ge g_{j-1}$, since $x_j > x_{j-1} \ge g_{j-1}$ and $x_j \in B_{t+\pi(j)}$, we have $x_j \in \{x \in B_{t+\pi(j)} : x > g_{j-1}\}$, which implies $x_j \ge \min\{x \in B_{t+\pi(j)} : x > g_{j-1}\} = g_j$. Thus $x_j \ge g_j$ holds for all $j \in [k]$.
- Candidate explorer_r2_L00_N25 proposed that a lookahead policy of depth $\Delta = O(1/\varepsilon)$ could achieve effective velocity $v_{\mathrm{eff}} > 1.0$ while retaining fixed horizontal tracks.
- Python simulations confirmed that across 500 trials, the greedy sequence achieved the minimum coordinate at every step, and lookahead policies yielded identical or strictly larger completion coordinates $x_k \ge g_k$.
- Because each strip of height $1/(2k)$ has Poisson rate $\lambda = (1/8+\varepsilon/2)k$, $\mathbb{E}[g_k] = k/\lambda \approx 8.0$, meaning $g_k > 1.0$ almost surely (succeeding with probability $\le \exp(-1.204k) \le 10^{-52}$ at $k=100$). Since $x_k \ge g_k$, all lookahead policies fail with probability $\ge 1 - 10^{-50}$.

## Implications
- To achieve supercritical traversal velocity $v_{\mathrm{eff}} > 1.0$ at host density $C = 1/4+\varepsilon$, an embedding strategy cannot restrict target elements to fixed horizontal strips.
- Lookahead can only accelerate forward traversal if it is paired with flexible spatial allocation (allowing elements to dynamically select among multiple alternative strips or 2D regions), which re-introduces the lookahead rank-inversion dilemma.

## Caveats
- This pointwise lower bound applies strictly when the sequence of spatial regions $(B_{t+\pi(j)})_{j=1}^k$ is fixed in advance for each thread. It does not apply to dynamic programming across multiple concurrently branchable threads where thread identity can be switched at valid junction points.
