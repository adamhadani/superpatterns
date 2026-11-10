# Current result ledger — 10 November 2026

This file lists what is accepted, at what scope, and how it was verified. It was first written on 10 September
2026; on 10 November 2026 the rows added between 22 and 27 September (workstreams W43–W89) were removed after the
[audit](AUDIT-2026-11-10.md) found none of their general claims proved. Those workstreams are archived, unedited,
in `experiments/archive-2026-09-unverified/`. **No proof or disproof of Alon's conjecture is claimed.** The
strongest new statements are rows W90 and W91: c₂₁ ≤ 1 is proved; E LIS − 2·E L₂₁ ≥ c·√n/ln n is proved (so
2 1 4 3 ⋯ is strictly harder than the identity); c₂₁ ≈ 0.99887 is the numerical value. **Update, 10 November
evening:** row W91b records a complete written proof that c₂₁ < 1, which contradicts Alon's conjecture for small
fixed ε. It is AI-written and AI-reviewed and has not been checked by a human; until it has, the status of the
conjecture in this ledger is "disproof claimed, unverified".

This is the authoritative status table after the review and authorized follow-up.
It supersedes stronger claims in dated logs and `historical-*` files. The
[original review](REVIEW-2026-09-10.md) records the audit findings; the
[experiment index](../experiments/README.md) preserves all forty-two directions.
This was a targeted audit, not a complete independent verification of every
historical theorem. No general Alon proof or new c₂₁ asymptotic bound is claimed.

**Featured W90 result:** [proof](../experiments/w90-layered-deficit/proof.md),
[log](../experiments/w90-layered-deficit/log.md) and [plan for the strict inequality](../experiments/w90-layered-deficit/strict-deficit-plan.md)
(the plan is superseded by W91).

**Featured W91 result:** [proof](../experiments/w91-strict-deficit/proof.md),
[log](../experiments/w91-strict-deficit/log.md), [independent review](../experiments/w91-strict-deficit/out/review-1.md).

**W40 result:** [standalone PDF](../output/pdf/repeated-21-frontier.pdf),
[readable Markdown](../output/pdf/repeated-21-frontier.md) and
[experiment report](../experiments/w40-c21-frontier/report.md) now contain
the full proof, primary prior-art comparison and conditional Alon obstruction
criterion. The [Alon strategy](ALON-STRATEGY.md) sets the new research priority.

## Models and quantifiers

- sp(k): minimum deterministic host length containing all k! targets.
- Π_N: Poisson intensity N on the unit square (mean point count N).
- Individual target: a bound for each prescribed π, possibly uniform over π.
- Typical target: probability over an independent uniform π and host; this
  is equivalent via Markov to all but o(1) of targets having failure o(1).
- Simultaneous class: the same host contains every target in the class.
  Neither individual nor typical high probability implies this automatically.

## Accepted main statements and exact scope

| ID | Statement | Dependencies / verification | Limits |
|---|---|---|---|
| A / W3 | Finite product inequality for pat_k(σ), odd k, every σ and x∈(0,1) | Stable even rule; [proof](../experiments/w3-lowerbound/proof.md); Lean `theoremA` | Lean numerical negativity uses λ=1.0003, θ=7.37. Optimized root ≈1.00031251 is numerical; the asymptotic sp corollary is not itself formalized |
| C′ / W7,W25 | sp(k)>1.0073 k²/e² for all sufficiently large k | [Full corrected proof](../experiments/w25-asymptopia-review/proof.md), [Decimal certificate](../experiments/w25-asymptopia-review/cprime_certificate.json), repaired class checker | No effective k₀ and no Lean formalization. Approximate optimum 1.0073384 must not be rounded up to 1.00734 |
| W1 | sp(7)≤23, sp(8)≤30 | Explicit witnesses; exhaustive Python/C; Lean sound checker plus `native_decide` | Compiler trust for native evaluations; no exact sp(7) or sp(8) claim |
| W31 / Thm 17 | Independent uniform target and host of length ceil(Ck²): containment 1−o(1) for every C>0.4649 | [Corrected reduction](../experiments/w31-lookahead/proof.md), [MPFR certificate](../experiments/w31-lookahead/certification.md); all 512 recurrences, ε=1/64; padding to all k | Typical, not simultaneous; very large hidden finite-k constants. Not an optimality certificate |
| W36 / Thm 20 | Independent-strip first-passage functional: n≤E K_n≤n+√(2n)+1/2, hence γ∞=1 | [Burke and comparison proof](../experiments/w36-gamma-limit/proof.md); centered compound-Poisson increments | Exact mean-cost constant does not prove an exact containment threshold |
| W34 repaired | Fix b,η,A>0 and C>C_b^mix. For min(r,h)≥log³k and successive same-strip visits ≥ηr, individual failure ≤k^(−A), uniformly in the visiting sequence | [Full reduction](../experiments/w34-grid-lookahead/reduction.md): failed-block continuation, conditional mean concentration, renewal mixing, boundary blocks | Old H_b (only fixed no-revisit window) is insufficient; no union bound over all row permutations is claimed |
| W34+W36 | Same uniform host at ceil((1/4+ε)k²) contains all tilted-grid shapes rh=k with min(r,h)≥log³k, and all dihedral images, failure O(k⁻²)+e^(−Ω(k²)) | Choose fixed b, A=3 in repaired reduction; at most 8k shapes; Poisson coupling | ε fixed; no matching lower threshold |
| W39 / Thm 22 | For fixed ε,A>0, some K_(ε,A): same host at ceil((1/4+ε)k²) contains every monotone inflation of any skeleton, total length k, all blocks ≥ceil(K√log k), failure ≤k^(−A) | [Shared-square proof](../experiments/w39-shared-squares/proof.md); fixed-ratio Deuschel–Zeitouni lower tail and ≤(k+1)³ host squares | Blocks are consecutive in both positions and values; no interleaving or short-defect claim. Novelty unestablished |
| W40 / Props 23–24 | Exact repeated-21 frontier; permanent pruning gives O(n log n) time and O(n) space; exact marked interval-union flux | [Full state](../experiments/w40-c21-frontier/proof.md), [pruning and flux proof](../experiments/w40-c21-frontier/pruning.md); 372,249 prefix-state checks, all hosts through length 8 | No invariant law or new asymptotic bound. Related O(n log n) layered algorithms predate this work; no novelty claim |
| W41 / Prop 25 | Exact canonical joint-emptiness integral at every overlap; nonnegative integer formula for fixed-host moments | [Proof](../experiments/w41-canonical-overlap/proof.md); 10 overlap-(k−2) and 22 general-overlap entries agree with exhaustive enumeration | Number of union types can be large; no asymptotic bounded-ratio or random-host divergence theorem |
| W42 | Two-exchange selection preserves existence, eliminates overlaps k−1,k−2; exact forbidden-pair first moment; pattern independence is false at k=3,n=6 | [Proof and finite counterexample](../experiments/w42-two-exchange/proof.md); 93,416 independent local checks and independent aggregate recount of all six targets | Exact formula is not an efficient evaluation; no uniform asymptotic moment bound or containment improvement |
| **W90** | **Block flip:** for all patterns α, β and all n, #{σ∈S_n ⊇ α⊕21⊕β} ≤ #{σ∈S_n ⊇ α⊕12⊕β}, with the exact difference Σ_fibres (a−1). Hence P(σ_n ⊇ 21^{⊕m}) ≤ P(LIS ≥ 2m), L₂₁ ≤_st ⌊LIS/2⌋ and **c₂₁ ≤ 1**. Equality when α or β is empty; smallest defect is a 3-point lens (weight 1/3); \|Av₉(214365)\| = \|Av₉(123456)\| + 1. **Numerical (not proved):** E⌊LIS/2⌋ − E L₂₁ = (0.00113 ± 0.00002)√n for n = 10³…10⁸, so c₂₁ ≈ 0.99887 < 1 and Alon's sharp conjecture would fail on 21^{⊕k/2} | [Proof](../experiments/w90-layered-deficit/proof.md), [log](../experiments/w90-layered-deficit/log.md); `verify_fibers.py` (all σ, n ≤ 8; n = 9 for (21,21)); exhaustive S_n, n ≤ 12; 1.29·10⁶ paired samples; independent cross-check with W40 `pruned.c` (0 disagreements on 81 240 permutations) | Theorem 1 is the k = 2 transversal case of Jelínek–Karpilovskij (2021) / Burstein–Pantone (2015): no novelty claimed. The strict asymptotic deficit, and with it the disproof of Alon's conjecture, is **open**. Layers of size ≥ 3: inequality conjectural, deficits measured (D/√n ≈ 0.0050, 0.0075, 0.0095, 0.0105 for sizes 3–6) |
| **W91** | **Strict deficit.** For large n: E LIS(σ_n) − 2·E L₂₁(σ_n) ≥ c·√n/ln n (c = 10⁻⁹⁴). Hence P(σ_n ⊇ 21^{⊕k/2}) → 0 for n ≤ (k²/4)(1 + c′/ln k), while the identity of length k is contained w.h.p. for n ≥ k²/4 + ω(k^{4/3}). **One transposition:** in a unit Poisson process on [0,T]², Σ_p [E LIS − E N(I_p ⊕ 21 ⊕ 1 ⊕ 1 ⋯)] ≥ 10⁻⁸⁰·T. Tools: a planted copy of 3416725 between consecutive points of the leftmost optimal copy produces the 3-point defect fibre; resampling identity (Mecke); first-moment bounds on chains with many small steps; transpositions at random positions so that one optimal copy serves a window of positions | [Proof](../experiments/w91-strict-deficit/proof.md), [log](../experiments/w91-strict-deficit/log.md), [review](../experiments/w91-strict-deficit/out/review-1.md). Gadget lemmas: `gadget_check.py` (7756 plantings, 15 512 injectivity cases, from the fibre definitions) and independent `review/lemma23_containment.py` (47 428 plantings by direct containment). Probabilistic part: proof re-derived by the main session and by an independent reviewer | **Not c₂₁ < 1**: the deficit proved is √n/ln n, not √n; Alon's conjecture for fixed ε is not decided. Constants are not meaningful. Depends on Theorem 1 of W90, the Mecke formula, Baik–Deift–Johansson and Talagrand (Corollary C only). Not refereed; no specialist asked; prior art searched on 10 Nov 2026 only |
| **W91c** | **Referee package.** Self-contained note `output/pdf/layered-refutation.pdf` (17 pages): Theorem 1.2 (c₂₁ < 1), Corollary 1.3 (sharp threshold of 2 1 4 3 ⋯ at (1+ε₀)k²/4, both directions), Theorem 1.4 (deficit ≥ 10⁻⁸⁴·T/(ln T)² with one planted pattern) | Two cold reads by reviewers that saw only the note (`out/review-3-note.md`, `out/review-4-note.md`: no error); citation audit (`out/citation-audit.md`); Lean small-case certificates for the block-flip theorem (`BlockFlip.lean`) | Same caveat as W91b: AI-written, AI-reviewed, not read by a human specialist. The note is the text to send to a referee |
| **W91b** | **c₂₁ < 1.** With ℓ(T) = E L₂₁ of a unit Poisson process on [0,T]²: ℓ(2T) ≤ 2ℓ(T) + 45√(T ln T) and c₂₁T − 200√(T ln T) ≤ ℓ(T) ≤ c₂₁T for large T; with row W91 this gives c₂₁ < 1. **Consequence:** for every fixed ε < c₂₁⁻² − 1, a uniform permutation of length ⌊(1+ε)k²/4⌋ contains 21^{⊕⌊k/2⌋} with probability → 0; so Alon's conjecture (He–Kwan, Conjecture 1.1) fails for small fixed ε | [Proof](../experiments/w91-strict-deficit/proof-c21.md), [review](../experiments/w91-strict-deficit/out/review-2.md), reviewer's code and data in `review2/`. Rate lemma is Alexander's (1994) argument; Talagrand's inequality checked against Alon–Spencer Thm 7.7.1 | **Claim, not externally verified.** Depends entirely on row W91 (Proposition 6.1) and W90 Theorem 1. No effective constant (1 − c₂₁ ≳ 10⁻⁹⁷ at T ≈ 10²⁰¹). Not testable by simulation. Says nothing about universality at C·k² |
| W28,W35 | Finite missing-pattern moment/witness inequalities; hereditary containment and Erdős–Szekeres | Lean `Witness`, `BlockSplit`, `ErdosSzekeres`, `Axioms`; `lake build` re-run 10 Nov 2026 after removing the September modules | No Poisson containment theorem or asymptotic constant is formalized |

## Numerical certificates

C′ uses exact λ=1.0073, τ=.96813, β₀=.53692, R=.00783, c₀=.4805.
Its certified interval for G is
[.08638273335657631565, .08640436420870837849]. The upper rates, including
the prefactor, are below −.0000310448 (good), −.0000376128 (bad window),
and −.2342401128 (large width). An independent SciPy calculation gives
G≈.08639355273193 and lies inside the enclosure. The proof controls the
whole width domain and real maximization variable, not a sampled grid.

W31 treats the old ε=.02 table as exact binary64 candidate potentials.
Directed MPFR checks a different rule with the exact symmetric margin 1/64.
At n=512 the upper recurrence is 121845.56860063219, the candidate is
121864.01799138699, and its ratio is at most .46487433620981994<.4649.
All 512 inequalities pass. The former multiplicative roundoff allowance
in `dp_cert.py` was not a certificate.

## Experiments, unresolved claims, and withdrawals

| Workstreams | Current reading | Next action |
|---|---|---|
| W3 both parities | **Withdrawn:** selected set changes under an allowed move; explicit k=5 counterexample in proof | Require a new stable rule or counting argument before numerical optimization |
| W4,W6 | Positive witnesses are checkable; small-alphabet/rosary lower values are solver-reported. No standalone UNSAT certificate found; length 22 unresolved | Generate and independently check proof artifacts if exact-value results are to be published |
| W2,W8 | Construction obstructions for the specified models; nonidentical blocks remain a distinct possibility | Archive local searches; resume only with a mechanism outside proved hypotheses |
| W5,W10,W16,W21 | Finite-k threshold / pattern-constant data | No proved typical limit .22 or identity-hardest theorem; large-k fitting alone is low priority |
| W9,W13,W14,W15,W18 | Partial thread results, false entropy/lag hypotheses, explicit hard families | No theorem ruling out every multi-thread strategy; require a structurally new argument |
| W11,W19,W20,W23,W26,W27 | Earlier strip, greedy, mean-field and cell-certificate bounds | Retain historical proofs; W19 .757 and W29 .527 are superseded by the external benchmark |
| W12,W17 | Canonical first-moment / renewal reductions; numerical constants ≈2.279 and .7866 respectively | W12's global operator supremum is not interval-certified; .787 is an upward rounding of the renewal lower estimate. The rigorous window is now 0.7866 ≤ c₂₁ ≤ 1 (upper bound from W90) |
| W22 | Limitations of the tested Janson/concentration/certificate formulations | Do not promote them to impossibility statements about the tools in general |
| W24,W28,W30,W33 | Missing-pattern counts, conditioning, empty rectangles and slopes | Useful supporting diagnostics; no demonstrated first-moment determination of the Alon constant |
| W29,W31,W32 | Fresh-search expected-cost recurrences; W31 upper bound now certified | Nonanticipation and variance hypotheses explicit; ≈.4623 and tiny limiting anticipation gain remain numerical |
| W37 | Strip rearrangement and finite box comparison valid; probability-direction and o(k log k) rate inferences withdrawn | Obtain uniform quantitative tails before renewed rate comparison. Defect-free box result strengthened by W39 |
| W38,W41 | Exact averaged moment identities, k−1 rigidity, and full joint-emptiness expression; two-point changes can shift every shared point | Integral task complete. Next finite target: first-moment cost of two-exchange lexicographic selection; no broad sampling |
| W40 | Exact one-gap update and local marked flux now available | Test a proposed stationary marked law against the generator; unmarked closure has a four-point counterexample |
| W43–W89 | **Not accepted** (audit of 10 November 2026): universality at C·k², sharp ¼ for bounded LDS, c₂₁ = 1, generic bulk | Archived in `experiments/archive-2026-09-unverified/`; reuse only with a new proof |

At C=1/4 the new W38 off-diagonal estimates are D=.98 [.89,1.08],
3.79 [3.53,4.07], 6.94 [6.25,7.71] for k=6,8,10. The total stays near20
because the diagonal decreases. The largest off-diagonal bin is k−2, but
smaller overlaps carry substantial mass. The paired bootstrap includes
numerator–denominator covariance; sparse fixed-target data do not establish
pattern uniformity. See [current interpretation](../experiments/w38-second-moment/results.md).
An upper first-moment bound ceasing to decay at .1925 does not prove growth.

W40's 64 hosts at n=4096 give mean L₂₁/√n=.941162109375, SE=.00316547.
This is finite-host evidence only. The continuation prunes each pending apex
at least its next completed threshold, localizing every arrival to one gap.
An exact flux identity integrates the covered interval length below a cut.
Activation marks remain indispensable: prefixes (3,2,4,1) and (2,3,1,4)
have the same F=(0,2,∞) and apices {1,4}, but only the latter completes a
second pair on height 2.5. No unmarked stationary closure follows.

W41's compatible ordered union-type counts for overlap k−2 at k=2,3,4,5
are 8,48,276,1648. The exact formula matches all ten cells with k+2≤n≤7;
22 additional cells check every overlap at k=2,3 and n≤6. A full-shift family
exists for all k: first and last k positions of 2,1,4,3,… of length k+2.
In a deterministic 21^(⊕r) host, all binom(r,q) copies of 21^(⊕q) are
canonical. These are obstructions to deterministic cluster suppression,
not lower bounds on their mass in random hosts.

## Reproduction and completed verification

Run from the repository root unless a working directory is specified.

```sh
python3 experiments/w25-asymptopia-review/certify_cprime.py
python3 experiments/w7-slots/lemma_check.py
python3 experiments/witnesses/check_witness.py
```

The MPFR compilation and run are in W31's `certification.md` (MPFR/GMP
required; complete TSV output is included). The new diagnostic is reproducible:

```sh
python3 experiments/w38-second-moment/run_diagnostic.py
experiments/w12-c21/.venv/bin/python experiments/w38-second-moment/analyze_diagnostic.py
python3 experiments/w38-second-moment/verify_diagnostic.py
cc -O3 -std=c11 experiments/w40-c21-frontier/frontier.c -o /private/tmp/superpatterns-c21-frontier
python3 experiments/w40-c21-frontier/verify.py /private/tmp/superpatterns-c21-frontier
cc -O2 -std=c11 -Wall -Wextra -pedantic experiments/w40-c21-frontier/pruned.c -o /private/tmp/superpatterns-c21-pruned
python3 experiments/w40-c21-frontier/verify_pruned.py /private/tmp/superpatterns-c21-pruned
python3 experiments/w40-c21-frontier/verify_flux.py
python3 experiments/w41-canonical-overlap/verify.py
python3 experiments/w41-canonical-overlap/verify_general.py
python3 experiments/w41-canonical-overlap/verify_families.py
python3 experiments/w42-two-exchange/selection.py
python3 experiments/w42-two-exchange/analyze.py
python3 experiments/w42-two-exchange/verify.py
python3 experiments/w42-two-exchange/verify_census.py
make -C output/paper frontier-note
# W91
sh experiments/w91-strict-deficit/run_checks.sh
python3 experiments/w91-strict-deficit/review/lemma23_containment.py selftest
# W90
cd experiments/w90-layered-deficit && python3 verify_fibers.py 8 && python3 skew_boards.py
cc -O2 -o /tmp/exact_dist exact_dist.c && /tmp/exact_dist 9
sh run_paired.sh   # paired L21/LIS batches (long); tables: python3 aggregate.py
```

The analysis needs NumPy; the listed existing virtualenv provides it. The
runner keeps existing CSV hosts rather than overwriting them. Certificate
programs and raw data are retained; compiled binaries are ignored or temporary.

Completed: C′ interval certificate and independent SciPy cross-check; all
W31 MPFR inequalities; repaired W7 per-class and summed checks; W38 direct
Python/C comparison on 35 hosts; W40 exhaustive verification on 6113 hosts;
W36 DP/brute comparison on 300 finite instances with the documented .002
staircase tolerance. `lake build` passed (8719 jobs), and its axiom output
confirmed the scope above. Witnesses were independently rerun in the
preceding review. Paper build and visual review are recorded in SESSION-STATE.

Continuation verification: all 372,249 completed prefix states agree between
pruned and unpruned algorithms; exhaustive final lengths through n=8 also
match brute force. The marked flux passes 5912 exact checks. All ten targeted
and 22 additional moment entries agree with direct host enumeration; 77
canonical cluster overlap counts through r=6 and the full-shift family
through k=100 pass. No Lean source was changed in this continuation; the
previous Lean build does not formalize these additions.

W90 verification (10 November 2026): the block-flip theorem was re-derived by the main session and checked by
`verify_fibers.py`, which recomputes U, S, the fibres and the boards from the definitions for seven choices of
(α, β) and every σ ∈ S_n, n ≤ 8 (n = 9 for (21, 21)); it reproduces |Av₈(1324)| − |Av₈(1234)| = 26. Exhaustive
counts on S_n, n ≤ 12, give #{L₂₁ ≥ m} = #{⌊LIS/2⌋ ≥ m} for n ≤ 8 and deficits 1, 66, 2565 (+2), 77232 (+213) for
n = 9…12. The sweep algorithm for L₂₁ agrees with an O(n³) dynamic programme on 180 000 permutations and with W40's
independently written `pruned.c` on 81 240 permutations (n up to 10⁶). Paired batches: 1 290 950 permutations,
n = 10³…10⁸, D(n)/√n = 0.002269 ± 0.000036, log–log slope 0.491 ± 0.006. Lean: after removing the September
modules `Greene`, `Interleaving`, `Lattice` and restoring `Witness`, `Axioms` to their 30 August state, `lake build`
was re-run (result recorded in SESSION-STATE).

W91 verification (10 November 2026): Lemmas 2.3–2.5 of `experiments/w91-strict-deficit/proof.md` were brute-forced
by `gadget_check.py`, which recomputes U_α, S_β, the inside sets, boards and fillings from the W90 definitions
(7756 plantings, all giving the 3-point lens with F = 3, a = 2; 15 512 injectivity cases; 1930 pairs of the
leftmost optimal copy), and by an independently written program that decides containment directly (47 428
plantings; 70 144 copy pairs; negative controls fail). The resampling identity (Lemma 3.1) was checked by Monte
Carlo with a one-point plant and exactly at leading order. Theorems A and B were re-derived line by line by the
main session and by a reviewer agent that did not write them; the reviewer found no error and its nine remarks on
under-justified steps were incorporated. The first-moment constants were recomputed (`out/constants.txt`).
