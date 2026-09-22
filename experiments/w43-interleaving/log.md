# Workstream W43: Research Log and Audit Trail

## Mission Objective
Establish a rigorous, boundary-compatible embedding lemma that bridges structured components
(monotone inflations / chains) with residual components in a host permutation of size $n = O(k^2)$,
fulfilling all requirements (R1–R4) of Workstream W43.

---

## Chronological Audit Trail

### 2026-09-22: Theory Design & Mathematical Exploration
- **Problem Analysis**: Reviewed past embedding bottlenecks.
  - In W39, monotone inflations with blocks $\ge K \sqrt{\log k}$ embed simultaneously into $O(k^3)$ host boxes.
  - In general permutations, structured and residual components interleave arbitrarily.
  - Naive sequential embedding fails because embedding the first component greedily consumes coordinate space, leaving residual coordinate ranges whose geometry cannot accommodate the second component without ordering conflicts.
- **Candidate Formulation 1 (Naive Unreserved Greedy Packing)**:
  - Formulated greedy packing of $M_1$ into earliest host columns/rows.
  - Tested on permutations with $\operatorname{LDS} \le 2$: produced catastrophic dead-end failures for 424 out of 613 non-monotone permutations (9/14 for $k=4$, 28/42 for $k=5$, 90/132 for $k=6$, 297/429 for $k=7$).
  - Conclusion: Coordinate reservation is mathematically mandatory.
- **Candidate Formulation 2 (Scalar Chain Tracking - W14 Trap)**:
  - Assessed whether chain lengths alone suffice to parameterize the interface.
  - Refuted: Two permutations can have identical chain lengths but different relative value interleavings. Scalar lengths fail to specify relative order.
- **Candidate Formulation 3 (Joint Interleaving Word Encoding)**:
  - For $\pi$ with $\operatorname{LDS}(\pi) \le 2$, partitioned into canonical chains $(M_1, M_2)$ via greedy Patience sorting.
  - Proved Proposition 1: $M_2$ is guaranteed to be strictly increasing, with no inversions (otherwise a 321 decreasing subsequence exists, contradiction).
  - Encoded joint placement via position word $w^{\mathrm{pos}} \in \{1, 2\}^k$ and value word $w^{\mathrm{val}} \in \{1, 2\}^k$.
  - Proved Proposition 2: $(w^{\mathrm{pos}}, w^{\mathrm{val}})$ uniquely reconstructs $\pi$.
  - Quantified word entropy: $\sum_{a=0}^k \binom{k}{a}^2 = \binom{2k}{k} < 4^k = e^{k \ln 4}$.
- **Candidate Formulation 4 (Boundary-Compatible Interface Specification)**:
  - Defined column intervals $I_x(t) = [x^{\mathrm{in}}(t), x^{\mathrm{out}}(t)]$ and row intervals $I_y(v) = [y^{\mathrm{in}}(v), y^{\mathrm{out}}(v)]$ with strict separation $x^{\mathrm{out}}(t) < x^{\mathrm{in}}(t')$ and $y^{\mathrm{out}}(v) < y^{\mathrm{in}}(v')$.
  - Allocated reserved cell boxes $B_t = I_x(t) \times I_y(\pi(t))$.
  - Formulated and proved Lemma 3 (Boundary-Compatible Embedding Lemma): Any valid embedding of $M_1$ in its reserved boxes leaves a residual coordinate domain containing $B_q$ for all $q \in M_2$, completely eliminating boundary collisions and ordering dead ends.
- **Interface Entropy & Common Host Event**:
  - Bound total interface profiles by $|\mathfrak{I}| \le 4^k \binom{3k}{k}^2 \le e^{5.59 k}$ on a $2k \times 2k$ grid.
  - Defined common host event $E_{\mathrm{host}} = \bigcap_{i, j} \{ N(Q_{i, j}) \ge 1 \}$ on Poisson host $\Pi_{C k^2}$.
  - Established failure probability $\le 4k^2 e^{-C/4} = o(1)$.
  - Concluded simultaneous containment for all 321-avoiding permutations on $E_{\mathrm{host}}$ without any $k!$ union bound.

---

## Computational Verification Audit (`verify.py`)

Implemented comprehensive test suite in `experiments/w43-interleaving/verify.py`:

```sh
python3 experiments/w43-interleaving/verify.py
```

### Execution Results:
1. **Catalan Census**:
   - $k=4$: 14 permutations
   - $k=5$: 42 permutations
   - $k=6$: 132 permutations
   - $k=7$: 429 permutations
   - Total: 617 permutations (exact match with Catalan numbers $C_k = \frac{1}{k+1}\binom{2k}{k}$).
2. **Canonical Decomposition**:
   - Greene / Patience sorting decomposed all 617 permutations into strictly increasing $M_1$ and $M_2$.
   - Exact reconstruction from $(w^{\mathrm{pos}}, w^{\mathrm{val}})$: 617/617 verified.
3. **Failure Audit of Naive Unreserved Packing**:
   - $k=4$: 9 failures
   - $k=5$: 28 failures
   - $k=6$: 90 failures
   - $k=7$: 297 failures
   - Total: 424 failures out of 613 non-monotone permutations.
4. **Boundary-Compatible Interface on $2k \times 2k$ Host Grids**:
   - 0 counterexamples across all 617 permutations.
5. **Sequential & Concurrent Interleaving Completions**:
   - Forward completion ($M_1$ embedded first, $M_2$ completed): 0 counterexamples.
   - Reverse completion ($M_2$ embedded first, $M_1$ completed): 0 counterexamples.
6. **Occupancy Grids with Slack & Noise**:
   - Randomized simulations on $(3k) \times (3k)$ grids: 0 failures across 617 trials.
   - Overall execution time: ~0.02s.

---

## Milestone Status & Acceptance Criteria Checklist
- [x] R1: Formulate Boundary-Compatible Embedding Lemma with entrance/exit intervals and reserved coordinate ranges.
- [x] R1: Quantify interface entropy $\le e^{O(k)}$ and common host event $E_{\mathrm{host}}$ of probability $1 - o(1)$ at $O(k^2)$.
- [x] R2: Implement automated combinatorial verification tool testing all $S_k$ permutations with $\operatorname{LDS} \le 2$ for $k \in \{4, 5, 6, 7\}$ (617 total) with 0 counterexamples.
- [x] R3: Rigorous proofs in `proof.md`; elimination of traps W14, W18, W34; zero $k!$ union bounds.
- [x] R4: Complete research documentation in `proof.md` and `log.md`.
