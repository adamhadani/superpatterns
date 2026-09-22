# Baik-Deift-Johansson (1999) Tracy-Widom Limit for Longest Increasing Subsequences

Type: reference
Confidence: high
Source: Candidates 17, 19, 20, 21 (Level 0)
Relevant to: LIS fluctuations, finite-size boundary lag, Tracy-Widom mean shift, multiscale penalty scaling.

## Bibliographic Info
- Authors: Jinho Baik, Percy Deift, Kurt Johansson
- Title: On the distribution of the length of the longest increasing subsequence of random permutations
- Year: 1999
- ArXiv/DOI: J. Amer. Math. Soc. 12 (1999), 1119-1178. DOI: 10.1090/S0894-0347-99-00307-0
- Theorem/Lemma Number: Theorem 1.1
- Verified via web search: yes

## Key Result
For $\sigma_N \sim \operatorname{Uniform}(S_N)$ (or for a Poisson point process of intensity $\lambda$ in a rectangle of area $A$ with $N = \lambda A$), the longest increasing subsequence $\operatorname{LIS}(\sigma_N)$ satisfies the Tracy-Widom GUE limit theorem:
$$\lim_{N \to \infty} \Pr\left( \frac{\operatorname{LIS}(\sigma_N) - 2\sqrt{N}}{N^{1/6}} \le s \right) = F_{\mathrm{TW}}(s) = \exp\left( -\int_s^\infty (x - s) q(x)^2 \, dx \right),$$
where $q(x)$ is the Hastings-McLeod solution to the Painlevé II differential equation $q'' = 2q^3 + x q$.
In particular, the non-asymptotic expected value exhibits a negative finite-size shift:
$$\mathbb{E}[\operatorname{LIS}(\sigma_N)] = 2\sqrt{N} - c_{\mathrm{TW}} N^{1/6} + O(N^{-1/6}),$$
with $c_{\mathrm{TW}} \approx 1.7711$.

## Hypotheses / Conditions
Applies to uniform random permutations $\sigma_N \in S_N$ or homogeneous Poisson directed paths in $[0, 1]^2$. The scaling exponent $N^{1/6}$ is characteristic of the KPZ universality class.

## How It Applies
1. Explains why empirical LIS surplus at finite $k$ (e.g. $k=100, C=0.26$, $N=2600$) is negative: $2\sqrt{2600} - 1.7711(2600)^{1/6} \approx 101.98 - 6.53 = 95.45 < 100$, producing an empirical deficit of $-4.55$ points.
2. In a multiscale dyadic decomposition, on each interval of length $2^{-j}$ with $L_j = k 2^{-j}$ points, the transverse fluctuation scales as $L_j^{1/3} = k^{1/3} 2^{-j/3}$. Across $2^j$ intervals, the total boundary lag sums to $\sum_{m=1}^{2^j} O(L_j^{1/3}) = \Theta(k^{1/3} 2^{2j/3})$, which grows exponentially in $j$ with ratio $2^{2/3} \approx 1.587 > 1$, reaching $\Theta(k)$ at fine scales.

## Caveats
The result applies strictly to increasing subsequences (monotone paths). It cannot be directly extended to evaluate the number of points acquired when embedding arbitrary non-monotone target permutations.
