# W30 — patterns killed by an empty rectangle: statements and proofs

Notation. σ ∈ S_n is identified with its point set S = {(i, σ(i))} ⊂ [n]². For a *generic* point x = (x₁, x₂) ∈ (ℝ∖ℤ)²
with 0 < x₁, x₂ < n+1, σ+x is the standardisation of S ∪ {x} (an element of S_{n+1}); every element of S_{n+1} arises
from exactly n+1 pairs (σ, slot) since a slot is a pair (⌈x₁⌉, ⌈x₂⌉) ∈ [n+1]². p_π(n) = Pr(π ⊄ σ_n),
μ(n) = Σ_{π∈S_k} p_π(n) = E M, N_j(σ) = #{τ ∈ S_j : τ ⊂ σ}. A rectangle Q = [a,b]×[c,d] ⊂ [n]² (positions × values)
has width w = b−a+1, height h = d−c+1, area A = wh; it is *empty* if S ∩ Q = ∅; its open hull is
Q° = (a−1, b+1) × (c−1, d+1), the set of generic points "in Q". Tags: PROVED / HEURISTIC / NUMERICAL.

## 1. Exact characterisation (task 2(i)) — PROVED

**Definition 1.1 (completion cells).** Let τ ∈ S_{k−1} and let T ⊂ S be a copy of τ with positions p₁ < ⋯ < p_{k−1}
and sorted values q₁ < ⋯ < q_{k−1}; put p₀ = q₀ = 0, p_k = q_k = n+1. For (i, j) ∈ [k]² the *completion cell* is
C_{i,j}(T) = (p_{i−1}, p_i) × (q_{j−1}, q_j). For π ∈ S_k and i ∈ [k] let π^{(i)} ∈ S_{k−1} be π with its i-th point
deleted; conversely τ^{+(i,j)} ∈ S_k is τ with a point inserted at position rank i and value rank j, so that
(π^{(i)})^{+(i,π(i))} = π. The k² cells of a copy T tile (0,n+1)² up to the grid lines through T.

**Lemma 1.2.** For generic x: π ⊂ σ+x ⟺ π ⊂ σ, or there are i ∈ [k] and a copy T of π^{(i)} in σ with x ∈ C_{i,π(i)}(T).
*Proof.* A copy of π in σ+x either avoids x (then π ⊂ σ) or uses x as its i-th point for a unique i; deleting x
from the copy leaves a copy T of π^{(i)} and, by definition of the pattern, x has position rank i and value rank π(i)
relative to T, i.e. x ∈ C_{i,π(i)}(T). Conversely a point of C_{i,π(i)}(T) added to T is a copy of π. ∎

**Corollary 1.3 (the revival region).** Put Rev(π) = Rev(π; σ) := ⋃_{i∈[k]} ⋃_{T copy of π^{(i)}} C_{i,π(i)}(T).
(a) If π ⊄ σ then every cell in Rev(π) is an *empty rectangle of σ*, and Rev(π) = {x : π ⊂ σ+x}.
(b) π is killed by the empty rectangle Q in the sense "π ⊄ σ and π ⊂ σ+x for some x ∈ Q°" iff π ⊄ σ and
    Rev(π) ∩ Q° ≠ ∅; in the sense "for every x ∈ Q°" iff π ⊄ σ and Q° ⊆ Rev(π); for a specific x ∈ Q° iff x ∈ Rev(π).
(c) π ⊄ σ ⟺ for every i and every copy T of π^{(i)}, the cell C_{i,π(i)}(T) is empty. In particular π ⊄ σ implies
    that every cell of Rev(π) is contained in some maximal empty rectangle of σ.
*Proof.* (a),(b) restate Lemma 1.2; (c) is Lemma 1.2 with x ranging over the cell (a cell containing a point of S
would give a copy of π in σ). ∎

Remark. (b) shows that "killed by Q" has no canonical single meaning: the natural quantities are K_x(σ) :=
|{π ⊄ σ : x ∈ Rev(π)}| = M(σ) − M(σ+x) for a point x, and the *revival fraction* ρ(π) := |Rev(π)|/(n+1)² (slots) of a
missing pattern. Numerically (results.md §1) Rev(π) is large — a uniformly random x revives ≈ 40 % of the missing
patterns — so the "∃ x ∈ Q" version is vacuous (≈ 99.9 % of M for the largest empty rectangle) and the "∀ x ∈ Q"
version is strong only because it is strong for every big region.

## 2. Random point identity — PROVED

**Proposition 2.1.** Let σ = σ_n be uniform and let x be a uniformly random slot of [n+1]², independent of σ. Then
σ+x is uniform in S_{n+1}, and E K_x = μ(n) − μ(n+1). Consequently
E[ Σ_{π ⊄ σ_n} ρ(π; σ_n) ] = μ(n) − μ(n+1), i.e. the μ-weighted mean revival fraction is 1 − μ(n+1)/μ(n).
*Proof.* The map (σ, slot) ↦ σ+x is (n+1)-to-1 onto S_{n+1} (choose which point of σ+x is x), so σ+x is uniform.
K_x = M(σ) − M(σ+x) since π ⊂ σ ⇒ π ⊂ σ+x; take expectations. The second identity is E K_x = E Σ_{π⊄σ} 1[x ∈ Rev(π)]
= E Σ_{π⊄σ} ρ(π). ∎
(Data check, results.md §1: Σ K_rand / Σ M = 0.40 at k=6, n=27, versus 1 − μ(28)/μ(27) = 1 − 2.407/4.113 = 0.415 from the W24 dumps.)

## 3. Upper bound for a fixed rectangle in a typical σ (task 2(ii)) — PROVED

**Lemma 3.1 (strip deletion).** Let Q = [a,b]×[c,d] with height h. Conditionally on {Q empty}, the standardisation
σ_V of σ restricted to the points with values outside [c,d] is uniform in S_{n−h}. Likewise, conditionally on {Q empty},
the standardisation σ_H of σ restricted to the positions outside [a,b] is uniform in S_{n−w}.
*Proof.* Let V = [c,d] and f = σ^{−1}|_V : V → [n], the positions of the values in V. {Q empty} = {f(V) ∩ [a,b] = ∅}
is f-measurable. Given f, the restriction of σ to the positions [n]∖f(V) is a uniformly random bijection onto
[n]∖V (a uniform permutation conditioned on a partial assignment is uniform on the completions), whose
standardisation is uniform in S_{n−h}; this law does not depend on f, so it also holds conditionally on {Q empty}.
The second statement is the same with positions and values exchanged (apply the argument to σ^{−1}). ∎

**Proposition 3.2.** For every π ∈ S_k and every rectangle Q of width w and height h,
Pr(π ⊄ σ_n | Q empty) ≤ min( p_π(n−h), p_π(n−w) ), hence E[M | Q empty] ≤ μ(n − min(w,h)),
and for every x ∈ Q° (or for K_any, K_all), E[K_x | Q empty] ≤ μ(n − min(w,h)).
*Proof.* π ⊄ σ ⇒ π ⊄ σ_V and π ⊄ σ_H; apply Lemma 3.1. K_x ≤ M. ∎

**Lemma 3.3 (one point costs at most a factor n).** For k ≥ 2 and every π ∈ S_k, n ≥ 1: p_π(n−1) ≤ n·p_π(n);
hence μ(n−j) ≤ n^j μ(n) and E[M | Q empty] ≤ n^{min(w,h)} μ(n).
*Proof.* Av_n(π) ≥ Av_{n−1}(π): if π(1) ≠ k, prepending a new maximum to a π-avoider of length n−1 gives a π-avoider
of length n (a copy of π would have to use the new point as its first and largest entry); if π(1) = k then π(k) ≠ k
and appending a new maximum works. Both maps are injective. So p_π(n−1) = Av_{n−1}/(n−1)! ≤ Av_n/(n−1)! = n p_π(n). ∎

**Corollary 3.4 (scale of the largest defect; PROVED bound + NUMERICAL scale).** If Q is an empty rectangle of area A
then min(w,h) ≤ √A, so E[M | Q empty] ≤ μ(n − √A) ≤ e^{√A ln n} μ(n). The largest empty rectangle of a uniform σ_n
has area A₁ ≈ n ln n (unit-square area ≈ (ln n)/n; data: mean A₁/n² = 0.116 at n = 37 vs ln 37/37 = 0.098, and 0.136 at
n = 27 vs 0.122), so √A₁ ≈ √(n ln n) ≈ k√(C ln n) with n = Ck² — i.e. **min(w,h) ≍ k√ln k**, and the rigorous
factor is e^{O(k ln^{3/2} k)}, while with the empirical slope s(n) := ln μ(n−1) − ln μ(n) ≈ 0.4–0.55 (k = 6, 7; W28 and
out/mu_small.txt) the factor is e^{s·min(w,h)} = e^{O(k √ln k)}. Numerically (results.md §2) the bound
μ(n − min(w,h)) exceeds E[M | Q₁ ≈ w×h] by a factor 12–80 but follows the same exponential trend in min(w,h).

Remarks. (i) The bound is about a *fixed* Q; the largest empty rectangle Q₁ is a maximum over ≈ n² log n
candidates, and {Q₁ = Q} ⊂ {Q empty} carries the extra (negative for M) information that no larger empty rectangle exists.
For a union bound over Q one uses Pr(Q empty) = C(n−w, h)/C(n, h) ≤ e^{−wh/n}: Pr(∃ empty Q with area ≥ A) ≤ n⁴e^{−A/n}.
(ii) What the bound cannot do: for A ≍ n ln n the exponent −A/n = −ln n is dominated by +s√A ≈ +s k√ln k, so
Proposition 3.2 does not exclude that rectangles with min side ≍ k contribute e^{Θ(k√ln k)} to R = E[M | M>0]; the
observed ln R ≈ 0.7k (W28) is compatible with min(w,h) ≈ 8–10 at k = 6, 7 and s ≈ 0.5 (e^{0.5·9} ≈ 90 vs the
factor E[M | top-3 % of A₁]/E M ≈ 20 at k = 6). Closing the gap needs the slope s(n) = O(1) *uniformly in k*
(Lemma 3.3 only gives ln n) — equivalently, the derivative of the per-point rate of W27 — plus the fact that the
maximal rectangles are elongated only rarely.
(iii) "Density" reading of task 2(ii): a pattern π is killed only if it is missing from the uniform sub-permutation
σ_V of size n − h *and* from σ_H of size n − w; the killed set is contained in Miss(σ_V) ∩ Miss(σ_H). We did not find
a way to exploit the intersection (σ_V and σ_H share the n − w − h points outside the cross of Q).

## 4. The deterministic version is false (task 2(iii)) — PROVED bound, NUMERICAL size

**Proposition 4.1.** For every σ and every generic x, |{π ∈ S_k : π ⊂ σ+x, some copy uses x}| ≥ N_{k−1}(σ)/k, hence
K_x ≥ N_{k−1}(σ)/k − N_k(σ).
*Proof.* Each copy T of a τ ⊂ σ has x in exactly one of its cells C_{i,j}(T), so τ^{+(i,j)} ⊂ σ+x through x; the map
τ ↦ τ^{+(i,j)} is at most k-to-one (τ is π minus one of its k points). ∎
This bound is useful only when N_k(σ) < N_{k−1}(σ)/k, which never happens (the same argument with any point of σ in
place of x gives N_k(σ) ≥ N_{k−1}(σ)/k whenever |σ| ≥ k). What matters is the *number of patterns whose every copy
uses x*, and this can be a constant fraction of (k−1)!:
**NUMERICAL (witness_phantom.py).** For σ = the sp(6) = 17 witness 6 14 10 2 13 17 5 8 3 12 9 16 1 7 11 4 15 and k = 7:
N₆(σ) = 720, N₇(σ) = 3502 of 5040; adding one point x at the best of the 18² = 324 slots (position slot 4, value slot 7)
revives K_x = 635 = 0.88·6! of the 1538 missing 7-patterns; the mean over slots is 341 = 0.47·6!, the minimum 102.
So for a *specific* (rigid, minimal) σ one point carries e^{(1−o(1)) k ln k}-many patterns (0.47·k ln k here), and
any statement "one defect kills e^{O(k)} patterns" must be a statement about typical σ — it cannot be deterministic.
The corresponding typical statement is Proposition 3.2; the deterministic mechanism (σ nearly a (k−1)-superpattern
whose k-copies are all rigid) has probability e^{−Θ(n ln n)} under the uniform law (it needs σ far from typical
in every block) and contributes nothing to R at n ≍ k².

## 5. What this means for the programme's conjecture — HEURISTIC, with PROVED pieces

The conjecture of W28 §4 was "E[M | M>0] is governed by defects that each kill e^{O(k)} patterns". The data (results.md)
replace it by the following picture.
(a) PROVED (Prop. 2.1) + NUMERICAL: a random point revives a fraction 1 − μ(n+1)/μ(n) ≈ 0.4 of the missing patterns;
    the centre of the largest empty rectangle revives ≈ 0.75, the best of a 3×3 grid of points ≈ 0.96, and the fraction
    revived by a rectangle's centre is *independent of its area and aspect ratio* (K_c/M = 0.74–0.78 over the whole
    range of areas). So there is no separate quantity "patterns killed by Q": K(Q) ≈ 0.75·M for any large empty Q,
    and the e^{Θ(k)} question is the tail of M itself, i.e. the joint law of the *cluster of cells* of the missing set.
(b) PROVED: the only rigorous handle is Prop. 3.2, E[M | Q empty] ≤ μ(n − min(w,h)), which gives e^{O(k√ln k)}·μ
    for the typical largest rectangle *if* the per-point slope of ln μ is O(1) uniformly in k (open; Lemma 3.3 gives
    only ln n per point, i.e. e^{O(k ln^{3/2} k)}).
(c) HEURISTIC reformulation: writing M = Σ_π 1[π ⊄ σ] and using Cor. 1.3(c), a missing π is a *set of empty cells*
    (one per copy of each child π^{(i)}), and M is large when many patterns' cell-systems are simultaneously empty.
    The number of copies of π^{(i)} in σ_n at n = 0.75k² is e^{Θ(k)} on average (C(n,k−1)/(k−1)! ≈ (0.75e²)^{k}),
    so a missing π certifies e^{Θ(k)} empty cells that lie in the union of the maximal empty rectangles; the
    conjecture R ≤ e^{O(k)} is the statement that the number of patterns whose cell-systems fit into the empty region
    of a typical σ conditioned on M>0 is e^{O(k)}. We could not turn this into a proof; see results.md §4 for the
    per-pattern revival fractions (mean ρ ≈ 0.42, decreasing to 0.37 for patterns in clusters with M ≥ 30).
