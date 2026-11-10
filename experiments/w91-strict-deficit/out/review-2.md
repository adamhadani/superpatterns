# W91 part 2 — independent adversarial review 2 (`proof-c21.md`: c₂₁ < 1)

Date: 10 November 2026 (15:07–15:25). Reviewer: a subagent that took no part in writing `proof-c21.md` or `proof.md`.
**The file changed during the review.** v1: 109 lines, 8049 bytes, mtime 15:06 (read at 15:07; md5 not recorded).
v2: 110 lines, 8204 bytes, mtime 15:18, md5 `65194cd2a95f5d1cfbf5f6f29eed38f9` (re-read at 15:25). Comparing v2 with
my reading of v1, the only change is Lemma C Step 1 (v2 lines 42–45): the citation is now "4th ed. 2016, Theorem
7.7.1; statement checked against the book", the first factor of Talagrand's inequality is written with ≤ instead
of <, and the choice t = u/√(2b) with "first factor P(Y_n ≤ m_n) ≥ ½" is spelled out. Everything else is
identical. `proof.md` was touched at the same minute (+17 bytes: the same citation in Corollary C, line 388;
§6 unchanged). Line numbers below are those of v2. Both versions of Step 1 were assessed (E2).
Black box, by instruction: (B) = Proposition 6.1 of `proof.md` (re-read for task 3 only, not re-proved).
Not re-proved by this review: W90 Theorem 1 / formula (★) / Corollary 2, Lemmas 2.1–2.5 and 3.1 of `proof.md`,
the Mecke formula, Logan–Shepp / Vershik–Kerov. Talagrand's inequality was checked against a secondary source
(§5.1), not against the book.

## 0. Verdict

| Statement | Verdict |
|:--|:--|
| (S1)–(S5) standing facts | Hold, **except that "(S4) 2Y_n ≤ LIS" is false as a pointwise statement** (σ = 21: Y = 1, LIS = 1). What is true and what is used: Y_n ≤ LIS pointwise, and 2Y_n ≤_st LIS (W90 Cor. 2). No conclusion is affected (E1). |
| Lemma C (upper-tail bound, E(Y − ℓ(T) − 13√T − 20√(T ln T))⁺ ≤ T⁻⁴) | **Holds.** One step is written incorrectly and is repaired in one line (E1); the v1 gap in the median step (E2) is closed in v2; all constants re-derived. |
| Lemma R (ℓ(2T) ≤ 2ℓ(T) + 45√(T ln T)) | **Holds.** Cutting construction, reflection, discretisation and union bound re-derived with no issue; the cutting inequality m ≤ 1 + M + M′ had 0 violations in 3300 sampled configurations and is attained with equality (the "+1" is needed). |
| Corollary R′ (c₂₁T − 200√(T ln T) ≤ ℓ(T) ≤ c₂₁T) | **Holds.** The series constant is 45·3.780 = 170.1 ≤ 200. |
| Theorem D (c₂₁ < 1) | **Holds, given (B).** Every inequality has the right direction; no circularity. The step is elementary once R′ and λ(T) ≤ 2T are available. |
| Corollary E (failure of Alon's conjecture for fixed ε < c₂₁⁻² − 1) | **Holds, given Theorem D.** One silent use of c₂₁ > 0 (E5). |
| (B), task 3 | **Nothing found** that makes the bound vacuous, conditional or restricted (§3). |

**I found no fatal error and no gap that needs a new idea.** After re-deriving every line, the argument of
`proof-c21.md` is the standard rate-of-convergence argument for superadditive functionals and it is correct.
Consequently the entire weight of "c₂₁ < 1" sits on (B) and, through (B), on W90 Theorem 1 with formula (★) and
on Lemmas 1.2, 2.3–2.5, 3.1 of `proof.md`. Those are one day old and have been checked only by AI sessions
(review-1 and brute force for the deterministic part). That, not anything in `proof-c21.md`, is where a human
referee should spend time before any announcement.

## 1. Errors and gaps, by severity

**Fatal:** none. **Gaps needing a new argument:** none.

**Wrong or incomplete as written; repair is one line; conclusions unchanged.**

- **E1. (S4), line 32, and Lemma C Step 3, line 58 (present in v1 and v2).** Quoted: "(S4) 2Y_n ≤ LIS" and "the part
  Y ≥ ℓ(T) + 13√T + 5T forces LIS ≥ 10T".
  *Why wrong:* a copy of 21^{⊕m} contains chains of length m, not 2m. For σ = 21, L₂₁ = 1 and LIS = 1; in S₄,
  2143 has L₂₁ = 2 and LIS = 2. The inequality 2L₂₁ ≤ LIS holds only in distribution: W90 Corollary 2 is
  P(σ_n ⊇ 21^{⊕m}) ≤ P(LIS(σ_n) ≥ 2m). So {Y ≥ 5T} does not "force" LIS ≥ 10T.
  *Where it matters:* (i) the increment bound μ_{n+1} − μ_n ≤ E[2Y_{n+1}]/(n+1) ≤ E LIS(σ_{n+1})/(n+1) and
  m_n ≤ 2μ_n ≤ 3√n use only E[2Y_n] ≤ E LIS(σ_n), which is true (Cor. 2); (ii) Step 3 uses the event.
  *Repair:* in (S4) write "Y_n ≤ LIS pointwise and 2Y_n ≤_st LIS(σ_n) (W90, Cor. 2)". In Step 3 write
  "P(Y ≥ 5T) ≤ P(LIS(P) ≥ 10T) by W90 Cor. 2 applied conditionally on N" (then the printed bound
  (E N²·(e/10)^{20T})^{1/2} stands), or avoid W90 altogether: Y ≤ LIS pointwise gives
  E[N; Y ≥ 5T] ≤ (E N²·P(LIS ≥ 5T))^{1/2} ≤ (E N²·(e/5)^{10T})^{1/2} = o(T⁻⁵).
- **E2. Lemma C Step 1 — a gap in v1, repaired in v2.** v1 quoted Talagrand's inequality with a strict first
  factor, P(Y_n < b − t√(2b))·P(Y_n ≥ b) ≤ e^{−t²/4}, and then wrote "With b = m_n + u and b = m_n this gives
  P(Y_n ≥ m_n + u) ≤ 2e^{−u²/(8(m_n+u))}".
  *Why that was incomplete:* with b = m_n + u and t = u/√(2b) the first factor is P(Y_n < m_n), and a median
  only gives P(Y_n < m_n) ≤ ½. One needs the first factor to be P(Y_n ≤ m_n) ≥ ½.
  *v2* states the inequality with P(Y_n ≤ b − t√(2b)) and says so explicitly. This is correct whichever form the
  book prints, because the two forms are equivalent: P(X ≤ b − t√f(b)) ≤ P(X < b − t′√f(b)) for t′ < t, apply
  the strict form with t′ and let t′ ↑ t. With the ≤ form both tail bounds of v2 follow directly (upper tail:
  b = m_n + u, t = u/√(2b); lower tail: b = m_n, t = u/√(2m_n)). I could not check v2's claim "statement checked
  against the book"; the secondary source I found has the strict form (§5.1).
  *Residual cosmetic point:* some statements of the theorem are for integer b (and f : ℕ → ℕ). Then replace
  b = m_n + u by ⌈m_n + u⌉ = m_n + u′ with u′ ≥ u; since v ↦ v²/(m_n + v) is increasing, the printed bound follows.

**Cosmetic / under-justified (true; a few words missing).**

- **E3. Lemma C Step 2, line 53.** "5 ln T + E[N; |N − T²| > r] ≤ 5 ln T + 1". On {N < T² − r} the difference
  |μ_N − μ_{⌊T²⌋}| is bounded by μ_{⌊T²⌋} ≤ T²/2, not by N. Correct bound: E[(N + T²)/2; |N − T²| > r] ≤
  ½(E(N+T²)²·2e^{−(ln T)²/3})^{1/2} → 0 (Cauchy–Schwarz). Also the number of increments between n and ⌊T²⌋ is
  ≤ r + 1, not r; (r+1)·3√2/T ≤ 5 ln T still holds for large T (3√2 = 4.243).
- **E4. Lemma R, line 79.** "There are 4T² values of k": ⌈4T²⌉ when 4T² is not an integer, and the last
  rectangles R̃_k may protrude from [0,2T]²; harmless because P lives on [0,∞)² and 4T²·T′⁻⁴ ≤ 4/T² ≪ 1.
- **E5. Corollary E, lines 105–107.** "m ≥ (1+η)c₂₁√n" is turned into m ≥ μ_n + n^{1/3} using c₂₁ > 0
  (η·c₂₁√n ≫ n^{1/3} + O(ln n)). True — ℓ(T) ≥ 0.03·T(1 − o(1)) by `proof.md` Lemma 4.4(ii) — but not said.
- **E6. (S3), lines 30–31.** "The same holds for λ, with limit 2 (Logan–Shepp, Vershik–Kerov)". Those theorems
  are for uniform σ_n; the Poisson statement needs λ(T) = E[E LIS(σ_N)], N ~ Poisson(T²), monotonicity of
  n ↦ E LIS(σ_n) and N/T² → 1 (or Hammersley's original Poisson formulation). One sentence. Independent route to
  λ(T) ≤ 2T that does not use superadditivity: E LIS(σ_n) ≤ Σ_{k≤n} k^{−1/2} ≤ 2√n for every n (Pilpel 1990; the
  exact form of his bound is quoted from memory, see §5.2) and Jensen, E 2√N ≤ 2T. My samples agree
  (E LIS/T = 1.671, …, 1.980 for T = 10, …, 800; §4.1).
- **E7. Size of the thresholds.** "for large T" in Lemma R (lines 82–83) needs 13√T′ + 2 ≤ 2√(T ln T), i.e.
  ln T ≥ 42.25, T₂ ≳ 2.2·10¹⁸. Theorem D needs ½·10⁻⁹⁴/ln T > 200√(ln T/T), i.e. T ≥ 1.6·10²⁰¹ (my computation:
  the difference is −2.8·10⁻⁹⁸ at T = 10²⁰¹ and +6.4·10⁻⁹⁸ at T = 10²⁰²). So the last line of the file,
  "1 − c₂₁ of order 10⁻⁹⁷ if T_B is not astronomically large", is right provided T_B ≤ 10²⁰³ or so (it gives
  1 − c₂₁ ≥ 9.3·10⁻⁹⁸ at T = 10²⁰³). None of this affects correctness; T_B, T₁, T₂ are never made explicit.
- **E8. Attribution, lines 14–16.** "Bollobás–Brightwell 1992 for heights of random partial orders" as a source
  of the cut-plus-concentration argument: I could confirm only that this paper proves concentration of the
  height (§4). Alexander 1994 is the right reference for exactly this statement (γn − C√(n log n) ≤ E L_n ≤ γn).
- **E9. Repository consistency (not a mathematical point).** `proof.md` still lists "c₂₁ < 1 — Open; §7 states
  the one estimate that is missing", and the memory notes say the disproof must not be stated as a theorem until
  (H) is proved. `proof-c21.md` bypasses (H). If the main session accepts this review, those places need to be
  updated together, and norm 1 (line-by-line re-derivation by the main session) still applies.

## 2. Lemma-by-lemma record (task 1)

**(S1).** Re-derived, no issue. For R = [x₀,x₀+w] × [y₀,y₀+h] the map z ↦ (a(x−x₀), (y−y₀)/a) with a = √(h/w)
is a measure-preserving bijection onto [0,√(wh)]² that preserves the coordinatewise strict order, hence maps the
unit Poisson process on R to the unit Poisson process on the square and copies of any pattern to copies. So the
law of L₂₁(R) is that of L₂₁([0,√area]²). Monotone: [0,s]² ⊂ [0,s′]² and L₂₁ is monotone under adding points.
No independence between different rectangles is claimed or needed.

**(S2).** Re-derived, no issue. Removing a point destroys at most one block; adding is the reverse; a move is a
removal followed by an addition, net change in [−1, 1]. L₂₁ ≥ m is certified by the 2m points of a copy.

**(S3).** Re-derived, no issue (see E6). Pointwise L₂₁([0,S+T]²) ≥ L₂₁([0,S]²) + L₂₁([S,S+T]²) (all points of
the first square are strictly below-left of all points of the second, a.s.), and the second term has the law of
L₂₁([0,T]²) by translation. Fekete for a non-negative superadditive function on (0,∞): for T = qS + r,
ℓ(T) ≥ qℓ(S), so liminf ℓ(T)/T ≥ ℓ(S)/S for every S; hence lim = sup, finite because ℓ ≤ λ. Same for λ; its limit
is 2, so λ(T) ≤ 2T for every T > 0. Superadditivity of E LIS in the Poisson square model is correct (chains in
[0,S]² and [S,S+T]² concatenate).

**(S4).** The inequality "2Y_n ≤ LIS" is false pointwise (E1). The increment bound is correct: realise σ_{n+1} by
n+1 i.i.d. points, delete a uniformly chosen one; Y drops (by 1) only if the deleted point is one of the 2Y_{n+1}
points of a fixed optimal copy, so 0 ≤ μ_{n+1} − μ_n ≤ E[2Y_{n+1}]/(n+1) ≤ E LIS(σ_{n+1})/(n+1) ≤ 3/√(n+1).
The middle step is W90 Cor. 2 in expectation; without W90 one gets 6/√(n+1) from Y ≤ LIS, which would only
change constants. E LIS(σ_n) ≤ 3√n for n ≥ n₀ follows from P(LIS ≥ k) ≤ (e√n/k)^{2k} (limsup ≤ e < 3).

**(S5).** Re-derived, no issue. Step 2 of Lemma C with T = √n gives |ℓ(√n) − μ_n| ≤ 5 ln T + 1, so
μ_n/√n → c₂₁. With Talagrand (Step 1) L₂₁(σ_n)/√n → c₂₁ in probability. So c₂₁ of this file (Poisson square, limit
of means) is the constant lim L₂₁(σ_n)/√n of W90.

**Lemma C.** Holds.
- Theorem checked against: Alon–Spencer, *The Probabilistic Method*, Theorem 7.7.1: if h on a product space is
  1-Lipschitz and f-certifiable, X = h(ω), then P(X < b − t√f(b))·P(X ≥ b) ≤ e^{−t²/4} for all b, t. Form of the
  inequality confirmed online in a paper that quotes it (§5.1; strict first factor there, ≤ in v2 — equivalent,
  E2). With f(s) = 2s this is the display on line 43.
  The product space is n i.i.d. uniform points; Lipschitz and certifiability hold for every configuration when
  containment is defined with strict inequalities.
- Upper tail (v2): first factor P(Y_n ≤ m_n) ≥ ½, so P(Y_n ≥ m_n + u) ≤ 2e^{−u²/(8(m_n+u))} (t²/4 = u²/(8b),
  b = m_n + u). ✓.
- Lower tail: b = m_n, P(Y_n ≥ m_n) ≥ ½, P(Y_n ≤ m_n − t√(2m_n)) ≤ 2e^{−t²/4}, i.e. 2e^{−u²/(8m_n)}. ✓.
- m_n ≤ 2μ_n (Markov) ≤ 3√n ≤ 3√2·T = 4.243T ≤ 5T for n ≤ 2T². ✓. For 0 ≤ u ≤ 5T, 8(m_n + u) ≤ 80T. ✓.
- Median versus mean: m_n − μ_n = E(m_n − Y_n) ≤ E(m_n − Y_n)⁺ ≤ ∫₀^∞ 2e^{−u²/(8m_n)}du = √(8πm_n) ≤ √(40πT) =
  11.21√T ≤ 12√T. ✓. Hence P(Y_n ≥ μ_n + 12√T + u) ≤ P(Y_n ≥ m_n + u) ≤ 2e^{−u²/(80T)}. ✓ (direction right: the
  median is at most mean + 12√T, which is what an upper-tail bound around the mean needs).
- Step 2: see E3. Poisson tail P(|N − T²| > T ln T) ≤ 2exp(−r²/(2(T² + r/3))) ≤ 2e^{−(ln T)²/3} for large T. ✓.
  μ_n ≤ ℓ(T) + 10 ln T + 1 ≤ ℓ(T) + √T on |n − T²| ≤ r, and that range is inside [n₀, 2T²]. ✓. The mixture over N
  gives line 55. ✓.
- Step 3: E(Y − ℓ − 13√T − s)⁺ = ∫_s^∞ P(Y > ℓ + 13√T + u)du. Piece 1: ∫_s^∞ 2e^{−u²/(80T)}du ≤ (80T/s)e^{−s²/(80T)};
  s = 20√(T ln T) gives s²/(80T) = 5 ln T and 80T/s = 4√(T/ln T): 4T^{−4.5}/√(ln T). ✓. Piece 2:
  10T·e^{−(ln T)²/3}, super-polynomially small. ✓. Piece 3: ∫_{5T}^∞ ≤ E[Y; Y ≥ 5T] ≤ E[N; Y ≥ 5T], bounded as in
  E1; E N² = T⁴ + T²; P(LIS ≥ k) ≤ T^{2k}/(k!)² ≤ (eT/k)^{2k}. ✓. Sum ≤ T⁻⁴ for large T. ✓.

**Lemma R.** Holds.
- Cutting. Block β_j = {a_j, b_j}, a_j NW of b_j, c_j = (x(b_j), y(a_j)). Both points of β_i, i ≤ j, are ≤ c_j, and
  both points of β_i, i > j, are > c_j strictly in both coordinates (x(c_j) = x(b_j) < x of both points of
  β_{j+1}; y(c_j) = y(a_j) < y of both). So j ↦ x(c_j) + y(c_j) is strictly increasing and {j : sum ≤ 2T} is an
  initial segment. β₁,…,β_{j*} ⊂ [0,x₁] × [0,y₁] ⊂ [0,x₁] × [0,2T−x₁] = R_{x₁} because y₁ ≤ 2T − x₁.
  β_{j*+2},…,β_m ⊂ [x₂,2T] × [y₂,2T] ⊂ R′_{x₂} because y₂ > 2T − x₂. Every block is counted exactly once:
  j* in R_{x₁}, m − j* − 1 in R′_{x₂}, one dropped (β_{j*+1}); the cases j* = 0 and j* = m are covered. Areas:
  x(2T − x) ≤ T² for both families. So m ≤ 1 + M + M′. ✓. The dropped block is really needed: equality
  m = 1 + M + M′ occurred in my samples (§4.2, slack min = 0).
- Reflection ρ(z) = (2T,2T) − z: ρ(R_x) = [2T−x,2T] × [x,2T] = R′_{2T−x}; ρ preserves the Poisson process on
  [0,2T]² and reverses both coordinates, so it maps copies of π to copies of the reverse-complement of π, and
  21^{⊕m} is its own reverse-complement. Hence M′ has the law of M. ✓. (The sup over x is a maximum of finitely
  many values, so M is measurable.) Empirically E M and E M′ agree (§4.2).
- Discretisation. kδ ≤ x ≤ (k+1)δ ⇒ [0,x] ⊂ [0,(k+1)δ] and [0,2T−x] ⊂ [0,2T−kδ]. Area of R̃_k:
  (k+1)δ(2T − kδ) = kδ(2T−kδ) + δ(2T−kδ) ≤ T² + 2Tδ = T² + 1. ✓. Number of k: ⌈4T²⌉ (E4).
- Union-type bound. max_k X_k ≤ a + Σ_k (X_k − a)⁺ holds pointwise; E(X_k − a)⁺ ≤ E(Y′ − a)⁺ because
  v ↦ (v − a)⁺ is non-decreasing and X_k ≤_st Y′ by (S1). Only marginals are used; no independence. ✓.
- ℓ(T′) ≤ ℓ(T) + 1: [0,T′]² ∖ [0,T]² has area 1 and L₂₁ grows by at most the number of added points. ✓.
- Lemma C at T′: 4T²·T′⁻⁴ ≤ 4/T² ≤ 1. ✓. E M ≤ ℓ(T) + 2 + 13√T′ + 20√(T′ ln T′) ≤ ℓ(T) + 22√(T ln T) for
  ln T ≥ 42.25 (E7); ℓ(2T) ≤ 1 + 2E M ≤ 2ℓ(T) + 45√(T ln T). ✓.

**Corollary R′.** Holds. Dividing Lemma R at scale 2^jT by 2^{j+1}T and summing gives line 88. ln(2^jT) ≤
(1 + j) ln T for ln T ≥ ln 2, and √(1+j) ≤ 1 + √j. ½Σ_{j≥0} 2^{−j/2}(1 + √j) = 3.7796 (computed; the text says
≤ 3.8), 45·3.7796 = 170.1 ≤ 200. All scales 2^jT ≥ T ≥ T₂. The limit along T, 2T, 4T, … is c₂₁ because the full
limit exists by (S3). So ℓ(T) ≥ c₂₁T − 171√(T ln T). ✓.

**Theorem D.** Holds given (B). 2c₂₁T − 400√(T ln T) ≤ 2ℓ(T) [R′] ≤ λ(T) − 10⁻⁹⁴T/ln T [(B)] ≤ 2T − 10⁻⁹⁴T/ln T
[(S3)]; divide by 2T. ✓. Circularity: none found. (B) uses Lemmas 1.1, 3.2, 4.2–4.4 of `proof.md` and W90
Theorem 1; none of them assumes c₂₁ < 1, hypothesis (H), or the existence of c₂₁. W90 Cor. 2 quotes "existence
of c₂₁ (W5 Lemma B)" only for the statement c₂₁ ≤ 1, which is not used here: existence comes from (S3).
The logic is sound and not too good to be true: (B) at a single scale T gives a deficit of T·10⁻⁹⁴/ln T, the
means are within 200√(T ln T) of their limits, so the deficit survives in the limit as soon as
T/ln T ≫ 10⁹⁴√(T ln T). The ln T lost in (B) is a constant at a fixed scale.

**Corollary E.** Holds given Theorem D. Quantifiers: ε ∈ (0, ε₀) fixed, k → ∞, n = ⌊(1+ε)k²/4⌋. √n ≤
(k/2)√(1+ε) and c₂₁√(1+ε) < 1 give ⌊k/2⌋ ≥ (1+η)c₂₁√n for large k. μ_n ≤ ℓ(√n) + 5 ln √n + 1 ≤ c₂₁√n + O(ln n)
(Step 2 and (S3)). Step 1 with T = √n (n ≤ 2T² ✓): P(Y_n ≥ μ_n + 12n^{1/4} + u) ≤ 2e^{−u²/(80√n)}; u = n^{1/3} −
12n^{1/4} gives exponent ≈ n^{1/6}/80 → ∞. With E5, P(L₂₁(σ_n) ≥ ⌊k/2⌋) → 0. Odd k: 21^{⊕(k−1)/2} ⊕ 1 contains
21^{⊕⌊k/2⌋}. ✓. This contradicts Conjecture 1.1 of He–Kwan ("For a fixed ε > 0, a random permutation of length
(1+ε)k²/4 is w.h.p. k-universal") for every ε < ε₀.

## 3. Task 3 — is (B) really what is proved in `proof.md` §6?

Read once more: statement and proof of Proposition 6.1; statements of Lemmas 1.1, 3.2, 4.2, 4.3, 4.4 (and the
proofs of 4.2–4.4, which are short). **Nothing found.** Specifically:

- Model and range. The statement is for the unit Poisson process on Q_T = [0,T]², all T ≥ T_B, unconditional
  expectations, constant 10⁻⁹⁴ (the proof gives 1.5·10⁻⁹⁴). T_B is not explicit; it must satisfy ln T ≥ 10,
  T/ln T ≳ 3·10⁴ (for J ≥ 3·10⁻⁴T/ln T) and P(𝒜ᶜ) ≤ ½.
- Sign. Every term is non-negative: Cost_S(i) ≥ 0 by W90 Theorem 1, and the lower bound is J times a positive
  constant with J = ⌊0.015T/K⌋ ≥ 1. The right-hand side T/ln T is positive and tends to infinity.
- Conditioning. The only conditional expectation is over the auxiliary randomness S (independent of P):
  E[Cost_S(i_j) | i₁,…,i_{j−1}] is bounded below by the same constant for every value of the conditioning, then
  averaged. The expectation over P in Lemma 3.2 is unconditional; the indicator 1{N ≥ p−s} sits inside it, and
  1{N ≥ p−s} ≥ 1{N ≥ ι₀+2K} because p − s ≤ ι₀ + 2K. The event 𝒜 is used as E[1_𝒜 · K·A₁⁸] with P(𝒜) ≥ ½,
  not as a conditional statement.
- Index bookkeeping re-checked: p = 2i − 2 ≥ T₀ + 2K ≥ T₀ + s + 2; ι = p − s − 1 covers ι₀, …, ι₀+2K−1 once;
  ι₀ ≥ T₀ + 1 (needed for Lemma 2.5 and for the level argument); ι₀ + 2K ≤ 4KJ ≤ 0.06T. Constants:
  10⁻⁸⁰/(12·(8!)²) = 5.13·10⁻⁹¹; 0.015/45.1 = 3.33·10⁻⁴; product 1.5·10⁻⁹⁴. ✓.
- Hypotheses of the lemmas as used: Lemma 4.2 and 4.3 with k = 2K ≥ 90 ln T give expected counts ≤ T⁻²;
  Lemma 4.4(ii) needs T ≥ 50. No hidden hypothesis; (H) is not used in §6.
- What (B) rests on that I did not re-prove: W90 Theorem 1 and (★) (through (F3), Lemma 1.1, Lemma 1.2), and
  Lemmas 2.3–2.5, 3.1. Review-1 re-derived those and reports brute-force support for the deterministic part;
  the probabilistic assembly cannot be sampled (10⁻⁹⁴). My simulations are consistent with the sign and the
  size reported in W90 (paired E LIS − 2E L₂₁ = 0.95, 1.31, 2.38 at T = 200, 400, 800, i.e. slope
  0.0024 ± 0.0002 per unit T between T = 200 and 800), which says nothing about a proof.

## 4. Numerical checks (task 2)

Own code, written from scratch: `/private/tmp/claude-501/-Users-adamhadani-Development-math-proofs-superpatterns/0c33b450-b609-4fd6-9183-ef318e6a7155/scratchpad/rev2/l21rev.c`
(O(n·scan) sweep, core routine reproduced in the appendix), with
`/private/tmp/claude-501/-Users-adamhadani-Development-math-proofs-superpatterns/0c33b450-b609-4fd6-9183-ef318e6a7155/scratchpad/rev2/run_all.sh`,
`/private/tmp/claude-501/-Users-adamhadani-Development-math-proofs-superpatterns/0c33b450-b609-4fd6-9183-ef318e6a7155/scratchpad/rev2/aggregate.py`,
`/private/tmp/claude-501/-Users-adamhadani-Development-math-proofs-superpatterns/0c33b450-b609-4fd6-9183-ef318e6a7155/scratchpad/rev2/defcheck.py`;
raw outputs in the `out/` subfolder of that directory. The scratch directory is session-specific: copy the four
files into `review/` if they are to be kept. Reproduce (about 7 minutes on 4 cores):

```sh
cd <scratch>/rev2
cc -O2 -o l21rev l21rev.c -lm
python3 defcheck.py 8                         # sweep algorithm vs definition on all of S_1..S_8
for n in 6 9 12 20 40 80; do ./l21rev validate $n 20000 $n; done   # C sweep vs O(n^3) reference DP
sh run_all.sh && python3 aggregate.py         # est (seeds 1001-1904) and cut (seeds 2001-2204) runs, tables
```

Validation of the code: the sweep agrees with pattern containment by subset enumeration on all permutations of
S₁,…,S₈ (46 233 permutations, 0 mismatches); with an O(n³) dynamic programme written from the definition on
120 000 random permutations, n = 6, …, 80 (0 mismatches); and with the repository's `l21_paired.c --stdin`
(binary built in the scratch directory) on 300 random permutations of length 3000 (identical L₂₁ and LIS).
Poisson squares are sampled exactly (exponential gaps in x, uniform y).

### 4.1 ℓ(T), approximate subadditivity

| T | samples | ℓ(T) = E L₂₁ | s.e. | ℓ(T)/T | E LIS | s.e. | E LIS/T | E LIS − 2E L₂₁ (paired) | s.e. |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 10 | 200000 | 8.0981 | 0.0022 | 0.80981 | 16.7131 | 0.0042 | 1.67131 | 0.5170 | 0.0048 |
| 20 | 200000 | 17.5877 | 0.0028 | 0.87938 | 35.7163 | 0.0054 | 1.78582 | 0.5411 | 0.0062 |
| 25 | 200000 | 22.3918 | 0.0030 | 0.89567 | 45.3390 | 0.0058 | 1.81356 | 0.5555 | 0.0068 |
| 40 | 200000 | 36.9301 | 0.0035 | 0.92325 | 74.4622 | 0.0068 | 1.86156 | 0.6020 | 0.0081 |
| 50 | 200000 | 46.6940 | 0.0037 | 0.93388 | 94.0076 | 0.0074 | 1.88015 | 0.6197 | 0.0088 |
| 80 | 100000 | 76.1016 | 0.0062 | 0.95127 | 152.8656 | 0.0122 | 1.91082 | 0.6624 | 0.0148 |
| 100 | 100000 | 95.7859 | 0.0067 | 0.95786 | 192.2801 | 0.0131 | 1.92280 | 0.7083 | 0.0161 |
| 200 | 40000 | 194.5947 | 0.0133 | 0.97297 | 390.1359 | 0.0261 | 1.95068 | 0.9466 | 0.0327 |
| 400 | 20000 | 393.0782 | 0.0237 | 0.98270 | 787.4711 | 0.0470 | 1.96868 | 1.3147 | 0.0601 |
| 800 | 10000 | 790.8424 | 0.0423 | 0.98855 | 1584.0616 | 0.0831 | 1.98008 | 2.3768 | 0.1081 |

| T | ℓ(2T) − 2ℓ(T) | s.e. | √(T ln T) | 45√(T ln T) (Lemma R) | (ℓ(2T) − 2ℓ(T))/T^{1/3} | E LIS(2T) − 2E LIS(T) | s.e. |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 10 | 1.3915 | 0.0052 | 4.80 | 215.9 | 0.6459 | 2.2901 | 0.0100 |
| 20 | 1.7548 | 0.0065 | 7.74 | 348.3 | 0.6465 | 3.0295 | 0.0127 |
| 25 | 1.9104 | 0.0070 | 8.97 | 403.7 | 0.6533 | 3.3296 | 0.0137 |
| 40 | 2.2414 | 0.0093 | 12.15 | 546.6 | 0.6554 | 3.9411 | 0.0183 |
| 50 | 2.3980 | 0.0100 | 13.99 | 629.4 | 0.6509 | 4.2649 | 0.0198 |
| 100 | 3.0228 | 0.0188 | 21.46 | 965.7 | 0.6512 | 5.5756 | 0.0371 |
| 200 | 3.8889 | 0.0356 | 32.55 | 1464.9 | 0.6650 | 7.1994 | 0.0703 |
| 400 | 4.6860 | 0.0635 | 48.95 | 2203.0 | 0.6360 | 9.1194 | 0.1255 |

Reading. ℓ(2T) − 2ℓ(T) is positive (superadditivity), ≈ 0.65·T^{1/3}, and between 0.10 and 0.29 times √(T ln T)
— two to three orders of magnitude below the bound 45√(T ln T) of Lemma R, as expected of a lemma whose
threshold is T₂ ≥ 10¹⁸. ℓ(T)/T and E LIS/T increase with T and stay below 1 and 2 respectively, consistent with
(S3). The standard deviation of L₂₁ is 1.33, 2.10, 3.36, 4.22 at T = 25, 100, 400, 800 (first seed of each
size), i.e. ∝ T^{1/3}; Lemma C allows 13√T + 20√(T ln T). The numbers cannot test the asymptotic regime of
the proof; they only show that nothing has the wrong sign or order.

### 4.2 The cutting inequality m ≤ 1 + M + M′

For each sampled configuration on [0,2T]²: m = L₂₁ of the square; M = sup_x L₂₁(R_x) and M′ = sup_x L₂₁(R′_x)
computed **exactly** (x ↦ P ∩ R_x changes only at the points' x-coordinates and at 2T − y; every inclusion-maximal
set is evaluated; R′_x is evaluated directly, not through the reflection); and M̃, M̃′ = the maxima over the
⌈4T²⌉ grid rectangles R̃_k of the proof (δ = 1/(2T)) and their reflections.

| T (square side 2T) | samples | E m | E M | E M′ | E M̃ (grid) | E M̃′ (grid) | slack 1+M+M′−m: mean | min | max | violations (exact) | violations (grid) | M̃ < M or M̃′ < M′ |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 10 (20) | 2000 | 17.574 | 8.903 | 8.925 | 8.915 | 8.939 | 1.254 | 0 | 4 | 0 | 0 | 0 |
| 20 (40) | 1000 | 36.977 | 18.777 | 18.653 | 18.783 | 18.658 | 1.453 | 0 | 4 | 0 | 0 | 0 |
| 40 (80) | 300 | 76.113 | 38.323 | 38.503 | 38.337 | 38.507 | 1.713 | 0 | 5 | 0 | 0 | 0 |

No violation in 3300 configurations (the program prints a line starting with `VIOLATION` for each one; there is
none in `out/cut_T*_s*.txt`). Slack 0 occurs at every size, so "1 +" cannot be dropped. R_x ⊂ R̃_k was never
contradicted (M̃ ≥ M, M̃′ ≥ M′ in all samples), and the grid costs almost nothing (E M̃ − E M ≈ 0.01).
E M − ℓ(T) = 0.81, 1.19, 1.39 at T = 10, 20, 40 (ℓ from §4.1), against the proof's bound 22√(T ln T) = 106, 170, 267.
E M and E M′ agree within sampling error, as the reflection argument requires.

## 5. Literature (task 4)

### 5.1 Talagrand's inequality as used in Lemma C

Alon–Spencer, *The Probabilistic Method* (Wiley), §7.7 "Applications of Talagrand's inequality", Theorem 7.7.1
(number as I recall it and as it appears in a citation returned by web search; editions not checked): for h 1-Lipschitz and f-certifiable on a product space,
Pr[X < b − t√f(b)]·Pr[X ≥ b] ≤ e^{−t²/4}. **Confirmed** in this form from a paper that quotes it — Theorem 3.2 of
https://arxiv.org/abs/2004.03359 ("Large induced matchings in random graphs"), citing Alon–Spencer [1], stated
"for all λ > 0 and b ∈ ℕ", with f : ℕ → ℕ — **Not checked against the book itself.** The book states it for all b, t (from
memory); the integer-b version suffices (E2). v2 of `proof-c21.md` cites "4th ed. 2016, Theorem 7.7.1; statement
checked against the book" and prints the first factor with ≤; the two forms are equivalent (E2).

### 5.2 Approximate subadditivity / rate of convergence of the mean — is the step standard? Yes.

- K. S. Alexander, "The rate of convergence of the mean length of the longest common subsequence", *Ann. Appl.
  Probab.* 4 (1994), no. 4, 1074–1082, DOI 10.1214/aoap/1177004903,
  https://projecteuclid.org/euclid.aoap/1177004903. Proves γn ≥ E L_n ≥ γn − C(n log n)^{1/2} with an explicit C
  independent of the letter distribution. This is exactly the shape of Corollary R′. Bibliographic data and the
  statement confirmed from the Project Euclid record as returned by web search; full text not read.
- W. T. Rhee, "On rates of convergence for common subsequences and first passage time", *Ann. Appl. Probab.* 5
  (1995), no. 1, 44–48, DOI 10.1214/aoap/1177004827, https://projecteuclid.org/euclid.aoap/1177004827. Short
  unified proof of Alexander's LCS rate and of his rate for first-passage percolation (per search summary; full
  text not read). J. Lember, H. Matzinger, F. Torres, "The rate of the convergence of the mean score in random
  sequence comparison", *Ann. Appl. Probab.* 22 (2012), no. 3, 1046–1058, DOI 10.1214/11-AAP778, generalises it.
- B. Bollobás, G. Brightwell, "The height of a random partial order: concentration of measure", *Ann. Appl.
  Probab.* 2 (1992), no. 4, 1009–1018, DOI 10.1214/aoap/1177005586,
  https://projecteuclid.org/euclid.aoap/1177005586. Proves concentration of the height of a random k-dimensional
  order about its mean; for k = 2 (longest increasing subsequence) in a window n^{1/4+ε}, improving Frieze's
  n^{1/3+ε}. **Could not confirm** from an accessible source that it also contains the cut-and-concentrate bound
  on the mean (c_k n^{1/k} − E H) that `proof-c21.md` attributes to it; I recall such a bound but did not see it.
- J. M. Steele, *Probability Theory and Combinatorial Optimization*, CBMS-NSF Regional Conference Series in
  Applied Mathematics 69, SIAM, Philadelphia, 1997, ISBN 0-89871-380-3. Chapter 6 "Talagrand's isoperimetric
  theory" has a section "Application to the longest-increasing-subsequence problem" (confirmed from publisher
  listings). That Chapter 1 treats subadditivity for the LCS and increasing-subsequence problems and
  Alexander/Rhee-type "concentration on rates" is from memory, **not confirmed online**.
- S. Pilpel, "Descending subsequences of random permutations", *J. Combin. Theory Ser. A* 53 (1990), no. 1,
  96–116, DOI 10.1016/0097-3165(90)90022-O: elementary proof that the constant is ≤ 2 (abstract confirmed); the
  explicit form E L_n ≤ Σ_{k≤n} k^{−1/2} is quoted from memory, **not confirmed**. Used only as a side remark (E6).

### 5.3 Status of Alon's conjecture, 2020–2026

- X. He, M. Kwan, "Universality of random permutations", *Bull. London Math. Soc.* 52 (2020), no. 3, 515–529,
  DOI 10.1112/blms.12345, https://arxiv.org/abs/1911.12878. Conjecture 1.1 (attributed to Alon, 1999, via
  Arratia): "For a fixed ε > 0, a random permutation of length (1+ε)k²/4 is w.h.p. k-universal"; main result
  n = 2000k² log log k suffices. Confirmed from the arXiv page and the ar5iv rendering.
- D. J. Altschuler, Q. Dubroff, K. Tikhomirov, "Online Permutation Embedding: Optimal Stopping and Scaling
  Laws", https://arxiv.org/abs/2608.19050 (submitted 19 August 2026). Title, authors and date confirmed from the
  arXiv abstract page (the repository's memory note lists the authors as unconfirmed). The abstract says random
  permutations embed online faster than monotone ones, to first order, and refers to "prevailing conjectures and
  heuristics in the offline theory"; it does not name Alon's conjecture and claims neither a proof nor a disproof.
- Two web searches (standard and extended) for a proof, disproof or counterexample of Alon's conjecture dated
  2020–2026, and for layered patterns in this context, returned nothing beyond He–Kwan and the Chroman–Kwan–Singhal
  lower-bound paper (*J. Combin. Theory Ser. A*, 2021, https://www.sciencedirect.com/science/article/pii/S0097316521000662).
  **No prior proof or disproof found.** The searches were brief and are not a substitute for the repository's
  priority check.

## Appendix — core routine of the reviewer's L₂₁ code

Sweep by increasing x. Y[k] = smallest top height of a copy of 21^{⊕k} among the points seen. A new point b
(height v) can only be the last point of a copy; it closes a block opened by an earlier point a with y_a > v
provided some k-copy lies to the left of a and below v, i.e. Y_k(at the arrival of a) < v. Only
k = level(a) := max{k : Y_k(arrival of a) < y_a} can improve Y_{k+1} (lower k is dominated by an existing copy
left of a), and only level(a) = level(b) (for larger k the threshold fails, for smaller k the new top y_a > v >
Y_{level(b)} ≥ Y_{k+1}). Within a level the stored thresholds are non-increasing in arrival order, so the scan
stops at the first failure.

```c
static int l21(const double*y,int n,Work*w){   /* y: heights in order of increasing x */
  double*Y=w->Y,*th=w->th; int*head=w->head,*prv=w->prv;
  int L=0; Y[0]=-INFINITY; head[0]=-1;
  for(int i=0;i<n;i++){
    double v=y[i];
    int lo=0,hi=L; while(lo<hi){int md=(lo+hi+1)/2; if(Y[md]<v) lo=md; else hi=md-1;}
    int k=lo; double best=INFINITY;
    for(int j=head[k]; j>=0 && th[j]<v; j=prv[j]) if(y[j]>v && y[j]<best) best=y[j];
    if(best<INFINITY){ if(k==L){L++; Y[L]=best; head[L]=-1;} else if(best<Y[k+1]) Y[k+1]=best; }
    th[i]=Y[k]; prv[i]=head[k]; head[k]=i;
  }
  return L;
}
```
