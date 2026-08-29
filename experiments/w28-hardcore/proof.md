# W28 — hard-core / cluster reduction of the union bound: statements and proofs

Notation. σ_n uniform in S_n; for π ∈ S_k, A_π = {π ⊄ σ_n}, p_π = Pr(A_π); M = Σ_π 1_{A_π} = #missing k-patterns;
μ = E M = Σ_π p_π; R = R(n,k) = μ / Pr(M>0) = E[M | M>0] (the union-bound slack). Tags: PROVED / HEURISTIC / NUMERICAL.

## 1. The witness (second-moment) reduction — PROVED

**Theorem 1.1.** For all n, k:
(a) Pr(M>0) = μ/R and R ≥ max(1, μ).
(b) R ≤ E[M²]/μ = μ^{−1} Σ_π p_π Λ_π ≤ max_π Λ_π, where Λ_π = Λ_π(n) := E[M | π ⊄ σ_n] is the mean number of
    missing k-patterns of a *uniformly random π-avoiding permutation of length n* (i.e. of Av_n(π) with the uniform law).
(c) (witness form) Let W be any random variable defined on {M>0} with values in a set 𝒲. Then
    R ≤ max_{w∈𝒲} E[M | W = w].

*Proof.* (a) R = E M / Pr(M>0) = E[M 1_{M>0}]/Pr(M>0) = E[M | M>0] ≥ 1 since M ≥ 1 on {M>0}; and R ≥ μ since Pr(M>0) ≤ 1.
(b) Cauchy–Schwarz: μ = E[M 1_{M>0}] ≤ (E M²)^{1/2} Pr(M>0)^{1/2}, so Pr(M>0) ≥ μ²/E M², i.e. R ≤ E M²/μ.
E M² = Σ_π E[M 1_{A_π}] = Σ_π p_π E[M | A_π] = Σ_π p_π Λ_π, and a p-weighted average is ≤ the maximum. Conditionally on
A_π, σ_n is uniform on Av_n(π), which is the stated interpretation of Λ_π.
(c) μ = Σ_w E[M ; W=w] = Σ_w Pr(W=w) E[M | W=w] ≤ max_w E[M|W=w] · Σ_w Pr(W=w) = max_w E[M|W=w] · Pr(M>0). ∎
(b) is (c) with W = the lexicographically first missing pattern, up to the weighting.

**Corollary 1.2 (hard-core criterion H(a)).** If Λ_π(n) ≤ e^{ak} for every π ∈ S_k, then Pr(M>0) ≥ μ(n) e^{−ak}.
Together with the union bound this sandwiches Pr(M>0) between μ e^{−ak} and μ, so the median threshold t(k)
(Pr(M>0) = 1/2) lies between the points n_0, n_1 with μ(n_0) = e^{ak}/2 and μ(n_1) = 1/2. Since ln μ(n) decreases by
Θ(1) per unit of n near the threshold (data: by 0.5 per unit n at k = 7, n ≈ 37; by 0.25–0.4 at k = 6; it must be
O(1) since adding one point changes each p_π by a bounded factor), n_1 − n_0 = O(ak) = o(k²) when a = o(k).
**Hence: if max_π Λ_π(n) = e^{o(k²)} in the window (in particular under R ≤ e^{O(k)}), the threshold constant
lim t(k)/k² equals the first-moment constant**, i.e. it is determined by the per-pattern rates I_π(C) of W27 alone.
(Proof: Pr(M>0) ≤ μ and Pr(M>0) ≥ μ/max_π Λ_π.) ∎

Remarks. (i) The criterion is *only about conditional expectations of a count*, no independence or correlation
inequality is used; that is why it escapes the Δ ≥ μ²/C cap of Janson/Suen (W22 Prop. B.1): Janson bounds
Pr(M=0) from above by e^{−μ+Δ/2} — with Δ = E M(M−1) ≫ μ here (Table 1 of results.md: Δ/μ = 20–430) the exponent is
positive and the bound is void — whereas Theorem 1.1 bounds Pr(M>0) from below and only needs E M²/μ = 1 + Δ/μ.
(ii) Δ = Σ_{π≠π'} Pr(A_π ∩ A_π') = E[M(M−1)] exactly (all pairs are dependent), so all Janson-type quantities are
functionals of the law of M; the Bonferroni truncations are the binomial moments: Pr(M>0) = Σ_{j≥1} (−1)^{j+1} E C(M,j).
(iii) The gap between R and E M²/μ is exactly 1 + Var(M | M>0)/E[M|M>0]², the squared coefficient of variation of
the conditional law: R = E[M|M>0], E M²/μ = E[M² | M>0]/E[M | M>0].

## 2. Erdős–Szekeres disjointness (task 3(iii)) — PROVED

**Theorem 2.1.** If (a−1)(b−1) < n then {I_a ⊄ σ_n} ∩ {D_b ⊄ σ_n} = ∅. In particular for n ≥ (k−1)²+1 the events
"identity missing" and "reverse missing" are disjoint, Pr(id ⊄ σ_n, rev ⊄ σ_n) = 0, and
Pr(M>0) ≥ p_id + p_rev = 2 p_id.
*Proof.* Erdős–Szekeres: every sequence of n > (a−1)(b−1) distinct reals has an increasing subsequence of length a or
a decreasing one of length b. ∎
(k−1)²+1 = 26, 37, 50, 65 for k = 6,7,8,9; the W24 observation "reverse/complement of the identity never co-miss" at
t(7) = 37 is this theorem. For k ≥ 8, t(k) < (k−1)²+1 and the theorem does not apply at the threshold; the numerical
co-miss count is still 0 (LIS < k and LDS < k simultaneously at n ≈ 0.75k² has probability far below p_id²).

**Why it does not help (PROVED, trivial).** The implication structure of pattern containment is monotone the wrong
way for this to propagate: I_a ⊄ σ ⇒ π ⊄ σ for all π ⊇ I_a, but π ⊄ σ says nothing about I_a. So the only pairs of
events made disjoint by Theorem 2.1 are the two monotone patterns (and the nested sub-monotone ones), and the gain in
Pr(M>0) is at most a factor 2 (Pr(M>0) ≥ p_id + p_rev versus ≥ max(p_id, p_rev)); it is invisible on the e^{Θ(k)} scale.
The LIS/LDS negative dependence at fixed n is thus a deterministic boundary effect, not a usable correlation inequality.

## 3. Structured families (task 3(i)) — PROVED where tagged

For a family F ⊆ S_k put M_F = Σ_{π∈F} 1_{A_π}, μ_F, R_F = μ_F/Pr(M_F>0). Trivially R_F ≤ |F| and R_F ≤ max_{π∈F} E[M_F | A_π].

**Proposition 3.1 (monotone patterns of all lengths; PROVED, exact).** For F = {I_j, D_j : 2 ≤ j ≤ k} (events nested:
I_j ⊄ σ ⟺ LIS(σ) < j): M_F = (k − LIS(σ_n))^+ + (k − LDS(σ_n))^+, so R_F ≤ 2(k−1), and R_F ≤ k−1 when n ≥ (k−1)²+1
(Theorem 2.1). Here R_F = e^{O(ln k)}: the whole family is "one hard core" (LIS) and the slack is the cluster size.

**Proposition 3.2 (near-identity family; PROVED as a bound).** For F_j = {π ∈ S_k : LIS(π) ≥ k−j}, |F_j| ≤ Σ_{i≤j} C(k,i)² i!
≤ (k^{2}·e/j)^{j}·(1+o(1)) so R_{F_j} ≤ e^{2j ln k}; in particular R_{F_j} = e^{O(k)} for j ≤ k/(2 ln k). No conditional
structure is needed. For j ≍ k this is vacuous, which is exactly the regime where the data (results.md §2) shows
that the missing patterns live: at k = 7, n = 37 F_1 together with its reverse image (max(LIS,LDS) ≥ k−1; 74 patterns) carries only 2.2 % of μ, and max(LIS,LDS) ≥ k−2 carries 22 %.

**Proposition 3.3 (R below the threshold; PROVED).** For n = ck² with c < c_1 := lim inf n_1(k)/k², R(n,k) ≥ μ(n,k) =
e^{Θ(k ln k)} (data: ln μ/ln k! = 0.62, 0.59 at n ≈ 0.6k², k = 7, 9). So "R ≤ e^{O(k)}" can only be true in the
form R ≤ max(1, μ) e^{O(k)}, and the content of the conjecture is the window μ ∈ [e^{−O(k)}, e^{O(k)}].

**Example: the witness bound (b),(c) is not tight in general (PROVED).** In the W19 rigid-row model (k position
blocks of length m = n/k, copies take one point per block), on the event E_i = {all values of block i are below all
other values} (probability 1/C(n,m) = e^{−Θ(m ln k)}) every copy has its i-th point lowest, so every π with π(i) ≠ 1 is
missing and M ≥ k! − (k−1)!: max_w E[M | W=w] = e^{Θ(k ln k)} for any witness map W that can see E_i, although E_i
itself contributes only e^{−Θ(m ln k)}·k! = o(1) to μ at n ≍ k². So a proof of R ≤ e^{O(k)} via Theorem 1.1 must
use the p-weighted average Σ p_π Λ_π/μ (or a witness W that does not isolate rare global events), not max_π Λ_π: the
average is what the data supports (max_π Λ_π / (E M²/μ) = 1.8 at k=6 and 2.2 at k=7 among patterns with ≥ 20 events; Table 4 of results.md).
In the uniform model there is no "global switch" of this kind: the missing sets of size ≥ 300 (k = 7) are only 32 %
covered by fully-missing (k−1)-patterns and consist of *generic* patterns (mean max(LIS,LDS) 4.0 vs 4.29 for
singletons; results.md Table 3). That the failure mechanism is local is the reason the slack is small; it is not a proof.

## 4. Why e^{O(k)}? — HEURISTIC + NUMERICAL (what a proof would need)

(H1) **No hard core.** p_π at n = t(k) varies over S_k by a factor ≤ 4 (k = 6: 0.45×–1.9× the mean; k = 7: 0.82×–2.9×);
the top 1 % of patterns carries 1.8 % (k=6) / 2.4 % (k=7) of μ; the dihedral class spread is 1.3–1.5. So μ is *spread
uniformly* over S_k and R is not a "few hard patterns" effect: it is entirely the conditional clustering.
(H2) **Hard patterns fail alone.** corr(p_π, Λ_π) = −0.75 (k=6, n=28), −0.43 (k=7, n=37): the (layered/co-layered) patterns
with the largest p_π have the *smallest* conditional cluster Λ_π, and the largest Λ_π (173 at k=7) belong to generic
patterns which are missed only when σ is globally bad. Layered patterns are the hardest (1543276 = 1⊕D₄⊕D₂,
7234561 = 1⊖I₅⊖1); the identity is not the hardest at k = 6,7 (p_id/max p = 0.74, 0.86), consistent with W27 Fact 1.1.
(H3) **Clusters are diffuse.** Given M>0 the missing set is one connected component in the one-point-move graph
(largest component 90–94 % of M; 1.2–1.4 components vs 2.5–5.5 for a random subset of the same size), but it is *not*
the up-set of missing (k−1)-patterns (fully missing children explain 0 % of M for M < 30 and 9 % for M ∈ [100,300)).
The greedy number of (k−1)-patterns needed to cover the missing set is ≈ M^{0.6} (cover/M = 0.35, 0.24, 0.16, 0.12 for
M ≈ 15, 50, 150, 500), i.e. each "weak" (k−1)-pattern τ loses only 3–9 of its 37 extensions.
(H4) **Where R is made.** R = E[M | M>0] is dominated by the far tail: the share of Σ M from events with M ≥ 256 is
0, 0.07, 0.29, 0.48 (k = 6..9 at t(k)); the local tail exponent α(m) = −log₂ [P(M≥2m)/P(M≥m)] rises from 0.4 (m=2)
through 0.6 (m=32–64) to > 2 beyond m ≈ 500 at k = 9. So R is set by the size at which the tail of the cluster-size
law steepens, ≈ e^{0.7k} in the observed range. A proof of R ≤ e^{O(k)} must show that P(M ≥ m | M>0) ≤ m^{−1−δ}
for m ≥ e^{O(k)}, i.e. that **missing e^{ω(k)} patterns at n ≈ t(k) costs e^{−ω(k)} relative to missing one** — a
large-deviation statement about the *number* of missing patterns, not about any single pattern.
(H5) **Monotone mechanism is too weak to matter (HEURISTIC).** A σ with LIS(σ_n) ≤ k−1−j misses all ≥ k^{2j}/j!
patterns with LIS ≥ k−j; by the Deuschel–Zeitouni speed-n lower tail, Pr(LIS ≤ k−1−j) ≈ p_id e^{−c' j k}
(c' = √n·|H'(x_0)|/k ≍ 1), so this contributes Σ_j k^{2j}/j! · e^{−c'jk} · p_id/Pr(M>0) = p_id k² e^{−c'k}/Pr(M>0) ≪ 1
to R: the *observed* e^{0.7k} is not produced by near-monotone σ. It must come from local defects of σ (a
position×value rectangle of area ≍ 1/k² emptier than typical kills every pattern all of whose copies need a point
there); the number of patterns that a single defect at scale 1/k can kill is what has to be e^{O(k)}. Not proved.
NUMERICAL support (results.md Table 5, independent sample): Spearman(M, largest empty rectangle) = +0.42,
Spearman(M, min 4×4 cell count) = −0.29, Spearman(M, LIS) = +0.11 (6000 σ, k=7, n=37) — M is driven by emptiness, not by small LIS.

## 5. Dead ends (this workstream)
- Bonferroni/inclusion–exclusion of orders 2, 3 (Table 1): order 2 is negative (−229 at k=7, n=37; need Pr ≥ 0),
  order 3 is > 1: E C(M,j) grows like the j-th moment of a heavy-tailed variable; the sieve is useless at all n ≤ k².
- Janson: −μ + Δ/2 > 0 at every n with μ > 0.0007 (both k); confirms W22.
- Hard-core = "near-monotone patterns": refuted by H1 (share of μ from max(LIS,LDS) ≥ k−1 is 9 % (k=6) / 2 % (k=7),
  barely above the uniform 7 % / 1.5 %).
- Hierarchical explanation "missing (k−1)-pattern drags k² extensions": refuted by H3 (fully missing children explain
  ≤ 1 % of M for M < 100; the ratio μ_{k−1}(n)/μ_k(n) ≈ e^{−6.8} at k=7, n=37 makes level-drops too expensive).
- Erdős–Szekeres anti-correlation: exact, but worth a factor 2 only (§2).
