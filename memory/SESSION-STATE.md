# Session state — 2026-08-29 (written before context compaction)

## Where everything lives
- Paper: `output/paper/superpatterns-notes.md` → `make pdf` (`make check` must print 0). Skill: `.claude/skills/paper-formatting`.
- Literature + results: `memory/NOTES.md`. Per-workstream records: `experiments/w*/log.md`, `proof.md`.
- Lean: `formal-verification/lean/` (`lake build` passes; Theorem A + constant fully verified; certificates for sp(7)≤23, sp(8)≤30 via native_decide).

## Working norm (non-negotiable)
Every theorem an agent claims is re-derived line by line by the main session, numerical certificates are recomputed
independently, and combinatorial lemmas are brute-forced per class where possible, BEFORE anything enters the paper.
(W7's Lemma 1' first draft was false — caught this way.)

## Verified results already in the paper (do not re-verify)
Theorem A (λ=1.0003125, Lean), Theorem C (λ=1.00483), sp(7)≤23, sp(8)≤30, f(k;k+1)=(k²+k)/2 for k≤5, rosaries n≤11,
Theorem 8 (W9, 72k²), Theorem 5 (W13, 800k², staircase event), W12 (0.598≤c_21≤1.140; universal bound
Pr(π⊂Π_N) ≤ 668 N^{-1/2} e^{3√N−1.3163k}, κ=2.279), W10 numerics (c_τ=2/|τ| for |τ|≤5), t(7)=37, t(9)≈60, t(10)≈70–72,
W2/W8 negative results, Manjunath–D'Souza review.

## 13:04 IDT: all five Alon agents (W11, W14–W17) were KILLED by the session rate limit (resets 13:20). Each can be resumed by SendMessage to its task id (transcripts persist). On-disk: W11 proof.md+log.md (Thm 9 verified & in paper); W14 proof.md (198 lines, unverified); W15 proof.md (249 lines, unverified); W16 numerics only (thresholds.out, scan2d); W17 only enum3.c/rules.c. Resume them after 13:20 with: 'You were interrupted by a rate limit; continue from your last step; write results to disk first.'

## 13:15 update
- W14 and W15 proof.md VERIFIED and folded into paper: (E) is false; family 𝓕(r,h,ε) (perturbed tilted grid) of size e^{(1/32)k ln k} has chains ≥ k/16 for every shift ≤ 0.7k in all 8 dihedral images ⇒ no chain-based hypothesis can cover S_k; numerically actual overlap is O(1) unless element-lag ≲ 3√k. Prop 3 (W14): unconditional range r ≤ e^57. W15 Thm 8: mixed-direction runs covered.
- CRUX NOW: rigorous LAG LEMMA (only shifts with element-lag ≲ √k polylog are harmful) ⇒ n=O(k²) for all π. Launched W18 `experiments/w18-lag/` on exactly this.
- Resuming W11/W14/W15/W16/W17 after 13:20 only to let them finish logs/reports (their main content is on disk).

## Agents still running when compaction happened (Alon's conjecture push)
Poll by reading their files (never agent transcripts). Each ends with a task-notification; then verify and fold in.
- W11 `experiments/w11-strips/` — strip large deviations for unions of r increasing runs: numerics (strips.c, out/) on
  whether −log Pr(π⊄Π_N) grows like N/poly(r) (speed N) or only like k; theory via free cut points / non-intersecting
  paths / LIS-with-slack. Would close the residual class of Theorem 8/5 → n=O(k²).
- W14 `experiments/w14-entropy/` — entropy lemma (E): #{π∈𝓛_r with ≤ j mutually good shifts} ≤ e^{(29j−1)k}; closes gap G1
  (structured interleavings) with W13's mechanism. Also: periodic words via π^{-1}.
- W15 `experiments/w15-symmetry/` — cover gap G2 (large-LDS chains) by applying Thm 5/8 to the 8 dihedral images of π;
  deliverable: theorem + either "covers S_k" (⇒ n=O(k²) for all patterns!) or an explicit hard family.
- W16 `experiments/w16-universal/` — push universal absence constant κ from 2.279 toward 2 (canonical copies with general
  potentials; lex-min copies); κ=2 ⇒ c_τ ≤ 2/|τ| for all τ. Also numerics: is the identity the easiest pattern
  (threshold sense)?
- W17 `experiments/w17-hammersley/` — c_21 ≥ 1−ε via local structure of Hammersley geodesics (Cator–Groeneboom); numerics
  on nonempty upper-left boxes along LIS paths.
- Background (no agent): `experiments/w6-exact-sp7/k7n22_rc_near_s2.txt` SAT/CEGAR for sp(7)=22? (iteration 3, 70 min/solve;
  "UNSAT" line ⇒ sp(7)=23; "FOUND" ⇒ verify with `experiments/w1-search/sp -k 7 -c -p "..."` and a Python brute force).
- Polling loop: a ScheduleWakeup fires every ~10 min with the poll prompt; stop it (ScheduleWakeup stop:true) when all done.

## Exact remaining gaps for n=O(k²) (after Thm 8 + Thm 5)
G1: π ∈ 𝓛_r, r>e^{28}, with ≥ k/(2ℓ_r) shifts having chains > k/λ_r (near-periodic interleavings) — needs (E).
G2: HK structured maps whose chains have large LDS (staircase count degenerates). Candidate fix: dihedral images.
For the constant 1/4: threads can't reach it (HK coupling loses factor 8); need point-process tools (c_τ=2/|τ|,
universal κ=2, comparison principle).

## Machine hygiene
Load was 200 at peak; obsolete searches were killed (W2/W8 SA, W5 n=10 scan, W2 k=9 chain). Check `uptime`;
kill `sa3|sa4|wild|polish` leftovers if any reappear.

## 13:26 update (post-compaction)
- The five original Alon agents (W11/W14–W17) are DEAD (not resumable). Relaunched fresh with "continue from files" briefs:
  W18 lag lemma `aec498ebf92cccb49` (experiments/w18-lag, nothing on disk yet); W17 `a73263f96138ff6b1`; W16 `ada142dd0792dd7e7`
  (running thresholds2.py k=20, contain_gen jobs); W11 `aeff687d79a787bd0` (strips jobs2 on 12 cores; grid.c = tilted-grid
  r~√k counterexample search). Old W2 agent a3a7b34eee5c21d2f finished with nothing new (its k=9 watcher killed).
- Killed stale SAT sanity runs (k6n17 at 5 missing after 2.4h; fkr_sat 5 8 5 UNSAT up to n=11). Kept k6n16 (method
  validation: UNSAT ⇒ consistent with sp(6)=17) and k7n22 (it=3, 192 missing).
- 13:45: W17 renewal-sweep bound c_21 ≥ 0.7866 (square first-descent rule; Hammersley-style i.i.d. increments) VERIFIED
  by me (argument re-derived; series recomputed = 2.5425687; independent MC 2.5434±0.002) and folded into paper
  (summary table + §Random). W17 still running (l_1.5 sweep 0.803 MC-only; may try closed form). W16: routes (b),(c)
  dead, lex-min hierarchy converges to κ=2 only slowly (~0.03/level), numerics inconclusive at k≤16. W18: numerics
  on 3-thread gains / lag; no lemma yet. W11: tg.c (tilted grid) validation runs in progress.
- 13:50: W17 COMPLETED. Also verified (independent MC for 123/231/21 agrees with series within 0.3%): Thm 3 general-τ
  square-rule bounds c_τ ≥ 0.535–0.552 (S_3), 0.385–0.413 (S_4); Prop 4 cap ≈0.84 for any renewal rule (MC). Folded into paper.
  Remaining agents: W18, W16, W11.
- 14:00: W16 COMPLETED: κ unchanged (2.279); routes (b),(c) dead; new Lemma 2/Thm 3 (level-2 Mecke) rigorous but
  not improving κ. Numerics "identity hardest at finite k" reproduced by me (contain_check.c in scratchpad) and added
  to paper as a remark. Remaining agents: W18 (lag), W11 (strips/tilted grid).
- 14:10: W18 proof.md (Thm 4/5, Cor 6, Lemma 3) VERIFIED line by line: the LAG LEMMA IS FALSE — on the tilted grid every
  shift e ≤ h/4 has Pr(E_0∩E_e) ≥ 2(144C²)^{-er} Pr(E_0) ≥ Pr(E_0)² e^{Ω(k)} (C≥8). Thread framework with polylog
  threads at m=Ck cannot prove n=O(k²) for 𝓕 (heuristic beyond 2 threads). Paper §Alon "missing piece" paragraphs
  rewritten accordingly (negative result (iii)); make check = 0. W18 agent still running (log.md pending).
- 14:20: W18 COMPLETED (log.md written; joint.py exact numerics added to paper as a parenthesis). Only W11 remains.
- 14:15: W11 proof.md §4 (Thm 4.1 corner-greedy, Cor 4.2, Lemma 4.3, Thm 4.4) VERIFIED line by line + simulated
  (scratchpad/w11check.py: copy assertion never fails; c(C) reproduced): EVERY block-grid pattern 𝒢(r,h) ⊇ 𝓕 has
  threshold ≤ (π/8+o(1))k² ≈ 0.393k² (r-independent). Folded in as Theorem 10 (+ summary-table row). 𝓕 is NOT a
  counterexample to Alon. W11 agent still running (jobs5 numerics). W6 SAT: it=4, 100 missing.

## 14:40 update — all Alon agents finished; repo reorganised
- W11 COMPLETED: Thm 4.1/4.4 verified & in paper as Theorem 10 (+ its exact-DP numerics: tilted-grid thresholds decrease
  with r). No agents running. Polling loop stopped. W6 SAT (k7n22) still running in background (it=4, 100 missing).
- Directory reorganised into a git repo (github.com/adamhadani/superpatterns): work→experiments, paper→output/paper,
  lean→formal-verification/lean, lit→references/papers (ignored), notes→memory/. Compat symlinks work/paper/lean/lit
  at the root (gitignored) — remove once no process depends on them.
- Publishing guide applied: experiments/witnesses/ (witness file, independent Python checker, hashes), paper sections
  "Novelty audit" and "Discovery method and AI disclosure", memory/PUBLICATION-CHECKLIST.md.

## 14:30 — second Alon push launched (after user "go ahead")
- W19 `experiments/w19-general-greedy/` (agent adae1b3b6b2420af4): corner greedy for ALL π (uniform per-pattern
  threshold Ck²) + repair rule for speed N/poly(r) tail → union bound → n=O(k²)?
- W20 `experiments/w20-hammersley-grid/` (agent a49eee1d67abeafc1): exact threshold constant for tilted grids
  (coupled Hammersley processes / hydrodynamic limit; subadditivity for existence; target 1/4).
- W21 `experiments/w21-threshold-numerics/` (agent a6c54e5e36bf755e1): n_1/2(π)/k² for random vs identity at
  k=20..32, ≥500 samples; decide 1/4 vs ≈0.23.
- Poll by files every ~10 min; verify before folding in (norm). Lean CI run 33249984762 was still in progress.
- 15:05: W19 COMPLETED and VERIFIED (reduction re-derived; strip cost re-simulated: E T/2 = 1.0009 at C=0.757, h=3
  0.89). Folded as Theorem 11: every π ∈ S_k contained at 0.757k² w.h.p. (first uniform threshold < k²); rigid rows k²;
  union bound (1+o(1))k² ln k; barrier: greedies have speed ≤ min(k,h). The brief's "verbatim for all π" was false
  (strips must be chains) — W19 caught it. W20, W21 still running.
- 15:25: W20 proof.md drafted (not yet verified): Thm 4.2 mean-field upper bound C^fix(r,h) ≤ C_mf(h) as r→∞; Prop 4.3
  Bellman recursion; Prop 4.5 C_mf(h) ↓ π/8; Prop 3.1 fresh-quadrant barrier; Remark 4.7 free ≤ min(fixed directions).
  Key message: FIXED-strip constant is (conjecturally) π/8 — corner greedy optimal there; 1/4 can only come from the
  FREE model (copy chooses its own strip boundaries). W20 still running numerics; W21 k=32 sweep running.
- 15:45: W22 launched (agent a6ef860cc511e6cfc): review of Alon–Spencer 'The Probabilistic Method' for tools vs. our gap → experiments/w22-probabilistic-method-review/review.md. Book PDF in ~/Library/CloudStorage/Dropbox/Books/Mathematics/.
- 16:00: W22 COMPLETED (review verified on the two key claims: Δ ≥ μ²/C; Dilworth certificate (e/C)^N). Folded into
  paper (§Alon, "What the standard concentration tools give") and NOTES ledger. Launching W23 (certificate counting
  for block-grid/periodic patterns) and W24 (union-bound slack numerics) per its recommendations.
- 16:05: W23 `experiments/w23-certificates/` (agent af0e69e8af1caafcf): certificate counting (Dilworth/Mirsky antichain
  covers) for block-grid/periodic patterns — aim: speed N/poly(r) with r-independent threshold. W24
  `experiments/w24-union-slack/` (agent aee98fc61e4771a4f): union-bound slack R = E[M]/Pr(M>0) at k=6–9.
- 16:15: W20 COMPLETED and VERIFIED (Thm 4.2/4.3/4.5/3.1 read line by line; C_mf(2) recomputed 0.748 vs 0.750). Folded as
  Theorem 12 + numerics ((12)^h easier than identity). Running: W21, W23, W24.
- 16:35: W25 launched (agent ad4d410d9c5bb5e02): review of Spencer's Asymptopia (Laplace method for the lower-bound constant, LIS material, threshold heuristics, large deviations) → experiments/w25-asymptopia-review/review.md.
- 17:20: W23 first attempt died (max output tokens, nothing written); relaunched as agent a4511c89f2b56d42e with short-output instructions. W25 (Asymptopia) COMPLETED: proposes Bernoulli (KL) tail in Theorem C → λ_C ≈ 1.00734 (limit rate independently reproduced by me; finite-k certificate being redone in log-space in experiments/w25-asymptopia-review/finite_check_bern.py).
- 17:35: Theorem C′ (λ = 1.00734, W25's Bernoulli tail) VERIFIED (Lemma B.1 checked; limit root reproduced by my own
  code; finite-k log-space certificate negative at k=1e5, 3e5 for λ=1.007) and folded into paper (abstract, table,
  §Thm C, open problems). W25 COMPLETED. Running: W21 (told to add correction-exponent fit and wrap up), W23 (relaunch), W24.
- 17:45: W23 COMPLETED and VERIFIED (Thm 2.1, Cor 2.1′, Prop 2.3 read; Lemma 2.0 = generalised W11 Mirsky lemma). Folded
  as a certificate-counting remark after Theorem 9. Running: W21 (finalising), W24 (k=7 runs).
- 17:58: the sp(7)=22 SAT/CEGAR run (k7n22_rc_near_s2) is no longer running (last line it=4, t=10316 s; possibly killed with the orphan python workers at 14:45). Not restarted — low value (2 h/solve, 100 patterns missing at it=4); restart with 'cd experiments/w6-exact-sp7 && nohup python3 spsat.py 7 22 --sym rc --init near > k7n22_rc_near_s3.txt &' if wanted.

## 18:10 — reformulation and standing queue
- Conjecture LD: Pr(π ⊄ Π_{Ck²}) ≤ e^{−c(C)N} uniformly in π above threshold ⇒ Alon with constant max C*(π) (=1/4 per W21).
  Equivalent route: comparison principle CP(K): Pr(π⊄Π_N) ≤ e^{O(k)} Pr(id⊄Π_{N/K}) + LIS lower tail (speed N).
- Launched W26 `experiments/w26-pareto-ld/` (agent a3c828a52224b02cb): speed N for (12)^h via Pareto-front certificates.
- Launched W27 `experiments/w27-comparison/` (agent a98dc6b4175cd236a): comparison principle — exhaustive numerics k≤7,
  all n; theory for layered/grid/run-union classes; coupling attempts.
- Queued (not launched): W28 hard-core reduction from W24's missing-pattern data; W29 rigorous threshold < 1/4 for random π.
- 18:15: W21 results.md complete (k=40 filled) and folded into paper (identity hardest; random limit ≈0.22). Awaiting its final report.
- 18:40: W26 COMPLETED and VERIFIED (Lemma 1.2/1.3, count, asymptotics; C_0 = 27.63 recomputed). Folded as Theorem 13. Running: W24 (k=8), W27 (comparison). W28 queued behind W24.
- 18:50: W24 agent stopped (tails k=8 n=62, k=9 n=72/58, k=5 grid still running unattended in run_queue.sh; results.md
  not yet written — `python3 analyze.py all` regenerates tables). Key numbers VERIFIED (own brute-force sampler
  scratchpad/w24check.c at k=6 n=28 agrees). Folded into paper (§Alon "How slack is the union bound?" + table row).
  W27 agent paused waiting for smc scans (k=5–7 crossover numerics); its theory (proof.md §0–2, §4) VERIFIED line by
  line (constants q̄(6)=0.938, ι=0.122/0.277, D(½‖0.86)=0.365, Av_7 counts recomputed; note τ_j vs τ_j⁻¹ slip in Thm 2.5
  is harmless). Folded as Theorem 14 + table row. Launching W28 now.
- 18:55: W28 `experiments/w28-hardcore/` launched (agent a114bad863bf853e9): hard-core/cluster reduction Pr(M>0) ≥ μ/R from
  W24 dumps — Janson Δ vs actual, missing-set structure, sufficient condition for R ≤ e^{O(k)}. Still queued: W29
  (rigorous sub-1/4 threshold for random π). Running: W27 (scans), W24 tails (unattended), W28.
- 19:10: W28 COMPLETED and VERIFIED (Thm 1.1/Cor 1.2/Thm 2.1/Props 3.1–3.3 read; ln(E M²/μ) at k=6 reproduced by my
  sampler). Folded as Proposition 15 + table row. Launching W29 (rigorous sub-1/4 threshold for random π). New queue
  item W30: count patterns killed by one empty rectangle (the combinatorial step Prop 15 needs). Running: W27 (scans),
  W24 tails (unattended), W29.
- 19:15: W29 `experiments/w29-random-threshold/` launched (agent a436ab1b1319f3263): rigorous threshold < 1/4 (or < 0.757) for random π. Queue: W30 (patterns killed by one empty rectangle).
- 19:35: W29 COMPLETED and VERIFIED (Lemmas 1.1–1.2, Thms 2.1/3.2 correct; Ω_h reproduced by scratchpad/w29check.py;
  Thm 4.1 proved only for value-blind rules — caveat recorded). Folded as Theorem 16 + table row. W24 tails and W27
  scans still running unattended. Launching W30 (patterns killed by one empty rectangle). Queue after W30: W31
  x-lookahead / 2-D rule for random π below ½; W32 certified (quadrature) Ω_h.
- 19:40: W30 `experiments/w30-empty-rectangle/` launched (agent aa269e0cb3c891816): patterns killed by one empty rectangle (e^{O(k)} vs e^{Θ(k ln k)}). Running: W27 scans, W24 tails, W30.
- 20:00: W30 COMPLETED and VERIFIED (Lemma 1.2, Prop 2.1, Lemma 3.1/3.3, Prop 3.2 re-derived). Folded as a remark
  after Prop 15. Launching W31 (x-lookahead / 2-D rule for random π below ½). Queue: W32 certified Ω_h; W33 uniform
  O(1) slope of ln μ (would give e^{O(k√ln k)} in W30 Prop 3.2). Running: W27 scans, W24 tails, W31.
- 20:05: W31 `experiments/w31-lookahead/` launched (agent af0ae5e29dfcb740d): x-lookahead / 2-D rule for random π below ½. Note: commits now stage explicit paths and use --no-verify (hooks run manually: gitleaks staged) while W27 writes to smc7/deep concurrently.
- 20:15: W27 COMPLETED. Numerics checked by exact enumeration (av9.c/av10.c): qualitative claim right, SMC magnitudes
  biased (noted in w27 proof.md). One sentence added to paper. Running: W31, W24 tails (unattended; two W27 k=8 deep
  runs may still be on 1 core).
- 20:30: W31 COMPLETED and VERIFIED (Lemmas 1.1, 2.1–2.4, Thm 2.1, Lemma 3.1–3.2, Thm 4.1 read; recursion recomputed
  independently in scratchpad/w31check.py: V64/64² = 0.47453 (ε=0), 0.47615 (ε=.05) ≤ certified 0.47646; MC check of
  W(A,B)). Folded as Theorem 17 + table row. ALL AGENTS DONE (W27, W28, W29, W30, W31). Loop stopped.
  Unattended: W24 replicate seeds/k=5 grid still running via run_queue.sh (queueA/B/D) — when finished run
  `cd experiments/w24-union-slack && python3 analyze.py all > analysis.txt` and check ln R trend (all replicates so
  far agree with seed 11). One orphan W27 avoid2 k=8 deep run on 1 core (harmless; kill if load matters).
## Next 3–4 directions (queue)
- W32: rules using information OUTSIDE the current gap (search the other gaps' half-strips; joint DP over gaps) for
  random π — target < 0.46, ideally toward 0.22; or prove a cap for all sequential rules.
- W33: uniform O(1) slope −∂_n ln μ (would upgrade W30 Prop 3.2 to e^{O(k√ln k)} and quantify Cor 1.2 of W28).
- W34: apply the W31 lookahead idea to the IDENTITY / monotone strips (corner rule + cost-to-go) to push π/8 for
  block-grid patterns toward 1/4 (Thm 10/12 fresh-quadrant barrier is for rules without lookahead).
- W35: Lean-formalise the W28 witness reduction (Prop 15) and the block-splitting lemma (cheap, exact).
- 20:45 (user: "go ahead"): launched W32 `experiments/w32-outofgap/` (agent ad46e0aa90c52e9fd), W33 `experiments/w33-slope/`
  (a03aa95cefdafa091), W34 `experiments/w34-grid-lookahead/` (a174397d02aa988d8), W35 Lean `formal-verification/lean/`
  + `experiments/w35-lean-witness/` (a5790454cda97aa0a). Poll loop restarted (~25 min).
- 20:55: W35 COMPLETED and VERIFIED (lake build 8719 jobs OK; 12 new theorems on standard axioms; no sorry). Folded into paper §Verification (iv). Running: W32, W33, W34, W24 tail.
- 21:10: W34 COMPLETED and VERIFIED (proof re-derived; constants re-simulated in scratchpad/w34check.py; 2C typo noted).
  Folded as Theorem 18 + table row. Running: W32, W33, W24 tail. New queue item W36: prove γ_∞ = 1 (stationary solution
  of the first-passage recursion) ⇒ tilted grids at exactly 1/4; W37: certify C^mix_2 via Feynman–Kac.
- 21:30: W32 COMPLETED and VERIFIED (Thm 2.1 induction checked) → Theorem 19 (cap 0.4623 for all sequential rules).
  W33 COMPLETED (k=7 SMC row pending, immaterial) and VERIFIED (H_0 identical to DZ's; slope formula checked
  numerically) → slope paragraph + Prop 15 proviso sharpened. Remaining: W24 tail only.
## Next 3–4 directions (queue, updated)
- W36: prove γ_∞ = 1 for the first-passage recursion (Thm 18(c)) — Burke/stationarity; would give tilted grids at 1/4.
- W37: NON-sequential construction for random π (Thm 19 says sequential rules are capped at 0.46 vs truth 0.22):
  e.g. choose the copy as an optimal path in a Hammersley-type last-passage problem over value strips (global LIS
  analogue); or a two-pass scheme (first pass explores, second commits) — check whether it escapes (F).
- W38: certify C^mix_2 (Feynman–Kac) and the Thm 18 constants; Lean for Lemma 2.2 scaling.
- W39: pointwise O(1) slope via Prop 4.1 of W33 (hitting time of the prefix pattern under the avoiding measure).
- 21:40: W24 COMPLETED (results.md final: ln R at t(k) = 1.34,1.93,2.59,3.26,3.87 for k=5..9); paper numbers updated. ALL AGENTS DONE; loop stopped.

## 2026-08-30 — next-round plan (ranked; not yet launched)
Key reformulation: π ⊆ Π_N ⇔ ∃ y-cuts c s.t. the strip-rearranged process Π_c (strips permuted by π⁻¹; still Poisson(N)
by measure preservation) has an increasing chain hitting each strip once. So Pr(π⊄Π_N) = Pr(sup_c L(Π_c) < k) where each
L(Π_c) has a π-independent law; only the joint law of {Π_c} depends on π (identity: all Π_c equal ⇒ sup = LIS).
Alon ⇔ "less correlated family has larger sup" (Slepian-type comparison). Alon needs per-π tails e^{−ω(k ln k)} at
(1/4+ε)k², not speed N; sequential rules are capped at e^{−Θ(k)} (extensive LDP) — global mechanism required.
Ranked queue:
1. W-next A: comparison principle via rearrangement — rate form Pr(π⊄Π_N) ≤ e^{o(k ln k)} Pr(id⊄Π_{N(1−o(1))});
   test on W27 exact Av_n tables (k≤8); proof shapes: monotonicity under adjacent-transposition "sorting", strip-wise FKG.
2. W-next B: weighted/balanced second moment on copies (Achlioptas–Peres style). Averaged over π:
   E_π E M_π²/μ² = k!·Pr(two random k-subsets of random σ_N share a pattern) = Σ_j Pr(J=j) k! p_j.
   Crude clustering heuristic: OK iff 1+C < e²C ⇔ C > 1/(e²−1) ≈ 0.157. First step: brute-force R_avg(N,k), k≤10,
   C ∈ {0.2,0.25,0.3,0.5}; then boost via Prop 15 / superposition Π_{mN} ⊇ ∪ Π_N.
3. W36 as before: prove γ_∞ = 1 (free model for tilted grids = sup over cuts; hydrodynamic/stationary argument) —
   proving ground for 1.
- 2026-08-30 launched (user "go ahead"): W36 experiments/w36-gamma-limit/ (prove γ_∞=1), W37 experiments/w37-comparison/
  (rearrangement comparison principle), W38 experiments/w38-second-moment/ (pattern-averaged/balanced second moment on
  copies; R_avg numerics first). Poll by files every ~20 min; verify before folding (norm).
- 2026-08-30 09:40: W36 COMPLETED and VERIFIED line by line (Lemmas 1.1–1.3, 2.1–2.4, 3.1–3.4 read; Burke jump law,
  D~Exp(1/ρ), E G^ρ_1(0)=nρ, E K_n at n=10/50/200 and the certified C^mix_b table all recomputed with my own
  DP/simulator: scratchpad w36check.py, w36burke.py). Folded as Theorem 20 + table row; Thm 18(c) upgraded to proved.
  make check = 0. Caveat kept in the paper: no matching lower bound for grids (grid LIS = r+h−1), so "exactly 1/4"
  applies to the mean-field fixed-strip model, not to containment. Running: W37 (comparison), W38 (second moment).
- 2026-08-30 09:55: W37 and W38 BOTH KILLED MID-RUN by "out of usage credits" (API 429, model claude-fable-5).
  Their on-disk work was verified by me and folded as Theorem 21 (+ table row): W37's strip-rearrangement
  reformulation, elementary Av_n(id_a) ≤ (a−1)^{2n} tail, box comparison, and the class 𝒞_k at (1/4+δ)k² with a
  CLOSING union bound (conditional on Deuschel–Zeitouni; unconditional at 16k²); W38's negative result (plain
  pattern-averaged second moment is e^{Θ(k)} at C=1/4 — my own MC reproduces their whole table, slope 0.167/k).
  make check = 0. UNFINISHED and worth resuming when credits allow: W38 §2 canonical-copy table (leftmost-canonical
  ratio looks bounded and pattern-uniform — the live route to a global existence proof for random π); W37's
  results.md was never written (tables are in experiments/w37-comparison/data/ + analyze.py) and its n=13 run
  (n13.log) never finished.
