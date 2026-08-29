# W9 — proved statements (multi-threaded scanning, refined overlap accounting)

Date: 2026-08-29.  Everything in this file is proved in full below.  Heuristics, numerics and dead
ends are in log.md.  Notation follows He–Kwan (arXiv:1911.12878, "HK").

## 0. Setting

M is a uniformly random q × m zero-one matrix (entries i.i.d. Bernoulli(1/2)); M(y,x) is the entry in
row y ∈ {0,…,q−1} and column x ∈ {0,…,m−1}.  π ∈ S_k is written 0-indexed, π : {0,…,k−1} → {0,…,k−1}.
M *contains* π if there are columns x_0 < ⋯ < x_{k−1} with M(π(j)+t, x_j) = 1 for some row offset t, or
more generally rows y_0,…,y_{k−1} ordered as π (HK's interval-minor notion); either implies π ⊂ σ under
HK's coupling (HK Lemma 2.2: q = 2k, m = n/(4k)).

**H-thread with shift t** (HK's thread): for j = 0,1,…,k−1 scan row π(j)+t from the column after the
previously found one until a 1 is found.  It exposes exactly one cell per column it passes, so if it
fails (runs out of columns before its k-th one) it has exposed exactly m cells, with ≤ k−1 ones.  Let
T_t be the set of exposed cells.  For each element j reached by the thread let I_j ⊆ T_t be the set of
cells exposed while seeking element j: it is a horizontal interval [X_j, X_j + z_j] in row π(j)+t whose
first z_j cells are zeros and whose last cell is a one (or, for the last element of a failing thread,
an interval of zeros ending at column m−1, in which case we still write |I_j| ≤ z_j + 1).  We call
(z_j)_j the *zero-run profile* of the thread.

**V-thread with shift s** (new; the transpose of the above): for v = 0,1,…,k−1 scan column π^{-1}(v)+s
upward from the row after the previously found one until a 1 is found.  It exposes exactly one cell per
row it passes; if it succeeds, the cells (y_v, π^{-1}(v)+s) with y_v increasing in v are a copy of π
(columns increase with position, rows increase with value).

**Δ-shift chains** (HK §3).  For Δ ≥ 1, A ⊆ [k] is a Δ-shift chain if the map b(a) := π^{-1}(π(a) − Δ)
is defined on A (π(a) ≥ Δ) and increasing on A.  L_Δ(π) is the maximum size of a Δ-shift chain; HK's
L_Δ(π) is the same quantity (LIS of i ↦ π^{-1}(π(i)+Δ)).

**Lemma 0 (exposure principle; standard).**  Consider any procedure that exposes cells of M one at a
time, the next cell being a function of the values exposed so far (no cell exposed twice), possibly
stopping.  Let ξ_1, ξ_2, … be the exposed values in order.  Then (ξ_i) is an i.i.d. Bernoulli(1/2)
sequence (up to the stopping time).  Consequently, for integers N, K: the event "at least N cells are
exposed and among all exposed cells there are at most K ones" has probability ≤ Pr(Bin(N,1/2) ≤ K).

*Proof.*  Conditionally on ξ_1,…,ξ_i the next cell is determined and has not been exposed, and its entry
is independent of the exposed entries, hence is Bernoulli(1/2).  On the event in question, ξ_1,…,ξ_N are
defined and contain ≤ K ones. ∎

## 1. Cross-direction threads

**Lemma 1.**  For any π, t, s: |T_H ∩ T_V| ≤ min(#rows visited by H, #columns visited by V) ≤ k, where
T_H, T_V are the cells exposed by the H-thread with shift t and the V-thread with shift s.

*Proof.*  The V-thread exposes at most one cell in each row (its row index strictly increases after every
exposure), and all cells of the H-thread lie in the ≤ k rows π(j)+t.  Hence each of these rows contains
at most one cell of T_H ∩ T_V.  Symmetrically each of the ≤ k columns π^{-1}(v)+s contains at most one
cell of T_H (one cell per column) and all of T_V lies in these columns. ∎

**Proposition 2.**  For every π ∈ S_k and all admissible t, s,
  Pr(H_t fails and V_s fails) ≤ Pr( Bin(m + q − k, 1/2) ≤ 2k − 2 ).
In particular Pr(M does not contain π) ≤ Pr(Bin(m+q−k,1/2) ≤ 2k−2).

*Proof.*  Run the H-thread to completion and then the V-thread; this is an adaptive exposure procedure
(the V-thread does not re-expose a cell already exposed by H; it just reads it).  If both fail, H
exposed m cells with ≤ k−1 ones, V read q cells with ≤ k−1 ones, and by Lemma 1 the union has at least
m + q − k cells, every one among them being a one of H or a one of V, so ≤ 2k−2 ones.  Apply Lemma 0
with N = m+q−k, K = 2k−2. ∎

*Remark (why this does not help asymptotically).*  Under HK's coupling n = 2qm.  A single H-thread gives
exponent ≍ m·ln 2 = (n/2q) ln 2, maximised at the minimal q = k.  Proposition 2 gives exponent
≍ (m+q−k) ln 2, and for fixed n = 2qm the sum m + q is maximised at the same extreme q = k, m = n/2k,
where it equals the single-thread exponent plus O(k).  So Proposition 2 cannot improve Alon's
n = O(k² log k) bound by more than a constant factor, and adds only an additive O(k) to the exponent in
HK's regime q = 2k.  Also, the *reversed* H-thread (elements k−1,…,0, columns right to left) fails on
exactly the same event as the H-thread (both fail iff no copy of π lies in rows t,…,t+k−1), so it gives
nothing; see log.md §2 for the numerical confirmation.

## 2. Refined overlap bound for two H-threads

**Lemma 3 (chain bound).**  Let t < t' = t + Δ and let (z_a)_a be the zero-run profile of the *leader*
thread t (defined for the elements it reached).  Then
  |T_t ∩ T_{t'}| ≤ W_Δ(z) := max { Σ_{a∈A} (z_a + 1) : A a Δ-shift chain of π consisting of elements
                                    reached by the leader }.
In particular |T_t ∩ T_{t'}| ≤ L_Δ(π)·(1 + max_a z_a), which is HK's bound.

*Proof.*  A cell (y,x) ∈ T_t ∩ T_{t'} lies in a row y = π(a)+t visited by the leader while seeking
element a, and in a row y = π(b)+t' visited by the follower while seeking element b; thus
π(a) = π(b) + Δ, i.e. b = b(a) := π^{-1}(π(a) − Δ).  Let A be the set of leader-elements a whose interval
I_a contains a shared cell.  The shared cells in row π(a)+t lie in I_a, so their number is ≤ |I_a| ≤
z_a + 1, and |T_t ∩ T_{t'}| ≤ Σ_{a∈A}(z_a+1).  It remains to show that A is a Δ-shift chain, i.e. that
b is increasing on A.  Let a < a' in A.  The leader visits I_a before I_{a'}, so every column of I_a is
smaller than every column of I_{a'}.  The follower exposes one cell per column and visits its intervals
I'_0, I'_1, … in increasing order of elements and of columns.  A shared cell in row π(a)+t belongs to
I'_{b(a)} and a shared cell in row π(a')+t belongs to I'_{b(a')}; the former has a smaller column than
the latter, hence I'_{b(a)} precedes I'_{b(a')}, hence b(a) < b(a') (b(a) ≠ b(a') because π is
injective). ∎

**Proposition 4 (two threads, exact conditional form).**  Let E_t be the event that thread t fails.
Then, with z the zero-run profile of thread t,
  Pr(E_t ∩ E_{t+Δ}) ≤ E[ 1_{E_t} · Pr( Bin(m − W_Δ(z), 1/2) ≤ k − 1 ) ].

*Proof.*  Expose thread t completely, then run thread t+Δ, which exposes fresh cells adaptively (Lemma 0
applies conditionally on T_t and its values).  If thread t+Δ fails it touched m cells, of which by
Lemma 3 at most W_Δ(z) were already exposed; so it exposed ≥ m − W_Δ(z) fresh cells containing ≤ k−1
ones.  Conditionally on the leader, Lemma 0 bounds this by Pr(Bin(m − W_Δ(z),1/2) ≤ k−1). ∎

(Unconditionally, z_0, z_1, … are i.i.d. geometric with P(z = i) = 2^{−i−1}, and E_t = {Σ_{a<k}(z_a+1) > m};
so Proposition 4 reduces the two-thread question to a large-deviation question about i.i.d. geometrics
weighted along Δ-shift chains of π.  Log.md §4 explains why this alone cannot beat e^{−m ln 2}.)

## 3. Multi-thread theorem with a global run-sum event

Let r(c) denote, for a cell c = (y,x), the number of consecutive zeros in row y starting at c and going
right (r(c) = 0 if M(c) = 1).  For cells in distinct rows the r(c) are independent, each geometric with
P(r = i) = 2^{−i−1}.

**Lemma 5 (HK Lemma 2.3, self-contained version).**  If c_1,…,c_j are cells in distinct rows and
s ≥ 4j then Pr(r(c_1)+⋯+r(c_j) ≥ s) ≤ e^{−s/8}.

*Proof.*  Σ r(c_i) ≥ s iff among the first s + j − 1 fair coin flips there are at most j − 1 heads
(the sum of j i.i.d. geometrics is the number of tails before the j-th head).  With N = s+j−1 ≤ 5s/4
and u = N/2 − (j−1) = (s − j + 1)/2 ≥ 3s/8, Hoeffding gives Pr ≤ exp(−2u²/N) ≤ exp(−2·(9s²/64)/(5s/4))
= e^{−9s/40} ≤ e^{−s/8}. ∎

**Definition.**  For integers L, s let 𝒜_{L,s} be the event: for every set S of at most L cells lying
in distinct rows, Σ_{c∈S} r(c) < s.

**Lemma 6.**  If s ≥ 4L then Pr(¬𝒜_{L,s}) ≤ 2 (qm)^L e^{−s/8}.

*Proof.*  Union bound over the ≤ Σ_{j≤L}(qm)^j ≤ 2(qm)^L sets, using Lemma 5 (s ≥ 4L ≥ 4j). ∎

**Theorem 7 (multi-thread amplification with chain-bounded overlaps).**  Let q = 2k and let
t_1 < ⋯ < t_ℓ ≤ k be shifts such that L_{t_j − t_i}(π) ≤ L for all i < j.  Let s ≥ 4L and suppose
(ℓ−1)(s+L) ≤ m/2.  Then
  Pr( M does not contain π, and 𝒜_{L,s} ) ≤ Pr( Bin( ℓ(m/2 − k), 1/2 ) ≤ ℓ(k−1) ).

*Proof.*  We use HK's device of "pretending" that 𝒜_{L,s} holds, in the following precise form.  Run
the threads t_1, …, t_ℓ one after another, maintaining a set P of *pretended* cells (initially empty)
and the set of really exposed cells with their values.  For a cell c define its *known run* r̃(c) as the
number of consecutive cells starting at c going right that are really exposed with value 0 (stopping
at the first cell that is unexposed, pretended, or exposed with value 1).  When a thread is about to
look at a cell c:
 (a) if c ∈ P, or c is really exposed, the thread reads it (a pretended cell reads as 1) and moves on
     as in the ordinary procedure;
 (b) otherwise, if there is a set S of ≤ L cells in distinct rows such that Σ_{c'∈S} r̃(c') would
     become ≥ s in case c were exposed as 0, then c is added to P (not exposed) and read as 1;
 (c) otherwise c is really exposed.
Call this the modified procedure and let T̃_i be the set of cells (exposed or pretended) that thread i
touched.  We record three facts.

(i) *On 𝒜_{L,s} the modified procedure coincides with the real one.*  Rule (b) fires only if exposing c
as 0 would produce a set S with Σ_S r̃ ≥ s; since r̃(c') ≤ r(c') for every c' whenever all counted cells
are genuine zeros, this would contradict 𝒜_{L,s} unless M(c) = 1 — and then pretending c = 1 is correct.
By induction all pretended cells are genuine ones on 𝒜_{L,s}, so every thread behaves exactly as in the
real procedure, and if M contains no copy of π in rows t_i,…,t_i+k−1 for each i, all ℓ modified threads
fail.  Hence Pr(M ⊅ π, 𝒜_{L,s}) ≤ Pr(all modified threads fail).

(ii) *In the modified procedure Σ_{c∈S} r̃(c) < s for every S of ≤ L cells in distinct rows, at all
times.*  r̃ values only grow when a cell is really exposed with value 0, and rule (b) prevents any such
exposure from making a sum reach s.

(iii) *Overlaps.*  Each modified thread touches one cell per column, its cells for element a form an
interval Ĩ_a in row π(a)+t_i consisting of really exposed zeros followed by one cell that is a genuine or
pretended one (or an interval of zeros truncated at column m−1), so |Ĩ_a| ≤ r̃(X_a) + 1 where X_a is the
first cell of Ĩ_a.  Lemma 3's proof used only these interval properties, so for i < j, T̃_i ∩ T̃_j lies
in Σ_{a∈A}|Ĩ_a| for a (t_j − t_i)-shift chain A of thread i's elements; |A| ≤ L by hypothesis, and by
(ii) Σ_{a∈A} r̃(X_a) < s, so |T̃_i ∩ T̃_j| ≤ s + L.

Now suppose all modified threads fail.  Each touched exactly m cells, of which at most k−1 read as one
(genuine or pretended).  By (iii) and Bonferroni,
  |⋃_i T̃_i| ≥ ℓm − C(ℓ,2)(s+L) = ℓm − (ℓ/2)(ℓ−1)(s+L) ≥ ℓm − ℓm/4 = (3/4)ℓm.
Every pretended cell reads as one for every thread touching it, so |P| ≤ ℓ(k−1); the really exposed
cells therefore number at least (3/4)ℓm − ℓ(k−1) ≥ ℓ(m/2 − k), and among them at most ℓ(k−1) are ones
(a genuine one is a one for every thread touching it).  The really exposed cells are exposed adaptively
(rule (b) depends only on exposed information), so Lemma 0 applies with N = ℓ(m/2−k), K = ℓ(k−1). ∎

**Theorem 8 (a larger quasirandom class at n = O(k²)).**  For k sufficiently large put
  m = 18k,  ℓ = ⌈ln k⌉,  L = ⌊k/(3 ln² k)⌋,  s = ⌈20 L ln k⌉.
Let 𝒬'_k be the set of π ∈ S_k for which fewer than k/(3 ln k) values Δ ∈ [k] satisfy L_Δ(π) > L, i.e.
π is (1/(3 ln² k), k/(3 ln k))-quasirandom in HK's sense (Definition 4.1 with X = [k]).  Then w.h.p. the random
2k × 18k matrix M contains every π ∈ 𝒬'_k; hence (HK Lemma 2.2) w.h.p. a uniformly random permutation
of length n = 72k² contains every π ∈ 𝒬'_k.  Moreover |S_k \ 𝒬'_k| ≤ k!·exp(−(1/3 − o(1)) k/ln k).

*Proof.*  First, Pr(¬𝒜_{L,s}) → 0: by Lemma 6 with q = 2k, m = 18k, s ≥ 4L,
Pr(¬𝒜_{L,s}) ≤ 2(36k²)^L e^{−s/8} ≤ 2 exp(L(2 ln k + 3.6) − 2.5 L ln k) = 2 exp(−0.5 L ln k + 3.6 L) → 0.
Fix π ∈ 𝒬'_k and let F = {Δ ∈ [k] : L_Δ(π) > L}, |F| < k/(3 ln k).  Choose shifts in {0,…,k} greedily:
each chosen t forbids the values t ± F and t itself, i.e. at most 2|F|+1 values, and
ℓ(2|F|+1) ≤ (ln k + 1)(2k/(3 ln k) + 1) < k + 1 for large k, so ℓ distinct shifts with all pairwise
differences outside F exist; order them t_1 < ⋯ < t_ℓ.  They satisfy the chain hypothesis of Theorem 7
(for i < j, L_{t_j−t_i}(π) ≤ L since t_j − t_i ∉ F).  Arithmetic hypotheses: s ≥ 4L, and
(ℓ−1)(s+L) ≤ ln k·(21 L ln k + 1) ≤ 7k + ln k ≤ 9k = m/2.
Theorem 7 gives, with N = ℓ(m/2 − k) = 8ℓk and K = ℓ(k−1) ≤ N/8,
  Pr(M ⊅ π, 𝒜_{L,s}) ≤ Pr(Bin(8ℓk,1/2) ≤ ℓk) ≤ exp(−8ℓk·D(1/8‖1/2)) ≤ e^{−2.5 ℓ k} ≤ k^{−2.5k},
using D(1/8‖1/2) = (1/8)ln(1/4) + (7/8)ln(7/4) > 0.316 (Chernoff–Hoeffding in relative-entropy form).
A union bound over |𝒬'_k| ≤ k! ≤ k^k patterns gives Pr(∃π ∈ 𝒬'_k: M ⊅ π, 𝒜_{L,s}) ≤ k^{−1.5k} → 0, and
adding Pr(¬𝒜_{L,s}) → 0 proves the first claim.

For the size of the exceptional set, HK's Lemma 3.1 proof shows that for a uniform π ∈ S_k,
Pr(max_Δ L_Δ(π) ≥ L') ≤ k·(e²k/L'²)^{L'}.  If π ∉ 𝒬'_k then some Δ has L_Δ(π) > L, so with L' = L+1,
|S_k \ 𝒬'_k| ≤ k!·k·(9e² ln⁴ k / k)^{k/(3 ln² k)} = k!·exp(−(k/(3 ln² k))(ln k − O(ln ln k)))
= k!·exp(−(1/3 − o(1))k/ln k). ∎

*Comparison with HK.*  HK Theorem 1.3 covers Q_k = {π : L_Δ(π) ≤ 3√k for all Δ}, whose complement has
size k!·e^{−Θ(√k)}; Theorem 8 covers all π with L_Δ(π) ≤ k/(3 ln² k) for all Δ (and more: up to k/ln k
exceptional Δ are allowed), with exceptional set k!·e^{−Θ(k/ln k)}.  The improvement comes from two
places: (a) Lemma 3 charges a shared row by the *actual* run at that row rather than by the maximal run
log² k in the whole matrix, and (b) the global event 𝒜_{L,s} controls *sums* of runs over sets of ≤ L
cells, which costs only a union bound over (qm)^L sets instead of e^{Θ(k log log k)} structured maps.
The log log k in HK Theorem 1.2 is *not* removed: for π outside 𝒬'_k one still needs HK's structured
decomposition, and its count is governed by the number of admissible exceptional shifts, which is
forced to be ≥ log k by the number-of-components term; see log.md §5 for the exact accounting.
