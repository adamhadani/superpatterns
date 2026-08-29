# W23 — certificate counting for absence of periodic / block-grid patterns

Files: `proof.md` (statements tagged PROVED/HEURISTIC/NUMERICAL with proofs), `log.md` (plan, analysis,
dead ends), `tg.c` (copy of W11's exact fixed/free containment DP), `runjobs*.sh`, `analyze*.py`,
`out/fix*.txt` (raw: `r h N reps found exact_notfound unknown`).

## Results in one paragraph

1. **Identity (Thm 1.1).** Dilworth certificates give the *exact identity*
   Pr(LIS < k) ≤ Σ_n N!/Π(n_i!)² ≤ (N+k)^k (e(k−1)²/(N−k+1))^N, i.e. rate ln(C/e) at N = Ck².  Against the
   Deuschel–Zeitouni rate H(1/√C) the loss δ(C) = H − ln(C/e) is 0.60 at C = e, 0.23 at C = 10, 0.034 at
   C = 100 and O(C⁻¹ ln C): the bound is asymptotically exact for large C, and for fixed k the loss is only
   polynomial in N (exactly N+1 for k = 3).  Canonical (patience) covers cannot push e down without RSK
   (Prop 1.5): the union over pile sequences is an identity.
2. **Fixed strips, periodic word (Thm 2.1).** With a general grid (αm column groups, βm rows per strip)
   the Mirsky/box certificate gives, for C > αβ ln(e/f), f = 1/r − 1/(rα) − 1/β,
   Pr(π_w ⊄_fix Π_N) ≤ exp(−(fN/r)(1 − αβ ln(e/f)/C)); e.g. C > 9r ln(3er) ⇒ ≤ exp(−(N/(3r²))(1 − 9r ln(3er)/C)).
   This improves W11 Thm 2.2 by a factor r in the speed (N/(3r²) vs N/(4r²(r+1))) and by a constant in the
   threshold (9r ln(3er) vs 8(r+1) ln(2er²(r+1))); the same holds for all of 𝒢(r,h) at fixed strips with
   threshold 9r ln(3er²) (Cor 2.1′).
3. **Floor (Prop 2.3).** Every "bad boxes ≤ fM ⇒ containment" lemma has f ≤ 1/r (half-kill blocks), and the
   binomial tail is then vacuous unless each box holds > ln r points, so C ≥ ln r − o(1) for any Mirsky-type
   grid: **the threshold cannot be made r-independent by any deterministic-tolerance certificate**.  The
   remaining gap (ln r vs 9r ln r) is Mirsky's factor-r loss on product orders.
4. **Speed cap (Prop 2.4).** Pr ≥ e^{−N/r} for all C, so the fixed-strip rate is ≤ 1/r for every C and a
   bound of the form exp(−N(ln C − f(r))) is impossible in the fixed model; the free model has rate ≥
   ln(C/e) from the identity alone (§3) but that is useless for the union over the residual class.
5. **Randomness-exploiting certificates (§2.5)** — molecule antichain covers (entropy n^r), greedy/thread
   certificates (speed k), point-level layerings (entropy ln k per point) — all fail, with reasons.
6. **Numerics (§4).** Exact fixed-strip absence probabilities (tg.c, 2·10⁵ samples) for r = 1,2,3, k = 12–30,
   C = 0.3–0.7: for r = 2, 3 the empirical rate −ln P/N is already k-independent at k = 12–24 (speed N),
   ≈ (0.4–0.8)/r × the identity's rate at the same C, and far below the cap 1/r; the identity's rate drifts
   down towards the Deuschel–Zeitouni value.  Theorem 2.1's regime (C > 9r ln(3er) ≈ 50) is not simulable.

## What this means for Alon's conjecture
For Theorem 8's residual class (r ≤ ln⁴ k) the certificate route gives n = O(k² · r ln r) = k² polylog k —
the same order as W11, with better constants; the ln r floor (Prop 2.3) shows that no box/certificate
argument of this kind can reach n = O(k²) for the class, and an r-independent threshold with speed N
needs a genuinely new certificate encoding the r-dimensional Pareto front of the exact DP.
