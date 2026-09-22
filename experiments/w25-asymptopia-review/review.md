> **Superseded numerical conclusion, 2026-09-10.** The current [proof](proof.md) repairs the finite width domain and minimum argument, and certifies coefficient 1.0073. The approximate optimization 1.0073384 below does not justify rounding up to 1.00734. This literature review is retained as history.

# W25 — Joel Spencer (with Laura Florescu), *Asymptopia* (AMS Student Mathematical Library 71, 2014): what it offers for the lower-bound constant, the containment threshold, and speed-N tails

Source: `~/Library/CloudStorage/Dropbox/Books/Mathematics/[Spencer] Asymptopia.pdf` (202 PDF pages; book page =
PDF page − 18 in the main text; all page numbers below are **book pages**). Read: the whole book (Ch. 0–13),
via full-text extraction and the table of contents (pp. v–viii).
Companion review: `experiments/w22-probabilistic-method-review/review.md` (Alon–Spencer). Nothing from W22 is
repeated here; where the two books overlap (Chernoff, LLL, Poisson paradigm, deletion) I only record what
*Asymptopia* adds, which is mostly the asymptotic-calculus viewpoint.

Notation as in the paper (`output/paper/superpatterns-notes.md`): `n = λk²/e²`, tilt `x = e^{−θ/k}`,
`τ = θλ/e²`, even widths `b = (k/θ)B`, `B ~ Γ(2,1)` in the limit; `N = Ck²` points of a Poisson process for
the Alon side; `μ = E#copies = N^k/(k!)²·(1+o(1))`.

---

## A. Executive summary

**What the book is.** An undergraduate text on asymptotic calculation: Stirling by the Laplace method (Ch. 1),
big-O calculus (Ch. 2), Laplace-type integrals with the MID/LEFT/RIGHT template (Ch. 3), sums vs. integrals
(Ch. 4), asymptotics of `C(n,k)` in every regime of `k` (Ch. 5), Prüfer codes and unicyclic graphs (Ch. 6),
Ramsey lower bounds by Erdős magic / deletion / LLL with the *asymptotic* evaluation done carefully (Ch. 7),
Chernoff bounds and the three deviation regimes (Ch. 8), the prime number theorem up to constants (Ch. 9),
random triangles and the convex hull of random points (Ch. 10), recurrences and sorting (Ch. 11), LIL, the
Poisson paradigm via Bonferroni, coupon collector, connectivity threshold, log* (Ch. 12), big numbers (Ch. 13).

**What is *not* in it (checked against the TOC, the index and the full text).** No Erdős–Szekeres, no longest
increasing subsequence, no Ulam/Hammersley/`2√n`, no Tracy–Widom, no random permutations beyond cycle structure
(pp. 54–55) and sorting lower bounds (pp. 146–147); no "Kinetic view" or "hypothetical reasoning" chapters
(those belong to Spencer's *The Strange Logic of Random Graphs* / *Ten Lectures*, not to this book); no
Janson, no martingales, no Talagrand, no entropy compression, no transfer operators. The Ramsey chapter has
no "algorithmic counting" — only Erdős magic (Thm 7.1, p. 94), deletion (Thm 7.2, p. 94), LLL (Thm 7.3, p. 95)
and their asymptotic evaluation (§7.4–7.6). So items (2) and (5) of the brief are essentially empty, and I say
so below rather than pad them.

**Bottom line, by item of the brief.**

1. *Laplace method / tilt for the lower bound.* The book's central lesson (Ch. 1, Ch. 5, Ch. 8) — an
   exponential-tilt/Chernoff bound on a sum of i.i.d. terms has the **exact** exponential rate, losing only a
   polynomial factor (pp. 8–12; Thm 5.7, p. 65; (8.29)–(8.30), p. 109) — means that Theorem A's inequality (A)
   is already tight at the exponential scale *for the weight `W = Π f(b_i)`*: no sharper evaluation of that
   sum exists, and no two-parameter tilt can help (§B.1(a)–(c)). Where the book *does* point to slack is the
   only place in Theorem C where a large deviation is bounded crudely: the slot count is a sum of `b−2`
   independent Bernoullis with success probabilities `≈ 0.6–0.85`, and the paper bounds its upper tail with the
   Poisson-type `exp(−m h(ε))`, which is the "large deviations, `λ → 0`" regime of p. 106; the count actually
   sits in the "very large deviations, `λ` constant" regime (p. 106, p. 109), where the exact Bernoulli
   (Cramér) rate `D((1+ε)p ‖ p)` is larger by a factor `≈ 1/(1−p) ≈ 3–6`. A one-line concavity lemma makes
   the Bernoulli bound uniform in `σ` (§B.1(d)). Re-running the paper's own limit formula (W7's `rate.py`,
   which I first reproduced: `λ_C = 1.004829`) with this single change and width-dependent `ε(b)` gives
   **`λ = 1.00734`** (files `rate_bernoulli2.py`, `rate_bernoulli2.out`), i.e. the excess over `1/e²` grows
   from `0.00483` to `0.00734` (from `63×` to `≈ 96×` CKS), halfway from the current constant to the `ε = 0`
   heuristic ceiling `1.0117`. This is the one genuinely new, rigorous-in-principle output of this review;
   it needs the coordinator's line-by-line check of Lemma B.1 and a rerun of `finite_check.py` with the new
   bad term.
2. *LIS / Erdős–Szekeres.* Absent. The only permutation content is cycles (prisoners, pp. 54–55), the
   information-theoretic sorting bound `lg n!` (pp. 146–147), Quicksort (pp. 148–150), and the "tilt your head
   45°" coordinate change for the 2-D walk (p. 22, fn. 9) — the light-cone coordinates of Hammersley's process,
   but used only for `Z²` return probabilities. Nothing usable.
3. *Threshold heuristics.* The book's threshold machinery is: first moment (Thm 7.1), Poisson paradigm through
   Bonferroni (Thm 12.12, pp. 162–164; coupon collector Thm 12.14, connectivity Thm 12.16), and
   parametrization to see the critical window (Ex. 5.4, pp. 61–62; p. 97 "solutions to basic problems lead to
   good parametrizations"). Applied to pattern containment it gives the first-moment threshold
   `N = k²/e² + (k ln k)/e² + O(k)` (§B.3(a)), correctly *diagnoses* why this is wrong (the Poisson-paradigm
   hypothesis `S_2 → μ²/2` fails: copies cluster), and stops there; the correction mechanism the book uses for
   connectivity — count one canonical representative per cluster (spanning trees, p. 169) — is exactly W12's
   canonical copies, whose loss (`2.279` vs `2`) is the residual clustering of canonical copies. For "identity
   vs. random pattern" the book's tools give only the *ordering* heuristic already in W22 (heavier clustering
   `c_j ≈ j!` for the identity ⇒ more mass at `X = 0` at equal mean ⇒ identity harder at finite `k`), no
   constant. Its critical-window discipline does yield one useful negative statement: with the Tracy–Widom
   scaling the finite-size correction is `N_{1/2}/k² = c + a k^{−2/3} + …`, and with `k ≤ 32` the fitted `c`
   cannot distinguish `1/4` from `0.23` (§B.3(d)); so the W21 question is not decidable by more samples at
   these `k`.
4. *Large deviations / Poisson vs Gaussian / certificates.* Ch. 8 (pp. 103–113) is the standard Chernoff
   material with a clear statement of the three regimes (p. 106) and the block-superadditivity trick that turns
   an asymptotic tail rate into a bound valid for all `n` (Thm 5.7, p. 65). Relevance to speed-`N` tails:
   the exponent of a Chernoff bound is `(number of independent summands) × (per-summand rate)`, so speed `N`
   requires `N` (near-)independent coins — precisely what the Dilworth-cover certificate of W22 §B.8 provides
   and no copy-count functional does. Nothing here goes beyond W22 §B.8/§B.10. Certificate counting in the
   Moser sense is not in the book; the closest relatives are the injective-encoding count of Ch. 0 (pp. 1–3,
   the template of CKS/Lemma 1) and the "give ground: replace the event by a tractable sufficient certificate"
   principle of §10.2 (p. 130).
5. *Permutation statistics.* Only cycle counts (expected number of `k`-cycles `= 1/k`, p. 55). Cycle type is
   not a pattern invariant (it is not preserved by reverse/complement), so it cannot inform which patterns are
   hard. Dead.

**Ranked actions** are in §C, **dead ends** in §D.

---

## B. Technique by technique

### B.1 Stirling, the Laplace method, binomial asymptotics, and the tilt (Ch. 1, 3, 5, 8)

**Statements.**
- §1.1 (pp. 5–12): `n! = ∫ x^n e^{−x}dx`; "integrals are dominated by the largest value", "scaling is the art
  of asymptotic integration" (p. 7), the scaling `x = n + λ√n` (1.8), the split MID `= [−n^{1/8}, n^{1/8}]`,
  LEFT, NEARRIGHT, FARRIGHT with explicit inequalities (1.24)–(1.26) for `ln(1+ε)`; the two principles
  "crude upper bounds can be used for negligible terms as long as they stay negligible" and "terms that are
  extremely small often require quite a bit of work" (p. 13). §1.4 (pp. 18–20): pushing to `1 + 1/(12n)`.
- Ch. 3 (pp. 37–46): Gaussian tail `GT(a) ~ e^{−a²/2}/(a√2π)` (3.8) and Thm 3.1 ("the weight of the tail is
  all very close to `a`"); boundary maxima give `e^{−w}` rather than `e^{−w²/2}` (p. 37, §3.3).
- Ch. 5: `C(n,k)` for `k = o(√n)`, `k ~ c√n` ((5.8): `C(n,k) ~ (n^k/k!) e^{−c²/2}`), `k = o(n^{2/3})`
  ((5.9)), linear `k` ((5.31), entropy), the middle coefficient ((5.38)–(5.43)), the all-`n` bound
  `C(n,k) ≤ (ne/k)^k` (5.14), and **Thm 5.7 (p. 65)**: `Pr[Bin(n,½) ≥ pn] ≤ 2^{n(H(p)−1)}` for *all* `n`,
  proved from the asymptotic statement by blocks (`Pr[Bin(as,½) ≥ pas] ≥ Pr[Bin(a,½) ≥ pa]^s`).
- Ch. 8: Chernoff `Pr[X ≥ a] ≤ E e^{λX}/e^{λa}` (8.4) with "the key is the choice of `λ`" (p. 104); the
  three regimes (p. 106): small deviations (CLT), large deviations (`a → ∞`, `λ = a/σ → 0`, Gaussian tail
  `e^{−a²/2}` from the first two moments), **very large deviations (`a = Ω(σ)`, `λ` constant, "the later terms
  are no longer negligible … the calculation of optimal `λ` can be challenging")**; the Poisson example
  (8.13)–(8.19); heads-minus-tails (8.29)–(8.30): for `Pr[S_n ≥ bn]` the optimal `λ = tanh^{−1} b` "matches the
  correct asymptotics as given by (5.33)" (p. 109); Thm 8.4/8.5 (pp. 112–113) sufficient conditions for the
  Gaussian regime.

**(a) Our tilt is the book's Chernoff bound, and it is exponentially exact for Theorem A.** The sum
`Σ_{a: Σa = n+1} W(a)` with `W(a) = Π_j f(a_{2j−1} + a_{2j})` is the coefficient of `x^{n+1}` in
`(x/(1−x))² F(x)^{(k−1)/2}`, `F(x) = Σ x^{a+a'} f(a+a')`; inequality (2) of the paper is the Chernoff bound
`Pr[ΣA = n+1] ≤ x^{−(n+1)} E[x^{ΣA}]` for i.i.d. pair-sums under the tilted law, i.e. exactly (8.4)/(8.5)
with `λ = −ln x`. By the book's own analysis of this situation (Thm 5.7; (8.29)–(8.30); §1.1's Gaussian
window of width `Θ(√k)` around the saddle), the bound is off from the true coefficient by a factor
`Θ(√k)` only. Hence: **there is no sharper way to evaluate `Σ_T W(T)` for the weight of Theorem A**; the
rate `g(θ*,λ)` of (A′) is the exact exponential rate of that sum. Any further gain must come from a
different weight (a different encoding), not from the evaluation. This settles the first half of item (1).

**(b) Two-parameter tilts.** A second tilt would target a second additive constraint. The only other
quantity in Lemma 1 is `|I|`, through `k!/(k−|I|)! ≤ k^{|I|}`. Its exact size: `|I|/k → ½ Pr(B > θ) =
½(1+θ)e^{−θ} = 0.0026` at `θ = 7.37`, so `(k)_{|I|}/k^{|I|} = exp(−|I|²/2k + …)` costs `0.0026²/2 = 3.5·10^{−6}`
in the rate `g`, i.e. `Δλ ≈ 3.5·10^{−6}` (since `∂g/∂λ = θ/e² ≈ 1`). In Theorem C the factor
`k!/(k−r)!` is not used at all (slot counts replace it). **Two-parameter tilts have nothing to act on.**

**(c) The odd/even two-parity encoding.** Its exact rate (`1.000437`, transfer operator) is not a Laplace
method problem: the factors are 2-dependent and the sum is a matrix product, not a scalar power. The book has
nothing on transfer operators or Perron roots. What the book *does* supply is the template for the missing
routine step of Theorem B ("the routine geometric-to-exponential limit which we have not written out in
full"): §1.1's MID/LEFT/RIGHT split with Taylor remainders (Thm 2.18, p. 36) and the uniform error bound
(1.20)–(1.23). Worth citing if Theorem B is ever written out, not worth an action.

**(d) Exact large deviations for the slot count — the one real gain.** Theorem C bounds, for each dropped
window of width `b`, the count `S = Σ_{ℓ=1}^{b−2} X_ℓ` of value-slots hit, with `X_ℓ = 1[B ∩ A_ℓ ≠ ∅]`
independent Bernoulli(`p_ℓ`), `p_ℓ = 1 − x^{s_ℓ}`, `s_ℓ = |A_ℓ|`, `Σ s_ℓ ≤ n − b − 1` (W7 `proof.md`
Step 3b), by the Poisson-type Chernoff `Pr[S ≥ (1+ε)m] ≤ e^{−m h(ε)}`, `m = (b−2)p̄`,
`p̄ = 1 − x^{(n−b−1)/(b−2)}` (Step 4). At the optimum `β̄ = 0.594`, `τ = 0.977` the relevant windows have
`p̄ = 1 − e^{−τ/β'} ∈ [0.5, 0.85]`: the variance is `Σ p_ℓ(1−p_ℓ)`, far below the mean, and the Poisson bound
is in the wrong regime (p. 106: it uses only "`1 + ½a²`"; here `λ = ln(1+ε)` is a constant and the exact
Laplace transform must be used, p. 109).

*Lemma B.1 (uniform Bernoulli domination).* For `c > 0` and `x ∈ (0,1)` the function
`f(s) = ln(1 + c(1 − x^s))` is increasing and concave on `s ≥ 0`. Hence for every `λ > 0`,
`ln E e^{λS} = Σ_ℓ f(s_ℓ) ≤ (b−2) f((n−b−1)/(b−2)) = (b−2) ln(1 + (e^λ − 1) p̄)`, i.e. the Laplace transform
of `S` is dominated by that of `Bin(b−2, p̄)`, and therefore
```
Pr[ S ≥ (1+ε) m ]  ≤  exp( −(b−2) · D( (1+ε)p̄ ‖ p̄ ) ),    D(a‖p) = a ln(a/p) + (1−a) ln((1−a)/(1−p)),
```
for `(1+ε)p̄ ≤ 1`, and `Pr = 0` when `(1+ε)p̄ > 1` (then `(1+ε)m > b−2 ≥ S`).
*Proof of concavity.* With `u = x^s`, `f'(s) = c|ln x| · u/(1 + c − cu)`; `u ↦ u/(1+c−cu)` has derivative
`(1+c)/(1+c−cu)² > 0`, and `u = x^s` is decreasing in `s`, so `f'` is decreasing. Monotonicity in `s` is
clear; Jensen plus monotonicity give the displayed inequality (the total `Σ s_ℓ` may be smaller than
`n−b−1`). The tail bound is the standard optimisation of `e^{−λ(1+ε)m}(1 + (e^λ−1)p̄)^{b−2}` over `λ`,
which is (8.29)–(8.30) of the book for a biased coin. ∎

Everything else in Theorem C is unchanged: the bad term becomes
`e·n·q·Σ_{b ≥ β} P(b) exp(−(b−2) D((1+ε_b) p̄_b ‖ p̄_b))`. One consequence the paper must absorb: with a fixed
`ε` the Bernoulli rate `β' D((1+ε)p ‖ p)` (`β' = b/k`, `p = 1 − e^{−τ/β'}`) is *not* increasing in `β'`
(it tends to the Poisson value `ε²τ/2` for wide windows, where `p → 0`), so the minimum over widths is no
longer at `b = β`; the remedy is the width-dependent `ε(b)` of W7's `rate2.py` (flat bad exponent `R`),
which is what I computed.

*Numbers* (`rate_bernoulli2.py`; same limit formula as W7, same `R_good` with the `s`-maximisation, `c̄`
recomputed as the minimum over widths of `(1+ε(b)) m(b)/k`):

| bad-event bound | fixed `ε` | width-dependent `ε(b)` |
|---|---|---|
| Poisson `e^{−m h(ε)}` (paper) | `λ_C = 1.004829` (reproduced) | `1.005007` (reproduces W7's `1.00501`) |
| Bernoulli (Lemma B.1) | `1.007756` (invalid: min over widths not at `b = β`; listed for the record) | **`1.007338`** (`τ = 0.968`, `β̄ = 0.537`, `R = 0.0078`, `s = 0.10`) |

At the new optimum the threshold drops to `0.54k` and the effective slack at the narrowest dropped window is
`ε ≈ 0.07` instead of `0.149`. The remaining distance to the `ε = 0` ceiling `1.0117` is the good-factor cost
of `ε(b)` plus the `+j` accounting; the book has nothing further to say about either.

**(e) Small items.** "In Asymptopia `A + B` is well approximated by `max(A,B)`" (p. 99) and "sums are often
approximated by their largest term" (p. 139) are the paper's `max(R_good, R_bad)`. The Stirling-corrected
first moment of copies, `μ = C(n,k)/k! ~ λ^k e^{−e²/(2λ)}/(2πk)` by (5.8) with `c = e/√λ`, gives the
first-moment absence threshold `n = k²/e² + (k/e²)(ln 2πk + e²/2) + O(1)`: the trivial lower bound
`sp(k) ≥ k²/e² + (k ln k)/e²` — a lower-order term, but a clean one to quote.

### B.2 Erdős–Szekeres / LIS / Ulam (absent)

Checked: index entries (pp. 181–183) contain "random permutation, 54", "uniformly random permutation, 55",
"Sorting Game, 145", "Prisoners Game, 54"; no "increasing subsequence", "Erdős–Szekeres", "Ulam",
"Hammersley", "Tracy–Widom". The text confirms it. Related crumbs:
- Ch. 0 (pp. 1–3): "there are `n` values `Ψ(s)` and polylog many codes" — the injective-encoding count used
  by CKS and by our Lemma 1 (`pat_k(σ) ≤ #codes`). Same idea, older and simpler; no new leverage.
- p. 22 fn. 9 "tilt your head at a 45 degree angle": the `(x+y, x−y)` coordinates that make the two
  coordinates of the `Z²` walk independent — the same rotation that turns increasing chains into Hammersley
  space-time paths, but used here only to compute `p(2t) ~ 1/(πt)`.
- §11.5 (pp. 145–147): `T(n) ≥ lg n!` for sorting — the information-theoretic count `n! ≤ 2^q`. Our lower
  bound is the same inequality with `k! ≤ #codes`.
Nothing on `2√n`, so the brief's guess of an LIS chapter is simply wrong for this book.

### B.3 Thresholds: Erdős magic, deletion, LLL, critical windows, the Poisson paradigm (Ch. 7, §5.2, §12.2–12.4)

**Statements.** Thm 7.1 (p. 94) first moment `C(n,k) 2^{1−C(k,2)} < 1 ⇒ R(k,k) > n`, evaluated in §7.4
(pp. 96–98) to `(1+o(1)) k 2^{k/2}/(e√2)` — with the explicit warning "we could not estimate `C(k,2)` by
`k²/2` since it was in the exponent" (p. 97); Thm 7.2 deletion (`R(k,k) > m − C(m,k)2^{1−C(k,2)}`), gaining
`√2`; Thm 7.4 LLL, gaining `2`; the parametrisation discipline "`m = y n_0`, compare `f(m)` with `f(n_0)`"
(p. 97); §7.5 two-constraint optimisation (`p^{−1/2} = (1−p)^{−1}`, golden ratio, p. 99); §7.6
`R(3,l) = Ω(l^{3/2}/ln^{3/2} l)` by deletion + parametrisation. Ex. 5.4 (pp. 61–62): the critical window of
`Σ k²(n)_k p^{k+1}` is `p = 1/n − K n^{−4/3}` — found by locating where the truncation factor `A(n,k)` starts to
bite. §12.2.3 Thm 12.12 (pp. 162–164): if `S_k → μ^k/k!` for each fixed `k` then `Pr[no A_i] → e^{−μ}`
(proof via Bonferroni, Thm 12.11, p. 161; the "incorrect argument" warning, p. 162); Thm 12.13 Poisson
distribution; §12.3–12.4: coupon collector and `G(n,p)` connectivity at `p = (ln n + c)/n`, limit
`e^{−e^{−c}}`; Thm 12.16's proof counts non-isolated small components by spanning trees with the remark
"graphs for which `S` contains more than one tree are multiply counted, so we obtain an upper bound" (p. 169).

**(a) Naive first-moment threshold.** `μ(N) = E#copies = (1+o(1)) N^k/(k!)²` in the Poisson model (exactly
`C(n,k)/k!` for a uniform permutation). By Stirling `μ = (Ne²/k²)^k/(2πk)·(1+o(1))`, so `μ → 0` iff
`C < e^{−2}`: absence threshold `k²/e²` for *every* `π` (Thm 7.1 mechanism). This is the constant of the
trivial lower bound `sp(k) ≥ k²/e²`, and the book's treatment adds only the `k ln k` correction of §B.1(e).

**(b) The Poisson-paradigm test, and why it fails.** Thm 12.12 needs `S_2 = Σ_{I<J} Pr(B_I ∧ B_J) → μ²/2`,
i.e. `E X(X−1)/μ² → 1`. W22 §B.2 computed `E X²/μ² = 1 + Σ_j c_j(π) (k²/N)^j/j! + …`, which is `≥ e^{e²}·(…)`
at `C = e^{−2}` and `Θ(1) ≠ 1` at every `C = Θ(1)`. So the hypothesis of the paradigm fails by a constant
factor at every scale `N = Ck²`; the book's own "incorrect argument" remark (p. 162) is the right warning:
inclusion–exclusion does not converge here. **The correction mechanism is clustering**: the `Θ(μ²/C)` pairs of
copies sharing one point (W22 Prop. B.1) mean that copies come in clusters of size `e^{Θ(1/C)}` (identity:
`≈ 1/(C−1)`-type growth; random `π`: `e^{1/C} − 1`), and `X = 0` is not a Poisson zero event but a
large-deviation event of a clustered count.

**(c) What the book's methods predict for the true constant.** Honestly: nothing quantitative. The book has
two devices for going beyond the first moment — deletion (gain a constant factor by removing blemishes) and
counting one canonical representative per cluster (p. 169). Deletion is meaningless for containment (we want
copies to *exist*). The canonical-representative device is exactly W12's canonical copies: count the copies
that are minimal in a total order (`Σ x_r`), whose expected number is a single transfer-operator quantity
uniform in `π`, giving absence for `k > 2.279√N`; the residual factor `2.279/2` is the clustering *among
canonical copies*, which the book has no tool to remove. For the ordering "random `π` easier than the
identity at finite `k`", the book's paradigm gives the heuristic of W22 item 3 (at equal `μ`, heavier
clustering ⇒ larger `Pr(X=0)`; identity `c_j ≈ j!`, random `c_j ≈ 1`), nothing more. Our numerics
(identity `¼`-consistent, random `≈ 0.23`–`0.25`) are outside the reach of any Poisson-paradigm reasoning
because both events are speed-`N` (identity: Deuschel–Zeitouni) or at least speed-`≫ k` deviations.

**(d) The critical window (Ex. 5.4 discipline) — a negative but useful statement.** For the identity,
`LIS_n = 2√n + n^{1/6}χ`, `χ ~ TW₂` (median `≈ −1.27`), so `LIS < k` at the median when
`√n = k/2 + 0.635 n^{1/6}`, i.e. `n_{1/2}/k² = ¼ + 0.50 k^{−2/3} + O(k^{−1})`: the window has width
`Θ(k^{4/3})` and the leading finite-size correction is `k^{−2/3}` with coefficient `≈ 0.5`. The paper's data
(identity `0.405 … 0.339` for `k = 8 … 20`) fit `¼ + 0.63 k^{−2/3}` to within the next-order term; the random
data (`0.384 … 0.304`) fit `¼ + 0.40 k^{−2/3}` **and equally well** `0.23 + 0.55 k^{−2/3}`. With five or six
`k`-values in `[8, 32]` a two-parameter fit `c + a k^{−2/3}` determines `c` to `±0.02` at best, which is the
size of the effect. Conclusion in the book's spirit ("parametrise so that you can *see* the transition"):
the `¼` vs `0.23` question cannot be settled by more samples at `k ≤ 32`; it needs either a proof that the
correction exponent is `−2/3` for random `π` (then a one-parameter fit works) or `k ≈ 100`, where containment
testing for a random 100-pattern in a 2500-point set is infeasible. This closes the numerical route.

**(e) What the LLL / deletion chapters add for the union over `S_k`.** Nothing beyond W22 §B.6: Thm 7.3's
`4dp ≤ 1` needs weak dependence between the absence events `A_π`, which are all decreasing in the point set
and positively correlated; Thm 7.2's deletion has no containment analogue (see §D.4 for the deterministic
"random plus repair" version).

### B.4 Large deviations, Poisson vs Gaussian regimes, certificate-style counting (Ch. 8, Thm 5.7, §12.1, §10)

**Statements.** Beyond §B.1: (8.13)–(8.19) Poisson tails (`Pr[P_n ≥ n + √(10 n ln n)] ≤ n^{−49}`, the
"large deviation" regime); Thm 8.3 (p. 111) `Pr[|Bin − np| ≥ K√(n ln n)] = o(n^{−c})`; §12.1 LIL by Borel–
Cantelli + independent blocks + the reflection principle (Thm 12.8, p. 157) with the observation (p. 159)
that the `√2` comes from the knife-edge `Σ u^{−β}` at `β = 1`; §10.1 Heilbronn triangles by deletion
(Thm 10.2, pp. 127–128); §10.2 convex hull: `E#hull vertices = Θ(n^{1/3})` by "giving ground" to the
tractable sufficient condition "extremal" (p. 130) and the scaling `s = z n^{−2/3}` (10.16); §12.5.2
(pp. 171–172) longest chain in a random subset of a binary tree, `E = log* t + Θ(1)`, first moment on
descendant pairs for the upper bound.

**Relevance to speed-`N` tails.** The book's message is the one already used: the Chernoff exponent equals
(number of independent summands) × (per-summand rate at the optimal `λ`), and in the very-large-deviation
regime the optimal `λ` is a constant to be computed exactly (p. 106). So (i) any functional of `Π_N` that is
a sum of `N` independent-ish contributions has speed `N`; (ii) copy counts are not such sums (they are
degree-`k` polynomials, W22 §B.5), (iii) the Dilworth cover certificate turns `LIS < k` into a union over
`(k−1)^N` assignments of a product of `N` i.i.d. Bernoulli-type events, which is why it has speed `N`.
Thm 5.7's block trick (pp. 65) gives all-`n` validity of an asymptotic *upper-tail* rate for superadditive
quantities; for our `c_τ` lower bounds the analogous superadditivity (`L_τ(N) ≥ Σ` over diagonal blocks) is
Hammersley's argument and already in use (paper §Random); for the *lower* tail of `LIS` (absence) there is
no such block structure. The "give ground" principle of p. 130 is the abstract form of both W12 (canonical
copies as a tractable sub-event) and W22's certificate idea; it is a principle, not a technique.
**No new tool for the `k ln k`-per-pattern gap.**

**Poisson vs Gaussian for our counts.** For the copy count `X` at `N = Ck²` the deviation needed for `X = 0`
is the mean itself (`a = Ω(σ)` in the notation of p. 106): the "very large deviation" regime, where the
Gaussian paradigm (Thm 8.4) is inapplicable and one needs `E e^{−λX}` at constant `λ` — not computable for a
degree-`k` polynomial of indicators. Consistent with W22's caps; nothing new.

### B.5 Permutation statistics (§4.2.3, §11.5–11.6)

The prisoners game (pp. 54–55): expected number of `k`-cycles `= 1/k` by counting `(2n)_k/k` potential
cycles each realised with probability `1/(2n)_k`; the probability of a cycle longer than `n` in `S_{2n}` is
`H_{2n} − H_n → ln 2`. Cycle type is invariant under inverse but not under reverse or complement, while
containment is dihedral-equivariant, so no cycle statistic can be a proxy for hardness. The paper's hard
patterns (identity perturbed by adjacent transpositions, `(21)^{⊕k/2}`, block grids) are characterised by
their *point-set* geometry (few monotone runs, shift chains), not by cycles. Quicksort's `2n ln n` and the
sorting bound `lg n!` (pp. 146–150) are unrelated. **Empty for our purposes.**

### B.6 Other material scanned for relevance

- Ch. 6 Prüfer codes / Cayley `r n^{n−r−1}` (pp. 72–88) and unicyclic count `~ √(π/8) n^{n−1/2}` (Thm 6.6):
  bijective encodings; the only echo is that `√(π/8)` also appears as our corner-greedy threshold
  `π/8` (Thm 10) — a coincidence of Gaussian integrals, not a connection.
- Ch. 9 primes (pp. 115–124): the "small primes contribute `2^{2n/K}`, large primes are counted exactly" split
  of §9.4 (p. 121) is the same accounting as our staircase/global-event splits; no transfer.
- Ch. 11 recurrences (Thm 11.1, p. 139): low/just-right/high overhead regimes — irrelevant.
- §12.5 tower/log*: irrelevant.

---

## C. Ranked actions

1. **Adopt the exact Bernoulli tail in Theorem C (rigorous, cheap, ≈ +50 % on the excess).**
   (a) Verify Lemma B.1 line by line (monotone + concave `f`, Jensen with `Σ s_ℓ ≤ n−b−1`, Cramér for
   `Bin(b−2, p̄)`; the zero-probability case `(1+ε)p̄ > 1`). (b) Replace Step 4 of `w7-slots/proof.md` and the
   `Bad` term of Theorem C by `e·n·q·Σ_{b≥β} P(b) exp(−(b−2)D((1+ε_b)p̄_b ‖ p̄_b))` with width-dependent
   `ε_b` (flat exponent), and note that the bad rate is then `−R` by construction (no monotonicity in `b`
   needed). (c) Recompute the limit root independently of my `rate_bernoulli2.py` (it reuses W7's `R_good`
   and reproduces both `1.004829` and `1.005007` in Poisson mode, so the only new ingredient is the bad term)
   and rerun `finite_check.py` at `k = 3·10^4, 10^5` with the new bad term. Expected outcome: `λ_C ≈ 1.0073`
   (paper: "`≈ 96×` CKS"). (d) Optional: since `p̄_b` now matters, check whether a *lower* threshold `β̄`
   combined with the cap `min(·, k)` changes the `s`-maximisation; my run keeps W7's form.
2. **Write the first-moment threshold with its `k ln k` term into the paper's introduction** (one line,
   §B.1(e)): `sp(k) ≥ k²/e² + (k ln k)/e² + O(k)` from `C(n,k) ~ (n^k/k!) e^{−e²/2λ}` ((5.8), p. 58). Cosmetic
   but exact and currently absent.
3. **Stop the W21 numerical route to "`¼` vs `0.23`" and reformulate it** (§B.3(d)): record in the paper that
   the Tracy–Widom scaling makes the finite-size correction `Θ(k^{−2/3})` with coefficient `≈ 0.5–0.65`, so
   that `k ≤ 32` cannot separate the two limits; what *can* be tested at these `k` is the *exponent* of the
   correction for random `π` (fit `log(n_{1/2}/k² − ¼)` against `log k`: slope `−2/3` supports a common limit
   `¼` with TW-type fluctuations; a slope near `0` or a poor fit supports a different limit). This is a
   re-analysis of existing W21 data, no new runs.
4. **(Low priority) Theorem A's `(k)_r` versus `k^r`**: keeping `k!/(k−|I|)!` exactly gains `Δλ ≈ 3.5·10^{−6}`
   (§B.1(b)). Not worth touching the Lean proof; mention in the paper's "further refinements" only if the
   Bernoulli improvement is adopted and the section is rewritten anyway.

## D. Dead ends (with reasons)

1. **Sharper evaluation of `Σ_T W(T)` for Theorem A by any Laplace/saddle-point refinement.** The tilt bound
   is exponentially exact for i.i.d. pair weights (Thm 5.7 / (8.29)–(8.30) logic); only `Θ(√k)` is lost.
2. **Two-parameter tilts.** No second additive constraint with non-negligible entropy (`|I|/k = 0.0026`;
   `Δλ ≈ 3.5·10^{−6}`).
3. **LIS / Ulam / Hammersley / Erdős–Szekeres material.** Not in the book.
4. **Alteration ("random plus repair") for a deterministic superpattern below `k²/2`** — the book's signature
   technique (Thm 7.2, Thm 10.2). Take a random `σ` of length `n` and insert one copy (`k` points) of each
   missing pattern: `sp(k) ≤ n + k·E#missing`. To beat `k²/2` one needs `n ≤ 0.49k²` and `E#missing ≤ 0.01k`,
   i.e. a per-pattern failure `≤ 10^{−2}/(k·k!)` at `n = 0.49k²` — the same `e^{−k ln k}` per pattern that the
   union bound needs, which no known method delivers below `k² ln k` (Thm 11: `e^{−ηk}` at `0.757k²`).
5. **Poisson paradigm / Bonferroni for the copy count at any `N = Ck²`.** Fails by a constant factor
   (`E X²/μ² ≠ 1`, W22 §B.2); inclusion–exclusion does not converge (p. 162 warning).
6. **Deletion, LLL, first moment for the true containment constant.** They locate `k²/e²` and cannot see the
   clustering correction; the book's canonical-representative device is W12, already at its limit (`2.279`).
7. **Deciding `¼` vs `0.23` by more samples at `k ≤ 32`.** Window scaling `k^{4/3}` with coefficient
   `≈ 0.5` makes the two hypotheses indistinguishable at these `k` (§B.3(d)).
8. **Cycle/fixed-point statistics as a hardness proxy.** Not dihedral-invariant.
9. **Thm 5.7's block trick for the lower tail of `LIS` (absence).** Absence in the square does not factor
   over blocks; only upper tails of superadditive functionals benefit (already Hammersley).
10. **Gaussian-regime Chernoff (Thm 8.4/8.5) for `Pr(X = 0)`.** The required deviation equals the mean; this is
    the very-large-deviation regime where the full Laplace transform of a degree-`k` polynomial would be
    needed.

Files: `rate_bernoulli.py`/`.out` (fixed-`ε` comparison, Poisson root `1.004829` reproduced; Bernoulli
fixed-`ε` value `1.007756` is *not* valid, see §B.1(d)), `rate_bernoulli2.py`/`.out` (width-dependent `ε`:
Poisson `1.005007` = W7's `rate2.py`; Bernoulli **`1.007338`**), `log.md`.
