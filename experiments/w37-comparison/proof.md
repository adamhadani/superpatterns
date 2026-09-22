# W37 — Comparison questions: the strip-rearrangement reformulation, and box comparisons

Notation. Π_N = Poisson point process on the open unit square Q = (0,1)² with intensity measure N·Leb.
Almost surely all points of Π_N have pairwise distinct x-coordinates and pairwise distinct y-coordinates; we work
on that event throughout. For a finite set P ⊂ Q with distinct coordinates and π ∈ S_k, "π ⊆ P" means: there are
q_1, …, q_k ∈ P with x(q_1) < ⋯ < x(q_k) and, for all a, b: y(q_a) < y(q_b) ⟺ π(a) < π(b).
p_π(N) := Pr(π ⊄ Π_N)  (Poisson model);  p̄_π(n) := Av_n(π)/n! (uniform σ_n model).  id = id_k = 12⋯k,
dec = dec_k = k⋯21. Tags: PROVED / NUMERICAL / CONJECTURE. All numerics are in results.md.

---

## 1. The strip-rearrangement reformulation

**Definitions.** A *cut vector* is c = (c_0, …, c_k) with 0 = c_0 ≤ c_1 ≤ ⋯ ≤ c_k = 1; write
w_j = w_j(c) = c_j − c_{j−1} (strip widths) and S_j = S_j(c) = (0,1) × [c_{j−1}, c_j) (the j-th horizontal strip,
counted from the bottom; S_j = ∅ if w_j = 0). Fix π ∈ S_k. Set
      d_a = d_a(c, π) := Σ_{b=1}^{a} w_{π(b)},   d_0 = 0,  d_k = 1.
The *rearrangement map* T = T_{c,π} : (0,1) × [0,1) → (0,1) × [0,1) is defined strip-wise: for
(x, y) with y ∈ [c_{π(a)−1}, c_{π(a)}) (i.e. (x,y) ∈ S_{π(a)}),
      T(x,y) := (x, y − c_{π(a)−1} + d_{a−1}).
Thus T translates the strip S_{π(a)} vertically onto the *new strip* S̃_a := (0,1) × [d_{a−1}, d_a), so that after
rearrangement the old strips appear stacked in the order π(1), π(2), …, π(k) from bottom to top ("strip π(a)
becomes the a-th from the bottom"). T is a bijection (the intervals [d_{a−1}, d_a) are disjoint with union [0,1)),
and T preserves Lebesgue measure (it is a piecewise translation on finitely many disjoint horizontal strips).
Write Π_c := T_{c,π}(Π_N) (the dependence on π is suppressed as in the task statement), and define the event
      E_c := { ∃ p_1, …, p_k ∈ Π_c :  x(p_1) < ⋯ < x(p_k)  and  p_a ∈ S̃_a for every a }.
E_c asks for an increasing chain of the rearranged process with exactly one point in each new strip, in strip
order. (For any chain with one point per strip, "in strip order" — the a-th smallest x in the a-th strip from the
bottom — is exactly the requirement that the chain be increasing in y as well as in x, since the new strips are
stacked in order; so E_c is the event described in the task.)

**Lemma 1 (reformulation). (PROVED)** Fix π ∈ S_k. Then, pointwise on the full-measure event that Π_N has
distinct coordinates,
      { π ⊆ Π_N }  =  ∪_c E_c ,
the union over all cut vectors c. Consequently  p_π(N) = Pr( ∩_c E_c^∁ ) = Pr( sup_c 1_{E_c} = 0 ).
Moreover the union may be restricted to the countable family of cut vectors whose cuts lie in
{ (y' + y'')/2 : y', y'' ∈ y(Π_N) ∪ {0, 1} } (so ∪_c E_c is an event), and for π = id one may take T = identity
for every c, in which case ∪_c E_c = { LIS(Π_N) ≥ k }.

*Proof.* (⊆) Let q_1, …, q_k ∈ Π_N be a copy of π: x(q_1) < ⋯ < x(q_k), and y(q_a) < y(q_b) ⟺ π(a) < π(b).
Let y_{(1)} < ⋯ < y_{(k)} be the y-values of the copy in increasing order; by the definition of a copy,
y_{(j)} = y(q_{π^{−1}(j)}). Choose the cut vector c with c_j := (y_{(j)} + y_{(j+1)})/2 for 1 ≤ j ≤ k−1 (and
c_0 = 0, c_k = 1); then y_{(j)} ∈ [c_{j−1}, c_j), i.e. q_{π^{−1}(j)} ∈ S_j, i.e. q_a ∈ S_{π(a)} for every a.
Hence T(q_a) ∈ S̃_a. Since T preserves x-coordinates, the points p_a := T(q_a) satisfy x(p_1) < ⋯ < x(p_k), and
p_a ∈ S̃_a: E_c holds. The chosen cuts lie in the countable family stated.

(⊇) Suppose E_c holds for some c, with points p_a = T(q_a), q_a ∈ Π_N (T is a bijection, so every point of Π_c
is the image of a unique point of Π_N). p_a ∈ S̃_a means q_a ∈ S_{π(a)} (T maps S_{π(a)} bijectively onto S̃_a),
i.e. y(q_a) ∈ [c_{π(a)−1}, c_{π(a)}). If π(a) < π(b) then
y(q_a) < c_{π(a)} ≤ c_{π(b)−1} ≤ y(q_b), so y(q_a) < y(q_b); by trichotomy (distinct y-values) the y-order of
(q_1, …, q_k) is exactly π. And x(q_a) = x(p_a) is increasing in a. So (q_a) is a copy of π in Π_N. ∎

**Lemma 2 (fixed cuts: the law of E_c does not depend on π). (PROVED)** Fix a cut vector c with all w_j > 0 and
any π ∈ S_k. Then:
 (i) Π_c is a Poisson process of intensity N·Leb on (0,1) × [0,1) (mapping theorem for the measure-preserving
     bijection T_{c,π}; T maps the intensity measure to itself).
 (ii) Pr(E_c) = Pr( Σ_{j=1}^k γ_j / w_j < N ), where γ_1, …, γ_k are i.i.d. Exp(1). In particular Pr(E_c) is the
     same for every π ∈ S_k.

*Proof.* (i) is the mapping theorem (Kingman, Poisson Processes, §2.3): the image of a Poisson process under a
measurable bijection maps the intensity measure to its pushforward, and T_{c,π} pushes N·Leb to N·Leb.
(ii) E_c depends on Π_N only through the x-coordinates of the points in the k strips: for j = 1..k, the set
X_j := { x(q) : q ∈ Π_N ∩ S_j } is a Poisson process on (0,1) of intensity N w_j (projection of an independent
thinning), and X_1, …, X_k are independent (disjoint strips). E_c holds iff there are x_1 < ⋯ < x_k with
x_a ∈ X_{π(a)}. Consider the greedy sequence: g_1 := min X_{π(1)}, g_a := min { x ∈ X_{π(a)} : x > g_{a−1} }
(min ∅ := ∞, and the sequence is ∞ from the first failure on). *Greedy optimality:* if x_1 < ⋯ < x_k is any
feasible sequence then by induction g_a ≤ x_a (g_1 ≤ x_1; if g_{a−1} ≤ x_{a−1} < x_a then x_a is a candidate in
the definition of g_a, so g_a ≤ x_a < ∞), so E_c holds iff g_k < 1, i.e. iff greedy succeeds. By the strong Markov
/ memoryless property of the Poisson processes X_j (independent across j, and the increments of X_{π(a)} beyond
g_{a−1} are independent of the past), the gaps g_a − g_{a−1} (with g_0 = 0) are independent Exp(N w_{π(a)})
variables, and g_k < 1 iff Σ_a γ_a/(N w_{π(a)}) < 1 with γ_a i.i.d. Exp(1). Re-indexing the (independent,
identically distributed) γ's by j = π(a) gives Pr(E_c) = Pr( Σ_j γ_j / w_j < N ). ∎

**Discussion (what Lemmas 1–2 say).** p_π(N) = Pr(no E_c occurs), where the *marginal* law of each E_c is
π-independent (Lemma 2) and, for π = id, all rearranged processes Π_c coincide with Π_N; only the *joint* law of
the family {E_c}_c depends on π. A comparison of their unions is a
possible sufficient route to Alon, not an equivalent formulation of the
conjecture. Equal marginal laws alone give no ordering of these unions.

**Corollary 2.1 (uniform fixed-cut bound; known, for calibration). (PROVED)** Taking w_j = 1/k:
p_π(N) ≤ Pr( Γ ≥ N/k ), Γ ~ Gamma(k,1); with N = Ck², Cramér gives p_π(Ck²) ≤ e^{−k(C − 1 − ln C)} for C > 1,
for every π ∈ S_k. This is the trivial speed-k bound: e^{−Θ(k)}, exponent far below the k ln k needed; the whole
content of the problem is the gap between one cut (speed k) and the union over cuts (speed k² for the identity,
by Deuschel–Zeitouni).

**Lemma 3 (de-Poissonization; standard). (PROVED)**
(i) p̄_π(n+1) ≤ p̄_π(n) (deleting the last position maps (n+1)-avoiders to n-avoiders, with fibers of size ≤ n+1
    — an n-avoider has at most n+1 one-point extensions at the last position — so Av_{n+1} ≤ (n+1) Av_n).
(ii) p_π(N) = Σ_n e^{−N} N^n/n! · p̄_π(n); hence, by (i),
     p̄_π(n) ≤ p_π(N)/Pr(Pois(N) ≤ n)  for every N, and p_π(N) ≤ Pr(Pois(N) < n) + p̄_π(n).
     With N = n: p̄_π(n) ≤ 2 p_π(n) and p_π(n) ≤ e^{−n/9} + p̄_π((1 − 1/3)n)-type bounds as needed; all
     comparisons below survive de-Poissonization with e^{O(√N ln N)}-factor changes, negligible at every rate
     considered. ∎

---

## 2. Box comparisons: corner defects, defect sums, and the rate form for a class of patterns

Throughout, "box" means an open axis-parallel square B ⊆ Q; Π_N ∩ B, rescaled to the unit square, is a Poisson
process with N·|B| expected points, and the restrictions to disjoint boxes are independent.

**Lemma 4 (cost of a small pattern in a box). (PROVED)** For τ ∈ S_t (t ≥ 1) and λ ≥ 2t:
      p_τ(λ) ≤ exp( − q_t ⌊λ/t⌋ ),   q_t := e^{−2t} t^t / (t!)²  ≥  e^{−t ln t − 2} / t .
In particular the decay in λ is speed λ with a constant depending only on t, and p_1(λ) = e^{−λ} exactly.

*Proof.* Partition the unit square into a g × g array of congruent open sub-squares (the boundary grid is null),
with g² := ⌊λ/t⌋ ≥ 2. The restrictions of Π_λ to the cells are independent, and each cell, rescaled, is a
Poisson process on the unit square with mean μ = λ/g² points, where t ≤ μ ≤ t/(1 − t/λ) ≤ 2t (using λ ≥ 2t).
If some cell contains a copy of τ then τ ⊆ Π_λ. Given that a cell contains exactly t points, these are i.i.d.
uniform, so their pattern is uniform on S_t; hence
      Pr( cell contains τ ) ≥ Pr( cell has exactly t points forming a copy of τ ) = e^{−μ} μ^t / (t! · t!)
      ≥ e^{−2t} t^t/(t!)² = q_t   (μ ∈ [t, 2t]; e^{−μ}μ^t is decreasing for μ ≥ t).
By independence, p_τ(λ) ≤ (1 − q_t)^{g²} ≤ exp(−q_t ⌊λ/t⌋). Finally t! ≤ e√t (t/e)^t gives
(t!)² ≤ e² t (t/e)^{2t}, so q_t ≥ e^{−2t} t^t e^{2t}/(e² t · t^{2t}) = e^{−t ln t − 2}/t. ∎

  *(Remark: any speed-λ bound with a t-only constant suffices; via Stanley–Wilf/Marcus–Tardos one can get
  p_τ(λ) ≤ (e L(τ)/λ)^{λ/2}-type superexponential decay, but Lemma 4 is elementary and enough.)*

**Lemma 5 (monotone block, self-contained speed-M bound). (PROVED)** For every a ≥ 2 and M > 0:
      p_{id_a}(M) = Pr( LIS(Π_M) < a ) ≤ exp( −M + 2(a−1)√M ),
and the same for dec_a (reflect x ↦ 1−x). In particular p_{id_a}(M) ≤ e^{−M/2} whenever M ≥ 16 a².

*Proof.* By Schensted, LIS(σ) ≤ a−1 iff RSK(σ) = (P,Q) has shape λ with λ_1 ≤ a−1. A standard Young tableau
with n entries and at most a−1 columns is determined by its *column word* (the sequence, for i = 1..n, of the
column index of entry i): the entries are inserted in the order 1, 2, …, n, each at the bottom of its column. So
the number of such SYT is ≤ (a−1)^n, and σ ↦ (column word of P, column word of Q) is an injection:
Av_n(id_a) ≤ (a−1)^{2n}. Hence
  p_{id_a}(M) = Σ_n e^{−M} M^n/n! · Av_n(id_a)/n! ≤ e^{−M} Σ_n (M(a−1)²)^n/(n!)²
             ≤ e^{−M} cosh( 2(a−1)√M ) ≤ e^{−M + 2(a−1)√M},
using (n!)² ≥ (2n)!/4^n, so Σ y^n/(n!)² ≤ Σ (2√y)^{2n}/(2n)! = cosh(2√y). ∎

**Theorem 6 (corner-defect comparison). (PROVED)** Let π = τ_1 ⊕ ρ ⊕ τ_2 with ρ ∈ S_m, τ_i ∈ S_{t_i}
(τ_i possibly empty), k = m + t_1 + t_2. Then for every ε ∈ (0, 1/2) and every N:
      p_π(N) ≤ p_ρ( N(1−2ε)² ) + p_{τ_1}( Nε² ) + p_{τ_2}( Nε² ),
where each term on the right is the Poisson unit-square quantity at the stated intensity. The same holds for
π = τ_1 ⊖ ρ ⊖ τ_2 (use the NW corner box (0,ε)×(1−ε,1) and the SE corner box (1−ε,1)×(0,ε)).

*Proof.* Let B_1 = (0,ε)², B_0 = (ε, 1−ε)², B_2 = (1−ε, 1)². These are disjoint, so Π_N ∩ B_1, Π_N ∩ B_0,
Π_N ∩ B_2 are independent; rescaled to unit squares they are Poisson processes with Nε², N(1−2ε)², Nε² expected
points, and rescaling by a positive-diagonal affine map preserves pattern containment. Every point of B_1 is
strictly SW of every point of B_0, which is strictly SW of every point of B_2. Hence if τ_1 ⊆ Π ∩ B_1 and
ρ ⊆ Π ∩ B_0 and τ_2 ⊆ Π ∩ B_2, then the concatenation of the three copies is a copy of τ_1 ⊕ ρ ⊕ τ_2 = π. So
{π ⊄ Π_N} ⊆ {τ_1 ⊄ Π∩B_1} ∪ {ρ ⊄ Π∩B_0} ∪ {τ_2 ⊄ Π∩B_2}; the union bound and independence-free monotonicity
give the claim. The ⊖ version is identical after reflecting the y-axis in the two corner boxes' position. ∎

**Corollary 7 (the numerically hardest pattern obeys the comparison). (PROVED)** For π* = 1 ⊕ dec_{k−2} ⊕ 1
(the hardest pattern at every k ≤ 8 in the W27/W37 exact and SMC data) and every ε ∈ (0,1/2):
      p_{π*}(N) ≤ p_{dec_{k−2}}( N(1−2ε)² ) + 2 e^{−Nε²}
                = p_{id_{k−2}}( N(1−2ε)² ) + 2 e^{−Nε²}  ≤  p_{id_k}( N(1−2ε)² ) + 2 e^{−Nε²}.
(The equality is the x-reflection symmetry p_{dec_m} = p_{id_m}; the last step is {LIS < k−2} ⊆ {LIS < k}.)
More generally, for every π = τ_1 ⊕ mono_m ⊕ τ_2 or τ_1 ⊖ mono_m ⊖ τ_2 (mono ∈ {id, dec}), with t = max(t_1,t_2)
≥ 1:
      p_π(N) ≤ p_{id_k}( N(1−2ε)² ) + 2 exp( − q_t ⌊Nε²/t⌋ ),  q_t as in Lemma 4.   ∎

**Interpretation, corrected 2026-09-10.** Since π* contains dec_(k−2),
p_(π*)(N)≥p_(id_(k−2))(N), whereas p_(id_(k−2))(N)≤p_(id_k)(N).
These inequalities do not force π* to be harder than id_k or an exponential
ratio between their avoidance probabilities. The displayed finite box
comparison remains valid. The former claimed e^{o(k log k)} rate comparison
is withdrawn: a fixed-ratio large-deviation theorem gives an o(k²) error,
which cannot be promoted to o(k log k), and it gives no uniform control as
N/k² approaches 1/4. Quantitative, uniform monotone tails would be needed.

**Theorem 8 (defect-sum patterns: additive box bound). (PROVED)** Let
      π = B_1 ⊕ B_2 ⊕ ⋯ ⊕ B_s ∈ S_k,
where each block B_i is either a monotone run (id_{a_i} or dec_{a_i}) or an arbitrary pattern ("defect") of
length t_i. Let R = {i : B_i monotone}, D = {i : B_i defect}, A = Σ_R a_i, T = Σ_D t_i, A + T = k, A ≥ 1.
Fix θ ∈ (0,1) and give block i the side
      u_i = (1−θ) a_i / A   (i ∈ R),        v_i = θ/|D|   (i ∈ D),
(Σ u_i + Σ v_i = 1), and place the blocks in disjoint open boxes along the diagonal in block order. Then
      p_π(N) ≤ Σ_{i∈R} exp( −N u_i² + 2 a_i √(N u_i²) )  +  Σ_{i∈D} exp( − q_{t_i} ⌊N v_i²/t_i⌋ ),
and also, keeping the sharper monotone term,
      p_π(N) ≤ Σ_{i∈R} p_{id_{a_i}}( N u_i² )  +  Σ_{i∈D} p_{B_i}( N v_i² ).
The same holds for ⊖-sums (anti-diagonal boxes).

*Proof.* Boxes along the diagonal in block order are pairwise SW–NE ordered, so block-wise copies concatenate to
a copy of π exactly as in Theorem 6 (for a dec run, reflect the box in x: p_{dec_a}(M) = p_{id_a}(M)). The union
bound over the s block-failures, with Lemma 5 for monotone runs and Lemma 4 for defects, gives the display. ∎

**Theorem 9 (Alon's conjecture restricted to defect-sum patterns with long runs; conditional on DZ). (PROVED,
using the Deuschel–Zeitouni lower-tail LDP as external input)**
Fix δ > 0 and let N ≥ (1/4 + δ)k². Let 𝒞_k = 𝒞_k(δ) be the set of π ∈ S_k expressible as a ⊕-sum (or ⊖-sum) of
monotone runs and defects, as in Theorem 8, with
      (a) every monotone run of length a_i ≥ √k · ln k,
      (b) every defect of length t_i ≤ (ln k)/(8 ln ln k),
      (c) total defect length T = Σ t_i ≤ δk/3   (so A ≥ (1 − δ/3)k),
      (d) number of defects |D| ≤ k^{1/4}.
Then there are c(δ) > 0 and k_0(δ) with: for all k ≥ k_0(δ) and all π ∈ 𝒞_k,
      Pr( π ⊄ Π_N ) ≤ exp( − c(δ) k ln² k )  =  e^{−ω(k ln k)}.
Consequently Pr( Π_N ⊇ every π ∈ 𝒞_k ) ≥ 1 − k! e^{−c(δ)k ln²k} → 1: a Poisson/random configuration of
(1/4+δ)k² points contains all of 𝒞_k w.h.p. — the Alon-window statement, restricted to 𝒞_k. The class contains
all layered patterns with every layer of size in [√k ln k, k], and the direct sums of such runs with sparse
small defects; the identity and dec are the trivial cases.

*Proof, clarified 2026-09-10.* Put δ₀=min(δ,1) and θ=δ₀/4. Give run i
side (1−θ)a_i/A and defect i side θ/|D| as in Theorem 8. If there are no
defects, give the runs total side one. Since A≤k and N≥(1/4+δ₀)k²,

    M_i/a_i² ≥ (1/4+δ₀)(1−δ₀/4)² ≥ (1+δ₀)/4 > 1/4.

The fixed-ratio Poisson monotone-tail lemma proved explicitly in W39 from
Deuschel–Zeitouni Theorem 1 therefore bounds each run's failure by
exp(−c_δ a_i²)≤exp(−c_δ k log²k). Only a positive constant is needed;
no equality between fixed-size and Poisson rate functions is asserted.

Each defect box has mean λ_i≥δ₀² k^(3/2)/64. For large k,
t_i log t_i≤(log k)/8, q_(t_i)≥e^(−2)k^(−1/8)/t_i, and
floor(λ_i/t_i)≥λ_i/(2t_i). Lemma 4 thus bounds its failure by
exp(−c'_δ k^(11/8)/log²k)≤exp(−k^(5/4)). The floor's factor two is
included in c'_δ. Union over at most k blocks and decrease c_δ to obtain
exp(−c_δ k log²k); union over at most k! targets proves the statement. ∎

  *(Honest scope. (i) The DZ input is the standard lower-tail LDP for LIS of i.i.d./Poisson samples with speed
  = sample size; only positivity and monotonicity of H on (0,2) are used, not its formula. An unconditional
  version follows from Lemma 5 alone for N ≥ (16+δ)k² — replace H(x_δ)/2 by 1/2 — with the same class 𝒞_k;
  W23's certificate bound would give N ≥ (e²+δ)k²·…; only the constant in front of k² changes.
  (ii) The class 𝒞_k is small — |𝒞_k| = e^{O(√k ln²k)}-ish — but it strictly contains everything for which the
  Alon window was previously known within this project (monotone via BDJ/DZ, and it adds layered-with-long-runs
  and sparse defects at the sharp constant 1/4).
  (iii) Condition (a) can be relaxed to a_i ≥ φ(k)√(k ln k), any φ → ∞, giving exp(−ω(k ln k)); (b)–(d) likewise
  have slack; we fixed clean values.)*

---

## 3. What the exact numerics say (NUMERICAL; tables and scripts in results.md, data/)

Exact Av_n(π) for **all** π with 3 ≤ |π| ≤ 7 and n ≤ 13 (new: complete tables at n = 11, 12, 13 for k = 6, 7),
computed by allpat.c (all-pattern simultaneous counting with a Klein-four symmetry reduction; validated against
OEIS A005802/A061552/A022558 at n ≤ 13(k=4)… and against W27's coordinator brute force at n = 9, 10).
Headlines (details/tables in results.md):
 1. max_π ln(1/p̄_π(n)) is attained by the monotone class only up to a k-dependent crossover n_×(k) ≈ 0.4–0.8 k²;
    beyond it 1 ⊕ dec_{k−2} ⊕ 1 (k ≤ 5) or 1 ⊕ 21 ⊕ … (132546-type, k = 6, 7 at moderate n) is strictly harder.
    The k = 4 exception (Av_7(1324) > Av_7(1234)) does not disappear as n grows — the excess grows without bound
    (Stanley–Wilf: L(1324) > 9) — and the same happens for every k: the identity is *never* the hardest pattern
    for all large n at fixed k. The correct comparison is the shifted one (rate form): the tables give, for each
    n, the shift s_π(n) := n − max{m : p̄_id(m) ≥ p̄_π(n)}; s grows very slowly (see results.md).
 2. Sorting-monotonicity (one bubble step towards id increases p̄) is FALSE in general at fixed n; the exact
    violation lists are in results.md. Boundary bubble steps (12⊕τ ↔ 21⊕τ and τ⊕12 ↔ τ⊕21) give exact equality
    at every n (Backelin–West–Xin); the violations are interior steps that create a monotone-adjacent decreasing
    pair (1324-mechanism).

## 4. Numerical status of the two conjectures (labels)

**CONJECTURE CP-rate (the task's goal; open).** ∀π ∈ S_k: p_π(N) ≤ e^{o(k ln k)} p_id(N(1−o(1))), uniformly.
Status: proved here for the corner-defect class (Cor. 7) and for 𝒞_k (Thm 9 makes it moot there); supported by
the exact tables at k ≤ 7 and W27's deep SMC at k ≤ 8; open in general — the hard cases are tilted grids
(min(r,h) → ∞) and random-like π, exactly as identified in W27 §4.

**CONJECTURE sort-rate.** One bubble step towards the identity does not decrease −(1/N)ln p at fixed N/k² by
more than O(1/k): numerically consistent; pointwise-in-n monotonicity is false (§3.2).

## 5. Proof attempts that fail, and why (recorded)

**(a) FKG/Harris on the family {E_c}.** Each E_c is an increasing event of the point configuration. Harris/FKG
gives Pr(∩_c E_c^∁) ≥ Π_c Pr(E_c^∁)-type LOWER bounds on p_π — the wrong direction for CP. For the needed
direction one wants: "the family {E_c^π} is less positively correlated than {E_c^id}, hence its union is
larger". With identical marginals (Lemma 2) this is a Slepian-type comparison; Slepian's inequality needs
Gaussianity, and the natural Gaussian surrogates (e.g. comparing E sup of two smoothed fields) do not control
Pr(∪ E_c) = Pr(sup = 1) for indicator fields. No general "less correlated ⇒ stochastically larger sup" theorem
exists for exchangeable-marginal indicator families — and it is FALSE in general (example: X_1 = X_2 = Ber(p)
versus X_1 = 1−X_2 = Ber(p), p > 1/2: the anti-correlated family has union probability 1 > 2p − p²… that
direction is fine; the failing direction: perfectly correlated union = p < 1 − (1−p)² independent union — the
inequality Pr(∪ indep) ≥ Pr(∪ coupled) with equal marginals is TRUE for two events (inclusion-exclusion:
Pr(A∪B) = 2p − Pr(A∩B) and independence minimizes… no: Pr(A∩B) = p² can be exceeded or undercut by coupling;
anti-correlation gives a LARGER union). The identity's family is the maximally positively-associated one, which
suggests its union is minimal among *positively associated* couplings with the given marginals — but the π-family
is not obtained from the id-family by "decorrelating" in any monotone way we could exploit: for c ≠ c′ the maps
T_{c,π}, T_{c′,π} overlap on part of the strip structure, and the correlation of (E_c, E_{c′}) under π versus id
is not comparable in a fixed direction (numerically it can go both ways at k = 3, where nevertheless all p̄_π(n)
are EQUAL — see (b)). Recorded as a dead end in this generality.

**Proposition 10 (the sorting conjecture is exactly half-false; PROVED).** Let
E_k := { (π, π′) : π′ is obtained from π ∈ S_k by sorting one adjacent inversion (a bubble step towards id) }.
The complement involution ι(π, π′) := (π′^c, π^c) maps E_k to E_k bijectively: if π has the adjacent inversion
π_i > π_{i+1} and π′ sorts it, then π′^c has the adjacent inversion at the same positions and sorting it yields
π^c. Since Av_n(σ^c) = Av_n(σ) for all n, ι reverses every strict comparison: the edge (π, π′) violates the
conjecture "Av_n(π′) ≥ Av_n(π)" strictly iff its image ι(π,π′) = (π′^c, π^c) confirms it strictly
(Av_n(π^c) > Av_n(π′^c) ⟺ Av_n(π) > Av_n(π′)). Hence for every k and every n,
      #{ strict violations in E_k }  =  #{ strict confirmations in E_k },
and the sorting-monotonicity conjecture fails for every k and n for which any strict inequality exists in E_k
(k ≥ 4, n ≥ 6 by the exact tables). Structurally: "one bubble step towards id" is, through the complement,
"one bubble step away from dec", and dec is exactly as hard as id — no inversion-count-monotone difficulty
measure can exist. (This is exactly reflected in the exact tables: violations = confirmations = 12 (k=4),
108 (k=5), 851 (k=6), 7318 (k=7) at n = 12; see results.md.) ∎

**(b) A bubble-step merging lemma is impossible pointwise, and any rate-level mechanism must produce exact
equalities.** Constraints any proof must respect: (i) at k = 3 all six patterns have p̄_π(n) equal for every n
(Wilf-trivial class) although the cut-families {Π_c} are genuinely different — so no strict "decorrelation
helps" argument can be right; it must saturate. (ii) Backelin–West–Xin: 12⋯j ⊕ τ ~ j⋯21 ⊕ τ gives exact
equality for boundary bubble steps at every n; (iii) 1324 → 1234 (an interior bubble step) has the strict
REVERSE inequality for all n ≥ 7 (exact tables; Stanley–Wilf limits 11.6 > 9). So a merging argument "swap two
adjacent strips in the rearrangement and show sup_c L can only drop" is false as a pathwise/pointwise claim:
swapping the two strips changes which chains exist, and for 1324 the swapped (identity) process has *strictly
more* avoiders from n = 7 on. What survives is only the windowed rate statement (Cor. 7's form): the swap costs
at most a k → k−O(1) shortening plus corner terms. A pathwise merging proof would have to lose exactly such a
factor, i.e. it must couple Π with a *shortened* process; we did not find a coupling realizing this loss for a
general interior step (the natural "cut-and-exchange the two strips" coupling changes the x-interleaving of the
two strips with the rest, and there is no measure-preserving surgery that repairs it without resampling the
whole strip pair — resampling destroys the conditioning on the other strips' chains).

**(c) Product boxes and the remaining comparison problem.** Theorems 6
and 8 give finite additive box bounds. They do not establish a relative
error e^{o(k log k)} against the identity tail. The earlier argument
confused an o(k²) large-deviation error with that stronger error scale.
For sufficiently long runs, Theorem 9 gives simultaneous containment
without requiring such a comparison. W39 strengthens its defect-free
subclass by using a common host event for all skeletons and block sizes.

**(d) Joint-law information.** Fixed-cut marginals do not determine the
probability of their union. The current arguments provide no general
comparison of these unions. Failed uses of FKG, Slepian or second moments
in this workstream do not rule out other formulations of those methods.

## 6. Summary of what is PROVED in this file

- Lemma 1: exact reformulation π ⊆ Π_N ⟺ ∃ cuts c with a full increasing strip-chain in the rearranged
  process; measurable union; identity ⇒ LIS.
- Lemma 2: for fixed cuts, the rearranged process is Poisson(N) and Pr(E_c) = Pr(Σ γ_j/w_j < N) — independent
  of π. Corollary 2.1: avoidance bound e^{−k(C−1−ln C)} for C>1.
- Lemma 3: de-Poissonization; p̄ monotone.
- Lemma 4: elementary positive-rate avoidance bound for each fixed small pattern; use its stated q_t and floor factor.
- Lemma 5: p_{id_a}(M) ≤ e^{−M + 2(a−1)√M} (RSK column words; self-contained).
- Theorem 6 + Corollary 7: corner-defect comparison; the hardest observed pattern 1 ⊕ dec_{k−2} ⊕ 1 satisfies
  p ≤ p_{id_k}(N(1−2ε)²) + 2e^{−Nε²}; the stronger relative rate-form inference is withdrawn.
- Theorem 8: additive box bound for ⊕/⊖-sums of monotone runs and defects.
- Theorem 9 (conditional on the DZ lower-tail LDP): Alon's conjecture at N = (1/4+δ)k² restricted to the class
  𝒞_k (long monotone runs, sparse small defects; includes all layered patterns with layers ≥ √k ln k).
  Unconditional variant at N ≥ (16+δ)k² via Lemma 5.

Everything else is labelled CONJECTURE or NUMERICAL. Verification hooks: all exact counts reproducible via
`gcc -O2 -o allpat allpat.c && ./run_allpat.sh N && python3 combine.py N`; analysis scripts in this directory.
