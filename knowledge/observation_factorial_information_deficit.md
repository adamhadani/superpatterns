# Factorial Target Information Deficit in Sub-Factorial Trees

Type: observation
Confidence: high
Source: Candidates 0, 2, 4, 5, 6, 7, 16, 20, 21, 23 (Level 0 falsers)
Relevant to: Description entropy, simultaneous universality, union bounds over permutations.

## Statement
By Shannon source coding and the pigeonhole principle, any discrete catalog or tree of embedding paths $\mathfrak{T}$ that certifies simultaneous containment of all $k!$ target permutations in $S_k$ must have description entropy of at least $\log_2(k!) = k \log_2(k/e) + O(\log k) = \Theta(k \log k)$ bits. Any tree structure restricted to entropy $O(\varepsilon^2 k)$ or $O(k)$ can represent at most $2^{O(k)}$ distinct permutation orderings, covering less than a $2^{-\Omega(k \log k)}$ fraction of $S_k$.

## Evidence
1. Exact information calculation: For $k=1000$, $\log_2(1000!) \approx 8529.4$ bits. A tree with claimed fine-scale entropy $(c/4)\varepsilon^2 k$ at $\varepsilon=0.01$ provides at most $0.10$ bits (an information deficit of $85,294\times$).
2. Candidate 23 falsification proved the exact telescoping identity for dyadic tree value partitions:
$$\prod_{j=0}^{\log_2 k - 1} \left[ \binom{2k/2^j}{k/2^j} \right]^{2^j/2} = k!$$
proving that dyadic tree partition entropy is identically $\ln(k!) = k \ln k - k + O(\log k)$, refuting the claim that scale $j$ contributes only $O(2^{-j} k)$ bits without multiplying by $2^j$.
3. Pigeonhole principle: If an interface profile $P$ uniquely determines the permutation's relative coordinate ordering, each profile embeds at most 1 permutation. Thus $|\mathfrak{T}| \ge k!$.
4. When authors claim $|\mathfrak{T}| \le \exp(O(k))$, they either omit the fine-scale permutations sharing coarse profiles (leaving $e^{\Omega(k)}$ fine paths uncertified) or omit the $2^j$ branching factor across dyadic tree levels.

## Implications
Simultaneous containment cannot be proved by taking a union bound over a tree of entropy $O(k)$ against a single-path concentration decay $\exp(-c \varepsilon^2 k)$. Either the tree does not cover $S_k$, or if the tree is expanded to cover $S_k$, the entropy $\Theta(k \log k)$ overwhelms the linear concentration exponent $\Omega(\varepsilon^2 k)$.

## Caveats
Shared host structures (such as shared squares $\mathcal{Q}_{\mathrm{squares}}$ of polynomial size $O(k^3)$) can be reused without multiplying entropy, but only for monotone blocks, not for unstructured arbitrary permutations.
