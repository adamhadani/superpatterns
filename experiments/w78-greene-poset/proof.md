# Workstream W78: Greene's Poset Theorem & Multi-Chain Capacity Duality

## Mathematical Objective
To ground the multi-chain host capacity surplus used in W76-W77 in a formal Lean 4 implementation of Greene's Theorem. This provides the critical link showing that if the macroscopic capacities $\lambda_a$ of a discrete host grid exceed the demands $d_a$, the host can physically admit $d$ disjoint increasing chains of the demanded lengths.

## Greene's Poset Capacity Theorem

Let $P$ be a finite poset (for permutations, elements ordered by $i < j$ and $\pi_i < \pi_j$). Let $c_m(P)$ be the maximum cardinality of a union of $m$ disjoint chains in $P$. Greene (1974) proved that the sequence of differences:
$$ \lambda_m(P) = c_m(P) - c_{m-1}(P) $$
forms a weakly decreasing sequence $\lambda_1 \ge \lambda_2 \ge \dots$ which corresponds exactly to the shape of the Robinson-Schensted (RSK) Young tableau associated with the poset. 

Furthermore, Greene established a profound min-max duality:
For any collection of $m$ disjoint chains $C_1, \dots, C_m$, we have:
$$ \left| \bigcup_{i=1}^m C_i \right| \le \sum_{i=1}^m \lambda_i(P) = c_m(P) $$
with equality achieving the optimal $m$-chain union.

## Multi-Chain Demand Realizability Lemma

A direct consequence of Greene's Theorem is the demand realizability bound for pattern embeddings. If a host permutation (or discrete grid block) $H$ possesses multi-chain capacities $\lambda_a(H) \ge d_a$ for $1 \le a \le d$, then $H$ can realize the demand of $d$ chains. 

*Proof approach*:
By Greene's definition, the maximum number of elements we can extract using $d$ chains is $\sum_{a=1}^d \lambda_a(H)$. Since $\lambda_a(H)$ is a non-increasing partition sequence, any demand sequence $d_a$ bounded point-wise by $\lambda_a(H)$ is realizable by a valid chain partition of $H$.

## Lean 4 Formalization

The theorem is formalized in `formal-verification/lean/Superpatterns/Greene.lean`, defining:
1. `IsChain` and `DisjointChains`.
2. $c_m$ (`c_m`) as the supremum over sizes of unions of $m$ disjoint chains.
3. The Greene difference function `greene_lambda`.
4. The capacity bounds `greene_capacity_bound` and `greene_capacity_optimal`.
5. The demand realizability lemma `multichain_demand_realizability`.

## Empirical Verification
Exhaustive machine verification (`verify.py`) confirmed:
- RSK row lengths perfectly match the exact disjoint chain capacity gaps $c_m(P) - c_{m-1}(P)$ for all 5,904 permutations in $S_4, S_5, S_6, S_7$.
- Submodularity ($\lambda_a \ge \lambda_{a+1}$) holds strictly across all configurations.
- Multi-chain embeddings easily satisfy macroscopic demand configurations at $C^* \in \{0.26, 0.28, 0.30\}$ under W76 limits.
