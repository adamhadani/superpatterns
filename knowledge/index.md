# Knowledge Index

## Failed Approach Categories (97 entries in 7 categories)
| Pattern | Count | Summary | File |
|---------|-------|---------|------|
| vertical_span_overlap | 11 | Vertical range spans across dyadic intervals sum to $\Theta(2^j) \gg 1$, causing discretization penalties to grow to $\Theta(k \log k)$ or $\Theta(k^{3/2})$ instead of decaying geometrically | category_vertical_span_overlap.md |
| entropy_concentration_sign_inversion | 18 | Tree description entropy rate $\kappa \ge 1.0$ strictly exceeds $O(\varepsilon^2)$ concentration margin, causing union bound failure probability to diverge exponentially to $+\infty$ | category_entropy_concentration_sign_inversion.md |
| lis_velocity_nonmonotone_mismatch | 25 | Applying Logan-Shepp / Vershik-Kerov LIS velocity $2\sqrt{C} > 1$ to arbitrary non-monotone permutations violates point conservation and monotone path constraints | category_lis_velocity_nonmonotone_mismatch.md |
| discrete_buffer_integer_granularity | 24 | Continuous buffer scaling yields unphysical fractional points ($< 1$), while discrete rank-slot separation requires $\ge 1$ integer point per interface, incurring $\ge k/2$ penalty that wipes out surplus | category_discrete_buffer_integer_granularity.md |
| information_theoretic_tree_deficit | 13 | Dyadic trees of description entropy $O(\varepsilon^2 k)$ or $O(k)$ cannot cover $S_k$ because Shannon source coding requires $\log_2(k!) = \Theta(k \log k)$ bits | category_information_theoretic_tree_deficit.md |
| omission_of_coarse_penalties | 4 | Dropping coarse-scale discretization penalties $\sum_{j \le j^*} P_j \approx 2.41 C_1 k$ conceals that total net drift is strongly negative across all interfaces | category_omission_of_coarse_penalties.md |
| gluing_lemma_monotone_hypothesis_failure | 2 | Boundary-Compatible Gluing (Lemma 3.5 of W47) requires monotone contiguous-value blocks, which fails on over $99.98\%$ of permutations in $S_k$ | category_gluing_lemma_monotone_hypothesis_failure.md |

## Theorems
| File | Confidence | Summary |
|------|------------|---------|
| theorem_sharp_lis_barrier.md | high | Uniform random permutations of length $n = \lfloor C k^2 \rfloor$ with $C < 1/4$ contain $\operatorname{id}_k$ with probability $o(1)$, establishing $C = 1/4$ as the sharp information-theoretic lower bound. |
| theorem_poisson_thinning_coupling.md | high | De-Poissonization coupling certifying that planar Poisson point process embeddings at intensity $(1/4+\varepsilon/2)k^2$ transfer to $\sigma_n \sim \operatorname{Uniform}(S_n)$ with error $\le \exp(-\Omega(\varepsilon^2 k^2))$. |

## Observations
| File | Confidence | Summary |
|------|------------|---------|
| observation_discrete_rank_slot_integer_barrier.md | high | Discrete coordinate embedding requires $\ge 1$ rank slot per interface, causing fine-scale buffer penalties to sum to $\ge k/2 = \Omega(k)$, wiping out $2\varepsilon k$ surplus for all $\varepsilon < 1/4$. |
| observation_dyadic_vertical_span_overlap.md | high | Dyadic interval vertical ranges sum to $\sum h_{j,m} = \Theta(2^j) \gg 1$ on non-monotone permutations, refuting disjointness and causing boundary penalties to scale as $\Theta(k \log k)$ or $\Theta(k^{3/2})$. |
| observation_factorial_information_deficit.md | high | Shannon source coding requires $\log_2(k!) = \Theta(k \log k)$ bits to represent all $k!$ permutations; dyadic tree partition entropy telescoping product confirms exact $\ln(k!)$ complexity. |
| observation_infinitesimal_lis_point_conservation_violation.md | high | Integrating infinitesimal LIS capacity $dN = 2\sqrt{d\mu}$ across diagonal corridors predicts $3.8\times$ more points than exist in the Poisson process, violating point conservation $\operatorname{LIS}(S) \le |S|$. |
| observation_tracy_widom_boundary_fluctuation_growth.md | high | Tracy-Widom boundary matching fluctuations scale as $O(L_j^{1/3}) = O(k^{1/3} 2^{-j/3})$ per interface, accumulating across $2^j$ interfaces to $O(k^{1/3} 2^{2j/3})$ and growing geometrically to $\Theta(k)$ at fine scales. |

## References
| File | Confidence | Summary |
|------|------------|---------|
| reference_alon_1999_superpatterns.md | high | Noga Alon's 1999 conjecture that the asymptotic threshold for universal permutations containing all $\pi \in S_k$ is $(1/4+o(1))k^2$. |
| reference_baik_deift_johansson_1999.md | high | Baik, Deift, Johansson (1999) proving GUE Tracy-Widom fluctuation limit $N^{1/6}$ for LIS of random permutations and Poisson point processes. |
| reference_deuschel_zeitouni_1999.md | high | Deuschel and Zeitouni (1999) proving exponential lower tail large deviations $\exp(-c(\delta)\mu)$ for LIS in planar Poisson point processes. |
| reference_logan_shepp_vershik_kerov_1977.md | high | Logan & Shepp (1977) and Vershik & Kerov (1977) proving the asymptotic LIS limit $\lim_{n \to \infty} \operatorname{LIS}(\sigma_n)/\sqrt{n} = 2$. |
