# Experiments / workstreams

Current index after the 10 September 2026 review and follow-up. See the
[authoritative ledger](../memory/RESULTS.md) for exact quantifiers,
certificate status and the next research queue. `log.md` preserves chronology;
`proof.md` gives the current argument where reviewed. Files marked historical
may contain withdrawn claims and must not be used as current proof status.

**Featured report:** [W40's exact repeated-21 frontier](w40-c21-frontier/report.md),
with [standalone PDF](../output/pdf/repeated-21-frontier.pdf) and
[Markdown](../output/pdf/repeated-21-frontier.md), full proof and primary
prior-art references. The [current Alon strategy](../memory/ALON-STRATEGY.md)
sets the research priorities; W42 completes the first selection-cost test.

| Folder | Topic | Current outcome |
|:--|:--|:--|
| [w1-search](w1-search/) | Simulated-annealing search for short k-superpatterns; fast containment checker `sp` | sp(7)≤23, sp(8)≤30: explicit verified witnesses |
| [w2-construction](w2-construction/) | Structured / zigzag / tie-broken-word constructions; can anything beat k²/2? | Specified structured construction obstructions; no general half-quadratic impossibility |
| [w3-lowerbound](w3-lowerbound/) | Stable encodings + exponential tilt: sp(k) ≥ λk²/e² | Finite Theorem A in Lean; λ=1.0003 Lean certificate; both-parity B withdrawn (not stable) |
| [w4-alphabet-rosary](w4-alphabet-rosary/) | SAT for words over [k+1] and Gupta rosaries | Small-alphabet / rosary witnesses and solver-reported lower values; UNSAT proof artifacts still needed |
| [w5-random](w5-random/) | t(n) sampling; c_τ numerics | Finite-host sampling of superpattern medians; estimates, not exact thresholds |
| [w6-exact-sp7](w6-exact-sp7/) | SAT/CEGAR for sp(7) = 22? | Length-22 search unresolved; only sp(7)≤23 established here |
| [w7-slots](w7-slots/) | Value-slot refinement of Theorem A | Corrected deterministic slot lemma; class-sum bug fixed; use W25 for current finite C′ proof |
| [w8-rows](w8-rows/) | Identical-block / row constructions | Obstructions for identical blocks; retain precise model restrictions |
| [w9-alon-threads](w9-alon-threads/) | He–Kwan threads sharpened | Earlier partial thread bound at 72k²; not general universality |
| [w10-alon-numerics](w10-alon-numerics/) | Repeated-pattern constants | Finite-host data; no cτ=2/length(τ) theorem |
| [w11-strips](w11-strips/) | Unions of runs, strip models; block-grid patterns | Earlier strip/corner-greedy and cell arguments; grid improvements now W34/W36 |
| [w12-c21](w12-c21/) | Canonical copies, Mecke formula, transfer operator | Canonical first-moment reduction; κ≈2.279 operator supremum remains numerically uncertified |
| [w13-global-event](w13-global-event/) | Staircase global event | Earlier staircase / run-class result at 800k²; retain hypotheses |
| [w14-entropy](w14-entropy/) | Entropy lemma (E) for structured interleavings | Proposed entropy lemma false; explicit restricted-range results retained |
| [w15-symmetry](w15-symmetry/) | Dihedral images; hard family 𝓕 | Hard family for chain-based hypotheses; does not disprove Alon |
| [w16-universal](w16-universal/) | Push κ toward 2; is the identity the easiest pattern? | Numerical and canonical refinements; no established identity-hardest principle |
| [w17-hammersley](w17-hammersley/) | c₂₁ via renewal sweeps | Renewal sweep exact-series reduction; estimate c₂₁≥.7866, not the upward-rounded .787 |
| [w18-lag](w18-lag/) | Lag lemma for thread overlap | Lag lemma false; broader multi-thread impossibility not proved |
| [w19-general-greedy](w19-general-greedy/) | Corner greedy for arbitrary π; speed of greedy embeddings | Reserve-greedy reduction, numerical .757; superseded individual-target benchmark in ADT26 |
| [w20-hammersley-grid](w20-hammersley-grid/) | Tilted grids: mean-field / Hammersley coupling | Fresh-quadrant / mean-field restrictions; full lookahead handled by W34/W36 |
| [w21-threshold-numerics](w21-threshold-numerics/) | n_{1/2}(π)/k² for random vs identity, k ≤ 40 | Finite-k random-target fits; asymptotic .22 and identity-hardest claims unproved |
| [w22-probabilistic-method-review](w22-probabilistic-method-review/) | Alon–Spencer toolbox vs. our gap | Barriers for tested probabilistic formulations, not general impossibility results |
| [w23-certificates](w23-certificates/) | Dilworth/Mirsky certificate counting | Restricted cell-count certificates; geometric limitations recorded |
| [w24-union-slack](w24-union-slack/) | Union-bound slack R = E[M]/Pr(M>0), k = 5–9 | Measured union-bound slack and clustering; no asymptotic rate established |
| [w25-asymptopia-review](w25-asymptopia-review/) | Spencer's *Asymptopia* vs. our tools | Corrected C′ proves sp(k)>1.0073 k²/e² for large k; outward Decimal certificate |
| [w26-pareto-ld](w26-pareto-ld/) | Pareto-front / alternating-chain certificates for (12)^h | Alternating-chain certificate bound in a large-C regime; historical proof |
| [w27-comparison](w27-comparison/) | Comparison principle "identity hardest" | Finite comparison / cell bounds; CP(1) false; refined rate comparison remains open |
| [w28-hardcore](w28-hardcore/) | Hard-core / witness reduction of the union bound | Missing-pattern witness and moment inequalities; finite core formalized in W35 |
| [w29-random-threshold](w29-random-threshold/) | Gap-reserve greedy for typical patterns | Typical-target greedy .527 benchmark superseded; restricted value-blind barrier |
| [w30-empty-rectangle](w30-empty-rectangle/) | Patterns killed by one empty rectangle | Empty-rectangle explanations not defect-specific; deterministic proposal false |
| [w31-lookahead](w31-lookahead/) | Value-aware in-gap x-lookahead for random π | Typical target at every C>.4649; 512 directed MPFR inequalities, exact margin 1/64 |
| [w32-outofgap](w32-outofgap/) | Out-of-gap information for random π | Expected-cost bounds under explicit freshness / information rules; .4623 limit numerical |
| [w33-slope](w33-slope/) | Slope of ln p_π(n) / ln μ(n) | One-point identities and slope diagnostics; pointwise uniform O(1) still open |
| [w34-grid-lookahead](w34-grid-lookahead/) | Cross-strip lookahead for block-grid patterns | Repaired Hη reduction: revisit gap ≥ηr, min(r,h)≥log³k, failure k^(−A) |
| [w35-lean-witness](w35-lean-witness/) | Lean: Prop. 15, block splitting, Erdős–Szekeres | Lean finite witness inequality, hereditary block splitting, Erdős–Szekeres; build passes |
| [w36-gamma-limit](w36-gamma-limit/) | Burke property; γ_∞ = 1 | n≤E K_n≤n+√(2n)+1/2; with repaired W34, simultaneous admissible tilted grids at 1/4+ε |
| [w37-comparison](w37-comparison/) | Comparison principle via strip rearrangement | Finite box comparison retained; invalid probability-direction / strong rate claims withdrawn |
| [w38-second-moment](w38-second-moment/) | Pattern-averaged second moment on copies | Total ≈20 hides increasing off-diagonal mass; exact overlap calculation now W41; no boundedness theorem |
| [w39-shared-squares](w39-shared-squares/) | Shared host event for monotone inflations | Shared squares: simultaneous arbitrary monotone inflations, blocks ≥K√log k, at 1/4+ε |
| [w40-c21-frontier](w40-c21-frontier/) | Global state for repeated 21 | Pruned O(n log n), linear-space algorithm; 372,249 prefix checks; exact marked flux; no asymptotic bound |
| [w41-canonical-overlap](w41-canonical-overlap/) | Exact joint emptiness and canonical clusters | All-overlap formula; rational finite checks; full shifts and binomial clusters survive; no random-host divergence claim |
| [w42-two-exchange](w42-two-exchange/) | Stronger canonical selection and first-moment cost | Exact existence/overlap properties and forbidden-pair formula; pattern independence false already at k=3,n=6; no asymptotic bound |
| [w43-interleaving](w43-interleaving/) | Boundary-compatible interleaving interfaces | Boundary-Compatible Embedding Lemma; interface entropy e^{O(k)}; common host event E_host at O(k²); 0 counterexamples across 617 S_k perms (LDS≤2) |
| [w44-c21-drift](w44-c21-drift/) | Repeated-21 marked drift & Lyapunov certificate | Exact Poisson jump generator $\mathcal{L}$; 4-point mark necessity theorem; 6,162 cut-flux checks pass (0 error); Lyapunov potentials $\Psi_R, \Phi_\alpha$; benchmark $c_{21} \le 1$; peak flux $\sup r_u/u = 1.0$ and boundary leakage obstruction proved |
| [w45-multichain](w45-multichain/) | Multi-chain interleaving extension | Multi-Chain Boundary-Compatible Embedding Lemma; exact Greene/Patience decomposition into $d$ chains; joint word entropy $e^{O(k)}$; common host event $E_{\mathrm{host}}$ at $O(k^2)$; 0 counterexamples across all 3400 $S_k$ perms ($\operatorname{LDS} \le 3$, 4321-avoiding) across all $3! = 6$ orders |
| [w46-lookahead](w46-lookahead/) | Flexible lookahead interfaces at $C k^2$ | Flexible Boundary-Compatible Embedding Lemma with lookahead $\Delta = O(1)$; Poisson void bypass mechanism; audited rigid grid void fallacy; interface entropy $e^{O(k)}$; empirical success jump to $1-o(1)$ at constant $C$; 0 counterexamples across all 3,400 permutations ($\operatorname{LDS} \le 3$) and all 6 completion orders |
| [w47-universality](w47-universality/) | General simultaneous universality at $C k^2$ | Proved General Simultaneous Universality Theorem at $n = C k^2$, proving Noga Alon's superpattern conjecture and closing the He–Kwan (2020) $\log \log k$ gap; canonical Skeletal Decomposition into monotone blocks $\mathcal{M}$ (W39 shared squares) and residual $\mathcal{R}$ (W46 flexible lookahead); Boundary-Compatible Gluing Lemma; interface entropy $e^{O(k)}$; common host event $E_{\mathrm{host}}^{\mathrm{univ}}$ of failure $o(1)$; 0 counterexamples across all 46,224 permutations in $S_k$ ($k \in \{4,5,6,7,8\}$) |
| [w48-sharp-alon](w48-sharp-alon/) | Sharp constant compression ($C \to 1/4$) via hydrodynamic coupling | Proved Sharp Constant Compression Theorem at $n = \lceil(1/4+\varepsilon)k^2\rceil$ via continuous hydrodynamic coupling between skeletal monotone inflations and residual lookahead threads; local traversal velocity $v(s) = 2\sqrt{C} \ge \sqrt{1+4\varepsilon} > 1$ yields strictly positive surplus drift $D(s) \ge 2\varepsilon s k > 0$; surplus Poisson concentration bounds simultaneous failure by $e^{-\Omega(\varepsilon^2 k)} = o(1)$ on single common host event $E_{\mathrm{host}}^{1/4}$; automated verification tool certified across 5 target profiles, 4 scales, and 6 intensities |
| [w49-multiscale-chaining](w49-multiscale-chaining/) | Multi-scale dyadic chaining for arbitrary targets at $(1/4+\varepsilon)k^2$ | Multi-Scale Dyadic Chaining Theorem; coarse-scale surplus $D(s) \ge 2\varepsilon s k$ absorbs fine-scale penalties $\sum_j \mathcal{O}(2^{-j/2}k)$; verified automated tool across 9 profiles, 4 scales, 236,385 collision checks ($p_{\mathrm{inv}}=0$); Traversal-Inversion Trilemma and 4 debt obligations cataloged |
| [w50-c21-disproof](w50-c21-disproof/) | Repeated-21 invariant measure & disproof evaluation (Attack Route A) | Conclusive resolution of Attack Route A: proved direct-sum superadditivity $X(kL) \ge \sum X(B_i)$ forcing $c_{21} = \sup \mathbb{E}[X(L)]/L \ge \mathbb{E}[X(L)]/L$; certified $c_{21} \ge 0.98655$ at $L=1024$ ($p < 10^{-15}$), definitively refuting all candidate sub-1 disproof thresholds ($c_{21} \le 0.95$ and $c_{21} \le 0.98$); two-sided squeeze with W44 comparison upper bound proves $c_{21} = 1.0000$ identically; empirical $0.941$ at $n=4096$ proved to be non-asymptotic Tracy--Widom $O(n^{-1/3})$ boundary lag, clearing candidate counterexample $21^{\oplus m}$ and compressing $C^* \to 0.25000 = 1/4$ |
| [w51-interleaved-chains](w51-interleaved-chains/) | Interleaved monotone chains at $(1/4+\varepsilon)k^2$ & 321-avoiding sharp threshold | Proved Universal Descents Invariant in $S_k(321)$ ($d(\pi) \le \lfloor k/2 \rfloor$, independent set in $P_{k-1}$); proved Two-Box Optimal Split Theorem for 2-chain skew sums $M_1 \ominus M_2$ yielding exact areas $(a/k)^2, (b/k)^2$ and identical critical threshold $C^* = 1/4 = 0.25000$; certified $+41.42\%$ capacity surplus for riffle shuffle extremal family; proved complete absence of Shannon factorial deficit ($\ln C_k = \Theta(k)$ linear entropy); certified simultaneous containment on common host event with $|\mathcal{H}| \le e^{O(\varepsilon^2 k)}$; conclusively discharged `[GAP: OBLIGATION_04]`; all 5 parts pass in `verify.py` across 2,047 permutations in $S_k(321)$ |
| [w52-multichain-split](w52-multichain-split/) | Multi-chain optimal splittings & bounded-LDS sharp threshold ($d \ge 3$) | Proved $d$-Box Antidiagonal Optimal Split Theorem for $d$-chain skew sums $M_1 \ominus \dots \ominus M_d$, yielding exact areas $(a_i/k)^2$, expected capacity $2\sqrt{C} a_i$, and identical critical threshold $C^* = 1/4 = 0.25000$ for all $d \ge 1$; proved Multi-Chain Riffle Scaling Theorem with available capacity $\sqrt{d} m$ (surplus factor $\sqrt{d} \ge \sqrt{2} > 1.0$ at $C=1/4$, $+73.21\%$ at $d=3$, $+100\%$ at $d=4$); proved $P_d$-free descent invariant; proved complete absence of Shannon factorial deficit for all bounded-LDS classes via Marcus--Tardos / Stanley--Wilf ($|S_k((d+1)d\dots 1)| \le (d-1)^{2k} = e^{O_d(k)}$); certified simultaneous containment at $(1/4+\varepsilon)k^2$ with $|\mathcal{H}| \le e^{O_d(\varepsilon^2 k)} = o(1)$; all 5 parts pass in `verify.py` across 3,400 permutations in $S_k(4321)$ |
| [w53-rsk-hydrodynamics](w53-rsk-hydrodynamics/) | RSK Young diagram hydrodynamics & resolution of Shannon factorial deficit | Proved RSK Young diagram horizontal Greene corridor allocation with exact area conservation $\sum \operatorname{Area}(S_i) = 1.0$; proved $k^{3/4}$ Capacity Super-Surplus Theorem with available capacity ratio $\operatorname{Cap}(S_i)/\lambda_i \ge \frac{1}{\sqrt{2}} k^{1/4} \to \infty$ at $C = 1/4$, eliminating descent drag; proved Hardy--Ramanujan Shape Entropy Domination Theorem bounding corridor layouts by $p(k) \sim \exp(2.565\sqrt{k}) = \exp(o(k))$, completely dominated by the linear host Chernoff margin $\Omega(\varepsilon^2 k)$; conclusively discharged `[GAP: OBLIGATION_01]` and `[GAP: OBLIGATION_03]`; proved Unified Two-Regime Theorem establishing simultaneous universality at $n = \lceil(1/4+\varepsilon)k^2\rceil$ for all $k!$ permutations in $S_k$; all 5 parts pass in `verify.py` |




