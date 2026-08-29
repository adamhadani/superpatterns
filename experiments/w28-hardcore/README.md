# W28 — hard-core / cluster reduction of the union bound

Question: W24 found ln R ≈ 0.7k for R = E[M]/Pr(M>0) (M = #missing k-patterns of a random σ_n) at the median
threshold t(k). Why is the union bound off by only e^{O(k)} and not e^{Θ(k ln k)}, and can it be proved?
Answer in `results.md` (tables, verdict) and `proof.md` (Thm 1.1 second-moment/witness criterion; ES disjointness;
structured families; heuristics H1–H5 for what a proof needs). Chronology and dead ends: `log.md`.

Data: the W24 dumps `../w24-union-slack/out/k{K}_n{N}_s11.txt` (one line per σ_n: `M c1 c2 …`; `patlib.decode(c, k)`
gives the pattern). Only new sampling: 6000 σ at k=7, n=37 with σ dumped (msigma, seed 21, ~5 min, 1 core) for Table 5; the rest is post-processing (numpy, single core, < 15 min total).

Files
- `hardcore.py K [n …]` — Tasks 1–3 tables for one k: law of M (μ, Δ = E M(M−1), Bonferroni binomial moments,
  Janson exponent, μ²/E M²), per-pattern p_π statistics (LIS/LDS/runs/distance to monotone, top-1 % share),
  cluster structure of the missing set (components under adjacent transpositions and under one-point moves,
  greedy (k−1)-pattern cover), Λ_π = E[M | π ⊄ σ_n] over π, id/rev co-miss counts.  → `out/k6.txt`, `out/k7.txt`.
- `hardest.py K n [N]` — hardest/easiest patterns, dihedral spread of p_π, and the null comparison (random subsets
  of S_k of the same size) for the cluster statistics.  → `out/k{K}_n{n}_hardest.txt`.
- `bigM.py K n` — anatomy of events by size of M: fully-missing (k−1)-patterns and how much of M they explain,
  max(LIS,LDS) of the missing patterns, cover/M.  → `out/k{K}_n{n}_bigM.txt`.
- `msigma.c` — mslack.c with the output line changed to `M | σ_1 … σ_n` (σ dumped, codes not); `./msigma K N SAMPLES SEED`.
  → `out/k7_n37_sigma_s21.txt` (6000 σ, independent seed).
- `defect.py K n` — per-σ largest empty rectangle, min cell counts (3×3, 4×4), LIS/LDS, grouped by M; Spearman
  correlations with M.  → `out/k7_n37_defect.txt`.
- `tail.py` — tail of M | M>0 and ln R, ln(E M²/μ) at t(k) for k = 6..9 (M lists only).

Rerun
```
python3 hardcore.py 6 > out/k6.txt; python3 hardcore.py 7 > out/k7.txt        # ~1 min / ~6 min
python3 hardest.py 6 28 400 > out/k6_n28_hardest.txt; python3 hardest.py 7 37 400 > out/k7_n37_hardest.txt
python3 bigM.py 6 28 > out/k6_n28_bigM.txt; python3 bigM.py 7 37 > out/k7_n37_bigM.txt; python3 bigM.py 7 33 > out/k7_n33_bigM.txt
python3 tail.py
cc -O3 -march=native -o msigma msigma.c && ./msigma 7 37 6000 21 > out/k7_n37_sigma_s21.txt   # ~5 min
python3 defect.py 7 37 > out/k7_n37_defect.txt
```
