# Erdős-Szekeres Vacuity of Bounded Monotone Subsequence Quasirandom Classes

Type: observation
Confidence: high
Source: explore_falser_r3_L00_N14 (Round 3 Level 0)
Relevant to: Quasirandom permutation class definitions, two-tier architectures, trichotomy decompositions.

## Statement
Defining a target quasirandom class $Q_k(\varepsilon)$ by imposing simultaneous upper bounds on both the longest increasing subsequence ($\operatorname{LIS}(\pi) \le M_1$) and the longest decreasing subsequence ($\operatorname{LDS}(\pi) \le M_2$) produces a strictly empty set ($Q_k(\varepsilon) = \emptyset$) for all $k > M_1 M_2$, by the Erdős-Szekeres Theorem ($\operatorname{LIS}(\pi) \cdot \operatorname{LDS}(\pi) \ge k$). In particular, setting $M_1 = M_2 = 4/\varepsilon$ renders $Q_k(\varepsilon)$ completely vacuous for all $k > 16/\varepsilon^2$ ($k > 6400$ at $\varepsilon = 0.05$).

## Evidence
1. **Erdős-Szekeres Theorem (1935)**: For any sequence or permutation $\pi \in S_k$, $\operatorname{LIS}(\pi) \cdot \operatorname{LDS}(\pi) \ge k$. Consequently, $\max(\operatorname{LIS}(\pi), \operatorname{LDS}(\pi)) \ge \lceil\sqrt{k}\rceil$.
2. **Candidate N14 Strategy Definition**: In candidate `explorer_r3_L00_N14`, the quasirandom subclass $Q_k(\varepsilon)$ was defined as the set of permutations with $\operatorname{LIS}(\pi) < 4/\varepsilon$ and $\operatorname{LDS}(\pi) < 4/\varepsilon$, claiming that generic permutations have bounded monotone runs and can be compressed.
3. **Rigorous Counter-Verification**: For any $\varepsilon \in (0, 1)$, if $k > 16/\varepsilon^2$, every permutation $\pi \in S_k$ satisfies:
   $$\max(\operatorname{LIS}(\pi), \operatorname{LDS}(\pi)) \ge \sqrt{k} > \frac{4}{\varepsilon}$$
   Therefore, no permutation in $S_k$ can satisfy both conditions simultaneously. For $\varepsilon = 0.05$, $16/\varepsilon^2 = 6400$; thus for any $k \ge 6401$, $|Q_k(0.05)| \equiv 0$. The claimed quasirandom class contains zero target permutations.

## Implications
Strategies that attempt to isolate "quasirandom" permutations by capping both increasing and decreasing subsequence lengths to $O(1/\varepsilon)$ are fundamentally flawed: the defined class is mathematically empty in the asymptotic regime $k \to \infty$. Any two-tier or trichotomy architecture relying on such definitions leaves 100% of target permutations unassigned or classified into undefined residuals.

## Caveats
Quasirandomness for permutations should be defined via discrepancy, cycle structure, or pair correlation (e.g. $L_2$ discrepancy or rank-window counts), not via simultaneous sub-linear upper bounds on both $\operatorname{LIS}$ and $\operatorname{LDS}$.
