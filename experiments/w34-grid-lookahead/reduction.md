# Repaired grid reduction with polynomially small failure

10 September 2026. This replaces §3 of the original W34 proof. The former
H_b assumption (no repetition in a window of b+1 visits) did not imply the
Ω(r) revisit separation used there. Also, a stationary mean cannot be
substituted for a conditional-on-the-partition mean. Both issues are repaired
below. The original first-passage functional and scaling lemma are unchanged.

**Theorem 3.4, corrected.** Fix b≥1, η>0, A>0, and C>C_b^mix, where

    C_b^mix = [(E K_b+E K_(b+1))/(2(2b+1))]².

Let k=rh and let π_τ∈G(r,h) have a deterministic strip-visiting sequence
in which any successive visits to the same strip have index difference at
least ηr. Assume min(r,h)≥(log k)³. For all sufficiently large k, uniformly
over such visiting sequences,

    P(π_τ not contained in Π_(Ck²) in the fixed-strip model) ≤ k^(−A).       (1)

The same statement in a uniform permutation of length ceil((C+ε)k²) holds
for every fixed ε>0, with an additional exp(−Ω_ε(k²)) coupling error.
Uniformity over individual patterns is the meaning of (1); simultaneous
containment requires a further union bound or a shared event.

## Construction and boundary blocks

Use W34's scaled coordinates, with clock budget k and each strip's vertical
budget h. Partition the integer visit line by an independent stationary
renewal process with block lengths b,b+1, each chosen with probability 1/2
at a renewal. Its phase Z_t=(length,position) has stationary probabilities

    P(Z_t=(l,j))=1/(2b+1), l∈{b,b+1}, 0≤j<l.

Intersect the partition with visits 0,...,k−1. The first and last blocks
may be partial; each has at most b+1 visits. Every block has distinct strips
for large k because ηr>b+1. Choose

    L²=(b+1)(A+3) log k/C.                                              (2)

For a block, put a*=max(a, e_s over its strips), and inspect each square
(a*,a*+L)×(v_s,v_s+L). Set its explored edge to a*+L. Choose the x-ordered
path minimizing x-advance plus the sum of vertical increments. This is
exactly the existing safe-clock rule on feasible blocks.

To define all random variables without conditioning on success, on an
infeasible block mark failure, assign artificial x-advance L and all its
vertical increments L, and continue the exploration. The artificial points
are bookkeeping only. On the event of no marked failure all choices are
actual points. This continuation keeps all increments in [0,L] and retains
freshness, so independent-increment estimates may be applied unconditionally.

Given the partition and earlier revealed windows, each newly inspected
window is conditionally a translated independent Poisson(C) square. Its
left edge is at least the explored edge of its strip. The safe edges are
stopping boundaries for the independent strip processes; Poisson independent
increments beyond these boundaries give the claimed conditional law.
Iterating this conditional law makes the relative block output vectors
independent given the partition. Their laws depend only on block length.

Write X_l^L,Y_(l,j)^L for the x and individual y outputs of a block of size l,
including the artificial convention on infeasibility. For the finite list
1≤l≤b+1, their means converge as L→∞ to the unwindowed means. Indeed the
unwindowed optimizer lies in the window whenever K_l<L, and K_l is bounded
by a sum of l corner-greedy costs with Gaussian tails. On infeasibility the
artificial outputs are at most L and its probability is at most
l exp(−CL²/l). These observations imply convergence in mean. In particular
all these means are bounded by a constant M_b for large L. Scaling gives

    E X_l^∞ = Σ_j E Y_(l,j)^∞ = E K_l/(2√C).

Define ρ=(E K_b+E K_(b+1))/(2√C(2b+1))<1. Fix δ>0 with ρ+6δ<1.
The two stationary mean rewards

    ρ_x^L=(E X_b^L+E X_(b+1)^L)/(2b+1),
    ρ_y^L=(Σ_j E Y_(b,j)^L+Σ_j E Y_(b+1,j)^L)/(2b+1)

both tend to ρ. They need not be equal at finite L. For large k both are
at most ρ+δ.

## Four failure estimates

**Infeasible blocks.** Divide each square into l vertical subwindows of
width L/l and use one subwindow in each successive strip. If these l
subwindows are occupied there is a feasible path. Hence the union bound,
including partial boundary blocks, is at most

    (b+1)k exp(−CL²/(b+1)) = (b+1)k^(−A−2).                             (3)

**Safe-clock offsets.** An offset is at most L and can occur only when the
clock has advanced less than L since the start of a strip's previous block.
Between two such blocks there are at least
m=floor(ηr/(b+1))−2 complete blocks, and m≥ηr/(2(b+1)) for large k.
Each block advances the clock by at least a variable distributed as
min(L,E), E∼Exp(CL): use the first point's x coordinate in its first square,
and the artificial value L on failure. These lower bounds can be sampled
independently by the conditional freshness law. For m≥2, a sum of these
truncated variables at most L entails no truncation, outside a null event.
Thus each possible offset has probability at most

    P(Gamma(m,CL)≤L) ≤ (eCL²/m)^m.

Union over at most k revisits gives k(eCL²/m)^m. With r≥log³k and (2), this
decays faster than every inverse polynomial in k, uniformly in τ.

**The x budget: renewal reward followed by conditional concentration.**
For an iid full-block length D∈{b,b+1}, the variable

    E X_D^L − ρ_x^L D

has mean zero and is bounded by a constant depending only on b,C. The
number of complete blocks is random, but at most k. A union bound over
all partial sums of this iid centered sequence and Hoeffding's inequality
give a bound k exp(−cδ²k) for an excess δk. Partial initial and final blocks
add at most 2L to the conditional mean. Therefore, outside this event,

    Σ_blocks E[X_block | partition] ≤ (ρ+2δ)k+2L.

Conditionally on the partition the actual x outputs are independent in
[0,L], so their sum exceeds this conditional mean by δk with probability
at most exp(−2δ²k/L²). The total x cost is at most (ρ+3δ)k+2L<k off
these events and the offset event. This explicitly controls the random
conditional mean; stationarity alone was insufficient in the old proof.

**The y budgets: mixing of the phase and conditional concentration.**
The phase chain Z_t is finite, irreducible, and aperiodic: its return cycles
include lengths b,b+1. Thus there are constants B_b,c_b>0 such that its
transition law after d steps, from any starting phase, differs in total
variation from stationarity by at most B_b exp(−c_b d). For completeness,
irreducibility and the coprime cycle lengths imply that a sufficiently high
power of its transition matrix is strictly positive. Its minimum entry
gives a Doeblin coupling, and iteration gives this exponential estimate.

For a fixed strip, its h deterministic visit times are at least ηr apart.
By sequential maximal coupling, their phases jointly differ from h
independent stationary phases by at most h B_b exp(−c_b ηr). The reference
conditional y-mean at a phase (l,j) is E Y_(l,j)^L, bounded by M_b; its
stationary mean is ρ_y^L≤ρ+δ. Hoeffding therefore bounds an excess δh in
the sum of reference means by exp(−2δ²h/M_b²), plus that coupling error.
Replacing reference means at the at most two boundary-block visits costs
at most 2L. Given the partition, this strip's outputs belong to distinct
blocks, are independent in [0,L], and have their actual conditional means.
A second Hoeffding bound exp(−2δ²h/L²) controls an excess δh. Thus its
vertical cost is at most (ρ+3δ)h+2L<h except with probability at most

    exp(−2δ²h/M_b²) + h B_b exp(−c_b ηr) + exp(−2δ²h/L²).                 (4)

After summing (4) over r strips, all terms decay faster than every inverse
polynomial because min(r,h)≥log³k and L² is a fixed multiple of log k.
The same is true of the x-budget and offset errors. Together with (3) this
proves (1) for large k. On the successful event the budget and ordering
invariants give an actual copy of π_τ in the original square. ∎

## Consequences and remaining limitation

W36 proves C_b^mix→1/4. For fixed ε>0 choose b with
C_b^mix<1/4+ε/2. Apply (1) with C=1/4+ε/2 and then couple to the fixed
host of length ceil((1/4+ε)k²).

In a tilted grid the revisit difference is r, so take η=1. There are at
most k pairs (r,h) with rh=k, and at most eight dihedral images per pair.
Taking A=3 and union bounding shows that the same random host simultaneously
contains all these tilted grids with min(r,h)≥log³k, and their images, with
failure O(k^(−2))+exp(−Ω_ε(k²)).

The family of all row-permutation sequences with the separation hypothesis
can be much larger than polynomial. The present estimates do not establish
simultaneous containment of that entire family, and the old weaker H_b
hypothesis remains insufficient for this proof.

Counterexample to the old inference: r=20,b=2, alternating rows
p=(0,1,...,19), q=(0,1,19,2,3,...,18) satisfy H_b; strip 19 is visited at
indices 19,22,59,62. Differences 3 contradict the claimed r−2b=16 bound.
