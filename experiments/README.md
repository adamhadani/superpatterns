# Experiments / workstreams

> **10 November 2026.** Workstreams W43–W89 were not accepted by the [audit](../memory/AUDIT-2026-11-10.md) and
> have been moved, unedited, to [archive-2026-09-unverified/](archive-2026-09-unverified/) (see its README for why
> each approach fails). Current status: [SESSION-STATE](../memory/SESSION-STATE.md).

Current index after the 10 September 2026 review, its follow-up, and the 10 November 2026 audit. See the
[authoritative ledger](../memory/RESULTS.md) for exact quantifiers,
certificate status and the next research queue. `log.md` preserves chronology;
`proof.md` gives the current argument where reviewed. Files marked historical
may contain withdrawn claims and must not be used as current proof status.

**Featured:** [W90](w90-layered-deficit/proof.md) — block-flip theorem, c₂₁ ≤ 1, and the numerical evidence that
c₂₁ < 1; [plan for the strict inequality](w90-layered-deficit/strict-deficit-plan.md). Also
[W40's exact repeated-21 frontier](w40-c21-frontier/report.md) with its [standalone PDF](../output/pdf/repeated-21-frontier.pdf).
The [current strategy](../memory/ALON-STRATEGY.md) sets the research priorities.

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




| [w90-layered-deficit](w90-layered-deficit/) | Layered patterns vs the identity: block-flip theorem, exact deficit identity, paired simulations | **Proved:** replacing a block 12 by 21 in a direct sum never increases containment; hence $L_{21} \le_{st} \lfloor \mathrm{LIS}/2 \rfloor$ and $c_{21} \le 1$. **Numerical:** $\mathbb{E}\lfloor \mathrm{LIS}/2\rfloor - \mathbb{E} L_{21} = (0.00113 \pm 0.00002)\sqrt{n}$ for $n = 10^3 \dots 10^8$, i.e. $c_{21} \approx 0.99887 < 1$, which would refute Alon's sharp conjecture; larger layers have larger deficits. Strict asymptotic deficit not proved |
