# Janson Covariance Overlap Explosion on Highly Symmetric and Alternating Patterns

Type: observation
Confidence: medium
Source: explorer_r2_L00_N12 (Level 0)
Relevant to: Janson inequality, correlation inequalities, bufferless permutation embedding, probabilistic container methods

## Statement
In attempts to prove universal permutation containment via the Janson inequality without buffer zones, assuming that permutation overlap counts decay factorially as $1/\ell!$ fails drastically for structured or periodic permutations. For alternating permutations such as $\pi = 21^{\oplus m}$ (the direct sum of length-2 inversions), the number of distinct order-isomorphic sub-permutations on an overlap of length $\ell$ is governed by the Fibonacci sequence $F_{\ell+1} \approx 1.618^\ell \ll \ell!$. Consequently, the Janson covariance dependency sum $\Delta = \sum_{A \sim B} \Pr(A \cap B)$ explodes by more than $10^{14}$ times above the factorial prediction at $\ell = 20$. Furthermore, the true Janson concentration exponent scales linearly as $\Theta(k)$, not quadratically as $\Omega(k^2)$, leading to a massive divergence of $+5412$ nats in the union bound over $k!$ permutations at $k = 1000$.

## Evidence
- Candidate explorer_r2_L00_N12 posited that dependencies between embedding events decay as $1/\ell!$ uniformly across all permutations.
- Computational and algebraic analysis of alternating patterns $\pi = 21^{\oplus m}$ reveals that sub-permutations must consist of disjoint or adjacent pairs, exactly enumerated by the Fibonacci recurrence $a_\ell = a_{\ell-1} + a_{\ell-2}$, giving $F_{21} = 10946$ distinct sub-patterns at $\ell = 20$ compared to $20! \approx 2.43 \times 10^{18}$, an explosion factor of $20! / F_{21} \approx 2.2 \times 10^{14}$ in overlap count.
- Calculation of Janson exponent $\mu^2 / (\mu + \Delta)$ shows linear scaling $\Theta(k) \approx 498$ nats, while $\ln(k!) \approx 5910$ nats at $k = 1000$, resulting in union bound failure: $\ln(k!) - \mu^2/(\mu+\Delta) \approx +5412 > 0$.
- In half-domain bufferless gluing, net drift is strictly negative: $0.6534 < 0.6931$ nats per element.

## Implications
- Any Janson-based probabilistic embedding strategy cannot rely on generic factorial suppression $1/\ell!$ of overlap covariances across all $k!$ permutations. Highly repetitive, periodic, or alternating patterns have exponentially fewer sub-patterns, resulting in severe covariance clustering and destroying exponential concentration.
- Bufferless gluing across domain halves cannot maintain required positive drift without explicit buffer zones or separation margins.

## Caveats
- Random or quasi-random permutations with no periodic structure have larger varieties of sub-patterns and less covariance concentration, but universal containment requires the bound to hold for *all* $\pi \in S_k$, including the worst-case alternating permutations.
