# W27 — The comparison principle: statements and proofs

Notation. Π_N = uniform random permutation of length N (equivalently N i.i.d. uniform points in the unit square,
ordered by x, ranked by y). p_π(N) := Pr(π ⊄ Π_N). id_k = 12⋯k. Av_N(π) = #π-avoiders of length N, so
p_π(N) = Av_N(π)/N!. Tags: PROVED / HEURISTIC / NUMERICAL.

## 0. What Alon's conjecture needs, and what CP would give (PROVED, elementary)

**Lemma 0.1 (union bound).** If max_{π∈S_k} p_π(N) ≤ e^{−(1+ε)k ln k} for all large k then Π_N is a k-superpattern
w.h.p. Proof: Σ_π p_π(N) ≤ k!·max ≤ e^{k ln k − (1+ε) k ln k} → 0. ∎

**Lemma 0.2 (block splitting; independence of disjoint position blocks).** For M ≤ N,
p_π(N) ≤ p_π(M)^{⌊N/M⌋}. Proof: the standardisations of Π_N on ⌊N/M⌋ disjoint position blocks of length M are
independent uniform elements of S_M (conditionally on the value sets of the blocks the orders inside the blocks are
independent and uniform), and π ⊄ Π_N forces π ⊄ every block. ∎

Consequences. (a) Any bound p_π(C_0k²) ≤ e^{−ιk²} valid for all π ∈ S_k (one C_0, one ι > 0) already gives
p_π(N) ≤ e^{−(ι/C_0)(N − C_0k²)} — speed N — and Alon's conjecture with n = C_0k² by Lemma 0.1 (ιk² ≫ k ln k).
(b) Conversely the known per-pattern bound (W19 Thm 11: p_π(0.757k²) ≤ e^{−ηk} for all π) gives only speed N/k:
p_π(N) ≤ e^{−ηN/(0.757k)}, i.e. e^{−Θ(k)} at N ≍ k², and Alon only at N = O(k² ln k) (worse than He–Kwan's
k² log log k). So the entire content of the problem, in this language, is the **exponent k² versus k at N ≍ k²**:
a per-pattern tail of exponent ω(k ln k) at N = O(k²), uniformly in π.

**Lemma 0.3 (CP ⇒ Alon).** Suppose CP(K, a): p_π(N) ≤ e^{ak} p_{id}(N/K) for all π ∈ S_k, N. Then Π_N is a
k-superpattern w.h.p. for N = K(1/4 + ε)k², any ε > 0 (with a = o(ln k) allowed). Proof: p_id(M) = Pr(LIS(Π_M) < k) =
exp(−M H_0(k/√M)(1+o(1))) for k/√M → x ∈ (0,2) (Deuschel–Zeitouni 1999; H_0 > 0 on (0,2)); with M = N/K =
(1/4+ε)k², x = 1/√(1/4+ε) < 2, so p_π(N) ≤ e^{ak − c_ε k²} and Lemma 0.1 applies. With the explicit W23 certificate
bound p_id(M) ≤ (M+k)^k (e(k−1)²/(M−k+1))^M one gets the same with N = K e² k² and no asymptotic input. ∎

Remark (only the tail matters). CP at N below the identity's threshold is vacuous (both sides ≈ 1). The
principle is a statement about the LOWER-TAIL LARGE DEVIATIONS of "number of copies = 0" for every π, compared with
the LIS lower tail. Lemma 0.2(a) shows that CP "above threshold" (N ≥ C k² for one fixed C) is all that is needed
(task item (iv)): a bound at one N = C_0k² with exponent ≫ k ln k propagates to all larger N.

## 1. CP(1) is false at fixed k; the correct formulation is asymptotic in k (PROVED / exact enumeration)

**Fact 1.1.** Av_7(1324) = 2762 > 2761 = Av_7(1234) (Bóna; re-verified here by avoid.c), and Av_N(1324) > Av_N(1234)
for all N ≥ 7, with L(1324) ≈ 11.60 > 9 = L(1234). Hence for k = 4 the ratio p_π(N)/p_id(N) exceeds 1 from
N = 7 = 0.44 k² on and grows like (L(1324)/9)^N: **identity-hardest-at-every-N (CP with K = 1) fails already at
k = 4**, inside the window N ∈ [k²/2, 3k²/2].

**Fact 1.2 (CP(K), K > 1, is unfalsifiable at fixed k).** For fixed π ∈ S_k and K > 1,
p_id(N/K)/p_π(N) ≥ Av_{N/K}(id_k)/(N/K)! · N!/Av_N(π) ≥ N!/((N/K)! L(π)^N (N/K)^{...}) → ∞, since N! ≫ (N/K)! e^{O(N)}.
So Stanley–Wilf effects (L(π) = 2^{Θ(k)} for typical π, Fox 2013) never contradict CP(K) with K > 1 at fixed k: the
only content of CP is uniformity in k in the window N ≍ k². The right object is the **per-point rate**
I_π(C) := −(1/N) ln p_π(N) at N = Ck² (finite k), and the conjecture becomes a comparison of rate functions:

**Conjecture CP* (rate form).** There are C_0 < ∞ and ι > 0 such that for all k and all π ∈ S_k,
I_π(C_0) ≥ ι, i.e. p_π(C_0k²) ≤ e^{−ιC_0k²}. (Stronger, "identity-hardest asymptotically":
liminf_k min_{π∈S_k} I_π(C)/I_id(C) ≥ 1/K for every C > K/4.)

**Heuristic 1.3 (why the identity should be the cheapest to avoid at N ≍ k²).** Lower bounds on p_π come from
π-avoiding classes 𝒞: p_π(N) ≥ Pr(Π_N ∈ 𝒞). The identity has the class of merges of k−1 decreasing sequences, of
growth rate (k−1)² and, at N = Ck², probability e^{−N ln(4C/e)(1+o(1))} (DZ). For a random π ∈ S_k every monotone
subsequence has length ≤ (2+o(1))√k, so π is not a merge of m monotone sequences for m < √k/2 and not
(a×b)-griddable by monotone cells for a+b < 2√k; the corresponding π-avoiding classes have growth rates m² ≲ k/4 and
ab ≲ k, i.e. cost per point ≈ ln(Ck) − O(1) ≫ ln(4C/e). The Stanley–Wilf class Av(π) itself has growth 2^{Θ(k)} ≫ k²,
but that growth is only reached for N ≫ 2^{Θ(k)} (Fact 1.2). So at N ≍ k² every *structured* avoidance
mechanism is far more expensive for random π than for the identity — consistent with the W21 thresholds (random π
contained 11% earlier at k = 36) and with CP*. The finite-k crossovers of Fact 1.1 are the small-k shadow of the
Stanley–Wilf regime; §3 measures how the crossover n_×(π) moves with k.

## 2. What is proved: speed-N tails for a class of patterns, and closure properties

### 2.1 Coarse-graining + Mirsky: direct sums of bounded blocks (PROVED)

Setting. Π_N as N i.i.d. uniform points in [0,1]²; cut the square into a g×g array of cells (area 1/g² each).
n_c = number of points in cell c (multinomial(N; 1/g², …)); given (n_c) the standardised patterns of the cells are
independent and uniform. Fix b ≥ 1 and call a cell **good** if its pattern contains every τ ∈ S_b. Let
q_b(n) = Pr(Π_n contains every τ ∈ S_b) (nondecreasing in n) and q̄ := E q_b(n_c), n_c ~ Bin(N, 1/g²).

**Theorem 2.1.** Let π = τ_1 ⊕ ⋯ ⊕ τ_h with all |τ_i| ≤ b (or the same with ⊖ throughout). Then for every g,
      p_π(N) ≤ Pr( #good cells ≤ (h−1)(2g−1) ) ≤ exp( −g² · D( (h−1)(2g−1)/g² ‖ q̄ ) )   whenever (h−1)(2g−1) < q̄ g²,
D(a‖q) = a ln(a/q) + (1−a) ln((1−a)/(1−q)). With g = Λh and N = m g² (m points per cell) this is
      p_π(N) ≤ exp( −(N/m) · D(2/Λ ‖ q̄) ) = e^{−ι N},   N ≥ mΛ²h² (h ≤ k, so N ≥ mΛ²k² suffices),
with ι = D(2/Λ‖q̄)/m > 0 as soon as Λ > 2/q̄; q̄ = q̄_b(m) depends only on b and m, not on k, h, τ_i.

*Proof.* (a) A chain c_1 < ⋯ < c_h of good cells, strictly increasing in both cell coordinates, gives π ⊂ Π_N:
every point of c_i is strictly SW of every point of c_{i+1}, c_i contains a copy of τ_i, and the union is a copy of
τ_1 ⊕ ⋯ ⊕ τ_h. (b) (Mirsky) If the poset E of good cells (strict product order on [g]²) has no chain of length h,
E is a union of h−1 antichains of E, each an antichain of [g]²; the width of [g]² under the strict product order is
2g−1 (the 2g−1 diagonals {(x+t, y+t)} are chains covering [g]², and {(1,y)} ∪ {(x,1)} is an antichain of that size).
Hence |E| ≤ (h−1)(2g−1). (c) The indicators 1[c good] are nondecreasing functions of the n_c (given counts, goodness is
an independent coin with success probability q_b(n_c), which we may realise as 1[U_c ≤ q_b(n_c)] with independent
uniforms U_c), and the multinomial vector (n_c) is negatively associated (Joag-Dev–Proschan); so the indicators are
NA, E e^{−λΣ} ≤ ∏ E e^{−λ 1[c good]}, and the Chernoff lower-tail bound for Bin(g², q̄) applies verbatim. ∎

(No union bound over antichain covers is needed: only the SIZE of the cover enters. The first version of this
proof used the 16^{g(h−1)} count of covers; it is superseded.)

**Corollary 2.2 (explicit instances; q̄ evaluated with Poisson(m) counts).**
(i) Identity: b = 1, q̄ = 1−e^{−m}. m = 3, Λ = 4: ι = D(0.5‖0.95)/3 = 0.28 for N ≥ 48k². Elementary speed-N proof
of the LIS lower tail by a mechanism that does not use the LIS structure (the DZ/W23 rate ln(C/e) is far better).
(ii) Layered patterns with layers ≤ b, in particular (21)^{k/2} (b = 2; a cell is good iff it has ≥ 2 points and is
not increasing; q̄(6) = 0.938): m = 6, Λ = 4: ι = D(0.5‖0.938)/6 = 0.12 for N ≥ 96h² = 24k². First speed-N tail bound
for (21)^{k/2} and for every layered pattern with bounded layers; W19's greedy has failure speed ≤ min(k, strip
height) = 2 for these, so it could not give it.
(iii) Every ⊕-sum (or ⊖-sum) of blocks of size ≤ b: p_π(N) ≤ e^{−ι_b N} for N ≥ Λ_b k², where m = m_b must make a
uniform Π_m a b-superpattern with probability bounded away from 0 — m_b = O(b² log log b) by He–Kwan, O(b²) if
Alon's conjecture holds at scale b. So Alon at scale b implies uniform speed-N tails for all block-diagonal
patterns with blocks ≤ b, of any total length.

### 2.1′ The same trick for GRID patterns: rigid rows, r strips (PROVED; new)

Let 𝒢(r,h) be the one-point-per-cell grid patterns: π ∈ S_{rh} with π((j−1)r + s) = (τ_j(s) − 1)h + j for
arbitrary τ_1, …, τ_h ∈ S_r (block j = positions (j−1)r+1 … jr; strip s = values (s−1)h+1 … sh; τ_j = order in
which block j visits the strips). It contains the tilted grids (12⋯r)^h (all τ_j = id), He–Kwan's family, and
W15's perturbed grids 𝓕 (|𝒢(r,h)| = (r!)^h = e^{k ln r − O(k)}, e^{(1/2 − o(1))k ln k} for r = √k).

**Theorem 2.5.** Cut the square into g_x = rn columns and g_y = rn rows (n ≥ 1), and group them into n column
blocks B_1 < ⋯ < B_n of r consecutive columns and r horizontal strips S_1 < ⋯ < S_r of n consecutive rows. For
i, y ∈ [n] let Z_{i,y} = 1[for every s ∈ [r] the cell (column (i−1)r + τ_j(s)… — precisely: all r cells
{column (i−1)r + t, row (s−1)n + y : t = τ(s) for the block that will use it} are nonempty]. Since the chain will
assign block index j to element (i,y) in order, define Z_{i,y}^{(j)} with τ_j; to keep Z independent of j use the
stronger requirement Z_{i,y} = 1[all r² cells of the r×r sub-array (block B_i) × (row y of every strip) are nonempty].
Then a chain (i_1,y_1) ≺ ⋯ ≺ (i_h,y_h) (both coordinates strictly increasing) with all Z = 1 gives a copy of every
π ∈ 𝒢(r,h) simultaneously: for block j take, in column block B_{i_j}, the point of strip s in column
(i_j −1)r + τ_j(s) at row y_j of strip s. Positions increase with j and within a block follow τ_j; values in strip s
increase with j (rows y_j increase) and strips are ordered. Hence, with E = {(i,y): Z_{i,y} = 1} ⊆ [n]² and Mirsky
as in 2.1(b): {π ⊄ Π_N} ⊆ {|E| ≤ (h−1)(2n−1)}. Let q_r := Pr(Z_{i,y} = 1) ≥ 1 − r² e^{−m}·(1+o(1)) (union bound over
r² cells, m = N/(rn)² points per cell; the o(1) is the binomial/Poisson correction). The Z's are NA (nondecreasing
functions of disjoint groups of the multinomial counts), so
      p_π(N) ≤ exp( −n² D( 2/Λ ‖ q_r ) )   for n = Λh,  N = m r² n² = m Λ² r² h² = m Λ² k²,
uniformly over π ∈ 𝒢(r,h). With m = 2 ln r + 2 (so q_r ≥ 1 − e^{−2} = 0.86), Λ = 4 and D(1/2‖0.86) = 0.365:
      p_π(N) ≤ exp(−0.365 n²) = exp( −N /(2.74 m r²) ) = exp( −N /(2.74 r² (2 ln r + 2)) )   for N ≥ 16 (2 ln r + 2) k²,
uniformly over π ∈ 𝒢(r,h). For the tilted grids (all τ_j = id) only the r "diagonal" cells of each sub-array are
needed, so m = ln r + 2 suffices: p_{(12⋯r)^h}(N) ≤ exp(−N/(2.74 r² (ln r + 2))) for N ≥ 16(ln r + 2)k².

**Honest assessment.** Speed N, but the rate is ∝ 1/(r² ln r): one chain element costs r cells (m r points) and the
sub-columns dedicated to one strip waste a fraction (r−1)/r of the area (their cells in the other strips serve no
element), whence the two factors of r. This is the same 1/r² as W23's periodic-word bound (speed N/(3r²)) — W23's
negative result "any bad-box-tolerance lemma has f ≤ 1/r" is exactly this — with the threshold improved from
9r ln(3er)·k² to 16(ln r + 2)·k² and the class enlarged from the periodic word to all of 𝒢(r,h) (a factor ln r in m).
For r = h = √k the exponent at N = 16(2 ln r + 2)k² is 16k²/(2.74 r²) ≈ 5.8k: **e^{−Θ(k)}, no better than Thm 10 plus
block splitting**. So rigid coarse-graining cannot pass the k-versus-k² barrier for grids with min(r,h) → ∞; it
does pass it for bounded r (Thm 2.5 with r fixed: rate Θ(1)), for direct sums of bounded blocks (Thm 2.1) and for the
identity — precisely the patterns that are chains of O(1)-cost gadgets.

*Remark (generalisation).* The argument needs only (1) a 2-D chain structure: a copy is a chain of h "block-rows",
(2) each block-row's requirement being a local event on disjoint cells of probability ≥ q > 1/2, uniformly in the
block. It therefore covers all patterns of the form "h blocks × r strips with one bounded-size gadget per cell and
all cells of a block-row aligned" (gadgets of size ≤ b need m ≥ m_b(ln r + c)), e.g. the periodic-word patterns
(1^{b}2^{b}⋯r^{b})^h, and by symmetry the same with strips and blocks exchanged.
### 2.2 Direct sums of two arbitrary patterns (PROVED, trivial but useful)

**Lemma 2.3.** For α ∈ S_a, β ∈ S_b and any x, y ∈ (0,1):
p_{α⊕β}(N) ≤ E p_α(Bin(N, xy)) + E p_β(Bin(N, (1−x)(1−y))), and the same for ⊖ with the NW/SE boxes.
Proof: the points in [0,x]×[0,y] and in [x,1]×[y,1] form uniform patterns of binomial sizes, and a copy of α in the
first plus a copy of β in the second is a copy of α ⊕ β. ∎
With x = y = a/(a+b) the two boxes receive N a²/k² and N b²/k² points: the *same* C = N/k² for both parts. Hence
CP* (uniform rate ι at C_0) is closed under ⊕ and ⊖ with ι ↦ ι·min(a², b²)/k², i.e. ι/4 for balanced sums;
CP(K, a) for α, β gives for α⊕β only the weaker p ≤ e^{ak} p_{id_{k/2}}(N/(4K)) ≈ e^{ak} p_{id_k}(N/K)^{1/4}.
Iterating over the ⊕-tree of a separable pattern loses a factor 4 per level, so this is useful only for bounded
depth (e.g. π = α ⊕ β with two halves for which CP* is known).

### 2.3 The relabelling identity (PROVED; reduces every π to a constrained LIS)

**Proposition 2.4.** For every ρ ∈ S_N: Π ↦ ρ∘Π preserves the uniform law, and a copy of id_k in Π at positions I
with value set V becomes, in ρ∘Π, a copy of the pattern ρ|_V at the same positions. Therefore, for every ρ,
      p_π(N) ≤ Pr( Π_N has no increasing k-subsequence whose value set V satisfies ρ|_V ≅ π ),
with equality when the right-hand side is minimised over ρ … in fact with equality for every ρ:
π ⊂ ρ∘Π ⟺ ∃ an increasing subsequence of Π with ρ|_V ≅ π, and ρ∘Π is uniform, so the two sides are equal.
So **p_π(N) = Pr(constrained LIS_ρ,π (Π_N) < k) for every ρ ∈ S_N** — the comparison with the identity is exactly the
question of how much a value-set constraint of "density" |𝒱_π(ρ)|/C(N,k) ≈ 1/k! costs the LIS lower tail.
Examples: ρ = reversal of value blocks of size s turns (21)^h into "an increasing subsequence with ≥ 2 points in
each of h prescribed value strips"; ρ = the tilted grid relabelling turns (12⋯r)^h into an increasing subsequence
with one point in each cell of an r×h grid of value strips × ??? — no: only values are relabelled, positions are not,
so grids are not reachable this way (see §4). The identity is the cheapest instance (no constraint).

## 4. The obstruction: patterns that are not sums of bounded blocks (tilted grids, random π)

**4.1 Why Theorem 2.1 stops at bounded blocks.** The certificate in 2.1 is a cover of the *coarse* poset (cells)
by h−1 antichains; its count 16^{gh} is e^{O(gh)} = e^{O(N/(Λm)·(h/g))} = o(N)·… only because h ≤ g/Λ, i.e. the chain
is required to be a positive fraction of the grid side. The gain over the fine-scale Dilworth certificate of the
identity ((k−1)^N labels) is that goodness of a cell is a *local, i.i.d.-like* event of constant probability, so
the cost is paid per cell (Θ(N) cells) — a genuine speed-N mechanism with no LIS structure. It needs the pattern to
be a CHAIN of local gadgets. A tilted grid (12⋯r)^h with r, h → ∞ is a *lattice* of gadgets: a copy is an r×h array
of points with increasing positions along each block and increasing values along each strip. The natural coarse
version is the fixed-strip model of W20: one cell per (block, strip), one point per cell, with 2(r−1)h order
constraints between neighbouring cells. Its failure has speed min(r, h) (a single empty cell in a *fixed* grid kills
the copy: Pr ≥ k·e^{−m}, and W19 Prop. 3.1 shows every greedy inherits this), and the true event is the intersection
over all ≈ N^{r+h} choices of grid lines — the "Θ(1)-precision coordination of the shared clock across strips" of
W20. The Mirsky trick does not apply: there is no poset whose chains are the grid copies (the constraint graph is
a 2-D lattice, not a chain), and Dilworth-type certificates for 2-D constraint systems (covers of the *gadget*
poset — one gadget per (cell, point) — by antichains) have count e^{Θ(N ln k)} because whole strips are antichains.

**4.2 The e^{O(k)} error factor and the greedy's speed (task (ii), block grids).** Theorem 10 (W11) gives for
block-grid patterns p_π(N) ≤ e^{−c·min(r,h)} at N ≥ (π/8 + ε)k²; block splitting (Lemma 0.2) improves this to
p_π(N) ≤ exp(−c·min(r,h)·N/((π/8+ε)k²)) — speed N·min(r,h)/k². CP(K) would need speed N. So for the diagonal grids
r = h = √k the greedy delivers exponent Θ(√k·C) at N = Ck², versus the k² needed: the greedy's speed min(r,h) DOES
obstruct any CP-type conclusion for grids, with a gap of k^{3/2}; and the e^{O(k)} error factor is irrelevant next to
it (it would matter only once speed N is available, and then only for the constant K: with speed N and rate ι at
C_0, K can be taken ι^{-1}·C_0·H_0-ish). For r or h bounded (Thm 9 / W23: speed N/(3r²)) CP* holds with ι ≈ 1/r².

**4.3 Random π (task (i)/(iii)).** For random π no structured super-pattern of size O(k) is available
(π is not (a×b)-griddable with a+b < 2√k, not a merge of < √k/2 monotone sequences, and not in a direct sum of
fewer than k blocks), so neither Theorem 2.1 nor a reduction to grids applies; the relabelling identity (Prop 2.4)
converts p_π(N) into a constrained-LIS lower tail with a constraint of density 1/k! among value sets, and the
identity is the unconstrained instance. A proof of CP* for random π must therefore control the LIS lower tail
*under a value-set constraint of density e^{−k ln k}* — a large-deviation problem with an entropy cost of exactly the
size of the union bound, which is the same obstruction seen from the other side (W19: per-pattern e^{−ηk}; W22:
every copy-event inequality capped at exponent O(C)).

**4.4 What CP "above threshold" buys (task (iv)).** Lemma 0.2(a): a bound at one N = C_0k² with exponent ω(k ln k),
uniform in π, is enough; no statement at small N (where the Stanley–Wilf crossovers of §3 live) is needed. So the
deep-tail failures of CP(1) at fixed k are harmless for Alon provided the crossover n_×(π) stays inside a window
where p_id itself is still ≥ e^{−o(k²)}... — precisely: CP(K) is only needed for N ≥ Kk²/4·(1+ε), and there any
excess factor e^{o(k²)} is tolerable.

### 2.4 Dead ends on the theory side (recorded with reasons)
- Greene/RSK for layered patterns: containment of (21)^h is NOT a function of the RSK shape. λ_1+λ_2 ≥ 2h is
  necessary but far from sufficient: 3412 and 2143 have the same shape (2,2) and only the latter is (21)^2;
  (h+1)(h+2)⋯(2h) 1 2 ⋯ h has shape (h,h) and avoids (21)^2. So no exact λ-characterisation, and the RSK lower tail
  cannot be transferred.
- Gadget posets for (12)^h ("tight" pairs low point/next high point; or (gap, low point) pairs): the chains are
  copies, but whole strips are antichains, so an antichain cover has e^{Θ(N ln k)} realisations and the size
  argument of Thm 2.1 fails because element goodness is not a product of local events. The rigid-row version
  (Thm 2.5) is what survives, at the price of r cells per element.
- Relabelling identity (Prop 2.4): exact but tautological — the constrained family has density 1/k! among value
  sets, i.e. exactly the union-bound entropy k ln k; no ρ makes the constraint "cheap".
- Direct-sum splitting (Lemma 2.3) loses a factor 4 in the exponent per ⊕-level: useless for the identity itself
  (depth k) and for any pattern with a deep ⊕/⊖ tree; fine for bounded depth.

## 3. Numerics (NUMERICAL; tables in results.md)

Setup: ln p_π(n) for every dihedral class, k = 4 (7 classes, n ≤ 24), 5 (23, n ≤ 38), 6 (115, n ≤ 48/54),
7 (694, n ≤ 45), by the SMC growth estimator (validated against exact avoider counts and the exact LIS tail);
deep-tail runs with larger populations for the extremal patterns at k = 6, 7, 8 (deep/). Excess := ln p_π − ln p_id.

**3.1 Which patterns are harder than the identity.** At every k the set {π : p_π(n) > p_id(n)} for n ≳ 0.5k² is
exactly the set of ⊕-sums (up to symmetry) that contain a DECREASING block of length ≥ 2 next to increasing ones:
k=4: 1324 only; k=5: 14325, 13254, 12435, 12354, 15432, 21354 (+21543 marginally); k=6: 154326, 132546, 123546,
125436, 124365, 123654, 143265, … (26 classes, 110 of 720 patterns at n = 48). The hardest is always
1 ⊕ dec_{k−2} ⊕ 1 (1324, 14325, 154326) or 1 ⊕ 21 ⊕ ⋯ ⊕ 1 (132546 ties at k = 6); Wilf-equivalent classes of the
identity (1243, 2143, 1432 at k = 4) sit at excess 0 within noise. Random-like patterns are much EASIER
(k = 6, n = 48: median excess −1.4, minimum −4.2 for 235164): the identity is close to the hardest pattern but is
not the hardest, and the exceptions are a structurally tiny family (⊕-sums with decreasing blocks).

**3.2 Size of the excess.** Max excess at n = k²: 0.07, 0.32, 0.76 (k = 4,5,6); at n = 1.33k²: 0.19, 0.92, 1.61;
per point at 1.33k²: 0.009, 0.028, 0.034. So the excess grows with k; whether it is Θ(k) (harmless: absorbed by the
e^{O(k)} error factor of CP(1)) or Θ(k²) at fixed n/k² (would refute CP(1) with e^{O(k)} but not CP(K), K > 1)
is what the k = 7, 8 deep runs are for (§3.4 below).

**3.3 Crossovers.** n_×(π)/k² (first n from which the excess stays > 0.02): 0.81 (1324, k=4); 0.52–0.64 (k=5);
0.39–0.58 (k=6). The crossover sits INSIDE the window [k²/2, 3k²/2] and, if anything, moves to smaller n/k² with k —
CP(1) cannot be rescued by "above threshold only" at fixed K = 1. CP(K) with K > 1 is untouched (Fact 1.2).

**3.4 Deep tail (results.md, deep/).** The hardest pattern is 1 ⊕ dec_{k−2} ⊕ 1 at every k ≤ 8; its excess at
n ≈ 1.33k² is 1.33, 2.96, 3.17 for k = 6, 7, 8 (4.0, 3.9 at 1.5k² for k = 7, 8): growing sub-linearly with k in this
range, hence consistent with an e^{O(k)} error factor and inconsistent with e^{Θ(k²)}. Its local per-point rate is
8–15% below the identity's (ratio 0.85–0.92 across k = 6–8, not deteriorating): CP(1) with e^{O(k)} error is
plausible but the rates genuinely differ, so at fixed K = 1 the error factor is the whole story; CP(K) with any
K > 1 has margin. Layered (21)^{k/2} is as hard as the identity (rate ratio 0.96); the 2-strip tilted grids are
easier at every n and have a slightly LARGER rate than the identity; random-like patterns are far easier (median
excess −1.4 at k = 6, n = 48; −3.1 minimum at k = 7, n = 45).

## 5. Conclusion: the precise conjecture, what is proved, the obstruction

**Conjecture (CP, sharpest form supported by the data).** There is an absolute a such that for all k, π ∈ S_k, N:
      p_π(N) ≤ e^{a k} · p_id(N)      (K = 1, error e^{O(k)}),
with the maximum over π attained (for k ≤ 8 exactly, conjecturally always) by 1 ⊕ dec_{k−2} ⊕ 1, whose excess is
Θ(k)·(N/k²)-ish at fixed N/k². Equivalently in rate form: I_π(C) ≥ I_id(C) − O(1/k) for all π and C — a per-point rate
deficit of O(1/k), which is exactly what a "shortening by O(1)" mechanism produces (a copy of 1 ⊕ dec ⊕ 1 needs a
decreasing (k−2)-run inside the rectangle spanned by an increasing pair; avoiding it is comparable to avoiding a
monotone pattern of length k − O(1)). Weaker forms that still suffice for Alon (Lemma 0.2(a)/0.3): CP(K) for any
fixed K > 1, or merely CP* (a uniform positive rate at one C_0). What the data exclude: identity-hardest at every N
(false from k = 4: 1324, and from n_× ≈ 0.4–0.6k² at k = 5–7), and any hope that the extremal family is
"random-like" — the exceptions are the ⊕-sums with decreasing blocks, a family of size e^{O(k)} that is trivially
covered by the union bound anyway.

**Proved here.** Lemmas 0.1–0.3 (reformulation: uniform speed-N/exponent-k² tail ⇒ Alon; block splitting; CP above
threshold suffices); Fact 1.1–1.2; Theorem 2.1 (speed-N tails, threshold O(k²), for all ⊕/⊖-sums of blocks of
bounded size, including (21)^{k/2} and every layered pattern with bounded layers — new); Theorem 2.5 (speed N for
the rigid grid family 𝒢(r,h) with rate 1/(r² ln r) and threshold O(k² ln r) — a modest improvement of W23's
periodic-word bound, same r² loss); Lemma 2.3 (⊕-closure); Proposition 2.4 (relabelling identity).

**Obstruction.** Every proof of a speed-N tail here is a chain-of-local-gadgets argument (Mirsky on a 2-D poset +
a count of good cells). It gives exponent Θ(N) exactly when a copy is a chain of O(1)-cost gadgets; for grids with
min(r,h) → ∞ the gadget costs r cells and wastes a factor r of area (rate 1/r²: exponent Θ(k) for r = √k, no
better than the greedy), and for random π there is no chain structure at all. The greedy's speed min(r,h) is
therefore not an accident of the greedy: rigid coarse-graining of any kind pays 1/r², and a speed-N proof for grids
needs Θ(1)-precision coordination across strips (W20). Passing from exponent k to exponent ω(k ln k) at N = O(k²)
for grids with r, h → ∞ — or for random π — is the open problem, unchanged in nature but now sharply stated as a
lower-tail large-deviation problem with the numerically supported answer "rate ≥ identity's rate − O(1/k)".

## Coordinator's verification note (main session, 2026-08-29 20:15)
Theory (§0–2, §4) verified earlier and folded as Theorem 14. Numerics (§3): the qualitative claim is confirmed by exact
enumeration — Av_9(14325) = 261863 > 261808 = Av_9(12345); Av_10(154326) = 3291662, Av_10(132546) = 3291715,
Av_10(143256) = 3291666 > 3291590 = Av_10(123456) (scratchpad/av9.c, av10.c). BUT the SMC excess magnitudes are
biased upward at k ≥ 5 and deep n: 15432 (k=5) and 123654 (k=6) are Wilf-equivalent to the identity
(Backelin–West–Xin: 1_j ⊕ τ ~ J_j ⊕ τ; exact Av_n equal for n ≤ 10 here), yet results.md lists excess +0.34 (n=38)
and +1.24 (n=48) for them. So the tables' "excess" values carry a systematic error of that order; only the
exact facts and the sign pattern at small n are taken into the paper.
