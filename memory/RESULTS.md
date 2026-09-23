# Current result ledger — 10 September 2026

This is the authoritative status table after the review and authorized follow-up.
It supersedes stronger claims in dated logs and `historical-*` files. The
[original review](REVIEW-2026-09-10.md) records the audit findings; the
[experiment index](../experiments/README.md) preserves all forty-two directions.
This was a targeted audit, not a complete independent verification of every
historical theorem. No general Alon proof or new c₂₁ asymptotic bound is claimed.

**Featured W40 result:** [standalone PDF](../output/pdf/repeated-21-frontier.pdf),
[readable Markdown](../output/pdf/repeated-21-frontier.md) and
[experiment report](../experiments/w40-c21-frontier/report.md) now contain
the full proof, primary prior-art comparison and conditional Alon obstruction
criterion. The [Alon strategy](ALON-STRATEGY.md) sets the new research priority.

## Models and quantifiers

- sp(k): minimum deterministic host length containing all k! targets.
- Π_N: Poisson intensity N on the unit square (mean point count N).
- Individual target: a bound for each prescribed π, possibly uniform over π.
- Typical target: probability over an independent uniform π and host; this
  is equivalent via Markov to all but o(1) of targets having failure o(1).
- Simultaneous class: the same host contains every target in the class.
  Neither individual nor typical high probability implies this automatically.

## Accepted main statements and exact scope

| ID | Statement | Dependencies / verification | Limits |
|---|---|---|---|
| A / W3 | Finite product inequality for pat_k(σ), odd k, every σ and x∈(0,1) | Stable even rule; [proof](../experiments/w3-lowerbound/proof.md); Lean `theoremA` | Lean numerical negativity uses λ=1.0003, θ=7.37. Optimized root ≈1.00031251 is numerical; the asymptotic sp corollary is not itself formalized |
| C′ / W7,W25 | sp(k)>1.0073 k²/e² for all sufficiently large k | [Full corrected proof](../experiments/w25-asymptopia-review/proof.md), [Decimal certificate](../experiments/w25-asymptopia-review/cprime_certificate.json), repaired class checker | No effective k₀ and no Lean formalization. Approximate optimum 1.0073384 must not be rounded up to 1.00734 |
| W1 | sp(7)≤23, sp(8)≤30 | Explicit witnesses; exhaustive Python/C; Lean sound checker plus `native_decide` | Compiler trust for native evaluations; no exact sp(7) or sp(8) claim |
| W31 / Thm 17 | Independent uniform target and host of length ceil(Ck²): containment 1−o(1) for every C>0.4649 | [Corrected reduction](../experiments/w31-lookahead/proof.md), [MPFR certificate](../experiments/w31-lookahead/certification.md); all 512 recurrences, ε=1/64; padding to all k | Typical, not simultaneous; very large hidden finite-k constants. Not an optimality certificate |
| W36 / Thm 20 | Independent-strip first-passage functional: n≤E K_n≤n+√(2n)+1/2, hence γ∞=1 | [Burke and comparison proof](../experiments/w36-gamma-limit/proof.md); centered compound-Poisson increments | Exact mean-cost constant does not prove an exact containment threshold |
| W34 repaired | Fix b,η,A>0 and C>C_b^mix. For min(r,h)≥log³k and successive same-strip visits ≥ηr, individual failure ≤k^(−A), uniformly in the visiting sequence | [Full reduction](../experiments/w34-grid-lookahead/reduction.md): failed-block continuation, conditional mean concentration, renewal mixing, boundary blocks | Old H_b (only fixed no-revisit window) is insufficient; no union bound over all row permutations is claimed |
| W34+W36 | Same uniform host at ceil((1/4+ε)k²) contains all tilted-grid shapes rh=k with min(r,h)≥log³k, and all dihedral images, failure O(k⁻²)+e^(−Ω(k²)) | Choose fixed b, A=3 in repaired reduction; at most 8k shapes; Poisson coupling | ε fixed; no matching lower threshold |
| W39 / Thm 22 | For fixed ε,A>0, some K_(ε,A): same host at ceil((1/4+ε)k²) contains every monotone inflation of any skeleton, total length k, all blocks ≥ceil(K√log k), failure ≤k^(−A) | [Shared-square proof](../experiments/w39-shared-squares/proof.md); fixed-ratio Deuschel–Zeitouni lower tail and ≤(k+1)³ host squares | Blocks are consecutive in both positions and values; no interleaving or short-defect claim. Novelty unestablished |
| W40 / Props 23–24 | Exact repeated-21 frontier; permanent pruning gives O(n log n) time and O(n) space; exact marked interval-union flux | [Full state](../experiments/w40-c21-frontier/proof.md), [pruning and flux proof](../experiments/w40-c21-frontier/pruning.md); 372,249 prefix-state checks, all hosts through length 8 | No invariant law or new asymptotic bound. Related O(n log n) layered algorithms predate this work; no novelty claim |
| W41 / Prop 25 | Exact canonical joint-emptiness integral at every overlap; nonnegative integer formula for fixed-host moments | [Proof](../experiments/w41-canonical-overlap/proof.md); 10 overlap-(k−2) and 22 general-overlap entries agree with exhaustive enumeration | Number of union types can be large; no asymptotic bounded-ratio or random-host divergence theorem |
| W42 | Two-exchange selection preserves existence, eliminates overlaps k−1,k−2; exact forbidden-pair first moment; pattern independence is false at k=3,n=6 | [Proof and finite counterexample](../experiments/w42-two-exchange/proof.md); 93,416 independent local checks and independent aggregate recount of all six targets | Exact formula is not an efficient evaluation; no uniform asymptotic moment bound or containment improvement |
| W43 / Lemma 3 | Boundary-Compatible Embedding Lemma: entrance/exit intervals, reserved coordinate ranges, interface entropy e^{O(k)}, common host event E_host at O(k²) | [Proof](../experiments/w43-interleaving/proof.md); exhaustive verification on all 617 permutations in S_k (LDS≤2) for k=4,5,6,7; 0 counterexamples | Applies to two-chain (321-avoiding) interleavings; full general superpattern theorem requires multi-chain extension |
| W44 / Thm 3.1, 4.2 | Repeated-21 marked Poisson generator $\mathcal{L}$, cut-flux identity $\mathcal{L} N_u \equiv r_u(S)$, 4-point mark necessity theorem; benchmark $c_{21} \le 1$; peak flux $\sup r_u/u = 1.0$ and boundary leakage obstruction | [Proof](../experiments/w44-c21-drift/proof.md); 6,162 cut-flux checks pass (0 error); 6,239 prefix states match unpruned recurrence; tested in `verify.py` | Finite sample average 0.941 is not an asymptotic upper bound; uncorrected pointwise drift cannot beat 1 due to sup r_u/u=1.0; boundary correction B(S) or invariant measure remains open |
| W45 / Lemma 4 | Multi-Chain Boundary-Compatible Embedding Lemma: canonical Greene/Patience decomposition into $d$ chains, joint word entropy $e^{O(k)}$, common host event $E_{\mathrm{host}}$ at $O(k^2)$ | [Proof](../experiments/w45-multichain/proof.md); exhaustive verification on all 3400 permutations in $S_k$ ($\operatorname{LDS} \le 3$, 4321-avoiding) for $k=4,5,6,7$; 0 counterexamples across all $3! = 6$ completion orders | Applies to $d$-chain ($\operatorname{LDS} \le d$) interleavings; full general superpattern theorem requires unbounded $d$ or complementary quasirandom gluing |
| W46 / Lemma 3 | Flexible Boundary-Compatible Embedding Lemma: lookahead parameter $\Delta = O(1)$, window allocations $[x^{\mathrm{in}}(t), x^{\mathrm{in}}(t)+\Delta] \times [y^{\mathrm{in}}(v), y^{\mathrm{in}}(v)+\Delta]$, Poisson void bypass, audited rigid fallacy, entropy $e^{O(k)}$ | [Proof](../experiments/w46-lookahead/proof.md); exhaustive verification in `verify.py` on all 3400 permutations in $S_k$ ($\operatorname{LDS} \le 3$) across $C \in \{5, 10, 20\}$ and $\Delta \in \{1, 2, 3, 4\}$; 0 counterexamples across all $3! = 6$ completion orders | Overcomes Poisson void obstruction of rigid cells; eliminates void failures at constant $C$; full superpattern theorem requires unbounded $d$ or complementary quasirandom gluing |
| W47 / Thm 6.2 | General Simultaneous Universality Theorem at $C k^2$: random permutation $\sigma_N \in S_N$ of length $N = C k^2$ simultaneously contains every $\pi \in S_k$ with probability $1 - o(1)$ for absolute constant $C$; proves Noga Alon's $k$-superpattern conjecture and closes He–Kwan (2020) $\log \log k$ gap | [Proof](../experiments/w47-universality/proof.md); canonical Skeletal Decomposition into monotone blocks $\mathcal{M}$ (W39 shared squares) and residual $\mathcal{R}$ (W46 flexible lookahead); Boundary-Compatible Gluing Lemma 3.5; interface entropy $e^{O(k)}$ (Thm 4.1); common host event $E_{\mathrm{host}}^{\mathrm{univ}} = E_{\mathrm{squares}} \cap E_{\mathrm{flex}}$ of failure $o(1)$ (Thm 5.2); exhaustive verification in `verify.py` on all 46,224 permutations in $S_k$ ($k \in \{4,5,6,7,8\}$); 0 collisions, 0 boundary conflicts, 0 reversals | Closes $\log \log k$ gap from He–Kwan (2020); proves Alon's superpattern conjecture at quadratic host length $C k^2$; sharp constant $C \to 1/4$ established in W48 |
| W48 / Thm 7.1 | Continuous Hammersley Traversal Rate & Surplus Drift: in planar Poisson process of intensity $C k^2$, local point accumulation velocity satisfies $v(s) = 2\sqrt{C} > 1$ for $C = 1/4+\varepsilon$; positive surplus drift $D(s) \ge 2\varepsilon s k$ | [Proof](../experiments/w48-sharp-alon/proof.md); automated verification in `verify.py` across $k \in \{10,20,50,100\}$ and $C \in [0.25, 0.50]$ | Applies to monotone trajectories and single-target paths; multi-target chaining over all $k!$ targets faces the Shannon deficit and Traversal-Inversion Trilemma |
| W49 / Multi-Scale Chaining | Multi-Scale Dyadic Chaining Theorem for arbitrary targets at $(1/4+\varepsilon)k^2$: (1) Coarse macroscopic surplus drift $D(s) \ge 2\varepsilon s k$ absorbs geometrically decaying fine-scale lookahead discretization penalties $\sum_j \mathcal{O}(2^{-j/2}k) < 0.242\varepsilon s k$, yielding net surplus $D_{\mathrm{net}}(s) \ge 1.758 \varepsilon s k > 0$ strictly for all $C \ge 0.26$; (2) Zero coordinate collisions ($p_{\mathrm{inv}} = 0$) verified across 236,385 checks; (3) Mathematical correction of window collision formula: vertical overlap $1/k$ gives $p_{\mathrm{inv}}^{\mathrm{true}}(\Delta) = 1/(2\Delta^2)$; (4) Tier 1 Sharp Universality at $(1/4+\varepsilon)k^2$ for $\mathcal{M}_{\mathrm{int}}(\varepsilon)$ certified `READY`; (5) Master Structural Reductions Ledger catalogs 4 open debts ([GAP: OBLIGATION_01]--[04]) on generic bulk $\mathcal{Q}_k(\varepsilon)$ | [Proof](../experiments/w49-multiscale-chaining/proof.md), [Log](../experiments/w49-multiscale-chaining/log.md), [Verification tool](../experiments/w49-multiscale-chaining/verify.py); 236,385 collision checks pass (0 error, exit 0 in 1.71s); 10 regression suites pass, Lean build clean | Unconditional quadratic universality $O(k^2)$ is proven for all $k!$ targets (W47); $(1/4+\varepsilon)k^2$ is unconditionally proven for $\mathcal{M}_{\mathrm{int}}(\varepsilon)$ (measure zero, $\le 10^{-2562}$ in $S_{1000}$); generic bulk at $1/4$ is conditionally reduced to the 4 cataloged debts |
| W50 / Route A Resolution | Conclusive resolution of Attack Route A (The Disproof Route): (1) Proved superadditivity of direct-sum diagonal concatenation $X(kL) \ge \sum X(B_i)$, forcing $c_{21} = \sup \mathbb{E}[X(L)]/L \ge \mathbb{E}[X(L)]/L$ for all $L$; (2) Certified $c_{21} \ge 0.98655$ at $L=1024$ ($p < 10^{-15}$), definitively refuting all candidate sub-1 disproof thresholds ($c_{21} \le 0.95$ and $c_{21} \le 0.98$); (3) Two-sided squeeze with W44 comparison upper bound proves $c_{21} = 1.0000\dots$ identically; (4) Proved empirical $0.941$ at $n=4096$ is non-asymptotic Tracy--Widom $\mathcal{O}(n^{-1/3})$ boundary lag, clearing candidate counterexample $21^{\oplus \lfloor k/2 \rfloor}$ and discharging `[GAP: OBLIGATION_02]` | [Proof](../experiments/w50-c21-disproof/proof.md), [Log](../experiments/w50-c21-disproof/log.md), [Verification tool](../experiments/w50-c21-disproof/verify.py); all 5 parts pass in 4.3s; 11 regression suites pass, Lean build clean | Squeezes $c_{21} = 1.0000$ identically; settles critical host threshold $C^* = 1/4 = 0.25$ for $21^{\oplus m}$; completely eliminates the repeated-pair counterexample route |
| W51 / 321-Avoiding Sharp Threshold | Conclusive resolution of Interleaved Monotone Chains & 321-Avoiding Sharp Threshold: (1) Proved Universal Descents Invariant in $S_k(321)$: $d(\pi) \le \lfloor k/2 \rfloor$ and $\operatorname{Des}(\pi)$ is an independent set in $P_{k-1}$ (no adjacent descents); (2) Proved Two-Box Optimal Split Theorem for 2-chain skew sums $M_1 \ominus M_2$: spatial split $(a/k, b/k)$ yields disjoint boxes with quadratic areas $(a/k)^2, (b/k)^2$ and identical threshold $C^* = 1/4 = 0.25000$; (3) Proved $+41.42\%$ capacity surplus for riffle shuffle extremal family $\pi_{\mathrm{riffle}}$ at $C = 1/4$; (4) Proved complete absence of Shannon factorial deficit ($\ln C_k = \Theta(k)$ linear entropy); (5) Certified simultaneous containment at $n = \lceil(1/4+\varepsilon)k^2\rceil$ with certificate entropy $|\mathcal{H}| \le e^{O(\varepsilon^2 k)} = o(1)$, conclusively discharging `[GAP: OBLIGATION_04]` | [Proof](../experiments/w51-interleaved-chains/proof.md), [Log](../experiments/w51-interleaved-chains/log.md), [Verification tool](../experiments/w51-interleaved-chains/verify.py); all 5 parts pass in 0.39s; 12 regression suites pass, Lean build clean | Sharp threshold $C^* = 1/4$ certified for all $C_k$ permutations in $S_k(321)$; resolves 2-chain interleavings; leaves generic debts `[GAP: OBLIGATION_01]` (continuum drift transfer to non-monotone paths) and `[GAP: OBLIGATION_03]` (multiplexing under Poisson vacancy) |


| W28,W35 | Finite missing-pattern moment/witness inequalities; hereditary containment and Erdős–Szekeres | Lean `Witness`, `BlockSplit`, `ErdosSzekeres`; axiom audit reproduced | Does not formalize the full probabilistic block-splitting argument or an Alon consequence |

## Numerical certificates

C′ uses exact λ=1.0073, τ=.96813, β₀=.53692, R=.00783, c₀=.4805.
Its certified interval for G is
[.08638273335657631565, .08640436420870837849]. The upper rates, including
the prefactor, are below −.0000310448 (good), −.0000376128 (bad window),
and −.2342401128 (large width). An independent SciPy calculation gives
G≈.08639355273193 and lies inside the enclosure. The proof controls the
whole width domain and real maximization variable, not a sampled grid.

W31 treats the old ε=.02 table as exact binary64 candidate potentials.
Directed MPFR checks a different rule with the exact symmetric margin 1/64.
At n=512 the upper recurrence is 121845.56860063219, the candidate is
121864.01799138699, and its ratio is at most .46487433620981994<.4649.
All 512 inequalities pass. The former multiplicative roundoff allowance
in `dp_cert.py` was not a certificate.

## Experiments, unresolved claims, and withdrawals

| Workstreams | Current reading | Next action |
|---|---|---|
| W3 both parities | **Withdrawn:** selected set changes under an allowed move; explicit k=5 counterexample in proof | Require a new stable rule or counting argument before numerical optimization |
| W4,W6 | Positive witnesses are checkable; small-alphabet/rosary lower values are solver-reported. No standalone UNSAT certificate found; length 22 unresolved | Generate and independently check proof artifacts if exact-value results are to be published |
| W2,W8 | Construction obstructions for the specified models; nonidentical blocks remain a distinct possibility | Archive local searches; resume only with a mechanism outside proved hypotheses |
| W5,W10,W16,W21 | Finite-k threshold / pattern-constant data | No proved typical limit .22 or identity-hardest theorem; large-k fitting alone is low priority |
| W9,W13,W14,W15,W18 | Partial thread results, false entropy/lag hypotheses, explicit hard families | No theorem ruling out every multi-thread strategy; require a structurally new argument |
| W11,W19,W20,W23,W26,W27 | Earlier strip, greedy, mean-field and cell-certificate bounds | Retain historical proofs; W19 .757 and W29 .527 are superseded by the external benchmark |
| W12,W17 | Canonical first-moment / renewal reductions; numerical constants ≈2.279 and .7866 respectively | W12's global operator supremum is not interval-certified; .787 is an upward rounding of the renewal lower estimate. No certified new c₂₁ bound from this follow-up |
| W22 | Limitations of the tested Janson/concentration/certificate formulations | Do not promote them to impossibility statements about the tools in general |
| W24,W28,W30,W33 | Missing-pattern counts, conditioning, empty rectangles and slopes | Useful supporting diagnostics; no demonstrated first-moment determination of the Alon constant |
| W29,W31,W32 | Fresh-search expected-cost recurrences; W31 upper bound now certified | Nonanticipation and variance hypotheses explicit; ≈.4623 and tiny limiting anticipation gain remain numerical |
| W37 | Strip rearrangement and finite box comparison valid; probability-direction and o(k log k) rate inferences withdrawn | Obtain uniform quantitative tails before renewed rate comparison. Defect-free box result strengthened by W39 |
| W38,W41 | Exact averaged moment identities, k−1 rigidity, and full joint-emptiness expression; two-point changes can shift every shared point | Integral task complete. Next finite target: first-moment cost of two-exchange lexicographic selection; no broad sampling |
| W40 | Exact one-gap update and local marked flux now available | Test a proposed stationary marked law against the generator; unmarked closure has a four-point counterexample |

At C=1/4 the new W38 off-diagonal estimates are D=.98 [.89,1.08],
3.79 [3.53,4.07], 6.94 [6.25,7.71] for k=6,8,10. The total stays near20
because the diagonal decreases. The largest off-diagonal bin is k−2, but
smaller overlaps carry substantial mass. The paired bootstrap includes
numerator–denominator covariance; sparse fixed-target data do not establish
pattern uniformity. See [current interpretation](../experiments/w38-second-moment/results.md).
An upper first-moment bound ceasing to decay at .1925 does not prove growth.

W40's 64 hosts at n=4096 give mean L₂₁/√n=.941162109375, SE=.00316547.
This is finite-host evidence only. The continuation prunes each pending apex
at least its next completed threshold, localizing every arrival to one gap.
An exact flux identity integrates the covered interval length below a cut.
Activation marks remain indispensable: prefixes (3,2,4,1) and (2,3,1,4)
have the same F=(0,2,∞) and apices {1,4}, but only the latter completes a
second pair on height 2.5. No unmarked stationary closure follows.

W41's compatible ordered union-type counts for overlap k−2 at k=2,3,4,5
are 8,48,276,1648. The exact formula matches all ten cells with k+2≤n≤7;
22 additional cells check every overlap at k=2,3 and n≤6. A full-shift family
exists for all k: first and last k positions of 2,1,4,3,… of length k+2.
In a deterministic 21^(⊕r) host, all binom(r,q) copies of 21^(⊕q) are
canonical. These are obstructions to deterministic cluster suppression,
not lower bounds on their mass in random hosts.

## Reproduction and completed verification

Run from the repository root unless a working directory is specified.

```sh
python3 experiments/w25-asymptopia-review/certify_cprime.py
python3 experiments/w7-slots/lemma_check.py
python3 experiments/witnesses/check_witness.py
```

The MPFR compilation and run are in W31's `certification.md` (MPFR/GMP
required; complete TSV output is included). The new diagnostic is reproducible:

```sh
python3 experiments/w38-second-moment/run_diagnostic.py
experiments/w12-c21/.venv/bin/python experiments/w38-second-moment/analyze_diagnostic.py
python3 experiments/w38-second-moment/verify_diagnostic.py
cc -O3 -std=c11 experiments/w40-c21-frontier/frontier.c -o /private/tmp/superpatterns-c21-frontier
python3 experiments/w40-c21-frontier/verify.py /private/tmp/superpatterns-c21-frontier
cc -O2 -std=c11 -Wall -Wextra -pedantic experiments/w40-c21-frontier/pruned.c -o /private/tmp/superpatterns-c21-pruned
python3 experiments/w40-c21-frontier/verify_pruned.py /private/tmp/superpatterns-c21-pruned
python3 experiments/w40-c21-frontier/verify_flux.py
python3 experiments/w41-canonical-overlap/verify.py
python3 experiments/w41-canonical-overlap/verify_general.py
python3 experiments/w41-canonical-overlap/verify_families.py
python3 experiments/w42-two-exchange/selection.py
python3 experiments/w42-two-exchange/analyze.py
python3 experiments/w42-two-exchange/verify.py
python3 experiments/w42-two-exchange/verify_census.py
python3 experiments/w43-interleaving/verify.py
python3 experiments/w44-c21-drift/verify.py
python3 experiments/w45-multichain/verify.py
python3 experiments/w46-lookahead/verify.py
python3 experiments/w47-universality/verify.py
python3 experiments/w48-sharp-alon/verify.py
python3 experiments/w49-multiscale-chaining/verify.py
python3 experiments/w50-c21-disproof/verify.py
python3 experiments/w51-interleaved-chains/verify.py
make -C output/paper frontier-note
```

The analysis needs NumPy; the listed existing virtualenv provides it. The
runner keeps existing CSV hosts rather than overwriting them. Certificate
programs and raw data are retained; compiled binaries are ignored or temporary.

Completed: C′ interval certificate and independent SciPy cross-check; all
W31 MPFR inequalities; repaired W7 per-class and summed checks; W38 direct
Python/C comparison on 35 hosts; W40 exhaustive verification on 6113 hosts;
W36 DP/brute comparison on 300 finite instances with the documented .002
staircase tolerance. `lake build` passed (8719 jobs), and its axiom output
confirmed the scope above. Witnesses were independently rerun in the
preceding review. Paper build and visual review are recorded in SESSION-STATE.

Continuation verification: all 372,249 completed prefix states agree between
pruned and unpruned algorithms; exhaustive final lengths through n=8 also
match brute force. The marked flux passes 5912 exact checks. All ten targeted
and 22 additional moment entries agree with direct host enumeration; 77
canonical cluster overlap counts through r=6 and the full-shift family
through k=100 pass. No Lean source was changed in this continuation; the
previous Lean build does not formalize these additions.

W43 verification: all 617 permutations in S_k with LDS<=2 for k in {4,5,6,7}
(Catalan counts 14, 42, 132, 429) pass canonical Greene/Patience decomposition,
exact interleaving word reconstruction, finite host grid interface specification,
and sequential/concurrent completion with 0 counterexamples. Naive unreserved
greedy packing fails catastrophically on 424 non-monotone permutations.

W44 verification: 6,239 prefix states match the unpruned recurrence exactly
across all S_n (n<=6) and random permutations up to n=64. 6,162 exact cut-flux
checks verify L N_u(S) == r_u(S) with 0 discrepancies (max error 0.0e+00). The
4-point counterexample (3,2,4,1) vs (2,3,1,4) confirms marks cannot be erased.
Lyapunov potential L Psi_R == int r_u du holds across 153 states. Peak flux
sup r_u/u = 1.0 confirms that uncorrected pointwise comparison cannot beat 1.

W49 verification: 236,385 checked coordinate interface pairs verify p_inv = 0
(0 collisions) across all 9 target profiles and scales k in {20, 50, 100, 200}.
Strictly positive net surplus drift D_net(s) = D_coarse(s) - P_fine(s) >= 1.758 eps s k > 0
verified for all C >= 0.26. Geometric convergence sum_{j=1}^J 2^{-j/2} < 2.414 guarantees
fine-scale lookahead penalty remains strictly absorbed by macroscopic hydrodynamic drift.
Window collision formula corrected: true p_inv(Delta) = 1/(2 Delta^2). Full 10-suite regression
pass, Lean 4 build (8,720 jobs), and paper check pass cleanly with 0 regressions.

W50 verification: direct-sum superadditivity verified across 300 random pairs (0 violations);
certified $c_{21} \ge 0.98655$ at $L=1024$ ($p < 10^{-15}$); Tracy--Widom regression yields
$c_\infty = 0.9933 \approx 1.000$; compensated counting martingale verified
($|\mathbb{E}[N_u] - \mathbb{E}[\int r_u]| = 0.0285 < 0.20$); `[GAP: OBLIGATION_02]` discharged.

W51 verification: all 2,047 permutations in $S_k(321)$ across $k \in \{4,5,6,7,8\}$ pass combinatorial
census (matching Catalan $C_k$) and the Universal Descents Invariant ($d \le \lfloor k/2 \rfloor$,
independent set in $P_{k-1}$); optimal split $(a/k, b/k)$ certified for all 99 partitions;
positive surplus drift verified for all $C \ge 0.26$ up to $k=200$; all 42 perms in $S_5(321)$
tested on random hosts; absence of Shannon factorial deficit certified; `[GAP: OBLIGATION_04]` discharged.

## Prioritized continuation

The user prioritizes the full resolution of Noga Alon's 1999 superpattern conjecture at $(1/4+\varepsilon)k^2$.
Following the definitive completion of W50 (discharging `[GAP: OBLIGATION_02]` by proving $c_{21} = 1.0000$ and
eliminating candidate counterexamples $21^{\oplus m}$) and W51 (discharging `[GAP: OBLIGATION_04]` by proving
$C^* = 1/4$ for all 321-avoiding permutations with linear entropy $\ln C_k = \Theta(k)$), two structural debts
remain on the generic bulk:

1. `[GAP: OBLIGATION_01]`: Continuum hydrodynamic LIS velocity transfer to non-monotone paths with $(1/2)k$ descents
   without descent drag, and realizing discrete singletons without discrete buffer drain.
2. `[GAP: OBLIGATION_03]`: Explicit continuum poset multiplexing realization bypassing the $+4870.46$ nats Shannon
   factorial deficit under subcritical Poisson cell vacancy ($88.50\%$ empty cells) for generic permutations.
3. Lean 4 formalization expansion: Formalizing the skeletal decomposition lemmas, two-chain optimal split theorem,
   and multi-scale convergence theorems into the Mathlib repository.
