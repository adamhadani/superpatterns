# W12 — c_{21} = 1 ?  (log)

Date 2026-08-29.  Directory work/w12-c21/.  Files: proof.md (theorems + proofs), bounds.py (lower bound + factorized
upper bounds), certify.py / cert2-4.py (transfer operators, spectral radii, Collatz–Wielandt certificate), transfer.py
(21-specific coupled operator), bern.c (Seppäläinen check), pat.c + pat.out (exact Pr(τ ⊂ S_k), k ≤ 10), lb_tau.py
(general-τ lower bounds), mecke_check.py (simulation check of the canonical-copy formula).  Python deps in .venv/.
Time spent ≈ 2 h.

## 0. Outcome in one line
Rigorous: **0.598 ≤ c_{21} ≤ 1.140** (before: 0.40 ≤ c_{21} ≤ 1.359).  General τ ∈ S_j: c_τ ≤ 2.279/j for ALL τ (first
moment: 2.718/j), c_τ ≥ explicit grid bound ≈ 0.55–0.60·(2/j) for |τ| ≤ 5.  c_{21} = 1 remains open; the numerics
(L_{21}/√N = 0.88 → 0.98 for N = 400 → 10⁵, approaching 1 like the LIS's 2 − 1.77N^{−1/3}) leave no doubt about the value.

## 1. Route (a), thickening — abandoned (why)
Thin Π_N into Π^A (intensity (1−η)N) and Π^B (ηN); take an LIS of Π^A (≈ 2√((1−η)N) points) and look for Π^B-points
in the corner boxes R_i = (x_{a_i}, x_{a_{i+1}}) × (y_{a_{i−1}}, y_{a_i}).  A 21-chain of length L is exactly an increasing
chain a_1 < … < a_L with ALL corner boxes nonempty (b_i ∈ R_i; the b's impose no further constraints among
themselves).  Corner boxes of a full LIS have expected η/4 points; subsampling every r-th chain point gives boxes
with ≈ ηr²/4 points and chain length 2√N/r, i.e. c_{21} ≥ max_{r,η} 2√(1−η)(1 − e^{−ηr²/4})/r ≈ 0.28 — worse than the
grid bound below.  The adaptive version (choose the subsequence by a 1-D DP along the chain) needs the law of the
gaps along a Hammersley geodesic, which is not explicit.  The real content of "c_{21} = 1" is the entropy statement
that among the e^{Θ(√N)} chains of length (2−ε)√N one can find one with all corner boxes nonempty after discarding
only o(√N) points; nothing in the exactly-solvable toolbox (RSK, stationary Hammersley) gives that.

## 2. Route (b), grid + Bernoulli LIS — done (Theorem 1)
Cells of side δ/√N; ξ_c = 1{cell contains τ^{⊕t}} i.i.d. Bernoulli(p); strictly increasing chains of cells give τ-chains;
Seppäläinen's constant g(p) = 2√p/(1+√p) (checked by simulation: n=1500, p=.1/.22/.5 → .473/.632/.825 vs .481/.639/.828).
c_τ ≥ t g(p_{τ,t}(δ²))/δ.  For 21, t=1: p = 1 − e^{−λ}I₀(2√λ), optimum δ = 1.11: 0.5769.  t = 2 (cells containing 2143,
weight 2): 0.5983 at δ = 2.67 (with q_k(2143) exact for k ≤ 10 and the monotone truncation).  t = 3: 0.377 (truncation
at k ≤ 10 kills it).  Other τ: S_3: 0.389 (=0.58·2/3); S_4: 0.299–0.300 (0.60·2/4); S_5: 0.219–0.222 (0.55·2/5).  Universal:
Arratia grid ⇒ c_τ ≥ (0.7−o(1))/(j√ln j).
Why it cannot reach 1: g(p)/δ ≤ 2/(δ(1+√p)) and p(δ²) ≤ 1 − e^{−δ²}(1+δ²) ⇒ the bound is < 0.6 for all δ.  The loss is
structural (one block per cell; cells in the same row unusable), not a matter of better Bernoulli constants.
Possible improvements (not done): i.i.d. cell weights w_c = L_{21}(cell) and strict-chain LPP — no exact constant is
known for general weights; a Monte-Carlo estimate would only give an MC-certified bound like W10's 0.96.

## 3. Route (c), upper bound — the useful surprise (Theorem 2, Proposition 3)
Idea: count only *canonical* copies.  Among all copies of π take the one minimizing Σ x; then every point is the
leftmost point of Π_N in its allowed box (the box in which it can move without changing the pattern), i.e. the strip
(x_pred, x_p) × (y_pred, y_succ) is empty.  The strips are disjoint (consecutive x-intervals), so
E#canonical = N^k ∫ exp(−N Σ_r g_r(h_{π(r)−1} + h_{π(r)})) over (x-gaps) × (y-gaps), and permuting the x-gaps shows
this is EXACTLY the same for every π ∈ S_k (Prop. 3; refines W10's identity E#copies = C(N,k)/k!).  Chernoff on the
two simplices + integrating the x-gaps leaves a 1-D transfer operator on consecutive y-gaps,
T_σ(u,u') = e^{−σu'}/(σ+u+u'), and P(π ⊂ Π_N) ≤ C N^{−1/2} e^{2σ√N} ρ(T_σ)^k.  Numerically ρ(1.5) = 0.268059, and
κ* = min_σ 2σ/log(1/ρ(σ)) = 2.2787 (σ = 1.5); certified by the test function φ(u) = 10^{−3} + (1+u/1.7777)^{−0.9584}
(sup Tφ/φ ≤ 0.26808, max at u = 0; floating-point quadrature, not interval arithmetic).  Hence
  P(π ⊂ Π_N) ≤ 668 N^{−1/2} exp(3√N − 1.3163 k)  for EVERY π ∈ S_k,
so every pattern of length > 2.279√N is absent whp (first moment: e√N = 2.718√N), and c_τ ≤ 2.279/j, c_{21} ≤ 1.1395.
Simulation check of the canonical-count formula at N = 5, k = 2: sim 1.0575/1.0572 vs integral 1.0570/1.0572 (12 / 21).
21-specific canonical rules tried (a leftmost & b lowest; regions (α_i+β_i)δ_{i−1} + β_{i−1}(γ_i+δ_i)): coupled kernel
e^{−σd'}e^{x}E₁(x)/(σ+d), x = σ(σ+d+d'): 1.1606 — worse than the universal 1.1395.  Factorized versions: corner boxes
only (k(σ) = 1/σ² − e^{σ²}E₁(σ²)): 1.2702; decoupled a/b regions (w(σ) = e^{σ²}∫_σ^∞ E₁(σr)/r dr): 1.2109.
Sanity: for the identity the same bound says LIS ≤ 2.279√N (truth 2); for 21-chains it says c_{21} ≤ 1.14 (truth ≈ 1):
the method is ≈ 14 % off in both cases, consistent with "21-chains behave like half an LIS".
Side remark (not a superpattern result): the bound gives the containment threshold of every individual π ∈ S_k as
≥ (1.42/e² − o(1))k² = 0.1925k² (vs k²/e² from the first moment).  It does NOT give sp(k) ≥ 0.19k²: for a fixed σ the
number of canonical k-subsets is not controlled (identity σ: canonical subsets are intervals; but other σ may have C(n,k)).
Whether "every π ∈ S_k has threshold ≥ 0.19k²" is new I could not check offline; it is at least not in NOTES.md.

## 4. Ideas for closing the gap (not executed)
Upper bound: canonical copies with respect to a general potential Σ ψ(p) (e.g. ψ = x + y gives triangular empty
regions; regions may overlap, so one must use the union area) — a family of bounds whose infimum might approach 2
for the LIS; the leftmost rule is just the first member.  Second: combine canonical counting with the interlacing
structure of 21-chains (a_i, b_i in each other's corner boxes) — the coupled kernel above is one attempt and lost to the
universal one, which suggests the 21-structure is not what limits the bound.
Lower bound: a Poisson-level (not grid) construction with an exactly solvable model: e.g. Hammersley with two
particle types or the "two-line" RSK dynamics; or prove the entropy statement of §1 via the Deuschel–Zeitouni
large-deviation description of near-optimal chains (they concentrate near the diagonal; one would need the local
statistics along typical near-optimal chains, which the LDP does not give).
