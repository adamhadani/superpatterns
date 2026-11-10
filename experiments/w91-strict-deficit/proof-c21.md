# W91, part 2 — c₂₁ < 1, and Alon's conjecture fails at the sharp constant

Date: 10 November 2026. Status: proved here; re-derived by the main session and by an independent reviewer agent
(`out/review-2.md`, no error affecting a conclusion); **not read by a human mathematician**. See §5.

Continues `proof.md` (same folder), whose Proposition 6.1 is used as a black box:

  (B)  E LIS(P_T) − 2·E L₂₁(P_T) ≥ 10⁻⁹⁴·T/ln T   for all T ≥ T_B   (P_T = unit Poisson process on [0,T]²).

| Item | Statement | Status |
|:--|:--|:--|
| Lemma R | ℓ(2T) ≤ 2ℓ(T) + 45√(T ln T) for large T, where ℓ(T) = E L₂₁(P_T) | **Proved** (§3); numerically ℓ(2T) − 2ℓ(T) ≈ 0.65·T^{1/3} |
| Corollary R′ | c₂₁·T − 200√(T ln T) ≤ ℓ(T) ≤ c₂₁·T for large T | **Proved** (§3) |
| Theorem D | c₂₁ < 1 | **Proved**, given (B) (§4) |
| Corollary E | For every fixed ε < c₂₁⁻² − 1, a uniform permutation of length ⌊(1+ε)k²/4⌋ does not contain 2 1 4 3 ⋯ k (k−1), with probability → 1. So Alon's conjecture fails for small fixed ε | **Proved**, given Theorem D (§4) |

Hypothesis (H) of `proof.md` §7 is **not** used. The idea is the classical one for superadditive functionals
(Alexander, Ann. Appl. Probab. 4 (1994) 1074–1082, proves γn − C√(n log n) ≤ E L_n ≤ γn for the longest common
subsequence; Rhee, Ann. Appl. Probab. 5 (1995) 44–48, gives a short proof; cutting along an antidiagonal and
using a concentration inequality is the scheme of Lember–Matzinger–Torres, Ann. Appl. Probab. 22 (2012)
1046–1058): superadditivity gives ℓ(T) ≤ c₂₁T, and cutting an optimal object in two plus concentration gives
the reverse inequality up to O(√(T ln T)). A deficit that is larger than this error at a single scale is
therefore a deficit of the limit constant.

## 1. Notation and standing facts

P is a unit Poisson process on [0,∞)². For a rectangle R, L₂₁(R) is the largest m such that P ∩ R ⊇ 21^{⊕m}, and
LIS(R) the longest chain. ℓ(T) = E L₂₁([0,T]²), λ(T) = E LIS([0,T]²). Y_n denotes L₂₁ of n i.i.d. uniform points
in a rectangle (its law is that of L₂₁(σ_n)), μ_n = E Y_n, m_n a median of Y_n.

 (S1) The law of L₂₁(R) depends only on the area of R, and is stochastically non-decreasing in the area.
      (The maps (x,y) ↦ (ax, y/a) and translations preserve the Poisson process and the relation <.)
 (S2) L₂₁ changes by at most 1 when one point is added, removed or moved; L₂₁ ≥ m is witnessed by 2m points.
 (S3) ℓ is non-decreasing and superadditive: ℓ(S+T) ≥ ℓ(S) + ℓ(T) (copies in [0,S]² and [S,S+T]² concatenate).
      Hence c₂₁ := lim ℓ(T)/T = sup_T ℓ(T)/T exists and ℓ(T) ≤ c₂₁T. The same holds for λ, with limit 2
      (Logan–Shepp, Vershik–Kerov: E LIS(σ_n)/√n → 2; λ(T) = E[E LIS(σ_N)] with N Poisson(T²)), so λ(T) ≤ 2T
      for every T. Also c₂₁ > 0 (proof.md, Lemma 4.4(ii)).
 (S4) Y_n ≤ LIS pointwise (one point from each block is a chain) and 2μ_n ≤ E LIS(σ_n) (W90, Corollary 2; the
      pointwise inequality 2Y_n ≤ LIS is false, e.g. for σ = 21). E LIS(σ_n) ≤ 3√n for n ≥ n₀ (proof.md, proof of
      Theorem B). μ_n is non-decreasing and μ_{n+1} − μ_n ≤ 2μ_{n+1}/(n+1) ≤ 3/√(n+1) for n ≥ n₀ (delete a
      uniform point: L₂₁ drops only if the point is one of the 2Y_{n+1} points of a fixed optimal copy).
 (S5) c₂₁ = lim E L₂₁(σ_n)/√n: by (S4), for T = √n and N = |P ∩ [0,T]²|, |ℓ(T) − μ_n| ≤ 5 ln T + 1 (see §2, step 2).

## 2. Concentration

**Lemma C.** For T ≥ T₁ and Y = L₂₁([0,T]²): E (Y − ℓ(T) − 13√T − 20√(T ln T))⁺ ≤ T⁻⁴.

*Proof.* Step 1 (fixed n ≤ 2T²). Y_n is a function of n independent points, 1-Lipschitz and certifiable with
f(s) = 2s by (S2). Talagrand's inequality (Alon–Spencer, *The Probabilistic Method*, 4th ed. 2016, Theorem 7.7.1;
statement checked against the book): P(Y_n ≤ b − t√(2b))·P(Y_n ≥ b) ≤ e^{−t²/4} for all b, t ≥ 0. With b = m_n + u,
t = u/√(2b) (so that the first factor is P(Y_n ≤ m_n) ≥ ½) and with b = m_n (second factor ≥ ½) this gives
P(Y_n ≥ m_n + u) ≤ 2e^{−u²/(8(m_n+u))} and P(Y_n ≤ m_n − u) ≤ 2e^{−u²/(8m_n)}. By Markov and (S4),
m_n ≤ 2μ_n ≤ 3√n ≤ 5T. So for 0 ≤ u ≤ 5T: P(Y_n ≥ m_n + u) ≤ 2e^{−u²/(80T)}, and
m_n − μ_n ≤ E(m_n − Y_n)⁺ ≤ ∫₀^∞ 2e^{−u²/(8m_n)} du = √(8πm_n) ≤ 12√T. Hence

  P(Y_n ≥ μ_n + 12√T + u) ≤ 2e^{−u²/(80T)}   (0 ≤ u ≤ 5T, n₀ ≤ n ≤ 2T²).

Step 2 (Poisson number of points). N is Poisson(T²); put r = T ln T. By (S4), for |n − T²| ≤ r,
|μ_n − μ_{⌊T²⌋}| ≤ r·3/√(T²/2) ≤ 5 ln T, and ℓ(T) = E μ_N differs from μ_{⌊T²⌋} by at most
5 ln T + E[(N + T²)/2; |N − T²| > r] ≤ 5 ln T + 1 (use μ_n ≤ n/2). So μ_n ≤ ℓ(T) + 10 ln T + 1 ≤ ℓ(T) + √T on |n − T²| ≤ r, and

  P(Y ≥ ℓ(T) + 13√T + u) ≤ 2e^{−u²/(80T)} + P(|N − T²| > r) ≤ 2e^{−u²/(80T)} + 2e^{−(ln T)²/3}   (0 ≤ u ≤ 5T).

Step 3. With s = 20√(T ln T): ∫_s^{5T} 2e^{−u²/(80T)} du ≤ (80T/s)·e^{−s²/(80T)} = 4√(T/ln T)·T⁻⁵;
5T·2e^{−(ln T)²/3} = o(T⁻⁵); and the part Y ≥ ℓ(T) + 13√T + 5T forces LIS ≥ Y ≥ 5T, so it contributes at most
E[N; LIS([0,T]²) ≥ 5T] ≤ (E N²·(e/5)^{10T})^{1/2} = o(T⁻⁵) (first moment: P(LIS ≥ k) ≤ (eT/k)^{2k}). ∎

## 3. Approximate subadditivity

**Lemma R.** For T ≥ T₂: ℓ(2T) ≤ 2ℓ(T) + 45√(T ln T).

*Proof.* Let m = L₂₁([0,2T]²) and take a copy with blocks β₁, …, β_m; block β_j consists of a_j NW of b_j, and
c_j = a_j ∨ b_j is the upper-right corner of its bounding box. Every point of β_j is below-left of every point of
β_{j+1}, so both points of β_i, i ≤ j, are ≤ c_j, and both points of β_i, i > j, are > c_j (coordinatewise,
strictly). Let j* be the largest j with x(c_j) + y(c_j) ≤ 2T (j* = 0 if there is none). Then

 * β₁, …, β_{j*} lie in [0,x₁] × [0,y₁], (x₁,y₁) = c_{j*}, x₁ + y₁ ≤ 2T, hence in R_{x₁} := [0,x₁] × [0,2T−x₁];
 * β_{j*+2}, …, β_m lie in [x₂,2T] × [y₂,2T], (x₂,y₂) = c_{j*+1}, x₂ + y₂ > 2T, hence in
   R′_{x₂} := [x₂,2T] × [2T−x₂,2T].

So m ≤ 1 + M + M′, M = sup_{0≤x≤2T} L₂₁(R_x), M′ = sup_{0≤x≤2T} L₂₁(R′_x). The reflection z ↦ (2T,2T) − z maps
R_x to R′_{2T−x}, preserves the Poisson process and maps copies of 21^{⊕m} to copies of 21^{⊕m} (the pattern is
its own reverse-complement); so M′ has the law of M and ℓ(2T) ≤ 1 + 2·E M.

Bound on E M. Put δ = 1/(2T). For kδ ≤ x ≤ (k+1)δ, R_x ⊂ R̃_k := [0,(k+1)δ] × [0,2T−kδ], whose area is
kδ(2T−kδ) + δ(2T−kδ) ≤ T² + 1. There are ⌈4T²⌉ values of k. By (S1), X_k := L₂₁(R̃_k) is stochastically dominated
by Y′ := L₂₁([0,T′]²), T′ = √(T²+1), and ℓ(T′) ≤ ℓ(T) + 1 (the added region has area 1; (S2)). For any a,
M ≤ max_k X_k ≤ a + Σ_k (X_k − a)⁺, so E M ≤ a + ⌈4T²⌉·E(Y′ − a)⁺ (no independence is needed). Take a = ℓ(T′) + 13√T′ + 20√(T′ ln T′); by
Lemma C, ⌈4T²⌉·E(Y′ − a)⁺ ≤ ⌈4T²⌉·T′⁻⁴ ≤ 1 for large T. Hence E M ≤ ℓ(T) + 2 + 13√T′ + 20√(T′ ln T′) ≤ ℓ(T) + 22√(T ln T) for
large T, and ℓ(2T) ≤ 2ℓ(T) + 1 + 44√(T ln T). ∎

**Corollary R′.** For T ≥ T₂: c₂₁T − 200√(T ln T) ≤ ℓ(T) ≤ c₂₁T.

*Proof.* The upper bound is (S3). Iterating Lemma R,
ℓ(2^kT)/(2^kT) ≤ ℓ(T)/T + Σ_{j<k} 45√(2^jT ln(2^jT))/(2^{j+1}T). Since √(ln(2^jT)) ≤ √(ln T)·(1+√j) for ln T ≥ 1,
the sum is at most 45√(ln T/T)·½Σ_{j≥0} 2^{−j/2}(1+√j) ≤ 45·3.79·√(ln T/T) < 171√(ln T/T). Let k → ∞ and use (S3). ∎

## 4. The constant

**Theorem D.** c₂₁ < 1.

*Proof.* For T ≥ max(T_B, T₂), by (B), (S3) and Corollary R′,

  2c₂₁T − 400√(T ln T) ≤ 2ℓ(T) ≤ λ(T) − 10⁻⁹⁴T/ln T ≤ 2T − 10⁻⁹⁴T/ln T,

so 1 − c₂₁ ≥ ½·10⁻⁹⁴/ln T − 200√(ln T/T), which is positive for large T. ∎

**Corollary E (Alon's conjecture fails at the sharp constant).** Let ε₀ = c₂₁⁻² − 1 > 0 and fix ε ∈ (0, ε₀).
For n = ⌊(1+ε)k²/4⌋ and k → ∞, P(σ_n ⊇ 2 1 4 3 ⋯) → 0, where the pattern is 21^{⊕k/2} for even k and
21^{⊕(k−1)/2} ⊕ 1 for odd k. In particular σ_n is not k-universal with probability → 1.

*Proof.* Both patterns contain 21^{⊕m} with m = ⌊k/2⌋ ≥ (1+η)c₂₁√n for some η = η(ε) > 0 and large k, because
√n ≤ (k/2)√(1+ε) and c₂₁√(1+ε) < 1. By (S5) and (S3), E L₂₁(σ_n) ≤ c₂₁√n + O(ln n), and by Step 1 of Lemma C
together with m_n ≤ μ_n + 12 n^{1/4}, P(L₂₁(σ_n) ≥ μ_n + n^{1/3}) → 0. ∎

Numerically (W90) c₂₁ ≈ 0.99887 and ε₀ ≈ 0.0023; the proof gives only 1 − c₂₁ > 0 (of order 10⁻⁹⁷ if T_B is not
astronomically large; the inequalities above need T of order 10²⁰¹).

## 5. Verification and what it does not cover

 * Written and re-derived line by line by the main session. Talagrand's inequality was checked against
   Alon–Spencer (4th ed.), Theorem 7.7.1, and the Mecke equation against Last–Penrose, Theorem 4.4.
 * Independent adversarial review (`out/review-2.md`, a reviewer agent that did not write the text): Lemma C,
   Lemma R, Corollary R′, Theorem D and Corollary E hold; one false auxiliary sentence (2Y_n ≤ LIS pointwise) and
   five cosmetic points, all corrected above; no circularity; Proposition 6.1 re-read with the question whether
   its bound is unconditional — nothing found.
 * Numerics by the reviewer's own code (`review2/`, raw outputs `review2/out/`, validated against the definition
   on S₁–S₈ and against W90's program): ℓ(2T) − 2ℓ(T) = 1.39, 1.75, 1.91, 2.24, 2.40, 3.02, 3.89, 4.69 for
   T = 10, 20, 25, 40, 50, 100, 200, 400 (about 0.65·T^{1/3}, far below 45√(T ln T)); ℓ(T)/T increases from
   0.810 (T = 10) to 0.9886 (T = 800); the cutting inequality m ≤ 1 + M + M′ holds in 3300 of 3300 sampled
   configurations, with equality occurring.
 * **Not covered.** Everything rests on Proposition 6.1 of `proof.md` (verified as recorded there: main session,
   one reviewer, brute-forced gadget lemmas) and on Theorem 1 of W90. The constants are far outside any range that
   can be simulated, so Theorem D cannot be tested numerically except through its consistency with
   c₂₁ ≈ 0.99887. No human mathematician has read any of this. A disproof of a published conjecture should not be
   announced on this basis; it should be given to a specialist first.

```sh
cd experiments/w91-strict-deficit/review2
cc -O2 -o /tmp/l21rev l21rev.c      # then see run_all.sh (uses ./l21rev) and aggregate.py
```
