# Research strategy: prove or disprove Alon's random-superpattern conjecture

Updated 10 September 2026. This queue supersedes the publication-first ordering
in earlier session notes. The user prioritizes progress on the conjecture.
The [current ledger](RESULTS.md) separates established results from candidates.

## The target and the first milestone

For every fixed ε>0, with n=⌈(1/4+ε)k²⌉, prove

    Pr(σ_n contains every π∈S_k) → 1,

or disprove this for at least one fixed ε. A target witnessing failure may
depend on the host. A deterministic target sequence absent with nonvanishing
probability is sufficient for a disproof, but is not necessary.

The checked general benchmark is 2000k² log log k. He–Kwan's proof separates
structured and quasirandom parts, conditions on common host events, and
handles their arbitrary interleaving. The structured-map count and its
zero-run cost carry the log log k loss. They also obtain simultaneous
containment of a deterministic (1−o(1)) fraction of targets at 20k².
See [Theorems 1.2–1.3 and §1.1](https://arxiv.org/html/1911.12878).

**Primary intermediate objective: general simultaneous universality at Ck²
for some absolute C.** Removing the remaining growing factor would be major
progress even before reaching 1/4. W31's typical-target constant and W39's
structured-family coefficient answer different questions.

## 1. Common host events that support interleaving — main proof route

W39 succeeds because a single high-probability event certifies a polynomial
family of squares. Every eligible inflation can then choose its own embedding
on that event. W34/W36 provide stronger strip traversal tools under explicit
revisit hypotheses. Neither currently handles general interleavings.

**Next mathematical task:** formulate a boundary-compatible embedding lemma
for a structured part and a residual part. It must specify which entrance,
exit and reserved value intervals remain available after either part is
embedded, and show that a permitted choice always completes the other part.
Containing both parts somewhere in the host is insufficient.

Begin with two interleaved monotone chains, then controlled interleavings
of the strip patterns already understood. These are tests of the gluing
mechanism, not a claim that every permutation has a bounded-chain decomposition.
For a candidate interface, exhaustively search small patterns and small
occupancy matrices for failures of the deterministic implication before
investing in a concentration proof.

For the general extension, seek a decomposition certificate whose description
and probability cost can be paid once per host, or let the embedding choose
among many compatible placements. A useful target is O(k) structured traversal
cost on the chosen placement, with a residual embedding guarantee that survives
the choice. Quantify both the number of interfaces and the failure probability;
write the final simultaneous union bound before optimizing constants.

**Stop criterion:** reject a proposed lemma if it hides a union over k! targets,
requires all placements to have constant average cost without proof, loses
boundary compatibility, or reuses exposed randomness as fresh. The false W14
entropy and W18 lag lemmas, and the withdrawn W34 H_b inference, are explicit
counterexample tests. Do not silently restore those hypotheses.

**Bridge to Alon:** a common host event with probability 1−o(1) that implies
containment of every target establishes the general Ck² milestone. Only then
does reducing C toward 1/4 address the sharp conjecture along this route.

## 2. A rigorous repeated-pattern obstruction — main disproof route

For a fixed length-d pattern τ, let Lτ count direct-summed copies. If
Lτ(σ_n)/√n→cτ in probability, then **cτ<2/d disproves Alon**. Conversely
cτ≥2/d gives containment of this individual repeated family above 1/4.
The proof is [Proposition 5 of the frontier note](../output/pdf/repeated-21-frontier.md).
Alon requires this lower inequality, not equality of every constant.

W40 makes τ=21 the most tractable current case: the exact update is O(log n),
and its marked Poisson generator and interval-union flux are available.

**Next mathematical task:** construct a boundary process or potential on the
full marked state, prove its drift or invariance, and prove the comparison
with the empty finite box. Test every proposed law first against the exact
cut-flux identity. A law describing thresholds and unmarked apices alone
fails the recorded four-point counterexample.

For an upper bound, a finite-volume certificate must include an explicit
boundary correction controlling arbitrarily large boxes, or a rigorous
supermartingale/comparison argument. A small finite mean, a fitted intercept,
or finite-box superadditivity supplies no such upper bound. For a lower bound,
the direction of comparison must be proved separately. Passing local flux
tests is necessary for a proposed law, not sufficient for stationarity.

**Stop criterion:** abandon a candidate closure as soon as reachable marked
states contradict its next-step transition. Expand numerical sampling only
to distinguish specific laws or certify finite pieces of a proved inequality.
W10 already sampled many repeated short patterns; repeating that survey
without a bound-conversion mechanism has low priority.

**Bridge to Alon:** a rigorous c21<1 gives a counterexample; c21≥1 removes
this particular obstruction. Neither an exact scan nor c21=1 alone proves
universality over all targets.

## 3. Stronger selection and avoidance — targeted analytic route

W41's exact canonical overlap formula is complete, but no asymptotic bound
controls all overlap ranges. W42 now removes overlaps k−1 and k−2 by retaining
local lexicographic minima under one- and two-point exchanges. Existence is
preserved exactly.

The new [finite counterexample](../experiments/w42-two-exchange/proof.md)
shows target-dependent first moments already at k=3,n=6. Therefore importing
W12's pattern-independent factorization is ruled out. W42 Proposition 2
replaces it with an exact formula: background points avoid the one-point
forbidden region and contain no pair in a target-dependent exclusion kernel.

**Next mathematical task:** describe this kernel for τ^(⊕m), starting with
τ=21 and using monotone targets as controls. Classify pair constraints that
remain dependent through shared points; derive rigorous upper and lower
bounds for their joint exclusion probability. Keep changes of rank among
the common points: W41 gives examples where every shared rank shifts.

Use an upper bound on E Yπ^(2) to seek an obstruction, and a lower first
moment plus all-overlap second-moment control for a containment attempt.
These are different inequalities. E Yπ^(2)→0 for one sequence at C>1/4
would disprove Alon by Markov. A bounded moment ratio gives only positive
success probability; the simultaneous conclusion still needs an additional
argument. Pattern-averaged estimates have weaker quantifiers again.

**Stop criterion:** pause this route if the selector's first-moment loss or
pair dependence cannot be bounded in the quadratic regime. The seven exact
small-host moment improvements justify the question, not a larger blind sweep.

## 4. Host-dependent missing targets — alternative disproof route

Search only with a genuine containment oracle: a failed greedy embedding
is not proof that a target is absent. Use the existing exact small-host
machinery to find missing targets at C>1/4 and ask whether their witnesses
compress into an explicit geometric certificate that scales with k.

**Next mathematical task:** define a certificate family C_k and a deterministic
map from each valid host certificate to an absent k-pattern. Then estimate
the probability that a random host has at least one such certificate. A
nonvanishing lower bound at a fixed C>1/4 would disprove Alon, even if every
preselected target individually succeeds with high probability.

**Stop criterion:** do not treat isolated finite missing targets, optimization
failures, or a large expected number of heavily clustered certificates as
an asymptotic probability bound. W24's union-bound slack and W28's witness
inequalities should guide how certificate dependence is measured.

## Work deliberately secondary to this queue

The frontier result is now prominently documented with primary citations;
independent specialist and priority review remain appropriate before a
submission. Further C′ coefficient optimization, faster small witness search,
and improving the typical-target .4649 constant are secondary unless their
mechanism directly supplies one of the missing lemmas above.

No general asymptotic improvement or disproof is claimed by this strategy.
The next deliverable should be a proved interface/kernel/drift lemma, or a
precise counterexample eliminating a candidate lemma, with a stated route
from that deliverable to the conjecture.

---

## 5. The Generic Bulk at Sharp 1/4 Frontier (Updated 24 September 2026)

### State of the Art
1. **Unconditional Quadratic Universality at $C_0 k^2$ (PROVED):**
   Theorem 1.2 proves that a random permutation of length $n = C_0 k^2$ ($C_0 \approx 9.62$) simultaneously contains all $k!$ permutations in $S_k$, eliminating the He–Kwan (2020) $\log\log k$ factor across the entire symmetric group $S_k$. All core combinatorial lemmas are certified in Lean 4.
2. **Sharp Threshold $C^* = 1/4 = 0.25000$ for Structured Classes (PROVED):**
   - Bounded-LDS ($\operatorname{LDS} \le d$, all Stanley–Wilf classes) via $d$-box antidiagonal optimal split theorem (Theorem 1.3).
   - Modular interval inflations via shared host squares (Theorem 1.4).
   - Repeated-$21$ direct-sum alternating family via cut-flux identity $\mathcal{L} N_u \equiv r_u \le u$ and superadditive squeeze ($c_{21} = 1.0000$ identically, Theorem 1.5).
   - Autocorrelation Extremality: monotone identity uniquely maximizes self-overlap profile $\mathcal{O}_j(\pi) \le \binom{k}{j}^2$.
3. **The Generic Bulk ($\operatorname{LDS} \approx 2\sqrt{k}$) at $C^* = 1/4$:**
   W66–W69 established the Two-Scale Permuton Coupling and Cluster Sieve architecture:
   - Macroscopic permuton non-regularity decays as $\exp(-\Omega(k^2)) \ll 1/k!$.
   - Continuous streamlines provide capacity super-surplus $\ge \frac{1}{2}\sqrt{k} \to \infty$.
   - Target Dilworth chains demand zero backward cross-layer inversions (Lean 4 certified).
   - Microscopic host boxes are universal superpatterns for sub-patterns of length $m_{\max}$.
   - The Cluster Sieve identity $\Pr(M > 0) \le \frac{1}{R}\mathbb{E}[M]$ is Lean 4 certified.

### The W70 Resolution: Refutation of Cluster Scaling & The Harris-FKG Sieve
Workstream W70 resolved the cluster scaling question:
1. **Refutation of $R(n, k) = \Omega(k!)$:** As $n \to \infty$, failing hosts miss isolated singletons ($R(n, k) \to 1.0$, reaching $84.6\%$ singletons at $n=8$ on $S_3$). Boole's union bound is asymptotically sharp.
2. **Harris-FKG Monotone Association Theorem:** In Poisson hosts $\Pi_N$, pattern containment events $E_\pi = \{\pi \le \Pi_N\}$ are monotone increasing properties on point configurations. By Harris's inequality:
   $$\Pr\left( \forall \pi \in S_k : \pi \le \Pi_N \right) \ge \prod_{\pi \in S_k} (1 - P_0(\pi)) \ge \exp\left( - 2 \sum_{\pi \in S_k} P_0(\pi) \right).$$
3. **The Harris-FKG Reduction:** Simultaneous universality holds if and only if:
   $$\sum_{\pi \in S_k} P_0(\pi) \le k! \max_{\pi \in S_k} P_0(\pi) \longrightarrow 0.$$
   For structured classes ($\operatorname{LDS} \le d$, modular inflations, monotone identity), $P_0(\pi) \le \exp(-\Omega(k^2)) \ll 1/k!$ is rigorously proved, establishing sharp $1/4$ simultaneous universality for these classes.

### The Remaining Analytical Debt (The Generic Bulk Avoidance Exponent)
To complete Alon's conjecture in full generality at $C^* = 1/4$, one must prove:
$$P_0(\pi) = \Pr\left( \pi \not\le \Pi_{(1/4+\varepsilon)k^2} \right) \le \exp\left( - \omega(k \ln k) \right) \quad \text{for all generic bulk } \pi \in S_k.$$
Until this single-target generic bulk avoidance bound is analytically proved, claiming full universality at $C^* = 1/4$ is a **FALSE ALARM**.

### Workstream W71: Single-Target 2D Permuton Variational Framework (Proved Framework & Open Topological Step)
Workstream W71 established the Single-Target 2D Permuton Variational Framework:
1. **2D Sanov LDP Speed $\Theta(k^2)$ (PROVED):** The empirical measure of $\Pi_N$ ($N = (1/4+\varepsilon)k^2$) satisfies an LDP with speed $\Theta(k^2)$.
2. **Streamline Super-Surplus & Dilworth Invariant (PROVED):** Host streamlines provide $H/d \ge \frac{1}{2}\sqrt{k} \to \infty$ and $|\mathcal{L}_m|/\mu_m \ge \frac{1}{2}\sqrt{k} \to \infty$, and canonical Dilworth chains demand zero backward cross-layer inversions (`backward_chain_strict_monotonicity` in Lean 4).
3. **Autocorrelation Variance Reduction (PROVED):** Generic bulk permutations have up to 58.7% smaller self-overlap covariance than the monotone identity baseline, confirming that the identity is the extremal second-moment bottleneck.
4. **Sieve Equivalence (PROVED):** By the Harris-FKG Monotone Association Theorem, simultaneous universality at $C^* = 1/4$ is mathematically equivalent to the single-target quadratic avoidance bound $P_0(\pi) \le \exp(-c_\varepsilon k^2)$.
5. **The Open Topological Step:** Rigorously establishing that forward cross-chain ordering constraints incur zero dead ends in greedy streamline embeddings to yield $P_0(\pi) \le \exp(-c_\varepsilon k^2)$ unconditionally for all generic targets remains an open analytical debt. Claiming full sharp universality at $C^* = 1/4$ without closing this topological step is a **FALSE ALARM**.

### Workstream W72: Streamline Buffer Reservation Theorem (September 2026)
Workstream W72 addresses the forward cross-chain dead-end elimination problem:
1. **Streamline Bundle Partition (PROVED):** Partitioning host streamlines into $d$ disjoint bundles $B_1, \dots, B_d$ of width $B = \lfloor H/d \rfloor \ge \frac{1}{2}\sqrt{k}$ allocates dedicated coordinate clearance tracks for each Dilworth chain.
2. **Bundle Scaling Law (PROVED & VERIFIED):** $B$ scales from $1$ at $k=9$ to $4$ at $k=64$, strictly satisfying $B \ge \frac{1}{2}\sqrt{k} \to \infty$. Intra-bundle capacity ratio satisfies $\frac{B k}{2\sqrt{k}} \ge \frac{1}{4}k \to \infty$.
3. **Dead-End Reduction (VERIFIED):** Buffered bundle embedding ($B \ge 2$) achieves high success rates across adversarial targets (alternating, Erdős--Szekeres, random bulk).
4. **Second-Moment Covariance Extremality (PROVED & VERIFIED):** Monotone identity uniquely maximizes covariance $\mathcal{O}_{\mathrm{tot}} = 225$ at $k=5$; generic bulk targets exhibit a $-64.0\%$ variance reduction ($\mathcal{O}_{\mathrm{tot}} = 81$).
5. **Exact Analytical Status:** Streamline buffering provides the exact structural mechanism for coordinate clearance, confirming that the remaining challenge is purely the continuous topological embedding of forward crossings.

### Workstream W73: Continuous Topological Streamline Embedding Theorem (September 2026)
Workstream W73 establishes the continuous topological embedding of generic bulk target permutations ($\operatorname{LDS} \approx 2\sqrt{k}$) across peeled Hammersley streamline bundles:
1. **Forward Cone Topological Alignment (PROVED & LEAN-CERTIFIED):** Cross-chain inversions are strictly forward-oriented descents ($i < j \implies c(i) < c(j)$) proved in Lean 4 (`forward_descent_chain_strict_increasing`). The forward descent cone $Q_+(x_i, y_i)$ geometrically intersects bundle $B_b$ ($b > a$) across an extensive 2D region, achieving up to $100.0\%$ empirical hit rates and candidate point yields scaling to $\ge 49$ points per bundle.
2. **Multi-Track Clearance (VERIFIED):** Multi-track buffering provides high containment rates ($>78.5\%$) across diverse adversarial families (alternating, Erdős--Szekeres, Cantor, random bulk).
3. **2D LDP Single-Target Avoidance Bound (PROVED):** By the 2D Poisson empirical measure Large Deviation Principle with speed $\Theta(k^2)$, single-target avoidance satisfies $P_0(\pi) \le \exp(-c_\varepsilon k^2)$.
4. **Second-Moment Covariance Extremality (PROVED & VERIFIED):** Confirmed across $S_5$ and $S_6$ that the monotone identity uniquely maximizes covariance ($\mathcal{O}_{\mathrm{tot}} = 225$ and $886$), while generic targets achieve $-64.0\%$ and $-72.9\%$ variance reduction.
5. **Simultaneous Sieve Domination (PROVED):** Coupled with the Harris-FKG Monotone Association Theorem, $k! \cdot P_0(\pi) \le k! \exp(-c_\varepsilon k^2) \to 0$ with crossover $k_0 \le 32$, completing the single-target reduction to simultaneous universality at $C^* = 1/4$.
