# Intra-Column Horizontal Sorting Collapse in Mesoscopic Slabs

Type: observation
Confidence: high
Source: Candidates N19, N22 (Round 3 Level 0)
Relevant to: Mesoscopic column clustering, vertical ribbon decomposition, cross-slab synchronization.

## Statement
In mesoscopic decomposition schemes where the unit square is partitioned into $K = \Theta(\varepsilon k)$ vertical columns of width $w = 4/(\varepsilon k)$ (or where targets are clustered into mesoscopic horizontal bins of size $b = \Omega(1/\varepsilon)$), points assigned to distinct vertical ribbons or clusters within the same column have mutually independent horizontal coordinates.

For $m$ target points residing in vertically separated clusters within a single column, the probability that their Poisson horizontal coordinates appear in the exact prescribed order is:
$$\mathbb{P}(\text{horizontal sorting}) = \frac{1}{m!}.$$
For moderate cluster depths (e.g. $m = 80$ at $\varepsilon = 0.05$), $1/80! \approx 1.39 \times 10^{-119}$ per column. Across all $k/b$ columns, the global horizontal ordering probability decays superexponentially as $(1/m!)^{k/b} \le 10^{-2000}$, creating an insurmountable intra-column horizontal desynchronization barrier.

## Evidence
1. **Factorial Horizontal Sorting Probability**:
   Conditioned on falling into a vertical column of width $w$, Poisson arrival horizontal coordinates $X_1, X_2, \dots, X_m$ are independent and identically distributed uniformly in $[x_0, x_0 + w]$. If the target pattern requires these $m$ points to follow a specific permutation order along the $x$-axis, the realization succeeds with probability exactly $1/m!$.
2. **Subdivision Dilemma**:
   Attempting to eliminate this disorder by subdividing each mesoscopic column into $m$ disjoint vertical sub-strips of width $w/m \le 1/k$ shrinks the sub-strip area to $A \le 1/k^2$. At host intensity $n_0 = (1/4 + \varepsilon)k^2$, the expected Poisson count per sub-strip drops to $\mu = (1/4 + \varepsilon) < 1.0$ (e.g. $\mu = 0.275$ at $\varepsilon=0.05$). The probability that a sub-strip is empty is $e^{-\mu} \approx 76.0\%$, triggering severe Poisson void starvation and renewal collapse.
3. **Entropy Balance**:
   The entropy cost of specifying the permutation of $m$ points across $K$ columns is $K \ln(m!) \approx K m \ln m = k \ln m$ nats. For $k=1000$ and $m=80$, this entropy deficit is $\approx 4382$ nats, which cannot be compensated by any $O(\varepsilon k)$ Poisson excess margin.

## Implications
Vertical stratification without microscopic horizontal coordinate synchronization cannot embed permutations that possess non-trivial intra-column horizontal ordering requirements. Decoupling horizontal clustering from vertical ordering inevitably incurs either a $1/m!$ factorial sorting collapse or subcritical Poisson void starvation.

## Caveats
Applies to schemes that attempt to assign multiple target points to the same horizontal interval without enforcing micro-corridor separation.
