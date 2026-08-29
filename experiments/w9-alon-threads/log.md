# W9 — removing log log k from He–Kwan: threads, overlap accounting, cross-direction threads (log)

Date: 2026-08-29.  Directory: work/w9-alon-threads/.  Files: threads.py (simulator), exp1_overlap.py,
exp2_crossdir.py, exp3_lemmaW.py, exp4_amplify.py, out_*.txt (raw runs), proof.md (proved statements).
Time-boxed session (~2h).  PROVED = in proof.md with full proof; everything else here is numerics or heuristics.

## 1. Model and simulator (threads.py)

M ∈ {0,1}^{q×m} i.i.d. Bernoulli(1/2), q = 2k unless stated, m = Ck.  H-thread (HK's): rows π(j)+t,
scan columns left→right; exposes one cell per column.  New thread types implemented: Hr (reverse
element order, scan right→left), V (columns π^{-1}(v)+s, scan rows bottom→top, one cell per row), Vr.
Functions: L_delta (HK's L_Δ), overlap_stats (shared cells / zeros / coincidence intervals),
W_delta (max-weight Δ-shift chain, exp3).  All claimed inequalities below were tested on random M
before being proved.

## 2. Numerical findings

### 2.1 H–H overlap for structured π (exp1, k = 200, m = 5k, unconditioned; out_exp1.txt)
π ∈ L_k^{(r)} = unions of r increasing runs on value intervals, interleaving word w random or periodic.
Selected rows (shared = |T_t ∩ T_{t+Δ}| mean over 20 matrices; HK bound = L_Δ·Z with Z = max zero run ≈ 17):

    r   w      Δ    L_Δ   shared  #coincidence intervals   L_Δ·Z
    1   -      1    199   358        0.9  (one long ride)   3383
    2   rand   1    148    58       18.2                    2516
    2   rand   25    89     0        0                      1513
    2   per    1    198   302        0.8  (one long ride)   3366
    5   rand   1    102    28       12.2                    1734
    5   per    1    195   248        0.8                    3510
    20  rand   1     58    12        5.7                    1044
    20  per    1    180    16        0.1                    3240
    50  rand   1     41     3        1.4                     697
    tilted-grid-like (periodic w): riding = one coincidence interval covering ~1/3 of the columns.

Two mechanisms visible: (a) *riding* — periodic w / identity: after one coincidence the threads stay
together (consecutive shift pairs); (b) *timing* — for Δ ≥ ~√m/r the threads never meet at all (the
follower is behind by ≈ rΔ elements ≈ 2rΔ columns and the column-lag random walk has spread only
≈ √(2m)); random w kills (a) (a consecutive shift pair after a coincidence has probability ≈ 1/r).
He–Kwan's bound L_Δ·Z overestimates the actual overlap by a factor 10–1000 in all cases.

### 2.2 Cross-direction threads (exp2; out_exp2_k12.txt, out_exp2_k20.txt)
* DEAD END: the reversed H-thread Hr fails on exactly the same event as H (both fail iff no copy of π
  lies in rows t..t+k−1; the greedy is complete).  Empirically Pr(H∧Hr fail) = Pr(H fail) to 4 digits.
  My initial "|T_H ∩ T_Hr| ≤ 1" claim was wrong (H's later cells and Hr's earlier cells share columns);
  the simulator caught it (130/300 violations).  Same for V vs Vr.
* H vs V are nearly independent for every π tried (identity, r=2 random, r=3 periodic, uniform):
  k=20, q=m=50: Pr(H∧V) = 0.00365 vs product 0.00357; k=36, m=q=72: ratios 0.97–1.02 (exp4).
  This is PROVED in the form |T_H ∩ T_V| ≤ k (proof.md Lemma 1, Prop. 2), but it is asymptotically
  worthless for the union bound (proof.md, Remark after Prop. 2): the exponent m+q−k under n = 2qm is
  maximised at the single-thread extreme q = k.

### 2.3 Refined chain bound (exp3; out_exp3.txt)
Lemma 3 (|T_t ∩ T_{t+Δ}| ≤ W_Δ(z) = max over Δ-shift chains A of Σ_{a∈A}(z_a+1), z = leader's
zero-run profile) and Lemma 1 (H–V ≤ k): 0 violations in 400 random instances (k ∈ [6,60],
m ∈ [1.5k, 6k], uniform / identity / runs / periodic runs).  Averages (all instances | leader failed):

    kind           mean shared   mean W_Δ(z)   mean L_Δ(Z+1)  |  shared, W given leader fails
    uniform            1.4          13.1           72.5       |     1.3   12.5
    identity           2.2          30.2          215.4       |     1.1   15.7
    runs (random w)    1.0          18.6          113.1       |     0.6   21.7
    runs (periodic w)  1.2          24.1          162.4       |     1.5   24.9

W_Δ is ≈ 6–8× below HK's L_Δ(Z+1); the true overlap is another ≈ 10× below W_Δ (timing).

### 2.4 Multi-thread amplification in the failure regime (exp4; out_exp4_k36.txt)
k = 36, m = q = 72 (single-thread failure ≈ 0.45), ℓ = 4 H-threads at shifts t, t+Δ, t+2Δ, t+3Δ,
ratio = Pr(all 4 fail)/Pr(fail)^4 (1 = independent):

    π              Δ=1    Δ=3    Δ=8
    identity       5.65   2.03   1.06
    runs r=2 rand  1.79   1.08   1.03
    runs r=5 rand  1.44   1.08   1.15
    runs r=5 per   1.16   1.20   1.12
    tilted grid    1.08   1.98   1.09
    uniform        1.17   1.16   1.22

Even for the identity, Δ = 8 already gives near-independence at this size: the timing mechanism
(§2.1(b)) dominates — a follower at lag Δ elements can only ride if it first waits ≈ CΔ columns.

### 2.5 L_Δ for the r-run family (out_LD.txt; k = 200, 400, 800, random w)
max_Δ L_Δ(π)/k ≈ 0.75, 0.57, 0.43, 0.32, 0.24, 0.17, 0.12 for r = 2, 4, 8, 16, 32, 64, 128, and
L_1(π)·√r/k ≈ 1.05–1.4 across k — i.e. L_1 ≈ 1.3 k/√r, with L_Δ decreasing in Δ.  So HK's tightness
example L_k with r = log^{10} k has L_Δ ≈ k/log^5 k ≪ k/(3 ln² k) at least for small Δ, i.e. it lies
inside the new class 𝒬'_k of Theorem 8 (numerically; not proved for all Δ).  The obstruction to the
union bound therefore moves to r ≲ (ln k)^4, where |L_k^{(r)}| = r^k = e^{Θ(k log log k)} still.

## 3. What is proved (proof.md)

* Lemma 3 / Prop. 4: the exact refined overlap bound and the two-thread conditional inequality
  Pr(E_t ∩ E_{t+Δ}) ≤ E[1_{E_t} Pr(Bin(m − W_Δ(z),1/2) ≤ k−1)].
* Theorem 7: with a global event 𝒜_{L,s} ("every set of ≤ L cells in distinct rows has total
  rightward zero-run < s", Pr(¬𝒜) ≤ 2(qm)^L e^{−s/8}), ℓ threads whose pairwise shifts have
  L_Δ(π) ≤ L give Pr(M ⊅ π, 𝒜) ≤ Pr(Bin(ℓ(m/2−k),1/2) ≤ ℓ(k−1)) provided (ℓ−1)(s+L) ≤ m/2.
* Theorem 8: at m = 18k (n = 72k²) w.h.p. σ contains every π that is (1/(3 ln²k), k/(3 ln k))-
  quasirandom, i.e. L_Δ(π) ≤ k/(3 ln² k) for all but < k/(3 ln k) shifts Δ.  The exceptional set has
  size ≤ k!·e^{−(1/3−o(1))k/ln k}, versus k!·e^{−Θ(√k)} for HK's Q_k (L_Δ ≤ 3√k for all Δ).
  This is a strict strengthening of HK Theorem 1.3 (larger class; constant 72 instead of 20).
* Prop. 2: cross-direction (H,V) threads: Pr(both fail) ≤ Pr(Bin(m+q−k,1/2) ≤ 2k−2) for every π.
  Honest remark: no asymptotic consequence.

## 4. Why "deterministic in the exposed set" accounting cannot, by itself, remove the union bound
(Heuristic but quantitatively precise; this answers plan item 2's question.)
Prop. 4 is sharp as an accounting: the leader's zero-runs z_a are i.i.d. Geom(1/2), failure is
Σ(z_a+1) > m, and the follower is free exactly on the heaviest Δ-chain.  Consider the event
H_A = {Σ_{a∈A} z_a ≥ m/2} for a fixed Δ-shift chain A of length L ≪ k.  Given failure, the z's behave
like i.i.d. geometrics of mean C = m/k, whose tail is ≈ e^{−x/C}; so Pr(H_A | fail) ≈ e^{−(m/2)/C} =
e^{−k/2}·poly — only e^{−Θ(k)}, NOT e^{−Θ(m)}.  Unconditionally Pr(fail ∧ H_A) ≈ 2^{−m}·poly, much
larger than Pr(fail)² ≈ 2^{−2m}·poly.  On H_A the follower rides for free.  Consequently, for any π
admitting a Δ-chain of length ≳ k/C for the available Δ's, the best per-π bound obtainable from
Prop. 4-type accounting is Pr(both fail) ≲ Pr(fail)·e^{−Θ(k)} ≈ e^{−m ln 2}·e^{O(k)}·e^{−Θ(k)}, and with
ℓ threads the exponent saturates at ≈ m ln 2 (the leader concentrates its zeros on chains and every
follower rides): per-π amplification is capped at e^{−m ln 2} = e^{−Ck ln 2}.  Since the union bound
needs e^{−k ln k}, C must be ≈ log k: no gain.  HK escape this with the *global* events A, B whose
failure is excluded once for all π; the price of a global event is the union bound over the objects
it controls — for B these are the structured maps, count e^{21k log log k}.  Theorem 7 replaces B by
𝒜_{L,s}, whose objects are arbitrary L-sets of cells (count (qm)^L = e^{O(L log k)}), which is cheap
precisely when L ≤ k/log k — the chain-length hypothesis of Theorem 8.

The plan's hope (log W5 §2.3(iv)) that "each re-alignment costs Ω(1) fresh coins" is TRUE in
expectation (§2.1–2.4: the timing mechanism makes actual overlaps tiny) but the *tail* is governed by
the leader's run profile, which conditioned on failure is heavy-tailed at scale C; the follower's
timing cost is real (a follower at lag Δ must first spend ≈ CΔ extra columns) but I could not turn it
into a per-π bound better than e^{−O(m)}: a chain of followers each catching the previous one costs
only e^{−CΔ} each, total e^{−Ck} = e^{−O(m)}.

## 5. Exact accounting of where log log k survives
With ℓ threads at m = Ck one needs ℓ ≥ (ln k)/(c·C) threads (each fresh half-thread costs e^{−Θ(Ck)},
target e^{−k ln k}), and each thread can afford ≤ m/(2ℓ) shared cells per earlier thread, i.e. chains of
length L ≤ Ck/(2ℓ·(run scale)) ≈ k/(ℓ log k) (Theorem 7 needs s ≈ 20 L ln k because of the (qm)^L union
bound; with HK's per-row bound Z = log²k it would be k/(ℓ log² k)).  So the quasirandomness parameter
must be α ≈ 1/(ℓ log k) ≈ 1/log² k, and HK's decomposition (Lemma 4.2/4.4) at level α with q admissible
exceptional shifts has count exp((b+q')log k + k log q') with q' ≈ (4/α)q, b ≈ (4/α)k/q: the k^b term
forces q ≥ (4/α) log k ≈ log³ k, hence k log q' ≈ 3k log log k, hence m ≈ k log log k for the event B.
The count is tight for L_k^{(r)} with r ≈ log^{2..3} k (e^{Θ(k log log k)} patterns, all with
L_Δ ≈ 1.3k/√r ≫ αk).  So the remaining gap is exactly: patterns that are unions of r ∈ [C, (ln k)^4]
increasing runs on value intervals (and HK's more general shift-systems of that size).  Neither
amplification (chains of length k/√r ≫ k/log² k) nor the union bound (r^k patterns need e^{−k log r}
per pattern, i.e. ≈ log r independent threads) covers them; a per-π tail bound of e^{−k log r} for
these π at m = Ck would finish the proof (cf. §4 for why chain-accounting alone cannot give it).

## 6. Dead ends (with reasons)
1. Reversed threads Hr, Vr: identical failure events to H, V (§2.2).
2. Cross-direction (H,V): rigorous 2× but the exponent-per-n is unchanged (proof.md Remark).
3. Per-run shifts (thread rows π(a)+t_{w(a)} with a shift per run): same-run coincidences are unchanged
   (a = Δ-th next occurrence of the same letter), so no gain for L_k^{(r)}.
4. Row-disjoint / column-residue-class threads: disjoint exposures give e^{−Ω(total cells/…)} = e^{−Ω(m)}
   in total — no amplification; amplification must reuse cells (as in HK).
5. Deterministic potential-function bound on re-alignments: the bound is W_Δ(z) (Lemma 3) and the
   heavy-chain event has only cost e^{−Θ(k)} given failure (§4) — cannot replace the global event.
6. Plan item 3 (direct LIS-type embedding of L_k^{(r)} via r strips): not attempted beyond noting that
   the lower tail of LIS has speed N (Deuschel–Zeitouni 1999; Ledoux 2005 gives
   Pr(LIS(N) ≤ (2−ε)√N) ≤ e^{−cε³N}), which would beat r^k for r ≤ k^{o(1)} *if* the interleaving word
   could be handled; the interleaving constraint is a joint condition on r chains and I know no
   large-deviation bound for it.  Lemma A of W5 (direct sums) does not apply because the runs are
   interleaved in position.
