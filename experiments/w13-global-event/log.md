# W13 — global event without log k; run-unions at n = O(k²) (log)

Date: 2026-08-29.  Directory: work/w13-global-event/.  Files: proof.md (proved statements),
exp1_LD_profile.py, exp2_staircase.py, exp3_spacing.py, exp4_joint.py, exp5_count.py, out_exp*.txt.
Reuses work/w9-alon-threads/threads.py.  Time-boxed (~2h).  PROVED = in proof.md; everything else
here is numerics or heuristics.

## 1. The idea that works: count staircase sets, not cell sets

W9's global event 𝒜_{L,s} controlled Σ r(c) over *arbitrary* sets of ≤ L cells in distinct rows, at
union-bound cost (qm)^L = e^{2L ln k}, which forces s ≳ 16 L ln k and hence chains ≤ k/(3 ln² k).

Observation: the cells that actually matter (W9 Lemma 3) are the *start cells* X_a of the leader's
intervals along a Δ-shift chain A, and these have (a) strictly increasing columns (leader order) and
(b) rows π(a)+t whose sequence is π|_A.  If π is a union of r increasing subsequences (LDS(π) ≤ r; in
particular every union of r increasing runs on value intervals), then π|_A is a union of ≤ r increasing
pieces, so {X_a} is a union of ≤ r monotone (row-and-column increasing) chains: a "ρ-staircase set"
with ρ ≤ r.  Counting these: C(2k,L)·C(m,L)·ρ^{2L} = (2e²Cρ²(k/L)²)^L — the k² from choosing rows and
columns freely is cancelled by the 1/L² from ordering (proof.md Lemma 1–2).  For L = k/λ the count is
e^{L(2 ln(ρλ) + O(1))}, no log k.  Hence s = 8L(ln(2e²Cρ²λ²)+2) = O(L log(ρλ)) suffices
(proof.md Lemma 2), and the budget (ℓ−1)(s+L) ≤ m/2 allows chains up to k/λ with
λ = O((ℓ−1) ln(ρλ)) = O(ln r · ln r) for ρ = r and ℓ ≈ ln r/D_C threads (proof.md Theorem 5).

The prompt's per-π alternative ("do not condition; union over chains of π only") was checked and is
indeed worse: it needs s ≤ m/(2ℓ) and #chains(π)·ℓ·e^{−s/8} ≤ e^{−k ln r}, i.e. C ≳ 4 ln r, giving
n ≈ k² ln² r = k²(ln ln k)² — worse than HK.  The global event avoids this because its union bound is
paid once for all π, and the count of staircase sets is e^{O(L log r)} ≪ e^{s/8} while s ≪ m/ℓ.

Why this does not simply reduce to the trivial union bound over 𝓛_r: the global event only needs to
control sets of size L = k/λ ≪ k (chains, not whole threads).  Controlling whole failing threads
(L = k) would cost e^{Θ(k log r)} objects — the same as the number of patterns — which is exactly the
trivial bound C ≥ 2 log₂ r (§4 below).

## 2. Numerics

### 2.1 L_Δ profiles for 𝓛_r (exp1, out_exp1.txt; k = 200, 400; r = 4…64)
For every Δ ∈ [k−1]: random interleaving word w gives max_Δ L_Δ(π) ≤ 1.5k/√r in ALL cases
(k=400: max L/k = 0.56, 0.43, 0.31, 0.25, 0.17 for r = 4, 8, 16, 32, 64; compare 1.5/√r = 0.75, 0.53,
0.375, 0.265, 0.19).  So F = ∅ at threshold 1.5k/√r, and the hypothesis of proof.md Theorem 5
(F(π;r,ℓ_r) small at the much larger threshold k/λ = 29k/((ln r+1)(ln r+10))) holds with room to
spare for random w — the whole "run-quasirandom" part of the residual class is covered at n = 800k².
Note that the W9 threshold k/(3 ln² r) is *smaller* than 1.5k/√r for all r ≤ 10⁴ (147–194 of the
Δ's exceed it); the new threshold k/λ is what makes the theorem non-vacuous for small r.

Periodic w (rectangular tilted grid): L_1 ≈ 0.96–0.99k, L_h ≈ 0.75–0.94k (h = k/r), and 12–198 of the
Δ's exceed 1.5k/√r.  Heuristic for periodic w: for Δ = dh + e the map b is a translation of positions
by e·r + d on each of two index groups (i ≥ e, i < e), giving L_Δ ≈ k·max(e, h−e)/h − O(Δ): long
chains for all Δ ≤ k/2, so no shift is "good": amplification is impossible for these π (but there are
few of them).

Periodic w with a fraction ε of positions randomly permuted ("def0.1", "def0.3"): at ε = 0.3 the number
of Δ with L_Δ > 1.5k/√r is 0–4 for r ≤ 32 (16 at r = 64, k = 400), i.e. already at 30% disorder the
pattern is amplifiable at the *random-w* threshold; at ε = 0.1 it is 1–23 (121 at r = 64).  Entropy of
the ε-ensemble ≈ εk(ln r + ln(1/ε) + 1); the structured (large-|F|) patterns are the low-entropy ones,
consistent with the conjectured entropy lemma of §4 but far from proving it.

### 2.2 Lemma 3 check (exp2, out_exp2.txt)
120 random instances (k ∈ {40,80,160}, r ∈ {2,4,8,16}, random and periodic w, m ∈ [1.5k, 6k], random
Δ ≤ k/2): the leader's start cells along the actual shared-cell chain A always have increasing columns,
increasing rows within each run, and LDS(rows) ≤ r: 0 violations.  Mean LDS 1.2–3.0 (max 10 at r = 16
periodic), mean |A| 1.4–23; Σ_{a∈A}(z_a+1) exceeds the true overlap by only ≈ 10–30%.

### 2.3 Prompt idea 1: shifts spaced by ≥ h = k/r (exp3, out_exp3.txt; k = 48, m = 3k, 6k)
Spacing shifts by the run height does NOT kill overlaps; it is the worst choice for periodic w:
   periodic w, r = 8:  Δ = h/2: shared = 0.00 (never meet);  Δ = h: 42 (of m = 144), P(>0) = 0.89;
                      Δ = h+1: 3.9;  Δ = 2h+1: 2.5.
   random w,  r = 8:  Δ = 1: 5.8;  Δ = h/2: 0.6;  Δ = h: 4.0;  Δ = h+1: 2.9.
Explanation (as in the prompt's own analysis): Δ = h maps run j to run j−1 with the same index, and for
periodic w the follower is exactly d = 1 element behind the leader ⇒ the two threads coalesce (two
random walks with the same increments, started 1 step apart, meet with probability 1 − O(1/√k)).
Δ = dh + e with e·r + d ≈ k/2 (e.g. Δ = h/2) puts the follower k/2 elements behind, and the threads
never meet.  For random w the lag is random of order √k, and all Δ give small overlaps.  Cross-run
chains (run j → run j−d) are exactly as long as same-run chains, so "shifts ≥ h ⇒ independent
threads" is false; what matters is the *lag* e·r + d, not Δ.

### 2.4 Joint failure (exp4, out_exp4.txt; k = 36, m = q = 72, ℓ = 3 threads at t, t+Δ, t+2Δ)
ratio = Pr(all 3 fail)/Pr(fail)³:  random w (r = 3, 6, 9): 1.00–1.36 for all Δ;
periodic w: Δ = h: 1.47, 2.16, 2.40 (coalescence), Δ = h+1: 1.03, 0.98, 1.09, Δ = h/2: 1.16, 1.44, 1.63.
Confirms W9 §2.4: near-independence except for periodic w at lag ≈ 0 mod r.

### 2.5 Count lemma (exp5, out_exp5.txt)
#{σ ∈ S_j : LDS(σ) ≤ ρ} ≤ ρ^{2j} verified for j ≤ 8, ρ ≤ 3 (e.g. j = 8, ρ = 2: 1430 ≤ 65536).

## 3. What is proved (proof.md)
* Lemma 1–2: the staircase event 𝓑_{L,s,ρ} has Pr(¬𝓑) ≤ L(e²qmρ²/L²)^L e^{−s/8}: object count
  e^{O(L log(ρk/L))}, no log k for ρ, k/L = polylog.
* Lemma 3: along any shift chain A the leader's start cells form an LDS(π|_A)-staircase set.
* Theorem 4: W9's Theorem 7 with 𝓑 in place of 𝒜 (same pretend mechanism).
* Theorem 5: n = 800k² handles (i) every π ∈ 𝓛_r (unions of ≤ r increasing runs on value intervals,
  arbitrary sizes) for every r ≤ k/(2 ln k) such that fewer than k/(2ℓ_r) − 1/2 shifts have a chain
  longer than k/λ_r, ℓ_r = ⌈(ln r+1)/29⌉, λ_r = (ℓ_r−1)(ln r+10) — unconditionally for r ≤ e^{28};
  (ii) every π with LDS(π) ≤ r (any r ≤ k) satisfying the analogous condition with ℓ'_r = ⌈(2 ln r+1)/29⌉;
  at r = k this is W9 Theorem 8 with threshold ≈ 14.5k/ln² k instead of k/(3 ln² k).
  By §2.1 the condition in (i) holds for random interleavings (F = ∅).
* Corollary 6: general π; the gain over W9 is ln k → ln(ρ(π) ln k), useful iff chains have LDS k^{o(1)}.

## 4. The exact gap
Theorem 5 + W9 Theorem 8 do NOT cover all of S_k.  Uncovered:

(G1) *Structured interleavings inside 𝓛_r / 𝓓_r*: π with LDS(π) ≤ r and at least k/(2ℓ_r) shifts Δ
having L_Δ(π) > k/λ_r, for r > e^{28} (below that everything in 𝓛_r is covered by one thread).
What is needed is an entropy lemma of the form

   (E)  for every j ≥ 1:  #{ π ∈ 𝓛_r : at most j shifts can be chosen with pairwise differences
        outside F(π; r, ℓ_r) } ≤ e^{(29 j − 1)k}.

Then Σ_π e^{−29 ℓ(π) k} → 0 and n = 800k² handles ALL of 𝓛_r (all r ≤ k/(2 ln k)), and 𝓓_r likewise.
The single-shift counting bound (proved easily by decoding w left-to-right: given A, B = b(A) as sets,
w on the smaller element of each pair determines w on the larger, so
#{π ∈ 𝓛_r : L_Δ(π) ≥ αk} ≤ (k+1)^r · C(k,αk)² · r^{k−αk} = |𝓛_r| e^{−αk(ln r − 2 ln(e/α))})
gives only e^{−k/λ_r · (ln r − 2 ln(eλ_r))} ≈ e^{−O(k/ln r)} — far from the e^{−29k} per lost thread
that (E) demands.  (E) needs the *many* long-chain shifts to give (nearly) independent constraints.
HK's shift-system encoding does not give this either: it pays log k per shift and per component, which
is where their k log log k comes from (W9 log §5).  Numerically (§2.1) the large-|F| patterns are the
near-periodic ones, whose entropy is ≪ k ln r, so (E) is plausible.  A toy check: for the ε-perturbed
periodic ensemble, entropy ≈ εk(ln r + ln(1/ε)+1) versus chains ≈ (1−2ε)k·max(e,h−e)/h; at
r = e^{57} (ℓ_r = 2) the ensemble has |F| = ∅ only for ε ≳ 0.47 and entropy ≈ 27k at ε = 0.47 < 29k:
consistent with (E) but with little slack — the constants (C = 100, D_C = 29) would need care.

(G2) *Non-monotone structure*: HK-structured π whose shift chains have large LDS — e.g. "tilted grids
with permuted rows" (value blocks V_j of size h, positions of block j given by the same arbitrary
permutation p of [h] for every j; then L_h = k − h and LDS(π|_A) = LDS(p^{-1}) can be ≈ h).  For these
the staircase count degenerates to (qm)^L.  Their number is small (h!·r^{…}) but no uniform treatment
exists yet.  Complement/reverse symmetries (decreasing runs; reverse threads fail on the same event,
W9 §2.2) reduce 𝓓_r-type classes with mixed monotone pieces to a count ρ^{2j}·2^ρ (each monotone chain
increasing or decreasing) — proof.md Lemma 1 extends verbatim — so unions of ≤ r monotone (increasing
or decreasing) runs are also covered under the same quasirandomness condition.  Not written up.

(G3) Intermediate r: Theorem 5(ii) at LDS(π) = r requires L_Δ(π) ≤ k/λ(r,ℓ'_r), λ = (ℓ'_r−1)(ln r+10)
= O(ln² r), for all but k/(2ℓ'_r) − 1/2 shifts.  A pattern with LDS ≈ √k and random-like chains
(≈ 3√k ≪ k/ln² k) is covered; patterns with chains between k/ln² r and k for many shifts are (G1)/(G2).

## 5. Prompt idea 2 (lag mechanism) — status
Not formalized.  The numerics (§2.3, §2.4) confirm W9's picture: the follower must be within ≈ √k
elements of the leader to ride, and the overlap is governed by the leader's zero-run profile on the
chain.  A rigorous per-pair statement Pr(both fail) ≤ Pr(fail)²·e^{o(k)} for Δ with lag ≫ √k would
have to control the *conditional* run profile given failure (heavy tails at scale C, W9 log §4); I see
no route that avoids a global event, and with the staircase event the pairwise loss is already only
e^{O(k log r/λ)} per pair, which is affordable — the lag idea is not needed for the amplifiable part.

## 6. Dead ends (with reasons)
1. Shifts spaced by ≥ h = k/r: cross-run chains are as long as same-run chains; Δ = h is the worst
   shift for periodic w (coalescence, §2.3).
2. Per-π chain sums without a global event: forces C ≈ 4 ln r (prompt's own computation, confirmed).
3. Global event over whole failing threads (L = k): object count = e^{Θ(k ln r)} = pattern count;
   no gain over the trivial union bound.
4. Single-shift entropy bound for (E): saving only e^{−O(k/ln r)}; the multi-shift version is the open
   lemma.
