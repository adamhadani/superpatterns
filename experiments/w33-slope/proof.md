# W33 — the slope of ln p_π(n) near the threshold: statements and proofs

Notation. σ_n uniform in S_n; for π ∈ S_k, p_π(n) = Pr(π ⊄ σ_n) = Av_n(π)/n!; μ(n) = Σ_{π∈S_k} p_π(n) = E M.
Slope s_π(n) := ln p_π(n−1) − ln p_π(n) ≥ 0 (deleting a point cannot create a copy), s_μ(n) := ln μ(n−1) − ln μ(n).
Window: n = Ck², x := k/√n = 1/√C. Tags: PROVED / HEURISTIC / NUMERICAL.

## 1. Exact identities for the one-point ratio — PROVED

**Lemma 1.1 (three faces of the ratio).** For every π ∈ S_k and n ≥ 1, with σ' uniform on Av_{n−1}(π):
(a) (slot form) p_π(n)/p_π(n−1) = 1 − E[ρ(π;σ')], ρ = |Rev(π;σ')|/n² the fraction of the n² insertion slots that create a copy (W30 Cor 1.3);
(b) (generating-tree form) p_π(n)/p_π(n−1) = E[S_max(σ')]/n, where S_max(σ') = #{p ∈ [n] : inserting a new maximum at position p keeps σ' π-avoiding};
(c) (deletion form) p_π(n−1) − p_π(n) = (1/n)·E[ |J_π(σ_n)| ; π ⊂ σ_n ], J_π(σ) = set of points of σ common to ALL copies of π in σ (J = ∅ if π ⊄ σ).
Consequently 0 ≤ s_π(n) ≤ ln(n/(k−1)) for n > k, and s_π(n) = ln(1 + (1/n)E[|J_π|; π⊂σ_n]/p_π(n)) ≤ ln(1 + (k/n)·Pr(J_π(σ_n)≠∅)/p_π(n)).

*Proof.* (a) The map (σ', slot) ↦ σ'+x from S_{n−1}×[n]² to S_n is n-to-1 (choose which point of the image is x), so
n·Av_n = Σ_{σ'∈Av_{n−1}} (n² − |Rev(π;σ')|); divide by n·(n−1)!·n = n²(n−1)!·… i.e. by n·n!/(n−1)!·Av_{n−1}/Av_{n−1}: p(n)/p(n−1) = Av_n (n−1)!/(n! Av_{n−1}) = (1/n²)·mean(n² − |Rev|).
(b) Every σ ∈ Av_n(π) arises exactly once by inserting a new maximum into the avoider obtained by deleting its maximum, so Av_n = Σ_{σ'∈Av_{n−1}} S_max(σ'); divide as before.
(c) Delete a uniformly random point x of σ_n: σ_n − x is uniform in S_{n−1}, so p(n−1) = Pr(π ⊄ σ_n − x) = Pr(π ⊄ σ_n) + Pr(π ⊂ σ_n, π ⊄ σ_n − x), and π ⊄ σ_n − x with π ⊂ σ_n iff x lies in every copy, i.e. x ∈ J_π(σ_n); average over x.
For the bounds: S_max ≥ k−1 for every avoider when n > k — if the maximum of π sits at position j, a new maximum at any position p ≤ j−1 (fewer than j−1 points to its left) or p ≥ n−(k−j)+1 has too few points on one side to be the maximum of a copy; these are (j−1)+(k−j) = k−1 distinct positions. So s = ln n − ln E S_max ≤ ln(n/(k−1)). |J| ≤ k gives the last bound. ∎
(W30 Lemma 3.3, s ≤ ln n, is the case S_max ≥ 1.) The μ-versions: μ(n)/μ(n−1) = 1 − E_μ[ρ] with E_μ the p_π(n−1)-weighted mean (W30 Prop 2.1), and μ(n−1) − μ(n) = (1/n) E Σ_π |J_π(σ_n)|.

**Remark 1.2 (what "slope O(1)" means).** By (b), s_π(n) ≤ A ⟺ a uniformly random π-avoider of length n−1 has, on average, ≥ n/e^A positions accepting a new maximum; by (a), ⟺ on average a fraction ≥ e^{−A} of the n² slots is safe. Since every safe slot lies outside every completion cell of every copy of every child π^{(i)} (W30 Cor 1.3), "slope O(1)" is a statement that the union of the e^{Θ(k)} completion cells of a typical avoider leaves a constant fraction of the square uncovered.

## 2. Reductions: what the two directions are equivalent to — PROVED

**Theorem 2.1 (a uniform LOWER bound on the per-pattern slope is at least as strong as the main conjecture).**
Suppose s_π(n) ≥ s_0 > 0 for all π ∈ S_k, all n ∈ [ck², Ck²] and all large k. Then p_π(Ck²) ≤ e^{−s_0(C−c)k²} for every π, i.e. Conjecture CP* of W27 holds with rate ι = s_0(C−c)/C, and by W27 Lemma 0.1/0.2 σ_n is a k-superpattern w.h.p. for n = Ck² (Alon's conjecture up to the constant).
*Proof.* Sum the slopes: ln p_π(ck²) − ln p_π(Ck²) ≥ s_0(C−c)k² and p_π(ck²) ≤ 1. ∎
So no argument confined to "insert one point" can prove the lower bound uniformly over the window: it would prove speed-k² tails for every pattern. The lower bound is only plausible, and only needed, *locally*:

**Proposition 2.2 (what W28 Cor. 1.2 actually needs; scale k, not k²).** (i) For every k and every n < n' one has s̄_μ[n,n'] := (ln μ(n) − ln μ(n'))/(n'−n) ≤ ln(k!)/(n'−n) − ln μ(n')/(n'−n). In particular, over any window of length εk² ending at the median threshold t(k) (μ(t) ≍ 1 by W28 (a)), the average μ-slope is ≤ (1+o(1)) ln k/(εk) → 0. Hence the μ-slope can NOT be bounded below by a constant over a window of length ≍ k²; the observed s_μ ≈ 0.5 (W24, results.md §2) is a local feature of the last O(k ln k) points before the threshold, where ln μ ≤ ln k! must be spent.
(ii) Cor. 1.2 needs n_1 − n_0 = o(k²) where μ(n_0) = e^{ak}/2, μ(n_1) = 1/2. If s_μ(n) ≥ s_0 for all n ∈ [n_0, n_1] then n_1 − n_0 ≤ (ak + ln 2)/s_0, which is o(k²) for every a = o(k); it suffices that s_μ ≥ s_0 on the range where 1/2 ≤ μ(n) ≤ e^{ak}/2 — a window of length O(ak) if the bound holds. Equivalently (by Lemma 1.1(a), μ-version) it suffices that a uniformly random slot revives on average a fraction ≥ 1 − e^{−s_0} of the missing patterns whenever 1/2 ≤ μ(n) ≤ e^{ak}.
*Proof.* (i) μ ≤ k!, and μ(t(k)) ≥ Pr(M>0) = 1/2. (ii) Sum the slopes as in 2.1. ∎

**Theorem 2.3 (the UPPER bound, averaged over the window, is a lower bound on avoidance probabilities).**
(i) If s_π(n) ≤ A for all n ∈ [k²/6, Ck²] then p_π(Ck²) ≥ ½·e^{−A(C−1/6)k²} (W12 universal absence: p_π(k²/6) ≥ 1/2 for all π and large k).
(ii) Conversely, if p_π(Ck²) ≥ e^{−Bk²} then the average of s_π over [0, Ck²] is ≤ B/C; i.e. "slope O(1) on average over the window" ⟺ "I_π(C) := −ln p_π(Ck²)/(Ck²) = O(1) uniformly in π, k" (the per-point rate of W27).
(iii) (μ-version, unconditional) Since μ(n) ≥ p_id(n) and p_id(n) = exp(−n H_0(k/√n)(1+o(1))) (Deuschel–Zeitouni; §3 gives H_0 in closed form), the average of s_μ over [0, Ck²] is ≤ H_0(1/√C) + o(1) for every fixed C > 1/4; e.g. ≤ 0.155 at C = 1, ≤ 0.083 at C = 3/4. Together with (i) of Prop. 2.2: on average over the window the μ-slope is provably O(1) (indeed → small constants); only the *pointwise* statement s_μ(n) ≤ A for every n in the window — which is what W30 Prop. 3.2/Cor. 3.4 uses with n − min(w,h) ≈ n − k√ln k — is open.
*Proof.* Telescoping sums of the slopes, as in 2.1; for (iii) −ln μ(Ck²) ≤ −ln p_id(Ck²). ∎

**Corollary 2.4 (pointwise bound from monotonicity, conditional).** If for some π the slope s_π(n) is nondecreasing in n on [ck², Ck²] (log-concavity of p_π there; true for the identity, §3, and for every pattern in our data, results.md), then for n in the window s_π(n) ≤ average of s_π over [n, Ck²] ≤ (ln p_π(n) − ln p_π(Ck²))/(Ck² − n) ≤ (−ln p_π(Ck²))/(Ck²−n) = C I_π(C) k²/(Ck² − n), and s_μ(n) ≤ C H_0(1/√C) k²/(Ck² − n)+o(1) in the μ-case if s_μ is nondecreasing. PROVED given the monotonicity hypothesis, which we did NOT prove.


**Proposition 2.5 (the slope at the point where a pattern reaches p_π = 1/k! tends to 0 — PROVED for the identity given §3, HEURISTIC in general).**
(i) Identity. Let n_id(k) be defined by p_id(n_id) = 1/k!. By §3, n_id = C_k k² with C_k H_0(1/√C_k) = ln k!/k², so C_k ↓ 1/4 and, since H_0(2−ε) ~ ε³/12, the slope there is s_id(n_id) ~ (3/4)·ε_k² with ε_k ~ (48 ln k/k)^{1/3}, i.e. s_id(n_id(k)) = Θ((ln k/k)^{2/3}) → 0. Numerically (formula of Prop 3.3): C_k = 0.99, 0.65, 0.44, 0.34 and s_id(n_id) = 0.44, 0.22, 0.080, 0.025 for k = 10, 10², 10³, 10⁴.
(ii) General scaling (HEURISTIC). Suppose −ln p_π(Ck²) = k² C I_π(C) with I_π vanishing at π's threshold τ_π like κ(C − τ_π)^γ (γ = 3 for the identity by Tracy–Widom; γ = 2 for a Gaussian-fluctuation mechanism; γ = 1 only for a kink). Then t(k)/k² → sup_π τ_π (first-moment argument: μ ≤ k! e^{−k² c(δ)} above sup τ_π + δ, and some p_π ≥ 1/2 below), and at n = t(k) the patterns carrying μ sit at C = τ_π + δ_k with k² δ_k^γ ≍ k ln k, so their slope is ≍ γκ δ_k^{γ−1} = Θ((ln k/k)^{1−1/γ}) → 0 unless γ = 1. Consequently the window of W28 Cor. 1.2 has length n_1 − n_0 = Θ(a k^{2−1/γ} (ln k)^{1/γ−1}) and is o(k²) iff a = o(k^{1/γ} (ln k)^{1−1/γ}): for γ = 3, a = o(k^{1/3} (ln k)^{2/3}); for γ = 2, a = o((k ln k)^{1/2}); W28's "a = o(k)" corresponds to γ = 1. The observed R = e^{≈0.7k} = e^{O(k)} is NOT covered by these windows asymptotically (O(k) ≠ o(k^{1/3})): under a smooth edge, the hard-core criterion H(a) with a = Θ(1) (i.e. Λ_π ≤ e^{O(k)}) still gives n_1 − n_0 = O(k^{5/3}) = o(k²) and the conclusion "threshold constant = first-moment constant" survives, but the sandwich is only e^{−O(k)} ≤ Pr(M>0)/μ ≤ 1 over a window of width k^{5/3}, not k. The flat s_μ ≈ 0.5 seen for k ≤ 9 (results.md §2) is pre-asymptotic: for the identity itself the exact slope at C = 3/4 falls from 0.60 to 0.40 between k = 4 and 9 while the limit is 0.29, and the decay (ln k/k)^{2/3} is invisible below k ≈ 100.

## 3. The identity: closed-form slope — PROVED modulo one numerically established input

Let ℓ = k−1 and let Q_λ = Pr(L ≤ ℓ) for a Poisson point process of intensity λ in the unit square (L = longest increasing chain), P_m = Pr(LIS(σ_m) ≤ ℓ) = p_id(m).

**Fact 3.1 (Gessel).** Q_λ = e^{−λ} det[ I_{i−j}(2√λ) ]_{i,j=1}^{ℓ} (modified Bessel functions).
**Input 3.2 (NUMERICAL, 3–4 digits; and consistent with the fixed-ℓ asymptotics det[I_{i−j}(t)] ~ c_ℓ e^{ℓt} t^{−ℓ²/2}).**
For 0 < y := ℓ/√λ < 2,   −(d/dλ) ln Q_λ = (1 − y/2)²  (out/lis_poisson.txt: ℓ = 10, 20; y = 0.8, 1, 1.2, 1.414, 1.7: 0.3603/0.3601, 0.2506/0.2502, 0.1614/0.1603, 0.0892/0.0866, 0.0309/0.0252 against 0.36, 0.25, 0.16, 0.0858, 0.0225.)
Integrating from λ = ℓ²/4 (y = 2, where the constraint is not binding) gives the Poissonized rate
   −ln Q_λ = λ H_P(y), H_P(y) = 1 − 2y + 3y²/4 + (y²/2) ln(2/y)   (numerically: 0.0993/0.0974 at y=1 → 0.0966; 0.1751/0.1738 at y=0.8 → 0.1732).
Interpretation of 3.2: in the Poisson process conditioned on L ≤ ℓ, a new uniform point completes an increasing chain of length ℓ+1 with probability exactly (1 − ℓ/(2√λ))² — the square of the relative deficit of ℓ below the unconstrained value 2√λ.

**Proposition 3.3 (de-Poissonization; PROVED given 3.2 and the existence of the fixed-n rate).** Write P_m = e^{−G(m)} with G nondecreasing (deletion monotonicity) and s(m) = G(m) − G(m−1). Then Q_λ = Σ_m e^{−λ}λ^m/m!·P_m, and by Laplace's method (G(m) = m H_0(ℓ/√m)(1+o(1)) with H_0 continuous, DZ 1999) the sum is dominated by m* solving ln(λ/m) = s(m), i.e. m* = λ e^{−s(m*)}, and −d ln Q/dλ = 1 − m*/λ (envelope theorem). With Input 3.2, m*/λ = 1 − (1−y/2)² = y(1 − y/4). Put x = ℓ/√m* (the fixed-n variable); then y = 4x²/(4+x²) and
     e^{−s(x)} = 16x²/(4+x²)²,   i.e.   s_id = 2 ln( (4+x²)/(4x) ) = ln( (4C+1)²/(16C) ) at n = Ck² (x² = 1/C),
     H_0(x) = −1 + x²/4 + (x²/2) ln((4+x²)/(2x²)) + 2 ln((4+x²)/(4x))   (fixed-n lower-tail rate: lim −(1/n) ln Pr(LIS(σ_n) ≤ x√n)).
Checks (all PROVED as identities, verified numerically in log.md §2): (i) H_0 − (x/2)H_0' = s(x) (the fixed-n slope is the n-derivative of nH_0(k/√n)); (ii) H_0(x) = 2 ln(1/x) − 1 + o(1) as x → 0, matching the rigorous bound Av_n(I_{ℓ+1}) ≤ ℓ^{2n} exactly (this is where the naive guess −1 + x²/4 + 2ln(2/x) fails); (iii) H_0(2−ε) = ε³/12 + O(ε⁴): cubic zero, matching the Tracy–Widom left tail e^{−|s|³/12} through the moderate-deviation regime; (iv) the Legendre transform min_t [1 − t + t ln t + t H_0(y/√t)] equals H_P(y) with t* = y(1−y/4) (checked to 5 digits); (v) the fixed-n expected number of admissible positions for a new maximum, E[S_max | Av_{n−1}(id_k)] = n e^{−s} = 16k²n²/(4n+k²)², interpolates between n at n = k²/4 (every position admissible: the constraint is void) and (k−1)² ≈ k² as n → ∞ (Regev: Av_n(I_k) ~ c (k−1)^{2n}n^{−(k²−2k)/2} gives s → ln(n/(k−1)²)); (vi) exact hook-length data (out/lis_k{4..9}.txt) approach the formula with O(1/k) corrections: at C = 1 the exact slopes 0.813, 0.735, 0.674, 0.630, 0.612, 0.583 (k = 4..9) extrapolate (a+b/k on k = 8, 9) to 0.45 vs the formula 0.446; at C = 3/4: 0.600, 0.486, 0.485, 0.449, 0.427, 0.403 vs limit 0.288.
We believe H_0 above is the function of Deuschel–Zeitouni (1999) (their H_0 contains the same ln(1+4/x²) terms); the coordinating session should compare with the paper before citing it as PROVED. In any case, for the purpose of the programme:

**Corollary 3.4.** For the identity the slope in the window is bounded above and below by constants depending only on C: s_id(n) → ln((4C+1)²/(16C)), which is 0 at C = 1/4, 0.118 at C = 1/2, 0.288 at C = 3/4, 0.446 at C = 1, 0.93 at C = 2, and ~ ln C − ln 4·… (precisely ln C + ln(1 + 1/(4C))²) for large C. It is increasing in C (log-concavity of p_id in n in the window), so the identity's slope is *smallest* just above its own threshold. Both W28's lower bound (for this one pattern) and W30's upper bound hold for the identity with A = e^{s_id} ≤ 1.6 for C ≤ 1.

## 4. General patterns: what is proved and what the data say

**Proposition 4.1 (prefix/suffix admissibility; PROVED).** Let π have its maximum at position j, α = st(π(1..j−1)), β = st(π(j+1..k)). For σ' ∈ Av_{n−1}(π) let τ_α(σ') = min{m : α ⊂ st(σ'(1..m))} and τ'_β = the analogous suffix time. Then S_max(σ') ≥ τ_α + τ'_β − 1 (positions p ≤ τ_α and p ≥ n − τ'_β + 1 are admissible), so
     s_π(n) ≤ ln n − ln E[ τ_α(σ') + τ'_β(σ') − 1 | σ' ∈ Av_{n−1}(π) ].
Hence s_π(n) = O(1) as soon as a uniformly random π-avoider of length n−1 needs, on average, Θ(n) steps before its prefix contains the sub-pattern α (or its suffix β). For the identity, α = I_{k−1}, and §3(v) is the statement E[τ_{I_{k−1}} | LIS ≤ k−1] = 16k²n²/(4n+k²)².
*Proof.* A new maximum at position p is the maximum of a copy of π only if the p−1 points to its left contain α and the points to its right contain β. ∎
Dead end (log.md §4): bounding Pr(τ_α ≤ m | π ⊄ σ') by block splitting (prefix ⊥ suffix) loses the factor p_π(n−1−m)/p_π(n−1) = e^{Θ(k²)} and gives nothing.

**Observation 4.2 (NUMERICAL, results.md §1; SMC with the exact generating-tree survival, validated against exact enumeration for n ≤ 11).**
For every class representative of S_4, S_5 and 16 patterns of S_6, 8 of S_7, the slope at n = Ck² lies within ±15 % of the identity's value at the same (k, C); it is increasing in n for every pattern (log-concavity in the window); its k-dependence at fixed C parallels the identity's (decreasing, O(1/k)); the largest slopes belong to the most "generic" patterns (246135, 13452) and the smallest to layered/near-layered ones (215436, 14325, 12435). The per-point rates I_π(1) lie in [0.26, 0.39] for all patterns tested (k = 4..7), decreasing slowly in k, consistent with I_π(1) = O(1) uniformly (Thm 2.3(ii)) and hence with the window-averaged slope being O(1). We found no pattern whose slope grows with k at fixed C.

**Observation 4.3 (NUMERICAL, μ-slope from the W24 dumps).** s_μ at the threshold (μ ≈ 1–10): 0.54–0.63 (k=5), 0.47–0.59 (k=6), 0.44–0.55 (k=7), 0.43–0.52 (k=8), 0.44–0.53 (k=9, noisy); increasing in n and essentially flat in k. Combined with Prop. 2.2(i) (average slope over the k² scale → 0) and Thm 2.3(iii), the picture is: ln μ(n) is ≈ 0.6 ln k! and nearly flat at n = 0.6k², bends down over the last ≈ k ln k points and crosses 0 with slope ≈ ½ — a slope of order 1 at the threshold and a total budget ln k! consumed over O(k ln k) points, both consistent with s_μ ≍ 1 exactly where W28 Cor. 1.2 needs it.

## 5. Summary of status
- Lower bound on the slope, per pattern, uniformly over the window: equivalent to the main conjecture (Thm 2.1) — not attempted.
- Lower bound needed by W28 Cor. 1.2: local (O(k)-length window), NUMERICALLY s_μ ≈ 0.5 for k ≤ 9, no proof; Prop 2.2 makes precise that it must be local, and Prop 2.5 shows it is expected to FAIL asymptotically (slope at the threshold Θ((ln k/k)^{2/3}) for a Tracy–Widom-type edge) — Cor 1.2 then needs a = o(k^{1/3}ln^{2/3}k) instead of o(k); a = O(1) remains fine.
- Upper bound: PROVED s_π ≤ ln(n/(k−1)) (Lemma 1.1, improves W30 Lemma 3.3 by ln(k−1), still not O(1)); PROVED that the window-average of s_μ is ≤ H_0(1/√C)+o(1) = O(1) (Thm 2.3(iii)); pointwise O(1) open, reduced (Prop 4.1) to a hitting-time statement for the prefix pattern under the avoiding measure.
- Identity: closed form s_id = ln((4C+1)²/(16C)) (Prop. 3.3; PROVED modulo the numerically established Poisson slope (1−y/2)² and standard Laplace asymptotics); corrects the naive DZ guess used in W28 §4 (H5), whose c' should read s_id ≈ 0.29 at C = 3/4.
