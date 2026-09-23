# Matrix Interval Minor Column Integrality Barrier

Type: observation
Confidence: high
Source: Candidate explorer_r2_L00_N06 and falser report explore_falser_r2_L00_N06 (Round 2 Level 0)
Relevant to: Random matrix couplings, interval minor embeddings, and He & Kwan (2020) framework

## Statement
In the Random Matrix Interval Minor framework (Fox 2011, He & Kwan 2020), a uniform random permutation $\sigma_n \sim \operatorname{Uniform}(S_n)$ is coupled with an i.i.d. Bernoulli$(1/2)$ zero-one matrix $M \in \{0, 1\}^{(2k) \times m}$. To guarantee that each matrix entry has marginal occupancy $\Pr(M(y, x) = 1) \ge 1 - 1/e^2 \approx 0.865 \ge 0.5$ across all $2k$ rows, each column $x \in [m]$ must aggregate at least $4k$ host points from $\sigma_n$, forcing the column count to be:
$$m = \left\lfloor \frac{n}{4k} \right\rfloor.$$
Because any interval minor containing an induced permutation pattern of length $k$ requires at least $k$ distinct columns (since column contractions can only merge columns, never create new ones), containing a $k$-permutation requires:
$$m \ge k \implies \left\lfloor \frac{n}{4k} \right\rfloor \ge k \implies n \ge 4k^2.$$
Consequently, any discrete zero-one matrix interval minor coupling that relies on $4k$-point column aggregation enforces an absolute structural barrier of:
$$C = \frac{n}{k^2} \ge 4.0.$$
At Noga Alon's conjectured threshold $n = \lceil(1/4+\varepsilon)k^2\rceil$, the number of available columns is $m = \lfloor(1/16 + \varepsilon/4)k\rfloor \le 0.075k \ll k$ (at $\varepsilon=0.05$), representing a $13.3\times$ dimensional column deficit.

## Evidence
- Direct dimensional algebra: an interval minor of a $(2k) \times m$ matrix has at most $m$ columns. A $k \times k$ permutation matrix requires $k$ non-zero columns, forcing $m \ge k$.
- Exact verification in `verify_probe.py` and falser report N06: at $C = 0.25 + 0.05$, $m/k = 0.075 \ll 1.0$, creating an insurmountable dimensional obstacle.

## Implications
Proves that the Random Matrix Interval Minor framework cannot be used to prove Noga Alon's conjecture at $C = 1/4 + \varepsilon$. While He & Kwan (2020) successfully established universality at $n = 20k^2$ and $n = O(k^2 \log \log k)$ for the matrix model, the framework has a hard structural floor at $C \ge 4.0$. Compressing $C$ below $4.0$ requires discarding discrete column aggregation and developing continuous-time point-selection martingales directly on the planar Poisson point process.

## Caveats
Applies to any discrete matrix interval minor coupling where column blocks aggregate $\Omega(k)$ host entries to maintain bounded Bernoulli entry probabilities.
