# W38 — pattern-averaged second moment on copies; canonical (Achlioptas–Peres-style) fix

Setting: σ uniform on S_N, N = ⌈Ck²⌉. For a k-subset A ⊂ [N] of positions, pat(A) ∈ S_k is the
standardisation of σ|_A. M_π = #{A : pat(A) = π}; Σ_π M_π = C(N,k); μ := E M_π = C(N,k)/k! for every π
(symmetry). J = |A∩B| for two independent uniform k-subsets A, B; P(J=j) = C(k,j)C(N−k,k−j)/C(N,k)
(hypergeometric). p_j := Pr(pat(A) = pat(B) | J = j), p_coll := Pr(pat(A)=pat(B)) = Σ_j P(J=j) p_j.

Everything in §1–§2 is a THEOREM (complete proofs). §3 is the derivation of a HEURISTIC rate function
(clearly marked). §4 records the negative result for hard balancing and the canonical fix with its
rigorous rigidity lemma. §5: boosting. Numerics: results.md.

## 1. The averaged second moment identity and its consequences

**Theorem 1.** For π uniform on S_k, independent of σ:
  (a) E_π E[M_π²] / μ² = k! · p_coll =: R_avg.
  (b) p_0 = 1/k! exactly; hence the j = 0 term of R_avg = Σ_j P(J=j)·k!·p_j is P(J=0) ≤ 1,
      and R_avg ≥ P(J=0) ≥ 1 − k²/(N−k).
  (c) E_π Pr(π ⊆ σ) ≥ 1/R_avg.
  (d) E[#distinct k-patterns of σ] ≥ k!/R_avg.

*Proof.* (a) E_π E M_π² = (1/k!) Σ_{π} Σ_{A,B} Pr(pat A = π, pat B = π) = (1/k!) Σ_{A,B} Pr(pat A = pat B)
= (1/k!) C(N,k)² p_coll (A, B running over all ordered pairs of k-subsets; averaging over uniform
independent A,B replaces the sum by C(N,k)² times the probability). Divide by μ² = C(N,k)²/k!².

(b) Let A, B be disjoint. Let G = S_A × S_B act on S_N as follows: for (α, β) ∈ G, σ ↦ σ ∘ g where g
permutes the positions of A according to α, the positions of B according to β (transported along the
order-isomorphisms A ≅ [k] ≅ B) and fixes all other positions. The action preserves the uniform
measure on S_N. Standardisation intertwines: pat(A)(σ∘g) = pat(A)(σ) composed with α (a free, transitive
action of S_k on the pattern of A for fixed σ), and independently for B. Hence conditionally on the
G-orbit of σ, (pat A, pat B) is uniform on S_k × S_k; averaging over orbits, pat(A) and pat(B) are
independent uniform, so Pr(pat A = pat B) = 1/k!. (The same argument with B = ∅ shows pat(A) is uniform,
giving E M_π = μ.) For the last inequality in (b): P(J=0) = C(N−k,k)/C(N,k) = Π_{i=0}^{k−1}
(1 − k/(N−i)) ≥ 1 − k²/(N−k).

(c) Paley–Zygmund/Cauchy–Schwarz at second moment: for each π, Pr(π ⊆ σ) = Pr(M_π > 0) ≥ (E M_π)²/E M_π²
= μ²/E M_π². Average over π and apply Cauchy–Schwarz in the form Σ p_i a_i²/b_i ≥ (Σ p_i a_i)²/(Σ p_i b_i)
with a_i = μ, b_i = E M_π²: E_π [μ²/E M_π²] ≥ μ²/(E_π E M_π²) = 1/R_avg (this is Jensen for x ↦ 1/x since
a_i is constant here). ∎ for (c).

(d) Two proofs. (i) E#distinct = Σ_π Pr(M_π > 0) = k! E_π Pr(π ⊆ σ) ≥ k!/R_avg by (c). (ii) Per-σ
Cauchy–Schwarz: #distinct(σ) ≥ (Σ_π M_π)²/Σ_π M_π² = C(N,k)²/Σ_π M_π²; take expectations and use Jensen
(x ↦ 1/x) : E#distinct ≥ C(N,k)²/E Σ_π M_π² = k!/R_avg. ∎

Remark (sanity): R_avg ≥ max_j' P(J=j') k! p_{j'} ≥ P(J=k)·k! = k!/C(N,k) = 1/μ, so (c) never gives more
than E_π Pr ≥ μ ∧ 1-type bounds can. Also R_avg = E_{A}[M_{pat(A)}]/μ: the ratio of the size-biased mean
copy count to μ.

## 2. The same for leftmost-canonical copies (the Achlioptas–Peres-style restriction)

Definition (W12 §2.1, finite-N version). A copy A = {a_1 < ... < a_k} (values v_r = σ(a_r)) is
**leftmost-canonical** if for every r the strip
  S_r(A) = (a_{r−1}, a_r) × (v⁻_r , v⁺_r)   (a_0 := 0; v⁻_r, v⁺_r = the A-values adjacent to v_r, with 0, N+1 at the ends)
contains no point of σ. Y_π := # leftmost-canonical copies of π.

**Claim A (existence).** π ⊆ σ ⟺ Y_π > 0. (⇐ trivial. ⇒: among all copies of π pick one minimising
Σ_r a_r; if some strip S_r contained a point q, then A − a_r + q would be a copy of π — q has the same
position rank and value rank in A − a_r as a_r — with smaller position sum.) 

**Theorem 2.** With p^can_j := Pr(A, B both leftmost-canonical and pat A = pat B | J = j) and
q := Pr(A leftmost-canonical),
  R_can := E_π E[Y_π²] / (E_π E Y_π)² = k! Σ_j P(J=j) p^can_j / q²   and   E_π Pr(π ⊆ σ) ≥ 1/R_can,
  E[#distinct k-patterns] ≥ k!/R_can.
*Proof.* Identical to Theorem 1: E_π E Y_π² = (1/k!)Σ_{A,B} Pr(both canonical, same pattern);
E_π E Y_π = C(N,k) q/k!; Pr(π ⊆ σ) = Pr(Y_π > 0) ≥ (E Y_π)²/E Y_π² by Claim A + Paley–Zygmund, and the
π-average passes through by the Cauchy–Schwarz inequality Σ p a²/b ≥ (Σ p a)²/(Σ p b) (no
pattern-independence of E Y_π is needed). ∎

**Lemma 3 (rigidity: no two canonical copies of the same pattern share k−1 points).** If A ≠ B are both
leftmost-canonical copies of the same π and |A∩B| = k−1, contradiction. Hence p^can_{k−1} = 0 exactly.

*Proof.* Write A = S ∪ {a}, B = S ∪ {b}, a ≠ b, and wlog x_b < x_a (the hypothesis is symmetric in A, B).
Let r = position rank of a in A, r' = position rank of b in B; x_b < x_a and A∖{a} = B∖{b} = S give r' ≤ r.

Case r' = r. Then a and b have the same S-position-gap. Pattern equality forces the same value rank m
in the common set: rank_y(b in B) = rank_y(a in A) = m (the order isomorphism φ : A → B fixes S and maps
a ↦ b). As in Case 2 below, the (m−1)-st and (m+1)-st smallest values of A sandwich y_b, and the position
window (x-rank) is shared, so b ∈ S_r(A): x_{a_{r−1}} < x_b < x_a and y_b strictly between the A-value
neighbours of a. A was canonical — contradiction.

Case r' < r. Let c := the S-point of position rank r' in A (rank r'+1 in B). Pattern equality: with
A_1 < ... < A_k, B_1 < ... < B_k the position-sorted lists, rank_y(B_i in B) = rank_y(A_i in A) ∀i;
B_{r'} = b, A_{r'} = c, so m := rank_y(b in B) = rank_y(c in A). The value multisets of A and B differ by
the single substitution y_a → y_b. If y_b < A_{(m−1)} (the (m−1)-st smallest A-value) then at most m−2
A-values are < y_b, hence at most m−2 B-values are < y_b, contradicting rank_y(b in B) = m; if
y_b > A_{(m+1)} then at least m+1 A-values are < y_b, hence at least m are in B — contradiction. So
A_{(m−1)} < y_b < A_{(m+1)}, i.e. y_b lies strictly in the open value-gap of c in A (whether or not one
of those neighbours is a itself: y_b ≠ y_a and the interval is open). Positions: rank r' of b in B means
x_{A_{r'−1}} = x_{B_{r'−1}} < x_b < x_{B_{r'+1}} = x_{A_{r'}} = x_c. Hence b ∈ S_{r'}(A), contradicting
A canonical. ∎

Interpretation: canonical copies are exactly the copies with no single-point left-move (Claim A's
argument is local), and Lemma 3 says distinct canonical copies of one π differ in ≥ 2 points — the
"local freedom" of a copy (each point free within a cell of ≈ 4C points, see §3), which is what makes
E M_π²/μ² = e^{Θ(k)}, is completely removed at overlap k−1. Numerics (results.md): the removal is
effective at ALL overlaps — R_can stays bounded where R_avg grows.

## 3. HEURISTIC: the rate of R_avg (relaxed cell-counting) — where the plain second moment fails

(Derivation of the marked heuristic; every approximation is an e^{O(1)}-factor claim, argued but not
proved. Numerics against it in results.md §3.)

Overlap j = k − m. Condition on S = A∩B (j points): S's positions cut [N] into j+1 columns of widths
N·g_a (g Dirichlet(1,…,1)), its values into j+1 rows N·h_b. The dominant pairs have the order
isomorphism φ : A → B fixing S ("no shift": a shifted φ costs an extra value-adjacency ≈ 1/k per shifted
point — an e^{O(1)} total, cf. Lemma 3's exact vanishing for canonical copies). Given "no shift", A∖S
and B∖S occupy the same cells (column,row) with the same multiplicities and matching internal orders.
For cell occupation numbers n_{ab} ∈ {0,1} (multiple occupancy is an e^{O(1)} correction:
E#collisions = O(m²/j²) = O(1)):
  E#pairs(A∖S, B∖S | S) ≈ Σ_{n} Π_{ab} E[(P_{ab})_2] · Π_a (n_{a·}!)⁻¹ Π_b (n_{·b}!)⁻¹,
using: choices of one point of each copy in each occupied cell contribute Π (P_{ab})_2; matching x-orders
within a column are two independent uniform shuffles agreeing with the prescribed order: (n_{a·}!)⁻² per
copy-pair... summed over the n_{a·}! Π n_{·b}! grid-patterns with that occupation, net Π (n_{a·}!)⁻¹(n_{·b}!)⁻¹.
For a uniform permutation E Π_{ab}(P_{ab})_{2n_{ab}} = Π_a (Ng_a)_{2n_{a·}} Π_b (Nh_b)_{2n_{·b}} / (N)_{2m}
(exact), and the Dirichlet average E Π g_a^{2n_a} = (Π_a (2n_a)!) · Γ(j+1)/Γ(j+1+2m) (exact). Using
Σ_n binom(2n,n) t^n = (1−4t)^{−1/2}, the column sum closes:
  Σ_{(n_a): Σn_a=m} (m!/Π n_a!) Π (1/n_a!) Π (2n_a)! = m!·[t^m](1−4t)^{−(j+1)/2} = 4^m Γ((j+1)/2+m)/Γ((j+1)/2),
whence, with L = j+1,
  E#pairs_j ≈ C(N,j) · N^{2m} Φ(L,m)² / m!,  Φ(L,m) = 4^m Γ(L)Γ(L/2+m) / (Γ(L+2m)Γ(L/2)),
  T_j := k!·E#pairs_j / C(N,k)²,  R_avg ≈ Σ_j T_j.       [relaxed.py]
Checks: m=0 gives T_k = 1/μ; m=1 gives T_{k−1} = 4Ck(1+O(1/k)) — i.e. Q_{k−1} := (expected # of B differing
from A in one point with the same pattern) = 4Ck: each of the k points sits in a cell (its S-position-gap ×
S-value-gap, both size-biased, mean 2N/k each) holding ≈ 4N/k² = 4C other points; moving it anywhere in
its cell preserves the pattern. For m = O(1): T_{k−m} ≈ C(k,m)(4C)^m — the "independent local moves"
regime, Σ_m C(k,m)(4C)^m = (1+4C)^k against μ ≈ (e²C)^k e^{−1/(2C)}/(2πk): already this forces
  R_avg ≥ e^{(ln(1+4C) − ln(e²C) − o(1))k},  positive exponent iff C < 1/(e²−4) ≈ 0.2953.
So the PLAIN averaged second moment provably-in-the-heuristic fails for all C < 0.295 (in particular at
C = 1/4), and the k→∞ rate function of ln T_{(1−θ)k}/k is (Stirling; θ = m/k, l = 1−θ)
  r(θ) = −1 + l(ln C − ln l + 1) + 2θ ln C + 2φ(θ) − θ ln θ + θ − 2 ln C − 2,
  φ(θ) = θ ln 4 + θ + l ln l + (l/2+θ)ln(l/2+θ) − (l+2θ)ln(l+2θ) − (l/2)ln(l/2),
with (1/k) ln R_avg → max_θ r(θ) =: ρ(C); r(0) = −ln(e²C) = −(1/k)ln μ. C₂^plain := inf{C : ρ(C) = 0}.
[Computed in relaxed.py / results.md; note ρ(C) ≥ ln((1+4C)/e²C) from the θ→0 expansion, and the true
maximiser sits at θ* bounded away from 0 for C < 0.45 — merged cells (columns with several moved points)
are worth (2n)!/n!² = 4^n·e^{o(n)} extra, the (1−4t)^{−1/2} enhancement.]

**C₂(plain, heuristic) = 1/2 exactly.** Numerically dr/dθ|_{θ=1⁻} = ln(2C) to 4 digits (rate.py /
inline check): r(1) = 0 always (the j = 0 term is O(1) by Theorem 1b), so ρ(C) > 0 iff C < 1/2, with the
near-critical maximiser θ* → 1: for C slightly below 1/2 the second moment fails through DILUTE overlaps
(j = o(k) shared points, each shared point worth a factor 1/(2C) in the pair count net of the
hypergeometric cost). C₂ bisection: 0.49999(1). At C = 1/4 the failure exponent is ρ = 0.141
(θ* = 0.62), at C = 0.2: 0.237 (θ* = 0.52), at C = 0.15: 0.389.

## 4. Why hard balancing fails, and why the canonical restriction is the right fix

Hard balancing (gap profile within (1±δ)/k of uniform) FAILS STRUCTURALLY: balanced copies of π are
geometrically pinned (point i near (i/k, π(i)/k)·N, up to δN/k), so M_π^bal ≈ Π_{i=1}^k P_i with P_i
independent ≈ Poisson(λ), λ = 4δ²C — a product of k independent counts, whence
E (M^bal)²/(E M^bal)² ≈ ((1+λ)/λ)^k = e^{Θ(k)} for every fixed δ; equivalently μ_bal ≈ (4δ²C)^k and the
independent-move count (1+4δ²C)^k always beats it: 1 + 4δ²C > 4δ²C. (The loss in the first moment,
Pr(balanced) = e^{−2k(1+ln(1/2δ)+o(1))}, exactly cancels the gain in cell size.) The problem is not the
profile: it is the per-point Poisson freedom, and no profile constraint removes it.

The leftmost-canonical restriction removes it: within any cell the canonical point is forced to be the
leftmost compatible one (Lemma 3: overlap-(k−1) pairs vanish EXACTLY), while the first moment only drops
from ≈ (e²C)^k to ≈ (κ²C)^k, κ = 2.2795 (W12: E Y_tot/C(N,k) — Poissonized — has threshold C = 1/κ² =
0.19246 < 1/4). The heuristic analogue of §3 for canonical pairs would need joint emptiness of the 2k
strips; we do not derive it — the decisive evidence is numerical (results.md §2): ln R_can is DECREASING
in k at C ≥ 0.25 (k = 4…10), consistent with R_can = e^{o(k)} (plausibly O(1)) for all C > C₂ with
  C₂ ≤ 0.25 < 1/4 (numerically C₂ ≈ 0.2, close to the canonical first-moment point 0.1925),
while at C = 0.15 < 0.1925 it must and does grow (μ_can → 0 exponentially there: R_can ≥ 1/E Y_π).

**Conjecture 4 (what the numerics support).** For every C > 0.1925…, R_can(k, Ck²) = e^{o(k)}; hence
E_π Pr(π ⊆ σ_{Ck²}) ≥ e^{−o(k)} and E#distinct patterns ≥ k! e^{−o(k)} for all C > 0.1925. For C > C₂'
(some C₂' ≤ 1/4) R_can = O(1): E_π Pr(π ⊆ σ) ≥ c > 0.

## 5. Boosting the averaged bound

**Proposition 5 (superposition).** In the Poisson model (Π_λ = rate-1 Poisson process on [0,λ]×[0,λ];
containment thresholds agree with σ_N, N = λ, up to o(k²) by monotonicity and de-Poissonization), for all
m ≥ 1: Pr(π ⊄ Π_{mN}) ≤ Pr(π ⊄ Π_N)^m.
*Proof.* The m diagonal N×N blocks of [0,mN]² carry independent copies of Π_N, any block containing π
gives π ⊆ Π_{mN} (a copy inside one diagonal block is a copy in the whole square, and containment is
monotone in the point set). ∎  Equivalently f(N) := −ln Pr(π ⊄ Π_N) is superadditive: f(mN) ≥ m f(N).

**Corollary 5.1 (positive fraction of patterns, w.h.p., at a log-factor area).** Suppose
R_can(k, C₂k²) ≤ R̄ (Theorem 2 gives E_π p_π ≥ 1/R̄, p_π := Pr(π ⊆ Π_{C₂k²})). Then:
 (a) Pr_π(p_π ≥ 1/(2R̄)) ≥ 1/(2R̄)   (Markov: 1/R̄ ≤ E p ≤ Pr(p ≥ a) + a with a = 1/(2R̄)).
 (b) For every π in that set and every A > 0, with m = ⌈2R̄·A ln k⌉: Pr(π ⊄ Π_{mC₂k²}) ≤ e^{−A ln k} = k^{−A}.
So if R̄ = O(1) at C₂: a positive fraction of π ∈ S_k is contained w.h.p. at N = O(C₂ ln k)·k², and a
positive fraction has Pr(π ⊆ Π_{C₂k²}) ≥ c > 0 already at C₂ itself. If R̄ = e^{o(k)}: an e^{−o(k)}
fraction of π has p_π ≥ e^{−o(k)}, boosted to w.h.p. at area factor e^{o(k)} (still N = k^{2+o(1)}... no:
N = C₂k²·e^{o(k)} is NOT o(k²)-tight — the e^{o(k)} form is only useful if o(k) = O(ln k), i.e. R̄ = poly(k)).

**Remark 5.2 (what the O(1)/(1+ε) loss question needs).** Superposition multiplies area by m, so from a
constant-probability bound it can never reach w.h.p. at C₂(1+ε): (1−c)^{1+ε} is still constant. The
missing ingredient is a sharp-threshold statement for the monotone Poisson property {π ⊆ Π_N} (its window
must be o(k²) around n_½(π); true for the identity via LIS = k²/4 + Θ(k^{4/3}) fluctuations, and
supported for random π by W21: fitted logistic widths ≈ 0.055·n_½ track the finite-k window k^{−2/3}n of
the identity). A Margulis–Russo/Friedgut argument for Poisson monotone properties would convert
"Pr ≥ c at C₂" into "w.h.p. at C₂(1+ε)"; we did not prove it here. Alternatively Prop 15 (paper) runs the
complementary direction: it needs max_π E[M | π ⊄ σ] = e^{o(k)}·max(1,μ) — our R_can numerics (results.md)
are evidence for its averaged form but do not prove the per-π maximum.

**Remark 5.3 (per-π vs averaged).** All k-superpattern consequences need "every π" or "1−o(1) of π";
Theorem 2 controls only the π-average. The quenched numerics (results.md §4: E[Y_π²]/(E Y_π)² varies by a
factor ≲ 2 over random π and the identity at k ≤ 10) support the conjecture that the same bound holds
per-π for 1−o(1) of π, but a proof would need concentration of E[Y_π²] over π (not attempted).
