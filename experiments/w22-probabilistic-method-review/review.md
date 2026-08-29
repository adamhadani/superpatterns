# W22 — Alon–Spencer, *The Probabilistic Method* (4th ed., 2016): what it offers for the union-bound gap in Alon's superpattern conjecture

Source: `~/Library/CloudStorage/Dropbox/Books/Mathematics/[Alon, Spencer] The Probabilistic Method (2016).pdf`
(book page = PDF page − 18). All page numbers below are book pages. Read: Ch. 1–8 in full, 10.1–10.3, 15.7,
Appendix A, and every Probabilistic Lens; skimmed Ch. 9, 11–14, 16–17.

Notation as in the paper: `Π_N` = Poisson process of intensity `N = Ck²` on the unit square (or `n = N` uniform
points / a uniform permutation of length `n`); `A_π = {π ⊄ Π_N}`; `X = X_π` = number of copies of `π`;
`μ = E X = N^k/(k!)² = (Ce²)^k·k^{O(1)}`; `Δ = Σ_{I~J} Pr(B_I ∧ B_J)` over ordered pairs of *distinct overlapping*
potential copies. The gap: we need `Pr(A_π) ≤ e^{−(1+ε)k ln k}` at `N = Ck²` (speed `> k ln k`), while every
greedy/renewal method has speed `≤ min(k, h)` (W19) and threads are capped at `k log log k` (W18).

---

## A. Executive summary

**Bottom line.** None of the concentration tools in the book can reach speed `k ln k` at `N = Ck²`, and for the
three main ones this is a *theorem*, not a failure of ingenuity:

| tool | best possible exponent for `Pr(π ⊄ Π_{Ck²})` | why |
|---|---|---|
| Janson / extended Janson / Suen / Brun's sieve (Ch. 8) on any family of "copy" events | `≤ C/2 + o(1)` | `Δ ≥ (1−o(1)) μ²/C` for **every** family of cell-configuration events (Prop. B.1 below): copies overlap in single points too often |
| Talagrand (7.6–7.7) on any certifiable functional | `≤ C/4` | certificates have size `k` per unit, median `≤ N/k`, so `t = √(m/k) ≤ √C` |
| Azuma / McDiarmid / Alon–Kim–Spencer (7.2–7.4) on point exposure | `≤ C/2` | deviation needed is `Θ(k) = Θ(√N)`, the martingale scale |
| Kim–Vu (7.8) | nothing | constants `8^k k!^{1/2}`; degree `k → ∞` |
| Lovász Local Lemma, lopsided LLL, Moser's fix-it (Ch. 5) applied to the union over `π` | only `Pr(all π present) > 0` | absence events are all decreasing hence positively correlated; LLL proves existence, never w.h.p. |
| second moment / Chebyshev (Ch. 4) | constant probability only | `Var X/μ² ≍ Σ_j c_j (1/C)^j/j! = Θ(1)` (computed exactly for `k=4,5`, §B.2) |

The obstruction in all three concentration tools is the same: at `N = Ck²` the natural fluctuation scale of every
copy-counting functional (`√N` for martingales, `√(k·median)` for Talagrand, `√Δ ≍ μ/√C` for Janson) is of the
same order as its mean. The LIS lower tail *does* have speed `N` (Deuschel–Zeitouni), but no tool in the book sees
it — the same phenomenon as the book's own `Pr(ω(G(n,½)) < k)` example, where Azuma gives `n²/k⁸`, Talagrand
`n²/ln⁶n`, extended Janson `n²/ln⁴n`, and the truth is `n²/ln²n` (pp. 107–108, 121, 185).

**What is genuinely worth pursuing (ranked):**

1. **Certificate counting / entropy compression (Ch. 5.7, pp. 85–87; "counting the certificates of absence").**
   The only technique in the book of a global nature that is *not* capped. For the identity it gives, in three lines,
   `Pr(LIS(Π_N) < k) ≤ exp(−N ln(C/e))` for `C > e` — **speed `N`**, the first speed-`N` statement obtainable without
   RSK (§B.8). The certificate is Dilworth's cover by `k−1` decreasing chains; the union bound is over `(k−1)^N`
   assignments. For general `π` there is no Dilworth duality (containment is NP-complete), but for our *residual
   classes* there is: block-grid patterns `𝒢(r,h)` and unions of runs have copies that are chains in a molecule poset
   (W11, Thm 9), whose absence certificates are antichain covers (Mirsky). **Next step:** (a) write the antichain-cover
   certificate bound for `(12⋯r)^{k/r}` and for `𝒢(r,h)` and compare its threshold constant with Thm 9's
   `8(r+1)ln(...)·k²` — it should remove the `poly(r)` in the *threshold* while keeping speed `N/poly(r)`; (b) for the
   identity, see how far below `e` refined certificates (canonical/patience-sorting covers) push the constant — this
   calibrates the method's loss against the known rate function; (c) formulate the "failure log" of the exact
   Pareto-front DP (W20) as a certificate and count it (Moser-style).
2. **Correlated absence — measure the slack of the union bound (Ch. 6, Harris/FKG Thm 6.3.2, p. 96).**
   `Pr(∃π ⊄ Π_N) = Σ_π Pr(A_π) / E[#missing | ≥1 missing]`. All `A_π` are decreasing events, hence pairwise
   positively correlated; if a random non-superpattern typically misses `e^{ω(k)}` patterns, the union bound is off by
   that factor and the needed per-pattern speed drops below `k ln k`. W18 already found `Pr(E_0∩E_Δ) ≥ Pr(E_0)²e^{Ω(k)}`
   for *thread* failures on tilted grids; the analogous question for the *true* absence events is open and cheap to
   measure. **Next step:** with the W21/W5 sampler, at `k = 7,8,9` and `n` from `0.6k²` to `1.2k²`, record the full
   distribution of `#missing` and the ratio `R(n,k) = E[#missing]/Pr(#missing > 0)`; also
   `Pr(A_π ∧ A_π')/Pr(A_π)Pr(A_π')` for `π' = π ∘ (adjacent transposition)` and for dihedral images. If `ln R` grows
   like `k ln k − O(k)` the aggregation problem changes character entirely; if `R = e^{O(√k)}` the union bound is
   essentially tight and speed `k ln k` is unavoidable.
3. **Exact second-moment diagnostics for "is the identity the hardest pattern?" (Ch. 4.3, §B.2).**
   `E X²/(EX)²` is computable exactly for `k ≤ 6` and heuristically `1 + Σ_j c_j(π)(k²/N)^j/j!`; the clustering
   coefficients `c_j(π)` are `≈ j!` for the identity and `≈ 1` for random `π` (data in §B.2). Heavier clustering at
   equal mean means more mass at `X = 0` — a *mechanism* for the observed "identity hardest" ordering, and a
   quantity that can be tracked to `k = 6–8` (numerically via `Δ` in the label model) to see whether the ordering
   persists or crosses. Not a proof tool for the gap.
4. **Talagrand for the identity with explicit constants (p. 120).** `Pr(LIS(Π_{Ck²}) < k) ≤ 2exp(−(2√C−1)²k/(8√C))`
   (speed `k`, e.g. `k/8` at `C = 1` versus `η(1) = 0.035` from Thm 11). Only for the identity (the Lipschitz
   property of "longest embedded prefix" fails for general `π`, §B.4). A remark for the paper, not a way forward.
5. **Shearer / Han (15.7, pp. 286–290)** for counting structured classes of patterns. Since (E) is false and the hard
   class `𝓕` is of size `e^{Θ(k ln k)}` in every dihedral image (W14/W15), entropy inequalities cannot shrink what is
   already too large; usable only for bookkeeping of certificate counts in item 1.

Everything else in the book is a dead end for this gap; the list with reasons is §C.

---

## B. Per-technique assessment

### B.1 Janson's inequalities, extended Janson, Suen, Brun's sieve (Ch. 8; also 10.1, 10.3)

**Statements (pp. 128–129, 133, 142–143).** Setting: `R ⊆ Ω` random with independent inclusions `p_r`; `B_i = {A_i ⊆ R}`,
`i ~ j` iff `A_i ∩ A_j ≠ ∅`, `μ = Σ Pr(B_i)`, `Δ = Σ_{i~j} Pr(B_i ∧ B_j)` (ordered pairs), `M = Π(1−Pr B_i)`,
`Pr(B_i) ≤ ε`.
- Thm 8.1.1 (Janson): `M ≤ Pr(∧ B̄_i) ≤ M e^{Δ/(2(1−ε))}` and `Pr(∧ B̄_i) ≤ e^{−μ+Δ/2}`.
- Thm 8.1.2 (extended Janson, `Δ ≥ μ`): `Pr(∧ B̄_i) ≤ e^{−μ²/(2Δ)}`. (Proof p. 131–132: apply 8.1.1 to a random
  `p`-subfamily with `p = μ/Δ`.)
- Thm 8.7.2 (Janson lower tail): `Pr(X ≤ (1−γ)μ) < e^{−γ²μ/(2+2Δ/μ)}`.
- Thm 8.7.1 (Suen): `|Pr(∧B̄_i) − M| ≤ M(e^{Σ y(i,j)} − 1)` in an arbitrary probability space with a
  superdependency digraph; p. 142 remarks that Janson's proof needs only the two correlation inequalities
  `Pr(B_i | ∧_{j∈J} B̄_j) ≤ Pr(B_i)` and `Pr(B_i | B_k ∧ ∧_{J} B̄_j) ≤ Pr(B_i | B_k)` for `J` non-adjacent to `i`.
- Thm 8.3.1 (Brun's sieve): if `E C(X,r) → μ^r/r!` for every fixed `r` then `X → Poisson(μ)`.
- Lemmas 8.4.1–8.4.2 (pp. 135–137): `Pr(∃ disjoint family of size s) ≤ μ^s/s!`, and the maximal-disjoint-family
  version `≤ (μ^s/s!) e^{−μ_s + Δ/2}` — this is how the book gets *two-sided* large deviations for counts (8.5).

**Formulation for pattern containment.** The Poisson model is not literally of the form "random subset of `Ω`", but its
standard discretisation is: tile the square into `M×M` cells (`M → ∞`), occupy each cell independently with
`p = N/M²`; then a potential copy is a `k`-set `I` of cells in `π`-configuration, `B_I = {all cells of I occupied}`,
`I ~ J` iff they share a cell. Janson applies verbatim, and `Pr(∧ B̄_I) → Pr(π ⊄ Π_N)` as `M → ∞`. Then
`μ = N^k/(k!)²·(1+o(1))`, i.e. `ln μ = k(2 + ln C) + O(ln k)`: the first-moment threshold is `C = e^{−2}`.

**Orders of `μ` and `Δ` (heuristic, then a theorem).** Condition on `B_I`; the expected number of other copies `J` with
`|I ∩ J| = j` is, by the symmetry "k uniform points form π with j labelled points in prescribed roles with
probability `(k−j)!/(k!)²`",
```
Δ_j / μ²  ≈  C(k,j) · (k)_j · N^{−j} · c_j(π),        (k)_j = k!/(k−j)!,
```
where `c_j(π)` is the correction from the shared points sitting in "copy-like" rather than uniform positions. So
`Δ_1/μ² ≈ c_1/C`, `Δ_2/μ² ≈ c_2/(2C²)`, …, and `Δ/μ² ≈ Σ_{j≥1} c_j C^{−j}/j!` — **`Δ ≍ μ²`, never `Δ ≪ μ²`**, at
every `N = Ck²`. (At `j = k − m` the terms are `≈ μ^{−1}(Ce³/β³)^{βk}`, `β = m/k`, negligible once `μ` is large.)
Exact values for `k = 4, 5` are in §B.2 and confirm `Δ_1/μ² = k²/N · c_1` with `c_1 ∈ [0.97, 1.37]`.

Consequently the extended Janson exponent is `μ²/(2Δ) ≈ (2Σ_j c_j C^{−j}/j!)^{−1} = O(1)` and the basic inequality
`e^{−μ+Δ/2}` is vacuous as soon as `μ > 2C`. This is not an artefact of taking *all* copies:

**Proposition B.1 (Janson is capped at exponent `C/2`).** Let `𝓘` be any family of `k`-sets of cells and let
`B_I ⊆ {all cells of I occupied}` be up-sets (e.g. "the cells of `I` contain a copy of `π` in the prescribed roles").
Then `Δ ≥ (1 − o(1)) μ² k²/N = (1−o(1)) μ²/C` as `M → ∞`.
*Proof.* For `I ∩ J = S ≠ ∅`: `Pr(B_I ∧ B_J) = p^{|S|} Pr(B_I ∧ B_J | x_S = 1) ≥ p^{|S|} Pr(B_I|x_S=1)Pr(B_J|x_S=1)`
(Harris, Thm 6.3.2, applied to the remaining coordinates) `= Pr(B_I)Pr(B_J)/p^{|S|} ≥ q_I q_J/p`. Summing over cells
`c` and pairs `I ≠ J ∋ c` and using Cauchy–Schwarz on `Σ_c(Σ_{I∋c} q_I)² ≥ (kμ)²/#cells`:
`Δ ≥ (1/p)[k²μ²/#cells − k Σ_I q_I²] ≥ μ²k²/N − k p^{k−1}μ`, and `p·#cells = N`. ∎
Hence for **any** family of configuration events, at `N = Ck²`: extended Janson `≤ e^{−C/2}`, Janson's lower tail
(8.7.2) `≤ e^{−γ²C/2}`, the maxdisfam bounds (8.4.2) carry the same `e^{Δ/2}`, and Suen's `Σ y(i,j) ≥ Δ` is `Θ(μ²)`.
To get exponent `k ln k` from Janson one needs `N ≥ 2k³ ln k`, worse than the trivial union bound at `k² ln k`. The
same cap holds at `N = k² polylog k` (He–Kwan's `2000k² log log k` gives `≤ 1000 log log k`).

**Brun's sieve at the first-moment threshold `N ≈ k²/e²`.** Requires `E X²/μ² → 1`; but `E X²/μ² ≈ 1 + Σ_j c_j C^{−j}/j!
≥ e^{e²}` at `C = e^{−2}`. The number of copies is nowhere near Poisson; copies come in clusters. This is consistent
with, and explains, the gap between the first-moment absence threshold `k²/e² = 0.135k²` and the true universal
absence threshold (`≥ 0.1925k²` by W12, conjecturally `k²/4`). **Dead.**

### B.2 Second moment (Ch. 4)

**Statements.** Chebyshev 4.1.1 (p. 45); `Pr(X=0) ≤ Var X/(EX)²` (4.3.1, p. 50); `Var X ≤ EX + Δ` and the symmetric
form `Δ = Δ* EX` (Cor. 4.3.4–4.3.5, pp. 50–51); balanced-subgraph thresholds 4.4.2 (p. 52) and the clique-number
computation 4.5.1 (pp. 55–56), where `Δ*/E X = Σ_i g(i)` with `g(2) ~ k⁴/n²` is exactly our `j = 1` term.

**Exact computation.** `secmom.c` (this directory) computes, for a uniform permutation of length `n`,
`E X² = Σ_{u=k}^{2k} C(n,u) A_u/u!` with `A_u = #{(ρ∈S_u, I, J): |I|=|J|=k, I∪J=[u], ρ|_I ≅ ρ|_J ≅ π}` by brute force.
Results (`E X²/(EX)²`, and the overlap-`j` contributions `Δ_j/μ²`):

| `π` | `n` (`C = n/k²`) | `EX²/EX²` | `j=1` | `j=2` | `j=3` | heuristic `k²/n` |
|---|---|---|---|---|---|---|
| 1234 | 16 (1.0) | 1.720 | 0.58 | 0.177 | 0.013 | 1.0 |
| 2413 | 16 (1.0) | 1.231 | 0.325 | 0.101 | 0.005 | 1.0 |
| 1234 | 96 (6.0) | 1.074 | 0.212 | 0.020 | 7.4e−4 | 0.167 |
| 2413 | 96 (6.0) | 1.015 | 0.162 | 0.011 | 4.3e−4 | 0.167 |
| 12345 | 24 (0.96) | 2.072 | 0.70 | 0.71 | 0.33 | 1.04 |
| 25314 | 24 (0.96) | 1.287 | 0.50 | 0.35 | 0.13 | 1.04 |
| 12345 | 150 (6.0) | 1.099 | 0.229 | 0.026 | 1.4e−3 | 0.167 |
| 21435 | 150 (6.0) | 1.061 | 0.200 | 0.018 | 8.0e−4 | 0.167 |
| 25314 | 150 (6.0) | 1.021 | 0.165 | 0.013 | 5.8e−4 | 0.167 |
| 31524 | 150 (6.0) | 1.023 | 0.167 | 0.013 | 5.9e−4 | 0.167 |

(The `j = 0` term is `< 1` at finite `n` because disjoint position sets are hypergeometrically negatively correlated;
it tends to 1.) Reading off `c_j = (Δ_j/μ²)/(C(k,j)(k)_j/n^j)` at `n = 150, k = 5`: identity `c_1 = 1.37, c_2 = 3.0,
c_3 = 8.0` (`≈ 1.3–1.5·j!`); 25314: `c_1 = 0.99, c_2 = 1.4, c_3 = 3.2`. So for the identity `Δ/μ² ≈ Σ_j C^{−j}` (diverging
for `C ≤ 1`, `≈ 1/(C−1)` above), for random-like `π` `Δ/μ² ≈ e^{1/C} − 1`.

**Assessment.** Chebyshev gives `Pr(π ⊄ Π_N) ≤ Var X/μ² = Θ(1)`: a *constant* failure probability, uniform over
patterns with bounded `c_j`, e.g. `≤ e^{1/C} − 1 < 1` for `C > 1/ln 2 = 1.44`. Dominated by Thm 11 (w.h.p. at
`0.757k²`). Not a route to the gap; the value is diagnostic (item 3 of §A): the identity's copies cluster the most
(`c_j ≈ j!`: shared points of an increasing chain are already ordered), consistent with the identity being the hardest
pattern at finite `k` (paper, §Random). Note also that `c_j` *must* blow up for every `π` at intermediate `j` when
`C < 0.1925` (W12 absence w.h.p. while `μ → ∞`), so the clustering is universal, not an identity-only effect.

### B.3 Martingales: Azuma, edge/vertex exposure, Alon–Kim–Spencer (7.1–7.5)

**Statements.** Azuma 7.2.1–7.2.2 (pp. 105–106); Lipschitz gradation Thm 7.4.1–7.4.2 (pp. 110–111): if `L` changes by
`≤ 1` when one block `B_{i+1}∖B_i` of coordinates changes, `Pr(L ≤ μ − λ√m) < e^{−λ²/2}`; Thm 7.4.3 (p. 111): with
independent choices of effects `c_i` and total variance `σ² = Σ p_i(1−p_i)c_i²` along every line of questioning,
`Pr(|Y − EY| > ασ) ≤ 2e^{−α²/2(1+ε)}` for `α ≤ σ(1+ε)δ/C`. The chromatic-number trick, Lemma 7.3.1/Thm 7.3.2
(pp. 107–108): choose `Y` = maximal number of *edge-disjoint* `k`-cliques so that `Y` is 1-Lipschitz, get
`Pr(ω < k) = Pr(Y = 0) ≤ e^{−E[Y]²/2m}`. Maurey's concentration on `S_n` is mentioned on p. 105.

**Formulation.** Point-by-point exposure of the `N` i.i.d. points (or of the `M²` cells). Bollobás' trick transfers:
`Y` = maximum number of point-disjoint copies of `π` is 1-Lipschitz in each point, and `Y = 0 ⟺ π ⊄ Π_N`. But
`E Y ≤ N/k = Ck`, so `Pr(Y = 0) ≤ exp(−(EY)²/2N) ≤ e^{−C/2}`. With 7.4.3 in the cell model `σ² = Σ p_c·1 = N`, same.
For `Y = LIS`, deviation `Θ(k) = Θ(√N)`: exponent `O(1)`. **Dead:** the martingale scale `√N = k√C` equals the
deviation we need. (Maurey's inequality on `S_n` for transposition-Lipschitz functions has the same `√n` scale.)

### B.4 Talagrand's inequality (7.6–7.7)

**Statements.** Def. 1 and `Pr[A](1 − Pr[A_t]) ≤ e^{−t²/4}` (p. 116); Thm 7.6.1 (`ρ(A,x) = min_{v∈V(A,x)}|v|`) and
7.6.2 (`∫ e^{ρ²/4} ≤ 1/Pr A`), p. 117; Def. 2 (`f`-certifiable) and **Thm 7.7.1** (p. 119): for `h` Lipschitz and
`f`-certifiable, `Pr[X ≤ b − t√f(b)]·Pr[X ≥ b] ≤ e^{−t²/4}`. **LIS example, pp. 120–121:** `X = LIS` of `n` uniform
points in `[0,1]` (the book's own version of our problem): Lipschitz, `f(s) = s`, `m = Θ(√n)`, so `|X − m| < s`
almost surely for `s ≫ n^{1/4}` — "a much stronger result … Baik, Deift and Johansson (1999)". Then the clique
application (p. 121): `Pr(ω < k) < exp(−Ω(n²/ln⁶n))`, with the remark that extended Janson (10.3) does better.

**Formulation and cap.** (i) `Y` = max number of point-disjoint copies: `f(s) = ks`, median `m ≤ Ck`; `Y = 0` requires
`t = √(m/k) ≤ √C`; so `Pr(π ⊄ Π_N) ≤ 2e^{−C/4}`. (ii) For the identity, `X = LIS`, `m ≈ 2√N = 2√C·k`, `X ≤ k − 1`
gives `t = (2√C−1)√k/√(2√C)` and
```
Pr(LIS(Π_{Ck²}) < k) ≤ 2 exp(−(2√C − 1)² k / (8√C))     (C > 1/4),
```
speed `k` with an explicit constant (`k/8` at `C = 1`, `≈ 0.10k` at `C = 2`), better than Thm 11's `η` but only for
the identity. (iii) One would like to boost Thm 11 for *all* `π` the same way, with `X` = "longest prefix of an
extension `π' ⊇ π` embedded". This fails: removing one point from an embedding of `π'|_{[j]}` leaves an embedding of
`π'|_{[j]∖{i}}`, which is not a prefix, so `X` is not 1-Lipschitz (it is for the identity because every restriction
of the identity is an identity). Using `π' = π^{⊕m}` restores Lipschitz-type control but costs `N ≥ 0.757m²k²`,
so `m = O(1)` and the exponent is `O(1)`. **Dead for speed `> k`**; a certificate of size `k` at `N = Ck²` can never
yield more than `e^{−O(C)}` from Talagrand, and speed `k` only when the functional's median has an `Ω(k)` margin.

### B.5 Kim–Vu polynomial concentration (7.8, p. 121–122)

Thm 7.8.1: for a polynomial `Y` of degree `k` in independent indicators, `Pr[|Y−μ| > a_k(EE')^{1/2}λ^k] < d_k e^{−λ}n^{k−1}`
with `a_k = 8^k k!^{1/2}`, `d_k = 2e²`. Our `X` is a degree-`k` polynomial in the cell indicators, `E' ≥ E_1 ≈ μ/(Ck)`.
Vacuous for `k → ∞` (`a_k λ^k` must be `≤ √(Ck)` for the deviation to be `≤ μ`). **Dead**, as the book itself
warns ("in applications, one generally has `k` fixed").

### B.6 The Local Lemma, lopsided LLL, Moser's fix-it (Ch. 5)

**Statements.** Lemma 5.1.1 (general, p. 70); Cor. 5.1.2 (`ep(d+1) ≤ 1`, p. 71); the *lopsided* remark (pp. 71–72):
mutual independence may be replaced by `Pr(A_i | ∧_{j∈S} Ā_j) ≤ x_i Π_{(i,j)∈E}(1−x_j)` for all `S` of non-neighbours;
**5.6 Latin transversals** (Thm 5.6.1, pp. 80–81): the lopsided LLL *on the uniform permutation space* with events
`{π(i)=j, π(i')=j'}`, made to work by an injection/swap argument; 5.7 Moser–Tardos (Thm 5.7.3–5.7.5, pp. 83–85)
and the **entropy-compression** proof of Thm 5.7.6 (pp. 85–87): if the algorithm runs long, its log determines the
random bits, so `Pr(run ≥ M) ≤ (#logs)·5^{−M}`.

**Union over patterns.** Bad events `A_π`, `π ∈ S_k`; all are decreasing in the point set, hence for any `S`,
`Pr(A_π | ∧_{π'∈S} Ā_{π'}) ≤ Pr(A_π)` by Harris — the lopsided LLL applies with the *empty* dependency graph and
gives `Pr(∧ Ā_π) ≥ Π(1 − Pr A_π)`, which is just FKG. It proves `Pr(Π_N is a k-superpattern) > 0`: true and useless
(sp(k) ≤ k²). There is no way to make the `A_π` "weakly dependent across `π`": they are all functions of one sample
and all positively correlated; and the LLL never gives probability `→ 1`. The Latin-transversal device (events
`π(i)=j`) has no analogue because `A_π` is not a conjunction of few coordinate events. **Dead for the union.**
Moser's compression idea survives as *certificate counting*, §B.8.

### B.7 Correlation inequalities (Ch. 6)

**Statements.** Four Functions 6.1.1 (p. 90); FKG 6.2.1 (p. 93); Kleitman 6.3.1 (p. 95); **Thm 6.3.2 (Harris with
`p`-biased coordinates, p. 96)**; graph-property version 6.3.3 (p. 96–97); XYZ 6.4.1 for linear extensions (p. 97).

**Uses here.** (a) In the cell model every `{π ⊆ Π_N}` is an up-set, so `Pr(all π contained) ≥ Π_π Pr(π contained)`
and `Pr(A_π ∧ A_π') ≥ Pr(A_π)Pr(A_π')`. (b) Harris is the engine of Prop. B.1. (c) **The union bound's slack:**
`Pr(∪A_π) = E[#missing]/E[#missing | ≥1 missing]`. Positive correlation says the denominator can be large; whether it
is `e^{Θ(k ln k)}` (aggregation is "free") or `e^{O(√k)}` (union bound tight) is exactly what decides whether speed
`k ln k` per pattern is necessary. No inequality gives the needed *lower* bound on the conditional expectation; it is a
structural question, and the experiment in §A item 2 is the cheapest way to learn the answer. (d) XYZ: random linear
extensions of a poset — random permutations conditioned on a set of order relations; no application found.

### B.8 Entropy, Shearer, and certificate counting (15.7 and 5.7)

**Statements.** Lemma 15.7.1 (basic properties, p. 284); subadditivity 15.7.2 (p. 286); Cor. 15.7.3
`|𝓕| ≤ 2^{Σ H(p_i)}`; **Shearer, Prop. 15.7.4** (p. 287): if every coordinate lies in `≥ k` members of `𝒢`, then
`k H(X) ≤ Σ_{G∈𝒢} H(X(G))`; Cor. 15.7.5 `|𝓕|^k ≤ Π|𝓕_i|` (projections); Loomis–Whitney 15.7.6; Chung–Frankl–Graham–
Shearer 15.7.7 (p. 288); Han's inequality, Ex. 15.8.4 (p. 290).

**Relevance to (E).** Shearer bounds the size of a family by the sizes of its projections; it could bound
`#{π ∈ 𝓛_r : ≥ k/(2ℓ_r) long-chain shifts}` only if the property were visible in projections, and W14 showed the
property carries no information about the interleaving word for near-translate runs — the statement is *false*, so
no counting lemma helps. Where Shearer/Han can still be used: bounding the number of certificates in item 1 (e.g.
antichain covers with prescribed projections onto slabs and strips).

**Certificate counting (the promising direction).** Moser's argument (pp. 85–87) is a union bound over the possible
*logs* of a failed run. The cleanest instance for us needs no algorithm at all:

*Identity.* `LIS(Π_N) < k` iff (Dilworth) the `N` points can be partitioned into `k−1` decreasing chains. Union bound
over the `(k−1)^N` assignments; a class of `s` i.i.d. points is a decreasing chain with probability `1/s!`; by
log-convexity `Π s_i! ≥ (⌊N/(k−1)⌋!)^{k−1}`. Hence
```
Pr(LIS(Π_N) < k) ≤ (k−1)^N / (⌊N/(k−1)⌋!)^{k−1} = exp(−N ln(N/(e(k−1)²)) + O(k ln N)) = exp(−N ln(C/e) + o(N)),
```
**speed `N` for every `C > e`**, from a three-line argument. (De-Poissonisation is trivial here since the bound is
monotone.) The loss (`C > e` instead of `C > 1/4`) is the entropy of *non-canonical* covers; the exact count of
permutations with `LIS < k` is `Σ_{λ_1<k}(f^λ)²`, i.e. the RSK/Plancherel large-deviation analysis, which is where
the true rate function comes from. Sub-tasks: canonical (patience-sorting) covers reduce the count — how far?

*Structured classes.* W11's Theorem 9 proves containment of `(12⋯r)^{k/r}` by exhibiting a chain of `m = k/r`
molecules in a poset (Mirsky-type argument + Chernoff on bad boxes). The dual certificate of *absence* is a partition
of the molecule poset into `m−1` antichains. Counting antichain covers of the box grid and multiplying by the
probability that the induced constraints hold gives a bound of the form `e^{−N·φ(C, r)}`; the question is whether
`φ(C,r) > 0` for `C ≥ C_0` *independent of `r`* (this would remove the `poly(r)` from Thm 9's threshold and thereby
close the residual class `r ≤ ln⁴k` at `n = O(k²)` — the exact gap named in the paper). For block-grid patterns
`𝒢(r,h)` the same poset exists (W11 §4). This is the concrete proposal in §A item 1(a).

*General `π`.* Containment is NP-complete (Bose–Buss–Lubiw), so no polynomial certificate of absence exists in
general; but Moser-style *partial* certificates (the failure trace of a specific complete search, e.g. the
Pareto-front DP of W20 restricted to a strip decomposition) may be countable. Also note the reformulation
`Pr(π ⊄ σ_n) = |Av_n(π)|/n!`: speed `N` at `n = Ck²` is literally the statement `|Av_{Ck²}(π)| ≤ (Ck²)!·e^{−cCk²}`,
a Stanley–Wilf-type count in the regime `n = Θ(k²)`. The Marcus–Tardos/Cibulka/Fox bounds `|Av_n(π)| ≤ L(π)^n` with
`L(π) = 2^{Θ(k)}` (typical `π`) are useless there (they need `n ≥ e·L(π)`), so this is a genuinely new regime for
avoider counting, not covered by existing enumerative results.

### B.9 Poisson paradigm for "most patterns" at `k²/e²`, and dependent random choice

*Second moment for the `k²/e²` threshold.* Paley–Zygmund gives `Pr(π ⊆ Π_N) ≥ μ²/E X² = 1/(1 + Δ/μ² + 1/μ)`, a
constant lower bound on containment for every `π` with bounded `c_j`, at every `C` where `Δ/μ²` stays bounded; it
cannot locate a threshold and is dominated by Thm 11. The universal absence threshold `≥ 0.1925k² > k²/e²` (W12)
shows that for every `π` the `c_j` diverge somewhere in `C ∈ (e^{−2}, 0.1925)`; a computation of `E X²/μ²` at
`k = 6–8` across `C ∈ [0.1, 0.5]` (feasible: `A_u` for `u ≤ 12` by DP over `ρ` with pruning) would show *where*,
pattern by pattern — a cheap complement to the W16/W21 "identity hardest" numerics.

*Dependent random choice* (Lens, pp. 317–319; Lemma 1 there): a random `r`-set's common neighbourhood contains a
large set `A_0` all of whose `r`-subsets have `≥ b` common neighbours, then embed a bipartite `H` greedily. Pattern
containment has no bipartite/common-neighbour structure to exploit (the order relations are total, not a sparse
graph); no formulation found. **Dead.**

### B.10 Appendix A (large deviations)

A.1.4/A.1.7 (`e^{−2a²/n}`), A.1.12–A.1.13 (binomial upper/lower tails), **A.1.15 Poisson tails** (used in Thm 11(a)),
A.1.16–A.1.19 (bounded/variance-form Chernoff, p. 328–330); **A.2.1–A.2.3** (three-point Laplace-transform lower bounds
and the Cramér-type limit `lim (1/n) ln Pr[Z_n > an] = F(λ) − aλ`, pp. 331–334). These are the tools behind our speed-`k`
and speed-`N/r` statements and their matching lower bounds; nothing new, but A.2.3 is the right reference for stating
the fixed-strip lower bound `Pr ≥ e^{−N/r}` (W11) as an exact rate.

---

## C. Dead ends (provable or definitive)

1. **Janson, extended Janson, Janson lower tail, Suen, Brun's sieve, maxdisfam lemmas** on any family of copy events:
   exponent `≤ N/(2k²) = C/2` (Prop. B.1). Requires `N ≥ 2k³ ln k` to reach `k ln k`.
2. **Second moment / Chebyshev / Paley–Zygmund:** constant probabilities only; `Var X/μ² = Θ(1)` at every `N = Ck²`,
   and `→ ∞` for `C < 0.1925` (forced by W12).
3. **Azuma / McDiarmid / Alon–Kim–Spencer / Maurey on `S_n`:** deviation `Θ(√N)`, exponent `≤ C/2`.
4. **Talagrand:** exponent `≤ C/4` for disjoint-copy functionals; speed `k` (never more) for Lipschitz-certifiable
   functionals with `Ω(k)` margin, and the natural "embedded prefix" functional is not Lipschitz for general `π`.
5. **Kim–Vu:** constants `8^k k!^{1/2}`, degree `k → ∞`.
6. **LLL in all forms for the union over `S_k`:** the absence events are positively correlated; lopsided LLL reduces to
   FKG and gives only positivity. LLL is an existence tool, and existence (`sp(k) ≤ k²`) is not the question.
7. **Poisson approximation of the copy count** at any `N = Ck²`: `E X²/μ² ≥ e^{1/C}·(…) ≠ 1`.
8. **Dependent random choice:** no formulation.
9. **Stanley–Wilf-type avoider counts** (`|Av_n(π)| ≤ L(π)^n`): need `n ≥ e·2^{Θ(k)}`.
10. **Shearer/entropy to rescue (E):** the statement is false (W14), and the hard class is `e^{Θ(k ln k)}` (W15).
11. **Templates / class-superpatterns** ("cover `S_k` by classes each contained in one structured pattern `Π_𝓒` of
    length `Lk` with speed-`N` containment"): a template of length `Lk` covers `≤ (eL)^k` patterns, so `L = O(1)`
    is needed, but a random `π` does not embed in any block-grid pattern of length `≪ k²` (a `r×h` grid decomposition
    without cell collisions needs `rh ≳ k²`), and the only templates with proven speed `N` are block-grid/periodic.

---

## D. Material on random permutations in the book (for the record)

- p. 19: fixed points of a uniform permutation, `E = 1` (linearity).
- p. 11, Thm 1.3.3 (Bollobás set-pairs): random order of `∪(A_i ∪ B_i)`, events "all of `A_i` precede `B_i`" are disjoint.
- p. 17, **Ex. 1.10**: an `n×n` matrix with distinct entries has a row permutation such that no column contains an
  increasing subsequence of length `≥ c√n` (first moment `C(n,ℓ)/ℓ!` on the LIS of a random permutation — the only
  Erdős–Szekeres-flavoured item; there is no probabilistic-lens on LIS/Ulam/Hammersley).
- p. 18, Lens (Erdős–Ko–Rado): Katona's proof with a random cyclic order.
- p. 28, Ex. 2.7: Sperner/LYM via a random permutation.
- p. 29–30, Lens (Brégman): random `σ ∈ S` and random `τ ∈ S_n` in the permanent bound; p. 65–67, Lens (Hamiltonian
  paths): Szele's `n!/2^{n−1}` and Alon's matching upper bound via permanents.
- p. 80–81, **5.6 Latin transversals**: lopsided LLL on the uniform permutation space (Erdős–Spencer); the injection
  `π ↦ π*` showing `Pr(A_{ij i'j'} | ∧ Ā) ≤ 1/(n(n−1))`.
- p. 100, Lens (Turán): Caro–Wei via a random total order.
- p. 105: Maurey's martingale isoperimetric inequality on `S_n`.
- p. 120–121: **LIS via Talagrand**, `|X − m| < s` for `s ≫ n^{1/4}`; reference to Baik–Deift–Johansson.
- p. 38–41, 3.6 (continuous time): random greedy packing via i.i.d. birth times = random orderings; the "Menendez
  rule" tree — the Poisson-clock viewpoint we use in the renewal sweeps (W17), no large-deviation content.
- p. 195, Lens (Counting subgraphs): union bound over partial isomorphisms `ρ` grouped by `|{x: ρx ≠ x}|` — the same
  bookkeeping as our structured union bounds.

Files: `secmom.c` (exact second moment), `secmom_k4_*.out`, `secmom_k5_*.out` (data for §B.2), `log.md`.
