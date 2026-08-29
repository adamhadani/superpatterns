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
  C > C_0(r) ≈ 3.5 r³ (r ≤ 8; = r^{3+o(1)}).  Union over patterns: no gain (the certificate is per-pattern; entropy k^{O(N)} vs
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

## 2. The exact Pareto front, and why the certificate uses a relaxation

**2.1 Exact level structure (PROVED).**  Index letters 1..k, letter t has colour (t−1) mod 2.  Let
U_t ⊂ [0,1]³ be the set of (x, y_0, y_1) such that letters 1..t embed in the points with x' ≤ x using colour-c
points of height ≤ y_c (c = 0,1).  U_t is an up-set, U_t ⊇ U_{t+1}, and
   U_{t+1} = up-closure{ (x_p, y_p@c, y') : p of colour c = t mod 2, (x_p^−, y_p^−@c, y') ∈ U_t },
where y_p@c means the c-th height coordinate equals y_p and the other is y'.  The section U_t ∩ {x} is the 2D
up-set of W20 Prop 1.2 (its minimal elements are the Pareto front; tg.c stores it).  Absence of (12)^h ⟺
U_k = ∅ ⟺ no colour-1 point lies in the 2D up-set Q_{k−1} := {(x, y_1) : (x, 1, y_1) ∈ U_{k−1}}.
More generally a colour-c point p has λ_true(p) ≥ t+2 iff (x_p, y_p) ∈ Q_{t+1}^{1−c} := {(x,y_c) : (x, y_c, 1) ∈
U_{t+1}} — a 2D up-set whose generators are the *virtual* points (x_q, ν_t(q)), q a colour-(1−c) point of level
≥ t+1 and ν_t(q) the minimal height of the colour-c letter t in an embedding of 1..t+1 ending at q.  The
alternating relaxation replaces the virtual generator (x_q, ν_t(q)) by the real point (x_q, y_q): it is exact
iff in every optimal embedding the colour-c letter t lies below the colour-(1−c) letter t+1.

**2.2 Dead ends (PROVED).**
(a) *Grid coarse-graining of U_t.*  A monotone subset of [0,1]³ on a grid of side a/k has boundary surface
of ≈ (k/a)² cells; the number of such sets is 2^{Θ((k/a)²)}, so k nested levels cost 2^{Θ(k³/a²)} ≫ e^{N} for
a = O(1); with a = Θ(√k) the count is fine but the boundary slack is k·(k/a)²·(a/k)³ = a ≫ 1 area, i.e. all
the forbidden area is lost.  The 3D state cannot be encoded geometrically.
(b) *Grid coarse-graining of the 2D relaxation.*  2k staircases on a grid of side a/k: count ≤ C(2k/a,k/a)^{2k}
≤ e^{(4 ln 2/a)k²}; the forbidden region loses the boundary cells, ≤ 2a per colour... total rate ≥ 1/2 − 2a −
4 ln 2/(aC) (Poisson), positive only for C > 64·2 ln 2 = 89 at the optimal a.  Points as generators (Thm 1.1)
avoid the slack entirely; this is the analogue of W23 Prop 1.3 (canonical covers): the geometry must be carried
by the points.
(c) *Virtual generators for the exact structure.*  Using Q_{t+1}^{1−c} with generators (x_q, ν_t(q)) = pairs
(q, p′) of real points (p′ the colour-c letter t): the antichain condition on virtual points has probability
1/(n!)² (x-order of the q's and y-order of the p′'s are independent) but the certificate must also carry the
matching q ↦ p′ (entropy n!) and the labels of the p′ (another (2k)^n), so the count-vs-probability balance is
worse than for the relaxation: the exact certificate has C_0 larger than 27.6 along this route.  (Rigorous as a
statement about this specific union bound; a cleverer canonical choice of p′ is not excluded.)
(d) *Label-all-points certificates.*  Giving every point a level label (entropy (2k)^N) requires per-class
probabilities ≪ (2k)^{−n}; non-minimal points of a class are only region-constrained (probability ≤ 1/2 each,
tight when the two staircase families are aligned), so any certificate that labels non-generators fails for
every C.  Hence the generator/non-generator split of Thm 1.1 is forced.

**2.3 Where the loss sits (HEURISTIC, with the PROVED pieces named).**  C_alt ≈ 9/16 (§4) is the best any
argument through the relaxation can give; the certificate's C_0 = 27.6 comes from dropping Remark 1.5(a)–(b).
Keeping (b) turns the Dilworth sum on the generators of one colour into E[Ω̄(P_m, k−1)], the expected number
of strictly order-preserving maps of a random m-point dominance poset into [k−1]; this is between
Pr(LIS(P_m) < k) and the Dilworth sum, so at best it moves 4e → 4·(DZ constant), i.e. C_0 down by a factor
≤ e in the β = 1 term; the interior maximiser β* = 0.315 (generator fraction; the typical fraction of minimal
elements in contained configurations is ≈ 0.51, §4) is dominated by the C(N,m) entropy, which (b) does not
touch.  Keeping (a) (witnesses) couples the two colour families and is the real gap: with witnesses, the two
generator families of aligned staircases become one interleaved decreasing chain per level, which would remove
the 2^{m} colour-interleaving entropy and give (heuristically) 4e → 2e in the β = 1 term.

## 3. What carries over

**3.1 r strips, periodic word (12⋯r)^m, k = rm (PROVED).**  Colour model with r iid uniform colours (W20 Prop
1.1).  Relaxation: a chain a_1<⋯<a_k with colour(a_t) = (t−1) mod r; λ(p) = 1 + max{λ(q): q<p, colour(q) =
colour(p)−1 mod r}; Lemma 1.2 holds verbatim; generators M_t^c, slabs S_t^c, allowed region for colour c is
∪_t S_t^{c−1} ∩ S_{t+1}^c with |Allowed_c| ≤ 1 for each c.  Per-point allowed probability (1/r)Σ_c |Allowed_c|
≤ (r−1)/r: one colour must lose, because S_{t+1}^c ≈ S_t^{c−1} for all c cyclically would force S_{t+1}^c ≈
S_{t+1−r}^c, contradicting the partition; the value r−1 is attained (colours 0..r−2 shift-aligned, colour r−1
offset).  Hence
   Pr((12⋯r)^m ⊄_fix) ≤ Σ_m C(N,m) r^{−m} ((r−1)/r)^{N−m} Σ_{n ⊨ m, r(k−1) parts} m!/Π(n_j!)²,
   ρ_r(C) = ln(r/(r−1)) − sup_β [ H(β) + β ln(r/(r−1)) + β ln(r e/(βC)) ]   (r(k−1) classes: (rk)^m (rek/m)^m
   = (r²e/(βC))^m, and r^{−m} cancels one factor r),
positive for C > C_0(r), where (rate_r.py) C_0(2) = 27.6, C_0(3) = 98.5, C_0(4) = 239, C_0(6) = 827, C_0(8) = 1983
(≈ 3.5 r³ numerically; analytically C_0(r) = r^{3+o(1)}: β ≍ 1/r is forced by the cap 1/r, and the entropy term
β ln(r e/(βC)) ≤ β·cap needs C ≳ r²e/β·e^{−O(1)} ≍ r³), and ρ_r ↑ ln(r/(r−1)) ≈ 1/r, the fixed-model cap (W23 Prop 2.4, W11 Prop 3.1).  Compared
with W23 Thm 2.1 (threshold 9r ln(3er), speed N/(3r²)) the threshold is worse in r but the speed is optimal.
Blocky words (1^ℓ⋯r^ℓ)^m: same proof with "colour successor" = the word's transition relation; the loss factor
is (number of admissible predecessor colours)/r, so blocks (same colour may follow itself) lose the antichain
rigidity within blocks and the method degrades to Dilworth-within-blocks.

**3.2 Free model (PROVED, trivial).**  ⊂_fix ⇒ ⊂, so Thm 1.1 bounds Pr((12)^h ⊄ N iid points) too; no union
over strip boundaries is needed (contrast W23 §3), because the certificate lives in the colour model.

**3.3 Union bound over patterns (PROVED negative).**  The rate never exceeds the cap ln 2 (iid) / 1/2 (Poisson)
in the fixed model, and the certificate only exists for fixed-r words; it says nothing about patterns with
r = Θ(k) colours, which dominate the union over S_k.  Nothing new for Alon's union bound.

**3.4 Warm-up: the identity as the word 0^h 1^h (PROVED sketch).**  The analogous relaxation is a 2D chain with
colour pattern 0^h1^h; λ(p) = LIS within colour 0 for colour-0 points, and h + LIS within colour 1 restricted
to V_h^0 for colour-1 points above a colour-0 chain of length h.  All level classes are antichains (no
cross-colour comparable pairs inside a class), every constrained point is a generator, and the certificate is
the Dilworth sum with 2(k−1) antichains: the mechanism of Thm 1.1 reduces to W23 Thm 1.1 (rate ln(C/(2e))-type)
exactly when no colour interleaving is required.  The interleaving of (12)^h is what creates the region-
constrained (non-rigid) points and the 2^{−N} cap.

## 4. Numerics (NUMERICAL)

**4.1 Exact value of the certificate sum (1.2)** (exact_bound.c, out/exact_bound.txt), −ln B/N and the
maximising generator fraction β*:

    C:      8      10     12     15     20     30     60
    k=10  −.336  −.247  −.179  −.101  −.009   .106   .265
    k=14  −.379  −.286  −.214  −.132  −.036   .084   .249
    k=20  −.413  −.316  −.241  −.156  −.057   .067   .237
    k=30    —      —    −.263  −.176  −.073   .054    —
    k=40    —      —      —    −.186  −.082    —      —
    ρ(C)  −.56   −.44   −.35   −.25   −.109   .026   .215  (asymptotic, rate.py)
    β*    .46    .43    .40    .37    .33     .28    .21   (k=10; → β*(∞) = .315 at C_0)

The finite-k threshold is C ≈ 20 (k=10), 22 (k=20), 24 (k=40), increasing towards C_0 = 27.6: the O(k ln N)
polynomial factors help at finite k.  At k = 20, C = 30 the bound is a certified Pr ≤ e^{−0.067·12000} = e^{−806}.

**4.2 Exact fixed-strip absence rates for the true pattern** (tg.c, r = 2, out/tg_r2.txt; 2·10⁵ reps, seed 7):
k = 12: −ln P/N = .0116 (C=.4), .027 (.5), .047 (.6), .071 (.7), .092 (.8, 5 hits); C ≥ 1: 0 hits (rate > .04).
k = 32, 10⁶ reps: C = .5 gives P = 2·10⁻⁶, rate .0256 (k = 12: .027; W23 k = 24: .0255) — k-stable, speed N confirmed;
C = .6: 0/10⁶.  As in W23 §4 the rate is k-stable; the truth at
C = 27.6 is unmeasurable (P ~ e^{−0.5N}) — the bound is checked only against the cap ln 2 and the sign.

**4.3 The relaxation itself** (alt.c, out/alt_rates.txt): alt-LIS ≈ 1.33√N (k=64, C=.6: 65.2 at N=2458), so
C_alt ≈ 9/16 ≈ 0.56 (HEURISTIC: 4/3 exactly?).  Rates −ln P/N at C = 0.8: .0105 (k=16), .0077 (24), .0064 (32)
— decreasing in k like the identity (W23 §4(i)), not k-stable like the true r = 2 rate.  Fraction of generators
(minimal elements of level classes) in typical (containing) configurations: .51–.55, decreasing towards 1/2.
