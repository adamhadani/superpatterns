# Workstream W62: Dyadic Quadtree Chaining & Hierarchical Coordinate Decomposition

## Objective
Investigate whether an adaptive dyadic quadtree decomposition of target permutations $\pi \in S_k$ can resolve the two fundamental bottlenecks of uniform grids:
1. **Adversarial dense clusters** (where up to $\sqrt{k}$ points concentrate in a single $1/\sqrt{k} \times 1/\sqrt{k}$ box), and
2. **Inter-box column and row coordinate scrambling** (where independent box embeddings fail to preserve relative ordering across points sharing a grid column or row).

## Mathematical Formulation

### 1. The Dyadic Quadtree $\mathcal{T}(\pi)$
Let $\pi \in S_k$ be represented as the point set:
$$\mathcal{P}(\pi) = \left\{ \left( \frac{i}{k}, \frac{\pi(i)}{k} \right) : i \in \{0, 1, \dots, k-1\} \right\} \subset [0, 1)^2.$$
Define the dyadic box of scale $j \ge 0$ at indices $(u, v)$ with $0 \le u, v < 2^j$:
$$Q_{j, u, v} := \left[ \frac{u}{2^j}, \frac{u+1}{2^j} \right) \times \left[ \frac{v}{2^j}, \frac{v+1}{2^j} \right).$$
- **Root:** $Q_{0, 0, 0} = [0, 1)^2$.
- **Recursive Splitting:** For any box $Q$, let $m(Q) = |\mathcal{P}(\pi) \cap Q|$.
  - If $m(Q) \le 1$, $Q$ is a **leaf**.
  - If $m(Q) \ge 2$, $Q$ is partitioned into 4 children of scale $j+1$:
    $Q_{0,0}, Q_{0,1}, Q_{1,0}, Q_{1,1}$.

### 2. Theoretical Questions to Resolve
1. **Tree Depth & Size:**
   - What is the maximum depth $J_{\max}(\pi)$? Since coordinates are spaced by $\ge 1/k$, is $J_{\max} \le \lceil \log_2 k \rceil$?
   - How many total nodes $V(\pi)$ and non-empty leaves $L(\pi)$ exist?
2. **Description Entropy:**
   - What is the total description entropy $\ln |\mathfrak{T}_k|$ of all possible quadtrees $\mathcal{T}(\pi)$ as $\pi$ ranges over $S_k$?
   - Is it bounded by $\mathcal{O}(k)$ bits (Catalan-like bound), or does it carry higher entropy?
3. **Hierarchical Separation & Order Preservation:**
   - For any pair of points $p_1 \ne p_2$, let $Q = \operatorname{LCA}(p_1, p_2)$ be their lowest common ancestor in $\mathcal{T}(\pi)$.
   - Does the split at $Q$ unambiguously establish their relative horizontal order, vertical order, or both?
4. **Host Coupling & Poisson Void Resolution:**
   - In a Poisson host $\Pi_n$ with $n = C k^2$, what is the point distribution across the nodes of $\mathcal{T}(\pi)$?
   - At depth $j$, $\mathbb{E}[N(Q)] = C k^2 4^{-j}$.
   - Can empty leaf boxes be resolved by hierarchical borrowing from parent or sibling boxes?
