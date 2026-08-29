# Theorem C: the value-slot refinement of Theorem A, made rigorous

Notation as in work/w3-lowerbound/proof.md: σ ∈ S_n, T = {t_1<…<t_k} ⊆ [n], widths b_i = t_{i+1}−t_{i−1},
pat(σ) = number of distinct k-patterns in σ. "Even indices" are i ∈ {2,4,…} ∩ [2,k−1]; e := ⌊(k−1)/2⌋ is their number.
For a finite set of values V ⊆ [n] and a value u, the *slot* of u relative to V is #{v ∈ V : v < u}.

## Statement

**Theorem C (finite k, fully rigorous).** Let k ≥ 3, n ≥ k, x ∈ (0,1), q := 1−x, an integer threshold β ≥ 3 and
ε > 0. Put h(ε) := (1+ε)log(1+ε) − ε, let P(b) := (b−1)q²x^{b−2} (b ≥ 2; the law of a sum of two i.i.d.
Geom(q) variables), and

    m(b) := (b−2)·(1 − x^{(n−b−1)/(b−2)})   (b ≥ 3),   m(2) := 0.

Let b_1,…,b_e be i.i.d. with law P, let I := {ι : b_ι ≥ β} = {ι_1<…<ι_r}, and

    W_good := min( 1,  Π_{j=1}^{r}  min( (1+ε)·m(b_{ι_j}) + j + 2,  k ) / (b_{ι_j} − 1) ),

    Bad := e·n·q · Σ_{b=β}^{n}  P(b) · exp(−m(b)·h(ε)).

Then for EVERY σ ∈ S_n,

    pat(σ) ≤ x^{−(n+1)} · (x/(1−x))^{k+1} · ( E[W_good] + Bad ).                                   (C)

**Corollary (asymptotics).** Write n = λk²/e², x = e^{−θ/k}, θ = τe²/λ, β = ⌊β̄k⌋. As k → ∞, with
B ~ Gamma(2) (density B e^{−B}), a := θβ̄, c̄ := (1+ε)β̄(1−e^{−τ/β̄}),

    (1/k) log( RHS(C)/k! ) → R(λ; τ, β̄, ε) := τ − 1 − log τ + log λ + max( R_good, R_bad ),

    R_good = max_{s ≥ 0} [ −c̄ s²/2 + ½ log( P(B < a) + e^{s}(1+ε) E[ (1 − e^{−τθ/B}) ; B ≥ a ] ) ],
    R_bad  = −β̄ (1 − e^{−τ/β̄}) h(ε).

The root of  min_{τ,β̄,ε} R(λ;·) = 0 is

    λ_C = 1.00483   (optimum τ = 0.9774, β̄ = 0.594, ε = 0.149; rate.py),

so sp(k) ≥ (1.00483 − o(1))·k²/e². This is a 15× larger excess over 1/e² than Theorem A (λ_A = 1.0003125) and
63× larger than CKS (1.000076). The exact finite-k inequality (C) evaluated by finite_check.py (dynamic programme,
no continuum approximation; all truncation errors added) gives (1/k)log(RHS/k!) = −3.99·10⁻⁴ at k = 30001 and
−6.77·10⁻⁴ at k = 100001 for λ = 1.004, i.e. for those k no permutation of length 1.004k²/e² is a k-superpattern.
(The O(log k/k) finite-size deficit is the polynomial factor e·n·q ≈ k² in Bad.)

## Proof

### Lemma 1' (slot encoding; deterministic)

Let I(T) ⊆ even indices be a *stable* rule (I(T) depends only on the odd positions t_1,t_3,…). For T write
I(T) = {ι_1<…<ι_r}, V(T) := σ({t_j : j ∉ I(T)}) (the k−r "off-I values"), and for i ∈ I(T)

    M_i(T) := #{ distinct slots relative to V(T) of the values σ(p), p ∈ (t_{i−1}, t_{i+1}) }.

Then

    pat(σ) ≤ Σ_T  min( 1,  Π_{j=1}^{r(T)} min( M_{ι_j}(T) + j − 1,  k ) / (b_{ι_j}(T) − 1) ).                (L1')

**Warning.** The per-factor cap min(…, b_{ι_j} − 1) that a first draft of this note used is FALSE (found by the
coordinator by per-class enumeration on the sp(6) witness, k = 6, β = 5: class I = {2,4}, off-I positions
(1,6,11,16), V = {4,6,9,17}, M = (2,4), b_4 − 1 = 4: the false bound gives 2·4 = 8 but the class realises 9
patterns; lemma_check.py's worst case there is I = {2,4}, off-I (2,11,16,17), V = {4,9,14,15}, M = (4,4),
b = (9,5): 18 patterns vs the false 16). The number of positions in window j does not bound the number of
achievable s_j given a prefix, because realisations of the same prefix with different values v_l put a fixed
window position into different slots.
Only the *product* Π(b_{ι_j} − 1) = |ext(ψ)| is a valid cap, whence the min(1, ·).

*Proof.* Fix for each pattern π ⊆ σ an occurrence T(π) and let ψ(T) := (I(T), (t_j)_{j∉I(T)}). Let ext(ψ) be the
set of T' agreeing with ψ off I; since I is non-adjacent, |ext(ψ)| = Π_{i∈I}(b_i−1), and by stability
I(T') = I for all T' ∈ ext(ψ), so the ext(ψ) are pairwise disjoint (T' determines ψ(T')). Every π equals
pat(σ|T') for some T' ∈ ext(ψ(T(π))), hence pat(σ) ≤ Σ_ψ N(ψ), N(ψ) := #{pat(σ|T') : T' ∈ ext(ψ)}.

Trivially N(ψ) ≤ |ext(ψ)| = Π_i(b_i−1). Claim: N(ψ) ≤ Π_{j=1}^r min(M_{ι_j} + j − 1, k), with M_i = M_i(T) for
any T ∈ ext(ψ) (V, hence M_i, is a function of ψ alone).

Write v_j := σ(t'_{ι_j}) for T' ∈ ext(ψ), V_j := V ∪ {v_1,…,v_{j−1}}, and s_j := slot of v_j relative to V_j.
pat(σ|T') is determined by the relative order of the k values; the relative order of V is fixed by ψ; and the
sequence (s_1,…,s_r) determines the relative order of V ∪ {v_1,…,v_r} (insert the v_j one at a time into the
sorted list). So N(ψ) ≤ #{(s_1,…,s_r) realised by some T' ∈ ext(ψ)} ≤ Π_j max_{prefix} #{s_j realised given
(s_1,…,s_{j−1})}. It remains to bound, for a fixed prefix (s_1,…,s_{j−1}), the number of values of s_j over ALL
T' ∈ ext(ψ) realising that prefix — note that different realisations may have different v_1,…,v_{j−1}, so the
set V_j varies; the count is not bounded by the number of positions t'_{ι_j} (that was the error).

The prefix determines the relative order of V_j = V ∪ {v_1,…,v_{j−1}}, hence for every l < j the V-slot
c_l ∈ {0,…,k−r} of v_l, and, within each V-slot c, the relative order of {v_l : c_l = c}. Let n_c := #{l<j : c_l = c}
(Σ_c n_c = j−1). For any realisation and any value u in V-slot c,

    slot of u relative to V_j  =  c + #{l<j : c_l < c} + #{l<j : c_l = c, v_l < u},

where the middle term depends only on the prefix and the last term is an integer in [0, n_c]. Hence over all
realisations of the prefix and all u ∈ σ((t_{ι_j−1}, t_{ι_j+1})), s_j takes at most Σ_{c hit by the window}(1 + n_c)
≤ M_{ι_j} + (j−1) distinct values. Also s_j ∈ {0,…,|V_j|} gives ≤ k − r + j ≤ k values. This proves the claim.

Finally Σ_ψ N(ψ) = Σ_ψ Σ_{T'∈ext(ψ)} N(ψ)/|ext(ψ)| ≤ Σ_{T'} min(1, Π_j min(M_{ι_j}+j−1,k))/Π_i(b_i−1) by disjointness. ∎

Remarks. (a) With min(M+j−1,k) replaced by k this is Lemma 1 of Theorem A (min(1, k!/(k−r)!/Π(b_i−1)) ≤ Π f). (b) Any
fixed ordering of I may be used; we use increasing index order. (c) Per-class brute force (lemma_check.py,
lemma_check_out.txt: every ψ-class enumerated, N(ψ) counted exactly): the corrected per-class bound has ZERO
violations over the sp(6)=17 and sp(7)=23 witnesses, random σ ∈ S_17, S_14, ζ_5, ζ_6, all thresholds β tested;
the old per-factor-capped bound is violated in up to 1273 classes (sp(7), β = 2). Summed values on the sp(6)
witness (pat = 720): corrected 1111 / 1011 / 2681 / 4460 for β = 2/3/5/6 vs Lemma 1's 1306 / 1306 / 3103 / 4822;
sp(7) witness (pat = 5040): 3747 / 3089 / 20585 / 41542 vs 4281 / 4281 / 25450 / 47311.

### Step 2 — the rule and the Bernoulli representation

Rule: I(T) := {i even : b_i ≥ β}; stable (depends on odd positions only). Let W(T) denote the summand in (L1').

Let B ⊆ ℕ be a Bernoulli(q) site process (each site independently in B with probability q = 1−x) and T(B) :=
the k smallest points of B; set W(T(B)) := 0 if |B ∩ [n]| < k. For T ⊆ [n], P(T(B) = T) = q^k x^{t_k − k}
(B ∩ [1,t_k] = T). Since x^{n+1} = x^{t_k}·x^{n+1−t_k} ≤ x^{t_k}·x/(1−x),

    Σ_T W(T) = x^{−(n+1)} Σ_T x^{n+1} W(T) ≤ x^{−(n+1)} (x/(1−x)) Σ_T x^{t_k} W(T)
             = x^{−(n+1)} (x/(1−x))^{k+1} · E_B[ W(T(B)) ].                                                (2)

Under B the gaps a_0 = t_1, a_j = t_{j+1} − t_j (j < k) of T(B) are i.i.d. Geom(q), P(a = t) = q x^{t−1}; hence the
even widths b_{2j} = a_{2j−1} + a_{2j}, j = 1..e, are i.i.d. with law P(b) = (b−1)q²x^{b−2}. (Theorem A is the
case W = Π f(b_i) of (2); E_B W = (1 − x^k)^e.)

### Step 3 — domination of the slot count by independent indicators

Fix an even i, and let lo := t_{i−1}, hi := t_{i+1}, b := hi − lo, U := σ((lo,hi)) (|U| = b−1), u_1 < … < u_{b−1}
its elements. Define

    M̌_i := #{ slots relative to V̌ := σ(B \ [lo,hi]) hit by U }.

(3a) M_i(T(B)) ≤ M̌_i + 2. Indeed T(B) ∩ (lo,hi) = {t_i} and t_i ∈ I, so the off-I positions lie in
B \ (lo,hi) = (B \ [lo,hi]) ∪ {lo,hi}; thus V ⊆ V̌ ∪ {σ(lo),σ(hi)}, and the slot count is monotone in the value set
and increases by ≤ 1 per added value.

(3b) M̌_i − 1 = Σ_{ℓ=1}^{b−2} X_ℓ, X_ℓ := 1[B ∩ A_ℓ ≠ ∅], A_ℓ := σ^{−1}((u_ℓ, u_{ℓ+1})) \ {lo,hi}. The A_ℓ are
pairwise disjoint subsets of [n] \ [lo,hi] (values strictly between consecutive elements of U are not in U, so
their positions are outside (lo,hi)), with Σ_ℓ |A_ℓ| ≤ n − b − 1. Under the product measure the X_ℓ are
independent Bernoulli(1 − x^{|A_ℓ|}), and they are independent of B ∩ [lo,hi].

(3c) E[M̌_i − 1] = Σ_ℓ (1 − x^{|A_ℓ|}) ≤ (b−2)(1 − x^{(n−b−1)/(b−2)}) = m(b), by concavity of g ↦ 1 − x^g (Jensen).
This is the only place where σ enters, and it enters only through Σ|A_ℓ| ≤ n − b − 1: the bound is uniform in σ.

### Step 4 — Chernoff

For S a sum of independent indicators with E S ≤ m and ε > 0: E e^{λS} = Π(1 + p_ℓ(e^λ−1)) ≤ exp(m(e^λ−1)) for
λ ≥ 0; Markov with λ = log(1+ε) gives P(S ≥ (1+ε)m) ≤ exp(−m h(ε)).

### Step 5 — assembly

Let G := ∩_{i∈I(T(B))} {M̌_i − 1 ≤ (1+ε)m(b_i)}. On G, by (3a), M_{ι_j} + j − 1 ≤ M̌_{ι_j} + j + 1 ≤
(1+ε)m(b_{ι_j}) + j + 2, so W(T(B)) ≤ W_good (W_good is a function of the even widths only). Off G we use
W ≤ 1, which holds because the summand of (L1') is min(1, ·) — i.e. because N(ψ) ≤ |ext(ψ)| = Π(b_i−1); note the
individual factors min(M+j−1,k)/(b−1) may exceed 1 when b − 1 < k, which is the case for the threshold β ≈ 0.59k
used below, so the cap on the whole product (not per factor) is what is needed here. Hence

    E_B W ≤ E[W_good] + Σ_{i even} P( i ∈ I(T(B)),  M̌_i − 1 > (1+ε)m(b_i) ).

For fixed i, the event is contained in ∪_{1≤lo<hi≤n, hi−lo≥β} {lo,hi ∈ B, |B∩(lo,hi)| = 1, M̌(lo,hi) − 1 > (1+ε)m(hi−lo)},
where M̌(lo,hi) is the count of (3b) for the fixed window (lo,hi). By (3b) the two events in each term live on
disjoint sets of coordinates, so the probability factorises as q²·(b−1)q x^{b−2} · P(M̌(lo,hi)−1 > (1+ε)m(b)) ≤
q·P(b)·exp(−m(b)h(ε)) (Steps 3c, 4). Summing over lo ≤ n, over b ≥ β and over the e even indices gives Bad.
Inserting into (2) proves (C). ∎

### Proof of the Corollary

E[W_good] ≤ E[ Π_{i∈I} g(b_i) · Π_{j=1}^{r} (1 + (j+2)/c) ] with g(b) := min((1+ε)m(b), k)/(b−1) (dropping the
min(1,·) cap except for the width tail below) and
c := (1+ε)·min_{β≤b≤n/2} m(b) (widths > n/2 have total probability e·e^{−Ω(k)} at rate ≥ τ/2, far below every
rate considered; they are bounded by weight 1). Π_j(1 + (j+2)/c) ≤ exp((r² + 5r + 6)/(2c)), and by Legendre
duality r²/(2c) = sup_s (sr − cs²/2) ≤ cΔ²/8 + max over a grid of spacing Δ, so

    E[W_good] ≤ e^{3/c + cΔ²/8} Σ_{s∈Δℤ_{≥0}} e^{−cs²/2} · [ P(b<β) + e^{s + 5/(2c)} E(g(b); b ≥ β) ]^{e},

using independence of the even widths. With b = (k/θ)B, B → Gamma(2), m(b)/k → (b/k)(1 − e^{−τk/b}) (since
x^{n/b} = e^{−θn/(kb)} = e^{−τk/b}), c/k → c̄, and (k+1)log(x/(1−x)) − (n+1)log x − log k! = k(τ − 1 − log τ +
log λ) + O(log k), the rate of E[W_good] is R_good (the sum over s is dominated by its largest term up to a factor
polynomial in k), and the rate of Bad is −min_{b≥β} m(b)h(ε)/k → R_bad because m(b)/k → β̄(1−e^{−τ/β̄}) at b = β̄k
is the minimum of m(b) over β ≤ b ≤ n/2 (attained at b = β: checked numerically in heur0.py; in the limit
(b/k)(1−e^{−τk/b}) is increasing in b) and P(b ≥ β) is a constant. The finite-k DP in finite_check.py uses m(b)
per width and needs no monotonicity.
finite_check.py evaluates (C) exactly (DP over r, truncations bounded) and confirms the limit. ∎

## The obstruction to the naive route, and why it is not needed

The heuristic in w3 wanted E_T[Π_i N_i] ≲ Π_i E[N_i]. The N_i (= M_i) are all *increasing* functions of the common
random set of off-I positions; under a product measure Harris/FKG gives E Π N_i ≥ Π E N_i — the wrong direction —
and the joint upper tails P(∩_i {N_i large}) are likewise ≥ the product. Negative association (Joag-Dev–Proschan)
fails as well: for two windows whose value sets are nested (σ can arrange this for every window of a typical T,
e.g. a "comb" permutation whose blocks all carry values of spacing n/k), N_i and N_{i'} are essentially the same
variable. A Hölder split of Σ_{i∈S}(N_i − 1) shows the joint upper tail can be as bad as the single-window
Chernoff bound e^{−m h(ε)} — comonotone windows — so no inequality of the form E Π N_i ≤ (1+o(1))Π E N_i can be
proved from marginal information (a variable equal to k w.p. 0.63 and 1 otherwise, common to all windows, has the
same marginal means).

What rescues the mechanism is that we do not need the product to factor: we need (i) an upper bound on the
*typical* value of every N_i simultaneously, and (ii) a bound on the probability that any single N_i is atypically
large. For (ii) only one window at a time matters (union bound), and for a single window the slot count is a sum of
hits of *disjoint* position sets by a *product* Bernoulli process — independent indicators — once the off-I
positions are dominated by the full Bernoulli process B ⊇ T(B) (Step 3). The union bound costs a polynomial
factor e·n·q ≈ k², invisible in the rate. Comonotonicity of the N_i is then harmless: the comonotone worst case
only makes the good event G fail with the single-window probability e^{−m h(ε)}, which is what Bad charges.

The price is the Chernoff slack ε: the good factor is (1+ε)m(b)/(b−1) instead of m(b)/(b−1), and the optimum
balances R_good = R_bad (ε ≈ 0.15, β̄ ≈ 0.59). With ε = 0 and no Bad term (the pure heuristic) the same rate
computation gives λ ≈ 1.0117 (heur0.py), so about 40% of the heuristic excess survives the rigorous treatment.

## What is rigorous vs heuristic

- Lemma 1', Theorem C (inequality (C)): rigorous, finite k, explicit, for every σ; independently verified on the
  sp(6), sp(7) witnesses, random permutations and ζ_5, ζ_6 (lemma_check.py, exact enumeration of all T).
- The certificates "(1/k)log(RHS(C)/k!) < 0 at k = 30001, 100001, λ = 1.004" (finite_check.py): floating-point
  evaluation of (C) with all truncation errors added (widths > bmax: exact geometric tail; r > 0.08k: Chernoff
  binomial tail, value ≤ 10⁻²⁷⁰); no continuum approximations. Interval arithmetic was not used.
- λ_C = 1.00483: root of the explicit continuum rate function; the discrete→continuum limit is the same routine
  limit as in Theorem A (errors O(log k/k)), corroborated by the finite-k evaluations (−4.0·10⁻⁴ at 3·10⁴,
  −6.8·10⁻⁴ at 10⁵ for λ = 1.004, versus the limit −8.2·10⁻⁴).
- Not done (possible improvements): width-dependent ε (flat Chernoff exponent) gives λ = 1.00501 (rate2.py);
  both parities as in Theorem B; keeping Π f(b_i) on the bad event instead of 1 (requires nothing new but a
  Cauchy–Schwarz split); replacing Chernoff by an exact large deviation for the Poisson-binomial slot count.
