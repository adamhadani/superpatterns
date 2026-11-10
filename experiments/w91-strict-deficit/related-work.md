# W91 — comparison with He–Kwan (2020) and Chen–Wang (2026 preprint)

Date: 10 November 2026. Both papers were read in full through a fetch agent (ar5iv/arXiv HTML); the summaries
below are in our words. Second-hand items are marked. Nothing here is a verification of either paper.

## 1. What each paper proves, and how ours relates

| | Statement | Direction |
|:--|:--|:--|
| He–Kwan, Bull. LMS 52 (2020), arXiv:1911.12878 | A uniform permutation of length 2000 k² log log k is k-universal w.h.p. (Thm 1.2); length 20k² contains all of a family of (1−o(1))k! "quasirandom" patterns (Thm 1.3) | upper bound on the universality threshold |
| Chen–Wang, arXiv:2610.13530v2 (preprint, unrefereed; proof credited to an AI system) | A uniform permutation of length 32 k² is k-universal with probability ≥ 1 − e^{−k/25} (Thm 1.1) | upper bound; removes the log log k |
| This repository, W91 | c₂₁ < 1: for fixed ε < c₂₁⁻² − 1 a uniform permutation of length (1+ε)k²/4 w.h.p. does not contain 2 1 4 3 ⋯ | **lower** bound above k²/4 |

**We do not improve on either result, and they do not bear on ours: the directions are opposite.** Together they
bracket the universality constant C* (least C such that length C·k² suffices w.h.p.):

  1/(4c₂₁²) ≤ C* ≤ 32,   numerically 0.2506 ≤ C* ≤ 32,

the lower bound claimed here, the upper bound claimed in the preprint; the published upper bound is not of the
form C·k². Before W91 the only lower bound was 1/4 (longest increasing subsequence).

What our result settles that neither paper addresses:

 * **He–Kwan Conjecture 1.1** (Alon): (1+ε)k²/4 suffices for all patterns. Refuted for small ε.
 * **He–Kwan Conjecture 5.3**: (1+ε)k²/4 suffices for every *fixed* pattern. This is the weaker statement, and
   it is the one our corollary contradicts directly, since the corollary concerns one explicit pattern.
 * **The heuristic behind the conjecture.** He–Kwan motivate it by analogy with random graphs (cliques and
   independent sets are the hardest subgraphs), saying monotone patterns are believed to be the hardest. The
   layered pattern 2 1 4 3 ⋯ is strictly harder than both monotone patterns.
 * **Their threshold question** (Section 5, unnumbered): for a fixed pattern π, what is the threshold length?
   They note it lies between (1/e² − o(1))k² and (1+o(1))k² and call k²/e² plausible for almost all π
   [second-hand reading of their Section 5; the (1+o(1))k² upper bound was not checked by us]. Our Lemma 23 and
   concentration give a **sharp threshold for 2 1 4 3 ⋯ at k²/(4c₂₁²)**, in both directions — the first pattern
   other than the monotone ones for which the threshold constant is identified as a limit constant, and the
   first shown to exceed 1/4.

Chen–Wang never mention the constant 1/4 after the introduction, give no lower bound other than the longest
increasing subsequence, and do not discuss individual patterns. Their concluding section sketches that 32 can be
replaced by any constant above 1 (in units of k²) and argues heuristically that 1 is a barrier for their method;
the fetch agent found gaps in that sketch (a Chebyshev step that does not give the claimed exponential bound, an
unjustified uniformity claim, a displayed inequality that does not follow). We therefore cite only their
Theorem 1.1. "The open problem of Alon" in their abstract is Alon's question whether 1000k² suffices, not the
sharp conjecture.

## 2. Anything usable for our remaining gap?

Not directly. Their proof couples the permutation with a 2k × 8k Bernoulli matrix (He–Kwan's interval-minor
lemma), cuts the pattern into tuples of length O(log k), calls a (shift, strip) "bad" for a tuple when a greedy
embedding fails, bounds the number of bad tests per tuple by a read-k tail inequality (Gavinsky–Lovett–Saks–
Srinivasan), and concludes by pigeonhole over the k shifts — so the union bound is over e^{O(log² k)} tuples, not
over k! patterns. Two points of contact with W91:

 * *Averaging over shifts instead of fixing one.* Our Theorem B randomises the position of each transposition so
   that one optimal copy serves a window of positions; their pigeonhole over shifts is the same kind of move.
   A read-k inequality might replace our union bounds over all chains (Lemmas 19, 20), which are what force
   windows of length log T; this is a possible route to hypothesis (H), not examined.
 * *Interval minors* give upper bounds only and say nothing about a specific pattern being hard.

For upper bounds on individual patterns the relevant comparison remains Altschuler–Dubroff–Tikhomirov
(arXiv:2608.19050): about 0.506·k² for every fixed pattern. So for the single-pattern threshold constant the
state is 1/(4c₂₁²) ≤ sup_π C(π) ≤ 0.506 (the upper bound from that preprint, as read on 10 Sept 2026).

## 3. Presentation: what both papers do that our note should do

 1. **Terminology.** "k-universal" throughout, "k-superpattern" mentioned once at the definition; "contains the
    pattern π"; "w.h.p." defined once in a footnote; the longest increasing subsequence spelled out, with
    Logan–Shepp and Vershik–Kerov (and Romik's book) for its asymptotics.
 2. **The conjecture as a numbered statement in the introduction**, attributed as He–Kwan do: Alon, 1999, "see"
    Alon's Oberwolfach abstract (Oberwolfach Rep. 13 (2016), no. 2) and Arratia (1999).
 3. **Section-based numbering** (Theorem 1.1, Lemma 2.1, …) with one counter per section.
 4. **Main theorem in the introduction, followed by a proof-outline subsection** ("1.1 Proof outline").
 5. **Short abstract**: the k²/4 threshold for the increasing pattern; the conjecture; the result; one sentence on
    the method. He–Kwan use four sentences.
 6. **AI disclosure as a separate short declaration directly after the abstract** (Chen–Wang's format: the
    abstract ends with one sentence naming the system; a three-sentence declaration says the authors do not claim
    credit for the proof ideas, have verified the proof and take responsibility). Ours must say what is true:
    at present the proofs have been checked by AI reviewers and computer experiments only.
 7. **A "Concluding remarks" section** with the open problems and the bracket for C*, instead of a paragraph at
    the end of the verification section. The verification record becomes an appendix.
 8. **Mention Conjecture 5.3 and the monotone-is-hardest heuristic explicitly** — that is the sentence a reader
    from this area will look for.

These are applied to `output/paper/layered-refutation.md` after its cold read (`out/review-3-note.md`) is in.
