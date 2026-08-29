# W18 — lag lemma (log)

Date: 2026-08-29.  Directory: work/w18-lag/.  Files: proof.md (PROVED statements only), joint.py
(exact joint-failure calculator), check_mc.py, exp1_pairs.py … exp5_three.py, out_*.txt.
Time-boxed ~2.5 h.  PROVED = in proof.md; everything else here is numerics or heuristics.

## 0. Summary (honest)

The W18 goal was a LAG LEMMA: "a shift Δ all of whose chains have element lag λ ≫ √k·polylog(k)
is harmless, Pr(E_t ∩ E_{t+Δ}) ≤ Pr(E_t)² e^{o(k)}", from which O(√k polylog) harmful shifts per π,
ℓ ≈ ln k mutually harmless shifts, and n = O(k²) for all π would follow.

**This lemma is false, and the numerics that suggested it (W15 exp3, "harmful only for λ ≲ 3√k")
were measuring the wrong regime.**  Proved (proof.md Theorems 4–5, Corollary 6): for the tilted grid
and every shift Δ = e ∈ [1, h/4] ∪ [3h/4, h) — element lags er = r, 2r, …, k/4, all ≥ √k —
   Pr(E_0 ∩ E_Δ) ≥ Pr(E_0) · e^{−Λ ln(12C)},   Λ = 2·lag  (positive lag) or lag + e + 1 (negative lag),
so Pr(E_0 ∩ E_Δ)/Pr(E_0)² ≥ e^{c_C k} for C ≥ 8.  The loss caused by a second thread is LINEAR in the
lag (rate ≈ ln C numerically, ≤ 2 ln(12C) rigorously), not Gaussian e^{−λ²/k}; the second thread at
lag λ = εk is worth at most a fraction ≈ 2ε ln(12C)/(C ln 2) of an independent thread.  The mechanism
(§1) is *coalescence*: the follower has to hit a leader interval once, after which it moves in
lock-step with the leader for the whole translation segment of the chain (proof.md Lemmas 1–2); on
the tilted grid that segment is the whole chain.  Hitting costs the leader a fast prefix of 2λ
elements (e^{−2λ·KL}) — cheap — and nothing else.

Consequences for the programme (§4–5): every shift of the tilted grid with lag ≤ k/4 is harmful, the
number of harmless shifts is not O(√k polylog) but 0 (for C ≥ 8, all Δ = e < h are covered, and the
numerics cover all Δ ≤ k), and the exponent obtainable with ℓ threads on the tilted grid is
(heuristically, §5) at most Ck ln 2 + O(k ln C · log ℓ): for ℓ = polylog(k) this is O(k ln C ln ln k),
far below the (1/32) k ln k needed to union-bound over the family 𝓕 of [W15].  The thread method with
polylogarithmically many threads at m = Ck therefore cannot prove n = O(k²) for 𝓕, whatever
lag/overlap lemma one proves; the barrier is the same k log log k as He–Kwan's.

A second, unexpected finding (§3.4): for a *random* π at C = 8 the exact ratio Pr(E_0 ∩ E_Δ)/Pr(E_0)²
is e^{140±10} (k = 100) for EVERY Δ — the second thread is worth only ≈ 46% of an independent one.
This is not the lag mechanism (random π has no long translation segments) but the mechanism of
[W9] log §4 (the failing leader concentrates its zeros on a short chain, the follower rides the
long intervals): it is exactly what the global events 𝒜/𝓑 of [W9]/[W13] remove.  So per-π
"independence of threads" never holds; a global event is indispensable, and the lag mechanism is an
*additional* loss that the global events do not remove (it uses no long runs).

## 1. The mechanism, and why W15's √k was an artefact

Two threads t (leader) and t + Δ (follower) share cells only in rows π(a) + t = π(b(a)) + t + Δ.
The prompt's picture — "the follower's interval must overlap the leader's window, offset walk of
scale √k, local time" — is right for the *first* shared cell, but wrong afterwards: proof.md Lemma 1
shows that as soon as the follower reads one cell of I_a it reads the rest of I_a including the
leader's one, so Y'_{b(a)} = Y_a and X'_{b(a)+1} = X_{a+1}: the follower is now *exactly* aligned
with the leader.  If b(a+1) = b(a)+1 (translation segment) it reads all of I_{a+1}, etc. (Lemma 2).
For the tilted grid with Δ = e < h the chain {a ≥ er} is one translation segment (b(a) = a − er), so
one entry = a ride to the end of the matrix, and the follower fails whenever the leader does.

The entry is cheap.  The follower at element a − λ must be at column ≈ X_a.  In the *unconditioned*
regime (W15 exp3, m = 4k, threads rarely fail) both walks have speed 2 and the follower is behind by
2λ columns; catching up is a Gaussian fluctuation, e^{−λ²/(2a)}, negligible for λ ≫ √k — that is
the "3√k" of W15.  But the relevant regime is E_0 (the leader fails, speed C).  There the cheapest
entry is: leader fast (runs 0) for its first 2λ elements, follower at natural speed for λ elements
(runs 1), meet at column 2λ — cost 2^{−4λ} for the prescribed cells, times the price of the leader's
remaining walk being the failing walk on m − 2λ columns with k − 2λ elements instead of (m, k), which
is ≤ (3C)^{2λ} by proof.md Lemma 3.  Heuristically the price of a fast prefix under the conditioned
(tilted, mean-C) law is e^{−2λ·KL(Geom(1/2) ‖ Geom(1−1/C))} = e^{−2λ ln(C²/(4(C−1)))}; the exact
numerics (§3) give a rate ≈ ln C per unit lag, between this and the rigorous 2 ln(12C).

Negative lag (follower ahead in element index, group 2 of the tilted grid, Δ = e > h/2): the follower
is naturally ahead; it coalesces at the leader's *first* element (leader waits μ columns in row π(1),
follower finds μ+1 ones immediately: cost 2^{−2μ−2}) and rides; it then fails iff the leader finds ≤
er − 1 ones, i.e. the leader is short by μ + 1 ones instead of 1 — price (3C)^{μ+e+1} (proof.md
Theorem 5).  Both signs give e^{−O(lag · ln C)}.

## 2. The exact calculator (joint.py)

Column-by-column Markov chain on the pair (a, b) of current elements: at column x thread i reads the
cell (π(a_i) + t_i, x); the two cells coincide iff π(a) + t_1 = π(b) + t_2, otherwise they are
independent fresh coins (each thread reads exactly one cell per column, so no other coincidence is
possible).  States with a thread completed are dropped, so the total mass after m columns is
Pr(both fail), exactly; log-scale via per-column renormalisation.  Cost O(k² m) per (π, Δ):
0.1 s at k = 100, 6 s at k = 400.  A 3-thread version (k³ states) is used at k = 64.
Validation (check_mc.py): 40 000-sample Monte Carlo on the 4×4 tilted grid, m = 28, Δ = 1, 4, 5:
exact 0.5132/0.5587/0.5104 vs MC 0.5117/0.5594/0.5129 (±0.0025); 3 threads (0,4,8): 0.4365 vs 0.4355;
identities joint2(0,k) = 2 log Pr(fail) and joint3(0,k,k) = 2 log Pr(fail) hold to 1e−13.
Every number below is exact up to floating point (no Monte Carlo, no conditioning approximations).

Notation: lf := ln Pr(E_0) = ln f(m, k−1); logratio := ln Pr(E_0 ∩ E_Δ) − 2 lf;
gain := −lf − logratio = the increase of −ln Pr when the second thread is added (independent
threads: gain = −lf; a useless thread: gain = 0).

## 3. Numerics

### 3.1 Tilted grid 10×10, k = 100 (exp1_pairs.py, out_exp1_k100.txt)
C = 8 (m = 800, −lf = 258.05).  Positive lags Δ = e ≤ 5 (lag 10e):
   e = 1: gain 20.1 (2.01/lag);  2: 41.5 (2.08);  3: 64.3 (2.14);  4: 88.7 (2.22);  5: 114.9 (2.30).
Negative lags Δ = h − e' (lag 10e' − 1): e' = 1: 28.1 (3.1/lag); 2: 48.6 (2.56); 3: 70.4 (2.43).
Lag-1 shifts Δ = dh (d = 1…9, lag d, chains with d gaps per r elements): gain 12.3, 22.9, 33.5, 44.7,
56.6, 69.7, 83.9, 99.4, 116.7 — ≈ 10.5 per unit d ≈ (2/lag-unit + 1 per gap)·… see §3.2.
The largest gain over all Δ ≤ k is 143 at Δ = 5 (= 55% of an independent thread), which is the
generic level of §3.4 — no shift of the tilted grid is better than a random pattern's worst shift.
C = 4 (m = 400, −lf = 56.1): gains 11.8, 25.1, 39.9, 55.6, 56.1 for e = 1..5 (1.18–1.39 per unit lag,
saturating at the full thread at lag ≈ 45): at C = 4 lags ≥ k/2 ARE harmless — consistent with the
rate ≈ ln C per lag versus the thread value C ln 2 per element.

### 3.2 Tilted grid 20×20, k = 400, C = 8 (exp3_k400.py, out_exp3.txt; −lf = 1018.05)
gain/lag for Δ = e = 1, 2, 3, 4, 5, 8: 1.98, 2.01, 2.04, 2.07, 2.10, 2.21 (lags 20–160): the same
rate as at k = 100 — the per-lag cost is k-independent, i.e. the loss is Θ(λ), not Θ(λ²/k).
Δ = dh (lag d, ≈ hd = 20d gaps): d = 1, 2, 3, 5, 10: gains 23, 42, 60, 96, 196: ≈ 1.0 per gap
(the follower re-enters after a gap with probability ≈ 2/C by "immediate re-entry", W13 log §2.3).
Best shift: Δ = h/2 = 10 (lag 200 both ways): gain 458 = 45% of an independent thread.

### 3.3 Rate versus C (exp2_rate.py, out_exp2.txt; k = 100)
gain per unit lag, positive lags (e = 1..4) / negative (e' = 1..3):
   C = 3: 0.79–0.87 / 1.06–0.69;  4: 1.18–1.39 / 1.69–1.43;  5: 1.46–1.68 / 2.16–1.76;
   6: 1.68–1.89 / 2.54–2.03;  8: 2.01–2.22 / 3.12–2.43;  12: 2.46–2.66 / 3.93–2.96.
   16: 2.77–2.96 / 4.52–3.33;  24: 3.20–3.39 / 5.34–3.84   (exp2b.py, out_exp2b.txt).
Compare ln C = 1.10, 1.39, 1.61, 1.79, 2.08, 2.48, 2.77, 3.18: the positive-lag rate at e = 1 is
≈ ln C to two decimals for C ≥ 8 (2.01/2.08, 2.77/2.77, 3.20/3.18) and slightly below at small C;
the heuristic 2 ln(C²/(4(C−1))) = 0.24, 0.58, 0.89, 1.18, 1.65, 2.37, 2.90, 3.67 is not the right
constant (the optimal entry is not "leader at density 1/2"); the rigorous 2 ln(12C) is a factor ≈ 3–4
too large.  Rate/thread-value = ln C/(C ln 2) → 0 as C grows: the larger C, the smaller the fraction
of an independent thread that a second thread at lag εk is worth (≈ ε ln C/(C ln 2)·2).

### 3.4 Random π and 𝓕 at k = 100 (exp4_random.py, exp4b.py; out_exp4.txt, out_exp4b.txt)
C = 8: two random π (max_Δ L_Δ = 20–22): logratio for Δ = 1..100 lies in [134, 153], mean 138, i.e.
gain ∈ [105, 124] = 41–48% of an independent thread, for EVERY Δ.  Block-perturbed grids
𝓕(10,10,ε): ε = 0.2: logratio ∈ [119, 233] (gain 25–139), minimum at Δ ≡ 5 mod 10 (lag ≈ k/2),
maximum at Δ = 10 (lag 1); ε = 0.4: [111, 218].  So on 𝓕 the lag structure of the grid persists
(perturbation only softens it) and the best shift is no better than for random π.
C = 4: random π: logratio ∈ [0, 13.7], mean 7.9 (of 56): near-independence.  C = 6: [?, 69.9], mean
59.5 (of 150): 40%.  The generic loss grows with C: this is [W9] log §4's mechanism (leader
concentrates ≈ m/2 zeros on a chain of length ≈ 20 at cost e^{−m/(2C)}; the follower's alignment
with 20 long intervals is cheap), which is precisely what the global events 𝒜_{L,s}/𝓑_{L,s,ρ}
exclude.  It is invisible in Monte Carlo (W13 exp4, W15 exp4 at m ≈ 1.6k) because it lives in the
large-deviation regime.

### 3.5 Three threads, tilted grid 8×8, k = 64, C = 8 (exp5_three.py, out_exp5.txt; −lf = 166.7)
Exact −ln Pr(all three fail) decomposed as −lf + gain₂ + gain₃ (pair gains in brackets):
   (0, 32, 64): 166.7 + 38.3 + 146.9 = 352   [gains (0,32): 38.3 (Δ = 4h, lag 4), (0,64): 166.7, (32,64): 38.3]
   (0, 3, 6):   166.7 + 52.9 + 44.4 = 264    [(0,3): 52.9, (0,6): 38.5, (3,6): 52.9]
   (0, 20, 40): 166.7 + 79.7 + 25.0 = 271    [(0,20): 79.7, (0,40): 49.3, (20,40): 79.7]
   (0, 4, 8):   166.7 + 73.7 +  4.7 = 245    [(0,4): 73.7, (0,8): 10.1, (4,8): 73.7]
   (0, 2, 4):   166.7 + 33.9 + 39.9 = 240;  (0, 4, 12): 166.7 + 73.7 + 7.0 = 247.
Independent threads would give 500.  gain₃ ≤ min of the two pair gains in every case (a follower can
ride whichever earlier thread is cheapest), and can be much smaller: in (0,32,64) thread 64's pair
gain with 32 is 38 but its gain given {0, 32} is 147 — because thread 32, when it fails together
with thread 0, rides thread 0 on the elements with s < 4, and thread 64 needs thread 32's elements with
s ≥ 4; the interaction is through the *actual trajectories*, not through pairwise lags only.  So the
transitive-riding heuristic of §5 is only an upper bound on the gain in the simple cases, and the true
multi-thread accounting needs the joint trajectory.

### 3.6 Brute-force verification of the constructions (verify_constructions.py, out_verify.txt)
Lemma 3: f(N−1,K−1) ≥ (K/N) f(N,K) checked for all N < 200, K ≤ N/3: 0 violations.
Theorem 4: for (r,h) ∈ {(4,4),(4,8),(8,8),(6,12),(12,8)}, all e ≤ h/4, m ∈ {1.15k, 1.3k, 1.6k}, 300
random matrices each with the cells of G imposed: the prescribed cell count is 4λ−1 and consistent in
every case; both threads are at (π(2λ), 2λ) at column 2λ (leader seeking 2λ, follower seeking λ) in all
9000 trials; among the 7412 trials where the leader failed, the follower failed in every one.
Theorem 5: same families, e ∈ [3h/4, h), G' imposed (2μ+2 cells, consistent) and the 2(e−1) gap cells
imposed adaptively at the columns X_{ir}: synchronisation at column μ+1 in row h holds in all 9000
trials; in the 7767 trials with ≤ er − 1 leader ones both threads failed (0 violations).

## 4. Relation to the "pretend" process and the global events

The multi-thread theorems ([W9] Thm 7, [W13] Thm 4) bound Pr(M ⊅ π ∧ 𝓑) by the failure probability
of a *modified* process in which a zero that would push some run-sum over s is replaced by a
pretended one.  The lower-bound construction of proof.md §3 uses runs ≤ 1 in the prefix and copies
the leader's own runs during the ride; rule (b) of the modified process never fires because of it, so
the same coalescence occurs in the modified process with the same probability 2^{−(4λ−1)} (heuristic
only in the last step: the analogue of Lemma 3 for the modified leader's failure probability, which is
not binomial; it is clearly of the same order since the modification only caps run-sums along
L-sets, which the prefix does not touch).  In other words: the global events remove the mechanism of
§3.4 but not the lag mechanism.  In [W9] Theorem 7's accounting the lag mechanism shows up as
|T̃_i ∩ T̃_j| ≈ m (a full ride), which the chain bound Σ_A (z_a + 1) with s ≥ Σ_A z_a correctly
predicts for long chains — so on the tilted grid the chain bound is NOT loose in the pretend process:
the follower really does ride.  W15's Remark ("𝓕 defeats the chain bound, not the threads") must be
corrected: 𝓕 defeats the threads, at every shift.

## 5. Heuristic multi-thread accounting on the tilted grid and the 𝓕 barrier

Take ℓ shifts 0 ≤ t_1 < ⋯ < t_ℓ ≤ k.  Each thread i ≥ 2 can ride an earlier thread j at price
≈ ln C · lag(t_i − t_j) + 1·gaps(t_i − t_j) (rates from §3.1–3.3 at C = 8), lag(dh + e) = er + d and
gaps ≈ hd, both ≤ k/2 in the relevant range.  Writing Δ_ij = d h + e, the price is ≈ r·min(e, h−e)·ln C
+ Δ_ij·(1 − e/h)·…  ≤ k ln C·[circdist(e_i, e_j)/h + Δ_ij/k].  Ordering the threads by t and letting
each ride the cheapest earlier one, Σ_i min_{j<i} circdist(e_i, e_j) ≤ (h/2)(1 + log₂ ℓ) and
Σ_i min_{j<i} Δ_ij ≤ (k/2)(1 + log₂ ℓ) (bisection bounds on a circle/interval), so
   −ln Pr(all ℓ fail) ≤ Ck ln 2 + O(k ln C · log₂ ℓ)   (heuristic; exact for ℓ = 2 up to constants).
Since |𝓕(√k, √k, 1/16)| ≥ e^{(1/32)k ln k} ([W15] Prop. 12) and the patterns of 𝓕 have the same lag
structure (§3.4), a union bound over 𝓕 needs −ln Pr ≥ (1/32) k ln k per pattern, i.e.
log₂ ℓ ≳ ln k/(32 ln C): ℓ ≥ k^{Ω(1/ln C)} threads, not polylog.  With ℓ = ln k threads at m = Ck the
exponent is O(k ln C ln ln k): the thread method reproduces He–Kwan's k log log k and cannot go
below it on 𝓕 — regardless of how overlaps are bounded, because here the overlaps are real.
(The 3-thread numerics of §3.5 show the bound Ck ln 2 + O(k ln C log ℓ) is not tight — actual gains
are smaller — so the barrier is if anything stronger.)

What would escape the barrier (not attempted, all speculative):
 (i) ℓ = k^{c} threads with a lag-cost lemma with rate > 2 ln 2 per unit lag (the numerics give ≈ ln C,
     so C > 4 would be needed) and an accounting of a follower against k^c leaders — a different
     programme (many cheap threads instead of few independent ones);
 (ii) a union bound over 𝓕 that exploits the correlation of its members (they all contain the same
     grid skeleton): e.g. bound Pr(∃ π ∈ 𝓕 with M ⊅ π) directly by a structured first-moment argument;
 (iii) non-thread methods (point-process / comparison with c_τ = 2/|τ|, cf. SESSION-STATE gaps).

## 6. What IS salvageable from W18 for general π (proved facts, not a theorem)

* proof.md Lemma 1–2 give the exact deterministic structure of overlaps: shared cells are unions of
  "rides" along Δ-translation segments, each ride starting with one entry.  For a π with no
  translation segment longer than u for any Δ (random π: u = O(log k) by [W14] Lemma 5), a ride is
  ≤ Σ_{x<u}(z_{a+x} + 1) cells and the number of rides is bounded by the number of entries.
* The count of entries is the true "local time" question of the prompt; but the numerics of §3.4 show
  that for random π at C ≥ 6 the joint failure is dominated by the run-concentration mechanism, not
  by entries, so any per-π lag lemma must be formulated inside a global event (as in [W9]/[W13]) —
  where the chain bound already does the job for random-like π ([W9] Theorem 8, 72k²).
* Hence the lag idea has no remaining target: for random-like π the chain bound suffices; for
  structured π (𝓕) the rides are real and no lag lemma can help.

## 7. Dead ends (with reasons)
1. Gaussian offset / local-time bound for the entry probability: correct only in the unconditioned
   regime; in the failure regime the leader can be fast for 2λ elements at price e^{−O(λ ln C)}.
2. "Choose shifts with pairwise lag ≥ √k polylog": on the tilted grid ALL shifts Δ ≤ h/4 have lag
   ≥ √k and are harmful (proof.md Cor. 6); residues mod h allow at most ≈ 1/(2ε) shifts with pairwise
   lag ≥ εk, and even those lose e^{−Θ(εk ln C)} each.
3. Per-pair bound Pr(follower fails ∧ shared ≥ s | leader) ≤ e^{−cm}: impossible for lag ≪ k
   (the ride event has probability e^{−O(λ ln C)} ≫ e^{−cm}).
4. Counting (Δ, a) pairs with lag ≤ Λ (≤ kΛ) to bound harmful shifts: the harmful threshold is Λ = Θ(k),
   so the count is Θ(k²)/L' — vacuous.
