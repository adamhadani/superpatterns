# W33 — slope of ln p_π(n) and ln μ(n) near the threshold n ≈ 0.75k²

Question (from W28 Cor 1.2 and W30 Cor 3.4): is s_π(n) = ln p_π(n−1) − ln p_π(n) bounded above (W30 needs it) and
below (W28 needs it) by absolute constants for n ∈ [ck², Ck²], for every π ∈ S_k or on μ-average?

Answer in brief: lower bound uniformly over the window ⟺ the main conjecture (proof.md Thm 2.1), and for μ it can only
hold on the last O(k ln k) points (Prop 2.2) — where the data give s_μ ≈ 0.5 for k = 5..9. Upper bound: proved
s_π ≤ ln(n/(k−1)); proved O(1) on window average for μ; pointwise O(1) open but strongly supported numerically (slopes
0.2–1.2 for C ∈ [0.5, 1.5], nearly pattern-independent, decreasing in k). Identity in closed form:
s_id → ln((4C+1)²/(16C)) with the LIS lower-tail rate H_0(x) = −1 + x²/4 + (x²/2)ln((4+x²)/(2x²)) + 2ln((4+x²)/(4x)).

Files: proof.md (statements/proofs, tagged), results.md (tables), log.md (chronology and dead ends).
Code: lis_exact.c (exact p_id(n) via hook lengths; `./lis_exact k nmax`), lis_poisson.py (Poissonized Gessel
determinant, needs mpmath: `.venv/bin/python lis_poisson.py 10,20 0.8,1.0`), avoid2 (= W27's generating-tree
exact/SMC tool), run_smc.sh + queueA.sh/queueB.sh (drivers), analyze.py (slope tables → out/analysis.txt).
Data: out/lis_k{4..9}.txt, out/lis_poisson.txt, out/mu_slopes.txt (from ../w24-union-slack/analysis.txt),
smc4/ smc5/ smc6/ smc7/ (SMC dumps "n p ln p"), exact/ (exact Av_n(π), k=4 n≤11, k=5 n≤10).
