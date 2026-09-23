# Diagonal Ribbon Domain Inversion Collapse

Type: observation
Confidence: high
Source: Candidates N25, N30 (Round 3 Level 0)
Relevant to: Multi-track corridor routing, laminar diagonal ribbons, multi-chain embeddings, 2D order preservation.

## Statement
Assigning interleaved sub-patterns or multi-chain components to parallel diagonal corridors (e.g. $|y - x - \delta_j| \le w$) tightly couples physical $x$-coordinates to $y$-coordinates ($x \approx y - \delta_j$). For target permutations with interleaved values across domain segments—such as $\pi = (1, 3, 5, \dots, 2, 4, 6, \dots)$ or $21^{\oplus (k/2)}$—this coupling forces an $85\%$ to $100\%$ domain inversion between elements in adjacent chains ($x_{k/2} \gg x_{k/2+1}$). Conversely, enforcing domain order by sorting $x$-coordinates across chains (e.g., $x(C_1, r) < x(C_2, s)$ for $r \le s$) completely destroys value interleaving, embedding the identity permutation $\operatorname{id}_k$ with 0 inversions rather than the intended target pattern.

## Evidence
1. **Geometric Coupling Breakdown**: In Candidate N25 (Theorem 7), two tracks $T_1$ with offset $\delta_1 = 0$ (values $\le k/2$) and $T_2$ with offset $\delta_2 = 0.85$ (values $> k/2$) enforce $x \approx y$ on $T_1$ and $x \approx y - 0.85$ on $T_2$. When embedding $\pi = (1, 3, \dots, 2, 4, \dots)$, the element at index $k/2$ has value near $1.0$, giving $x_{k/2} \ge 0.925$. The subsequent element at index $k/2+1$ has value near $0.0$, giving $x_{k/2+1} \le 0.075$. Across 100% of simulation runs, $x_{k/2} > x_{k/2+1}$, producing an 85% domain inversion that destroys order isomorphism.
2. **Domain Sorting Symmetrization Collapse**: In Candidate N30, to eliminate domain inversions, the embedding rule mandated $x(C_1, r) < x(C_2, s)$ whenever $r \le s$. Testing this rule on interleaved patterns of length $2m$ demonstrated that points were ordered strictly as $(x_1, y_1), (x_2, y_2), \dots$ with $x_1 < x_2 < \dots < x_{2m}$ and $y_1 < y_2 < \dots < y_{2m}$, successfully embedding only the monotonic identity permutation $\operatorname{id}_{2m}$. On target permutations with non-zero descent count, the embedded pattern had 0 inversions, failing pattern matching in 100% of trials.

## Implications
- Demonstrates a fundamental topological obstacle for diagonal ribbon / multi-track parallel routing: parallel ribbons can only embed patterns where horizontal and vertical orders are mutually compatible (concordant).
- Interleaved permutations require discording horizontal and vertical rankings, which creates an irreconcilable conflict between diagonal localization and domain monotonicity.

## Caveats
- Does not affect single monotone chains where $x$ and y are naturally co-increasing. It is specific to multiple interleaved chains or non-monotone target permutations.
