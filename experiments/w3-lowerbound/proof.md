# Improved lower bound for superpatterns via exact-rate encoding

Notation: σ ∈ S_n, k-subsets T = {t_1<…<t_k} ⊆ [n], gaps a_0 = t_1, a_j = t_{j+1}−t_j (1≤j<k), a_k = n+1−t_k
(so a_j ≥ 1, Σ_{j=0}^k a_j = n+1, and T ↔ (a_0,…,a_k) is a bijection onto compositions of n+1 into k+1
positive parts). Width of index i: b_i = t_{i+1}−t_{i−1} = a_{i−1}+a_i (2 ≤ i ≤ k−1). pat(σ) = number of
distinct k-patterns contained in σ. Throughout k is odd (WLOG, as in CKS).

## Theorem A (fully rigorous, finite k)

For every σ ∈ S_n, every odd k ≥ 3 and every x ∈ (0,1):

    pat(σ) ≤ x^{−(n+1)} · (x/(1−x))^{k+1} · (1 − x^k)^{(k−1)/2}.                        (A)

Consequently, writing n = λk²/e² and choosing x = e^{−θ/k},

    (1/k)·log( pat(σ)/k! ) ≤ λθ/e² − log θ + 1 + ½·log(1−e^{−θ}) + O(log k / k),      (A')

and minimising over θ (θ* = 7.3696) the right-hand side is negative for every fixed λ < λ_A, where

    λ_A = 1.0003125…   (the root of  min_θ [λθ/e² − log θ + 1 + ½ log(1−e^{−θ})] = 0).

Hence for λ < λ_A every σ ∈ S_n with n ≤ λk²/e² contains only e^{−Ω(k)}·k! patterns, and

    sp(k) ≥ (1.0003125 − o(1))·k²/e²,

improving CKS's 1.000076 by a factor ≈ 4.1 in the excess over 1/e².

## Theorem B withdrawn (2026-09-10)

The both-parity rule is not stable. For k=5, take

    T=(1,2,6,9,10), I(T)={3}; T′=(1,2,3,9,10), I(T′)={4}.

The tuples agree outside I(T), but the selected set changes. Thus the
encoding lemma cannot justify either 1.000384 or 1.000437. The transfer
operator calculations remain numerical investigations of an invalid
encoding rule; certifying their arithmetic would not repair the argument.
Theorem A's even rule is unaffected. Its finite inequality is Lean-verified;
the Lean numerical certificate is at λ=1.0003, not the optimized λ_A.
The stronger certified coefficient 1.0073 is proved in
[corrected C′](../w25-asymptopia-review/proof.md).

## Proof of Theorem A

### Step 1 – stable encodings (double counting)

Let 𝓘 be a map T ↦ I(T) ⊆ {2,…,k−1} such that I(T) contains no two consecutive integers and is
**stable**: whenever T' agrees with T outside I(T) (i.e. t'_j = t_j for j ∉ I(T)), we have I(T') = I(T).

**Lemma 1.** For every stable 𝓘,

    pat(σ) ≤ Σ_T  k!/(k−|I(T)|)! · Π_{i∈I(T)} 1/(b_i(T)−1).

*Proof.* For each pattern π contained in σ fix an occurrence T = T(π); encode π by
φ(π) = ( I, (t_j)_{j∉I}, (π(i))_{i∈I} ), I = I(T). Injectivity (CKS): from (t_j)_{j∉I} and σ we know the
relative order of the values σ(t_j), j ∉ I; from (π(i))_{i∈I} we know which k−|I| ranks the j ∉ I occupy,
hence π. So pat(σ) ≤ |φ(range)|. Group the triples by ψ = (I,(t_j)_{j∉I}); each ψ admits at most
k!/(k−|I|)! third components. Let ext(ψ) be the set of T' ∈ C([n],k) agreeing with ψ off I; since I is
non-adjacent, t'_i ranges independently over the open interval (t_{i−1},t_{i+1}), so
|ext(ψ)| = Π_{i∈I}(b_i−1), where b_i is determined by ψ. By stability every T' ∈ ext(ψ) satisfies
I(T') = I, so the sets ext(ψ), ψ ∈ Ψ := {ψ arising from some T}, are pairwise disjoint (a T' determines
I(T') and hence ψ). Therefore

    Σ_{ψ∈Ψ} k!/(k−|I|)!  =  Σ_{ψ∈Ψ} Σ_{T'∈ext(ψ)} k!/(k−|I|)!/|ext(ψ)|  ≤  Σ_{T'} k!/(k−|I(T')|)!/Π_{i∈I(T')}(b_i−1).  ∎

Note: no threshold parameter and no case split; CKS's Lemma 2.1 ("Case 1") is not needed because the
right-hand side is an *expectation of a product*, and the large-deviation cost of "few large widths" is
paid automatically by that product.

### Step 2 – the even rule

Take I(T) = { i even : b_i − 1 > k }. It is non-adjacent and stable (it depends only on the odd t_j).
Since k!/(k−|I|)! ≤ k^{|I|}, Lemma 1 gives

    pat(σ) ≤ Σ_T W(T),   W(T) := Π_{i even} f(b_i),   f(b) := min(1, k/(b−1)).        (1)

### Step 3 – exact Chernoff tilt for the sum constraint

Identify T with its composition a = (a_0,…,a_k), Σa = n+1, and W with the function W(a) = Π_{j=1}^{(k−1)/2}
f(a_{2j−1}+a_{2j}) (even i = 2j has b_{2j} = a_{2j−1}+a_{2j}). For any x ∈ (0,1),

    Σ_T W(T) = x^{−(n+1)} Σ_{a: Σa=n+1} x^{Σa} W(a) ≤ x^{−(n+1)} Σ_{a∈ℤ_{≥1}^{k+1}} x^{Σa} W(a),

and the unconstrained sum factorises (a_0, a_k are free; the pairs (a_{2j−1},a_{2j}) are disjoint):

    Σ_{a} x^{Σa} W(a) = (x/(1−x))² · Π_{j=1}^{(k−1)/2} Σ_{a,a'≥1} x^{a+a'} f(a+a')
                      = (x/(1−x))^{k+1} · ( E_x[ f(a+a') ] )^{(k−1)/2},

where under E_x the gaps a,a' are i.i.d. geometric, P(a=t) = (1−x)x^{t−1}.

### Step 4 – the closed form E_x f(a+a') = 1 − x^k

P(a+a' = s) = (s−1)(1−x)²x^{s−2} and P(a+a' ≥ s) = x^{s−2}(1+(s−2)(1−x)). With f(s) = 1 for s ≤ k+1 and
f(s) = k/(s−1) for s ≥ k+2:

    E_x f(a+a') = 1 − P(a+a' ≥ k+2) + Σ_{s≥k+2} k(1−x)² x^{s−2}
                = 1 − x^k(1+k(1−x)) + k(1−x)x^k = 1 − x^k.

(Verified numerically in verify.py.) Combining Steps 2–4 proves (A).

### Step 5 – asymptotics

Put x = e^{−θ/k}. Then −(n+1)log x = (n+1)θ/k, and (k+1)log(x/(1−x)) = (k+1)[log(k/θ) − θ/(2k) + O(k^{−2})]
because 1−e^{−θ/k} = (θ/k)(1 − θ/(2k) + O(k^{−2})). With log k! = k log k − k + O(log k) and n = λk²/e²:

    log( RHS(A)/k! ) = k[ λθ/e² − log θ + 1 + ½ log(1−e^{−θ}) ] + O(log k),

which is (A'). Setting θ = τe²/λ this is k·Φ(τ,λ) + O(log k) with
Φ(τ,λ) = τ − 1 − log τ + log λ + ½ log(1 − e^{−τe²/λ}); Φ is strictly convex in τ, min at τ* = 0.99768, and
min_τ Φ(τ,λ) is increasing in λ with root λ_A = 1.0003125 (trackA.py, verify.py: at k = 10⁵, λ = 1.00031
the finite-k bound (A) gives log(pat/k!)/k ≤ −1.1·10⁻⁵ < 0). ∎

Remark (where the number comes from). Per even index the factor is E min(1, θ/B), B ~ Gamma(2), which equals
1 − e^{−θ} = 1 − e^{−e²τ/λ} ≈ 1 − 6.2·10⁻⁴; half the indices are even, and the tilt costs τ−1−log τ ≈ 2.7·10⁻⁶.
CKS instead select only ck = 0.00075k indices above a threshold d = 8.18 and pay a Chernoff "Case 1"; the
exact treatment recovers *all* the mass e^{−θ} = Σ_{B>θ} E[(1−θ/B)] instead of c·log(d/e²).

## Verification scope

Theorem A's finite inequality and a rational-parameter negativity certificate
at λ=1.0003 are formalized in Lean. The optimized root λ_A≈1.00031251 is a
numerical evaluation of the displayed analytic minimization. For even k,
apply the odd result to k−1 and use sp(k)≥sp(k−1).
