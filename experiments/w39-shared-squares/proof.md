# Shared squares: simultaneous containment of monotone inflations

10 September 2026. Complete argument using the classical LIS lower-tail
theorem. Novelty has not been established; this is a consequence worth
recording, not a claim to resolve general Alon universality.

**Theorem.** Fix ε>0 and A>0. There is K_(ε,A)>0 such that, for all
sufficiently large k, a uniform permutation of length ceil((1/4+ε)k²)
simultaneously contains every inflation of an arbitrary permutation by
increasing or decreasing blocks of total length k, each block having
length at least ceil(K_(ε,A)√log k), with failure probability at most k^(−A).

An inflation ρ[α₁,...,α_m] replaces position i of ρ∈S_m by a block α_i
of consecutive positions and consecutive values. The relative value order
of the blocks is ρ. Their sizes may differ, and each α_i may independently
be increasing or decreasing.

## The only external probabilistic input

For any C>1/4 there are c_C>0 and a_C such that a Poisson process with
mean Ca² on a square lacks an increasing subsequence of length a with
probability at most exp(−c_Ca²), for integer a≥a_C. The same holds for a
decreasing subsequence by reflection.

To obtain precisely this formulation, choose 1/4<C₁<C and
1/√C₁<x<2. Set m=floor(C₁a²). The probability that Poisson(Ca²)<m is
exp(−Ω_C(a²)), by the Poisson Chernoff bound. Conditional on having at
least m points, retain the first m of an iid uniform-point construction;
their standardized order is uniform in S_m. For large a, a<x√m, and
Deuschel–Zeitouni, Theorem 1, gives P(LIS_m<x√m)=exp(−Ω_x(m)). Adding
the two errors and decreasing the exponent constant gives the claimed
Poisson estimate. This uses a fixed x<2, with no moderate-deviation or
uniform-near-edge claim. [Primary source, Theorem 1](https://arxiv.org/html/math/9803035v1).

## One event for every skeleton and every block composition

Work in the unit square with Poisson intensity Ck², where
C=1/4+ε/2. Let L≥a_C. For integers a,s,t satisfying L≤a≤k and
0≤s,t≤k−a, form

    Q(s,t,a)=(s/k,(s+a)/k) × (t/k,(t+a)/k).

There are at most (k+1)³ squares. Each contains Poisson(Ca²) points
after rescaling. Let E be the event that every such square contains both
an increasing and a decreasing subsequence of length a. A union bound over
squares and the two directions yields

    P(E fails) ≤ 2(k+1)³ exp(−c_C L²).                                  (1)

No independence between these overlapping squares is required.

Fix any skeleton ρ and block sizes a₁,...,a_m≥L summing to k. Put

    s_i=Σ_(j<i) a_j,        t_i=Σ_(ρ(j)<ρ(i)) a_j.

On E choose a monotone subsequence of length a_i with the required
direction inside Q(s_i,t_i,a_i). The x intervals of successive blocks
are disjoint and correctly ordered, and their y intervals are disjoint
and ordered according to ρ. Within a block, its chosen direction supplies
α_i. Thus the union of these chosen points is ρ[α₁,...,α_m]. Because E
was specified without reference to ρ, the sizes, or the directions, this
proves simultaneous containment of the entire class on E.

Choose K with c_CK²>A+4 and L=ceil(K√log k). Equation (1) is o(k^(−A)).
To pass to n=ceil((1/4+ε)k²), construct the Poisson process from a count
M∼Poisson(Ck²) and an independent infinite iid uniform-point sequence.
When M≤n, its points are a subset of the first n points, whose order
standardizes to a uniform permutation. The error P(M>n) is
exp(−Ω_ε(k²)); together with (1) this proves the theorem. ∎

## Comparison and scope

For direct and skew sums alone, O(k²) diagonal/antidiagonal squares
suffice. The arbitrary-skeleton extension uses O(k³) squares and the same
order of minimum block length. This strengthens the defect-free subclass
of W37, which required each monotone run to have length at least √k log k.
Arbitrary small defect blocks are not included in this theorem.

The condition is on blocks of consecutive positions AND consecutive
values. It does not cover general interleaved grids or a typical uniform
target. In particular, the repeated-21 family has block length 2 and lies
outside the stated regime. Applying the eight dihedral symmetries causes
only a constant-factor union bound (the inflation class is itself closed
under these symmetries).

This is a concrete example of controlling a polynomial family of host
certificates instead of union bounding a separate construction over all
target permutations. Extending such shared certificates to interleaving
is the next unresolved step.
