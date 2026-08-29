# W2 — constructive sub-1/2 superpatterns: running log

Started 2026-08-29. Goal: explicit k-superpatterns of length (c+o(1))k², c < 1/2.

Tools in this directory:
- `check.c` — brute-force k-pattern counter for words over [m] (enumerates k-subsets of positions with distinct letters, pruned). Verified: Arnarson 17-perm → 720/720; Miller 135642135642135 (k=5) → 120/120; z_5 = 1354213542135 without tie-breaking → 68/120 (ties matter).
- `sa.c` — simulated annealing over words σ ∈ [m]^n maximising #k-patterns contained.
- `eulerian_bound.py` — counting bound for ρ^B family.

## 0. Literature digest (what the zigzag proof really uses)

Miller/EV score: s(p) = (#runs of the infinite zigzag needed to contain p literally) − |p|.
For words without immediate repetition, s(p) + s(p⁺¹) = 1 exactly. Consequence: **every** τ ∈ S_k costs
exactly k or k+1 runs; there is zero slack. Runs have length (k+1)/2, so length ≈ k²/2 for all τ alike.
The shift p ↦ p⁺¹ is the only realization freedom with alphabet [k+1] and the two shifts are perfectly
anti-correlated (sum of scores = 1).

Hunter (2108.05474): for alphabet r = (1+o(1))k, need (1/2−o(1))k². Mechanism: Remark 1.2,
#patterns(σ) ≤ C(r,k)·F(k,n), and F(k,n)/k! ≤ e^{−c(ε)k} for n ≤ (1/2−ε)k², c(ε) ≈ ε⁴/33.
Hunter admits his method cannot show f(k;1.0001k) ≥ k²/4, and announces 15/32 (unpublished, no trace
on the web as of 2026-08-29; searched).

## 1. Reformulation: collapses / literal containment

For σ ∈ [m]^n and Y ⊂ [m], |Y| = k, let σ|_Y be σ restricted to letters in Y, relabelled to [k]
("collapse"). Then σ contains τ ∈ S_k as a pattern ⇔ τ is a **literal** subsequence of some collapse σ|_Y.

Two immediate NEGATIVE results (rigorous):

**(N1) Copy models are dead.** Any construction in which each τ-value v is assigned a fixed candidate set
C_v ⊂ [m] of letters (with C_1 < C_2 < … < C_k, e.g. "odd copy / even copy" of each value in [2k])
is equivalent to a word W over [k] (replace each letter of C_v by v) containing every τ ∈ S_k literally.
By Kleitman–Kwiatkowski, |W| ≥ k² − O(k^{7/4+ε}). So the realization freedom must be *global*
(the image of v must depend on the whole of τ), as in Miller's shift.

**(N2) Polynomially many distinct collapses are dead.** If the words {σ|_Y} take only N distinct values,
then N·F(k,n) ≥ k!, so with n ≤ (1/2−ε)k² we need N ≥ e^{c(ε)k}. Any construction whose realization
freedom is a "threshold" (split values into low/high at a cut point), a bounded number of shifts, etc.,
cannot beat 1/2. Need exponentially many *genuinely different* collapses, each of which must cover an
exponentially small (but non-negligible) fraction of S_k, and they must cover different τ's.

## 2. Block constructions ρ^B — covering formulation

σ = ρ^B (B copies of a permutation ρ of [m]). Greedy embedding shows: σ contains τ ⇔ ∃ k-pattern π of ρ
(π = pattern of ρ|_Y for some Y) with des(π⁻¹τ) ≤ B−1. I.e.

    S_k = Pat_k(ρ) · D_B,   D_B = {permutations with < B descents}.

So we need Pat_k(ρ) ⊂ S_k to be a *covering code* of covering radius < B for the (left-invariant) distance
d(π,τ) = des(π⁻¹τ). Miller = ρ is the zigzag pair 135…642 on [k+1], Pat_k(ρ) = 2 essential patterns,
and des(π₀⁻¹τ) + des(π₁⁻¹τ) ≈ k−1 (score identity in descent language).

Counting bound (eulerian_bound.py, k=400): C(m,k)·|D_B| ≥ k! gives only the trivial-type numbers
(length coefficient ≥ 0.31 at m=1.1k, ≥ 0.19 at m=2k, → 0.16 ≈ 1/e² region). Uninformative; the
obstruction (if any) is structural.

## 3. Generalised zigzags — all dead against alternating permutations (rigorous)

Any σ made of monotone runs over residue classes (c classes, any directions, any alphabet ck):
a block of c runs (length ck) hosts at most c−1 alternating monotone runs of τ, so the alternating
permutation 1 3 2 5 4 … needs ≥ k/(c−1)·… ≈ k/c blocks → length ≥ k². With alphabet (1+δ)k and
parity-flip freedom (d = δk flip points from the deleted letters): cost(τ) = (k−1) − max over ≤ d+1
segments of alternating segment sums of h(v) = (−1)^v g(v)/2 where g(v) ∈ {−2,0,2} records whether the
position of value v is a double ascent / extremum / double descent. For alternating τ, h ≡ 0: no gain, ever.
Mod-3 zigzags (idea (d)): expected cost per letter = q/2 runs of length k/q → k²/2 again, and worst case
is worse. So ideas (a) and (d) as literally stated FAIL; the reason is that "run-change" costs are tied to
extrema of τ, and alternating τ has k−2 extrema.

Also computed: zigzag over [2k] with free parity labels: runs needed = 1 + #extrema(τ) (exact, via the
identity cost = (k−1) − ½Σ_j x_j(a_{j−1}+a_j)); great for identity (1 run) but k² for alternating.

## 4. Merged halves (two zigzags, low/high values, runs interleaved)

Cost accounting in "pair units": every transition averages 1 pair; interleaved τ (a b a b …) costs
(k−1)/2 + min(X, k−1−X) where X = #parity mismatches — the shifts flip all transitions at once, so
worst case is still k−1 pairs = k²/2. This is exactly Chase's DFA (Hunter §5.2.2): gains only k^{3/2}.

## 5. Experiments (see runs/)

### 5.1 Calibration of tools
- `zig.py` reproduces EV: ζ_k universal for k=3..8 with |ζ_k| = 5, 9, 13, 19, 25, 33. ✔
- **ζ_k is irredundant** (trim.py): for k=5,6,7 no single position of ζ_k can be deleted (universality lost
  for each of the 13/19/25 deletions; greedy multi-deletion also removes nothing). So "trim the zigzag"
  is not available as-is; EV's permutation is locally minimal even though sp(6)=17 < 19.
- SA on random words: k=6, n=17: m=8 → 644/720, m=10 → 695, m=12 → 708, m=17 → 719/720 (200k iters).
  SA cannot find the (rare) 17-superpatterns from random starts; it is a weak tool for exact objects.
- ζ_7 minus its least-harmful single letter (position 11) leaves 5031/5040 (9 patterns lost).

### 5.2 Exhaustive ρ^B searches (rhoB.c)
- k=6, ρ ∈ S_7, ρ²   (length 14): best 290/720  (ρ = 3 5 1 7 4 2 6)
- k=6, ρ ∈ S_8, ρ²   (length 16): best 562/720  (ρ = 3 7 5 1 8 4 2 6)
- k=7, ρ ∈ S_8, ρ³   (length 24): best 4245/5040 (all 8!/2 ρ up to reverse-complement)
  Best ρ's are Miller-pair-like ("1 7 5 3 8 2 4 6": odds down, evens up). The identical-block family with
  m = k+1 is far from universal at length < (k²+1)/2; counting bound was vacuous, the obstruction is real.
- SA over general words, k=7, n=24: m=8 → 4141, m=9 → 4724, m=10 → 4655 (100k iters). Not close.

## 6. The tie-break ("EV") family — where the small-k gains actually live

**Observation (rigorous, computed):** Arnarson's 17-permutation is exactly the decreasing-tie-break of
the word  W = 3 6 5 1 6 7 3 4 2 6 5 7 1 4 6 3 7  over [7] = [k+1]: its inverse
13 4 9 16 7 1 14 8 11 3 15 10 5 2 17 12 6 splits into 7 decreasing chains of consecutive values
{1,2},{3},{4,5,6},{7,8},{9,10},{11..14},{15,16,17}. Letter multiplicities 2,1,3,2,2,4,3 (non-uniform);
as periods: 3 6 5 1 6 7 | 3 4 2 6 5 7 | 1 4 6 3 7 — three near-permutations of [7] (EV's z_6 is
135642 ×3 = 18, +1 max). So the record object is NOT a zigzag but is in the EV family
"word over [k+1] + decreasing ties". (compress.py, arnarson.py)

Framework: for a word w over [m] with per-letter tie direction, w̃ ⊇ τ ⇔ ∃ ψ:[k]→[m] weakly increasing
whose fibres are intervals of values forming monotone (matching direction) subsequences of τ, with
ψ(τ) a literal subsequence of w. For all-decreasing ties, τ can use as few as k − des(τ⁻¹) letters
(maximal decreasing runs of τ⁻¹), ≈ k/2 for random τ, but the identity needs k distinct letters.

**Zigzag + merges give nothing** (rigorous): in the infinite zigzag runs(p)+runs(p⁺¹) = 2k + 2·rep(p)
for any p with rep immediate repetitions; merges reduce the alphabet used but never the run count.

### 6.1 ρ^B with decreasing ties (rhoB2.c, exhaustive over ρ ∈ S_m up to reverse-complement)
- k=5: ρ = 3 5 1 4 2 (S_5), ρ³ (15): 120/120; ρ ∈ S_6, ρ² (12): best 117/120.
- k=6: ρ ∈ S_7, ρ² (14): 599/720; ρ ∈ S_8, ρ² (16): 697/720 (16 impossible, Pantone);
  **ρ = 1 4 8 5 7 3 9 2 6 ∈ S_9, ρ² (18): 720/720** — a 6-superpattern of length 18 = k²/2 of the form ρρ.
- k=7: ρ ∈ S_8, ρ³ (24 = (k²−1)/2 < 25 = EV): best **5039/5040**, e.g. ρ = 1 3 7 5 4 2 6 8,
  1 3 7 5 8 4 2 6, 3 7 5 1 4 2 6 8. The unique missing pattern is 7654321 (exactly EV's even-n
  phenomenon: LDS(ρ)+B−1 = 4+2 = 6 < 7). All 256 tie-direction masks, all single letter moves
  (delete+insert), and full 2-opt polish of the 24-letter word stay at 5039. (fix24.py, polish.c)
  NOTE: even if a 24 exists, (k+1)(k−1)/2 blocks-structure is still (k²−1)/2 — no constant gain;
  a constant gain needs B ≤ (1/2−ε)k blocks of length k+O(1), i.e. > 2+ε letters of every τ per block.

### 6.2 NEW RESULT: sp(7) ≤ 24  (previous best upper bound 25 = (k²+1)/2)
sa3.c (SA over three *different* permutation blocks of [8], decreasing ties) found, verified with two
independent checkers (check.c on the tie-broken permutation; missing.py pure-python subset enumeration):

  word  3 7 1 5 2 8 4 6 | 2 4 8 1 5 3 6 7 | 2 4 7 5 1 8 3 6   (over [8], decreasing ties)
  perm  9 21 3 15 6 24 12 18 5 11 23 2 14 8 17 20 4 10 19 13 1 22 7 16      (5040/5040)

  word  3 6 8 1 2 4 5 7 | 3 1 7 5 6 2 4 8 | 2 7 4 1 5 8 6 3
  perm  9 18 24 3 6 12 15 21 8 2 20 14 17 5 11 23 4 19 10 1 13 22 16 7      (5040/5040)

Structure: 3 blocks, each a permutation of [k+1]; every τ ∈ S_7 splits into ≤ 3 pieces after choosing a
shift/merge realization. Identical blocks (ρ³) cannot do it (exhaustive: max 5039, missing 7654321);
the three blocks must differ. Length 24 = (k²−1)/2 — so this is an O(1) improvement, not a constant-factor one.

### 6.3 Coordinator's witnesses (sp(7) ≤ 23, sp(8) ≤ 30/31): are they tie-broken small-alphabet words?
structure.py: for each witness and all 8 symmetries (rev/comp/inverse), minimal number of "rows"
(intervals of consecutive values whose positions are monotone) — this is the exact minimum alphabet of any
monotone-tie-break word representation (greedy maximal monotone segments of the inverse is optimal):
  sp7a (23): 10 letters (mixed dirs), 11 all-dec.  sp7b: 10 / 11.  sp7c: 9 / 11.     [k+1 = 8]
  sp8_30:   13 letters (comp, mixed), 14 all-dec.  sp8_31: 13 / 15.                    [k+1 = 9]
  Arnarson 17: 7 = k+1 (all-dec).  my 24: 8 = k+1 (all-dec, 3 blocks of 8).
Answer: NO. The 23's and the 30 are genuinely "wider" permutations (≈ k+2 … k+5 rows, mixed tie
directions, no clean block structure: greedy distinct-letter blocks have sizes like [8,5,4,6] / [6,9,6,9]).
So "B blocks over [k+1] with ties, B ≈ k/2 − c" is NOT what the record objects at k=7,8 look like; the
tie-break family is a convenient *search space* (it found 24 quickly) but the true optima leave it.
All witnesses verified 5040/5040 resp. 40320/40320 with check.c.

## 7. Summary of the asymptotic question (state at end of session; results of k=8,9 runs appended below)

What is PROVED here (elementary, in this log):
 (P1) Copy models / fixed candidate sets reduce to Kleitman–Kwiatkowski ⇒ ≥ k² − o(k²).      [§1 N1]
 (P2) Constructions with poly(k) distinct collapses ⇒ ≥ (1/2 − o(1))k² via Hunter's F(k,n).   [§1 N2]
 (P3) Any monotone-run/residue-class zigzag over any alphabet, with or without merges, costs ≥ k−1
      run-changes on the alternating permutation, and runs(p)+runs(p⁺¹) = 2k+2·rep kills merges in
      zigzags; mod-q zigzags cost ≥ 2k²/3 on the decreasing permutation for q ≥ 3.              [§3, §6]
 (P4) Low/high merged zigzags reproduce Chase's DFA: at most k^{3/2} gain.                       [§4]
 (P5) ρ^B with dec ties: S_k = Pat_k(ρ)·D_B covering formulation; identical blocks fail at k=7, n=24
      solely because of the decreasing permutation (LDS(ρ)+B−1 < k).                              [§6.1]
What is OBSERVED:
 (O1) sp(7) ≤ 24 via 3 different blocks of [8] with dec ties (then ≤ 23 by the search workstream,
      not in this family); sp(6)=17 (Arnarson) is a 3-near-block word over [7] with dec ties.
 (O2) Small-k optima below (k²+1)/2: 17, 23, 30 for k = 6,7,8 — i.e. k²/2 − 1, k²/2 − 1.5, k²/2 − 2.
      This is consistent with (k² − c·k)/2 or with (1/2 − ε)k²; k ≤ 8 cannot distinguish.
What is CONJECTURED (by me, weakly): every "block/run" family whose realization freedom is shifts +
monotone-row merges has max-cost (1/2 − o(1))k²; a genuine constant-factor gain needs either exponentially
many *non-monotone-row* realizations (rows with up-down internal patterns) or a random-like ingredient.
Idea (a),(d) are refuted; (b) grid families reduce to blocks (not separately tested beyond ρ^B);
(c) done: Arnarson = tie-broken 3-block word.

### 6.4 k=8 structured family (sa3, dec ties)
- B=4 blocks of [9] (length 36 > 33): found 40320/40320 within ~100 SA steps, e.g.
  7 3 1 4 9 5 8 6 2 | 1 2 7 5 3 4 8 6 9 | 3 7 9 1 2 8 5 4 6 | 2 9 1 6 5 3 7 8 4  (verified with check.c).
  Uninformative (too long); the real test is B=3: 3×9 = 27 and 3×10 = 30 — results below.
- B=3 blocks of [9] (length 27): best 39947 and 39956 / 40320 after 6000 SA steps (two seeds). Fails.
  (Zigzag-like blocks again: 2 4 8 6 1 3 5 7 9 | 4 1 8 6 3 5 7 2 9 | 1 4 7 5 2 8 6 9 3.)
- B=3 blocks of [10] (length 30 = the unstructured record): seed 1 → **40316/40320**,
  word 2 5 9 7 1 3 8 6 4 10 | 2 5 7 9 1 4 8 3 10 6 | 2 5 9 3 6 8 1 10 7 4 (dec ties).
  Missing exactly: 54367812, 78123456, 78123546, 87654132 — all "near-monotone" patterns with long runs of
  consecutive values (78123456 is a rotation of the identity). This is the predicted bottleneck of
  block families: such τ have no merges (few distant inverse-descents), only the k+2 shifts, and need blocks
  containing long *consecutive-letter* increasing subsequences, which fight the zigzag-like structure the
  other patterns want. 1-opt/2-opt polish: see runs/polish_k8_30.txt.
- B=3 blocks of [10], seed 2 → 40315/40320. So the structured family comes within 4–5 patterns of the
  unstructured length-30 record but (in 4000 SA steps) does not reach it. Length 30 = k²/2 − 2.

### 6.5 k=9 structured family (still running at end of session; outputs → runs/sa3_k9_*.txt/.err)
- 3 blocks of [12] (36 = k²/2 − 4.5): 362377/362880 after 176 steps (503 missing) — improving slowly.
- 4 blocks of [10] (40 = k²/2 − 0.5, vs EV 41): 362818/362880 after ~50 steps (62 missing) — likely to
  complete; would give sp(9) ≤ 40 (an O(1) improvement only).
- 3 blocks of [10]/[11] (30/33): 335516 / 357978 — hopeless.
Still running: polish of the length-30 k=8 word (runs/polish_k8_30.txt), sa3 k=9 (m=10,B=4; m=11,12,B=3).

## 8. Bottom line
No sub-1/2 construction found; several natural families are PROVED to be stuck at ≥ 1/2 (§1,§3,§4,§6),
and the small-k record objects (17, 23, 30 for k=6,7,8, i.e. k²/2 − 1, −1.5, −2) are consistent with
k²/2 − O(k) as much as with (1/2−ε)k². New explicit results from this workstream: sp(7) ≤ 24 via a
3-block tie-broken word over [8] (superseded by the search workstream's 23); a 6-superpattern of length 18
of the form ρρ; the structural identification of Arnarson's 17 as a decreasing-tie-break of a word over [7];
exact "minimal row alphabet" statistics for all known record witnesses. The best candidate mechanism for a
constant-factor gain that is NOT excluded by the arguments here: rows (letter classes) whose internal
tie-break pattern is non-monotone (so fibres can be arbitrary small patterns), giving exponentially many
non-shift realizations — untested.

### 6.5 update (later snapshot; searches still running)
- k=9, 4 blocks of [10] (length 40): 362868/362880 (seed 1, step 221) and 362863 (seed 2, step 173) — 12/17
  patterns missing, still climbing; a completion gives sp(9) ≤ 40 (vs EV 41).
- k=9, 3 blocks of [12] (36): 362715/362880 at step 648 (165 missing), still climbing slowly.
- k=9, 3 blocks of [11] (33): finished at 359959/362880 — fails.
- k=8 length-30 polish: 2-opt still running, no improvement over 40316 yet.
- k=9, 3 blocks of [12] (36): FINISHED at 362715/362880 (165 missing) — fails in 800 steps.
  word 2 7 11 5 9 1 3 10 6 4 8 12 | 2 10 6 1 9 3 7 11 5 8 4 12 | 2 9 7 3 11 5 8 1 12 6 10 4.
- k=9, 4 blocks of [10] (40): 362870/362880 at step 263 (10 missing), still running.
- k=9, 4 blocks of [10] (40): original runs reached 362873 (7 missing) / 362863 before being killed with
  the session's watcher (sa3 printed nothing before exit, best words lost). Relaunched (macOS has no setsid; first relaunch failed, redone with nohup) as
  sa3v (dumps best word on every improvement): runs/sa3_k9_m10_B4_s3.err, _s4.err.
  (detached relaunches s3/s4 were killed again with the session watchers; final relaunch as a managed
  background task: runs/sa3_k9_m10_B4_s5.{txt,err}, _s6.{txt,err} — best word dumped on each improvement.)
