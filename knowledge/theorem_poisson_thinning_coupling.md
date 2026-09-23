# Poisson Thinning Coupling and De-Poissonization

Type: theorem
Confidence: high
Source: Candidates 0, 1, 2, 3, 4, 5, 6, 7 (Level 0); explore_merger_r3_L04_N00, explore_falser_r3_L04_N00 (Round 3 Level 4)
Relevant to: Transferring pattern containment results from continuous planar Poisson point processes to discrete uniform random permutations.

## Statement
Let $\Pi_{n_0}$ be a homogeneous Poisson point process on $[0, 1]^2$ with intensity $n_0 = (1/4 + \varepsilon/2)k^2$. Let $n = \lceil(1/4 + \varepsilon)k^2\rceil$, and let $\sigma_n \sim \operatorname{Uniform}(S_n)$.
If an event $E_{\mathrm{host}}$ on $\Pi_{n_0}$ certifies that every $\pi \in S_k$ is embedded as an induced sub-pattern in $\Pi_{n_0}$, then:
$$\Pr\left(\sigma_n \text{ fails to contain all } \pi \in S_k\right) \le \Pr\left(E_{\mathrm{host}}^c\right) + \exp\left( - \frac{\varepsilon^2 k^2}{8(1/4+\varepsilon)} \right).$$
In particular, if $\Pr(E_{\mathrm{host}}^c) \le \exp(-\Omega(\varepsilon^2 k)) = o(1)$, then $\sigma_n$ contains every $\pi \in S_k$ simultaneously with probability $1 - o(1)$.

## Proof
Let $(U_i, V_i)_{i \ge 1}$ be an infinite sequence of i.i.d. uniform random points in $[0, 1]^2$. Let $M \sim \operatorname{Poisson}(n_0)$ be independent of $(U_i, V_i)$.
The point set $\Pi_{n_0} = \{(U_i, V_i) : 1 \le i \le M\}$ is a homogeneous Poisson point process of intensity $n_0$.
The point set $S_n = \{(U_i, V_i) : 1 \le i \le n\}$ standardizes to a uniform random permutation $\sigma_n \sim \operatorname{Uniform}(S_n)$.
On the event $\{M \le n\}$, $\Pi_{n_0} \subseteq S_n$.
Because permutation pattern containment is monotone under point addition (adding points to a planar point set cannot destroy an existing induced sub-pattern), any pattern embedded in $\Pi_{n_0}$ is simultaneously embedded in $\sigma_n$.
By the standard Poisson Chernoff upper tail bound:
$$\Pr(M > n) = \Pr\left(\operatorname{Poisson}(n_0) > n\right) \le \exp\left( - \frac{(n - n_0)^2}{2 n} \right) \le \exp\left( - \frac{(\varepsilon k^2 / 2)^2}{2(1/4 + \varepsilon)k^2} \right) = \exp\left( - \frac{\varepsilon^2 k^2}{8(1/4+\varepsilon)} \right).$$
Taking a union bound over $E_{\mathrm{host}}^c$ and $\{M > n\}$ yields the result.

## Hypotheses / Conditions
- Poisson intensity $n_0 < n$.
- Uniform planar distribution on $[0, 1]^2$.
- Sub-pattern containment is monotone under point addition.

## How It Applies
Allows all geometry, large deviations, and concentration arguments to be conducted in the continuous planar Poisson model $\Pi_{n_0}$, where spatial independence holds across disjoint regions, and transfers the result to discrete permutations $\sigma_n \in S_n$ with negligible error $\exp(-\Omega(\varepsilon^2 k^2))$.

## Caveats
Requires $n_0$ strictly below $n$ (specifically $n - n_0 = \Omega(\varepsilon k^2)$) to ensure the Chernoff tail is exponentially small.
