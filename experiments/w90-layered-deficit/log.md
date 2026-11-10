# W90 log — layered patterns vs the identity (10 November 2026)

Chronology of the session, including the dead ends. Statements and proofs are in `proof.md`; every number below
points to a file in `out/` or to a command.

## 0. Why this workstream exists

The session started as a review of the repository. Reading the ledger showed two eras: the careful one (W1–W42,
through 10 September) and a burst (W43–W89, 22–27 September) whose headline in `memory/SESSION-STATE.md` claims a
complete proof of Alon's conjecture, while later rows of `memory/RESULTS.md` and the working copy of
`output/arxiv/main.tex` retract parts of it. In particular the repo simultaneously contained
"c₂₁ = 1.0000 identically" (W50) and the rigorous window 0.7866 ≤ c₂₁ ≤ 1.140 (W12/W17). Since Alon's conjecture
needs c₂₁ ≥ 1 and the pattern 21^{⊕m} has LDS = 2, the question "is c₂₁ = 1?" decides both the W50 claim and the
"bounded-LDS sharp threshold" theorem (W51/W52). That made it the natural first thing to settle.

## 1. Exhaustive comparison of L₂₁ with ⌊LIS/2⌋  (`exact_dist.c`)

Motivation: W10's table shows j·L_τ − LIS within a few units for every τ ∈ S₂…S₅ at N = 10⁴–10⁵ (with tens of
samples). For τ = 12 this is pointwise; for τ = 21 it suggested a distributional identity.

Result: #{σ ∈ S_n : L₂₁ = m} = #{σ : ⌊LIS/2⌋ = m} for every m and every n ≤ 8. First difference at n = 9, m = 3,
by exactly one permutation; 66 at n = 10; 2565 (+2 at m = 4) at n = 11; 77232 (+213) at n = 12.
Files: `out/exact11.txt`, `out/exact12.txt`; n ≤ 10 printed by the command in `proof.md` §6.

Interpretation found afterwards: 21^{⊕2} = 2143 is Wilf-equivalent to 1234 (Backelin–West–Xin); 214365 is
equivalent to 124356 (flip the two end blocks) but not to 123456 — the same phenomenon as 1324 vs 1234.

Dead end 1: I first hoped L₂₁ and ⌊LIS/2⌋ were equidistributed for all n (which would give c₂₁ = 1 exactly).
False from n = 9 on. The Backelin–West–Xin exchange only applies to the block at an end of the direct sum.

## 2. Fast exact L₂₁ and the paired statistic  (`l21_paired.c`)

Sweep algorithm: thresholds F(1) < F(2) < … (least top of a j-chain so far), pending apexes (lo, hi) per level.
A new value v at level j completes the pending apex with the smallest hi among those with lo < v < hi, setting
F(j+1) ← min(F(j+1), hi); then v becomes a pending apex (F(j), v). Only the top level of an apex matters.
Validation: `l21_paired n 20000 seed v` for n ∈ {4, 6, 8, 10, 12, 16, 24, 40, 60}: 0 mismatches against the O(n³)
dynamic programme on 180 000 permutations. Speed: 0.075 s per permutation at n = 10⁶.

First surprise: at n = 10⁶ the mean of L₂₁/√n is 0.990, not the 0.98655 "certified" in W50 (that number is a
Monte Carlo lower confidence limit from a handful of samples; see the audit in `memory/AUDIT-2026-11-10.md`).

Paired runs (`run_paired.sh`, 7 workers, files `out/l21_n*_w*.txt`, table by `aggregate.py`):

    n         samples   E[LIS]      E[L21]     E[2L-LIS]   D=E[2fl-2L]   D/sqrt(n)
    1000      700000    58.1748     28.8003    -0.5742     0.0736        0.00233 ± 0.00013
    10000     420000    192.2978    95.7774    -0.7429     0.2412        0.00241 ± 0.00008
    100000    140000    620.9003    309.8561   -1.1880     0.6881        0.00218 ± 0.00007
    1000000   28000     1982.8267   990.0109   -2.8049     2.3035        0.00230 ± 0.00007
    10000000  2800      6298.9221   3145.7750  -7.3721     6.8821        0.00218 ± 0.00011
    100000000 150       19960.8067  9969.6467  -21.5133    20.9600       0.00210 ± 0.00022   (run_followup.sh)

After n = 10³, 10⁴ I fitted two three-parameter models to the first three points to see what would distinguish
them: D/2 = A√n + B n^{1/6} + C predicted D(10⁶) ≈ 1.98, D(10⁷) ≈ 5.9; D/2 = B n^{1/3} + C n^{1/6} + E predicted
1.78 and 4.3. Observed 2.30 ± 0.07 and 6.88 ± 0.34: the n^{1/3} model is excluded; the data are a pure √n law.
With the n = 10⁸ batch added afterwards (prediction of the √n law: 22.7; of the n^{1/3} model: ≈ 10; observed
21.0 ± 2.2): weighted mean D/√n = 0.002269 ± 0.000036, χ² = 7.1 on 5 d.o.f.; log–log slope 0.491 ± 0.006.

Why earlier workstreams could not see it: W40 had 64 hosts at n = 4096 (standard error 0.4 on 2L₂₁, effect 0.15);
W10 had 6–48 hosts per N (standard error ≈ 1, effect 0.24–0.7).

## 3. Independent cross-check  (`crosscheck_w40.py`, `run_crosscheck.sh`)

numpy PCG64 permutations; L₂₁ from W40's `pruned.c` (segment tree, written 10 September by a different session)
and from `l21_paired.c --stdin`; LIS by Python `bisect`. Files `out/cross_n*_s*.txt`.

    n=10000    samples=72000  L21 mismatches=0  LIS mismatches=0  D=0.2379 ± 0.0189
    n=100000   samples=9000   L21 mismatches=0  LIS mismatches=0  D=0.7740 ± 0.0813
    n=1000000  samples=240    L21 mismatches=0  LIS mismatches=0  D=3.38 ± 0.80

## 4. The mechanism  (`verify_fibers.py`, `skew_boards.py`)

Thinking of 21^{⊕m} as built block by block gave a Markov chain on staircase regions, and Backelin–West–Xin says
its one-point functions coincide with those of the Hammersley (LIS) chain; the deficit had to come from two-point
correlations. Making that precise led to the fibre decomposition of `proof.md` §2: given the points outside the
skew region U ∩ S the inside points are a uniformly random valid filling; "contains α⊕12⊕β" means "not the
decreasing filling" and "contains α⊕21⊕β" means "has a D-inversion". Two sorting arguments give Theorem 1.

Literature check (web search, 10 Nov 2026): the skew-shape statement is Jelínek–Karpilovskij (DMTCS 2021,
arXiv:2002.12308), who also conjecture the size-k analogue and say it is known only for k ≤ 2; the transversal
prototype is Burstein–Pantone (arXiv:1402.3842), extending Bóna. Searches for the asymptotic statement about
random permutations or a counterexample to Alon's conjecture via layered patterns returned nothing. The August
2026 paper arXiv:2608.19050 ("Online Permutation Embedding: Optimal Stopping and Scaling Laws") notes that the
increasing permutation is not extremal online and states the dichotomy "either online and offline have different
extremisers, or Alon's conjecture and its weakening do not hold"; the present data point to the second branch.

`skew_boards.py` enumerates all boards S ∩ U ⊂ [N]²: the smallest board with two D-inversion-free fillings is
N = 3, the 3×3 square minus its lower-left and upper-right cells (fillings 321, 231, 312; the last two are
D-inversion-free). `verify_fibers.py` recomputes everything from the definitions for seven (α, β) and all σ ∈ S_n,
n ≤ 8 (n ≤ 9 for (21, 21)): all assertions pass (`out/verify_fibers_n8.txt`, `out/verify_fibers_n9_21_21.txt`).
At n = 9 the single extra avoider of 214365 comes from exactly one fibre of type (3 points, 3 fillings, a = 2).

Dead end 2: I looked for a slick route from "strict at every finite n" to "strict in the limit" (superadditivity of
the deficit; stationary Hammersley with sources and sinks; sparse swaps plus relaxation between them). None closes:
the deficit is a difference of two superadditive quantities; sources on the axes break the uniform-filling
property of fibres that touch the boundary; and every formulation needs a lower bound on the probability of a
marginal region made of one defect lens plus harmless lenses. The useful reductions that came out of it:

 * E[X − Y] at a stage equals Σ_b P(the level-b filling is D-inversion-free and is not the canonical one);
 * a fibre whose board has an isolated 3-point defect lens contributes at least ½·P(avoid α⊕21⊕β | fibre);
 * hence it suffices to show that, for a positive fraction of the ≍ √n stages, with probability bounded below
   there is a level at which the 21-version fails and an isolated defect lens is present.

## 5. Other layered patterns  (`layered_paired.c`, `run_family.sh`)

General sweep with partial layers (t, lo, cur, top) and dominance pruning; validated against brute force for
sizes 2, 3, 4, 5, (1,2), (2,1), (1,3), (2,3), (1,1,2), (1,2,3) at n ∈ {7, 10, 13, 16}, 3000 permutations each,
0 mismatches. Table: `out/family_table.txt` (from `aggregate_family.py`).

Findings: the deficit is positive for every family, stable in D/√n between n = 10⁴ and 10⁵, and increases with
the layer size (D/√n ≈ 0.0023, 0.0051, 0.0075, 0.0095, 0.0105 for layers of size 2…6). Isolated 21 blocks among
singletons cost about the same per block as in the pure pattern (≈ 0.0025 per block in length units), i.e. the
cost is roughly additive in the number of interior 21 blocks.

## 5a. Cost per converted block  (`hybrid_profile.c`, `run_hybrid.sh`, `aggregate_hybrid.py`)

Pattern 21^{⊕i} ⊕ 1 ⊕ 1 ⊕ … (first i blocks flipped, rest increasing), N_i = longest contained prefix, paired with LIS
on the same permutation (i = 1 must give mean 0 by the equality case; it does: 0.006 ± 0.004).

    n = 10^4 (60 000 samples):  i = 8: 0.028   16: 0.044   32: 0.080   48: 0.118   64: 0.163 ± 0.017
    n = 10^5 ( 4 500 samples):  i = 32: 0.078  64: 0.152  128: 0.331  192: 0.448 ± 0.092

E[LIS − N_i] is linear in i with slope ≈ 0.0025 per block in both cases, the same as D(n)/(number of blocks) for the
full pattern. So the deficit is produced block by block at a constant rate — exactly the picture of the exact
identity (one non-negative term per flip).

## 5b. Larger layers and n = 10^8  (`run_followup.sh`)

See `out/family_table.txt`. D/√n keeps increasing with the layer size up to at least 16 (≈ 0.012, 0.0135, 0.014,
0.017 for sizes 8, 10, 12, 16 at n = 10^5), so the hardest layered pattern has not been located; the general solver
becomes slow beyond size 16 (pending lists of thousands). The n = 10^8 batch for the pure 21 pattern is in
`out/l21_n100000000_w*.txt` (150 samples, D = 20.96 ± 2.18).

Process note: I edited `run_followup.sh` (to make it build its own binaries) while it was still running; all of
its jobs had been dispatched and completed, but the shell then hit a syntax error on the rewritten file and did
not write `out/FOLLOWUP_DONE`. No data were affected. Do not edit a running script.

## 5c. Attempt at the strict inequality  (`strict-deficit-plan.md`)

Worked out a "gadget" argument: flip sparse swaps from the south-west end, condition on the explored region, and
plant in the cell of a good notch of the front a 3-point lens followed by a short increasing run whose length
exceeds the cell's deficit; then the lens is the unique top structure and the fibre contributes exactly 1/3. This
reduces c₂₁ < 1 to a "start regularity" lemma (some good notch has bounded deficit, with probability bounded below,
at most stages). I could not prove the lemma by elementary means: the reference object changes with the stage, so
the coarse-path averaging that settles the single-swap case does not transfer; see the plan file for the list of
dead ends. No claim is made.

## 5d. Second pass on the strict inequality (time-boxed, about two hours)  (`fibre_cost.py`, plan file addendum)

Evaluated the exact fibre formula stage by stage (exact agreement on S₈, S₉; 0.15641 ± 0.00083 for flips 1…63 at
n = 10⁴ against 0.153 ± 0.012 directly). Replaced the grid-box gadget by resampling the rectangle between two points
of an optimal copy, which is affine-invariant and needs neither margins nor a regular front. This appears to give
the single-swap statement by elementary means, and reduces the many-swap statement to a local increment estimate for
point-to-point last passage times plus a multiplicity bound for near-optimal windows. Neither was proved; stopped
at the time limit. Details and dead ends: `strict-deficit-plan.md`, addendum.

## 6. What this does and does not establish

Established rigorously: Theorem 1, Corollary 2 (c₂₁ ≤ 1), the exact deficit identity, the equality cases and the
smallest defect. Established numerically, not proved: c₂₁ = 0.99887 ± 0.00002 < 1, hence (if true) Alon's conjecture
fails for ε < 0.0023 already on the single pattern 21^{⊕k/2}, and for ε up to ≈ 0.014 on layers of size 12.
Not addressed: what the true universality threshold is (it is at least the largest layered threshold), and whether
universality at C·k² holds for some constant C.
