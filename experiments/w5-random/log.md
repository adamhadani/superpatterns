# W5 — random permutations as superpatterns (log)

Date: 2026-08-29.  Directory: work/w5-random/.  Files: sp.c (checker), bf.c (brute-force cross-check),
chain.c (τ-chain DP), hk.pdf/hk.txt (He–Kwan arXiv:1911.12878v2), out/*.txt (raw runs).

Definitions used below.  t(n) (Arratia) = least m such that ≥ 1/2 of S_m are n-superpatterns.
Poissonized model: Π_N = Poisson point process of intensity N on [0,1]²; σ ∈ S_N uniform ≈ N uniform points.
θ(π) = "containment threshold" of a single π ∈ S_k (N above which Pr(π ⊂ Π_N) → 1).  Alon's conjecture
(1/4+ε)k² for superpatterns implies θ(π) ≤ (1/4+o(1))k² for every π (He–Kwan Conj. 5.3, itself open).

--------------------------------------------------------------------------------------------------
## Part 1 — empirical

### Checker (sp.c) — verified against brute force
For σ ∈ S_m compute the set of n-patterns contained as a bitset over n! codes (code_j = code_{j-1}·j + r_j,
r_j = # earlier chosen values below the new one; a prefix of the code is the code of the prefix pattern).
DFS over n-subsets in position order, pruned when cnt[j][prefix] = n!/j! (every completion of that prefix
pattern already found); seeded first with 200·m² random subsets so that pruning bites immediately.
Cross-checked against unpruned enumeration (bf.c) on identical permutations: n=5,m=14 (15 perms), n=6,m=20
(8 perms), n=7,m=30 (3 perms) — per-permutation counts of contained patterns agree exactly.
Speed: n=8,m=48 ≈ 0.1 s/perm; n=9,m=60 ≈ 3 s/perm; n=10,m=75 ≈ 75 s/perm.


### 1.2 Reproduction of Engen–Vatter's t(n) (frac = fraction of random σ ∈ S_m that are n-superpatterns)
n=4: m=11 .30, 12 .45, 13 .67 (400 each)                       → t(4)=13 ✓
n=5: m=18 .30, 19 .52, 20 .65 (400 each)                       → t(5)=19 or 20 (EV: 20; 19 is at 1σ)
n=6: m=26 .35, 27 .46, 28 .57 (400 each)                       → t(6)=28 ✓
n=7: m=33 .099, 34 .188, 35 .280, 36 .413, 37 .552 (1000 each) → t(7)=37 (EV: 36; 36 gives .41±.016, so EV's 36 looks slightly off)
n=8: m=44 .17, 45 .30, 46 .37, 47 .44, 48 .59, 49 .67, 50 .79, 51 .81, 52 .86, 53 .91 (300 each) → t(8)=48 ✓
(EV's own values were obtained by sampling too; they say so.)

### 1.3 New values (out/n9_*.txt, out/n10_*.txt)
n=9: m=54 .11 (100), 56 .22 (100), 58 .43 (60), 60 .53 (60), 62 .75 (60), 64 .80 (60), 66 .89 (100), 68 .97 (100)
     → t(9) = 60 (±1; 59 not run — 58 gives .43±.06, 60 gives .53±.06).
n=10 (75 s/sample; pooled over 3–4 independent seeds per m): m=72 12/18 = .67, 76 15/18 = .83, 80 12/12;
      m=66, 68 (20 samples each) — see out/n10_m66_s*.txt, n10_m68_s*.txt and the summary line at the end of this file.
      → t(10) ≈ 68–72 (≤ 72 with confidence; see final line).
Summary table (this work; EV values in brackets where different):
  n :    1  2  3   4   5      6   7      8   9    10
  t(n):  1  3  7  13  19–20  28  37[36] 48  60   ≈68–72

### 1.4 Fits of t(n), n = 4..8 (t = 13,20,28,36,48)
n:            1     2     3     4     5     6     7     8
t(n)/n²:    1.00  .750  .778  .812  .800  .778  .735  .750
√t − n/2:    .50   .73  1.15  1.61  1.97  2.29  2.50  2.93
- t ≈ a·n²:            a = 0.755 (residuals ≤ 1.1).  Over this range t(n) ≈ 3·(n²/4), NOT n²/4, and also > n²/2.
- t ≈ a·n² + b·n:      a = 0.667, b = 0.61 (residuals ≤ 0.9) — best 2-parameter fit; a ≈ 2/3 (!).
- t ≈ (n/2 + c)²:      fails (c would have to grow: √t − n/2 increases ≈ 0.4 per unit n; residuals up to 9).
- log-log slope (4..8): 1.86 — still below 2, so the pre-asymptotic correction is large and positive.
Adding t(9)=60, t(10)≈70: t/n² = .741, ≈.70; √t−n/2 = 3.25, ≈3.4; log-log slope 8→10 ≈ 1.7.
Verdict: the data through n = 10 do not support n²/4 at all in this range; they are closest to
(2/3)n² + O(n) or 0.75n².  This is *not* evidence against Alon (the LIS of a random permutation of length
n²/4 is only ≈ n − c·n^{2/3}·(n²/4)^{-1/6}… i.e. even the monotone pattern alone needs ≈ (1+O(n^{-2/3}))n²/4 plus
a huge finite-size term: LIS(N) ≈ 2√N − 1.77 N^{1/6}, so LIS ≥ n needs √N ≥ n/2 + 0.9 N^{1/6}, i.e. N ≈ (n/2+1.5)²
already for n=8: (5.5)² ≈ 30 — and the last 1% of patterns costs much more than the median one).  The point of
the table is rather that √t − n/2 keeps growing (≈2.9 at n=8): the "half-probability" superpattern length is
dominated by rare-pattern tails, not by the LIS constant, at every accessible n.

### 1.5 Which patterns appear last (classification of the full missing-count vector over S_n, at m just below t(n))
Class means (ratio of a class's mean miss-count to the all-patterns mean); "layered" = ⊕ of decreasing blocks
(includes n…1), "co-layered" = its complement (⊖ of increasing blocks, includes 12…n):
                     n=5,m=17 (20000 σ)   n=6,m=25 (4000 σ)   n=7,m=33 (1500 σ)
  co-layered              1.15                1.44                1.87
  layered                 1.12                1.30                1.73
  skew-decomp. other      0.99                1.06                1.10
  sum-decomp.  other      0.97                0.99                1.08
  ⊕/⊖-indecomposable      0.88                0.83                0.79
The gap widens with n.  The monotone patterns are NOT the very last ones: at n=6 the top of the list is
345621, 564231, 653421, 215436, 154326, then 654321 (rank 6 of 720, 98 misses; 123456 had 67 — by symmetry σ ↦ reverse(σ) the two must have equal miss
rates, so this 98-vs-67 gap over 4000 samples is a ≈2.5σ fluctuation; at n=7 they agree, 24 vs 21).
At n=7 the top is 7234561, 2134576, 6754123, 6753412, 7643512, 5764123, 1654327, 1432567, 1236547, … ;
7654321 has rank ≈ 10–15 and 1234567 rank ≈ 20 (of 5040), each ≈ 2× the average miss rate, while the
top layered patterns are ≈ 2.5×.
Structural reading: the last patterns are layered/co-layered permutations whose blocks are a mix of one big
monotone block and a few blocks of size 1–3 (e.g. 1 ⊕ 321 ⊕ 21, 21 ⊕ 4321 ⊕ 1, 1 ⊕ 54321 ⊕ 1), i.e. "monotone
with a few small stairs at the ends".  This is exactly what Lemma A predicts at finite n: a ⊕-decomposition
forces the copy into diagonal sub-squares, and a block of size 2 or 3 costs a square of side ≈ 2/√N
(need λ ≈ 4–5 expected points to see a 21 reliably) versus 1/√N per element for a long monotone block; so a
layered pattern with r small blocks needs ≈ (k/2 + 1.1 r)²/… points, more than the monotone pattern's
(k/2 + O(k^{1/3}))².  Asymptotically this correction is O(rk), i.e. lower order iff r = o(k) — consistent with
Alon — but for k ≤ 10 it dominates.  Indecomposable ("quasirandom-like") patterns are the easiest, as in
He–Kwan's picture (they have exponentially small failure probability with many disjoint ways to embed).

### 1.6 τ-chains: an asymptotic test of Alon's conjecture (chain.c; exact DP; means over 8 point sets)
L_τ(N) = max L with τ^{⊕L} ⊂ N uniform points.   Alon ⇒ lim L_τ/√N = c_τ ≥ 2/|τ|.   Baselines: c_12 = 1,
c_123 = 2/3 exactly (chains of 12- or 123-blocks are just LIS/2, LIS/3).
   N     L_12     L_21   |   N    L_123  L_321  L_132  L_231  L_312  L_213
   400   17.88   18.25   |  200    8.12   7.50   8.12   8.25   8.12   8.38
  1600   36.50   36.62   |  400   11.50  11.62  11.88  11.62  11.50  12.00
  6400   77.12   76.12   |
Within noise, L_τ(N) = L_{12…j}(N) for every τ of length 2 and 3: the longest τ-chain is as long as the
LIS divided by |τ|.  So for these ⊕-of-small-blocks patterns the threshold is (1/4+o(1))k², matching the
monotone one — supporting Alon's conjecture, and showing the finite-n excess in §1.5 is the additive
(k/2 + c·r)² effect, not a different constant.  (Conjecture suggested by the data: c_τ = 2/|τ| for all τ,
i.e. a random point set's longest τ-chain ≈ LIS/|τ|.)

--------------------------------------------------------------------------------------------------
## Part 2 — theory

### 2.1 He–Kwan's proof, and where log log k comes from  (all of this is a reading of their paper: PROVED by them)

Reduction (Lemma 2.2). Cut [0,1] (values) into 2k rows of height 1/(2k) and positions into m = n/(4k)
column-blocks of 4k consecutive positions; M(y,x) = 1 iff block x has a point in row y.  M dominates an i.i.d.
Bernoulli(1/2) matrix, and π ⊂ M ("permutation matrix P_π is an interval minor of M") ⇒ π ⊂ σ.  So one needs:
a random (2k)×m ±-matrix is k-universal whp.  This step already loses a constant: n = 4k·m, and m ≥ 2k is
forced (k ones needed in ≤ m columns at density 1/2), so the reduction can never give better than n ≈ 8k².

Single thread (Alon's O(k² log k)).  Fix a shift t ∈ [k].  Scan row π(1)+t left-to-right until a 1, then row
π(2)+t from the next column, etc.  Each query is a fresh fair coin; the thread exposes ≤ 1 entry per column,
so it fails only if m coins give < k heads: Pr(fail) ≤ e^{-Ω(m)}.  Union bound over k! patterns needs
m ≫ k log k, i.e. n ≫ k² log k.  This is the whole loss: per-pattern failure e^{-Ω(n/k)} vs. k! patterns.

Amplification (He–Kwan).  Run ℓ = log² k threads t_1<…<t_ℓ in the same M.  If thread i fails it has exposed
m entries; if those are mostly *fresh* (not exposed by threads 1..i−1) then conditioned on anything about the
earlier threads, Pr(thread i fails) ≤ e^{-Ω(k)} again, and the product gives e^{-Ω(k·ℓ)} = o(1/k!) already at
m = O(k), i.e. n = O(k²).  Threads t and t+Δ can share an entry (y,x) only if both are in row y at column x;
sharing a whole sequence of rows requires a Δ-shift in π: sets A,B, π(a_i) = π(b_i)+Δ.  The deterministic
worst case really occurs: once the two threads sit in the same (row,column) they "ride together" — the
lagging thread finds exactly the ones the leading thread found — for the length of the Δ-shift.  Hence
|T_t ∩ T_{t+Δ}| ≤ L_Δ(π)·(max run of zeros) ≤ L_Δ(π)·log²k on the event A (no run of zeros > log² k).
Quasirandom π (L_Δ ≤ 3√k for all Δ, which holds for (1−o(1))k! patterns): m = 5k works → Theorem 1.3, n = 20k².

Structured part.  Non-quasirandom π has long Δ-shifts for many Δ, which pins π down: Lemma 4.2 splits
[k] = Q ∪ Z with π|_Q quasirandom and π|_Z a "structured map" from a family Z_k, |Z_k| ≤ e^{21 k log log k}.
The structured part is NOT handled by threads at all: it is handled by a union bound (event B: for every
φ ∈ Z_k and every placement, the total zero-run length at the placement is < 16·21·k log log k), and B needs
m ≥ 17·21·k log log k because there are e^{21k log log k} structured maps.  That is the whole source of
log log k: the number of structured maps.  Their §5 shows the count is tight for their notion: the family
L_k = {π : π is a union of r = log^{10}k increasing subsequences, each occupying an interval of values}
(equivalently: π^{-1} has ≤ r ascending runs) has |L_k| ≈ r^k = e^{Θ(k log log k)} and lies in Z_k.

So to remove log log k with their architecture one needs, for every π, Pr(π ∉ σ) ≤ e^{-ω(k log k)} at
n = Ck² (their Conjecture 5.1 asks for e^{-k^{3/2+o(1)}}, and Fox's construction shows this is best possible
for typical π).  Note the inversion: quasirandom π have the *worst* containment probability (e^{-k^{3/2}}),
structured π (monotone: e^{-Ω(k²)}) the best; He–Kwan's technique is only weak on structured π because it
handles them by counting.  The hard cases are hybrids (tilted grid; members of L_k with the runs interleaved).

### 2.2 What I can prove (PROVED unless marked)

Lemma A (direct sums; PROVED).  Let π = π₁ ⊕ π₂ ⊕ … ⊕ π_r (block-diagonal; skew sums identical by symmetry).
If Π_{N_i} contains π_i with probability ≥ 1−δ_i for each i, then Π_N with N = (√N₁+…+√N_r)² contains π with
probability ≥ 1 − Σδ_i.
Proof.  Put squares S_i of side s_i = √(N_i/N) along the diagonal (Σ s_i = 1, disjoint).  Π_N restricted to S_i
is Poisson of intensity N on an s_i×s_i square, i.e. an affine image of Π_{N s_i²} = Π_{N_i}; the restrictions
are independent.  Copies of π_i in S_i, i = 1..r, together form a copy of π since S_i lies entirely
below-left of S_{i+1}.  ∎  (De-Poissonization: containment is monotone in the point set and |Π_N| is
concentrated, so the same holds for uniform σ ∈ S_{N(1+o(1))}.)

Corollary A1 (layered permutations; PROVED).  If π is layered (⊕ of decreasing blocks) with r blocks of
sizes k_i ≥ K₀(ε), then θ(π) ≤ (1/4+ε)k².  More precisely, with N_i = (1+ε)k_i²/4 (monotone blocks: LIS
theorem), N = (1+ε)(Σk_i/2)² = (1+ε)k²/4, and failure ≤ Σ δ_i where δ_i = Pr(LIS(Π_{N_i}) < k_i) ≤ e^{-c k_i²}
(lower-tail large deviations for LIS, speed N).  So Alon's Conj. 5.3 holds for all layered π with all block
sizes ≥ K₀(ε) (and by symmetry for co-layered ones).  Same argument for any ⊕/⊖-decomposition into blocks of
"known" threshold: θ(⊕π_i)^{1/2} ≤ Σ θ(π_i)^{1/2}.
Limitation: for blocks of bounded size the additive corrections do not vanish.  E.g. π = (21)^{⊕k/2}: a 21 in a
diagonal square with λ expected points appears with probability p(λ) = 1 − e^{-λ}I₀(2√λ), and the best
diagonal-square strategy gives only max_λ p(λ)/√λ ≈ 0.40 blocks per √N, i.e. θ ≤ (1/0.40)²·k²/4 ≈ 1.6 k², far
above k²/4.  Whether such patterns are really harder than the identity is exactly the c_τ question below.

Lemma B (τ-chains; standard, proof as for Hammersley's LIS theorem — PROVED modulo citing the subadditive
ergodic theorem).  Fix τ ∈ S_j.  Let L_τ(N) = max L such that τ^{⊕L} ⊂ Π_N.  Then L_τ(N)/√N → c_τ a.s. and in
mean, for a constant 0 < c_τ < ∞ (super-additivity comes from Lemma A; c_τ ≤ e/j from the first moment
E#copies = C(N,jL)/(jL)!, and c_τ ≥ 0.4/… >0 from the diagonal-square greedy).  c_{1} = 2 (LIS), and
c_{12} = 1 exactly (a chain of 12-blocks is an increasing sequence of even length).
Consequence.  Alon's conjecture ⇒ θ(τ^{⊕L}) ≤ (1/4+o(1))(jL)² ⇔ c_τ ≥ 2/j.  Conversely, if for some τ one
finds c_τ < 2/|τ| then π = τ^{⊕L} has threshold > k²/4·(1+o(1)) and Alon's conjecture is FALSE (a random
permutation of length (1/4+ε)k² would miss τ^{⊕ k/|τ|}).  This is a concrete, testable criterion.
Numerics (chain.c, DP over blocks with a Fenwick prefix-max sweep, exact): see §1.4.

Proposition C (the obstruction family is easy for a direct argument; HEURISTIC, sketched).  For π ∈ L_k with
π^{-1} having r ascending runs (values split into r intervals, each increasing in position), split the square
into r horizontal strips of heights k_i/k.  A copy of π is r increasing chains, one per strip, interleaved in
x according to the word w ∈ [r]^k.  For fixed r, the event "no such interleaved chain of total length k at
N = Ck²" is a lower-tail LIS-type event in a product of r independent Poisson strips and should have
probability e^{-Ω(N/poly(r))}; that beats r^k as soon as r ≤ k^{o(1)} — covering the whole family L_k with
r = polylog k.  I could not turn this into a proof: the interleaving word forces the x-coordinates of the r
chains to alternate in a prescribed way, and I do not know a large-deviation bound for "interleaved LIS".

### 2.3 Attempts to remove log log k, and the obstacle (all HEURISTIC / FAILED)

(i) Second moment on X_π = #copies.  E X_π = C(N,k)/k! is the same for all π (first-moment threshold k²/e²
for every π!), but X_π is log-normally spread (copies cluster), Var/E² is exponentially large, and no version
of the second moment gives tails e^{-k log k}.  Dead end — this is why LIS needs Hammersley/Logan–Shepp.

(ii) Disjoint-region amplification.  Split the square into ℓ vertical strips and run one greedy per strip:
independence is free but each strip needs N/ℓ ≥ Ck² points on its own, so the total failure e^{-Ω(N/k)} is
unchanged.  Amplification must reuse the SAME points with different exposure patterns (as He–Kwan do): a
thread exposes only m of the 2km entries, so up to ~k mostly-disjoint threads are conceivable, giving
e^{-Ω(N)} — which Fox's construction shows is false for typical π; so any proof must use ≈ log k threads
whose overlap is controlled by π's structure, i.e. exactly He–Kwan's dichotomy.

(iii) Other thread families.  Instead of shifts t, use arbitrary increasing injections f:[k]→[2k] (rows f(π(j))).
Two threads f,g can ride together on the rows where f∘π and g∘π coincide *in increasing order of index*, i.e.
along the LIS of the partial map π^{-1}g^{-1}fπ.  For structured π (unions of few increasing runs) this LIS is
Θ(k) for essentially all pairs f,g; so no choice of thread family fixes the structured case.

(iv) Refined accounting of "riding together" (the most promising idea I found; HEURISTIC).  He–Kwan's bound
|T_t ∩ T_{t'}| ≤ L_Δ·log²k is worst-case in the columns: it charges every row of the Δ-shift.  But two threads
share entries only while they are in the same row at the same column.  Between consecutive elements of the
shift (a_i,b_i) → (a_{i+1},b_{i+1}) each thread handles the pattern elements strictly between them, which lie
in different rows for the two threads, so the threads separate; to coincide again at the next shared row they
must re-align in the column, and stalling one thread costs it fresh exposed zeros.  A potential-function
argument ("shared entries ≤ log²k × number of re-alignments, and each re-alignment costs Ω(1) fresh
exposures on average") would replace L_Δ by the number of *maximal runs of consecutive-in-π* shift pairs —
which for the L_k family (runs interleaved with other runs) is small.  I did not manage to make this
rigorous: the difficulty is that conditioning on earlier threads' failure exposes long zero-runs that the
lagging thread can use for free, and the accounting must be deterministic in the exposed set.

(v) Weak but honest target: a k-superpattern at n = Ck² for *all* π simultaneously would follow from
Pr(π ∉ σ) ≤ e^{-C'k log k} for each π at n = Ck².  What is proved: this holds for quasirandom π (HK Prop 5.2,
e^{-Ω(k^{5/4})}) and for monotone / layered-with-large-blocks π (Lemma A + LIS lower tail, e^{-Ω(k²)}).  The gap
is precisely the hybrid class (many interleaved structured pieces), where neither method applies.

Status.  Nothing new is proved beyond Lemma A/Corollary A1 (routine but I have not seen it stated) and the
reformulation of Alon's conjecture for τ^{⊕L} as c_τ ≥ 2/|τ| (Lemma B), which gives a genuinely falsifiable
numerical test.  No progress on removing log log k; the obstacle is identified exactly (structured-map count,
handled by union bound, tight for the L_k family) together with a candidate repair (iv).

--------------------------------------------------------------------------------------------------
## Final n=10 line (pooled over independent seeds; 75 s/sample)
m=66: 5/20 = .25;  m=68: 2/20 = .10 (noise: 0,0,2,0 of 5);  m=72: 12/18 = .67;  m=76: 15/18 = .83;  m=80: 12/12.
→ t(10) ≈ 70–72 (binomial ±.11 at 20 samples).  Final table:
  n :    1  2  3   4   5      6   7      8   9   10
  t(n):  1  3  7  13  19–20  28  37[36] 48  60  ≈70–72
t(n)/n²: .74 (n=9), ≈.70 (n=10); √t − n/2 = 3.25, ≈3.9;  log-log slope over 8→10 ≈ 1.7.
