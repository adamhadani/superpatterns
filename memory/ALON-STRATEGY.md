# Research strategy: prove or disprove Alon's random-superpattern conjecture

## 0. Revised strategy — 10 November 2026 (supersedes the ordering below)

**Change of target.** W90 shows c₂₁ ≤ 1 rigorously and c₂₁ ≈ 0.99887 numerically (deficit ∝ √n over five decades,
two independent programs). The working hypothesis is now that **the sharp conjecture is false** and that the
identity is *not* the hardest pattern: every interior 21 block (more generally every interior decreasing layer)
costs a fixed positive amount. Sections 1–5 below were written under the opposite hypothesis; §2 ("repeated-pattern
obstruction") was the right instinct, §5 (generic bulk at ¼) is retracted (see the audit).

### D1. Rigorous disproof: prove liminf (E⌊LIS/2⌋ − E L₂₁)/√n > 0   — top priority

What is in hand (W90): the exact identity
  E⌊LIS/2⌋ − E L₂₁ = Σ_{stages} E[(a − 1)/F],
each term ≥ 0, where a stage is one flip 12 → 21 with prefix α and suffix β, F is the number of valid fillings of
the skew region U_α ∩ S_β given the outside points, and a the number of those without a D-inversion. The smallest
contributing fibre is a 3-point lens (weight 1/3), and a fibre with an *isolated* 3-point lens contributes at
least ½·P(21-version avoided | fibre).

Routes, in order of expected tractability:

 (a) *Near-maximiser tightness.* Flip from the south-west end, so that S is a Hammersley region of fresh Poisson
     points in U. Show: with probability ≥ p₀, the set of fresh points within two levels of the maximum of
     h(z) = LIS(NE(z)) on U has at most N₀ points. Then a finite-energy resampling inside a bounded window around
     the maximiser produces a defect lens at bounded cost. Needs: a local description of ∂U (it has an outer
     corner between any two consecutive minimal points, which is all the lens needs) and an O(1) bound on the
     number of near-maximal starting points. Test numerically first: measure the empirical law of the number of
     points in the top two levels at each stage, and the frequency of isolated defect lenses; the product should
     reproduce 0.00114 per pair.
 (b) *Sparse swaps.* By Theorem 1 it is enough to beat the benchmark for ANY pattern with fewer 21 blocks, e.g.
     the identity with one adjacent transposition every 2K places. Between swaps the thresholds evolve by the
     Hammersley rule; show the composite particle's output relaxes to the stationary Poisson structure
     (Mountford–Prabhakar type statement for tandem queues) and compute the single-defect cost in the stationary
     system, where both fronts are Hammersley lines and the Burke/Cator–Groeneboom structure is explicit.
 (c) *Single swap, exact.* For I_a ⊕ 21 ⊕ I_b both regions are Hammersley regions of the same Poisson process (one
     from each corner). Compute or bound lim Σ_b E[(a−1)/F] directly; this is a statement about pure LIS geometry
     and may be accessible through known determinantal structure.

 Progress on (a)/(b), 10 Nov: `experiments/w90-layered-deficit/strict-deficit-plan.md` gives an explicit gadget
 (a planted 3-point lens plus a short run in the cell of a good notch) that makes a stage contribute exactly 1/3,
 and reduces everything to a "start regularity" lemma; the lemma is not proved.

 Stop criterion: do not claim the disproof from numerics; do not accept a "density of defects" argument that
 ignores the global condition that the *whole* marginal region is inversion-free.

### D2. Size-≥3 layers and the hardest layered pattern

Prove P(⊇ α⊕J_d⊕β) ≤ P(⊇ α⊕I_d⊕β) for d ≥ 3 (transversal case of the Jelínek–Karpilovskij conjecture); the fibre
argument reduces it to: in every skew board, #fillings without an increasing d-chain ≤ #fillings without a
D-decreasing d-chain. Numerically the deficit per unit length increases from d = 2 to d = 16 (0.0023 → 0.017 in
D/√n). Determine the maximiser; for d → ∞ the per-layer cost should scale like d^{1/3} (KPZ), so the relative
deficit must eventually decrease. The best lower bound on the true universality constant C* is the largest
layered threshold.

### D3. What replaces the conjecture?

(i) Is sup over patterns of the single-pattern threshold attained by layered patterns? (ii) Is universality true
at C*·k² with that C*? (iii) Independently of the constant: universality at C·k² for some C (remove He–Kwan's
log log k). W9/W13/W15 are the honest starting points; nothing from W43–W89 can be reused without a new proof.

### D4. Bookkeeping that follows from the audit

Done on 10 November 2026 (paper rewritten, withdrawn preprint and September Lean modules removed, workstreams
archived). Remaining: an outside specialist reading before anything is announced.

---

*The text below is the strategy of 10–24 September, kept for reference.*

Updated 10 September 2026. This queue supersedes the publication-first ordering
in earlier session notes. The user prioritizes progress on the conjecture.
The [current ledger](RESULTS.md) separates established results from candidates.

## The target and the first milestone

For every fixed ε>0, with n=⌈(1/4+ε)k²⌉, prove

    Pr(σ_n contains every π∈S_k) → 1,

or disprove this for at least one fixed ε. A target witnessing failure may
depend on the host. A deterministic target sequence absent with nonvanishing
probability is sufficient for a disproof, but is not necessary.

The checked general benchmark is 2000k² log log k. He–Kwan's proof separates
structured and quasirandom parts, conditions on common host events, and
handles their arbitrary interleaving. The structured-map count and its
zero-run cost carry the log log k loss. They also obtain simultaneous
containment of a deterministic (1−o(1)) fraction of targets at 20k².
See [Theorems 1.2–1.3 and §1.1](https://arxiv.org/html/1911.12878).

**Primary intermediate objective: general simultaneous universality at Ck²
for some absolute C.** Removing the remaining growing factor would be major
progress even before reaching 1/4. W31's typical-target constant and W39's
structured-family coefficient answer different questions.

## 1. Common host events that support interleaving — main proof route

W39 succeeds because a single high-probability event certifies a polynomial
family of squares. Every eligible inflation can then choose its own embedding
on that event. W34/W36 provide stronger strip traversal tools under explicit
revisit hypotheses. Neither currently handles general interleavings.

**Next mathematical task:** formulate a boundary-compatible embedding lemma
for a structured part and a residual part. It must specify which entrance,
exit and reserved value intervals remain available after either part is
embedded, and show that a permitted choice always completes the other part.
Containing both parts somewhere in the host is insufficient.

Begin with two interleaved monotone chains, then controlled interleavings
of the strip patterns already understood. These are tests of the gluing
mechanism, not a claim that every permutation has a bounded-chain decomposition.
For a candidate interface, exhaustively search small patterns and small
occupancy matrices for failures of the deterministic implication before
investing in a concentration proof.

For the general extension, seek a decomposition certificate whose description
and probability cost can be paid once per host, or let the embedding choose
among many compatible placements. A useful target is O(k) structured traversal
cost on the chosen placement, with a residual embedding guarantee that survives
the choice. Quantify both the number of interfaces and the failure probability;
write the final simultaneous union bound before optimizing constants.

**Stop criterion:** reject a proposed lemma if it hides a union over k! targets,
requires all placements to have constant average cost without proof, loses
boundary compatibility, or reuses exposed randomness as fresh. The false W14
entropy and W18 lag lemmas, and the withdrawn W34 H_b inference, are explicit
counterexample tests. Do not silently restore those hypotheses.

**Bridge to Alon:** a common host event with probability 1−o(1) that implies
containment of every target establishes the general Ck² milestone. Only then
does reducing C toward 1/4 address the sharp conjecture along this route.

## 2. A rigorous repeated-pattern obstruction — main disproof route

For a fixed length-d pattern τ, let Lτ count direct-summed copies. If
Lτ(σ_n)/√n→cτ in probability, then **cτ<2/d disproves Alon**. Conversely
cτ≥2/d gives containment of this individual repeated family above 1/4.
The proof is [Proposition 5 of the frontier note](../output/pdf/repeated-21-frontier.md).
Alon requires this lower inequality, not equality of every constant.

W40 makes τ=21 the most tractable current case: the exact update is O(log n),
and its marked Poisson generator and interval-union flux are available.

**Next mathematical task:** construct a boundary process or potential on the
full marked state, prove its drift or invariance, and prove the comparison
with the empty finite box. Test every proposed law first against the exact
cut-flux identity. A law describing thresholds and unmarked apices alone
fails the recorded four-point counterexample.

For an upper bound, a finite-volume certificate must include an explicit
boundary correction controlling arbitrarily large boxes, or a rigorous
supermartingale/comparison argument. A small finite mean, a fitted intercept,
or finite-box superadditivity supplies no such upper bound. For a lower bound,
the direction of comparison must be proved separately. Passing local flux
tests is necessary for a proposed law, not sufficient for stationarity.

**Stop criterion:** abandon a candidate closure as soon as reachable marked
states contradict its next-step transition. Expand numerical sampling only
to distinguish specific laws or certify finite pieces of a proved inequality.
W10 already sampled many repeated short patterns; repeating that survey
without a bound-conversion mechanism has low priority.

**Bridge to Alon:** a rigorous c21<1 gives a counterexample; c21≥1 removes
this particular obstruction. Neither an exact scan nor c21=1 alone proves
universality over all targets.

## 3. Stronger selection and avoidance — targeted analytic route

W41's exact canonical overlap formula is complete, but no asymptotic bound
controls all overlap ranges. W42 now removes overlaps k−1 and k−2 by retaining
local lexicographic minima under one- and two-point exchanges. Existence is
preserved exactly.

The new [finite counterexample](../experiments/w42-two-exchange/proof.md)
shows target-dependent first moments already at k=3,n=6. Therefore importing
W12's pattern-independent factorization is ruled out. W42 Proposition 2
replaces it with an exact formula: background points avoid the one-point
forbidden region and contain no pair in a target-dependent exclusion kernel.

**Next mathematical task:** describe this kernel for τ^(⊕m), starting with
τ=21 and using monotone targets as controls. Classify pair constraints that
remain dependent through shared points; derive rigorous upper and lower
bounds for their joint exclusion probability. Keep changes of rank among
the common points: W41 gives examples where every shared rank shifts.

Use an upper bound on E Yπ^(2) to seek an obstruction, and a lower first
moment plus all-overlap second-moment control for a containment attempt.
These are different inequalities. E Yπ^(2)→0 for one sequence at C>1/4
would disprove Alon by Markov. A bounded moment ratio gives only positive
success probability; the simultaneous conclusion still needs an additional
argument. Pattern-averaged estimates have weaker quantifiers again.

**Stop criterion:** pause this route if the selector's first-moment loss or
pair dependence cannot be bounded in the quadratic regime. The seven exact
small-host moment improvements justify the question, not a larger blind sweep.

## 4. Host-dependent missing targets — alternative disproof route

Search only with a genuine containment oracle: a failed greedy embedding
is not proof that a target is absent. Use the existing exact small-host
machinery to find missing targets at C>1/4 and ask whether their witnesses
compress into an explicit geometric certificate that scales with k.

**Next mathematical task:** define a certificate family C_k and a deterministic
map from each valid host certificate to an absent k-pattern. Then estimate
the probability that a random host has at least one such certificate. A
nonvanishing lower bound at a fixed C>1/4 would disprove Alon, even if every
preselected target individually succeeds with high probability.

**Stop criterion:** do not treat isolated finite missing targets, optimization
failures, or a large expected number of heavily clustered certificates as
an asymptotic probability bound. W24's union-bound slack and W28's witness
inequalities should guide how certificate dependence is measured.

## Work deliberately secondary to this queue

The frontier result is now prominently documented with primary citations;
independent specialist and priority review remain appropriate before a
submission. Further C′ coefficient optimization, faster small witness search,
and improving the typical-target .4649 constant are secondary unless their
mechanism directly supplies one of the missing lemmas above.

No general asymptotic improvement or disproof is claimed by this strategy.
The next deliverable should be a proved interface/kernel/drift lemma, or a
precise counterexample eliminating a candidate lemma, with a stated route
from that deliverable to the conjecture.

---

## 5. (removed)

The section "The Generic Bulk at Sharp 1/4 Frontier" added on 24 September 2026 (W66–W75) asserted results that the
audit of 10 November found unproved; it has been deleted. See `memory/AUDIT-2026-11-10.md` §3(d) and the archive.
