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
