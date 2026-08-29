# W33 — slope of ln p_π(n) near the threshold: working log

## 0. Setup (t+0)
Read NOTES.md, W28 proof (Cor 1.2 needs slope of ln μ bounded BELOW by Ω(1) near threshold), W30 proof (Prop 3.2 needs
slope of ln μ bounded ABOVE by O(1) uniformly in k; Lemma 3.3 gives only ln n), W27 §0, W24 analysis.txt (E[M] columns).
Tools copied: ../w27-comparison/avoid2 (generating-tree exact enumeration and SMC). SMC inserts a new MAXIMUM into a
π-avoider of length m at each of the safe positions; the survival fraction tot/(pop (m+1)) is exactly
p_π(m+1)/p_π(m) (generating tree: every avoider of length m+1 arises once). So SMC measures the slope directly.

## 1. Identity: exact slopes (t+10)
lis_exact.c: p_id(n) = Σ_{λ ⊢ n, ≤k−1 rows} f_λ²/n! by hook lengths (log-doubles). k=2: s = ln n (exact, p=1/n!).
k=3: s = ln(n(n+1)/(2(2n−1))) (Catalan) — both reproduced. Files out/lis_k{4..9}.txt: n, ln p, s(n), E[T]=n e^{−s}
(= mean number of positions at which a new maximum can be inserted into a uniformly random avoider of length n−1,
= expected first time the prefix-LIS reaches k−1 — capped at n).
Observation: at fixed C = n/k² the slope DEcreases with k (C=1: 0.81, 0.73, 0.67, 0.63, 0.61, 0.58 for k=4..9).
My first guess for the DZ rate (H_0 = −1 + x²/4 + 2ln(2/x)) predicted s → ln(4C) — wrong: that H_0 has a
quadratic zero at x=2, incompatible with the Tracy–Widom left tail e^{−|s|³/12} (needs a cubic zero), and it
overshoots the exact rates by ×3. DEAD END, replaced by the Poissonized computation below.

## 2. Poissonized identity: Gessel determinant (t+25)
lis_poisson.py (mpmath, venv): Q_λ(ℓ) = P(L ≤ ℓ) for Poisson(λ) points = e^{−λ} det[I_{i−j}(2√λ)]_{ℓ×ℓ}, with
−d ln Q/dλ by central differences. Result (out/lis_poisson.txt): −d ln Q/dλ = (1 − ℓ/(2√λ))² to 3–4 digits at
ℓ = 10, 20 (x = 0.8: 0.3603/0.3601 vs 0.36; x = 1: 0.2506/0.2502 vs 0.25; x=1.2: 0.1614/0.1603 vs 0.16;
x=1.414: 0.0892/0.0866 vs 0.0858). Integrating: Poissonized rate H_P(x) = 1 − 2x + 3x²/4 + (x²/2) ln(2/x)
(matches the computed rates 0.0993/0.0974 → 0.0966 at x=1; 0.1751/0.1738 → 0.1732 at x=0.8).
Poissonization is NOT innocuous at speed n (the Poisson number of points tilts): de-Poissonize by a Legendre step
(proof.md §3) ⇒ fixed-n slope s_id(n) = 2 ln((4+x²)/(4x)), x = k/√n, i.e. s_id = ln((4C+1)²/(16C)) at n = Ck²,
and H_0(x) = −1 + x²/4 + (x²/2) ln((4+x²)/(2x²)) + 2 ln((4+x²)/(4x)), which has the correct x→0 asymptotics
2 ln(1/x) − 1 (from Av_n(I_{ℓ+1}) ≤ ℓ^{2n}) and a cubic zero at x = 2 (TW matching). The finite-k exact slopes
approach it with O(1/k) corrections (C=1: limit 0.446; data 0.58 at k=9, 1/k-extrapolation ≈ 0.45).

## 3. SMC slopes for general patterns (t+35..t+70)
queueA.sh / queueB.sh (2 cores): all 7 classes of S_4 (nmax 40, pop 3000, 2 seeds), all 23 of S_5 (nmax 40, pop 2000),
16 patterns of S_6 (nmax 58, pop 1500), 8 of S_7 (nmax 78, pop 1000). Cost: 1324 at nmax 40, pop 20000 took 91 s,
so populations were cut; SMC slopes validated against exact generating-tree counts (exact/, k=4 n ≤ 11, k=5 n ≤ 10):
agreement ±0.01 (out/analysis.txt bottom vs top). Wilf-equivalent classes (1234~1243~1432~2143, 1342~2413) give
identical exact slopes, as they must.
Result (out/analysis.txt): at fixed (k,C) the slope is nearly pattern independent (spread ±15 %), increasing in n,
decreasing in k like the identity; generic patterns slightly steeper than layered ones. No pattern with slope
growing in k. Rates I_π(1) ∈ [0.26, 0.39].

## 4. Dead ends
- Naive DZ rate −1 + x²/4 + 2 ln(2/x) (gives s_id → ln 4C): wrong (see §1); replaced by §2.
- Proving E[τ_α | Av(π)] = Θ(n) (Prop 4.1 of proof.md) by block splitting: Pr(α ⊂ prefix_m, π ⊄ σ') ≤ q_α(m) p_π(n−1−m)
  loses e^{Θ(k²)}; the conditioning cannot be discarded. Harris/FKG-type positive correlation of the decreasing events
  {α ⊄ prefix} and {π ⊄ σ'} would suffice for E[τ_α | Av] ≥ E τ_α (unconditional threshold of α ≍ |α|²) — but
  S_n is not a product space and no such inequality is available; noted as the natural next target.
- A uniform lower bound on s_π over the whole window is equivalent to CP*/Alon (Thm 2.1) — not attempted.
- "Boundary insertions cannot beat ln(n/4)": FALSE reasoning — the generating tree (new maximum only) is exact,
  Av_n = Σ S_max; the slot count is n·Av_n. Kept only the correct form (Lemma 1.1).
- μ-slope lower bound over a k²-window: impossible (Prop 2.2(i)), since μ ≤ k!; only a window of length O(k ln k)
  below the threshold can carry slope Θ(1).

## 5. Asymptotic caveat found late (t+75)
Using the closed form: the identity's slope at the point where p_id = 1/k! is 0.44, 0.22, 0.08, 0.025 at
k = 10, 10², 10³, 10⁴ → Θ((ln k/k)^{2/3}) (cubic TW edge). Hence "s_μ = Θ(1) at the threshold" (W28 Cor 1.2) is
pre-asymptotic unless the extremal patterns have a kinked rate function; proof.md Prop 2.5 gives the scaling and the
corrected requirement on a (a = o(k^{1/3} ln^{2/3} k) for γ = 3). Exact k=10 identity run added (out/lis_k10.txt);
1/k-extrapolations of k = 9, 10 slopes: 0.157/0.255/0.435 at C = 0.5/0.75/1 vs formula 0.118/0.288/0.446.
