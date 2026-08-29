# W7 — value-slot refinement (2026-08-29), ~90 min

Goal: make Track B's "nonempty value-slot" idea rigorous or find the precise obstruction. Result: Theorem C, λ_C = 1.00483.

1. Lemma 1' (slot encoding). N(ψ) = #patterns from ext(ψ) ≤ Π_j min(M_{ι_j}+j−1, k, b−1): sequential insertion of the
   I-values into the sorted off-I values V; the j-th inserted value sees V plus j−1 earlier ones, and a fixed window's
   slot count grows by ≤1 per added value. M_i depends only on ψ (V = off-I values), so the extension sets stay disjoint
   (stability unchanged: rule depends on odd positions). Exact check on sp6, sp7 witnesses, random S_17, ζ_5, ζ_6
   (lemma_check.py): holds; RHS is 0.55–0.92 of Lemma 1's.

2. Obstruction to E[Π N_i] ≲ Π E[N_i]: N_i are increasing functions of the common off-I position set ⇒ FKG gives ≥,
   NA fails for nested windows (comb permutations make all windows comonotone); Hölder on Σ_{i∈S}(N_i−1) shows joint upper
   tails can be as bad as one window's. So no product/independence statement is available for arbitrary σ.

3. Way around: don't factor. (i) Represent the tilted sum as E over T(B) = first k points of a Bernoulli(q) process B
   (geometric gaps ⇔ Bernoulli sites): Σ_T W ≤ x^{−(n+1)}(x/(1−x))^{k+1} E_B W(T(B)). (ii) Dominate off-I values by
   σ(B \ [lo,hi]) ∪ {σ(lo),σ(hi)}: M_i ≤ M̌_i+2, and M̌_i − 1 = Σ_ℓ 1[B ∩ A_ℓ ≠ ∅] over DISJOINT position sets A_ℓ
   (positions of values between consecutive window values) ⇒ independent indicators, independent of B∩[lo,hi], mean
   ≤ m(b) = (b−2)(1−x^{(n−b−1)/(b−2)}) by Jensen, uniformly in σ. (iii) Chernoff per window + union bound over
   (i, lo, hi): costs a factor e·n·q ≈ k² only. (iv) On the good event W ≤ W_good (function of widths only, i.i.d. even
   widths ⇒ computable); off it W ≤ 1. The "+j−1" cost r²/(2c) is handled by Legendre duality (rate) or an exact DP
   over r (finite k).

4. Numbers (rate.py): optimum τ=0.9774, β̄=0.594 (select even widths ≥ 0.59k — far more aggressive than b>k),
   ε=0.149; R_good = R_bad at the optimum; λ_C = 1.004829. ε=0 heuristic ceiling of the same computation: 1.0117.
   Width-dependent ε (rate2.py): 1.00501 (not adopted).
   finite_check.py (exact (C), DP, truncation tails added): λ=1.004: rate −3.99e-4 at k=30001, −6.77e-4 at k=100001
   (limit −8.2e-4); positive at k=10001 (+2.8e-4) because of the k² union-bound factor. λ=1.0048 positive up to 1e5.
   Bug found on the way: floating "1−ΣP" tail (5e-12) swamped the e^{−500} terms; replaced by exact geometric tail.

5. Not done: both parities (Theorem-B style Hölder), keeping Π f(b_i) on the bad event, exact Poisson-binomial LDP
   instead of Chernoff, certified interval arithmetic for the finite-k certificates.

6. ERROR CAUGHT BY COORDINATOR (after first write-up). My first Lemma 1' capped each factor by min(M_j+j−1, k, b_j−1).
   The cap b_j−1 is FALSE: the number of achievable s_j given a prefix (s_1..s_{j−1}) is NOT bounded by the number of
   window positions, because different realisations of the same prefix (different values v_l in the same V-slot) put a
   fixed window position into different slots (coordinator's example: sp6, k=6, β=5, I={2,4}, off-I (1,6,11,16),
   V={4,6,9,17}: bound 8, class has 9 patterns). My original lemma_check.py only tested the SUMMED inequality
   pat ≤ Σ_T W(T), which is far weaker and hid the error. Corrected statement: N(ψ) ≤ min(Π_j(b_j−1), Π_j min(M_j+j−1,k)),
   proof via: given the prefix, the V-slot c_l of every earlier v_l is determined, so s_j = c + #{l: c_l<c} + (0..n_c),
   giving ≤ Σ_{c hit}(1+n_c) ≤ M_j + j − 1 values. Per-class brute force added (lemma_check.py → lemma_check_out.txt):
   corrected bound has 0 violations on sp6, sp7, random S_17/S_14, ζ_5, ζ_6 for all β; the old bound is violated in up to
   1273 classes. Theorem C propagated: W_good := min(1, Π_j min((1+ε)m+j+2,k)/(b−1)); "off G, W ≤ 1" now justified by
   N(ψ) ≤ |ext ψ| (product cap), stated explicitly. Numerics: rate.py never used the per-factor cap, so λ_C = 1.00483 is
   unchanged; finite_check.py with corrected weights gives identical certificates to the printed digits (the cap was
   inactive at β ≈ 0.59k where (1+ε)m(b)+j+2 ≈ 0.99(b−1) for typical j). Lesson: per-class checks, not summed checks.
