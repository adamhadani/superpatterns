# Inversion Duality Interval Block Preservation

Type: observation
Confidence: high
Source: Candidate N24 (Round 3 Level 0)
Relevant to: Tier 1 structural decomposition, block substitution, modular decomposition, permutation inversion duality $D_4$ symmetry.

## Statement
For any permutation $\pi \in S_k$, a subset $B \subseteq [k]$ is an interval block (or module) of $\pi$—meaning both the domain $B$ and the image $\pi(B)$ form contiguous intervals in $[k]$—if and only if $\pi(B)$ is an interval block of the inverse permutation $\pi^{-1}$. Consequently, the set of non-trivial monotone interval blocks $\mathcal{M}_{\mathrm{int}}(\pi)$ is preserved under inversion transposition $\pi \mapsto \pi^{-1}$, satisfying:
$$|\mathcal{M}_{\mathrm{int}}(\pi^{-1})| = |\mathcal{M}_{\mathrm{int}}(\pi)|.$$
In particular, the dual block partition $\mathcal{M}_{\mathrm{int}}^*$ is identically equal to $\mathcal{M}_{\mathrm{int}}$ in size and structure. The operation of inversion duality cannot transform interleaved monotone sequences (which possess no contiguous domain/value blocks) into contiguous interval inflations.

## Evidence
1. **Mathematical Proof**: Let $B$ be an interval block of $\pi$. By definition, $B = \{i, i+1, \dots, i+|B|-1\}$ and $\pi(B) = \{j, j+1, \dots, j+|B|-1\}$. For the inverse permutation $\pi^{-1}$, the domain subset $B' = \pi(B)$ is a contiguous interval, and its image $\pi^{-1}(B') = B$ is also a contiguous interval. Thus $B'$ is an interval block of $\pi^{-1}$.
2. **Monotonicity Preservation**: If $\pi|_{B}$ is monotone increasing (or decreasing), then $\pi^{-1}|_{B'}$ is likewise monotone increasing (or decreasing) because $u < v \implies \pi^{-1}(u) < \pi^{-1}(v)$ (or $> \pi^{-1}(v)$).
3. **Exhaustive Simulation on Interleaved Runs**: For the canonical interleaved permutation $\pi = (1, 3, 5, \dots, 2, 4, 6, \dots)$, the maximum size of any interval block is $|B| = 1$ in $\pi$, and exactly $|B| = 1$ in $\pi^{-1}$. Candidate N24's Lemma 3.2 claimed that inversion duality mapped interleaved permutations with $M_{\mathrm{int}} \le 2$ to dual blocks of size $M_{\mathrm{int}}^* \ge k/2$. Falser testing demonstrated that $M_{\mathrm{int}}^* = M_{\mathrm{int}} = 1$ identically on all interleaved permutations, giving a $0\%$ match to claimed dual structures.

## Implications
- Eliminates proof strategies attempting to salvage Tier 1 monotone inflation decompositions via transposition or $D_4$ group symmetries.
- Re-routing generic permutations with interleaved runs to their inverse $\pi^{-1}$ leaves the permutation simple or unstructured, providing zero expansion in interval block coverage.

## Caveats
- Applies strictly to interval blocks (modules in substitution decomposition). It does not preclude decomposing $\pi$ into monotone subsequences via Dilworth's theorem or Greene's theorem, though those non-contiguous chains face cross-chain blocking and ordering collisions rather than interval gluing.
