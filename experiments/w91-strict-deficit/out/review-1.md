# W91 — independent adversarial review 1

Date: 10 November 2026 (13:10–13:45). Reviewer: a subagent that took no part in writing the proof.
Scope: `experiments/w91-strict-deficit/proof.md` §1–§7, taking `../w90-layered-deficit/proof.md` §1–§2
(definitions, Lemmas 1–4, Theorem 1 with (★), Corollary 2) as given. `gadget_check.py` was not read at any point.

## 0. Which text was reviewed — the file changed during the review

| Version | Lines | md5 | Theorem B | Status |
|:--|--:|:--|:--|:--|
| v1 | 443 | `1bb7d42322d4b7d95eaa050749391196` | c·√n/(ln n)¹⁰, c_B = 10⁻¹⁸ (K = ⌈2 ln T⌉, thin threshold 1/(8 ln T)) | the version the review request describes; read at 13:10; kept by the main session as `proof_v1_log10.md` in the scratch directory |
| v2 | 468 | `5503bbc67ded37f083e2504b241c4a79` | c·√n/ln n, c_B = 10⁻⁹⁴ (K = ⌈45 ln T⌉, constant thin threshold 10⁻¹⁰, new Lemmas 4.2, 4.3) | written to `proof.md` at 13:20:12, still the current file at 13:42 |

`diff` of the two versions: §1–§3 (lines 1–226) are identical except the title and three lines of the summary
table. §4–§7 differ: v1 Lemma 4.2 (long chains have few thin steps) is v2 Lemma 4.1 and v1 Lemma 4.3 (elementary
bounds) is v2 Lemma 4.4; v1 Lemma 4.1 (no chain of many thin steps, threshold 1/(8 ln T)) is replaced by v2
Lemma 4.2 (area budget of a window) and v2 Lemma 4.3 (windows of bounded area have few thin steps); Proposition 6.1
is rewritten accordingly. **Both versions of §4–§6 were re-derived.** Lemma numbers below are those of v2 unless
marked (v1).

## Verdict

| Statement | Verdict |
|:--|:--|
| Theorem A (Σ_p Δ_p ≥ 10⁻⁸⁰·T) | **Holds** (v1 and v2; same proof). |
| Theorem B, v1: D(n) ≥ 10⁻¹⁸·√n/(ln n)¹⁰ | **Holds.** |
| Theorem B, v2: D(n) ≥ 10⁻⁹⁴·√n/ln n | **Holds.** The new steps (Lemmas 4.2, 4.3, event 𝒜 in Prop. 6.1) were re-derived with no issue. |
| Corollary C (v1 with (ln k)⁻¹⁰, v2 with 1/ln k) | **Holds** given Baik–Deift–Johansson and Talagrand; three routine sentences are missing (U9). |
| Prop. 7.1 (conditional on (H)) | Holds as a conditional statement; constant as printed is off by the floor in J (C2). |

**No fatal error and no repairable mathematical gap was found in §1–§6 of either version.** What follows are
under-justified steps (true, I supplied the missing argument each time) and cosmetic points. Dependencies that this
review did not re-prove: W90 §1–§2 (by instruction), the multivariate Mecke formula, BDJ, Talagrand's inequality
(the theorem numbers quoted for Last–Penrose and Alon–Spencer were not checked against the books).

--------------------------------------------------------------------------------------------------
## Part 1 — line-by-line review

### 1.1 Findings, in order of severity

**Fatal:** none. **Repairable gaps (a needed statement that is false or unproved as written):** none.

**Under-justified steps (correct; each needs one or two sentences).**

- **U1. Lemma 1.2**, "So a = 2 and (a−1)/F = ⅓ in formula (★) of W90, Theorem 1, whose other terms are
  non-negative." (★) is a statement about uniform σ_n and its fibres; the lemma is about the Poisson P and the event
  "lens at (α, b)". Two things are used silently: conditioning on |P| = n (stated once under **Model**), and that
  "P has a lens at (α, b)" is a function of (O, X, Y) alone, hence constant on fibres, so that
  E[(a−1)/F] ≥ E[⅓·1{lens}]. Repair: add that sentence. I re-derived F = 3, a = 2 (321 has the D-inversion in
  columns 1, 2 with corners (x₁,y₂), (x₂,y₃) ∈ D; in 231 the corners are (x₁,y₁) ∉ U and (x₃,y₃) ∉ S; in 312 they
  are (x₁,y₁) ∉ U and (x₃,y₃) ∉ S).
- **U2. Lemma 2.4**, "exchanging the two pairs if necessary, e′ is NW of e" and "exchanging the pairs if
  necessary x′ is NW of x". Legitimate, but only because every hypothesis used afterwards is symmetric in the two
  pairs (membership in 𝒢_{p,s}, h(x) = h(x′), Q = Q′, and in the second step e = e′). I wrote out the mirrored
  argument (e NW of e′ ⇒ e violates (O5) for (e′,x′), using (O3) for (e,x)) and it goes through verbatim.
  Also "both have the same inside set {p₁,p₂,p₃} (p₁ < p₂, and p₃ is the third point)": the *labels* agree
  because among the three inside points exactly one pair is comparable; worth saying, since Q = Q′ is derived from
  the labelled points p₁, p₂.
- **U3. Lemma 3.1**, "By the bivariate Mecke formula … ∫∫ E f(e, x, P) de dx". Used silently: e, x ∉ R(e,x)
  (open rectangle), so adding the two points does not change P ∩ R; R(e,x) ⊂ Q_T, so the intensity of R is its
  area; Φ is measurable. The independence of P ∩ R and P ∖ R is applied *after* Mecke, for deterministic e, x,
  which is the legitimate order. P(P ∩ R ≅ π_s) = e^{−A}·A^m/m!·1/m! is right (given m points, they are i.i.d.
  uniform in R and the order type is uniform on S_m).
- **U4. Lemma 4.3 (v2)**, "There is an integer r with |r| ≤ R₀ such that W ≤ M·2^r and H ≤ 2M·2^{−r}". The two
  inequalities are shown; r ≤ R₀ in the first case is not. It holds: W ≤ T and M = 2k ≥ 2 give
  r = ⌈log₂(W/M)⌉ ≤ ⌈log₂T⌉ − 1 < R₀. The last display also uses (A₁/2)^{⌈k/2⌉/2} ≤ (A₁/2)^{k/4}.
- **U5. Lemma 4.1 (= v1 Lemma 4.2)**: (2√A₁)^{⌈k/2⌉} ≤ (2√A₁)^{k/2} needs 2√A₁ ≤ 1 (v1 assumed A₁ ≤ ¼; v2 fixes
  A₁ = 10⁻¹⁰ but no longer says why the rounding is harmless).
- **U6. Theorem A, remark after the statement**, "Σ_{p≥3T} Δ_p(T) ≤ E[|P|²; LIS(P) ≥ 3T] → 0 (Lemma 4.4(iii))".
  Needs Cauchy–Schwarz with E|P|⁴ = O(T⁸). Not used in the proof of Theorem A itself.
- **U7. Prop. 6.1**, "using J ≥ 3·10⁻⁴·T/ln T" (v2) / "J ≥ 0.007·T/ln T" (v1). True only for T/ln T ≳ 3·10⁴
  (v2) resp. 7·10³ (v1), i.e. T_B is larger than the standing assumption ln T ≥ 10 suggests. Harmless.
- **U8. Proof of Theorem B**, "D(n) ≥ E D(|P|) − 7 ln n − o(1)": the o(1) is E[|P|; ||P|−n| > r], which needs
  Cauchy–Schwarz; "E LIS(σ_m) ≤ 3√m for large m" is applied to all m ∈ [n−r, n+r], fine.
- **U9. Corollary C.** (i) "fluctuations of order n^{1/4} around the median, in particular
  P(L₂₁ ≥ E L₂₁ + n^{1/3}) → 0" needs |E L₂₁ − median| = O(n^{1/4}) (standard consequence of the same inequality).
  (ii) "E L₂₁(σ_n) ≤ √n − (c_B/3)·√n/ln n" uses E LIS ≤ 2√n + O(n^{1/6}). (iii) "this holds for n ≤ …": the
  statement is for all n below the threshold; say that P(σ_n ⊇ τ) is non-decreasing in n (or that n ≥ k → ∞ and
  √n(1 − c/ln n) is increasing). Directions of all inequalities are correct.

**Cosmetic.**

- **C1. §8**, "an independent adversarial review is recorded in log.md". `log.md` (13:20) contains no such
  entry; this file is the review.
- **C2. Prop. 7.1**, "≥ κ·a⁸/(12·K²·(8!)²)·T for large T". With J = ⌊κT/K⌋ the bound is that expression minus
  O(1); the consequence for c₂₁ is unaffected. The step "hence c₂₁ ≤ …" also needs the de-Poissonisation of
  Lemma 6.2 (available).
- **C3.** Remark 2.6 sits between Lemma 2.4 and Lemma 2.5.
- **C4. Lemma 2.1(b)**: the "In particular" clause does not need ℓ(q) ≥ T₀+1 and is used without it in
  Lemma 2.3 ("ℓ(q) ≥ ℓ(e)+1"); the proof given ("(a) with t = ℓ(r)−1") covers this.
- **C5. Lemma 2.3**, "By Lemma 2.1(a),(d) … inside … iff ℓ(q) ≥ p+1 and h(q) ≥ b+1": the level half is the
  definition of ℓ, not Lemma 2.1(a).
- **C6. Lemma 2.5**: (O5), (O6) are obtained without the emptiness clauses and (O4) for every r, not only class
  (c) — stronger than stated.
- **C7.** "level" denotes both ℓ and the lens index b (Lemma 2.4, Remark 2.6); §5 says "A₁-thin", §4 "thin".

### 1.2 Lemma-by-lemma record

**§1.**
- (F1), (F2): re-derived, no issue.
- (F3), odd prefix lengths: W_S[1..2m+1] = (B₁ ⊕ ⋯ ⊕ B_m) ⊕ 1 whether or not m+1 ∈ S, because the first entry of
  block m+1 is a new maximum in both cases; only complete blocks i ≤ m are replaced, each by Theorem 1 of W90 with
  β containing the trailing single point. Re-derived, no issue. Exact check below (§1.3).
- Lemma 1.1: for fixed t the telescoping over the elements of S that are ≤ t/2 is correct;
  W_{S_{m−1}}[1..t] = α_{i_m} ⊕ 12 ⊕ I_{t−2i_m} holds because blocks after i_m are 12 in S_{m−1} and S_m;
  stage i collects exactly the t ≥ 2i. Cost_S(i) depends on S only through S ∩ [1, i−1] (by the definition of
  α_i). The consequence uses 2 E L₂₁ ≤ E N_{W_ℕ} ≤ E N_{W_S}, correct direction. Re-derived, no issue.
- Lemma 1.2: see U1.

**§2.**
- Lemma 2.1 (a)–(d): re-derived, no issue. (a) uses Π[1..t+1] = Π[1..t] ⊕ 1, valid exactly for t ≥ T₀.
- Classes: the claim "class (c) points lie NW or SE of the whole rectangle" is correct (the other two sign
  combinations are contradictory).
- Lemma 2.2: re-derived, no issue. Every quantity in (O1)–(O6) is ℓ of e or of a class (a) point (SW avoids R),
  h of x or of a class (b) point (NE avoids R), both for class (c), or the emptiness of a set disjoint from R.
  The classes themselves are subsets of P ∖ (R ∪ {e,x}). So the conditions do not depend on the points in R.
- Planted order types: the list of order relations of 3416725 is exactly right (checked all 21 pairs).
- Lemma 2.3: re-derived, no issue. Levels a: ℓ(e)+1; u₁, u₂: p; p₁, p₃: p+1; p₂: p+2 (v₁: p+3, v₂: p+2).
  Heights v₁, v₂: b; p₂, p₃: b+1; p₁: b+2 (u₁: b+3, u₂: b+2, a: b+4). Inside set: (O2) kills class (a) and e,
  (O3) kills class (b) and x, (O4) is exactly "no class (c) point is inside". Each of the nine cells was checked:
  below (x₁,y₁) only a, e, class (a) (levels ≤ p−1); (x₁,y₂) > u₁, (x₂,y₁) > u₂; above (x₃,y₃) only x, class (b)
  (heights ≤ b−1); (x₂,y₃) < v₁, (x₃,y₂) < v₂. Lemma 2 of W90 is used in the right direction (U_α(O) = U_α(P)).
- Lemma 2.4: re-derived, no issue beyond U2. Q ∩ SW(p₂) = {q < p₂ : ℓ(q) ≥ p−s} and Q ∩ NE(p₁) = {q > p₁ :
  h(q) ≥ b} are correct for s = 0 and s = 1, and Q is the union of these with {p₁,p₂,p₃}.
- Remark 2.6: re-derived, no issue (inside sets are nested in b; the rightmost inside point has h = b+1).
- Lemma 2.5: re-derived, no issue.

**§3.**
- Lemma 3.1: see U3; no issue. Independent leading-order check with a 21-block (mine, by hand): B = (21), p = 4,
  s = 0. Left side: the only 11-point order type with 𝒢 ≠ ∅ is 21 ⊕ 1 ⊕ 3416725 ⊕ 1, giving e^{−T²}T²²/(11!)².
  Right side: four points of type 2134, e^{−T²}(T⁸/4!)·(1/4!)·(E S⁷)²·T¹⁴/(7!)² with S ~ Beta(1,4),
  E S⁷ = 7!·4!/11!, again e^{−T²}T²²/(11!)².
- Lemma 3.2: re-derived, no issue. i = p−s−1 ≥ T₀+1 and i < N are exactly the hypotheses of Lemma 2.5.

**§4.** (numerics recomputed: 1−e⁻¹ = 0.63212, 4e⁻⁴ = 0.07326, 2e⁴(2·10⁻⁵)^{1/2} = 0.4883,
2·0.132²·2 = 0.0697, 16e²(5·10⁻¹¹)^{1/4} = 0.3144; v1: V(ln T = 10) = 0.3173, decreasing in T)
- Lemma 4.1 (v1 4.2): re-derived, no issue (U5).
- Lemma 4.2 (v2 only): re-derived, no issue. The diagonal-cell argument works for every aspect ratio.
- Lemma 4.3 (v2 only): re-derived, no issue (U4). The substitution gives 8·P(E₁E₂ < A₁/8) ≤ 8·√(A₁/2).
- v1 Lemma 4.1 (all steps thin): ∫₀^T min(T, A₁/w) dw = A₁(1 + ln(T²/A₁)), correct.
- Lemma 4.4 (v1 4.3): Hoeffding exponents 2·0.1² = 0.02 and 2·0.01² = 2·10⁻⁴; thresholds T ≥ 47.9 and T ≥ 42;
  (iii) with k = ⌈3T⌉. Re-derived, no issue.

**§5 Theorem A.** Re-derived, no issue. Lemma 3.2 is applied with the empty block word, s = 0, p ≥ 2; the sum over
p = 2..L is Σ_{i=1}^{L−1}; on 𝒜 more than (L−1)/2 ≥ T/4 steps are not thin; constant 10⁻⁷⁰/(24·7!²) = 1.64·10⁻⁷⁹.

**§6 Proposition 6.1 (index bookkeeping, both versions).**
- (6.1): Lemma 1.1 for each S, averaged; Cost_S(i_j) is a function of (i₁,…,i_j) only. Correct.
- Π = W_{{i₁,…,i_{j−1}}} does not depend on the candidate i, so N and (z_ι) are the same for the whole window:
  correct. α_i = Π[1..2i−2] because blocks strictly between i_{j−1} and i are 12 in both.
- p = 2i−2 ≥ T₀+2K ≥ T₀+s+2: correct. ι = p−s−1 ∈ {2i−3, 2i−4}; over i = i_{j−1}+K+1, …, i_{j−1}+2K this is
  each of ι₀, …, ι₀+2K−1 once, ι₀ = 2i_{j−1}+2K−2 ≥ T₀+1: correct. 1{N ≥ p−s} ≥ 1{N ≥ ι₀+2K}: correct.
- Averaging s = 0, 1 for the same i (not adding): correct, no double counting.
- ι₀+2K = 2i_{j−1}+4K−2 ≤ 4K(j−1)+4K−2 < 4KJ ≤ 0.06·T: correct. P(N ≥ t) ≥ P(2L₂₁ ≥ t) by (F3), (F2): correct.
- v1: no chain of 2K thin steps (T²·3^{−4 ln T} ≤ T⁻²) ⇒ one non-thin step in the window; total
  0.007/(12·2.1·8!²·8⁸) = 1.018·10⁻²⁰. Correct.
- v2: a chain inside R(z_{ι₀}, z_{ι₀+2K}) has ≤ 2K−1 points (levels are strictly increasing in the tail and
  ℓ(z_{ι₀}) ≥ T₀+1) ⇒ by (b) span area < 4(2K)² ⇒ by (c) fewer than K thin steps. Correct.
  T⁴e^{−0.069·90 ln T} = T^{−2.21}; A₁⁸/(12·8!²) = 5.126·10⁻⁹¹; 0.015/45.1 = 3.33·10⁻⁴. Correct.
- Lemma 6.2 and de-Poissonisation: re-derived, no issue (U8).
- Corollary C: see U9.

**Use of identity-only properties when the pattern has 21-blocks.** I looked for each use of "levels increase
strictly along chains" or "equal levels are incomparable": Lemma 2.1(b),(c) (hypothesis ℓ ≥ T₀+1), Lemma 2.3
((O1) puts e, hence all of Q, in the tail; class (a) points may lie in the head but only (O2) is used for them),
Lemma 2.4 (levels p−s−1 ≥ T₀+1 by (O1)), Lemma 2.5 (only i ≥ T₀+1; (O2) treats head points separately), Prop. 6.1
(ι₀ ≥ T₀+1). Heights never involve the pattern (β = I_b throughout). No silent use found. The numerical negative
control below shows that dropping (O1) destroys the conclusion in about 80 % of cases, so the hypothesis is doing
real work exactly where the proof invokes it.

### 1.3 Exact checks of §1 on all of S_n (my code, direct containment)

`section1_exact.py` (scratch), n = 7, 8, 9, for S, S′ among ∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {2,4}, {1,2,3},
{1,2,3,4}:

- (F3) for all pairs S ⊊ S′ and all t ≤ n, odd t included: 210 / 240 / 270 comparisons, **0 violations**.
- Lemma 1.1: Σ_σ (LIS − N_{W_S}) equals Σ_{i∈S} of the stage costs for every S, all stage costs ≥ 0.
  Values: n = 7 all 0; n = 8: 1 whenever 2 ∈ S, else 0; n = 9: 46 whenever 2 ∈ S, else 0 (e.g. S = {1,2,3,4}:
  stage costs [0, 46, 0, 0]). The totals 1 and 46 for 21^{⊕m} agree with W90 §5 (`fibre_cost.py exact`).

--------------------------------------------------------------------------------------------------
## Part 2 — independent numerical certificate for Lemma 2.3 (direct containment)

Script (written without reading `gadget_check.py`):
`/private/tmp/claude-501/-Users-adamhadani-Development-math-proofs-superpatterns/0c33b450-b609-4fd6-9183-ef318e6a7155/scratchpad/lemma23_containment.py`
(md5 `8ec575c0c5126651d5ac9b5c29500ccc`; companion `section1_exact.py`, md5 `ec1b3f2270e7a8215b74a17dff3fd474`, in the
same directory. The scratch directory is session-specific — copy the two scripts into the workstream if they are to
be kept).

Method. Containment of a direct sum of blocks 1 / 21 is decided by a corner dynamic programme
(f[i][j] = "the points with x-rank ≤ i, y-rank ≤ j contain the prefix"), which uses only the meaning of ⊕; no
fibres, fillings, or level formulas. Levels are ℓ(q) = 1 + max{t : SW(q) ⊇ Π[1..t]} from that DP, heights by the
O(n²) chain recursion. A second, generic backtracking matcher (arbitrary patterns, no ⊕ structure) is run on every
fifth planting. Self-test: DP = generic = subset enumeration on 4000 + 3000 random cases;
#{σ ∈ S_n ⊇ 1234} − #{σ ∈ S_n ⊇ 1324} = 1 (n = 7), 26 (n = 8); 145278369 contains 123456 and avoids 124356.

Protocol. Random configurations of 20–40 uniform points; block words ∅, (21), (21,21), (1,21), (21,1,1,21),
(1,1,21,21); all pairs e < x with empty rectangle satisfying (O1)–(O4) are listed, up to 4 per (configuration,
block word, s) are sampled; π_s is planted at uniformly random positions in R(e,x); p = ℓ(e)+s+1, b = h(x)+1,
α = Π[1..p].

```sh
cd /private/tmp/claude-501/-Users-adamhadani-Development-math-proofs-superpatterns/0c33b450-b609-4fd6-9183-ef318e6a7155/scratchpad
python3 lemma23_containment.py selftest
python3 lemma23_containment.py plant 201 400 4 5     # also seeds 202, 203; about 7.5 min each, one core
python3 lemma23_containment.py canon 301 3000
python3 lemma23_containment.py canonplant 401 300
python3 section1_exact.py 9                          # also 7, 8; about 4 min for n = 9
```

Results (seeds 201 + 202 + 203; outputs `plant_201.txt`, `plant_202.txt`, `plant_203.txt` next to the script):

| Quantity | Count |
|:--|--:|
| candidate pairs with empty rectangle and (O1)–(O4), s = 0 / s = 1 | 80 340 / 83 089 |
| plantings tested | **47 428** (identity pattern 9 600; patterns with 21-blocks 37 828; s = 0: 23 714, s = 1: 23 714) |
| N − ℓ(e) − h(x) = 0 / 1 / 2 / 3 (0 = pair on an optimal copy) | 36 373 / 7 328 / 3 092 / 635 |
| Lemma 2.2: ℓ(e), h(x), (O1)–(O4) unchanged by the planting | 47 428 / 47 428 |
| **(i)** planted configuration contains α⊕12⊕I_b and avoids α⊕21⊕I_b | **47 428 / 47 428** |
| **(ii)** among 231, 312, 321: exactly two contain α⊕12⊕I_b, exactly one contains α⊕21⊕I_b | **47 428 / 47 428** |
| detail of (ii) | always 231: (yes, no); 312: (yes, no); 321: (no, yes) |
| inside set for (Π[1..p], I_b) is {p₁,p₂,p₃} (from the definition) | 47 428 / 47 428 |
| board = 3×3 minus (x₁,y₁) ∉ U_α(O), (x₃,y₃) ∉ S_β(O) (from the definition, computed on O) | 47 428 / 47 428 |
| generic matcher against DP (all six arrangements, both patterns) | 113 820 decisions, 0 mismatches, 0 timeouts |
| **counterexamples** | **none** |

**(iii)** The other three arrangements, in all 47 428 cases:

| Arrangement | inside flags of the points in columns x₁, x₂, x₃ | contains α⊕12⊕I_b | contains α⊕21⊕I_b |
|:--|:--|:--|:--|
| 123 | no, yes, no | no | no |
| 132 | no, yes, yes | no | no |
| 213 | yes, yes, no | no | no |

So a point placed on (x₁,y₁) is no longer above a copy of α, a point placed on (x₃,y₃) is no longer below a copy
of I_b, the configuration leaves the fibre, and it contains neither pattern — as the board predicts.

Negative controls (pairs violating exactly one of (O1)–(O4); the lemma does not apply) — the test can fail:

| Violated | tested | (i) fails | (ii) fails | not a lens (definition) |
|:--|--:|--:|--:|--:|
| (O1) | 24 000 | 17 868 | 19 190 | 19 190 |
| (O2) | 18 838 | 3 710 | 5 123 | 5 436 |
| (O3) | 17 933 | 4 676 | 6 738 | 7 073 |
| (O4) | 4 238 | 1 598 | 2 066 | 4 238 |

Bonus checks with the same code (not requested, all from the definitions):

- Lemma 2.4 / Remark 2.6 in each of the 47 428 planted configurations: |𝒢_{p,s}| ≤ #lens levels ≤ 1 always; the
  set of lens levels is exactly {h(x)+1} always; |𝒢_{p,s}| = 0 in 19 407 cases and 1 in 28 021; with (O1)–(O4)
  only there are ≥ 2 pairs in 4 813 cases, so the tie-break (O5), (O6) is needed and sufficient.
- Lemma 2.5 (`canon 301 3000`): 70 144 consecutive pairs (z_i, z_{i+1}); chain, empty rectangle, (O1)–(O6) for
  s = 0, 1 in all; no empty G_i.
- The pair actually used in Lemma 3.2 (`canonplant 401 300`): 14 024 plantings into steps of the leftmost optimal
  copy (9 616 with 21-blocks): (p, b) = (i+s+1, N−i+1) and N(planted) = N+s+4 in all; (O1)–(O6) still hold after
  planting in all (Lemma 2.2 for all six conditions); (i), (ii), inside set, board in all; |𝒢_{p,s}| = 1 exactly
  in all.

Not covered numerically (same as the author's §8): the probabilistic assembly (§4–§6) beyond recomputing the
constants; it was checked by re-derivation only.
