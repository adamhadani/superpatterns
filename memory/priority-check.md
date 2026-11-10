# Priority and literature comparison — 10 September 2026

This is a qualified comparison, not a certificate of novelty. The earlier
priority survey is preserved in `archive/priority-check-before-2026-09-10-followup.md`;
its stronger “new” verdicts and dismissal of online embedding are superseded.
The current review checked primary papers and targeted searches around the
constants, witnesses, monotone inflations and repeated-pattern frontiers.
No specialist was contacted. Unpublished work, alternate formulations and
restricted-class universality literature can still affect priority.

| Topic | Primary comparison | Assessment |
|---|---|---|
| Deterministic lower bound | [Chroman–Kwan–Singhal](https://arxiv.org/abs/2004.02375), Thm 1.1: coefficient 1.000076/e² | Corrected C′ certifies 1.0073/e², increment .007224/e²; no stronger published coefficient found in the checked sources. The mechanism refines their encoding ideas |
| Small witnesses | [Engen–Vatter](https://arxiv.org/abs/1810.08252), §6: general bounds 25 and33 for k=7,8 | Our witnesses have lengths23 and30. Earlier equal or better witnesses were not found by this review; verify tables and specialist knowledge before priority claims |
| General random universality | [He–Kwan](https://arxiv.org/abs/1911.12878): 2000k²loglogk | Still the general upper bound in the primary literature checked; our structured results do not supersede it |
| Individual / typical targets | [Altschuler–Dubroff–Tikhomirov](https://arxiv.org/html/2608.19050v1), Thms1.3,1.5,1.7 | Their online concentration yields offline individual .50568+ε and typical .49967+ε coefficients by standardizing an iid prefix. W19 .757 and W29 .527 are superseded; W31's certified typical .4649 upper bound remains quantitatively stronger. No “first below1/2” claim |
| Shared squares | [Deuschel–Zeitouni](https://arxiv.org/html/math/9803035v1), Thm1 | Supplies the fixed-ratio monotone lower tail; W39 is a short common-event consequence. Priority as an inflation theorem not established |
| Burke / c₂₁ frontier | Classical Hammersley-type stationary methods; the full local derivations are in W36/W40 | No priority claim for the boundary formulation or algorithm. An exact frontier does not establish its invariant law |
| Small alphabets | [Hunter](https://arxiv.org/abs/2108.05474) | Use the verified arXiv entry; old notes disagree on journal metadata. No located proof of the announced 15/32 general upper bound is used |

The Deuschel–Zeitouni journal metadata was checked against the publisher:
[Combinatorics, Probability and Computing 8(3), 247–263 (1999)](https://doi.org/10.1017/S0963548399003776).
The theorem is used with a fixed margin below2, followed by a Poisson count
coupling; it is not treated as a uniform moderate-deviation estimate.

Before external release, obtain an independent mathematical reading of C′,
W31's directed checker, W36's marked-process argument and W34's repaired
application. Search explicitly for random universal permutations for
monotone inflations, layered classes and arbitrary inflated skeletons.
Proof verification and priority verification are separate tasks.

## Continuation: frontier and overlap formulas

The dedicated [frontier note](../output/pdf/repeated-21-frontier.md) now
includes a full prior-art table. Checking the primary
[Albert et al. 2003 paper](https://ajc.maths.uq.edu.au/pdf/28/ajc_v28_p225.pdf)
sharpens the comparison: §3.7, p. 236 gives O(n²) for layers of sizes one
and two; §3.5 gives O(n² log n) for arbitrary layers. Do not attribute only
the broader bound to the specialized problem. Albert's later paper was
published in *Random Structures and Algorithms* 31(2), 227–238 (2007),
[DOI 10.1002/rsa.20140](https://doi.org/10.1002/rsa.20140); its 2005
preprint provides the checked §4 algorithm statement.

[Albert's primary preprint](https://arxiv.org/html/math/0505485), §4, explicitly
reports O(n log n) for longest subsequences in Av(231,312,321), the layered
class allowing blocks of sizes 1 and 2. W40's new pruning achieves that order
for maximizing complete 21 blocks. The objectives differ, but a weighted
adaptation may connect them; no algorithmic novelty is asserted.

W41's underlying joint-emptiness identity is a direct specialization of
the multivariate Mecke formula; the standard reference is
[Last–Penrose, Theorem 4.4](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf).
Its fixed-host derivation and gap integration are elementary and supplied
in full. The structural examples and finite evaluation are project results,
not independently established priority claims.

W42's two-exchange selection is a standard local-minimum construction applied
to copies. Its Poisson first moment is an elementary Mecke/conditioning
specialization with a forbidden-pair kernel. The explicit k=3,n=6
counterexample to pattern independence is exhaustively verified here, but
no literature-priority claim or new asymptotic bound is asserted for W42.

## Continuation: W90 (10 November 2026)

| Topic | Primary comparison | Assessment |
|---|---|---|
| Block-flip inequality (α⊕21⊕β vs α⊕12⊕β) | [Jelínek–Karpilovskij](https://arxiv.org/abs/2002.12308), DMTCS 22:2 (2021): for every skew shape, #fillings avoiding δ₂ = #fillings avoiding ι₂ and φ_D; [Burstein–Pantone](https://arxiv.org/abs/1402.3842): 1234 ∼ {1324, 3416725}; Bóna for 1324 vs 1234 | **Not new.** Theorem 26 is the size-2 transversal case in pattern language; our proof (fibres + two sorting arguments) is short and self-contained. The JK statement was confirmed from the abstract and search excerpts on 10 Nov 2026; the paper itself was not read line by line |
| Equality when α or β is empty | Backelin–West–Xin (I_k ⊕ τ ∼ J_k ⊕ τ) | Known; the k = 2 case has a three-line direct proof |
| c₂₁ ≤ 1 and L₂₁ ≤_st ⌊LIS/2⌋ | No source located | Immediate corollary of the above; the asymptotic formulation for random permutations was not found in searches (10 Nov 2026) |
| Numerical c₂₁ ≈ 0.99887 and the bearing on Alon's conjecture | [arXiv:2608.19050](https://arxiv.org/abs/2608.19050) states the dichotomy "online and offline have different extremisers, or Alon's conjecture fails" | No prior numerical or rigorous statement that a layered pattern beats the identity offline was found. Unpublished work may exist; a specialist should be asked before any announcement |

## Continuation: W91 (10 November 2026, afternoon)

| Topic | Primary comparison | Assessment |
|---|---|---|
| E LIS − 2·E L₂₁ ≥ c·√n/ln n; 2 1 4 3 ⋯ not contained for n ≤ (k²/4)(1 + c′/ln k) | [He–Kwan](https://arxiv.org/abs/1911.12878) and the survey literature state Alon's conjecture with the identity as the only known obstruction; [arXiv:2608.19050](https://arxiv.org/abs/2608.19050) raises the possibility that the identity is not extremal offline | No prior statement that a specific pattern has a strictly larger containment threshold than the identity was found (three web searches, 10 Nov 2026: layered patterns / 2143 and LIS thresholds; Alon's conjecture and lower bounds from specific patterns; Burstein–Pantone and random permutations). Prior best in this repository: the non-strict Corollary 2 of W90. Improvement: from "≥ 0" to √n/ln n. Unpublished work may exist; no specialist was asked |
| Planted configuration 3416725 | [Burstein–Pantone](https://arxiv.org/abs/1402.3842): 1234 ∼ {1324, 3416725} | The gadget is their pattern; its use inside a resampling (Mecke) identity along an optimal copy is, as far as checked, new. No claim beyond that |
| One transposition costs a constant (Theorem A) | Enumerative literature on 1324 vs 1234 (Bóna; Burstein–Pantone) concerns exact counts, not random permutations at the LIS scale | Not found. The statement is elementary once the gadget is available |
| Tools | Bivariate Mecke formula ([Last–Penrose, Thm 4.4](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf)); Talagrand's inequality; Baik–Deift–Johansson | Standard; the Alon–Spencer theorem number for Talagrand's inequality was not checked against the book and is cited by section only |

The searches were shallow relative to the claim. Before any external announcement: ask a specialist in
last-passage percolation or permutation patterns, and search for "universality threshold" lower bounds in the
2024–2026 arXiv listings (math.CO, math.PR).

## Continuation: W91 part 2 (10 November 2026, evening)

| Topic | Primary comparison | Assessment |
|---|---|---|
| c₂₁ < 1; failure of Alon's conjecture for small fixed ε | [He–Kwan](https://arxiv.org/abs/1911.12878), Conjecture 1.1 (statement confirmed); searches for a proof or disproof dated 2020–2026 by the main session and by the reviewer | Nothing found. If the proofs are correct this is new. The searches were brief; unpublished work may exist |
| Rate of convergence of a superadditive mean (Lemma R) | [Alexander 1994](https://www.projecteuclid.org/euclid.aoap/1177004903), Ann. Appl. Probab. 4, 1074–1082: γn − C√(n log n) ≤ E L_n ≤ γn for the longest common subsequence; Rhee 1995, Ann. Appl. Probab. 5, 44–48 | **Not new**: the same argument, adapted to L₂₁ in a Poisson square. Bollobás–Brightwell 1992 (Ann. Appl. Probab. 2, 1009–1018) is confirmed only as a concentration result |
| Talagrand's inequality | Alon–Spencer, *The Probabilistic Method*, 4th ed. (2016), Theorem 7.7.1 — statement checked against the book | Standard |
