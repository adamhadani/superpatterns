# W24 — how loose is the union bound for random superpatterns?  (numerics, k = 5..9)

Date: 2026-08-29.  Question: W22 review §A item 2.  Tools/rerun: README.md.  Chronology: log.md.  Raw dumps: out/.

## 0. Setup and notation

σ_n uniform in S_n; M = #{π ∈ S_k : π ⊄ σ_n}; A_π = {π ⊄ σ_n}.  Then

    Pr(M > 0) = E[M] / E[M | M > 0],      R(n,k) := E[M | M > 0] = E[M] / Pr(M > 0) ≥ 1,

and ln R is exactly the additive error (in the exponent) of the union bound Pr(∃π ⊄ σ_n) ≤ Σ_π Pr(A_π) = E[M].
All A_π are decreasing events in the point set, so (Harris) the A_π are pairwise positively correlated and R ≥ 1.
Two readings of the same number: (i) R is the mean number of missing patterns of a random *non*-superpattern;
(ii) k!/R is the "effective number of independent absence events".

Estimators (analyze.py): R̂ = mean of M over the samples with M > 0; ln R̂ with a bootstrap SE (200 resamples).
Because M | M > 0 is heavy-tailed (see the histograms) R̂ is dominated by rare σ with huge M when Pr(M>0) is small;
the tables therefore also give the median, q10/q90/q99, the geometric mean of M | M>0, and "R w/o max" (R̂ with the
single largest sample removed).  t(k) = the n at which Pr(M>0) = 1/2 (interpolated), so R(t(k),k) = 2·E[M] there.

Sampler: mslack.c = the w5-random checker (exact set of contained k-patterns of each σ, bitset over k! codes, pruned
DFS), verified against a naive Python enumeration of all C(n,k) subsets on the *sets* of missing patterns (0 mismatches
on 43 permutations, k = 5,6,7).  Pattern codes are the w5 mixed-radix codes (patlib.py decodes them).
Samples per point: k=5: 20000–40000; k=6: 4000–30000; k=7: 3000–20000; k=8: 2000–10000; k=9: 300–3000 (1.5–2.5 s/σ).
