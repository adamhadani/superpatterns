# Dominance pruning, a local update, and the exact flux

See the [standalone note](../../output/pdf/repeated-21-frontier.md) and
[experiment report](report.md) for the prominent, self-contained presentation
with primary prior-art references and the conditional implication for Alon.

10 September 2026 continuation. Starting from the exact full state in
[proof.md](proof.md), we obtain an O(n log n)-time, O(n)-space algorithm.
This is an improvement over this repository's original implementation;
algorithmic priority is not claimed. The asymptotic c_21 problem stays open.

## 1. Permanent dominance and localization

Use positive distinct heights. F_0=0 and F_m is the smallest maximum height
of a completed m-pair copy; append infinity after the last finite threshold.
Finite thresholds are strictly increasing: deleting the last pair from a
minimizing (m+1)-pair copy leaves an m-pair copy with strictly smaller maximum.
Every F_m is nonincreasing in time. A recorded level-m interval (l,z) has
l=F_m at the time the upper point z arrived, so l≥F_m(current).

**Lemma 1 (permanent pruning).** A level-m pending interval with z≥F_(m+1)
can be deleted permanently without altering any future completed threshold.

*Proof.* Completing that interval can only propose maximum z, which is
already dominated by the available F_(m+1). Since this threshold only
decreases, the proposal can never improve it. Any future extension from
such a completed copy is also available from the smaller threshold: all
future points arrive after the presently available dominating copy. The
full recurrence starts later pending intervals only from the least
completed threshold, so deletion cannot change those updates either. ∎

After pruning, every retained level-m interval satisfies

    F_m ≤ l < z < F_(m+1).                                                   (6)

In particular its apex z belongs to exactly one current threshold gap,
which identifies its level. No separate per-level trees are needed.

**Theorem 2 (one-gap update).** On arrival of a fresh height y, let j be the
unique index with F_j<y<F_(j+1), and let b=F_(j+1), all before the update.
In the globally stored intervals find

    z=min{a : (l,a) is retained and l<y<a}.

If this set is nonempty, then y<z<b. Replace F_(j+1) by z and delete every
retained interval whose apex lies in [z,b). If b was infinity, append a
new infinite threshold. Finally insert the single interval (F_j,y).
If the set is empty, only the insertion is performed. This preserves all
completed thresholds of the full recurrence at every time.

*Proof.* For m<j, all retained apices are below F_(m+1)≤F_j<y, so cannot
close at y. For m>j, all lower activation endpoints are at least F_m≥b>y,
so cannot close either. Thus only level j can improve, and any improving
apex is below b. Its new threshold z makes exactly the old level-j apices
in [z,b) dominated; higher levels' apices exceed their old left boundary
at least b, and lower levels' apices lie below F_j, so no unrelated interval
is deleted. Old level-(j+1) intervals keep their historical lower marks;
they are not activated in the newly gained region just because their
current left threshold decreased.

As for insertion, levels m>j cannot start at y, because F_m>y. At levels
m<j, an insertion with apex y is immediately dominated by F_(m+1)<y.
Only (F_j,y) at level j survives. F_j itself does not change on this arrival,
so this is its old value, as the full recurrence requires. Induction using
Lemma 1 proves exactness, including when a new largest finite level appears. ∎

## 2. Implementation and verification

For a permutation of [n], maintain the sorted array of finite F_m and one
segment tree indexed by apex. The leaf of a retained apex holds its lower
mark; an absent leaf holds n+1. Subtrees hold minima and a lazy clear flag.
Binary search identifies j; a first-cover query finds the smallest apex
above y with lower mark below y; a range clear deletes [z,b); a point update
inserts (F_j,y). Each operation takes O(log n) time. The first-cover query
has one range boundary and follows only the first subtree with a qualifying
minimum; all preceding fully covered subtrees are pruned. Space is O(n).
Sorting distinct real input heights first gives the same complexity.

`pruned.c` implements this rule. `verify_pruned.py` checks every completed
threshold at every prefix against an independently written, unpruned list
recurrence, and checks the final answer against brute-force subsequences
on every permutation of length≤8. The retained raw verification is:

- 46,233 exhaustive hosts, 100 random hosts through 128, 9 extreme hosts;
- 372,249 prefix states, every completed threshold agrees;
- every exhaustive final answer also agrees with brute subsequences.

Commands from the repository root:

```sh
cc -O2 -std=c11 -Wall -Wextra -pedantic experiments/w40-c21-frontier/pruned.c -o /private/tmp/superpatterns-c21-pruned
python3 experiments/w40-c21-frontier/verify_pruned.py /private/tmp/superpatterns-c21-pruned
```

## 3. Activation marks remain indispensable

The prefixes P=(3,2,4,1) and Q=(2,3,1,4) have the identical completed
frontier F=(0,2,∞) and the identical set of retained apices {1,4}.
For P their intervals are (0,1),(3,4); for Q they are (0,1),(2,4).
Arrival y=5/2 completes a second pair only for Q. Indeed P has no pending
interval covering 5/2, while Q uses its apex 4 to obtain F_2=4.
Thus even **all** completed thresholds plus **all** pending apices are
not an exact Markov state; the historical activation marks cannot be erased.
This is a reachable-state counterexample, using the same four past values.

## 4. Exact local flux for a stationary-law attempt

Let unit-intensity planar Poisson points arrive in x order in the strip
0<y<R. On any finite time interval there are finitely many arrivals. For a
bounded state function f the jump generator is exactly

    (L f)(S)=∫_0^R [f(T_y S)−f(S)] dy,                                      (7)

where T_y is Theorem 2's update, retaining the activation marks.
For 0<u<R not equal to a threshold, let N_u=# {m≥1:F_m≤u}, j=N_u, and set

    r_u(S)=length( union{(l,z): retained (l,z), F_j<z≤u} ).                    (8)

**Proposition 3 (flux identity).** The instantaneous drift of N_u equals
r_u(S). Consequently, for the process started empty,

    E N_u(t)=∫_0^t E r_u(S_s) ds.                                           (9)

*Proof.* A completion can increase N_u only by moving the first threshold
b=F_(j+1)>u to an apex z≤u in its preceding gap. The arrivals accomplishing
this are exactly the union in (8). If an interval covers y with apex≤u,
the chosen least covering apex also lies≤u; conversely every increase
uses such an interval. Each increase is by one, since only one threshold
changes. Unit Poisson intensity gives (8) as its rate. The compensated
counting-process identity gives (9); integrability follows from
N_u(t)≤#Π([0,t]×[0,R])/2 and 0≤r_u≤u. ∎

This replaces a proposed unmarked closure with an explicit equation a
candidate stationary law must satisfy. A stationary comparison yielding
a boundary cost ρu+t/(4ρ) would optimize to √(tu), the desired pair scale,
but neither that stationary law nor the necessary boundary comparison
has been proved. Equation (9) alone does not identify c_21.

## 5. Prior-art limit

Albert et al., *Longest subsequences in permutations* (2003), discuss
layered classes with layers of sizes 1 and 2. Albert's subsequent
[*On the length of the longest subsequence avoiding an arbitrary pattern
in a random permutation*](https://arxiv.org/abs/math/0505485), §4, already
reports an O(n log n) algorithm for that class. Its objective maximizes
total selected points and permits singleton layers; ours maximizes complete
21 pairs. A reduction or weighted adaptation may connect the algorithms.
The pruning proof is independently useful for this project, but the
matching complexity is not presented as a literature improvement.
