# Exact joint emptiness for canonical overlapping copies

10 September 2026 continuation. This completes W38's bounded overlap-(k−2)
task. It gives exact finite formulas and structural obstructions, not an
asymptotic second-moment bound. The formulas apply to every overlap j.

## 1. Compatible union types

Fix k≥2 and 0≤j≤k, and put m=2k−j. Let Z_(k,j) be the number of **ordered**
pairs (A,B) of leftmost-canonical k-copies with the same pattern and exactly
j shared points, summed over all target patterns. For j=k these are diagonal
pairs. Define leftmost-canonical as in W38: the open rectangle before each
selected point, between its two selected value neighbours, is empty.

A union type is (ρ,I,J), where ρ∈S_m, I,J⊆[m], |I|=|J|=k and I∪J=[m].
Require pat(ρ|I)=pat(ρ|J). Write the actual union points as
(x_a,y_(ρ(a))), where 0<x_1<…<x_m<1 and 0<y_1<…<y_m<1.
Put x_0=y_0=0 and x_(m+1)=y_(m+1)=1.

For each copy, a selected position b with previous selected position a
(a=0 at the start) and selected value-neighbour ranks L,U in the **union**
(using 0,m+1 at the ends) contributes the rectangle

    (x_a,x_b) × (y_L,y_U).

Call the type compatible if none of its m union points lies in any of these
rectangles for either copy. This is an order-only test: reject if
a<c<b and L<ρ(c)<U for any contributed rectangle and c∈[m]. Let T_(k,j)
be the compatible types. This rejects cross-blocking by the other copy's
exclusive points before any background emptiness calculation.

Let g_i=x_(i+1)−x_i and h_q=y_(q+1)−y_q, 0≤i,q≤m. Define a Boolean matrix
D of size m+1 by setting D_iq=1 iff some contributed rectangle has
a≤i<b and L≤q<U. Then the **union**, not the sum, of all forbidden
rectangles has area

    V_T(g,h)=Σ_i,q D_iq g_i h_q.

Both g,h belong to the m-dimensional simplex Δ_m={positive gaps summing
to 1}. In every integral below dg,dh mean Lebesgue measure on the first m
coordinates, with the final coordinate determined by the sum. Its volume
is 1/m!, not 1. Write Q=1−D entrywise and
a_i(h)=Σ_q Q_iq h_q, so 1−V_T=Σ_i g_i a_i(h).

## 2. Exact Poisson and fixed-host expressions

**Theorem 1.** For Π_λ, intensity λ on the unit square,

    E Z_(k,j)(Π_λ) = λ^m Σ_(T∈T_(k,j)) ∫_(Δ_m×Δ_m) exp(−λ V_T(g,h)) dg dh.       (1)

For a uniform permutation σ_n, n≥m,

    E Z_(k,j)(σ_n) = (n)_m Σ_T ∫_(Δ_m×Δ_m) (1−V_T(g,h))^(n−m) dg dh,            (2)

and the expectation is zero for n<m. Here (n)_m=n!/(n−m)!.

*Proof.* Represent σ_n by n iid uniform points and standardize. Every
ordered pair has a unique unordered union, unique x ordering of its union,
and unique (ρ,I,J). Compatibility is necessary and sufficient to ensure
that the inserted union points themselves do not violate either canonical
condition. Conditional on these points, the remaining n−m iid points
avoid the union of the forbidden rectangles with probability (1−V)^(n−m).
There are binom(n,m) choices of labels for the union. On its x-ordered
domain the density is m!; partition its y coordinates by ρ. The resulting
factor is binom(n,m)m!=(n)_m, with no further division for I,J: pairs are
ordered. Changing to gaps has Jacobian 1. This proves (2).

For (1), either apply the multivariate Mecke formula with the x ordering,
or Poisson-average (2):

    e^(−λ) Σ_(n≥m) λ^n/n! · (n)_m (1−V)^(n−m)
      = λ^m exp(−λ V).

The interchange is justified by nonnegativity. The latter derivation is
self-contained. The standard general identity is Last–Penrose,
[Theorem 4.4](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf). ∎

For the pattern-averaged second moment, divide E Z_(k,j) by k!, then by
μ_can² to obtain this overlap's contribution to R_can. Fixed-target versions
restrict T to types having that target. No equality of different targets'
second moments is implied.

## 3. Integrating out one entire gap vector

Let H_s(a_0,…,a_m)=Σ_(d_0+…+d_m=s) Π_i a_i^(d_i) be the complete homogeneous
symmetric polynomial, with H_0=1.

**Corollary 2 (exact rational evaluation).** With s=n−m,

    E Z_(k,j)(σ_n) = Σ_T ∫_(Δ_m) H_s(a_0(h),…,a_m(h)) dh.                       (3)

If H_s(a(h))=Σ_(|α|=s) c_(T,α) h^α, then

    n! E Z_(k,j)(σ_n) = Σ_T Σ_(|α|=s) c_(T,α) Π_q α_q! .                      (4)

All coefficients are nonnegative integers. Thus the formula avoids
alternating cancellation from expanding (1−V)^s.

*Proof.* For d_i≥0 with Σd_i=s, the elementary Dirichlet integral is
∫_(Δ_m) Π_i g_i^(d_i) dg=Π_i d_i!/(s+m)!. Expand (Σ_i g_i a_i)^s by the
multinomial theorem. The factorials cancel, giving
∫(Σg_i a_i)^s dg=s!/(s+m)! H_s(a). Its prefactor cancels (n)_m in (2).
Apply the same Dirichlet identity to the h monomials, using s+m=n. ∎

`overlap.py` evaluates (4) using integer polynomial multiplication and
Σ_(s≥0) H_s(a) z^s=Π_i(1−z a_i)^(-1). It groups only identical matrices,
without assuming additional symmetries. This is an exact finite algorithm,
not a polynomial-time algorithm in k: the number of union types can be large.

Independent verification uses direct replacement tests on every host
permutation, without rectangle or gap code. The following entries are
**sums over all n! hosts**, namely n! E Z_(k,k−2):

| k | n=k+2 | n=k+3 | n=k+4 | n=k+5 |
|:--|--:|--:|--:|--:|
| 2 | 8 | 88 | 784 | 6944 |
| 3 | 48 | 840 | 10696 | — |
| 4 | 276 | 7484 | — | — |
| 5 | 1648 | — | — | — |

All ten entries agree exactly. Overlap k−1 has no compatible union types
for k=2,…,5, also recovering W38's rigidity lemma in these checks.
The JSON retains all normalizing denominators and example types.

## 4. A two-point change can move the whole common correspondence

**Proposition 3 (full-shift family).** For every k≥2 there are two compatible
canonical k-copies with overlap k−2 for which every shared point has
different position rank in the two copies.

*Proof.* Let ρ of length k+2 be 2,1,4,3,6,5,…, with a final largest
singleton if its length is odd. Let I={1,…,k}, J={3,…,k+2}. Both restrictions
have the pattern of descending pairs, followed by a largest singleton
when k is odd. Every shared position c=3,…,k has rank c in I and c−2 in J.
The first copy uses consecutive positions starting at 1, so every open
preceding position window is empty. The second copy is also consecutive;
its only possible blocking points are positions 1,2 before its first
point. They have values 2,1, below the value 3 of its first point's lower
selected neighbour. Thus they do not block. Both copies are canonical. ∎

Consequently a reduction keeping only correspondences that fix the common
core is not exact, even at overlap k−2. For k=3,4,5, respectively 20 of 48,
120 of 276 and 640 of 1648 compatible types shift some common position.
These are counts of types, not their weighted probabilities. They do not
prove an asymptotically significant contribution. W38's proposed small
cost for shifted correspondences needs an estimate, not a local-exclusion claim.

**Proposition 4 (canonical clusters survive).** In the deterministic host
σ=21^(⊕r), the target τ=21^(⊕q), 1≤q≤r, has exactly binom(r,q) copies, all
canonical. The number of ordered pairs overlapping in 2s points is

    binom(r,q) binom(q,s) binom(r−q,q−s),                                    (5)

with out-of-range binomial coefficients interpreted as zero. In particular
the overlap 2q−2 count is binom(r,q) q(r−q).

*Proof.* All inversions of σ are its r individual blocks. Each descending
pair in a target copy must be a whole block, so copies correspond exactly
to q-subsets of blocks. For an upper point in a chosen block, all skipped
points before it have values below its lower neighbour in that same block.
For a lower point, the preceding selected position is adjacent. Thus all
copies are canonical. Choose the first q-subset, then the s shared and
q−s new blocks of the second subset to obtain (5). ∎

This is a deterministic obstruction to a uniform cluster-size bound. It
does **not** show divergence of R_can under a random host, since these hosts
may be rare. Any average bound must pay for both cluster size and its frequency.

## 5. Decision and next finite target

The joint-emptiness calculation is complete. It does not yet give usable
uniform control of all overlaps or a lower bound on μ_can; large sampling
is not the missing step. The most concrete alternative is stronger local
selection: among copies of a fixed pattern retain those having no
lexicographically earlier copy differing in at most two points. A global
lexicographic minimum always survives, and any two retained copies have
overlap at most k−3 (compare the lexicographically later one). This removes
the entire k−2 bin, but requires avoiding two-point configurations rather
than just empty rectangles. Pattern-independent first moments cannot be
assumed for this stronger selection. This is a proposed next calculation,
not an improved random-containment bound.

Reproduce: `python3 experiments/w41-canonical-overlap/verify.py`.
