# W28 — hard-core / cluster reduction of the union bound (log)

Date: 2026-08-29, start 18:50. Dir: experiments/w28-hardcore/. Machine load ≈ 10 on start; I use ≤ 2 processes.
Data: W24 dumps experiments/w24-union-slack/out/k{6,7}_n*_s11.txt (missing sets of random σ_n; codes via patlib.decode).

## Chronology
- 18:50 read NOTES/W22/W24/W27. Observations before any computation:
  * Δ := Σ_{π≠π'} Pr(both missing) = E[M(M−1)] exactly (every pair is dependent), and the Bonferroni truncations are
    the binomial moments E C(M,j): Pr(M>0) = Σ_j (−1)^{j+1} E C(M,j). So Task 1 needs only the law of M, not the
    5040×5040 co-miss matrix. (Matrix still computed for the per-π conditional expectations.)
  * Erdős–Szekeres: n ≥ (k−1)²+1 ⇒ σ contains I_k or D_k. (k−1)²+1 = 26 (k=6), 37 (k=7): the W24 "never co-miss"
    observation for identity/reverse at t(7)=37 is a THEOREM, not a correlation (task 3(iii)).
  * Cauchy–Schwarz: Pr(M>0) ≥ μ²/E[M²] ⇒ R ≤ E[M²]/μ = Σ_π p_π E[M | π⊄σ] / μ ≤ max_π E[M | π ⊄ σ_n].
    W24 numbers: E[M²]/μ = 20.8, 78, 511 at t(k), k = 6,7,9 (ln: 3.04, 4.35, 6.24 ≈ 1.05k) vs ln R ≈ 0.7k.
    So the second-moment route ALREADY gives e^{O(k)} numerically; the question becomes why max_π E[M | π⊄σ_n] = e^{O(k)}.
- 18:55 hardcore.py written and run for k=6 (all n) and k=7 (all n) (out/k6.txt, out/k7.txt). Findings:
  * Table 1: Janson void everywhere (Δ/μ = 20–430), Bonferroni order 2 negative / order 3 > 1 for all n ≤ 0.9k²;
    ln Pr(M=0)/(−μ) = 0.22 (k=6), 0.11 (k=7) at t(k), → 1 only at n ≥ 1.05k². Second moment: R ≤ E M²/μ = 20.8 / 78.
  * NO hard core: p_π flat within ×4 over S_k; top 1 % of patterns carries 1.8 % / 2.4 % of μ; near-monotone classes
    only 1.25–1.5× mean. Hardest patterns are layered/co-layered (1543276, 7234561, 7456231), identity is not the
    hardest at k = 6, 7 (p_id/max p = 0.74 / 0.86).
  * corr(p_π, E[M | π⊄σ]) = −0.75 / −0.43: hard patterns are missed alone, generic ones in bulk.
- 19:05 hardest.py (null comparison) and bigM.py (anatomy by M). Missing set given M>0: one diffuse one-point-move
  component (1.2–1.4 components vs 2.5–5.5 null; largest component 92–94 % of M); NOT the up-set of fully-missing
  (k−1)-patterns (they explain < 1 % of M for M < 100, 32 % for M ≥ 300); large clusters made of MORE generic patterns
  than singletons (max(LIS,LDS) 4.0 vs 4.29). Greedy cover ≈ M^{0.6}: each weak (k−1)-pattern loses 3–9 of 37 extensions.
- 19:10 tail.py: R is made in the far tail; share of Σ M from M ≥ 256 = 0, .07, .29, .48 (k = 6..9); local tail exponent
  < 1 up to m ≈ e^{0.7k}, then steepens. ln R = 1.76, 2.54, 3.11, 3.65; ln(E M²/μ) = 3.04, 4.35, 5.46, 6.11 (k = 6..9).
- 19:00 proof.md (Thm 1.1 witness/second-moment criterion + Cor 1.2 "threshold constant = first-moment constant
  under R = e^{o(k²)}"; Thm 2.1 Erdős–Szekeres; Props 3.1–3.3; witness-bound-not-tight example; heuristics H1–H5),
  results.md, README.md, experiments/README.md row.

- 19:05 H5 test: msigma.c (= mslack.c printing σ instead of the missing codes) run for k=7, n=37, 6000 σ, seed 21
  (independent of the W24 sample); defect.py computes per σ the largest empty axis-parallel rectangle, the min cell
  count of 3×3 and 4×4 grids, LIS, LDS. Result (results.md Table 5): M is driven by emptiness (Spearman +0.41 with the
  largest empty rectangle; 98 % of M ≥ 100 events have an empty 4×4 cell vs 41 % at M = 0) and not by small LIS/LDS
  (Spearman +0.11). Done 19:15; writing finished 19:25.

## Dead ends (with reasons)
1. Janson / Suen / Brun sieve / Bonferroni at any order ≤ 3: all void because M | M>0 is heavy-tailed (E C(M,j) grows
   like a j-th moment); confirms W22's Δ ≥ μ²/C cap from the data side. Only the second moment (no correlation
   inequality needed) survives — Thm 1.1.
2. "Hard core = near-monotone patterns (LIS or LDS ≥ k − j)": refuted; share of μ from max(LIS,LDS) ≥ k−1 is 9 % / 2 %
   (uniform 7 % / 1.5 %). Prop 3.2 gives R_F ≤ e^{2j ln k} for such families for free, but they carry no weight.
3. Hierarchical model "a missing (k−1)-pattern drags its k² extensions": refuted by bigM.py; also the level cost
   μ_{k−1}(n)/μ_k(n) ≈ e^{−6.8} at k=7, n=37 exceeds the k² = e^{3.9} gain.
4. Using max_π Λ_π as the criterion: not tight in general (rigid-row counterexample in proof.md §3) and 1.8–2.2× above
   E M²/μ in the data; the p-weighted average is the right object.
5. Erdős–Szekeres negative dependence of LIS/LDS events: exact, but propagates to nothing beyond the two monotone
   patterns (implication direction is wrong): factor 2 at most.
6. Deciding e^{0.7k} vs e^{0.23 k ln k} from k ≤ 9: impossible (increments of ln R per unit k: 0.66, 0.68, 0.71 — both
   fits within noise; a fixed power of k is rejected, the log-log slope rises 4.3 → 6.0).
7. The "why e^{Θ(k)}" question is NOT settled: the monotone (small-LIS) mechanism is provably too weak (H5), so the
   clusters come from local defects of σ; counting patterns killed by one scale-1/k defect is the missing step.
   Would need the σ's themselves (not dumped by W24) — a follow-up should dump σ for the M ≥ 100 events and look at
   the empty rectangles / cell counts of the point set.
