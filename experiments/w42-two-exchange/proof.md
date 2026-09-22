# W42: two-exchange selection and its first-moment cost

10 September 2026. This is an exact finite and analytic follow-up to
[W41](../w41-canonical-overlap/proof.md), not an asymptotic containment bound.

## 1. Selection preserves existence and removes large overlaps

Order all position k-subsets of a host lexicographically. For a target π,
retain a copy A if there is no earlier copy B of π with |A∩B|≥k−d.
Let Yπ^(d) count retained copies. Comparisons use **all** earlier copies,
including rejected ones. This is local-minimum selection, not greedy packing.

**Proposition 1.** For d≥1, Yπ^(d)>0 if and only if π is contained. Also
Yπ^(d+1)≤Yπ^(d), and distinct retained copies intersect in at most k−d−1
positions.

*Proof.* When any copy exists, the globally first copy has no earlier
competitor and is retained. Increasing d enlarges the set of competitors.
If two retained copies had intersection at least k−d, the later one would
be rejected by the earlier one. These prove all three statements. ∎

For d=1 this equals leftmost-canonical selection. One implication is
immediate: a single-point left move is an earlier one-exchange copy.
Conversely, let B be an earlier one-exchange copy of A. Its new point b
precedes the removed point a. At the first differing position i, b replaces
c=A_i in the position correspondence between the copies. If b has value
rank m in B, c has rank m in A. Replacing one value can change counts below
b by at most one, so b lies strictly between the value neighbours of c
in A: below the lower neighbour would give rank at most m−1 in B, and
above the upper neighbour would give rank at least m+1. Its position is
between A_(i−1) and c. Replacing c by b is therefore a valid single-point
left move in A. Boundary neighbours mean −∞ and +∞. This is the stronger
direction already implicit in [W38, Lemma 3](../w38-second-moment/proof.md).

In particular, d=2 eliminates overlaps k−1 and k−2, while preserving the
containment event exactly. No moment estimate follows from separation alone.

## 2. An exact first-moment representation

Fix k points A of pattern π in the unit square, with distinct coordinates.
Let U_A be the set of points u for which replacing one point of A by u
gives an earlier copy of π. Equivalently it is the ordinary canonical
forbidden union of rectangles. For two points u,v outside A, put
K_A(u,v)=1 if replacing some two points of A by {u,v} gives an earlier
copy of π, and put K_A=0 otherwise. This symmetric Boolean kernel accounts
for all position and value rank changes; no fixed common correspondence
is assumed. All conditions are measurable order inequalities.

Write D_A=[0,1]²\U_A. For r≥0 define

    q_r(A) = ∫_(D_A^r) ∏_(i<j) (1−K_A(z_i,z_j)) dz_1…dz_r,    q_0(A)=1.

**Proposition 2.** The probability that A survives two-exchange selection
after adding r iid uniform square points is q_r(A). For background Poisson
intensity λ it is

    Q_λ(A) = exp(−λ) Σ_(r≥0) λ^r q_r(A)/r!.

Let Ωπ be the region with x_1<…<x_k and the y-order specified by π, with
ordinary 2k-dimensional Lebesgue measure, of volume 1/(k!)². Then

    E Yπ^(2)(σ_n) = (n)_k ∫_(Ωπ) q_(n−k)(A) dA,              n≥k,
    E Yπ^(2)(Π_λ) = λ^k ∫_(Ωπ) Q_λ(A) dA.

*Proof.* Every competing copy differing in one point uses one background
point in U_A. Every competitor differing in exactly two points uses two
distinct background points that form an edge of K_A. Excluding both is
necessary and sufficient, giving the integrand for r iid points. Averaging
over their Poisson number proves the series, which converges since
0≤q_r≤1. For the fixed-size first moment, choose k of the n labels and
order their positions: binom(n,k)k!=(n)_k. Integrate over their specified
pattern region and apply the conditional survival formula. Poisson-average
this expression and interchange nonnegative terms to get the final formula.
Equivalently this is the multivariate Mecke identity, in the standard form
of [Last–Penrose, Theorem 4.4](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf). ∎

This is an exact representation, not an efficient evaluation or a new
probabilistic inequality. Unlike ordinary canonical emptiness, a one-point
area alone does not encode the conditional event: the remaining background
must contain no forbidden pair. Dependence between overlapping pairs must
be handled in any approximation.

## 3. Pattern independence is false

**Finite counterexample (exhaustively verified).** For k=3,n=6, the exact
sums over all 720 hosts are as follows. Divide each entry by 720 to obtain
its probability or expectation.

| π | Hosts containing π | Σ Yπ^(1) | Σ Yπ^(2) |
|---|---|---|---|
| 123 | 588 | 672 | 595 |
| 132 | 588 | 672 | 598 |
| 213 | 588 | 672 | 594 |
| 231 | 588 | 672 | 594 |
| 312 | 588 | 672 | 598 |
| 321 | 588 | 672 | 595 |

Thus the ordinary canonical mean is 14/15 for every target, whereas the
two-exchange mean differs, even though these containment probabilities are
identical. The pattern-independent first-moment factorization from W12
cannot be imported unchanged. This does not exclude useful target-uniform
bounds on the new kernel.

The enumeration proof lists every permutation in S_6 and every position
triple, then applies the defining selection predicate. The independently
written verifier enumerates removed/added subsets directly instead of
comparing grouped copy masks. It reproduces all six rows, including their
second moments. See [verify_census.py](verify_census.py),
[census-verification.txt](census-verification.txt) and [exact data](exact-census.json).
This is a computer-assisted finite result; no asymptotic extrapolation or
Lean formalization is claimed.

## 4. The proof or disproof bridge

By Proposition 1, Markov gives Pr(π is contained)≤E Yπ^(2). A proved
expectation tending to zero for some target sequence at Ck² with C>1/4
would therefore disprove Alon. For a proof attempt, Cauchy–Schwarz gives

    Pr(π is contained) ≥ (E Yπ^(2))² / E[(Yπ^(2))²].

Even a bounded ratio only gives positive success probability for that
target. Pattern-averaged moments give an averaged conclusion; neither is
simultaneous high-probability universality. A common host event or sufficiently
strong control of all missing targets remains necessary. The next calculation
should bound the target-dependent forbidden-pair cost, not assume it away.
