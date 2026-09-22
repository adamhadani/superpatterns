# W40 experiment report: exact repeated-21 frontier

**An exact O(n log n)-time, O(n)-space algorithm now computes the maximum
number of complete direct-summed 21 pairs, with every completed threshold
maintained at every prefix.** Permanent dominance pruning reduces each arrival
to one threshold gap. This removes the factor M+1 from the project's original
O(n(M+1) log n)-time, O(n(M+1))-space implementation, where M is the answer.

The complete, self-contained write-up is available as
[PDF](../../output/pdf/repeated-21-frontier.pdf) and
[readable Markdown](../../output/pdf/repeated-21-frontier.md), with
[editable paper source](../../output/paper/repeated-21-frontier.md).
It includes the full correctness and complexity proofs, prior-art comparison,
marked flux, verification record and the conditional implication for Alon.

## What is established

For each m, F_m is the least maximum value of a completed m-pair copy.
A pending pair records its apex z and historical activation threshold l.
Once z≥F_(m+1), that pending pair can never improve any future threshold
and can be deleted permanently. Every surviving interval obeys
F_m≤l<z<F_(m+1); its apex identifies its unique current level.
Only intervals in the arriving point's threshold gap can close.

One segment tree supports the first covering apex, range deletion and
insertion in O(log n) time each. The supplied program outputs the optimum
and optional threshold traces; witness reconstruction is not implemented.
See [the full recurrence](proof.md), [pruning and flux proof](pruning.md),
and [implementation](pruned.c).

The same state yields an exact Poisson flux: the instantaneous rate at which
completed thresholds cross a cut is the length of a union of marked intervals.
Prefixes (3,2,4,1) and (2,3,1,4) have identical completed thresholds and
pending apices, but respond differently to a next height 2.5. Thus the
historical activation marks cannot simply be discarded.

## Prior art and limits of the claim

[Albert et al., *Longest subsequences in permutations* (2003)](https://ajc.maths.uq.edu.au/pdf/28/ajc_v28_p225.pdf),
§3.7, p. 236, give O(n²) for the layered class with layers of sizes one or
two; their §3.5 gives O(n² log n) for arbitrary layer sizes.
[Albert, *On the length of the longest subsequence avoiding an arbitrary
pattern in a random permutation*](https://arxiv.org/html/math/0505485),
§4 of the 2005 preprint (published in *Random Structures and Algorithms*
31(2), 227–238, 2007, [DOI](https://doi.org/10.1002/rsa.20140)), reports
an O(n log n) algorithm for the same class allowing singleton layers.

Those algorithms optimize total selected length. W40 maximizes the number
of complete two-point layers, equivalently a weighted score on that class.
A weighted adaptation may already provide this complexity. **No algorithmic
priority claim is established.** The explicit pruned state and its flux are
the research tools documented here.

## Verification and evidence

| Check | Recorded outcome |
|---|---|
| Independent unpruned recurrence vs. pruned implementation | All 372,249 prefix states agree on every threshold |
| Exhaustive hosts | All 46,233 permutations of lengths 1–8; final answers also match brute subsequences |
| Additional hosts | 100 seeded random hosts through length 128 and nine extreme hosts |
| Exact marked flux and activation counterexample | 5,912 cut checks pass |
| Existing sample at n=4096 | 64 hosts; mean L21/√n=.941162109375, SE=.00316547 |

Commands and raw records are in [pruning-verification.txt](pruning-verification.txt),
[flux-verification.txt](flux-verification.txt), [results.md](results.md) and
the standalone note. The last row is a finite-host statistic, not an
asymptotic bound. These results are not Lean-formalized.

## Connection to the conjecture

If L21(σ_n)/√n converges in probability to c21, a proved c21<1 would disprove
Alon's conjecture; a proved c21≥1 would settle containment of the individual
family 21^(⊕m) above coefficient 1/4. Neither has been proved here.
The general criterion for a repeated length-d pattern is cτ<2/d; its short
proof is Proposition 5 of the note. Alon requires simultaneous containment
of all targets, as stated in
[He–Kwan, Conjecture 1.1](https://arxiv.org/html/1911.12878).

Next work is directed by the [Alon research strategy](../../memory/ALON-STRATEGY.md):
seek a common host event for general interleavings, and in parallel as a
research direction test a rigorous repeated-pattern obstruction through the
marked process. A stationary law or finite-volume upper certificate is the
missing mathematical step; larger simulations alone cannot supply it.
