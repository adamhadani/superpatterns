# W8 — rows with NON-monotone internal patterns: does the mechanism help?

Started 2026-08-29 (time-boxed ≈ 90 min; long runs continue in background, see §5).

Language. A *row-structured* permutation = word w ∈ [m]^n + row patterns ρ_ℓ ∈ S_{mult(ℓ)}; letter ℓ owns the
value interval base(ℓ)..base(ℓ)+mult(ℓ)−1 and its j-th occurrence (left→right) gets value base(ℓ)+ρ_ℓ(j).
τ ∈ S_k embeds ⇔ ∃ weakly increasing ψ:[k]→[m] whose fibres (intervals of τ-values) are realised by chosen
occurrences of ℓ carrying the fibre's pattern. Monotone rows = EV/tie-broken words; arbitrary rows = anything
(NB: every σ ∈ S_n with every interval partition of its values is "row-structured" — the family is only smaller
than S_n if the row patterns are restricted; see §2).

Tools (this dir): `fibres.c` (per-pattern embedding counts, and how many embeddings use only monotone fibres,
for a given σ and value partition), `rows.py` (DP over interval partitions + hard-pattern fibre analysis; output in
`runs/rows_analysis.txt`), `sa4.c` (SA over row-structured perms; modes -R 0 all-dec rows / 1 monotone rows /
2 free rows / 3 monotone + at most -Q non-monotone rows; -P B identical blocks), `wild.c` ("wildcard rows":
each fibre may carry ANY pattern — the union over all row-pattern choices, an upper bound on the coverage of every
row-structured perm with that word; SA over words, EXH=1 exhaustive over ρ for ρ^B, MISS=1 lists missing patterns),
`check.c`, `sp.c` (copied from w2/w1 as independent checkers).

**Tool bug found (matters for anyone reusing sp.c):** sp.c's incremental pair-update `dfs_pair` (subsets containing
BOTH swapped positions) is only correct for adjacent-position swaps and adjacent-value swaps (there a bijection
handles the subsets containing one of the two positions). For a general transposition it is wrong (`swaptest.c`:
184/300 random swaps at n=12,k=5 give wrong counts). sp.c itself only uses those two move types (+ full recount for
"big" moves), so the w1 results are unaffected; sa4 uses the incremental update only for those two move types and a
full recount otherwise (verified with -rep 1: 0 mismatches in all modes).

## 1. Row-structure of the record witnesses (Task 1)

Witnesses (verbatim, from work/w1-search/results.md; all re-verified here with check.c / sp.c -c, 0 missing):
- sp7a (23): 7 20 13 10 2 18 23 4 12 16 8 5 19 15 1 9 22 14 6 17 11 3 21
- sp7b (23): 7 18 12 2 15 23 6 19 13 4 8 11 22 17 3 20 10 5 14 1 21 9 16
- sp7c (23): 10 16 2 22 6 11 19 15 5 21 12 1 9 18 4 13 23 7 17 3 14 20 8
- sp8_30 (30): 13 4 25 18 8 30 12 22 1 28 19 10 6 14 24 27 3 16 21 11 5 20 29 15 7 23 2 17 26 9
- Arnarson 17 (k=6): 6 14 10 2 13 17 5 8 3 12 9 16 1 7 11 4 15

For each witness and each number of rows m, DP over all partitions of the values into m intervals of size ≤ 4
minimising the number of non-monotone rows (rows.py). "need-nonmono" = number of k-patterns *every* embedding of
which uses at least one non-monotone fibre (fibres.c, exhaustive over all C(n,k) subsets).

| witness | k | n | min m all-monotone | m → min #non-monotone rows | at m=k+1: row patterns | need-nonmono at m=k+1 / k+2 / k+3 |
|---|---|---|---|---|---|---|
| Arnarson | 6 | 17 | 7 = k+1 | 5:2, 6:1, 7:0 | 1,12,321,21,21,4321,321 (all monotone) | 0 / 0 / 0 |
| sp7a | 7 | 23 | 10 | 6:5, 7:3, 8:2, 9:1, 10:0 | 1,12,123,123,**4132**,321,**4231**,321 | 22 / 8 / 0 |
| sp7b | 7 | 23 | 10 | 6:4, 7:3, 8:2, 9:1, 10:0 | 21,21,21,12,4321,**3124**,**2314**,321 | 4 / 1 / 0 |
| sp7c | 7 | 23 | 9 | 6:5, 7:2, 8:1, 9:0 | 21,321,12,21,1234,321,321,**3241** | 0 / 0 / 0 |
| sp8_30 | 8 | 30 | 13 | 8:6, 9:4, 10:3, 11:2, 12:1, 13:0 | **4132,4213,4231**,123,**3412**,321,321,321,21 | 9 / 8 / 2 |

Findings:
- With m = k+1 rows the records need only 1–2 (k=7) resp. 4 (k=8) non-monotone rows; the non-monotone row patterns
  that occur are 4132, 4231, 3124, 2314, 3241, 4213, 3412 — all "one element displaced from monotone", never
  alternating-like (2143, 1324 do not occur).
- The patterns that *force* a non-monotone fibre are few (22/5040, 4/5040, 0/5040; 9/40320) and are irregular
  ones (5312467, 1567243, 6145732, 54238761, 67283451, …), NOT the hard families.
- **All hard patterns (identity, decreasing, alternating up-down/down-up, layered 21 43 65…, 321 654…, (k−1,1),
  (1,k−1)) embed with monotone fibres only in every witness and every partition tested** (rows.py, "needs nonmono
  fibre: False" throughout). Their fibre multisets are size-2/3 monotone pieces (e.g. alternating 1325476 in sp7a:
  23 embeddings, fibres {12,21},{21,21},{21},…).
- Conclusion: the optima at k=7,8 do *not* use non-monotone rows for the hard patterns; they use k+2..k+5 monotone
  rows with mixed directions (as w2 §6.3 found), and a couple of "nearly monotone" rows only to mop up a handful of
  irregular patterns. sp7c is a pure mixed-direction tie-broken word over 9 letters with no non-monotone row at all.

## 2. Search over row-structured permutations (Task 2)

Design note. Free row patterns of unrestricted size = S_n, so the honest intermediate spaces are
 (a) -R 3 -Q q: tie-broken word over [m] (monotone rows, mixed directions) + at most q non-monotone rows;
 (b) -R 1: monotone rows only (mixed directions), m > k+1;
 (c) -P B: identical blocks ρ^B with free row patterns (rows of size B) — the covering family of w2 §2/§6.
sa4 energy = weighted #missing + 0.3·#singletons (as sp.c), incremental for adjacent moves, full recount otherwise.

Results at the end of the time box (runs still going are marked ⟳; files runs/*.err hold every improvement with the
full state, runs/*.out the final line):

k = 8, n = 29 (unstructured SA in w1: best 12 missing):
- m=10, R=2 free rows (= S_n with row-moves), seed 803: **13 missing** at it≈14k ⟳
  word 6 3 10 5 7 1 5 8 5 6 2 7 10 6 3 5 7 3 7 1 5 9 3 6 4 10 7 6 2, rows 21 12 3421 1 25134 35241 34512 1 1 132,
  perm 17 7 27 11 22 2 14 25 10 19 3 23 29 16 8 12 24 6 20 1 13 26 5 18 9 28 21 15 4
- m=10, R=3 Q=2: 25 missing ⟳; m=11, R=3 Q=3: 28 missing ⟳; m=11, R=1 (monotone mixed): 32 missing ⟳.
- wildcard upper bound (wild.c SA over words, m=10 rows, multiplicities 3/2): **40315/40320** after 26 (slow)
  iterations ⟳; the 5 patterns missing even with wildcard rows: 56783124, 56783214, 56784123, 73218645, 75324186
  (word 5 3 6 10 1 3 9 5 2 4 5 9 8 10 1 8 4 2 6 6 4 7 9 1 3 7 2 7 8). m=12 rows: 40193 ⟳.
  => no evidence that 10–11 rows with arbitrary patterns reach n=29; the missing patterns are "two long consecutive
  runs" types, exactly the bottleneck seen in w1/w2.
k = 9, n = 38 (target: any 9-superpattern of length ≤ 38 would be a record; EV gives 41):
- m=13, R=2: 17 missing at it 623 ⟳ (each iteration ≈ 1 s; state in runs/k9n38_m13_R2_s902.err); m=12, R=3 Q=3: 65 missing ⟳;
  wildcard m=13 ⟳ (no output yet).
- **No new record.** Nothing to verify.
Identical blocks ρ^B with free rows (covering family):
- k=7, m=8, B=3 (n=24): SA best 5039/5040 (missing 7654321), and the wildcard EXHAUSTIVE search over all ρ ∈ S_8 is at
  5039 after 295 ρ's ⟳ — the theorem in §3 says 5040 is impossible for any rows, so this run is a check only.
- k=6, m=8, B=2 (16): free rows 704/720 (SA), wildcard exhaustive best 716 so far ⟳ (16 is impossible anyway, Pantone).
- k=8 m=9,10 B=3 and k=9 m=12 B=3: killed after the theorem below showed them impossible (best before kill: 357, 16,
  277 missing).

## 3. Theory: covering formulation with non-monotone fibres (Task 3)

Identical-block family σ = ρ^B, ρ ∈ S_m, m = k+d, arbitrary row patterns r_ℓ ∈ S_B. τ embeds iff there are
ψ:[k]→[m] weakly increasing (fibres = value intervals) and a block assignment b:[k]→[B], weakly increasing along the
positions of τ, with (i) inside one block the assigned letters are distinct and in ρ-order, (ii) for every letter ℓ the
fibre positions i_1<…<i_t get blocks b_{i_1}<…<b_{i_t} and pattern(τ on the fibre) = pattern(r_ℓ(b_{i_1}),…,r_ℓ(b_{i_t})).
Dropping (ii) ("wildcard rows") the minimal number of blocks is 1 + wdes_ρ(ψ(τ)), where wdes counts consecutive
positions of the word ψ(τ) whose letters are equal or in ρ-descending order (a repeated letter costs a block exactly like
a descent — this is the whole point). Hence for every row-pattern choice
    cost(τ) ≥ 1 + min_ψ wdes_ρ(ψ(τ)),  and  S_k = ⋃_ψ { τ : wdes_ρ(ψ(τ)) ≤ B−1 } is necessary.
Compared with w2 §2 (S_k = Pat_k(ρ)·D_B) the new freedom is the exponentially many non-injective ψ, each paying one
block per merged value; non-monotone rows are what makes non-decreasing fibres admissible.

**Theorem (id/dec trade-off, any row patterns).** For S ⊆ [m] let asc(S) = #{consecutive-in-S pairs a<b with a before b
in ρ}, desc(S) likewise. Then cost(id) = k − max_S asc(S) and cost(dec) = k − max_S desc(S) (wildcard rows; for real
rows ≥). Inserting a letter into S never decreases asc(S) or desc(S) (if a<x<b and a before b, then not both (a,x),(x,b)
can be descents, etc.), so both maxima are attained at S=[m]:  I(ρ)=asc([m]), D(ρ)=desc([m]), I+D = m−1.
(Verified exhaustively for m ≤ 9: I+D = m−1 for every ρ, tradeoff.py.) Therefore
    max(cost(id), cost(dec)) ≥ k − (m−1)/2 = (k − d + 1)/2,   i.e.   B ≥ ⌈(k−d+1)/2⌉,  n = Bm ≥ (k−d+1)(k+d)/2.
Consequences: k=7,m=8 ⇒ B≥4 (so 24 = 3 blocks is impossible with ANY rows — matches rhoB2's 5039 and the wildcard
exhaustive); k=8,m=9 or 10 ⇒ B≥4 (27 and 30 impossible; sa3's 40316 at 30 used three *different* blocks); k=9,m=12 ⇒
B≥4 (36 impossible), m=13 ⇒ B≥3 (39 > 38, useless). Asymptotically, with alphabet m=(1+o(1))k the identical-block
family with any row patterns needs (1/2−o(1))k² — the identity and the decreasing permutation alone force it, and the
non-monotone-row mechanism does nothing for them (their fibres are monotone anyway, and merges cost a block each).
To beat 1/2 inside this family one needs d = Θ(k): d = δk gives only n ≥ (1−δ²)k²/2 from this argument (e.g. 3k²/8 at
m=1.5k), which is outside Hunter's proven (1+o(1))k-alphabet regime — so the family is *not* excluded at alphabet
(1+δ)k, but the gain would have to come from the alternating/layered side, not from rows.

Alternating and layered permutations in this formulation: with fibres of size 2 and decreasing rows, alt = 1 3 2 5 4 …
has ψ(alt) = 1 2 2 3 3 4 4 … (wdes = k/2) and layered 21 43 65 … has ψ = 1 1 2 2 3 3 … (wdes = k/2); with injective ψ
their cost is 1 + des_ρ(ψ(τ)) and they need ρ-descents on the consecutive-letter pairs (2j,2j+1) resp. (2j−1,2j) and
ρ-ascents on the distance-3 pairs — i.e. both want the *same* half of the consecutive pairs to be descents that id wants
to be ascents. Non-monotone fibres (2143, 1324, 213, 132 pieces of alt/layered) do not reduce wdes, they only relabel;
so within identical blocks the covering radius does not drop for these families either (numerically: the k=7 SA with
free rows reached exactly the dec-ties value 5039, and the wildcard exhaustive is at 5039).

For *different* blocks ρ_1…ρ_B (the family that actually contains the small-k records) the id/dec argument collapses
to Σ_j LIS(ρ_j) ≥ k, Σ_j LDS(ρ_j) ≥ k (trivially satisfiable), and I have no bound; the wildcard SA (§2) is the numerical
probe: at k=8, n=29 with 10 or 12 rows it has not reached universality (40315, 40193) within the time box.

## 4. Honest status of the asymptotic question
- Non-monotone rows are NOT what the k=7,8 optima use for the hard patterns (§1), and they provably cannot help the
  identical-block covering family at alphabet (1+o(1))k (§3 theorem: id and dec alone cost (k−d+1)/2 blocks whatever
  the rows are). The mechanism survives only in (i) non-identical-block words and (ii) alphabets (1+δ)k with δ = Θ(1),
  where nothing here rules it out and nothing here supports it.
- Searches: no k-superpattern of length 29 (k=8) or ≤ 38 (k=9) found; row-structured spaces did not beat the plain SA
  (13 vs 12 missing at n=29). k=9, n=38 stands at 17 missing (early; ⟳).

## 5. Background processes still running (all write to runs/)
sa4: k8n29_m10_Q2_s801, k8n29_m11_Q3_s802, k8n29_m10_R2_s803, k8n29_m11_R1_s804, k9n38_m12_Q3_s901, k9n38_m13_R2_s902
     (each prints every improvement to .err with word/rows/perm; on success prints FOUND … to .out — verify with
      `./check 8 29 <perm>` and `./sp -k 8 -c -p "<perm>"`).
wild: wild_k8n29_m10, wild_k8n29_m12, wild_k9n38_m13 (SA over words, wildcard rows), wild_k7_P3m8_EXH, wild_k6_P2m8_EXH
     (exhaustive over ρ; expected to end at 5039 resp. ≤ 719 by the theorem/Pantone).
