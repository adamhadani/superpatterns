# W23 — certificate counting for absence of block-grid / periodic patterns

Tags: **PROVED** (complete proof here or cited), **HEURISTIC**, **NUMERICAL**.
Notation as in W11 proof.md §0: Π_N = Poisson process of intensity N on [0,1]²; N = Ck²; fixed-strip
containment ⊂_fix with equal strips S_j = [0,1] × [(j−1)/r, j/r); w = (12⋯r)^m, k = rm.

## 0. Summary of results

* **Thm 1.1 (PROVED).** Pr(LIS(Π_N) < k) ≤ Σ_{n} N!/Π(n_i!)² over compositions n of N into k−1 parts
  ≤ N^{k} (e(k−1)²/N)^N; at N = Ck² this is (e/C)^N e^{O(k ln N)}.  The rate ln(C/e) is asymptotically
  exact as C → ∞ (Deuschel–Zeitouni rate = ln C − 1 + O(1/C)), and for fixed k the loss is only polynomial
  in N (Regev).  The loss is concentrated near the threshold (e instead of 1/4).
* **Prop 1.3 (PROVED, dead end).** Canonical (patience-sorting) covers cannot lower the constant e without
  the RSK computation: the union over pile sequences is an identity, not an inequality.
* **Thm 2.1 (PROVED).** Fixed strips, w = (12⋯r)^m, grid parameters α, β: if N = Ck² with
  C > αβ·ln(e/f), f := 1/r − 1/(rα) − 1/β > 0, then Pr(π_w ⊄_fix Π_N) ≤ exp(−(fN/r)(1 − αβ ln(e/f)/C)).
  With α = 3, β = 3r: C > 9r ln(3er) ⇒ Pr ≤ exp(−(N/(3r²))(1 − 9r ln(3er)/C)).  Speed N/r² (W11 Thm 2.2
  had N/(4r²(r+1)) with threshold 8(r+1)ln(2er²(r+1))).
* **Prop 2.3 (PROVED).** No argument of the form "bad boxes ≤ fM ⇒ containment" (any grid, any
  deterministic lemma) can give a threshold below C = ln r: the band-kill set has density 1/r and blocks,
  and the binomial Chernoff bound is tight.  The threshold cannot be made r-independent along this route.
* **Prop 2.4 (PROVED).** In the fixed-strip model the rate is ≤ 1/r for every C (W11 Prop 3.1), so a bound
  exp(−N(ln C − f(r))) is impossible there; the speed cap N/r is r-dependent, and Thm 2.1 loses one more
  factor r (N/r²) because only the diagonal sub-columns (area 1/r) are used.
* **§3 (PROVED, weak).** Free model: union over strip boundaries costs N^{r−1}; harmless at speed N/r².
* **§4 (NUMERICAL).** Exact absence probabilities (tg.c) for r = 1, 2, 3, k = 12..30, C = 0.5..3, compared
  with e^{−N/r} and the identity's rate.

## 1. The identity: Dilworth certificates

**Theorem 1.1 (PROVED).**  Let X_1,…,X_N be i.i.d. uniform in [0,1]² (or a uniform σ ∈ S_N).  For k ≥ 2,
   Pr(LIS < k)  ≤  Σ_{n_1+⋯+n_{k−1}=N, n_i ≥ 0}  N! / Π_i (n_i!)²                                   (1.1)
               ≤  (N+k)^{k} · ( e (k−1)² / (N−k+1) )^N.                                             (1.2)
At N = Ck²:  Pr(LIS(Π_{Ck²}) < k) ≤ exp(−N ln(C/e) + O(k ln N)).

*Proof.*  If LIS < k then by Dilworth (or Mirsky applied to the decreasing order) the N points are the
union of k−1 decreasing chains D_1,…,D_{k−1} (some possibly empty).  Union bound over the (k−1)^N
assignments a: [N] → [k−1]:  Pr(LIS < k) ≤ Σ_a Pr(each class a^{−1}(i) is a decreasing chain).  For i.i.d.
uniform points the relative orders of disjoint classes are independent, and a class of size n is a
decreasing chain (y decreasing along increasing x) with probability 1/n!.  Grouping assignments by the
class-size vector n (there are N!/Π n_i! of them) gives (1.1).  By log-convexity of n ↦ n!, Π(n_i!)² is
minimised, for fixed Σ n_i = N, when the parts are as equal as possible; the number of compositions is
C(N+k−2, k−2) ≤ (N+k)^{k−2}.  For a composition n write the term as (N!/Πn_i!)·(1/Πn_i!) ≤
(k−1)^N / Π n_i!.  With q = ⌊N/(k−1)⌋ ≥ (N−k+1)/(k−1) and n! ≥ (n/e)^n,  Π n_i! ≥ (q!)^{k−1} ≥
(q/e)^{(k−1)q} ≥ (q/e)^{N−k+1} ≥ ((N−k+1)/(e(k−1)))^{N−k+1}.  Hence each term is at most
(k−1)^N (e(k−1)/(N−k+1))^{N−k+1} ≤ (e(k−1)²/(N−k+1))^N · (N/(e(k−1)))^{k−1} ≤ (e(k−1)²/(N−k+1))^N N^{k−1},
and multiplying by the number of compositions gives (1.2).  For a uniform σ ∈ S_N use the N i.i.d. points
(LIS depends only on the relative order).  At N = Ck², (k−1)²/(N−k+1) = C^{−1}(1+O(1/k)), so the exponent
is −N ln(C/e) + O(k ln N).  ∎

**Remark 1.2 (de-Poissonisation, PROVED).**  {LIS(P) < k} is decreasing in P.  Conditioning on
|Π_N| = n, Pr(LIS(Π_N) < k) ≤ Pr(Poisson(N) ≤ N') + max_{n > N'} Pr(LIS(n i.i.d.) < k).  With N' = N/2:
Pr(Poisson(N) ≤ N/2) ≤ exp(−N(1/2 − (1/2)ln 2)) ≤ e^{−0.15N}, and (1.2) at N/2 gives
(2e(k−1)²/N)^{N/2}: at N = Ck² the bound is exp(−(N/2) ln(C/(2e)) + O(k ln N)) + e^{−0.15N}.  Conversely
the i.i.d. statement is what matters for σ ∈ S_n, and (1.2) applies directly.

**Proposition 1.3 (quantifying the loss; PROVED given the cited rate).**  Deuschel–Zeitouni (1999,
Thm 1.1 lower tail; also Logan–Shepp/Seppäläinen) give, for N i.i.d. points and 0 < x < 2,
   Pr(LIS ≤ x√N) = exp(−N H(x) + o(N)),   H(x) = −1 + x²/4 + 2 ln(x/2) − (2 + x²/2) ln( 2x²/(4+x²) ).
At N = Ck² the event LIS < k is LIS ≤ x√N with x = 1/√C.  Since H(x) = −1 − 2 ln x + O(x² ln(1/x)) as
x → 0, the true rate is ln C − 1 + O(C^{−1} ln C), i.e. **Theorem 1.1 is asymptotically exact as
C → ∞**; the loss δ(C) := H(1/√C) − ln(C/e) is

    C      0.5    1      2      e      4      10     20     50     100    1000
    δ(C)   1.72   1.15   0.74   0.60   0.45   0.23   0.13   0.061  0.034  0.0046
    H      0.023  0.154  0.430  0.596  0.838  1.528  2.126  2.973  3.639  5.912

(the certificate rate ln(C/e) is negative for C < e; the true threshold is C = 1/4).  In threshold terms
the loss factor is 4e ≈ 10.9; in rate terms it is o(1) for large C.

**Proposition 1.4 (fixed k: polynomial loss; PROVED).**  For fixed ℓ = k−1 and N → ∞, both sides of (1.1)
are ℓ^{2N}/N! up to factors N^{O(ℓ²)}: the exact count of permutations with LIS ≤ ℓ is Σ_{λ_1 ≤ ℓ}(f^λ)² ~
c_ℓ ℓ^{2N} N^{−(ℓ²−1)/2} (Regev 1981), while by Stirling the largest term of (1.1) is
N!/((N/ℓ)!)^{2ℓ} = (1+o(1)) ℓ^{ℓ}(2πN)^{−(ℓ−1)} ℓ^{2N}/N! and the sum has ≤ N^{ℓ−1} terms.  For ℓ = 2 exactly: Σ_p N!/(p!(N−p)!)² = C(2N,N)/N! while the truth is
Catalan_N/N! = C(2N,N)/((N+1)N!): the Dilworth bound overcounts by exactly N+1 (each 123-avoiding
permutation has on average N+1 covers by two decreasing chains).  So the exponential loss of Theorem 1.1
appears only when k grows like √N; it is entirely the entropy of non-canonical chain covers.

**Proposition 1.5 (canonical covers do not help; PROVED, dead end).**  Patience sorting assigns each point
(in x-order) to the leftmost pile whose top exceeds its y-value; the piles are decreasing chains and their
number is LIS (Aldous–Diaconis).  Hence LIS < k iff the pile sequence a ∈ [k−1]^N, and
   Pr(LIS < k) = Σ_{a ∈ [k−1]^N} Pr(pile sequence = a)
is an identity.  Any improvement over (1.1) must therefore come from a per-sequence bound
Pr(pile sequence = a) < Π 1/n_i!, i.e. from the "sandwich" constraints top(a_i − 1) < y_i < top(a_i) at
every step.  These constraints couple the piles: for two piles they say that the merged permutation is
123-avoiding with prescribed pile sizes, whose count is the ballot number, and for k−1 piles the count of
sequences with prescribed shape is f^λ (RSK: the pile sequence determines the recording tableau Q and the
insertion tableau P is the final pile configuration).  So evaluating the canonical certificate exactly is
the identity Σ(f^λ)² and its asymptotics is the Logan–Shepp/Vershik–Kerov variational problem — the
canonical route reproduces the known rate but offers no elementary shortcut below e.  (The only elementary
improvement is the factor N+1 for k−1 = 2 above.)  ∎

## 2. Fixed strips, periodic word: certificate bounds and their limits

Setting (W11 §2 with free grid parameters).  r ≥ 2, k = rm, w = (12⋯r)^m, equal strips of height 1/r.
Fix integers n_0 ≥ m (column groups) and n_1 ≥ m (rows per strip).  Column group c ∈ {0,…,n_0−1} is the
x-interval [c/n_0, (c+1)/n_0), cut into r sub-columns of width 1/(rn_0); strip j is cut into n_1 rows of
height 1/(rn_1).  The *relevant box* (c, j, b) is sub-column j of group c intersected with row b of strip
j; there are M := r n_0 n_1 relevant boxes, each of area 1/(r² n_0 n_1), total area 1/r.  A box is *bad*
if it contains no point of Π_N; the bad indicators are i.i.d. Bernoulli(p), p = e^{−λ}, with
   λ := N/(r² n_0 n_1)      (so Mλ = N/r).
Let B be the number of bad relevant boxes.

**Lemma 2.0 (Mirsky, general grid; PROVED).**  If B ≤ B*(n_0,n_1,m) := n_0 n_1 − m(n_1 + r n_0), then
π_w ⊂_fix Π_N.

*Proof.*  Identical to W11 Lemma 2.1 with (n_0, n_1) in place of (2m, 2(r+1)m): the molecule poset
P = {(c, b_1..b_r): all r boxes (c, j, b_j) good} has |P| ≥ n_0 n_1^r − n_1^{r−1}B and width ≤
n_1^r + r n_0 n_1^{r−1}, so by Mirsky's theorem it has a chain of length ≥ (n_0 n_1 − B)/(n_1 + r n_0),
which is ≥ m iff B ≤ B*; a chain of m molecules yields a copy of π_w in the fixed strips (W11).  ∎

**Theorem 2.1 (PROVED).**  Let α, β > 0 with f := 1/r − 1/(rα) − 1/β > 0, put n_0 = ⌈αm⌉, n_1 = ⌈βm⌉,
and N = Ck² with C > αβ ln(e/f).  Then
   Pr(π_w ⊄_fix Π_N)  ≤  exp( −M·D(f ‖ e^{−λ}) )  ≤  exp( −(fN/r)·(1 − αβ ln(e/f)/C) ),
where D(a‖b) = a ln(a/b) + (1−a) ln((1−a)/(1−b)) and λ = C/(αβ)·(1+o(1)).  In particular
 (α, β) = (3, 3r):  C > 9r ln(3er)      ⇒  Pr(π_w ⊄_fix Π_N) ≤ exp(−(N/(3r²))(1 − 9r ln(3er)/C));
 (α, β) = (4, 4r):  C > 16r ln(2er)     ⇒  Pr(π_w ⊄_fix Π_N) ≤ exp(−(N/(2r²))(1 − 16r ln(2er)/C));
 (α, β) = (2, 2(r+1)):  W11 Theorem 2.2 (threshold 8(r+1)ln(2er²(r+1)), speed N/(4r²(r+1))).
The fixed-strip lower bound Pr ≥ e^{−N/r} (W11 Prop 3.1) shows the speed is N/poly(r) genuinely.

*Proof.*  With n_0 = αm, n_1 = βm (rounding changes constants by 1+o(1)): B* = m²(αβ − β − rα) = fM,
M = rαβm², λ = Cr²m²/(r²αβm²) = C/(αβ).  By Lemma 2.0, failure ⇒ B > fM, and B ~ Bin(M, e^{−λ}); the
Chernoff bound gives Pr(B ≥ fM) ≤ exp(−M D(f‖e^{−λ})) when f ≥ e^{−λ}.  Using D(f‖p) ≥ f ln(f/p) − f =
f(λ − ln(e/f)) and Mλ = N/r: exponent ≤ −(fN/r)(1 − ln(e/f)/λ) = −(fN/r)(1 − αβ ln(e/f)/C).  For
(3, 3r): f = 1/r − 1/(3r) − 1/(3r) = 1/(3r), ln(e/f) = ln(3er); for (4, 4r): f = 1/(2r).  ∎

*Remark 2.2 (choice of α, β).*  The speed is (fN/r) = (N/r²)(1 − 1/α − 1/c) for β = cr, and the
threshold is αc·r·ln(e/f).  Both are optimised at moderate α, c; the product form "speed × threshold" is
≈ N ln r, independent of the choice.  Speed N/r² and threshold Θ(r ln r) are the best this lemma can give:
the factor r in β (rows per strip) is forced by Mirsky's width bound n_1^r + rn_0n_1^{r−1}, which is lossy
by a factor ≈ r on product orders (W11 log §3.1).

**Corollary 2.1′ (block-grid class 𝒢(r,h), fixed strips; PROVED).**  Let π_τ ∈ 𝒢(r,h) (W11 §4), k = rh,
m = h.  Declare a molecule (c, b_1..b_r) good iff ALL r² boxes (c, a, j, b_j) (a = sub-column index) are
nonempty.  Then a chain of m molecules gives a copy of π_τ ⊂_fix Π_N (slab t uses group c_t and sub-column
τ_t^{−1}(j) for strip j; the x-order inside the group is then τ_t, and rows increase with t inside each
strip).  Every bad box (among M′ = r²n_0n_1) kills n_1^{r−1} molecules, so Lemma 2.0 holds with B′ (all
bad boxes) in place of B, M′λ = N, and the proof of Theorem 2.1 gives, for C > αβ ln(er/f),
   Pr(π_τ ⊄_fix Π_N) ≤ exp(−(fN/r)(1 − αβ ln(er/f)/C)),   e.g. (3,3r): C > 9r ln(3er²), speed N/(3r²),
uniformly over τ ∈ (S_r)^h.  ∎

**Proposition 2.3 (floor of the box method; PROVED).**  Consider any argument of the form: "for some
partition of the strips into boxes, with M relevant boxes, a bad-box density B/M ≤ f implies π_w ⊂_fix",
followed by a bound on Pr(B > fM), B ~ Bin(M, e^{−λ}).  Then (i) f ≤ 1/r + O(1/n_0) + O(1/n_1) (with
n_0, n_1 the number of distinct box x- and y-ranges per strip), (ii) the resulting bound is non-trivial
only if e^{−λ} < f, i.e. λ > ln r − o(1), and (iii) λ ≤ C for Mirsky-type grids (λ ≤ Cr in general), so
the method gives nothing for C < ln r − o(1) (resp. (ln r)/r): **no r-independent threshold is obtainable
from a deterministic bad-box tolerance**.

*Proof.*  (i) Half-kill (W11 Prop 3.1): declare bad every box of strip 1 whose x-range meets [0,1/2)
and every box of strip 2 whose x-range meets [1/2, 1].  If all points of chains A_1 ⊂ S_1, A_2 ⊂ S_2 lie in
good boxes, every point of A_1 lies right of every point of A_2, so no merge word has a 1 before a 2 and
π_w ⊄_fix (Lemma 0.1(c)).  The killed boxes number ≤ (1/2 + 1/n_0)(M/r)·2 = M(1/r + 2/(rn_0)) (each strip
has M/r boxes, n_0 distinct x-ranges).  Hence any deterministic tolerance satisfies f ≤ 1/r + 2/(rn_0).
(ii) If p := e^{−λ} > f then Pr(Bin(M,p) ≥ fM) → 1 as M → ∞, so the bound Pr(fail) ≤ Pr(B > fM) is
vacuous; a non-trivial bound needs e^{−λ} < f ≤ 1/r + o(1), i.e. λ > ln r − o(1): every box must contain
more than ln r points on average.  (iii) With equal boxes, λ = N/M; a chain of m molecules needs m distinct
column groups and, in every known lemma (Remark 2.2), n_1 ≥ rm rows per strip, so M ≥ r·m·rm = r²m² = k²
and λ ≤ N/k² = C; with only n_1 ≥ m rows one still has M ≥ rm² and λ ≤ Cr.  Hence C ≥ λ > ln r − o(1)
for all Mirsky-type lemmas, and C > (ln r)/r for any conceivable deterministic tolerance lemma.  ∎

**Proposition 2.4 (speed cap and impossibility of the ln C form; PROVED).**  For every r ≥ 2, every C > 0
and every m ≥ 1:  Pr(π_w ⊄_fix Π_N) ≥ e^{−N/r}.  Consequently the fixed-strip rate
g_r(C) := lim inf −(1/N) ln Pr(π_w ⊄_fix Π_N) satisfies g_r(C) ≤ 1/r for all C: the bound requested in the
task, exp(−N(ln C − f(r))) with ln C unbounded, cannot hold in the fixed-strip model for any f.  The
certificate bound of Theorem 2.1 has rate (N/r²)-speed saturating at f/r ≤ 1/(3r²) as C → ∞; the gap
to the cap is the factor r explained in Remark 2.2 and the following: the band-kill event has intensity
N/r on the square but only N/r² on the relevant (diagonal sub-column) region of Theorem 2.1, so the
method's own lower bound is exp(−N/r²)-type, and speed N/r² is the best it can reach.

*Proof.*  W11 Prop 3.1 for the lower bound; the rest is arithmetic (relevant region area 1/r, band-kill
removes a 1/r fraction of it).  Using all r sub-columns per group (Corollary 2.1′) makes the relevant
region the whole square, but the tolerance B* is unchanged while M grows by r, so fMλ is unchanged: the
molecule count |P| ≥ n_0 n_1^r − n_1^{r−1}B is an *average* bound and does not see that killing a whole
sub-column band is needed.  ∎

### 2.5 Certificates that use the randomness of the bad set: what was tried (dead ends, with reasons)

The only way past Proposition 2.3 is a certificate whose count is much smaller than C(M, fM), i.e. one
that exploits that blocking sets are *structured*.  Three natural candidates:

(a) **Molecule-level antichain covers.**  Absence ⇔ the good molecules G ⊂ [n_0] × [n_1]^r are covered
by m−1 antichains of the strict product order (Mirsky).  For r = 1 antichains are lattice paths, there
are ≤ 4^{n_0+n_1} of them, and the union bound "4^{(m−1)(n_0+n_1)} × Pr(all sites outside the cover are
bad)" gives, for a Bernoulli(p) site percolation on [αm]×[βm], a positive rate as soon as
p < exp(−(α+β)ln 4/(αβ−α−β)) — **a constant bad density is tolerated** (this is the r = 1 analogue of an
r-independent threshold, proved by certificate counting).  For r ≥ 2 the antichains live in [n]^{r+1}
and their number is exp(Θ(n^r)) ≫ exp(n²): the certificate has more entropy than the point set.  The
product structure of G does not obviously reduce it: the rank function ρ(c, b) = 1 + max{ρ(c′,b′): c′<c,
b′<b, (c′,b′) ∈ G} has level sets that are general down-sets of [n_1]^r.  DEAD END (entropy).

(b) **Greedy/thread certificates.**  Process column groups left to right with levels b_j; accept a group
iff every strip can advance by ≤ K rows.  Failure ⇒ ≥ (α−1)m+1 rejected groups, each certified by K+1
consecutive bad boxes above the current level in one strip: count ≤ (rβm)^{(α−1)m}·..., probability
e^{−λ(K+1)(α−1)m}: **speed m·λ ≈ k**, not N.  The adversary blocks a greedy with a "wall" of K+1 boxes
per group (linear cost), whereas the true blocking cost is quadratic; any level-based greedy has this
defect (it is the thread model of W9 in disguise).  DEAD END.

(c) **Point-level level functions.**  Strengthening the requirement to "x and the unwrapped height
ỹ = ry − (j−1) both increase along the whole copy" makes a copy a path in a DAG on the points and absence
a layering with rm−1 levels; the per-point entropy is ln(rm) while the classes (level, strip) have only
Ck/r points, and the per-class probability ((ln n)/n)^n does not compensate: the bound is
exp(+N(ln k)/2 + …).  With m levels (period index) instead, level classes are not antichains (the level
is monotone but not strictly under within-strip dominance), so no per-class probability is available
without recording, for every point, the height of the best partner in the neighbouring strip (ln N bits
per point).  DEAD END (the state of the exact DP is an r-dimensional Pareto front; the certificate must
encode it).

*Conclusion of §2 (PROVED + reasons).*  f(r) in the requested form is: threshold C_0(r) = 9r ln(3er)
(Theorem 2.1; W11: 8(r+1)ln(2er²(r+1))), floor for all deterministic-tolerance lemmas C_0(r) ≥ ln r − o(1)
(Prop. 2.3); the speed is N/(3r²) (Theorem 2.1) against the cap N/r (Prop. 2.4); the ln C growth is
impossible in the fixed model.  An r-independent threshold with speed N/poly(r) requires a
randomness-exploiting certificate, and the three natural ones fail for the reasons above.

## 3. Free model (PROVED, weak)

For the free periodic pattern, containment ⇐ fixed-strip containment for ANY choice of strip boundaries
0 < H_1 < ⋯ < H_{r−1} < 1 (W11 Lemma 0.1(b)).  Hence Pr(π_w ⊄ Π_N) ≤ Pr(π_w ⊄_fix Π_N) for the equal
strips, and no union bound is needed: the free model only helps.  Conversely, a union over boundary
choices cannot *improve* an upper bound; it would be needed only to transfer a lower bound (Prop 3.1)
to the free model, which is false there (the free rate is unbounded in C: the free periodic pattern is
contained whenever LIS ≥ k, and Theorem 1.1 gives rate ≥ ln(C/e) − o(1), independent of r).  Thus in the
free model Pr(π_w ⊄ Π_N) ≤ min{ (e/C)^N e^{O(k ln N)}, Theorem 2.1 } — the identity bound already has
the ln C form with f(r) = 1, r-independent, but only for C > e and with the wrong (fixed-r-only)
comparison class: it says nothing new for Alon's conjecture since C > e is above the He–Kwan constant
only in the sense of the constant, and the union over the residual class still needs the union-bound
slack of W24.

## 4. Numerics (NUMERICAL): exact fixed-strip absence probabilities vs the bounds

tg.c (W11, exact Pareto-front DP, FIXED equal strips, tilted grid r × h = k/r; N i.i.d. uniform points);
2·10⁵ samples per point (10⁵ for batch 1), seeds 7 and 11, out/fix.txt, out/fix2.txt, analyze2.py.

Pr(π ⊄_fix Π_N), N = Ck² (r = 1 is the identity, Pr(LIS < k)):

    C:        0.30    0.35    0.40    0.45    0.50    0.55    0.60    0.70
    r=1 k=12  .811    .579    .297    .125    .0401   .0097   .0018   2.0e-5
    r=1 k=18  .756    .421    .133    .0256   .0028   1.3e-4  5e-6    <5e-6
    r=1 k=24  .689    .276    .0521   .0036   9.3e-5  5e-6    <5e-6   <5e-6
    r=2 k=12  .906    .756    .511    .300    .143    .0558   .0180   8.1e-4
    r=2 k=18  .869    .610    .282    .0858   .0159   .0019   1.4e-4  <5e-6
    r=2 k=24  .814    .433    .120    .0137   6.4e-4  2.5e-5  <5e-6   <5e-6
    r=3 k=12  .953    .865    .692    .500    .314    .171    .0822   .0102
    r=3 k=18  .935    .767    .474    .215    .0669   .0142   .0021   <5e-6
    r=3 k=24  .902    .616    .257    .0520   .0051   2.4e-4  <5e-6   <5e-6
    r=3 k=30  (C=0.5) 1.1e-4

Empirical rate −ln P / N (same grid), with the Deuschel–Zeitouni rate H(1/√C) and the fixed-strip cap 1/r:

    C:        0.30    0.35    0.40    0.45    0.50    0.55    0.60    0.70   cap 1/r
    r=1 k=12  .0049   .0109   .0211   .0321   .0447   .0585   .0734   .1073   1
    r=1 k=18  .0029   .0076   .0155   .0251   .0362   .0502   .0628    —
    r=1 k=24  .0022   .0064   .0128   .0217   .0322   .0385    —       —
    DZ H      .0005   .0029   .0077   .0146   .0232   .0334   .0446   .0697
    r=2 k=12  .0023   .0055   .0116   .0186   .0270   .0364   .0465   .0706   1/2
    r=2 k=18  .0014   .0044   .0098   .0168   .0256   .0350   .0458    —
    r=2 k=24  .0012   .0042   .0092   .0165   .0255   .0334    —       —
    r=3 k=12  .0011   .0029   .0064   .0107   .0161   .0223   .0289   .0454   1/3
    r=3 k=18  .0007   .0023   .0058   .0105   .0167   .0239   .0318    —
    r=3 k=24  .0006   .0024   .0059   .0114   .0183   .0263    —       —
    r=3 k=30   —       —       —       —      .0203    —       —       —

Readings.  (i) The identity's empirical rate decreases with k towards the DZ rate (0.045 → 0.032 at C = 0.5
vs H = 0.023; the N^{1/6} Tracy–Widom correction is still large at k ≤ 24).  (ii) For r = 2, 3 the rate at
fixed C is essentially k-independent already (r=2, C=0.5: .0270, .0256, .0255; r=3: .0161, .0167, .0183, .0203),
i.e. speed N with no visible finite-size drift, and it is ≈ 1/r of the identity's at the same C in the
sample: r=2 ≈ 0.55–0.8 × identity, r=3 ≈ 0.36–0.6 × identity, both increasing towards the identity's value as
k grows.  (iii) All rates are far below the cap 1/r (Prop 2.4) — at C ≤ 0.7 the fixed-strip rate is
< 0.05 for r = 2 — and Theorem 2.1 is vacuous here (its threshold is C > 9r ln(3er) ≈ 51 for r = 2,
≈ 82 for r = 3); at such C the true probability is far below anything measurable, so the certificate bound
is only checked in the regime where the deterministic Lemma 2.0 applies (W11 validated the lemma itself).
(iv) A fixed-strip threshold C_{1/2}^{fix} (P = 1/2): ≈ 0.37 (r=1), 0.40 (r=2), 0.45 (r=3) at k = 12,
decreasing with k (0.29/0.34/0.39 at k = 24), consistent with W11 §6.2; nothing grows with r at these sizes.
Conclusion: the numerics are consistent with a rate g_r(C) that is positive for all C > 1/4-ish, of order
(1/r)·(identity rate) at small C, and capped by 1/r; the certificate bounds of §2 describe only the
C ≳ r ln r regime and are numerically inaccessible.
