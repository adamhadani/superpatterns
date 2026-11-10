# W90 — plan for a rigorous proof of c₂₁ < 1 (NOT a proof)

Status: **plan and partial reductions only.** Nothing in this file is claimed as a theorem except where it
restates `proof.md`. It records how far the attempt of 10 November 2026 got and exactly what is missing, so that
the next session does not have to rediscover it.

## 1. Reduction to sparse swaps

By Theorem 1 (`proof.md`), flipping more blocks 12 → 21 only lowers containment. Fix K and let W = W_K be the
identity pattern with adjacent transpositions at positions (π_j + 1, π_j + 2), π_j = 2Kj (j ≥ 1). Writing
I_{2K−2} = 12^{⊕(K−1)} and flipping all of those blocks gives 21^{⊕}; hence 2·L₂₁ ≤_st N_W + 2K, where N_W is the
length of the longest contained prefix of W. **So c₂₁ < 1 follows from liminf (E LIS − E N_W)/T > 0** for one K
(T = √n; Poissonised square [0,T]² of intensity 1).

Let W^{(j)} have only the first j swaps. Then (Corollary 3 of `proof.md`, flips taken from the south-west end)

  E LIS − E N_W = Σ_{j ≥ 0} Cost_j,   Cost_j = Σ_{b ≥ 0} E[(a − 1)/F]_{α = W^{(j)}[1..π_{j+1}], β = I_b} ≥ 0.

The suffix β is increasing at every stage; this is what makes the stage tractable (the pattern after the flipped
block is shift-invariant).

## 2. What a stage looks like

Put p = π_{j+1}, λ(z) = max{t : SW(z) ⊇ W[1..t]} (the prefix-level function of the *full* pattern; for λ < p it
coincides with that of W^{(j)}, so it does not depend on j). The front F_p = ∂U_p is the level-p curve of λ; fronts
of different stages are disjoint level curves of one function. Conditionally on the explored region U_p^c the
points in U_p are a fresh Poisson process; write h(z) = LIS of fresh points strictly NE of z. Then

  Cost_j = E[X − Y],  X = LIS of fresh points in U_p,  Y = 2 + max{h(a∨b) : (a,b) fresh inversion with a∧b ∈ U_p},

and the level-b fibre has inside set {q fresh : h(q) ≥ b}.

Minimal points of U_p are Poisson points u_1, u_2, … (a decreasing sequence); between consecutive ones the
explored region has an outer corner. A **defect lens at the notch (u_k, u_m), m > k**, level b, is: three fresh
points p₁ = (x₁,y₂), p₂ = (x₂,y₃), p₃ = (x₃,y₁) with x(u_k) < x₁ < x(u_{k+1}), y₂ > y(u_k), y(u_m) < y₁ < y(u_k),
x(u_m) < x₂ < x₃, y₃ > y₂; two fresh points v₁ ∈ (x₂,x₃) × (y₃,∞), v₂ ∈ (x₃,∞) × (y₂,y₃) with h(v₁) = h(v₂) = b − 1;
no fresh point with h ≥ b − 1 above-right of (x₃,y₃); and {q : h(q) ≥ b} = {p₁,p₂,p₃}. Then the board is the 3×3
square minus (x₁,y₁) ∉ U_p and (x₃,y₃) ∉ S_b, F = 3, a = 2, and the fibre contributes 1/3 (checked against
Proposition 4(c)). Only ONE horizontal gap x(u_{k+1}) − x(u_k) ≥ r₀ is needed (or, by symmetry, one vertical gap).

Consequently  **Cost_j ≥ (1/3)·P(for some b the level-b inside set is a defect lens).**

## 3. The gadget (bonus planting)

Everything is conditional on the explored region; only fresh points are resampled.

**Good notch.** Consecutive minimal points u_{k−1}, u_k, u_{k+1}, u_{k+2} of the front such that the four gaps
x(u_{k+1}) − x(u_k), x(u_{k+2}) − x(u_{k+1}), y(u_{k−1}) − y(u_k), y(u_k) − y(u_{k+1}) all lie in [r₀, R].
Its *cell* is C_k = (x(u_k), x(u_{k+2})) × (y(u_{k+1}), y(u_{k−1})) ∩ U_p and z_k = (x(u_{k+2}), y(u_{k−1})) is the
cell's north-east corner. The point of the cell is that U_p ∩ SW(z_k) = C_k: no fresh point outside the cell is
below-left of anything planted inside it.

**Deficit.** Fix a designated location c* in the upper-right part of the cell. Let Π^out be the fresh points
outside C_k, X^out = LIS(Π^out), and D_k = X^out − h^out(c*) ≥ 0, where h^out(z) is the LIS of Π^out strictly
north-east of z. D_k is measurable with respect to the explored region and Π^out.

**Planting.** Empty the cell and put in it: the lens p₁, p₂, p₃ (p₁ above the notch rectangle, p₃ to its right,
p₂ north-east of p₁ and north-west of p₃), then v₁ ∈ (x₂,x₃) × (y₃, ·), v₂ ∈ (x₃, ·) × (y₂,y₃), then an increasing
run c₁ < … < c_s = c* with v₁, v₂ < c₁, all inside the cell, s = D_k + 3. This is an open set of cell configurations
of Poisson probability ≥ δ(R, r₀, D_k) > 0.

**Check list** (done on paper; to be written out in full before any use). Write h for h_new.

 * No fresh point outside the cell is below-left of a planted point, so a chain that uses planted points starts
   with planted points. Along the run, h(c₁) ≥ (s − 1) + h^out(c*) = X^out + 2, while every outside point q has
   h(q) = h^out(q) ≤ X^out − 1.
 * Therefore h(v₁) = h(v₂) = h(c₁) + 1 (their only continuations of that length go through c₁), and with
   b := h(c₁) + 2 we get h(p₂) = h(p₃) = b, h(p₁) = b + 1, h(v_i) = b − 1, h(c_i) ≤ b − 2, h(q) < b − 1 for q outside.
   The level-b inside set is exactly {p₁, p₂, p₃}.
 * (x₁,y₁) ∉ U_p because x₁ < x(u_{k+1}) and y₁ < y(u_k); (x₃,y₃) ∉ S_b because the only points with h ≥ b − 1 are
   p₁, p₂, p₃, v₁, v₂ and none of them is above-right of (x₃,y₃); the other seven cells of the 3×3 board are in
   U_p ∩ S_b (each is ≥ one of p₁, p₃ and ≤ one of p₂, v₂ up to the obvious coordinate checks).

 So the fibre is a pure 3-point defect fibre and contributes 1/3. The events "the cell of notch k carries the
 planted structure" are disjoint for different k (the level-b inside set is a function of the configuration), so

   **Cost_j ≥ (1/3)·E[ Σ_{k good} δ(R, r₀, D_k) ] ≥ (δ(R,r₀,D)/3)·P(G_j(D)),**

 G_j(D) = {some good notch k of the front F_p has deficit D_k ≤ D}.

## 4. What is missing

**Lemma needed (start regularity).** There are R, r₀, D and c > 0 such that for all large T and at least half of
the stages j in the bulk, P(G_j(D)) ≥ c.

Equivalently: with probability bounded below, the optimal fresh chain can be started, at bounded loss D, from the
corner of the cell of a good notch of the front F_p. The front is a level curve of a
complicated explored process and the starting point is an argmax, so there is a selection effect to control.
Two ways it could be closed:

 (a) *Near-maximiser multiplicity.* Show E #{boxes along the front within deficit D of the optimum} ≤ e^{CD}.
     Then rich boxes (probability super-exponentially small in their richness) and dense-front boxes cannot carry
     the start with probability > ½. This is a statement about point-to-curve Poissonian last passage percolation;
     it is known heuristically (local Brownian behaviour, count ≍ D³) and should follow from the moderate-deviation
     estimates for Poissonian LPP used by Basu–Sidoravicius–Sly, but I did not find an elementary proof and did
     not verify that their estimates apply to a rough random front.
 (b) *One reference path.* The coarse-path union bound shows that along any ONE chain-like copy at most a θ
     fraction of positions is bad (rich box, thin margin). It closes the single-swap case α = I_p, β = I_b — there
     the reference is the LIS geodesic, the same for all p — and would give: *one adjacent transposition in the
     identity costs at least ε₁ > 0 in expected length, uniformly in n, for most positions p*. For many swaps the
     reference copy changes with the stage and the averaging is "diagonal"; I found no deterministic relation
     between the optimal copies of W^{(j)} for different j that would restore it. Dead ends tried: random gaps
     (averages over a window of ONE copy but the window is still stage-specific); telescoping in another order
     (swaps after the flipped block destroy shift-invariance; periodic bonus of one full period realigns the phase
     but then partial copies are phase-slipped patterns with no pointwise comparison); comparing with the union of
     single-swap costs (Theorem 1 gives only the maximum, not the sum).

## 5. Numerical targets that would support the lemma

 * Empirical law of the number of fresh points in the top two levels at a stage, and of the deficit of the
   nearest good-notch box (should be tight in n).
 * Frequency of pure 3-point lenses at the critical level per stage (times 1/3 it is a lower bound for the
   per-block cost 0.0025 measured in `out/hybrid_n*.txt`; how much of the cost do 3-point lenses explain?).

--------------------------------------------------------------------------------------------------
# Addendum — second, time-boxed attempt (10 November 2026, about two hours). Outcome: not proved.

Nothing below is a theorem unless it says "checked". It supersedes §3–§4 where they differ.

## A1. An exact formula that is easy to evaluate (checked)

For a stage (prefix α, increasing suffix), with X = longest increasing chain of fresh points beyond the front and
Y = 2 + best increasing continuation after a front-anchored inversion,

  Cost = E[X − Y] = E[ Σ_{b ≥ Y−1} (1 − 1/a_b) ],

where a_b is the number of valid fillings without a D-inversion in the level-b fibre of the configuration (the
realised level-b filling has no D-inversion exactly when b ≥ Y − 1). `fibre_cost.py` evaluates the right-hand side
by brute force over fillings.

 * Exact check on all of S_n: n = 8: both sides sum to 1; n = 9: both sides sum to 46 (80 + 6 + 6 realised defect
   levels, each worth ½). Files `out/fibre_exact9.txt` and the command in the script header.
 * At n = 10⁴, flips 1…63, 120 000 permutations (`out/fibre_table.txt`): formula 0.15641 ± 0.00083; direct
   E[LIS − N₆₄] on the same permutations 0.153 ± 0.012; the C program gave 0.163 ± 0.017 on other permutations.
   The formula is the same quantity with about fifteen times less noise.
 * Per stage the contribution is 0.0024–0.0027, flat across the stage range. Essentially every contributing level
   has a_b = 2; the inside set has 3 points in 20% of the cases, 4 in 28%, 5 in 23%, 6 in 16%, 7–8 in 14%; the level
   is one or two below the top. So a stage has an ambiguous fibre with probability ≈ 0.5%, a pure 3-point lens with
   probability ≈ 0.1%. The lemma asks only that this be bounded below.

## A2. Two simplifications of the problem (reasoned, not written out)

 1. *The fresh field is an independent environment.* For a minimal point u of the front, the best fresh chain
    from u is the point-to-point LIS from u to the corner (T,T) in a Poisson process independent of the front. So
    X = max_k ψ(u_k) with ψ(z) = LIS(z → (T,T)) of an independent process, evaluated along an independent staircase.
 2. *Resample the rectangle between two points of an optimal copy, not a grid box.* Take e < x on an optimal copy
    with g copy points strictly between them, both at levels in the increasing run before the swap. Empty the open
    rectangle (e, x) and plant in it: an increasing run (long enough that its levels exceed those of every outside
    point below-left of x, i.e. more than g points), two incomparable points u₁, u₂ at the swap level (they create
    the notch), the lens, v₁, v₂, and a second run of more than g points ending below x. Chains in a rectangle are
    invariant under (x,y) → (λx, y/λ), so the probability of the planted configuration depends only on the AREA of
    the rectangle and on g — not on its shape, and not on the front. The deficit is at most g automatically. The
    only condition on the pair is that the area lie in a fixed range [g²/Λ, Λg²].

    With this gadget the stage is good as soon as one of the ≈ K/(g+1) consecutive segments of an optimal copy in
    the window before the swap spans a rectangle of area in that range.

## A3. What this settles and what it does not

 * **One swap (expected to be provable by elementary means; not written).** For α = I_p, β = I_b the optimal copy
   is an LIS geodesic, the same for every p. A first-moment bound over chains of anchors, with the exponential
   tilt e^{−s(Σw+Σh)} (which removes the logarithmic divergence from extreme aspect ratios: ∫∫ f(wh) e^{−s(w+h)} dw dh
   = ∫ f(A)·2K₀(2s√A) dA < ∞), shows that with high probability no geodesic has more than a θ fraction of
   bad-area segments. Hence (1/T) Σ_p [E LIS − E N(I_p ⊕ 21 ⊕ I_∞)] ≥ ε₁ > 0: one adjacent transposition at a
   typical position costs a positive constant, uniformly in n. This would be a theorem but does not give c₂₁ < 1.
 * **Many swaps (open).** The reference copy changes with the stage, and the stage only looks at one window of it
   (the first ≈ K positions after the previous swap). A bad stage therefore means that this particular window
   consists entirely of bad-area segments, and the fraction statement above cannot be transferred. Two estimates
   would close it:
   - (E1) *Local increments of ψ.* For z in the bulk, P(ψ(z) − ψ(z + (w,0)) ≤ w/3) ≤ Ce^{−cw}, and the same
     vertically. I tried to derive it from superadditivity and independence of the strip to the left of an optimal
     chain; the argument closes only if the chain is not flat at its start, which is the statement being proved.
     In the literature this is obtained by comparison with the stationary Hammersley process (Cator–Groeneboom;
     Pimentel, "Local behaviour of Airy processes"; the Poissonian toolbox in Basu–Sidoravicius–Sly). I did not
     check those statements against what is needed here.
   - (E2) *Multiplicity of near-optimal windows.* E[number of windows within deficit D of optimal at a given level]
     ≤ (CD)^D, by a Mecke-formula argument: planting D + 1 points in a near-optimal window makes it the unique
     optimum, and these events are disjoint. With (E2), a rare local structure of weight ε^K on the optimal copy at
     a given level has probability ≤ ε^K (CK)^K, small for suitable Λ. Sketched only.
   With (E1) and (E2) the bad-stage probability is ≤ ½ for K large, giving Σ_j Cost_j ≥ cT and c₂₁ < 1.

## A4. Dead ends of this attempt

 * Stationary boundary conditions (sources and sinks) to get exact independence of increments: boundary points can
   be inside points when the prefix or suffix is increasing, and then fibres are not uniformly distributed.
 * Counting bad windows over all stages by a union bound over "one window per front": entropy ≈ J·log T.
 * Bounding flat initial segments by Talagrand concentration plus curvature of 2√(xy): needs the difference of
   two passage times to (T,T) from nearby points, which concentration of each one separately does not control.
 * Grid boxes instead of pair windows: need margins and a regular front; both are selection problems at an argmax.
