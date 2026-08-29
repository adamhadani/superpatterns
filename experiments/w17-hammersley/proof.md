# W17 — c_{21} ≥ 0.7866 by renewal ("sweep") rules; general τ (proofs)

Date 2026-08-29.  Setting as in W5/W10/W12: Π_N = Poisson process of intensity N on [0,1]²; a τ-chain of length L is
a copy of τ^{⊕L}; L_τ(N) = longest τ-chain; c_τ = lim L_τ(N)/√N (exists a.s. and in mean, W5 Lemma B; only the
limit in probability is used below).  Known before this note: 0.598 ≤ c_{21} ≤ 1.140 (W12).  Conjecture: c_{21} = 1.

## Results

**Theorem 1.**  c_{21} ≥ 2 / Σ_{n≥1} Γ(n+3/2)·n(3n+7) / (2(n+2)·n!·(n+1)!) = 2/2.5425687… = **0.78660**.

**Proposition 2 (simpler, closed form).**  c_{21} ≥ √(2/(e(4−e))) = 0.75765.

**Theorem 3 (general τ).**  For every τ ∈ S_j put a_m = |Av_m(τ)|/m! (a_m = 1 for m < j), and for m ≥ j let
cnt_m(τ) = m·|Av_{m−1}(τ)| − |Av_m(τ)| and sumTop_m(τ) = Σ over pairs (σ ∈ Av_{m−1}(τ), r ∈ {1..m}) such that
appending to σ a new last entry of rank r creates a copy of τ, of the minimum over such copies of the largest value
in the copy (ranks in {1..m}).  Then
  (a) c_τ ≥ 2 / Σ_{m≥j} (Γ(m+½)/Γ(m)) · [ (cnt_m(τ)+cnt_m(τ⁻¹))/(2·m!) + (sumTop_m(τ)+sumTop_m(τ⁻¹))/(2(m+1)·m!) ];
  (b) c_τ ≥ 1/√(E n_τ · E top_τ), E n_τ = Σ_{m≥0} a_m, E top_τ = Σ_{m≥j} sumTop_m(τ)/((m+1)·m!), and the same with τ⁻¹.
All quantities are exact enumerations; for m > 11 they were bounded (§4), giving (table in §4; conjectured values 2/j):
  S_3: c_τ ≥ 0.5384 (123, 321), 0.5354 (132, 213), 0.5516 (231, 312)          [W12: 0.389; conjecture 0.667]
  S_4: c_τ ≥ 0.385 … 0.413 for every τ ∈ S_4 (0.4035 for 1234, whose true value is 1/2)  [W12: 0.30; conjecture 0.5].

**Proposition 4 (limit of the method).**  Every rule of the kind used here (Theorem A) has E[dx+dy] ≥ E M, where
M = min over descent pairs (a,b) of the unit Poisson process in the quadrant of x_b + y_a, and E M = 2.386 ± 0.002
(Monte Carlo).  Hence no renewal rule can prove c_{21} > 0.84; reaching 1 requires dependence between consecutive
blocks (§5).  Monte Carlo (not rigorous) for the ℓ_p-sweep first-descent rules: c_{21} ≥ 0.8037 ± 0.0001 at p = 1.5.

So the rigorous window is now **0.7866 ≤ c_{21} ≤ 1.140**.

--------------------------------------------------------------------------------------------------
## 1. The renewal principle (Theorem A)

Throughout, Π is a Poisson process of intensity 1 on the open quadrant Q = (0,∞)².  For c ∈ Q write Q_c = c + Q.
For a finite set of points P ⊂ Q containing a copy K of τ (j points whose x-order and y-order realize τ), the
*corner* of K is cor(K) = (max_{z∈K} x_z, max_{z∈K} y_z).  Two copies K, K' with K' ⊂ Q_{cor(K)} are stacked (every
point of K' is strictly above-right of every point of K), so K ∪ K' is a copy of τ^{⊕2}, and inductively a sequence
K_1, K_2, … with K_{i+1} ⊂ Q_{cor(K_i)} is a τ-chain.

**Sweep families.**  Fix a family (D_s)_{s>0} of open subsets of Q with: D_s ⊂ D_{s'} for s < s'; each D_s is
*down-closed* in Q (z ∈ D_s, z' ∈ Q, z' ≤ z coordinatewise ⇒ z' ∈ D_s); φ(s) := |D_s| is finite, continuous and
strictly increasing with φ(0+) = 0, φ(∞) = ∞; and D_s = ∪_{s'<s} D_{s'} (left-continuity).  The two families used:
  (Sq)  D_s = (0,s)², φ(s) = s²;    (St_h)  D_s = (0,s) × (0,h), φ(s) = hs.
For z ∈ Q let s(z) = inf{s : z ∈ D_s} (so z ∈ ∂D_{s(z)} and z ∉ D_{s(z)} since D_{s(z)} is open and left-continuous).

**Lemma A1 (sweep representation).**  Let z_1, z_2, … be the points of Π ordered by increasing s(z) (a.s. no ties),
s_i = s(z_i).  Then (i) φ(s_1), φ(s_2) − φ(s_1), … are i.i.d. Exp(1); (ii) for (Sq), z_i = (s_i, U_i s_i) or
(U_i s_i, s_i) according as ε_i = R or T, with (ε_i, U_i) i.i.d., ε_i uniform on {R, T}, U_i uniform on (0,1),
independent of (s_i); for (St_h), z_i = (s_i, hU_i) with U_i i.i.d. uniform, independent of (s_i).
Proof.  (Sq): the map z ↦ (s, u, ε) = (max(x,y), min(x,y)/max(x,y), side) is a bijection of Q minus the diagonal onto
(0,∞) × (0,1) × {R,T} with Jacobian |dx dy| = s ds du on each side; by the mapping theorem the image of Π is Poisson
with intensity s ds du (counting measure on {R,T}) = (2s ds) ⊗ (du/1) ⊗ (uniform on {R,T}); a Poisson process with
product intensity (2s ds) ⊗ ν is a Poisson process of intensity 2s ds on (0,∞) with i.i.d. ν-marks (marking
theorem), and the process of s-values with intensity 2s ds is the image of a rate-1 Poisson process under
φ^{-1}(t) = √t.  (St_h): dx dy = (h dx) ⊗ (dy/h) on (0,∞) × (0,h), same argument.  ∎
In both cases we may realize Π as a measurable function of an i.i.d. sequence ξ_i = (E_i, m_i) (E_i ~ Exp(1), m_i the
mark), with φ(s_i) = E_1 + … + E_i and z_i = ψ(s_i, m_i) ∈ ∂D_{s_i}.

**Rule.**  A rule is a stopping time N ≥ j for the filtration F_n = σ(ξ_1..ξ_n) together with an F_N-measurable
choice of a copy K ⊂ {z_1, …, z_N} of τ with z_N ∈ K.  (In all rules below N = first n such that {z_1..z_n} contains a
copy of τ; then every copy contains z_N.)  Put c = cor(K) and (dx, dy) = c.

**Lemma A2.**  Q_c ∩ D̄_{s_N} = ∅, and conditionally on F_N the process Π ∩ Q_c − c is a Poisson process of intensity
1 on Q, independent of F_N.
Proof.  Let z' ∈ Q_c.  Then z' > c ≥ z_N coordinatewise, strictly in both coordinates.  If z' were in the closure of
D_{s_N}, some z'' ∈ D_{s_N} would lie so close to z' that still z'' > z_N coordinatewise, and down-closure would give
z_N ∈ D_{s_N}, contradicting z_N ∈ ∂D_{s_N} ∖ D_{s_N}.  So Q_c ∩ D̄_{s_N} = ∅.  Next, since N is a stopping time of the
i.i.d. sequence (ξ_i), the shifted sequence (ξ_{N+k})_{k≥1} is i.i.d. with the law of ξ_1 and independent of F_N
(for A ∈ F_N and measurable B: P(A ∩ {(ξ_{N+k})_k ∈ B}) = Σ_n P(A ∩ {N=n} ∩ {(ξ_{n+k})_k ∈ B}) = Σ_n P(A ∩ {N=n}) P(B)
= P(A) P(B), because A ∩ {N=n} ∈ F_n is independent of (ξ_{n+k})_{k≥1}).  The points
{z_{N+k}}_{k≥1} = Π ∖ D̄_{s_N} are the image of (ξ_{N+k}) under the same map that produces Π from (ξ_k), started at the
level φ(s_N) (F_N-measurable), so conditionally on F_N, Π ∖ D̄_{s_N} is a Poisson process of intensity 1 on Q ∖ D̄_{s_N}
(the sweep representation of Lemma A1 applied to the region Q ∖ D̄_{s_N} with the family (D_s ∖ D̄_{s_N})_{s>s_N},
whose area is φ(s) − φ(s_N)).  Restricting to Q_c ⊂ Q ∖ D̄_{s_N} (restriction of a Poisson process to a measurable
set is Poisson) and translating gives the claim.  ∎

**Theorem A (renewal principle).**  Apply the rule to Π, obtaining (dx_1, dy_1) and c_1; apply the same rule to
Π ∩ Q_{c_1} − c_1, obtaining (dx_2, dy_2), c_2 = c_1 + (dx_2, dy_2); and so on.  Then (dx_i, dy_i)_{i≥1} are i.i.d.,
the copies K_1, K_2, … form a τ-chain, and, if μ_x = E dx, μ_y = E dy are finite,
        c_τ ≥ 1 / max(μ_x, μ_y).
If, moreover, the law of (dx, dy) is exchangeable (the rule commutes with transposition x ↔ y, as (Sq) does), then
c_τ ≥ 2/E[dx + dy].
Proof.  I.i.d.: by Lemma A2 and induction, the input of step i+1 is a unit Poisson process on Q independent of
everything used in steps 1..i.  Chain: K_{i+1} ⊂ Q_{c_i} by construction.  Location: every point of K_i lies in
c_{i−1} + D̄_{s^{(i)}} where s^{(i)} is the stopping level of step i; since c_i − c_{i−1} ≥ z_{N}^{(i)} coordinatewise
and max(x, y) of z_N^{(i)} equals s^{(i)} for (Sq) (resp. x = s^{(i)} for (St_h), where also y ≤ h), we get
K_1 ∪ … ∪ K_n ⊂ [0, X_n + ρ_n] × [0, Y_n + ρ_n] with (X_n, Y_n) = c_n and ρ_n = max(dx_n, dy_n) + h (h = 0 for (Sq)).
Now Π_N (intensity N on [0,1]²) has the law of (Π ∩ (0,√N)²)/√N, and containment is scale invariant, so L_τ(N) is
equal in law to L_τ(Π ∩ (0,√N)²) ≥ n(N) := max{n : X_n + ρ_n ≤ √N, Y_n + ρ_n ≤ √N}.  By the strong law
X_n/n → μ_x, Y_n/n → μ_y, ρ_n/n → 0 a.s., hence n(N)/√N → 1/max(μ_x, μ_y) a.s.  Since L_τ(N)/√N → c_τ in probability
(W5 Lemma B), for every ε > 0, P(c_τ + ε ≥ 1/max(μ_x,μ_y) − ε) ≥ P(L_τ(N)/√N ≥ n(N)/√N ≥ 1/max μ − ε) − o(1) → 1, so
c_τ ≥ 1/max(μ_x, μ_y).  If (dx, dy) is exchangeable, μ_x = μ_y = E[dx+dy]/2.  ∎
(This is Hammersley's 1972 lower-bound argument for the LIS — the ℓ_1 sweep with τ = 1 gives E[dx+dy] = √(π/2) and
LIS ≥ √(8/π)·√N — applied to blocks τ instead of single points.)

--------------------------------------------------------------------------------------------------
## 2. The strip rule (Proposition 2)

Rule (St_h) for τ = 21: N = first n such that some earlier point lies strictly above z_n (the points z_1..z_{n−1} are
then increasing in arrival order, i.e. their heights are records); K = {a, z_N} with a the lowest earlier point above
z_N; c = (x_{z_N}, y_a).  Heights V_i = hU_i are i.i.d. uniform on (0,h); N = first index with V_N < max_{i<N} V_i =
V_{N−1}.
  P(N > n) = P(V_1 < … < V_n) = 1/n!, so E N = Σ_{n≥0} 1/n! = e, and E dx = E s_N = E N / h = e/h (Wald: s_N = Σ_{i≤N} E_i/h).
  dy: on {N = n+1} (n ≥ 1), among the n+1 i.i.d. heights the last one has rank k+1 for some k ∈ {0..n−1} (k = number of
  earlier heights below it) and the other n are in increasing order; each of these n orderings has probability
  1/(n+1)!, independent of the order statistics; a is the (k+2)-th order statistic of n+1 uniforms on (0,h), whose mean
  is h(k+2)/(n+2).  Hence
    E dy = h Σ_{n≥1} (1/(n+1)!) Σ_{k=0}^{n−1} (k+2)/(n+2) = h Σ_{n≥1} n(n+3)/(2(n+2)(n+1)!) = h Σ_{n≥1} [1/n! − 2/(n+2)!]
         = h [(e−1) − (2e−5)] = h(4−e)/2 = 0.64086 h.
  (Check: Σ_n P(N=n+1) = Σ n/(n+1)! = 1.)  By Theorem A with h chosen so that μ_x = μ_y, i.e. h² = 2e/(4−e):
    c_{21} ≥ 1/max(e/h, h(4−e)/2) = 1/√(e(4−e)/2) = √(2/(e(4−e))) = 0.757655.  ∎
Monte Carlo check (rules.c, rule 0, h = 1.458, 2·10⁶ samples): E dx = 1.86384 (e/h = 1.86436), E dy = 0.93398
(h(4−e)/2 = 0.93437).

--------------------------------------------------------------------------------------------------
## 3. The square rule (Theorem 1)

Rule (Sq) for τ = 21: N = first n such that {z_1..z_n} contains a descent; K = {a, b} where, if z_N = (U s_N, s_N)
lies on the top side, a = z_N and b = the earlier point with the smallest x-coordinate exceeding U s_N, and if
z_N = (s_N, U s_N) lies on the right side, b = z_N and a = the earlier point with the smallest y-coordinate exceeding
U s_N.  So c = (x_b, s_N) resp. (s_N, y_a).  The rule commutes with transposition, so (dx, dy) is exchangeable and
Theorem A gives c_{21} ≥ 2/E[dx+dy].

**Lemma 3.1.**  Conditionally on s_{n+1} = r, the points z_1..z_n are i.i.d. uniform on (0,r)², and z_{n+1} is
independent of them, uniform on the two sides {r}×(0,r), (0,r)×{r} (side chosen with probability ½).
Proof.  By Lemma A1, conditionally on φ(s_{n+1}) = r², the values φ(s_1) < … < φ(s_n) are the order statistics of n
i.i.d. uniforms on (0, r²), the marks are i.i.d. and independent of everything; mapping back (s_i = √φ(s_i), and the
mark) yields n i.i.d. points with density (2s ds)(du)(½ on each side)/r² on (0,r)², i.e. uniform (Jacobian computation
of Lemma A1 read backwards).  ∎

**Lemma 3.2.**  Let W_1..W_n be i.i.d. uniform on (0,1)² conditioned on forming an increasing chain (an event of
probability 1/n!).  Then the sorted x-coordinates and the sorted y-coordinates are independent, each distributed as
the order statistics of n i.i.d. uniforms on (0,1).
Proof.  For i.i.d. uniform points, the vector of x-order statistics, the vector of y-order statistics, and the
permutation π relating x-order to y-order are independent (the coordinates are independent, and for i.i.d. continuous
variables the order statistics are independent of the ranks).  The chain event is {π = id}.  ∎

**Proof of Theorem 1.**  The event {N = n+1} means: z_1..z_n form an increasing chain (no descent among them) and
z_{n+1} creates a descent.  Since {N = n+1} and the ratios (dx, dy)/s_{n+1} are functions of the "shape"
(z_i/s_{n+1})_{i≤n+1}, which by Lemma 3.1 is independent of s_{n+1}, and s_{n+1} = √(E_1+…+E_{n+1}) with
E[√Γ(n+1,1)] = Γ(n+3/2)/Γ(n+1) = Γ(n+3/2)/n!,
    E[dx+dy] = Σ_{n≥1} (Γ(n+3/2)/n!) · E[ (dx+dy)/s_{n+1} ; N = n+1 ].
Take r = 1 and z_{n+1} on the top side (the right side gives the same by symmetry): z_{n+1} = (W, 1) with W uniform;
the n earlier points are i.i.d. uniform, a chain with probability 1/n!, and by Lemma 3.2 their sorted x-coordinates
x_(1) < … < x_(n) are uniform order statistics, independent of W.  A descent exists iff W < x_(n); the partner b has
x-coordinate x_(k+1) where k = #{i : x_(i) < W} ∈ {0..n−1}; the rank of W among the n+1 i.i.d. values
x_(1..n), W is uniform, and given k, x_(k+1) is the (k+2)-th order statistic of these n+1 uniforms, with mean
(k+2)/(n+2).  The cost is dx + dy = x_b + 1.  Therefore
    E[(dx+dy)/s_{n+1}; N = n+1] = (1/n!) · (1/(n+1)) Σ_{k=0}^{n−1} (1 + (k+2)/(n+2)) = (1/n!) · n(3n+7) / (2(n+1)(n+2)),
and
    E[dx+dy] = Σ_{n≥1} Γ(n+3/2) · n(3n+7) / (2(n+2) · n! · (n+1)!) =: Σ_n T_n.
Checks: Σ_n P(N = n+1) = Σ_n (1/n!)·n/(n+1) = Σ_n n/(n+1)! = 1 and E N = Σ (n+1) n/(n+1)! = e (Monte Carlo 2.7184).
Numerically T_1..T_8 = 1.107784, 0.900074, 0.387724, 0.115106, 0.026180, 0.004834, 0.000752, 0.000101;
Σ_{n≤10} T_n = 2.5425685820, and T_{n+1}/T_n = (n+3/2)(3n+10) / (n(n+3)(3n+7)) ≤ 0.096 for n ≥ 10,
so the tail after n = 10 is ≤ 2 T_{11} < 3·10⁻⁷: E[dx+dy] = 2.5425687 (to 7 digits), and
    c_{21} ≥ 2/2.5425687 = 0.786606.  ∎
Monte Carlo of the rule (rules.c, rule 1, 2·10⁷ samples): E[dx+dy] = 2.54276 ± 0.00022 (1 s.e.), E dx = E dy = 1.2714.

--------------------------------------------------------------------------------------------------
## 4. General τ (Theorem 3)

Square rule for τ ∈ S_j: N = first n such that {z_1..z_n} contains a copy of τ; among the copies (all contain z_N)
choose one minimizing the cost; c = cor(K).  If z_N = (s_N, U s_N) is on the right side, z_N is the rightmost point
of the copy, c = (s_N, max y of the copy); on the top side, c = (max x of the copy, s_N).
By Lemma 3.1, conditionally on s_{N}=r and N = m, the m−1 earlier points are i.i.d. uniform in (0,r)², i.e. (ranks) a
uniform permutation σ of size m−1, conditioned to avoid τ (probability a_{m−1}), and the new point has a uniform
independent rank r' ∈ {1..m} in the other coordinate.  Right side: the configuration is σ with a new rightmost point
of y-rank r'; the number of (σ, r') creating a copy is cnt_m(τ) = m·|Av_{m−1}(τ)| − |Av_m(τ)| (each corresponds to a
permutation of size m containing τ whose first m−1 entries avoid it); given the ranks, the m y-values are i.i.d.
uniform on (0,r) independent of the ranks, and the copy's top y-value is the t-th order statistic, t = minTop(σ,r'),
with mean r·t/(m+1).  Top side: transposing, the same with τ⁻¹.  With E s_m = Γ(m+½)/Γ(m) and independence of shape
and radius exactly as in §3,
   E[dx+dy] = Σ_{m≥j} (Γ(m+½)/Γ(m)) · [ (cnt_m(τ)+cnt_m(τ⁻¹))/(2·m!) + (sumTop_m(τ)+sumTop_m(τ⁻¹))/(2(m+1)·m!) ],
which is (a) (for τ = 21: cnt_m = m−1, sumTop_m = (m−1)(m+2)/2, and this is the series of §3 with n = m−1).
Strip rule for τ: N = first n such that {z_1..z_n} contains a copy, K = a copy with minimal top; dx = s_N with
E dx = E N/h, E N = Σ_{m≥0} P(N > m) = Σ_m a_m = E n_τ; dy = h·(top of K) with E dy = h Σ_m sumTop_m/((m+1) m!) = h E top_τ;
Theorem A with h² = E n_τ/E top_τ gives (b); c_τ = c_{τ⁻¹} (W10 Lemma B) allows τ⁻¹.  ∎

**Evaluation (tau_bounds.py, enum3.c).**  cnt_m, sumTop_m were enumerated exactly for m ≤ 11 (enum3.c; for 21 they
agree with the closed forms).  Tail m > 11: sumTop_m ≤ m·cnt_m, so each term of (a) is ≤ 2(Γ(m+½)/Γ(m))·(a_{m−1}−a_m)
with cnt_m/m! = a_{m−1} − a_m; for (b), Σ_{m>11} sumTop_m/((m+1)m!) ≤ Σ_{m>11}(a_{m−1}−a_m) = a_{11}.  For a_m, m > 11:
|Av_m| = Catalan(m) for j = 3; for j = 4, Gessel's formula |Av_m(1234)| = Σ_k C(2k,k)C(m+1,k+1)C(m+2,k+1)/((m+1)²(m+2))
[I. Gessel, *Symmetric functions and P-recursiveness*, JCTA 53 (1990), §7] and Bóna's formula
|Av_m(1342)| = (−1)^{m−1}(7m²−3m−2)/2 + 3Σ_{i=2}^m (−1)^{m−i} 2^{i+1} (2i−4)!/(i!(i−2)!) C(m−i+2,2)
[M. Bóna, *Exact enumeration of 1342-avoiding permutations*, JCTA 80 (1997), Thm 1]; both were checked against the
enumerated |Av_m| for all m ≤ 11 (the enumeration determines |Av_m| = m|Av_{m−1}| − cnt_m) and used for m ≤ 400
(beyond which a_m ≤ a_{11}^{⌊m/11⌋} < 10⁻³⁰ is negligible).  Each pattern of S_4 is Wilf-equivalent to 1234, 1342 or 1324
[Z. Stankova, *Forbidden subsequences*, Discrete Math. 132 (1994) 291–316, and *Classification of forbidden
subsequences of length 4*, European J. Combin. 17 (1996) 501–517: the three Wilf classes of S_4 are those of 1234
(8 patterns), 1342 (8 patterns), 1324 (8 patterns)]; which formula applies to each class was also confirmed by the
enumerated counts for m ≤ 11; the 1324 class (1324 and 4231; the 1324 counts have no closed form) uses the block bound
a_m ≤ a_{11}·a_{11}^{⌊(m−11)/11⌋} (disjoint x-blocks avoid τ independently).  Results (classes under τ ↦ τ⁻¹, τ ↦ τ^{rc},
which preserve c_τ):
  τ        square (a)   strip (b)     τ        square (a)   strip (b)
  123/321   0.5384       0.5243       1342~    0.4100       0.4036
  132~213   0.5354       0.5214       2341~    0.4127       0.4075
  231~312   0.5516       0.5390       2413~    0.4105       0.4047
  1234/4321 0.4035       0.3963       2431~    0.4115       0.4057
  1243~     0.4020       0.3947       3412     0.4126       0.4064
  1324      0.3853*      0.3742*      3421~    0.4114       0.4064
  1432~     0.4017       0.3944       4231     0.3932*      0.3832*
  2143      0.4020       0.3947       (* block tail bound; the others use exact |Av_m|)
For j = 4 the tail m > 11 carries real mass (a_{11} ≈ 0.094): the "sumTop ≤ m·cnt" bound costs about 0.15 in E[dx+dy],
i.e. about 0.01 in the constant.  Sanity: for 1234 the bound 0.4035 is below the true value c_{1234} = 2/4 = 0.5 (LIS).

--------------------------------------------------------------------------------------------------
## 5. Limits of the method (Proposition 4) and the obstruction to c_{21} = 1

For any rule as in Theorem A, K contains a descent pair (a,b) with a above-left of b, and c = cor(K) ≥ (x_b, y_a), so
dx + dy ≥ M := min over all descent pairs of Π ∩ Q of (x_b + y_a).  Monte Carlo (floor.py, 2·10⁵ samples of Π on
(0,7)²): E M = 2.3861 ± 0.0019.  Hence 2/E[dx+dy] ≤ 0.838 for every rule, causal or not: **the renewal method cannot
give c_{21} > 0.84**.  The rules actually tried (rules.c): strip 2.6397 (exact), square 2.5426 (exact), ℓ_1 sweep
2.5064, ℓ_1.5 sweep 2.4884 ± 0.0002 (c ≥ 0.8037), ℓ_2 2.4943, ℓ_3 2.5102; delayed stopping (accept iff cost ≤ θ·s) never
helps.  The exactly computable rules are those with a product sweep region (rectangles: Lemma 3.2); the ℓ_p rules
would need the law of a uniform chain in a triangle/ℓ_p ball, for which no closed form is available.

Why 1 is out of reach for local rules.  The renewal construction advances by E[dx+dy]/2 ≈ 1.27 per copy in each
coordinate, whereas c_{21} = 1 requires an average advance of exactly 1 per copy, i.e. each descent pair must sit in a
box of mean area 1 (mean number of points 1) — impossible for a pair chosen without looking ahead, since the pair
itself needs two points.  The optimal chain is not a Markov object: it picks, among the e^{Θ(√N)} near-optimal chains
of blocks, one whose blocks are globally compatible.  Quantitatively, for the LIS the same greedy method gives
√(8/π) = 1.596 = 0.80·2, and here 0.804 vs (conjecturally) 1: the loss ratio is the same.  The "boxes along a maximal
chain" route of the task statement (boxes U_i = (x_{i−1},x_i) × (y_i,y_{i+1}) along a patience-sorting LIS path) is
much weaker: only 15 % of the boxes are nonempty and a stacked greedy selection gives L_{21}/√N ≥ 0.26 (boxes.c,
N = 10⁵) — the gaps along a maximal chain are ≈ 1/(2√N) so the boxes have mean N·area ≈ ¼; the joint law of
consecutive gaps along the point-to-point geodesic (which would be needed to make this rigorous) is not available
from Cator–Groeneboom, whose Burke-type results describe the stationary process on lines, not along the geodesic.
What a proof of c_{21} = 1 needs is the entropy statement of W12 log §1 (near-optimal chains with all corner boxes
nonempty after discarding o(√N) points), for which neither renewal rules nor the exactly solvable Hammersley
structure suffice.
