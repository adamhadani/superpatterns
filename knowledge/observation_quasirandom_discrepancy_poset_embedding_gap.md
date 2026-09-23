# Quasirandom Discrepancy Poset Embedding Gap

Type: observation
Confidence: medium
Source: explorer_r3_L00_N01, explorer_r3_L00_N02 (Round 3 Level 0)
Relevant to: Proof strategies attempting to derive poset embedding, LIS containment, or pattern containment from macroscopic Kolmogorov-Smirnov discrepancy or graphon convergence.

## Statement
Macroscopic Kolmogorov-Smirnov discrepancy $|F_n(x, y) - xy| \le \varepsilon$ provides no non-trivial lower bound on the longest increasing subsequence (LIS) or on pattern containment of non-monotone permutations. Specifically, a deterministic point set formed by an $M \times M$ antidiagonal grid of clusters in $[0, 1]^2$ achieves Kolmogorov-Smirnov discrepancy $\le 1/M \le \varepsilon$, yet has longest increasing subsequence bounded by $\operatorname{LIS} \le 2M - 1$, independent of total point count $N$.

## Evidence
In `explorer_r3_L00_N01` and `explorer_r3_L00_N02`, candidates attempted to embed target permutations into point sets certified by discrepancy bounds. For $M=10$ and $\varepsilon = 0.1$, the antidiagonal block construction yields discrepancy $\le 0.10$ with $\operatorname{LIS} \le 19 \ll k$, failing to contain even monotone permutations of length $k=1000$, let alone generic or alternating permutations.

## Implications
Graphon regularity, quasirandomness, and continuous 2D discrepancy metrics control macroscopic area densities but fail to preserve microscopic 1D and 2D poset order relations. Any strategy asserting that discrepancy $\varepsilon \to 0$ guarantees sub-pattern containment without fine-scale order-preserving control suffers from an unbridgeable regularity gap.

## Caveats
Discrepancy bounds do constrain coarse block distributions, but converting coarse block density into order-isomorphic embeddings requires microscopic rank control, which re-introduces Poisson void starvation or discrete buffer penalties.
