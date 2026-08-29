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
