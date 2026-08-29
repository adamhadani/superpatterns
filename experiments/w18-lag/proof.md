# W18 — the lag mechanism: exact bookkeeping, and a LOWER bound showing that lag ≫ √k does not make a shift harmless

Date: 2026-08-29.  Everything in this file is proved in full; each statement is marked PROVED.
Numerics, heuristics, the honest assessment and the exact remaining obstruction are in log.md.
Notation as in [W9] (work/w9-alon-threads/proof.md): M is a uniformly random q × m Bernoulli(1/2)
matrix, q = 2k, m = Ck; the H-thread with shift t seeks rows π(0)+t, π(1)+t, … from left to right;
E_t is the event that it fails; I_a = [X_a, Y_a] (Y_a = X_a + z_a) is the interval of columns the
thread spends on element a, in row π(a)+t; X_{a+1} = Y_a + 1.  For the follower (shift t+Δ) the same
objects are primed.  b(a) := π^{-1}(π(a) − Δ), the *element lag* of a is a − b(a) (positive: the
follower is behind in element index when the two threads are in the same row).  Lemma 0 of [W9]
(exposure principle) is used throughout.  f(N,K) := Pr(Bin(N,1/2) ≤ K), so Pr(E_t) = f(m, k−1)
exactly (the thread exposes one fresh cell per column and fails iff fewer than k of the m exposed
values are ones).

## 1. Deterministic bookkeeping of shared cells (PROVED)

**Lemma 1 (coalescence).**  Let the leader (shift t) be run to completion and then the follower
(shift t+Δ).  Suppose that while seeking element b the follower reads a cell of I_a, where
π(b) + Δ = π(a) (so b = b(a)), and that Y_a carries a genuine one of the leader (i.e. a is not the
truncated last element of a failing leader).  Then
 (i) the shared cells of I_a and I'_b are exactly the columns [max(X_a, X'_b), Y_a] of row π(a)+t;
 (ii) Y'_b = Y_a, hence X'_{b+1} = X_{a+1}: the follower's next element starts at the column at which
      the leader's next element starts.
*Proof.*  The follower scans its row from X'_b rightwards; the first column at which it is inside I_a
is max(X_a, X'_b) (it cannot enter I_a from the right, since it moves right and I_a is an interval).
From there it reads the leader's cells, which are zeros up to Y_a − 1 and a one at Y_a; it stops at
Y_a.  So the shared cells are exactly [max(X_a, X'_b), Y_a], Y'_b = Y_a and X'_{b+1} = Y_a + 1 =
X_{a+1}.  ∎

**Lemma 2 (rides along translation segments).**  Call positions a, a+1, …, a+u−1 a *Δ-translation
segment* if b is defined on them and b(a+x) = b(a) + x for 0 ≤ x < u.  If the follower shares a cell
of I_a with the leader (as in Lemma 1) and [a, a+u) is a translation segment, then the follower's
elements b(a)+x, 1 ≤ x < u, read exactly the cells I_{a+x} (all of them, no fresh coin), i.e.
|T_t ∩ T_{t+Δ}| ≥ (Y_a − max(X_a, X'_{b(a)}) + 1) + Σ_{x=1}^{u−1} (z_{a+x} + 1), provided the leader's
ones at Y_{a+x} are genuine (leader not yet truncated).
*Proof.*  By Lemma 1(ii) the follower starts element b(a)+1 at X_{a+1} in row π(b(a)+1) + t + Δ =
π(a+1) + t (because b(a+1) = b(a)+1 means π(b(a)+1) = π(a+1) − Δ).  So it reads I_{a+1} entirely and
by Lemma 1 ends at Y_{a+1}; induct on x.  ∎

*Remark.*  Lemmas 1–2 are the exact form of the "riding" of [W13] log §2.3: sharing is not a matter of
overlapping *windows* but of *coalescence* — once the follower enters a leader interval it moves in
lock-step with the leader for as long as the chain is a translation.  For the tilted grid with
Δ = e < h (below) the whole chain is one translation segment of length k − er, so a single entry
gives a ride to the end.  This is why the lag has to be paid only ONCE, at the entry, and why the
cost is linear in the lag (Theorem 4) rather than Gaussian e^{−λ²/k}.

## 2. A binomial shift inequality (PROVED)

**Lemma 3.**  If N ≥ 3K − 1 and K ≥ 1 then f(N−1, K−1) ≥ (K/N) · f(N, K).  Consequently, if
m ≥ 3k and 1 ≤ j ≤ k − 2 then
   f(m − j, k − 1 − j) ≥ ((k − 1 − j)/m)^j · f(m, k−1).
*Proof.*  For 1 ≤ i ≤ K, C(N,i−1)/C(N,i) = i/(N − i + 1) ≤ K/(N − K + 1) ≤ 1/2 by N ≥ 3K − 1; hence
f(N,K) = 2^{−N} Σ_{i ≤ K} C(N,i) ≤ 2^{−N} C(N,K)(1 + 1/2 + 1/4 + ⋯) = 2^{1−N} C(N,K).  On the other
hand f(N−1,K−1) ≥ 2^{−(N−1)} C(N−1,K−1) = 2^{1−N} (K/N) C(N,K).  Divide.  For the consequence apply
the first claim j times to (N,K) = (m − i, k − 1 − i), i = 0, …, j−1: the hypothesis m − i ≥
3(k − 1 − i) − 1 follows from m ≥ 3k, and each factor (k−1−i)/(m−i) ≥ (k−1−j)/m.  ∎

## 3. The lower bound (PROVED)

Throughout this section π is the tilted grid on k = rh elements, π(i·r + s) = s·h + i (0 ≤ i < h,
0 ≤ s < r), the leader has shift 0 and the follower shift Δ = e with 1 ≤ e < h.  Recall ([W14]
Lemma 1(c), with d = 0): for a = ir + s with i ≥ e, b(a) = a − er ("group 1", lag +er, a translation
on all of {a ≥ er}); for i < e and s ≥ 1, b(a) = a + (h−e)r − 1 ("group 2", lag −((h−e)r − 1),
undefined at s = 0).

**Theorem 4 (positive lag: coalescence costs e^{−2λ ln(6C)}).**  Let 1 ≤ e ≤ h/4, λ := e·r,
m = Ck with C ≥ 3, k ≥ 6.  Then
   Pr(E_0 ∩ E_e) ≥ 2 · (2^{4} · 9C²)^{−λ} · Pr(E_0) = 2 e^{−2λ ln(12 C)} Pr(E_0).
*Proof.*  Define the event G: (i) M(π(a), a) = 1 for 0 ≤ a < 2λ; (ii) M(π(b) + e, 2b) = 0 and
M(π(b)+e, 2b+1) = 1 for 0 ≤ b < λ.
*The prescribed cells are consistent and number 4λ − 1.*  For b = i'r + s' < λ = er we have i' < e, so
π(b) + e = s'h + (i' + e) = π((i'+e) r + s') = π(b + λ) (as i' + e < 2e ≤ h/2 < h).  A cell of (ii)
coincides with a cell of (i) iff its row is π(a) with a = b + λ ∈ [λ, 2λ) and its column is a, i.e.
b + λ ∈ {2b, 2b+1}, i.e. b = λ (excluded) or b = λ − 1, a = 2λ − 1, column 2λ − 1, where (i) and (ii)
both prescribe the value 1.  Within (i) rows π(a) are distinct; within (ii) rows π(b)+e are distinct.
So G prescribes 2λ + 2λ − 1 = 4λ − 1 distinct cells and Pr(G) = 2^{1−4λ}.
*On G both threads coalesce at column 2λ.*  On G, the leader at column a < 2λ seeks element a (induction:
it reads the one at (π(a), a) and advances), so X_{2λ} = 2λ.  The follower at columns 2b, 2b+1 seeks
element b < λ (reads 0 then 1), so X'_λ = 2λ, and its element λ = (e, 0) has row π(λ) + e = 2e =
π(2λ) (2λ = (2e, 0), 2e < h).  Hence at column 2λ both threads are in row π(2λ) at the same column.
By induction on the column, for every x ≥ 2λ the leader seeks some element a(x) ≥ 2λ and the follower
seeks a(x) − λ, both in row π(a(x)) (for a ≥ 2λ the position a has i ≥ 2e ≥ e, so π(a − λ) + e =
π(a)); they read the same cell and advance together.  Therefore, if the leader fails — runs out of
columns while seeking some a(m−1) ≤ k − 1 — the follower runs out while seeking a(m−1) − λ ≤ k − 1 and
fails too: G ∩ E_0 ⊆ E_e.
*Probability.*  On G the leader's exposures at columns ≥ 2λ are cells in rows π(a), a ≥ 2λ, at columns
≥ 2λ, none of which is prescribed by G; by the exposure principle (Lemma 0, applied to the procedure
"reveal the 4λ−1 cells of G, then run the leader") they are i.i.d. fair bits, and E_0 ∩ G = G ∩
{fewer than k − 2λ ones among these m − 2λ bits}.  So Pr(E_0 ∩ E_e) ≥ Pr(G ∩ E_0) =
2^{1−4λ} f(m − 2λ, k − 1 − 2λ).  By Lemma 3 with j = 2λ ≤ k/2 (e ≤ h/4), f(m−2λ, k−1−2λ) ≥
((k−1−2λ)/m)^{2λ} f(m,k−1) ≥ ((k/2 − 1)/(Ck))^{2λ} f(m,k−1) ≥ (3C)^{−2λ} Pr(E_0) for k ≥ 6.  Hence
Pr(E_0 ∩ E_e) ≥ 2 · 2^{−4λ} (3C)^{−2λ} Pr(E_0) = 2 (16 · 9C²)^{−λ} Pr(E_0).  ∎

**Theorem 5 (negative lag: the follower ahead in element index).**  Let 3h/4 ≤ e ≤ h − 1, r ≥ 4,
μ := (h − e) r − 1, m = Ck with C ≥ 3, k ≥ 6.  Then
   Pr(E_0 ∩ E_e) ≥ (12C)^{−(μ + e + 1)} Pr(E_0) = e^{−(μ+e+1) ln(12C)} Pr(E_0).
*Proof.*  Define G': (i) M(π(b) + e, b) = 1 for 0 ≤ b ≤ μ; (ii) M(π(0), 0) = M(0,0) = 1;
(iii) M(π(1), x) = M(h, x) = 0 for 1 ≤ x ≤ μ.  Rows of (i): for b = i'r + s' ≤ μ we have i' ≤ h−e−1, so
π(b) + e = s'h + (i' + e) with i' + e ≤ h − 1; this equals row 0 never (e ≥ 1) and equals row h iff
s' = 1, i' = h − e, which is excluded; the rows of (i) are pairwise distinct.  So G' prescribes
(μ + 1) + 1 + μ = 2μ + 2 distinct cells, Pr(G') = 2^{−2μ−2}.
On G' the leader finds element 0 at column 0 and then seeks element 1 in row h through column μ; the
follower finds elements 0, …, μ at columns 0, …, μ; so at column μ + 1 the leader seeks element 1 in row
π(1) = h and the follower seeks element μ + 1 = ((h−e), 0), whose row is π(μ+1) + e = (h − e) + e = h.
They coalesce.  From then on, by induction, at each column the leader seeks some element a ≥ 1 and the
follower seeks a + μ, and their rows agree whenever a = ir + s has s ≥ 1 (then π(a+μ) + e = π(a), group
2); at the *gap elements* a = ir, 1 ≤ i ≤ e − 1 (a < er, s = 0) the follower's row is
π(ir + μ) + e = rh + i − 1 ≥ k, a row the leader never visits.  Let G'' be the event that G' holds and,
for each of the e − 1 gap elements a = ir, the first cell the leader reads for element a AND the first
cell the follower reads for element a + μ are both ones.  These 2(e−1) cells are read at the columns
X_{ir} (the same column for both, by the induction), are fresh at that moment (each thread reads one
cell per column; the two cells are in different rows), so each is a fair bit independent of the past;
on G'' both threads advance together at the gap and remain synchronised, for all leader elements
a = 1, …, er − 1 (these are exactly the elements with i < e; the follower's element a + μ ≤ k − 2).
The follower's last element k − 1 = er + μ corresponds to the leader element er = (e, 0), whose row
π(er) = e differs from the follower's row π(k−1) + e = k − 1 + e ≥ k; so the follower starts its last
element (in a fresh row) exactly when the leader starts element er, i.e. only if the leader has found
er ones.  Hence on G'': if the leader finds at most er − 1 ones in total, the follower never starts
its last element and fails, and so does the leader (er − 1 ≤ k − 1).  The leader's ones on G'' consist
of the prescribed one at column 0, the e − 1 prescribed gap ones, and the ones among its remaining
m − (μ + 1) − (e − 1) = m − μ − e fresh bits; "at most er − 1 ones in total" is "at most
er − 1 − e = k − 2 − μ − e ones among the fresh bits" (using er = k − μ − 1).  So
   Pr(E_0 ∩ E_e) ≥ Pr(G'') · f(m − μ − e, k − 2 − μ − e) = 2^{−2μ−2e} f(m − (μ+e), k − 1 − (μ+e+1)).
Since f is monotone in its second argument, f(m − (μ+e), k−1−(μ+e+1)) ≥ f(m − (μ+e+1), k−1−(μ+e+1)),
and μ + e + 1 ≤ k/4 + h ≤ k/2 (μ ≤ (h/4) r = k/4 as e ≥ 3h/4; e + 1 ≤ h ≤ k/4 as r ≥ 4), so Lemma 3
gives f(m−(μ+e+1), k−1−(μ+e+1)) ≥ (3C)^{−(μ+e+1)} f(m, k−1), and 2^{−2μ−2e} ≥ 4^{−(μ+e+1)}.  ∎

**Corollary 6 (no shift with lag ≤ k/4 is harmless).**  Let π be the tilted grid with r, h ≥ 4, and
m = Ck with C ≥ 8.  Put Λ(e) := 2er for 1 ≤ e ≤ h/4 and Λ(e) := (h−e)r + e for 3h/4 ≤ e < h (so that
Theorems 4–5 read Pr(E_0 ∩ E_e) ≥ (12C)^{−Λ(e)} Pr(E_0)); in both cases Λ(e) ≤ k/2.  Then
   Pr(E_0 ∩ E_e) / Pr(E_0)² ≥ exp( k (C ln 2 − 1 − ln C) − Λ(e) ln(12C) ) ≥ e^{c_C k},
with c_C := C ln 2 − 1 − ln C − (1/2) ln(12C) > 0 for C ≥ 8 (c_8 = 0.18, c_9 = 0.70, c_{18} = 5.9,
c_{100} = 60.2).  In particular, for the He–Kwan tilted grid every shift Δ ≤ h/4 — whose element lag
er ranges over r, 2r, …, k/4 (all ≥ √k when r ≥ √k) — satisfies Pr(E_0 ∩ E_Δ) ≥ Pr(E_0)² e^{Ω(k)}.
*Proof.*  Pr(E_0) = f(m, k−1) ≤ exp(−m D((k−1)/m ‖ 1/2)) ≤ exp(−m D(1/C ‖ 1/2)) (Chernoff; D(p‖1/2) is
decreasing in p ≤ 1/2), and D(1/C‖1/2) = ln 2 − H(1/C) ≥ ln 2 − (1 + ln C)/C (H(p) ≤ p ln(e/p)).  So
1/Pr(E_0) ≥ exp(k(C ln 2 − 1 − ln C)).  Combine with Theorems 4 and 5 and Λ(e) ≤ k/2.  ∎

## 4. What the lower bound says about the multi-thread framework (PROVED parts marked)

**Proposition 7.**  (PROVED)  In the setting of Corollary 6, for every shift e with Λ(e) ≤ 2εk
(e.g. positive lag er ≤ εk), the two-thread exponent satisfies
   −ln Pr(E_0 ∩ E_e) ≤ −ln Pr(E_0) + 2εk ln(12C) + O(1),
whereas two independent threads would give −ln Pr(E_0)² = 2·(−ln Pr(E_0)) ≥ −ln Pr(E_0) + k(C ln 2 − 1 − ln C).
So the second thread contributes at most a fraction 2ε ln(12C)/(C ln 2 − 1 − ln C) + o(1) of an
independent thread; for ε = 1/4 (lag k/4, the largest lag covered) and C = 100 this fraction is
≤ 0.056, for C = 18 it is ≤ 0.31; numerically the true fraction is smaller still (log.md §3).
*Proof.*  Restate Theorems 4–5 and Corollary 6.  ∎

*Consequences (the multi-thread part is heuristic; see log.md §4–5).*  (a) The W18 conjecture
"a shift whose chains all have element lag ≫ √k · polylog(k) is harmless (Pr(E_t ∩ E_{t+Δ}) ≤
Pr(E_t)² e^{o(k)})" is FALSE: on the tilted grid every shift Δ ≤ h/4 has all chain lags ≥ r = √k
(for r = h) and yet Pr(E_0 ∩ E_Δ) ≥ Pr(E_0)² e^{Ω(k)}.  The loss is linear in the lag (rate
≤ 2 ln(12C) rigorously; ≈ ln C numerically, log.md §3), not e^{−Ω(λ²/k)}; the √k threshold observed
in W15's simulations is an artefact of the *unconditioned* regime (both walks at speed 2, diffusive
offset), see log.md §2.
(b) The mechanism (fast prefix + coalescence + ride) uses no long zero-run: all runs in the prefix
are ≤ 1 and the ride copies the leader's own runs.  It is therefore not excluded by the global
events 𝒜_{L,s} ([W9]) or 𝓑_{L,s,ρ} ([W13]) — those cap run-sums, and the ride needs none — so the
same loss is present in the "pretend" process of [W9] Theorem 7 (heuristic, log.md §4).
(c) Since a follower can ride whichever earlier thread has the smallest lag, and the sum over ℓ
shifts of "lag to the nearest earlier shift" is at most (k/2)(1 + log₂ ℓ) (bisection bound on a
circle of length h), the exponent obtainable from ℓ threads on the tilted grid is at most
Ck ln 2 + O(k ln C · log ℓ) (heuristic beyond ℓ = 2).  For ℓ = polylog(k) this is O(k ln C ln ln k)
≪ (1/32) k ln k, the exponent needed to union-bound over the family 𝓕(√k, √k, 1/16) of [W15].
Hence the thread framework with polylogarithmically many threads at m = Ck cannot prove n = O(k²)
for 𝓕, whatever lag lemma one proves; the barrier is of the same k log log k type as He–Kwan's.
