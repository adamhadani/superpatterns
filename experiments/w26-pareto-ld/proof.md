# W26 — Pareto-front / level-set certificates for the two-strip pattern (12)^h

Tags: **PROVED**, **HEURISTIC**, **NUMERICAL**.  Notation: k = 2h, N points, the *iid colour model*
(W20 Prop 1.1): N iid uniform points in [0,1]² with iid uniform colours in {0,1}; fixed-strip containment of
π = (12)^h = 1 (h+1) 2 (h+2) ⋯ h (2h) in N iid uniform points is equivalent to the existence of points
q_1,…,q_k with x(q_1)<⋯<x(q_k), colour(q_t) = (t−1) mod 2, and y increasing along each colour class.  (The
Poisson model Π_N is handled in Remark 1.4.)  "p < q" means x_p < x_q and y_p < y_q (2D dominance).

## 0. Summary

* **Thm 1.1 (PROVED).**  Pr((12)^h ⊄_fix N iid points) ≤ 2^{−N} Σ_{m=0}^{N} C(N,m) Σ_{n} m!/Π_{j}(n_j!)²,
  the inner sum over compositions n of m into 2(k−1) parts.  Consequently, at N = Ck²,
  Pr ≤ exp(−ρ(C)·N + O(k ln N)) with ρ(C) = ln 2 − sup_{0<β≤1}[H(β) + β ln(4e/(βC))]
  (H = binary entropy in nats), ρ(C) > 0 iff C > C_0 = 27.63, ρ(C) ↑ ln 2 as C → ∞ (ρ(50) = .166,
  ρ(100) = .31, ρ(1000) = .57).  ln 2 is the exact cap of the iid model (W11 Prop 3.1: Pr ≥ 2^{−N}).
  Speed N, rate independent of k.  Same bound for free containment.
* The certificate is the *alternating-chain relaxation*: a 2D-increasing chain a_1<⋯<a_k with alternating
  colours is a copy of (12)^h.  Its level function λ (longest alternating chain ending at p) is monotone within
  each colour; the minimal elements of the level classes are antichains (the "generators", rigid, probability
  1/n!), and every other point is confined to a union of slab intersections whose total area over both colours
  is ≤ 1 (Lemma 1.3), hence is allowed with probability ≤ 1/2.  This mixed rigid + empty-region certificate is
  what the task asked for; the exact Pareto front (3D up-sets U_t) is too rich to encode (§2).
* **§2 (PROVED negative facts + HEURISTIC).**  Where the proof stops: (i) the relaxation itself has threshold
  C_alt ≈ 9/16 (alt-LIS ≈ (4/3)√N numerically) vs the true fixed threshold ≈ 0.25; (ii) the certificate loses
  the witness (existence) constraints and the stacking constraints — this is what moves C_0 from C_alt to 27.6;
  (iii) encoding the exact 3D Pareto-front evolution costs e^{Θ(k³)} on any grid.
* **§3 (PROVED).**  r strips, periodic word (12⋯r)^m: same certificate with cyclic colours; per-point allowed
  probability ≤ (r−1)/r, so rate ↑ ln(r/(r−1)) ≈ 1/r (matching the fixed-model cap of W23 Prop 2.4) for
  C > C_0(r) = O(r⁴).  Union over patterns: no gain (the certificate is per-pattern; entropy k^{O(N)} vs
  the e^{−N ln 2} cap is hopeless, as for all fixed-r certificates).
* **§4 (NUMERICAL).**  tg.c exact fixed-strip rates for r = 2, k = 12..40, and alt.c rates.

## 1. The alternating-chain certificate

**Definition.**  For a point p of colour c let λ(p) be the length of the longest chain q_1 < q_2 < ⋯ < q_ℓ = p
(2D dominance) with colours alternating along the chain.  Then λ(p) ≥ 1 and
   λ(p) = 1 + max{λ(q) : q < p, colour(q) ≠ colour(p)}   (max ∅ := 0).                                  (1.1)

**Lemma 1.2 (PROVED).**  (a) If an alternating chain of length k exists then (12)^h ⊂_fix (the colour model),
i.e. π is contained in the fixed-strip sense.  (b) λ is monotone within each colour: q < p, colour(q) =
colour(p) ⇒ λ(q) ≤ λ(p).
*Proof.*  (a) Along a_1<⋯<a_k the x's increase, colours alternate, and a_{t+2} > a_{t+1} > a_t gives y
increasing within each colour.  (b) In a longest chain ⋯, s, q ending at q, replace q by p: s < q < p and
colour(s) ≠ colour(p).  ∎

**Structure.**  Let A_t^c = {p : colour c, λ(p) = t}, M_t^c = the set of minimal elements of A_t^c (an antichain
for dominance = a decreasing chain in x-order), V_t^c = ∪_{t' ≥ t} ∪_{g ∈ M_{t'}^c} [x_g,1]×[y_g,1] (nested
up-sets, V_0^c := [0,1]²), and the slabs S_t^c = V_{t−1}^c \ V_t^c, t ≥ 1.  If no alternating chain of length k
exists then λ ≤ k−1 everywhere, V_k^c = ∅, and S_1^c,…,S_k^c partition [0,1]² for each c.

**Lemma 1.3 (PROVED).**  Almost surely every point p of colour c with λ(p) = t lies in
   R_t^c := S_t^{1−c} ∩ S_{t+1}^c,
and the "allowed" sets Allowed_c := ∪_{t=1}^{k−1} R_t^c satisfy |Allowed_0| + |Allowed_1| ≤ 1.
*Proof.*  p ∈ V_t^c since p is dominated by a minimal element of A_t^c.  If p ∈ V_{t+1}^c then some generator
g of level ≥ t+1 and colour c satisfies g ≤ p, a.s. g < p, so λ(p) ≥ λ(g) ≥ t+1 by Lemma 1.2(b) — contradiction;
so p ∈ S_{t+1}^c.  If p ∈ V_t^{1−c} then some g of colour 1−c and level ≥ t has g < p, so λ(p) ≥ t+1 by (1.1) —
contradiction.  If t ≥ 2, (1.1) gives q < p of colour 1−c with λ(q) = t−1, so p ∈ V_{t−1}^{1−c}; for t = 1
V_0 = [0,1]².  Hence p ∈ S_t^{1−c}.  For the area: |Allowed_0| + |Allowed_1| = Σ_t |S_t^1 ∩ S_{t+1}^0| +
Σ_t |S_t^0 ∩ S_{t+1}^1| = Σ_t |S_t^1 ∩ S_{t+1}^0| + Σ_t |S_{t+1}^1 ∩ S_t^0| ≤ Σ_{t ≠ t'} |S_t^1 ∩ S_{t'}^0| ≤ 1,
because {S_t^1} and {S_{t'}^0} are two partitions of the unit square and the index pairs (t,t+1), (t+1,t) are
disjoint families.  ∎

**Theorem 1.1 (PROVED).**  In the iid colour model with N points,
   Pr(no alternating chain of length k) ≤ 2^{−N} Σ_{m=0}^{N} C(N,m) Σ_{n ⊨ m, 2(k−1) parts} m!/Π_j (n_j!)².   (1.2)
In particular Pr((12)^h ⊄_fix) and Pr((12)^h ⊄) are bounded by (1.2).  At N = Ck² the right side is
exp(−ρ(C) N + O(k ln N)) with ρ(C) = ln 2 − sup_{0<β≤1}[H(β) + β ln(4e/(βC))].

*Proof.*  Suppose no alternating chain of length k exists.  Let M = ∪ M_t^c (the generators), m = |M|, and record
the labels (t,c) of the generators.  Then the event E(M, labels) holds:
  (i) colour(g) = c for every g ∈ M_t^c;  (ii) each M_t^c is an antichain;  (iii) every p ∉ M lies in
  Allowed_{colour(p)}(M, labels), where V, S, R, Allowed are *defined from the labelled generators* by the formulas
  above (Lemma 1.3, applied to the true generators, gives (iii); (i),(ii) hold by construction; the labels use
  only t ≤ k−1).
Union bound over the choice of M ⊂ [N] and of the labels: the number of labellings with class sizes (n_{t,c}) is
m!/Π n_{t,c}!.  For a fixed labelled M: positions of all N points and colours are independent; (ii) has
probability Π 1/n_{t,c}! (relative orders of disjoint classes are independent; an antichain of n points is a
decreasing sequence, probability 1/n!); (i) has probability 2^{−m}, independent of positions; given the
positions of M, each p ∉ M is independent, colour c w.p. 1/2, uniform in [0,1]², so it satisfies (iii) w.p.
(|Allowed_0| + |Allowed_1|)/2 ≤ 1/2 by Lemma 1.3 (the area inequality only uses that the V's are nested up-sets
with V_0 = [0,1]², V_k = ∅, which holds for any labelled generator family).  Multiplying, Pr(E) ≤
2^{−m} Π(1/n_{t,c}!) 2^{−(N−m)}, and summing gives (1.2).  Containment: Lemma 1.2(a) and ⊂_fix ⇒ ⊂.
Asymptotics: as in W23 Thm 1.1, the inner sum is ≤ (2k)^m (2ek/m)^m (m+2k)^{2k}, and C(N,m) ≤ e^{N H(m/N)};
with m = βN, N = Ck² the summand is exp(N[H(β) + β ln(4e/(βC)) − ln 2] + O(k ln N)), and there are N+1 terms.  ∎

**Corollary (numbers; PROVED by rate.py).**  ρ(C) > 0 iff C > C_0 = 27.63; at the threshold the maximising
β* solves β − ln(1−β) = ln 2 (β* = 0.315) and C_0 = 4(1−β*)/β*².  ρ(30) = .026, ρ(40) = .108, ρ(50) = .166,
ρ(100) = .313, ρ(200) = .420, ρ(1000) = .569, ρ(∞) = ln 2 = .693.  Compare W23 Thm 2.1 for r = 2: threshold
≈ 51, speed N/12.

**Remark 1.4 (Poisson model, PROVED).**  For Π_N, condition on the number of points n ~ Poisson(N); the bound
(1.2) with N replaced by n gives Pr ≤ Σ_n e^{−N}N^n/n! · B(n).  Since the exponent of B(n) is ≈ −ρ(C n/N)·n, at
N = Ck² this is exp(−N·inf_{s>0}[s ln s − s + 1 + s ρ(sC)] + o(N)), positive for C > C_0 (the Poisson cap is
1/2 instead of ln 2, obtained from the same computation as s → 1/2·…; not optimised here).

**Remark 1.5 (what is dropped; PROVED statements about the loss).**  E(M, labels) omits: (a) *witnesses*: every
generator g ∈ M_t^c, t ≥ 2, has some q < g with colour 1−c and λ(q) = t−1; (b) *stacking*: M_{t'}^c contains no
point below a point of M_t^c for t' > t (λ monotone within colour), i.e. for each colour the labels form a
strictly order-preserving map of the generator poset to [k−1]; (c) generators also lie in R_t^c.  Without (a)–(c)
the bound is exactly the Dilworth sum on the generators times 2^{−N}; the entropy C(N,m) of choosing the
generators is what costs the factor between 2e (β = 1, all points generators) and C_0 = 27.6.
