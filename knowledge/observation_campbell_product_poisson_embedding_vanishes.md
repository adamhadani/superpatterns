# Campbell Product Formula and Markov Non-Containment Barrier for Global Strip Embeddings

Type: observation
Confidence: high
Source: Candidate 27 (Level 0, Round 2)
Relevant to: Poisson embedding strategies, global rank strip partitioning, Janson concentration arguments for permutation patterns

## Statement
Let $\mathcal{P} \subset [0, 1]^2$ be a homogeneous Poisson point process of intensity $\lambda = C k^2$ with $C > 0$. If an embedding of a permutation $\pi \in S_k$ requires selecting points $(x_i, y_i) \in \mathcal{P}$ such that the vertical coordinates fall into independent global rank strips $S_{\pi(i)} = [0, 1] \times [(\pi(i)-1)/k, \pi(i)/k]$, each of area $1/k$, then by Campbell's formula / Poisson product moments, the expected number of valid embeddings $N_\pi$ satisfying the horizontal ordering $x_1 < x_2 < \dots < x_k$ is exactly:
$$ \mathbb{E}[N_\pi] = \frac{(\lambda / k)^k}{k!} = \frac{(C k)^k}{k!} $$
By Stirling's approximation $k! \ge \sqrt{2\pi k} (k/e)^k$, this expected count satisfies:
$$ \mathbb{E}[N_\pi] \le \frac{(e C)^k}{\sqrt{2\pi k}} $$
Whenever $C < 1/e \approx 0.367879$, $e C < 1$, forcing $\mathbb{E}[N_\pi] \to 0$ exponentially fast as $k \to \infty$. By Markov's inequality:
$$ \Pr(N_\pi \ge 1) \le \mathbb{E}[N_\pi] \le \frac{(e C)^k}{\sqrt{2\pi k}} \to 0 $$
Consequently, the probability of non-containment satisfies:
$$ \Pr(N_\pi = 0) \ge 1 - \frac{(e C)^k}{\sqrt{2\pi k}} \to 1 $$
Furthermore, any attempt to apply Janson's inequality $\Pr(N_\pi = 0) \le \exp(-\mu^2 / (\mu + \Delta))$ produces an exponent upper-bounded by $\mu = \mathbb{E}[N_\pi] \to 0$, rendering the Janson upper bound $\le \exp(0) = 1$ completely vacuous.

## Evidence
1. **Exact Symbolic Integration**: The domain of valid embeddings in $(\mathbb{R}^2)^k$ under disjoint vertical strips is the simplex $0 \le x_1 < \dots < x_k \le 1$ with volume $1/k!$, and each point $(x_i, y_i)$ is independently chosen from an area $1/k$ with intensity $C k^2$, giving arrival rate per strip $\lambda/k = C k$. The product intensity integrated over the simplex yields $\frac{(C k)^k}{k!}$.
2. **Numerical Verification for $C = 1/4 + \varepsilon/2 = 0.275$**:
   - $e C \approx 2.71828 \times 0.275 = 0.747528 < 1$.
   - For $k = 100$: $\mathbb{E}[N_\pi] \le \frac{(0.7475)^{100}}{\sqrt{200\pi}} \approx 9.19 \times 10^{-15}$.
   - For $k = 1000$: $\mathbb{E}[N_\pi] \le 5.35 \times 10^{-129}$.
   The probability that a Poisson point process at intensity $(1/4+\varepsilon) k^2$ contains *any* embedding of $\pi$ in rigid rank strips is bounded above by $10^{-14}$ at $k=100$ and $10^{-128}$ at $k=1000$.

## Implications
- Any proof strategy that partitions the unit square into $k$ disjoint horizontal strips $[(j-1)/k, j/k]$ of height $1/k$ and attempts to embed an arbitrary permutation $\pi$ by picking one point in $S_{\pi(i)}$ ordered horizontally fails unconditionally for any $C < 1/e$.
- Since $1/4 = 0.25 < 1/e \approx 0.3679$, the critical threshold for the Arratia conjecture lies strictly inside the Markov extinction regime for independent global strip embeddings.
- This proves that successful embeddings at $C \in [1/4, 1/e]$ *must* exploit flexible height assignments, dynamic multi-strip pooling, or 2D poset chain routing rather than fixed 1D global rank decomposition.

## Caveats
- This barrier applies specifically to embeddings where each element $\pi(i)$ is assigned to a fixed disjoint strip of vertical height $1/k$. It does not prevent embeddings where strips overlap, where multiple elements share wider windows, or where elements are selected dynamically via poset longest chains (such as Greene's theorem or Schensted routing).
