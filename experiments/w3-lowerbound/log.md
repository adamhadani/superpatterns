# W3 lower bound — log (2026-08-29)

## 0. Reading
- CKS: encode π by (I, (t_j)_{j∉I}, (π(i))_{i∈I}); I ⊆ even indices with width b_i=t_{i+1}-t_{i-1} ≥ dn/k, |I|=ck.
  Constant comes from: per-index gain log(d/e^2) (~0.10 nats at d=8.18) times c=0.00075 → log λ ≈ 7.6e-5.
  Their Case-1 Chernoff forces c ≈ 0.27·p(d)/2 where p(d)=e^{-d}(1+d) = P(Gamma(2) ≥ d): most large widths are wasted.

## 1. Key reformulation (Track A)
Let I(T) be ANY rule choosing a non-adjacent index set that is *stable*: I(T) depends only on T|_{I(T)^c}
(equivalently, every T' agreeing with T off I(T) has I(T')=I(T)). Then, by double counting extensions,
   #patterns(σ) ≤ Σ_T  k!/(k-|I(T)|)! · Π_{i∈I(T)} 1/(b_i(T)-1)     (*)
No case split, no threshold parameter: include i iff factor k/(b_i-1) < 1. The "Case 1" large-deviation
is absorbed automatically because (*) is an expectation of a product (Chernoff-tight after tilting).
Stable rule with both parities: I_even = {even i: b_i-1>k}; I_odd = {odd i: b_i-1>k, i±1 ∉ I_even}.
Sum constraint Σ gaps = n+1 handled by an exact Chernoff/geometric tilt:
   Σ_T W(T) ≤ x^{-(n+1)} (x/(1-x))^{k+1} E_{Geom(x)^{⊗(k+1)}}[W]   for every 0<x<1.
Even-only: even widths are i.i.d. under the product measure → E[W] = (E f(a+a'))^{(k-1)/2} exactly.
Both parities: 2-dependent → transfer operator (numerics) or Hölder splitting (rigorous, small loss).

## 2. Track A results (trackA.py, verify.py, mc_both.py, holder_opt.py; proof in proof.md)
- Closed forms: E min(1,θ/B), B~Gamma(2) = 1-e^{-θ};  discrete: E_x min(1,k/(a+a'-1)) = 1-x^k EXACTLY (geometric gaps).
  => even-only bound is a fully explicit finite-k inequality: pat(σ) ≤ x^{-(n+1)}(x/(1-x))^{k+1}(1-x^k)^{(k-1)/2}.
- Constants (log λ*):  CKS 7.6e-5 | even-only (rigorous) 3.125e-4, λ=1.0003125 | both parities Hölder p=1.6
  (rigorous mod continuum limit) 3.85e-4, λ=1.000384 | both parities exact rate (MC-verified) 4.37e-4, λ=1.000437.
- Tilt optimum τ*≈0.9977 (2nd-order effect ~3e-6). (k-r)/k refinement in k!/(k-|I|)! worth ≈ p²/2 ≈ 1e-5, not used.
- Dead end: runs of adjacent dropped indices (encode j consecutive values, span S): j-th index gains
  log(S/k) - log j - ..., needs S > 2k already for j=2 → runs never pay; non-adjacent is right.
- Surprise: odd-index deficit (2.4e-4) ≪ even deficit (6.2e-4) because a large width is usually one big gap,
  shared by two adjacent widths; only one can be used. So "both parities" gives 1.4x, not 2x.
- Hölder loss 3.85e-4 vs 4.37e-4: inherent to squaring; closing it needs certified transfer-operator numerics.

## 3. Track B (slots_test.py, trackB_patcount.py)
- Max #distinct k-patterns over σ∈S_n (exhaustive n≤8, hill-climb n≤15): ratios maxpat/C(n,k):
  (8,4) 23/70=.33  (8,5) 41/56=.73  (9,5) 71/126=.56  (10,5) 93/252=.37  (12,6) 398/924=.43  (13,6) 511/1716=.30
  (14,6) 610/3003=.20 (15,6) 679/5005=.14. Too small to read off an exponential rate; ratios drop fast as n grows
  past sp(k) (k=6: sp=17, C(17,6)=12376 vs 720 → ratio ≤ .058 at the superpattern length itself).
- "Nonempty slots" mechanism: #patterns from moving t_i in its window = #value-slots hit by σ(J), N ≤ min(k,b-1).
  For ANY σ: boundaries are σ at ~uniform random positions, P(gap g split) ≤ 1-e^{-gk/n}, gaps sum ≤ n, concavity ⇒
  E[N|J] ≤ 1+(b-2)(1-e^{-k/(b-2)}).  Verified on real σ: sp(6)=17: mean N/(b-1)=0.77 (CKS-type 0.96, Jensen 0.84);
  random σ 0.69; identity 0.35; grid16 0.51 (Jensen 0.61). Single-index version only gives a constant factor
  ≤ 1-E[e^{-e²/G}] ≈ 0.95.
- Multi-index version: for |I|=ck, #pat(ext S) ≤ Π_r (N_{i_r}(S)+r-1) — the "+r-1" costs ~1.85c² in rate vs
  gain c·g with g = E[-log(1-e^{-e²/G})] ≈ 0.052 → heuristic net ≈ g²/7.4 ≈ 3.7e-4 (comparable to Track A) BUT
  unproved: need E[Π_i N_i] ≲ Π E[N_i]; separations of value-gaps of different windows are NOT negatively
  associated when value intervals nest. Combining with large-width selection (b>k: N ≈ 0.63k instead of k, i.e.
  extra 0.46 nats per selected index) could give ~2e-3 heuristically. This is the most promising new direction.
- EELW obstruction: any bound >k²/4 must use worst-case patterns; not attacked (time).
