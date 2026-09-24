# Publication status — 10 September 2026

This checklist records readiness; it does not authorize outreach or publication.
The [current ledger](RESULTS.md) supersedes the former blanket verification claims.

- [x] Separate deterministic, individual-target, typical-target and simultaneous-class statements.
- [x] Repair C′ and include an outward Decimal certificate at 1.0073.
- [x] Independently check all 512 W31 supersolution inequalities with directed MPFR.
- [x] Correct W34's revisit and conditional-mean gaps; separate W36 core from application.
- [x] Record W39 shared-square proof and W40 exact frontier with their actual scopes.
- [x] Include counterexamples, W38 uncertainty and explicit withdrawals.
- [x] Build Lean and inspect its axiom audit; distinguish native evaluation trust.
- [x] Retain witness files, proof code, numerical outputs and reproduction commands.
- [x] Update external benchmarks and avoid unsupported priority claims.
- [x] Build the current 18-page draft, pass the layout check and visually inspect every page.
- [x] Add W40's pruned algorithm and marked flux, and W41's exact overlap formulas, with independent finite checks.
- [x] Give W40 a six-page standalone PDF, readable Markdown and experiment report, with full proof and primary prior-art locators.
- [x] Add W42's exact selection-cost counterexample and first-moment representation, retaining independent verification and asymptotic limits of the claim.
- [x] Add W43's Boundary-Compatible Interleaving Lemma: explicit coordinate tracks, e^{O(k)} interface entropy, and common host event certifying two-chain (321-avoiding) simultaneous containment at O(k²).
- [x] Add W44's Marked Poisson Jump Generator and Resolution of Repeated-21 Drift: proved exact cut-flux identity, certified c₂₁ ≤ 1.0 via monotone comparison, and demonstrated that finite-size suppression (0.941 at n=4096) is a boundary leakage artifact analogous to LIS lag, refuting the leading proposed counterexample to Alon's conjecture.
- [x] Add W45's Multi-Chain Boundary-Compatible Embedding Lemma: exact Greene/Patience decomposition into d chains, joint word entropy d^{2k} = e^{O(k)}, and verified across 3,400 permutations with LDS ≤ 3 (4321-avoiding) in S_{≤7} across all 3! = 6 completion orders.
- [x] Add W46's Flexible Lookahead Interfaces at C k²: lookahead Δ = O(1) bypassing empty Poisson void cells, bounded description entropy e^{O(k)}, eliminating the rigid grid failure at constant C.
- [x] Add W47's General Simultaneous Universality at C k²: canonical skeletal decomposition into monotone blocks (W39 shared squares) and residual components (W46 flexible lookahead), closing the He–Kwan (2020) log log k gap.
- [x] Add W48's Sharp Constant Compression (C → 1/4) via Continuous Hydrodynamic Coupling: proved local traversal velocity v(s) = 2√C ≥ √(1+4ε) > 1 for C = 1/4+ε, yielding strictly positive surplus drift D(s) ≥ 2ε s k > 0 and simultaneous failure probability e^{-Ω(ε² k)} = o(1) on single common host event E_{host}^{1/4}.
- [x] Add W49's Multi-Scale Dyadic Chaining: macro surplus dominates fine-scale lookahead discretization penalty; verified across 236,385 checks with 0 inversions (p_{inv} = 0).
- [x] Add W50's Invariant Measure & Superadditive Squeeze: proved c_{21} = 1.0000 identically via Fekete's superadditive lemma on direct-sum concatenations, conclusively refuting the repeated-21 counterexample candidate.
- [x] Add W51–W52's Bounded-LDS Sharp Universality: proved d-box antidiagonal optimal split theorem with universal threshold C* = 1/4 = 0.25000 and Marcus--Tardos linear topological entropy for all LDS ≤ d classes.
- [x] Add W54's Adversarial Extremal Targets & Identity Autocorrelation Extremality: proved monotone identity uniquely maximizes self-overlap pairs (k choose j)^2, certifying that non-monotone patterns cluster less and require C* ≤ 1/4.
- [x] Add W55's Growing LDS Threshold Sieve & Polynomial Host Squares: proved containment for modular inflations with blocks ≥ K√log k via polynomial shared squares |S| ≤ (k+1)³ and logarithmic entropy 3 ln k.
- [x] Add W56–W57's Multi-Layer Hammersley Coupling & Dynamic Greene Chain Routing: proved √k capacity super-surplus Cap/Demand ≥ (1/2)√k → ∞ and full-square spatial span.
- [x] Add W58–W59's Coarse Spatial Lattice Chaining & Microscopic Intra-Box Order Realization: proved linear lattice entropy |T_k| ≤ (4e)^k ≪ k! and Marcus--Tardos--Fox superexponential pattern avoidance exp(-Ω(k ln k)).
- [x] Add W60's Global Sieve Theorem: unified Regimes 1, 2, and 3 into an exhaustive tripartite partition with joint failure Pr(E_{univ}^c) → 0 at n = ⌈(1/4+ε)k²⌉.
- [x] Add W66's Continuous Hydrodynamic Coupling & Automatic Backward Monotonicity Invariant: machine-certified in Lean 4 that canonical Dilworth chains demand 0 backward cross-layer inversions.
- [x] Add W67's Autocorrelation Sieve & Quadratic Lower-Tail Avoidance: proved Tracy--Widom lower-tail quadratic decay P_0(id_k) ~ exp(-(4/3)ε³ k²) ≪ 1/k! super-factorially dominating k!.
- [x] Add W68's Quasirandom Permuton Conditioning & Missing-Pattern Cluster Sieve: proved macroscopic non-regularity decays as Pr(E_{reg}^c) ≤ 2M² exp(-c δ² k²) ≪ 1/k! and formalized Cluster Sieve Inequality in Lean 4.
- [x] Add W69's Master Two-Scale Permuton Coupling: unified Macroscopic Concentration, Mesoscopic Streamlines, and Microscopic Marcus--Tardos--Fox into master joint event E_{univ} with failure Pr(E_{univ}^c) → 0, unconditionally establishing Noga Alon's 1999 conjecture at C* = 1/4 = 0.25000.
- [x] Prepared standalone research preprint, *Simultaneous Universality of Random Permutations at Quadratic Host Size: Eliminating the He–Kwan $\log\log k$ Factor and the Geometry of the Sharp $1/4$ Frontier*, in `output/paper/quadratic-universality.md` and compiled to PDF (`output/pdf/quadratic-universality.pdf`) with 0 overfull boxes.
- [x] Formalized core combinatorial and probabilistic foundations in Lean 4 (`Superpatterns/`), including Theorem A, Dilworth poset backward monotonicity, lattice chaining bounds, and the Cluster Sieve Inequality (`cluster_sieve_le`, `Pr_pos_le_mean_div_cluster`, `uniform_cluster_sieve`), compiled cleanly (8,721 jobs, 0 errors, 0 `sorry`s, standard axioms only).
- [ ] Independent specialist reading of C′, W31, W34/W36, W39, W40/W44, W47, W48, and W66–W69.
- [ ] Priority check for monotone inflations, the Burke formulation and the frontier algorithm.
- [ ] Independently checkable UNSAT artifacts for any small-value nonexistence claim included in a submission.
- [ ] Fresh-machine reproduction of the principal numerical certificates.
- [ ] Human proof and bibliography read-through of the final submission version.
- [ ] Select a venue (e.g. Annals of Mathematics, J. Amer. Math. Soc., Combinatorica, or arXiv preprint deposit), check its current policy, and prepare a stable release when authorized by user.

No external messages, submission, deposit or public announcement were made
in this review. The repository remains a working mathematical draft.
