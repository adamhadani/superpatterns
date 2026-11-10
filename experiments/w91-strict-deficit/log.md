# W91 — log (10 November 2026)

Goal: write the single-swap theorem announced at the end of W90's plan
(`../w90-layered-deficit/strict-deficit-plan.md`, Addendum A3) and test the planted gadget; then see how far the
same tools go for many swaps. Statements and proofs are in `proof.md`; this file is the chronology, including what
did not work.

## 0. Starting point

W90 left: (i) the exact stage formula Cost = E Σ_b (a_b − 1)/F_b; (ii) a "pair-window" gadget — empty the rectangle
between two points of an optimal copy and plant a lens surrounded by two increasing runs; (iii) a sketched
first-moment bound for thin segments; (iv) for many swaps, two missing estimates (E1), (E2).

## 1. Three simplifications found while writing the single-swap proof

 1. **No runs are needed when the two anchors are consecutive on the copy.** With no copy point between e and x,
    every point outside the rectangle and below x has level ≤ ℓ(e), so the two notch points u₁, u₂ can sit directly
    above e. The plant is then 7 points: u₁, p₁, u₂, p₂, v₁, p₃, v₂ = 3 4 1 6 7 2 5 — exactly the pattern 3416725 of
    Burstein–Pantone. (The runs of the W90 plan were only there to beat the levels of outside points when there
    are g > 0 copy points in between.) An 8-point variant 1 ⊕ 3416725 shifts the lens by one level; it is needed
    only for parity in Theorem B.
 2. **Only a lower bound on the area is needed.** The reference event is "rectangle empty" (probability e^{−A}),
    the planted event has probability e^{−A}A⁷/(7!)². The ratio A⁷/(7!)² is increasing in A, so fat rectangles are
    harmless; W90's plan asked for the area in a bounded window, which was unnecessary.
 3. **The comparison is an identity, not an inequality** (Lemma 3.1): E #{planted pairs} = E Σ_{empty compatible
    pairs} area⁷/(7!)². The outside conditions must be the same on both sides, which is Lemma 2.2.

Hand check of the smallest case, σ = 1 4 5 2 7 8 3 6 9 (e = 1, x = 9, s = 0, p = 2, b = 2). It contains 123456
(1 4 5 7 8 9). For 124356 = I₂ ⊕ 21 ⊕ I₂ one needs an inversion (hi, lo) with an increasing pair below-left of both
and an increasing pair above-right of both. The inversions of σ are (4,2), (5,2), (4,3), (5,3), (7,3), (8,3), (7,6),
(8,6). For (4,2), (5,2), (4,3), (5,3) only the value 1 is below-left; for (7,3), (8,3), (7,6), (8,6) only the value 9
is above-right. So σ avoids 124356, as Lemma 2.3 predicts (realised filling 231, no D-inversion).

## 2. Multiplicity, and the tie-break

First version of the counting: "each planted pair gives a lens level, so #lens levels ≥ #planted pairs". False as
stated: two anchors e, e′ at the same level, both below the same planted lens with nothing else in the L-shaped
region between their rectangles, give two planted pairs and one lens. Found by thinking about which data pin the
anchor; confirmed by `gadget_check.py tie` and by the random tests (4975 of 15 512 cases have extra pairs when the
tie-break is dropped). Repair: conditions (O5), (O6) keep only the north-west-most anchor on each side. They hold
for consecutive points of the *leftmost* optimal copy (Lemma 2.5), and with them the map to lens levels is
injective (Lemma 2.4). Afterthought (Remark 2.6): a stage has at most one lens level, so |𝒢_{p,s}| ≤ 1.

## 3. Theorem A (one transposition)

Thin steps of the leftmost longest chain are handled by a first moment over all chains with the tilt
e^{2T − Σ(w+h)} (Lemma 4.2): a thin step then costs P(E₁E₂ < A₁) ≤ 2√A₁ instead of the divergent
∫∫_{wh<A₁} dw dh. This is the "2K₀(2s√A)" computation of the W90 plan with the cruder bound 2√A₁.

## 4. Theorem B (many transpositions) — the idea that made it work

Theorem 1 of W90 allows un-flipping *any* set of blocks, so 21^{⊕m} can be compared with W_S for any S, hence with
a random S. If the j-th transposition is placed uniformly in a window of K consecutive blocks, then for every
position in the window the prefix is the same pattern Π = W_{S<j} followed by an increasing tail, so **one
reference copy (the leftmost optimal copy of Π) serves the whole window**, and the plant sizes 7 and 8 cover all
2K steps of the window. A stage therefore pays as soon as one step in the window is not thin. In the tail, levels
of Π behave exactly like LIS levels (Lemma 2.1), so the deterministic lemmas are the same as for one transposition.

What is not available is the budget argument (Σw ≤ T, Σh ≤ T) for a window of bounded length.

*First version (superseded, kept in the scratch copy only).* K ≈ 2 ln T and a thin threshold A₁ ≈ 1/(8 ln T): then
no chain of 2K thin steps exists anywhere in Q_T (expected number T²·(A₁(1+ln(T²/A₁)))^{2K}), every window has one
usable step, and the bound is √n/(ln n)¹⁰ = √n/(K²·A₁⁻⁸).

*Second version (the one in proof.md).* A window of 2K steps of an optimal copy has a budget of its own: a chain
inside its span has fewer than 2K points, and with high probability every rectangle of area ≥ 4k² spanned by two
points of P contains a chain of k points (Lemma 4.2, k = 2K ≥ 90 ln T). So the span has area < 4(2K)², i.e.
(Σw)(Σh) ≤ 16K². A hyperbolic budget is a union of O(log T) rectangular budgets W ≤ a, H ≤ b with ab = 8k², and
the tilt e^{k(1−W/a)+k(1−H/b)} is invariant under (x,y) ↦ (λx, y/λ); so the count of Lemma 4.1 applies with a
*constant* thin threshold (Lemma 4.3). More than half of the 2K steps of every window are then usable, each
stage costs a constant, and the only loss is the spacing K ≈ 45 ln T between transpositions: √n/ln n.

## 5. Dead ends of this session

 * Thin threshold 1/(8 ln T) (first version of Theorem B): unnecessary, see §4.
 * Planting an increasing run to reach a prescribed level from a non-thin step further back in the window:
   probability cost A₁^K per stage; with K ≈ ln T this is T^{−c ln ln T}. Replaced by randomising the position.
 * Pair windows with g ≥ 1 interior copy points, to use the area of a multi-step rectangle: the ratio
   (planted)/(reference) is ≈ A^{m−g} and still vanishes as A → 0; and flat windows have all sub-rectangles thin.
 * A staircase path can have every bounded sub-window thin although its bounding rectangle is fat (steps
   w_i = W·2^{−i}, h_i = H·2^{−(K−i)}), so "fat window ⇒ some fat short sub-window" is false.
 * Super-additivity of costs, c(t | S) ≥ c(t | ∅), which would give c₂₁ < 1 from Theorem A: no such inequality is
   known, 1234/1243/2134/2143 give equality, and W90's data (0.00227 per block for all blocks flipped against
   ≈ 0.0025 for the first blocks) suggest the opposite sign. Not pursued.
 * A bounded number J of transpositions with windows of length ≈ T/J, using Lemma 4.2 on each window: the thin
   threshold must shrink like e^{−cJ}, total cost J·e^{−cJ} = O(1).
 * Inserting empty strips to fatten a thin step: costs e^{−(strip area)} ≈ e^{−δT}.
 * A front-regularity estimate from local data: "the level is constant along a horizontal segment of length w"
   is implied by a flat chain in the slab below it, which exists; the estimate needs the global direction of the
   level lines (this is (E1)).

## 6. Checks

`run_checks.sh` → `out/gadget_checks.txt` (table in proof.md §8). First run and second run (with one extra
counter) agree. The Monte Carlo check of the resampling identity uses a one-point plant because the 7-point event
is too rare to sample.

## 7. Literature (10 Nov 2026)

Searches for a prior statement that a specific pattern is strictly harder than the identity for random
permutations, or for any lower bound on the containment threshold of 2 1 4 3 ⋯ above k²/4: nothing found (He–Kwan
arXiv:1911.12878 and the Wikipedia article "Superpattern" state the conjecture with the identity as the only
obstruction; Burstein–Pantone arXiv:1402.3842, J. Comb. 6 (2015), is purely enumerative). As in W90, a specialist
should be asked before any announcement.

## 8. Exact leading-order check of Lemma 3.1 with the real plant

As T → 0 the first non-zero term on the left of Lemma 3.1 (p = 2, s = 0, empty block word) comes from nine points
with order type 1 4 5 2 7 8 3 6 9: e^{−T²}·T¹⁸/(9!)². The first term on the right comes from two points e < x:
e^{−T²}·(T⁴/2)·½·(E|U−U′|⁷)²·T¹⁴/(7!)² with E|U−U′|⁷ = 1/36 for independent uniforms on [0,1], i.e.
e^{−T²}·T¹⁸/(4·36²·(7!)²). Since 9! = 72·7! and 4·36² = 72², the two agree exactly.

## 9. Verification (norm 1)

 * Main session: after writing, every lemma of §1–§6 was re-derived line by line a second time (levels and heights
   of the seven planted points, the nine board cells, both exchange steps of Lemma 2.4, the index bookkeeping of
   Proposition 6.1, each numerical constant — `out/constants.txt`).
 * Independent reviewer (separate agent, instructed to attack; report `out/review-1.md`): re-derived §1–§6 of both
   versions (√n/(ln n)¹⁰ and √n/ln n — the file was improved while the review ran, and the reviewer noticed and
   covered both). Verdict: no fatal error, no repairable gap; nine under-justified steps (all incorporated into
   proof.md: U1 fibre-measurability of "lens", U2 symmetry of the exchange steps, U3 open rectangle in Mecke,
   U4 range of r in Lemma 4.3, U5 rounding, U6/U8 Cauchy–Schwarz, U7 size of T_B, U9 three sentences in
   Corollary C) and seven cosmetic points.
 * Independent code by the reviewer (`review/`, raw outputs `review/out/`), deciding containment directly rather
   than through fibres: 47 428 plantings, all as Lemma 2.3 predicts; negative controls fail as they should;
   Lemma 2.5 on 70 144 pairs; (F3) and Lemma 1.1 exactly on S₇–S₉. The raw output files were read by the main
   session and agree with the report; the self-test was re-run from the repository copy.
 * Not externally refereed. Theorem B is one day old. Before any announcement it should be read by someone who
   did not write it and is not an AI system; the deterministic part is machine-checked on tens of thousands of
   random cases, the probabilistic part (§3–§6) rests on the written proof only.

## 10. Ideas for (H) that were not tried or not finished

 * *The reference content of the rectangle can be arbitrary.* The outside conditions do not see the rectangle,
   so P(lens at stage p) ≥ min_{A∈[A₁,A₂]} e^{−A}A⁷/(7!)² × E #{pairs with the outside conditions and area in
   [A₁, A₂]}, whatever the rectangle contains. More generally one may empty a "moat" D ⊃ R(e,x) of bounded area
   at cost e^{−|D|}. What is needed is then: with probability bounded below there are e < x in P and a bounded
   moat such that, after emptying it, (e,x) are consecutive points of the leftmost optimal copy at the right
   level with area R(e,x) ≥ A₁. Deleting the points of the copy inside a thin window may hand optimality to a
   different copy, so this needs an iteration that terminates in boundedly many rounds; not analysed.
 * *Near-optimal anchors count as well.* For e of tail level i and x > e with R(e,x) empty: (O2) is equivalent
   to ℓ(x) = i+1, (O3) to h(x) = h(e) − 1, and (O4) follows from h(e) ≥ max{h(r) : ℓ(r) = i} − 2 − s. So every
   front point within 2 of the best, with a first step to a minimal fresh point, contributes to the sum of
   Lemma 3.1 — not only the optimal copy. Derived on paper, not brute-forced, not used.
 * Both still need a statement about the local environment at an argmax of the point-to-corner passage time
   over the front (item 4 of proof.md §7).

## 11. c₂₁ < 1 without (H) (10 November 2026, evening)

Asked to attack (H) directly, I first rewrote the stage cost in "two fronts" form — given the outside points, the
inside points are a Poisson process on the region between the level-p front and the height-b front, so
Cost ≥ E Σ_b e^{−|G_{p,b}|}·Λ, with Λ the volume of lens placements in crossing notches of the two fronts. This is
cleaner than optimal copies but still needs tightness of the local picture at an argmax; not pursued further
(not written up, not verified).

What closed the question is unrelated to (H): **a rate of convergence for the superadditive mean ℓ(T) = E L₂₁(P_T)**.
Cutting an optimal copy where the upper-right corners of its blocks cross the antidiagonal x + y = 2T puts each
half in a rectangle of area ≤ T²; with Talagrand's inequality and a grid of ⌈4T²⌉ rectangles,
ℓ(2T) ≤ 2ℓ(T) + 45√(T ln T), hence c₂₁T − 200√(T ln T) ≤ ℓ(T) ≤ c₂₁T. Proposition 6.1 gives
2ℓ(T) ≤ 2T − 10⁻⁹⁴T/ln T. If c₂₁ were 1 the two would contradict each other. So c₂₁ < 1 (`proof-c21.md`).
In hindsight any deficit ≫ √(T ln T) at one scale suffices; the earlier W90 dead end "superadditivity of the
deficit" was the wrong question — the right one is the rate of convergence of E L₂₁ alone (Alexander 1994).

Verification: `proof-c21.md` §5; reviewer report `out/review-2.md`; reviewer's code and raw outputs `review2/`.
Statements checked against the user's copies of Alon–Spencer (Thm 7.7.1) and Last–Penrose (Thm 4.4).
Corrections after review: "2Y_n ≤ LIS" is false pointwise (σ = 21) — replaced by Y_n ≤ LIS and the expectation
form; median step of Talagrand spelled out; Bollobás–Brightwell is cited only for concentration (the cut
argument could not be confirmed there), Alexander and Rhee for the technique.

Status discipline: this is a claimed disproof of Alon's conjecture for small fixed ε, written and reviewed by AI
systems on one day. It is recorded as "proved here, not externally verified".
