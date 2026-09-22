# An exact global frontier for repeated 21

10 September 2026. The target is c_21=1, where L_21 is the maximum number
of direct-summed decreasing pairs. This work gives an exact state and a
verified algorithm; it does not yet establish that limiting constant.
No algorithmic novelty is claimed.

**Continuation:** [pruning.md](pruning.md) proves permanent dominance pruning,
an exact one-gap update in O(n log n) time and O(n) space, and a marked-state
flux identity. The per-level implementation below is retained as the original
full recurrence and a verification reference. Its larger resource bound does
not describe the improved `pruned.c` implementation.

Scan points in increasing x coordinate, with distinct y coordinates. A
completed m-pair copy has pattern 21⊕...⊕21. Let F_m be the least possible
maximum y of such a copy among the points already scanned, with F_0=0
and F_m=∞ if no such copy exists. Smaller maxima dominate larger maxima
for any future extension, since all future x coordinates are larger.

A pending pair at level m consists of a previous first (upper) point z,
and a completed m-pair copy available strictly before that point, whose
maximum is below the eventual second (lower) point. It suffices to record
the interval (l,z), with l=F_m immediately before z arrived. Define

    H_m(y)=min{z : a recorded interval (l,z) satisfies l<y<z},

where the minimum of the empty set is infinity.

**Exact update.** On arrival of a point of height y, using the old state,

    F_(m+1) ← min(F_(m+1), H_m(y)),
    H_m(t)  ← min(H_m(t), y) for F_m(old)<t<y,

and leave H_m(t) unchanged outside that interval. F_0 stays zero.

**Proof.** Any newly completed (m+1)-pair copy ends at the new point y.
Its penultimate point z appeared earlier, and all points of the preceding
m pairs appeared before z and had values below y. Therefore F_m at the
time z arrived was below y, so (F_m,z) is a recorded interval covering y.
Conversely, every recorded interval covering y has a witnessing earlier
m-pair copy and gives an actual extension with maximum z. Taking the least
such z gives the first update. Every new pending pair starts at the new
point y; the smallest feasible earlier m-pair maximum is precisely the old
F_m. This gives the second update. Both inclusions prove the invariant by
induction. The old-state condition prevents using the same point to close
one pair and start the next pair in a single copy. ∎

For a permutation of 1,...,n, store one segment tree per level m, indexed
by the upper endpoint z. Its leaf stores the least lower endpoint l; an
internal node stores the minimum l in its subtree. A query finds the first
z>y whose stored l<y, pruning any subtree with minimum at least y. This
returns H_m(y) in O(log n) time. Insert (F_m(old),y) by a point update.
Process m in descending order, so F_m has not yet been changed by a
completion at the current point. Allocate a new level only when F_m becomes
finite. With M=L_21, the implementation takes O(n(M+1)log n) time and
O(n(M+1)) space. The worst case is quadratic up to the logarithm; there is
no claim of a worst-case subquadratic algorithm.

**Why W36 cannot be imported directly.** The complete frontier F alone is
not a Markov state for extension: the increasing prefixes (1,3) and (1,4)
have the same completed frontier, but the next height 3.5 closes a pair
only in the second. Even the pending profile need not be nondecreasing.
For the prefix (5,4,6,3,2,10), the level-1 pending intervals include exactly
(5,6) and (3,10). Thus H_1(4)=10 but H_1(5.5)=6. This differs from W36's
nondecreasing compound-Poisson boundary functions. The levels also share
one incoming Poisson process. An invariant-law argument must address both
the downward activation jumps of H and this coupling between levels.

The next precise analytic target is an invariant distribution for this
coupled interval-profile process, or a comparison process with controlled
loss in the resulting pair-growth rate. Finite-dimensional closures must
first preserve both updates; retaining only completed thresholds or a
single pending apex loses necessary information.

**Verification.** `verify.py` compares the segment-tree implementation to
an independent exhaustive-subsequence predicate for every permutation of
length at most 7 and 200 additional random permutations through length 14.
The implementation retains all pending choices and computes exact L_21
for each host. Monte Carlo using this checker estimates finite-host means
only, and is not a proof of c_21=1.
