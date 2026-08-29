# W32 — information outside the current gap: every sequential fresh-search rule is capped at ≈ 0.4623

Date 2026-08-29.  Tags PROVED / NUMERICAL / HEURISTIC.  Numerics: results.md; chronology and dead ends: log.md.
Notation as in experiments/w31-lookahead/proof.md ([W31]) and experiments/w19-general-greedy/proof.md ([W19]).
Π is a Poisson process of intensity N = Ck² on [0,1]²; scaled coordinates x' = kx, y' = ky make it a Poisson
process of intensity C on [0,k]²; π ∈ S_k is uniform and independent of Π, 0-indexed positions and values.
V_0 = 0, V_n = (1/n) Σ_{m<n} W(V_m, V_{n−1−m}) is the Bellman sequence of [W31] §4 (W(A,B) = E min over a
Poisson(1) process on (0,∞)×(0,1) of x + A/y + B/(1−y)); values in ../w31-lookahead/dp_V.txt: V_n/n² decreases
from 1 (n = 1) to 0.46275 (n = 2000), differences halving per doubling of n, limit ≈ 0.4623 (NUMERICAL).

**Summary.**  The brief asked for a threshold below 0.46·k² for a random π using information outside the current
gap (other gaps of the strip, neighbouring strips, other processing orders), or a proof that sequential rules
cannot get there.  Answer: they cannot.  Theorem 2.1 (PROVED) shows that *every* rule that places the points
one position at a time, each inside the gap of its value, choosing from a region on which the process is
conditionally Poisson (the hypothesis of the fresh-search lemma [W19] Lemma 1.2 — the tool behind every threshold
of this programme), has expected x-consumption ≥ V_k/(Ck) whatever it looks at, whatever partition into strips it
uses, and however far it looks ahead.  Hence no such rule proves a constant below inf_n V_n/n² ≈ 0.4623.  The
reason is not that out-of-gap information is unavailable but that it is worthless: the Bellman cost-to-go of the
future is a deterministic function of the current gaps, because the future searches are fresh (§4 quantifies:
what one sees now in another gap is left of the clock when that gap is next visited unless the lookahead is a
constant fraction of the whole width).  Knowing the whole of π in advance changes the cap by a factor
1 − 4·10^{−5} (Theorem 2.2, NUMERICAL).  Rules with several candidates per step (two-sided position scan,
r lanes) escape the theorem's hypotheses but not its conclusion in practice: two-sided and lanes ≈ 0.46 (NUMERICAL: no gain
over one-sided within ± 0.01), lanes fail beyond r = 4 (results.md).  Conclusion
for the programme: below ≈ 0.46 for a random pattern requires abandoning sequential commitment, i.e. a
Hammersley/LIS-type global argument (§5).

## 1. Sequential fresh-search rules (definition)

A *sequential rule* processes the positions p = 0, 1, …, k−1 in this order.  Its state after p steps is the
clock a (the x'-coordinate of the last chosen point; a = 0 initially), the placed values with the
y'-coordinates of their points, and an information σ-field 𝓕_p (everything the rule has looked at).  The
placed points cut [0,k] into *gaps*: for the step of value v = π(p), let (y_L, y_R) be the y'-coordinates of
the placed points with the nearest values below and above v (0 resp. k if none), let n_i and G_i be the
number of unplaced values and the height of the i-th gap.  The step chooses a point q_p of Π in a region
   A_p ⊆ (a, ∞) × (y_L, y_R),
any measurable function of 𝓕_p, and updates a := x'(q_p).  Hypotheses:
 (F) *freshness*: conditionally on 𝓕_p, Π ∩ A_p is a Poisson process of intensity C on A_p, and the choice
     q_p is measurable with respect to 𝓕_p ∨ σ(Π ∩ A_p); then 𝓕_{p+1} ⊇ 𝓕_p ∨ σ(Π ∩ A_p) ∨ σ(q_p) may contain
     any further information satisfying (F) at the next step;
 (N) *non-anticipation in π*: 𝓕_p is independent of (π(p+1), …, π(k−1)) conditionally on (π(0), …, π(p)) — the
     rule knows the values already processed and the current one, not the future ones.
Copy property (as [W31] Thm 2.1): on {a_k < k} the points q_0, …, q_{k−1} form a copy of π (x-order = position
order since a increases; y-order = value order since every point lies in the gap of its value).
Examples: all rules of [W19], [W29], [W31] (regions inside a value strip's gap, beyond a safe clock; (F) by
[W19] Lemma 1.2), the same rules with the whole fresh half-strip visible (W31 log §5, "lookahead outside the
gap"), rules whose windows cross strip boundaries (the gap is then the overall gap, as here), rules using several
strips' processes at once, and rules with unbounded x-lookahead as long as the looked-at region is excised from
later regions ([W19] Lemma 1.2 hypothesis A_t ∩ Δ_{t'} = ∅).  Not covered: rules that re-use points seen but not
excised (then (F) fails), rules that process positions in another order or keep several candidate copies (§3),
and rules that use the future of π (§2, Theorem 2.2).

## 2. The cap (PROVED)

**Lemma 2.1 (conditional law of the next value).**  Under (N), conditionally on 𝓕_p, the value v = π(p) is
uniform among the k − p unplaced values; hence it lies in gap i with probability n_i/(k−p) and, given the gap,
its rank m among the n_i unplaced values of the gap is uniform on {0, …, n_i − 1}.

*Proof.*  Under (N), (π(p), …, π(k−1)) given 𝓕_p is a uniformly random arrangement of the unplaced values (it is
so given (π(0..p−1)), and 𝓕_p adds only information independent of it).  ∎

**Theorem 2.1 (cap for sequential fresh-search rules).**  For every sequential rule satisfying (F) and (N),
   E[a_k] ≥ V_k/(Ck),   and more precisely   E[a_k − a_p | 𝓕_p] ≥ Ψ_p := Σ_i V_{n_i}/(C G_i)
(sum over the gaps of the state after p steps).  Consequently, with N = Ck²: (a) E[a_k] ≥ (V_k/k²)·k/C ≥ k for
C ≤ V_k/k²; (b) if the rule's consumption satisfies a weak law (Var(a_k) = o(k²), e.g. rules with windows of
height ≥ β > 0 as in [W29] Thm 4.1, or the margin rules of [W31]), it fails with probability → 1 for every
C < lim inf_k V_k/k², which is ≈ 0.4623 (NUMERICAL value of the limit; PROVED: ≥ V_k/k² for every k, the
sequence V_n/n² being decreasing on n ≤ 2000 by dp_V.txt).

*Proof.*  Backward induction on r = k − p (remaining values).  r = 0: both sides vanish (V_0 = 0).  Step: let
v = π(p) lie in gap i with rank m (Lemma 2.1 gives their conditional law given 𝓕_p; the rule may know them —
they are 𝓕_p ∨ σ(v)-measurable — but that only fixes the conditioning).  Given 𝓕_p, v, i, m, the chosen point
q_p = (a + u, y) ∈ A_p ⊆ (a,∞) × (y_L, y_R) creates two gaps of heights y − y_L and y_R − y holding m and
n_i − 1 − m values; the other gaps are unchanged.  By the induction hypothesis (which holds for every state and
every information field satisfying (F), (N) at the later steps),
   E[a_k − a_p | 𝓕_p, v, Π ∩ A_p] ≥ u + Σ_{i'≠i} V_{n_{i'}}/(C G_{i'}) + V_m/(C(y − y_L)) + V_{n_i−1−m}/(C(y_R − y)).
The right-hand side is Σ_{i'≠i} V_{n_{i'}}/(C G_{i'}) + φ(q_p) with φ(x,y) := (x − a) + [V_m/(y − y_L) +
V_{n_i−1−m}/(y_R − y)]/C, and q_p ∈ Π ∩ A_p, so φ(q_p) ≥ min_{Π ∩ A_p} φ.  By (F), Π ∩ A_p is Poisson of
intensity C on A_p given 𝓕_p; let Π' := (Π ∩ A_p) ∪ Π'' with Π'' an independent Poisson process of intensity C
on ((a,∞) × (y_L, y_R)) ∖ A_p, so that Π' is a Poisson process of intensity C on the whole half-gap and
min_{Π ∩ A_p} φ ≥ min_{Π'} φ.  Scaling y by 1/G_i and x by G_i (Poisson(C·G_i·(1/G_i)) = Poisson(C) preserved) and
then x by C ([W31] Lemma 2.2) gives E[min_{Π'} φ | 𝓕_p, v] = W(V_m, V_{n_i−1−m})/(C G_i).  Averaging over m (uniform
on {0..n_i−1} given i, Lemma 2.1) gives (1/n_i) Σ_m W(V_m, V_{n_i−1−m})/(C G_i) = V_{n_i}/(C G_i), and then over i
(probability n_i/(k−p)):
   E[a_k − a_p | 𝓕_p] ≥ Σ_i (n_i/(k−p)) [ V_{n_i}/(C G_i) + Σ_{i'≠i} V_{n_{i'}}/(C G_{i'}) ] = Σ_i V_{n_i}/(C G_i) = Ψ_p.
The initial state is one gap of height k with k values: E[a_k] ≥ V_k/(Ck).  (a) is arithmetic; (b): success needs
a_k < k while E a_k ≥ (V_k/k²)k/C > (1+δ)k for C < V_k/(k²(1+δ)), and Chebyshev.  ∎

*Remarks.*  (i) The proof uses nothing about A_p except A_p ⊆ half-gap and (F): the strip partition, the safe
clock, the window margins, the x-lookahead and every piece of information outside A_p (other gaps' half-strips,
neighbouring strips, the whole fresh strip) are irrelevant — the cost-to-go Ψ of the future is a deterministic
function of the gaps because the future searches are fresh.  This extends [W31] Thm 4.1 from the fresh-window
model to the real process and to rules that look anywhere.  (ii) The value strips of height h of [W29]/[W31] are
the special case A_p ⊆ half-gap ∩ strip; their cap m·V_h/(Ch) = (V_h/h²)k/C ≥ V_k/(Ck) is weaker (V_n/n² is
decreasing), so removing the partition (h = k, one strip, windows crossing strip boundaries) can only gain
V_h/h² − V_k/k² (0.0141 at h = 64, 0.0026 at h = 512; results.md §1 confirms numerically: a single strip with
h = k = 2000 gives 0.456–0.465).  (iii) Non-anticipation (N) is used only in Lemma 2.1.

**Theorem 2.2 (anticipating rules: the cap with π known in advance).**  Drop (N) and let the rule know all of π.
For a gap with n values arriving in a known order σ, define V(σ) := W(V(σ_b), V(σ_a)) where σ_b, σ_a are the
sub-orders of the values below/above the first value (so V(σ) depends on σ only through its binary search tree
T(σ)); V(∅) = 0.  Then E[a_k] ≥ E_σ V(σ)/(Ck) =: V_k^{ant}/(Ck) for every rule satisfying (F), and
V_n^{ant} ≤ V_n with V_n^{ant}/V_n = 1 for n ≤ 3 and = 0.999994 (n = 4), 0.999971 (8), 0.999961 (11) exactly (all
Catalan(n) tree shapes, bst.py), ≈ 0.99995 for n ≤ 60 (quantised distributions, NUMERICAL).

*Proof.*  Same induction with the arrival order known: the cost-to-go of a gap with known sub-order σ is V(σ)/(CG)
(scaling), the next value's gap and rank are known, and pointwise minimisation of φ with potentials V(σ_b), V(σ_a)
gives W(V(σ_b), V(σ_a))/(CG) = V(σ)/(CG).  The average over uniform σ is over the random binary search tree.
V^{ant} ≤ V: W is concave and nondecreasing in (A,B) (a mean of minima of functions linear in (A,B)); given the
root rank m, σ_b and σ_a are independent uniform, so by Jensen and induction E[W(V(σ_b), V(σ_a)) | m] ≤
W(E V(σ_b), E V(σ_a)) ≤ W(V_m, V_{n−1−m}); average over m.  Numbers: bst.py (exact for n ≤ 11: the distribution of V(T) over the
Catalan(n) shapes with random-BST probabilities; for n > 11 the distribution is quantised to 40 atoms by merging
neighbouring values, which by concavity of W can only *increase* the computed value, so for n > 11 the printed
ratios are upper bounds on V^{ant}_n/V_n and the true gain may be slightly larger; the exact values for n ≤ 11 and
the smooth trend of the ratio (decreasing by ≈ 10^{−6} per unit of n) leave no room for a gain beyond 10^{−4}).  ∎

*Comment.*  The anticipation gain is 4·10^{−5}: knowing which values arrive when is worthless because the
cost-to-go of a gap is almost linear in the potentials of its sub-gaps.  Hence the cap ≈ 0.4623 holds for
anticipating sequential fresh-search rules as well, up to a NUMERICAL factor 1 − 4·10^{−5}.

## 3. Several candidates per step: two-sided scans and lanes (PROVED comparison, NUMERICAL constant)

A *two-sided rule* keeps a left clock a (positions consumed from p = 0 upward) and a right clock b (positions
consumed from p = k−1 downward, searching to the left of b for the rightmost cheap point); at each step it
evaluates the fresh in-gap minimiser of φ (potentials V) for both ends and takes the cheaper one; success iff
all values are placed with a < b (consumption a + (k − b) < k).  Both ends' searches are fresh (their regions
are disjoint: left regions lie left of all right explored sets and vice versa; formally with safe clocks
e^L_j ≤ e^R_j per strip and the [W31] Lemma 2.4 collision accounting, see log.md §3).  With r *lanes* the
positions are cut into r blocks, block i owns the x'-interval [ik/r, (i+1)k/r] and is scanned two-sidedly; 2r
candidates per step; success iff every block finishes inside its interval.

**Observation 3.1 (telescoping).**  Let Ψ(state) = Σ_i V_{n_i}/(CG_i) and Z_p := u_p + Ψ(new state) − Ψ(old state)
for the chosen candidate.  Then a_k + (k − b_k) = Σ_p u_p = V_k/(Ck) + Σ_p Z_p identically (Ψ(final) = 0).  For the
one-sided rule with potentials V, E[Z_p | 𝓕_p] = 0 in the fresh model (Bellman equality, [W31] Thm 4.1).  For the
two-sided rule the *optimal* policy is at least as good as one-sided (always taking the left end is a feasible
policy), so the two-sided optimum is ≤ V_k/(Ck) — but the greedy rule "take the cheaper of the two" is not that
optimum, and the naive argument "each candidate's Z has conditional mean 0, so E min(Z_L, Z_R) ≤ 0" is FALSE:
a candidate that was not taken persists, and conditionally on that its Z is biased upward (selection);
measured E Z_L ≈ +0.9 per step, E min(Z_L, Z_R) ≈ −0.12 (zdiag.py).  Whether the greedy two-sided rule beats
one-sided is therefore a numerical question.  ∎

**NUMERICAL (results.md §4).**  There is no measurable gain: single strip, implied constant C·consumption/k =
0.461 (k = 512, C = 0.5), 0.464 (k = 1024, C = 0.6) for the two-sided rule versus 0.461 for one-sided at k = 1024
(± 0.01); the two-sided rule fails at C = 0.45 (3/8) and C = 0.40 (0/8).  The selection is weak because the candidate
not taken persists: its Z is re-drawn at the next step but its gap is the same, so the pair's minimum hovers
around 0 (measured E Z_L ≈ +0.9, E min ≈ −0.12 per step, zdiag.py).  Lanes: r = 2, 4 give 0.456, 0.450 at k = 512 and
0.467 at k = 1024 (no gain); r ≥ 8 fails half the runs (a lane's consumption exceeds its budget k/r).  Rigorous
version: the reduction is the same as [W31] Thm 2.1 with two safe clocks per strip (log.md §3); the constant is
Monte-Carlo, not certified, and the concentration step (the lanes/ends couple the strips, so the per-strip costs
are no longer independent) is not written out.  Given the size of the gain this was not pursued further.

## 4. Why out-of-gap information is worthless: staleness (HEURISTIC + NUMERICAL)

The rule of §1 may look at the other gaps' half-strips at no cost, and the theorem says it gains nothing.  The
mechanism: a gap with n_i unplaced values is next visited after ≈ (k−p)/n_i steps, during which the clock
advances by that many step costs, while the points one can see now in that gap are within x'-distance L of the
clock.  Measured with the one-sided single-strip rule (single_strip.py; D = clock advance between the creation
of a gap and its next visit, weighted by step cost): the cost share of steps with D < L depends on L/k only —
k = 1024 / 2000: 0.093 / 0.097 at L = 0.01k, 0.156 / 0.166 at 0.02k, 0.30 / 0.31 at 0.05k, 0.46 / 0.49 at 0.1k,
0.69 / 0.71 at 0.2k (≈ 1.2 (L/k)^{0.7}).  So a lookahead L = o(k) can inform a vanishing share of the cost: any
rule that could profit from out-of-gap information must look at a constant fraction of the whole square, which
is the regime of global (non-sequential) algorithms.  (The earlier estimate CL/k in log.md §1 was too optimistic
about staleness — the revisit times have a heavy lower tail — but the conclusion is the same.)

## 5. What is left

| statement | class | consequence | status |
|---|---|---|---|
| Thm 2.1 | every sequential rule with (F) + (N): any partition, any lookahead, any information | E a_k ≥ V_k/(Ck): no threshold below inf V_n/n² ≈ 0.4623 | PROVED (limit value NUMERICAL) |
| Thm 2.2 | the same with π known in advance | cap V^{ant}_k/(Ck), V^{ant}_n/V_n = 1 − 4·10^{−5} | PROVED formula; NUMERICAL ratio |
| Obs 3.1 | two-sided / lane rules (2 or 2r candidates) | optimum ≤ one-sided (trivial); greedy version numerically ≈ 0.46, no gain | NUMERICAL constant |
| §4 | staleness | out-of-gap information needs lookahead Θ(k) | HEURISTIC + NUMERICAL |

The random-pattern truth (≈ 0.22, W21) is a factor 2 below the sequential cap; the identity's truth ¼ is below
its sequential cap π/8 by π/2 — Hammersley's ratio.  For the identity the gap is closed by a global argument
(LIS = longest path; patience sorting keeps *all* candidate chains).  For a random π there is no path structure
(W20 §4.4: the exact DP state is a Pareto front of dimension growing with k), and Theorem 2.1 says that no
amount of local cleverness substitutes for it.  Open: a global argument for random π, e.g. a second-moment /
Talagrand bound on the number of copies restricted to a structured subclass, or a branching (multi-copy)
scheme whose state stays polynomial.
