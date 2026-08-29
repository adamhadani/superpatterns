# W12 — rigorous bounds on c_{21} and on c_τ (proofs)

Date 2026-08-29.  Setting as in W5/W10: Π_N = Poisson process of intensity N on [0,1]²; for τ ∈ S_j, a τ-chain of
length L is a copy of τ^{⊕L}; L_τ(N) = longest τ-chain; c_τ = lim L_τ(N)/√N (exists a.s. and in mean, W5 Lemma B).
Known before this note: 0.40 ≤ c_{21} ≤ e/2 = 1.359 (diagonal greedy; first moment).  Conjecture: c_{21} = 1, c_τ = 2/j.

## Results

**Theorem 1 (lower bound).**  c_{21} ≥ 0.598.  More generally, for every τ ∈ S_j, every δ > 0 and every t ≥ 1,
    c_τ ≥ t · g(p_{τ,t}(δ²)) / δ,   g(p) := 2√p/(1+√p),   p_{τ,t}(λ) := Pr(τ^{⊕t} ⊂ Π_λ).
For 21: p_{21,1}(λ) = 1 − e^{−λ} I₀(2√λ) gives c_{21} ≥ 0.5769 (δ = 1.11); t = 2 gives c_{21} ≥ 0.5983 (δ = 2.67).

**Theorem 2 (universal upper bound).**  For every k, N ≥ 1 and EVERY pattern π ∈ S_k,
    Pr(π ⊂ Π_N) ≤ 668 · N^{−1/2} · exp(3√N − 1.3163 k).
Hence for every π of length k ≥ 2.2790·√N + C log N, Pr(π ⊂ Π_N) → 0; in particular
    c_τ ≤ 2.2790 / j  for every τ ∈ S_j,   and   c_{21} ≤ 1.1395.
(The first moment gives only e/j = 2.7183/j and c_{21} ≤ 1.359.)  The constant 2.2790 is
κ* = min_σ 2σ / log(1/ρ(σ)), ρ(σ) = spectral radius of the positive kernel T_σ(u,u') = e^{−σu'}/(σ+u+u') on
(0,∞); the number 1.3163 = log(1/0.26808) is a Collatz–Wielandt certificate at σ = 1.5 (§2.4, computer-assisted).

**Proposition 3 (exact pattern-independence).**  For every N and every π, π' ∈ S_k the expected numbers of
*leftmost-canonical* copies (§2.1) of π and of π' in Π_N coincide (this refines W10's first-moment identity
E#copies(π) = C(N,k)/k!, which is what one gets by dropping the canonical condition).

So: **0.598 ≤ c_{21} ≤ 1.140**, and 0.55·(2/j) ≲ c_τ ≤ 1.14·(2/j) for all τ of length ≤ 5 (numerical values §1.3).

--------------------------------------------------------------------------------------------------
## 1. Lower bound (Theorem 1)

### 1.1 The Bernoulli-site theorem (Seppäläinen)
Let the sites of {1..n}² be occupied independently with probability p, and let B_n(p) be the maximum number of
occupied sites on a chain (i_1,j_1), …, (i_M,j_M) with i_1 < i_2 < … and j_1 < j_2 < … (strictly increasing in
both coordinates).  Then B_n(p)/n → g(p) = 2√p/(1+√p) a.s. and in L¹.
[T. Seppäläinen, *Increasing sequences of independent points on the planar lattice*, Ann. Appl. Probab. 7 (1997)
886–898: the limit shape is Ψ(x,y) = (2√(pxy) − p(x+y))/(1−p) for p ≤ y/x ≤ 1/p; at x = y = 1 this is g(p).]
Numerical check (bern.c, n = 1500, 4 samples): p = .10/.22/.50 give B/n = .473/.632/.825 vs g(p) = .4805/.6386/.8284,
the deficit being the usual negative n^{−1/3} correction.

### 1.2 Proof of Theorem 1
Fix τ ∈ S_j, t ≥ 1, δ > 0.  Put m = ⌊√N/δ⌋ and tile [0, mδ/√N]² ⊂ [0,1]² by the m² closed squares
C_{ab} = [ (a−1)δ/√N, aδ/√N ] × [ (b−1)δ/√N, bδ/√N ], 1 ≤ a,b ≤ m (open interiors are disjoint; the boundaries
carry no points a.s.).  The restrictions Π_N ∩ C_{ab} are independent, and each is the image of a Poisson process of
intensity N on a square of side δ/√N, i.e. an affine image of Π_{δ²}; containment of τ^{⊕t} is affine-invariant, so
ξ_{ab} := 1{τ^{⊕t} ⊂ Π_N ∩ C_{ab}} are i.i.d. Bernoulli(p) with p = p_{τ,t}(δ²).
If (a_1,b_1), …, (a_M,b_M) is a chain of occupied sites with a and b strictly increasing, then the copies of τ^{⊕t}
inside C_{a_1b_1}, …, C_{a_Mb_M} are pairwise strictly separated (every point of C_{a_ib_i} is strictly below-left of
every point of C_{a_{i+1}b_{i+1}}, as the squares are in different rows and columns), so their union is a copy of
τ^{⊕tM}: L_τ(N) ≥ t·B_m(p).  Dividing by √N ≥ mδ: L_τ(N)/√N ≥ t B_m(p)/(mδ) · (mδ/√N) → t g(p)/δ a.s. as N → ∞
(mδ/√N → 1).  Since L_τ(N)/√N → c_τ a.s., c_τ ≥ t g(p)/δ.  ∎

### 1.3 Numbers
p_{21,1}(λ) = 1 − e^{−λ} Σ_k λ^k/(k!)² = 1 − e^{−λ}I₀(2√λ) (a k-point cloud avoids 21 iff it is increasing, prob. 1/k!).
Maximizing g(p_{21,1}(δ²))/δ: 0.57694 at δ = 1.11 (p = 0.222).  With t = 2 one needs p_{21,2}(λ) = Pr(2143 ⊂ Π_λ);
q_k(τ) := Pr(τ ⊂ uniform σ ∈ S_k) was computed exactly by enumeration for k ≤ 10 (pat.c, pat.out; e.g.
Av_10(1234) = 586590 = Av_10(2143), as it must be by Wilf-equivalence), and since q_k is nondecreasing in k
(deleting a uniformly random point of a uniform permutation gives a uniform permutation, and containment is
monotone), p_{τ,t}(λ) ≥ Σ_{k≤10} e^{−λ}λ^k/k!·q_k + Pr(Poisson(λ) > 10)·q_{10}.  This gives
2·g(p_{21,2}(δ²))/δ ≥ 0.5983 at δ = 2.67, i.e. **c_{21} ≥ 0.598**.  (t = 3 gives only 0.377: the truncation at k ≤ 10
is far too lossy there.)
Other τ (t = 1, lb_tau.py; all exact-enumeration truncations):
  τ ∈ S_3 (all Wilf-equivalent: Av = Catalan): c_τ ≥ 0.3890 = 0.584·(2/3);
  τ ∈ S_4: 0.2991 (1234, 1243, 2143), 0.3000 (1342), 0.2990 (1324) ≈ 0.60·(2/4);
  τ ∈ S_5: 0.2191 (12345, 21345), 0.2215 (25314), 0.2190 (13254) ≈ 0.55·(2/5).
Universal in j: Arratia's grid gives p_{τ,1}(λ) ≥ (1 − e^{−λ/j²})^j for every τ ∈ S_j (place a j×j sub-grid of cells of
side δ/j and ask that cell (i, τ(i)) be nonempty), hence with λ = j²(ln j + s): c_τ ≥ g(e^{−e^{−s}}(1+o(1)))/(j√(ln j + s)),
i.e. c_τ ≥ (0.7 − o(1)) / (j √ln j), off from 2/j by a factor O(√ln j) only.

--------------------------------------------------------------------------------------------------
## 2. Upper bound (Theorem 2, Proposition 3)

### 2.1 Leftmost-canonical copies
Let π ∈ S_k and let P = {p_1, …, p_k} ⊂ Π_N be a copy of π, p_r = (x_r, y_r) listed in increasing x, so that the
y-rank of p_r is π(r).  For each r let
   g_r = x_r − x_{r−1} (x_0 := 0),   h_m = y_{(m)} − y_{(m−1)} for m = 0..k (y_{(0)} := 0, y_{(k+1)} := 1),
where y_{(1)} < … < y_{(k)} are the y-values in increasing order; so g_1, …, g_k, g_{k+1} := 1 − x_k and h_0, …, h_k
are the x- and y-gaps.  The *allowed box* of p_r is B_r = (x_{r−1}, x_{r+1}) × (y_{(π(r)−1)}, y_{(π(r)+1)}): replacing
p_r by any point of B_r keeps the x- and y-ranks of all k points, hence gives another copy of π.  Call the copy
**leftmost-canonical** if for every r no point of Π_N lies in the strip
   S_r = (x_{r−1}, x_r) × (y_{(π(r)−1)}, y_{(π(r)+1)}) ⊂ B_r,        |S_r| = g_r (h_{π(r)−1} + h_{π(r)}).
**Claim A.** If π ⊂ Π_N then Π_N contains a leftmost-canonical copy of π.  Proof: Π_N is a.s. finite with distinct
x-coordinates; among the (finitely many) copies take one minimizing Σ_r x_r.  If some S_r contained a point q, then
(P \ {p_r}) ∪ {q} would be a copy of π (q ∈ B_r) with smaller Σ x.  ∎
**Claim B.** The strips S_1, …, S_k are pairwise disjoint (their x-projections (x_{r−1}, x_r) are consecutive
disjoint intervals).  ∎

### 2.2 The expected number of canonical copies
By the multivariate Mecke formula (for a Poisson process, E Σ_{distinct p_1..p_k ∈ Π} f(p_1..p_k; Π \ {p_1..p_k})
= N^k ∫ E f(p_1..p_k; Π) dp), and since given the k points the number of points of Π_N in the union of the strips
is Poisson(N Σ|S_r|) (Claim B),
   E_k(π, N) := E #{leftmost-canonical copies of π in Π_N} = N^k ∫_{pattern π} exp(−N Σ_{r=1}^k g_r (h_{π(r)−1}+h_{π(r)})) dx dy.
In the gap coordinates the domain {configurations with pattern π} is exactly Δ_x × Δ_y with Δ_x = {g_1..g_k > 0,
Σ_{r≤k} g_r < 1} and Δ_y = {h_0..h_k > 0, Σ h = 1} (Lebesgue measure on the y-simplex is the k-dimensional one),
and the Jacobian is 1.  **Proposition 3** follows: substituting g'_m = g_{π^{-1}(m)} (a permutation of coordinates,
which preserves Δ_x) turns the integrand into Π_m exp(−N g'_m (h_{m−1}+h_m)), which does not depend on π.  ∎
(Sanity check by simulation, mecke_check.py, N = 5: E_2(12, 5) = 1.0575 / integral 1.0570; E_2(21,5) = 1.0572 / 1.0572.)

Since Pr(π ⊂ Π_N) ≤ E_k(π, N) by Claim A, Theorem 2 follows from a bound on E_k := E_k(π, N).

### 2.3 Laplace (Chernoff) decoupling
For s, t > 0: on Δ_x, e^{s(1 − Σ_{r≤k} g_r)} ≥ 1; on Δ_y, e^{t(1 − Σ h)} = 1.  Extending both domains to the full orthants,
   E_k ≤ N^k e^{s+t} ∫_{R_+^k} ∫_{R_+^{k+1}} e^{−s Σ g − t Σ h} Π_{m=1}^k e^{−N g'_m (h_{m−1}+h_m)} dg' dh
       = N^k e^{s+t} ∫_{R_+^{k+1}} e^{−t Σ_{m=0}^k h_m} Π_{m=1}^k 1/(s + N(h_{m−1} + h_m)) dh          (g'_m integrated out).
Take s = t = σ√N and substitute h_m = u_m/√N.  Each factor becomes N^{−1/2}/(σ + u_{m−1} + u_m), dh = N^{−(k+1)/2} du, so
   E_k ≤ N^{−1/2} e^{2σ√N} ∫_0^∞ e^{−σ u_0} (T_σ^k 1)(u_0) du_0,     (T_σ f)(u) := ∫_0^∞ e^{−σ u'} f(u')/(σ + u + u') du'.   (★)
(Check: replacing e^{−Nab} by 1, i.e. dropping the canonical condition, the same computation gives the first-moment
bound with kernel e^{−σu'}/σ, ρ = 1/σ², and min_σ 2σ/(2 log σ) = e/2 per √N for k/2 — i.e. k ≤ e√N, as it should.)

### 2.4 Collatz–Wielandt certificate
Let φ > 0 be bounded above and below on (0,∞) and suppose (T_σ φ)(u) ≤ ρ̄ φ(u) for all u ≥ 0.  Then T_σ^k 1 ≤
T_σ^k(φ/inf φ) ≤ ρ̄^k φ/inf φ ≤ ρ̄^k sup φ/inf φ (T_σ is a positive operator), and (★) gives
   E_k ≤ (sup φ / inf φ) · N^{−1/2} e^{2σ√N} ρ̄^k / σ.
**Certificate.**  σ = 1.5, φ(u) = 10^{−3} + (1 + u/1.7777)^{−0.9584}.  Then sup φ/inf φ ≤ 1001 and
   sup_{u ≥ 0} (T_σ φ)(u)/φ(u) ≤ 0.26808.                                                              (C)
Verification of (C): for u ≥ 3400, (T_σφ)(u) ≤ (1+10^{−3})/(σ(σ+u)) ≤ 2·10^{−4} ≤ 0.2·φ(u); for u ∈ [0, 3400] the ratio
was evaluated by adaptive quadrature (scipy.integrate.quad, abs/rel tolerances 10^{−15}/10^{−13}) on a grid of 1550
points (step 0.01 on [0,12], 0.2 on [12,80], then 100 … 3400); the maximum is 0.268072 at u = 0, the ratio is flat on
[0,1] (0.268056–0.268072) and then decreases monotonically (0.2678 at u=2, 0.2590 at 16, 0.2188 at 200, 0.0888 at 3400);
consecutive grid values differ by < 2·10^{−7} near the maximum.  The true spectral radius,
computed by power iteration on a discretized kernel (M = 40…120, n = 4000…8000 nodes, converged to 7 digits) is
ρ(1.5) = 0.268059, so the certificate is sharp to 2·10^{−5}.  **This step is computer-assisted in floating point
(not interval arithmetic)**; everything else in the proof is exact.
With (C): E_k ≤ 1001/1.5 · N^{−1/2} e^{3√N} 0.26808^k ≤ 668 N^{−1/2} exp(3√N − 1.31637 k), which is Theorem 2.  ∎
(Scanning σ: 2σ/log(1/ρ(σ)) = 2.426 (σ=1), 2.298 (1.3), 2.2843 (1.4), 2.2787 (1.5), 2.2791 (1.6), 2.318 (2), 2.524 (3):
the optimum κ* = 2.2787 is at σ ≈ 1.5; no further gain is available from σ.)

### 2.5 Consequences
(i) For τ ∈ S_j and L ≥ (2.2790/j + ε)√N: Pr(L_τ(N) ≥ L) ≤ Pr(τ^{⊕L} ⊂ Π_N) ≤ 668 N^{−1/2} e^{3√N − 1.3163 jL} → 0, and since
L_τ(N)/√N → c_τ in probability, c_τ ≤ 2.2790/j.  For j = 2: **c_{21} ≤ 1.1395**.
(ii) Uniform permutations: Pr(π ⊂ σ_n) ≤ Pr(π ⊂ Π_{(1+ε)n}) + Pr(|Π_{(1+ε)n}| < n), so every pattern π of length
k ≥ (2.2790+ε)√n is absent from a uniform σ_n whp; in other words the containment threshold of *every* π ∈ S_k is
≥ (0.1925 − o(1))k² = (1.42/e²)k², versus the first-moment value k²/e² = 0.1353k².  (Deterministic superpattern
lower bounds are NOT implied: the count of canonical k-subsets of a fixed σ can be as large as C(n,k).)
(iii) The 21-specific variants of the canonical condition ("a_i leftmost in its box, b_i lowest in its box", regions
(α_i+β_i)δ_{i−1} + β_{i−1}(γ_i+δ_i) in the notation of log.md §3) give a coupled transfer kernel
T(d,d') = e^{−σd'} e^{x}E₁(x)/(σ+d), x = σ(σ+d+d'), with min_σ 2σ/log(1/ρ) = 1.1606 — slightly WORSE than the universal
1.1395; the fully factorized versions (corner boxes only: 1.2702; decoupled: 1.2109) are worse still.  So among the
canonical rules tried, "leftmost for every point" is the best, and it does not see the pattern at all.

--------------------------------------------------------------------------------------------------
## 3. What is not proved
c_{21} = 1 (numerically L_{21}(N)/√N = 0.881, 0.904, 0.940, 0.955, 0.958, 0.971, 0.981 at N = 400 … 10⁵, W10 data,
the deficit being ≈ 1.77·N^{−1/3}/2 as for the LIS).  The rigorous window is [0.598, 1.140].  Both bounds are limited
by their method, not by computation: the grid lower bound cannot exceed max_δ 2/(δ(1+√p)) < 1 by construction
(one cell = one block, and cells in the same grid row are wasted), and the canonical-copy upper bound cannot go below
what it gives for the identity (κ* = 2.279 per √N for the LIS, whose truth is 2), i.e. below 1.14 for c_{21}.
