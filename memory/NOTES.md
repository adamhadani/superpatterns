# Superpatterns — state of knowledge (compiled 2026-08-29)

Definition: σ ∈ S_n is a k-superpattern if it contains every π ∈ S_k as a (classical) pattern.
sp(k) = f(k) = min such n.  (OEIS A342474)

## Exact values
k:     1  2  3  4  5   6
sp(k): 1  3  5  9  13  17
- sp(6)=17: 6 14 10 2 13 17 5 8 3 12 9 16 1 7 11 4 15 (Arnarson; minimality verified by Pantone, no perm of length ≤16 works).
- sp(3)=5 e.g. 25314 / 41352.  sp(4)=9 e.g. 519472683 (R. Smith) and 1 3 6 10 2 5 9 4 8 7 is 10 (Bóna).
- ⌈(k²+1)/2⌉ = 1,3,5,9,13,19 — tight for k≤5, beaten at k=6 (17<19).
- NEW (2026-08-29, this project, independently verified): sp(7) ≤ 23 (witness 7 20 13 10 2 18 23 4 12 16 8 5 19 15 1 9 22 14 6 17 11 3 21), sp(8) ≤ 30 (witness 13 4 25 18 8 30 12 22 1 28 19 10 6 14 24 27 3 16 21 11 5 20 29 15 7 23 2 17 26 9). Lower bound: sp(k) ≥ (1.0003125−o(1))k²/e² (Theorem A, experiments/w3-lowerbound/proof.md). Paper draft: paper/superpatterns-notes.md.

## Asymptotic bounds
Upper: k² (Arratia 99) → 2k²/3 (Eriksson–Eriksson–Linusson–Wästlund 07, chessboard) → (k²+k)/2 (Miller 09, zigzag word over [k+1]) → ⌈(k²+1)/2⌉ (Engen–Vatter 21, zigzag restricted to [k] + tie-breaking).
  * Z. Hunter (arXiv 2108.05474, 2021) states "in forthcoming work [9] the author will show f(k) ≤ (15/32)k² + O(k)" — ref [9] "A new upper bound for superpatterns, in preparation". As of 2026-08 NO such paper is on arXiv. So constant<1/2 is *claimed but unpublished*.
Lower: k²/e² (trivial C(n,k) ≥ k!) → 1.000076·k²/e² (Chroman–Kwan–Singhal 21, encoding: for indices with large "width" t_{i+1}-t_{i-1} ≥ dn/k, store value π(i) instead of index t_i; they note using odd+even widths and exact large deviations would improve constant slightly, "unlikely to get much larger than 1/e² without new ideas").

## Conjectures
- Arratia: sp(k) ~ k²/e²  — DISPROVED (CKS).
- EELW: sp(k) ~ k²/2 — Hunter claims refuted (15/32) but unpublished.
- Alon: random perm of length (1/4+ε)k² is k-superpattern whp; best known He–Kwan 2020: n = 2000 k² log log k suffices. t(n) data (Engen–Vatter): 1,3,7,13,20,28,36,48 for n=1..8.
  - Our results (2026-08-29, all in paper §Random): c_τ = lim L_τ/√N; 0.7866 ≤ c_21 ≤ 1.140 (W17 renewal sweep / W12 canonical copies); c_τ ≥ 0.535 (S_3), ≥ 0.385 (S_4); universal absence κ=2.279; 72k²/800k² partial results toward n=O(k²) (Thm 8, Thm 5, Thm 9); lag lemma is FALSE (W18: thread framework capped on tilted grids); but every block-grid pattern incl. the family 𝓕 has threshold ≤ (π/8)k² (W11 Thm 10, corner greedy).
- Hunter Problem 3: is f(k;k+1) = (k²+k)/2 exactly (words over alphabet [k+1])? Hunter proved f(k;(1+o(1))k) = (1/2+o(1))k² (DFA random-walk method).
- Kleitman–Kwiatkowski: f(k;k) = k² − O(k^{7/4+ε}); exact 1,3,7,12,19,28,39 (k≤7), upper bound ⌈k² − 7k/3 + 19/3⌉ (Radomirović).
- Gupta rosary (circular, one direction): r(n) ≤ n²/2; proved for even n (Lecouturier–Zmiaikou 2012), odd n: r(n) < n²/2 + n/4 − 1, open. Bidirectional version (3n²/8+1/2) refuted by Hunter.
- EELW: perm of length (1+o(1))k²/4 containing all but exponentially small fraction of k-patterns exists → any proof that sp(k) ~ k²/2 must distinguish "all" from "almost all".

## Key constructions
- Arratia: k×k grid read column by column, bottom-up.
- Miller zigzag: Z_k = (1 3 5 …)(… 6 4 2)(1 3 5 …)… k runs, length k(k+1)/2 over [k+1]. Either π or π+1 embeds (score function s(p)+s(p+1)=1).
- Engen–Vatter: z_n = first n runs restricted to [n]; break ties so equal letters form a decreasing subsequence → ζ_n. Universal for odd n; for even n misses only n…21, fix by prepending a max. Proof: non-layered perms have a distant inverse-descent → decrement trick; layered handled by parity score walk.


## Results ledger of this project (2026-08-29) — positive AND negative; details in experiments/wN/{log,proof}.md and the paper

Positive (all independently verified by the coordinating session before entering the paper):
- Thm A: sp(k) ≥ (1.0003125−o(1))k²/e² (W3; Lean-verified). Thm C: 1.00483 (W7; first draft's lemma was FALSE, corrected); Thm C′: 1.00734 via exact Bernoulli/KL tail for the slot count (W25 Lemma B.1, verified; finite-k certified at k=1e5, 3e5).
- sp(7) ≤ 23, sp(8) ≤ 30 (W1; three independent checkers incl. Lean). Structured 7-superpattern of length 24 (W2).
- f(k;k+1) = (k²+k)/2 for k ≤ 5 (W4, SAT); Gupta rosaries: r(n) = ⌊n²/2⌋ for n ≤ 5, ≤ ⌊n²/2⌋ for n ≤ 11 (W4).
- t(7) = 37, t(9) ≈ 60, t(10) ≈ 70–72 (W5); c_τ = 2/|τ| numerically for |τ| ≤ 5 (W10).
- 0.7866 ≤ c_21 ≤ 1.140 (W17 renewal sweep / W12 canonical copies); c_τ ≥ 0.535 (S_3), ≥ 0.385 (S_4) (W17).
- Universal absence: every π ∈ S_k absent w.h.p. if k > 2.279√N (W12).
- Alon: Thm 8 (72k², all π with L_Δ ≤ k/3ln²k for all but k/3ln k shifts; W9); Thm 5 (800k², unions of ≤ e^28 runs,
  unconditional range r ≤ e^57; W13/W14); Thm 9 (speed N for fixed r; W11); Thm 10 (every block-grid pattern incl. the
  family 𝓕 has threshold ≤ (π/8)k²; W11); Thm 11 (EVERY π ∈ S_k has threshold ≤ 0.757k², failure e^{−ηk}; rigid rows
  give k² and the union bound (1+o(1))k² ln k; W19).
- Circular corollaries L_circ(8) ≤ 24, L_circ(9) ≤ 31 (from MD26 review).

Negative / dead ends (with the reason; each is a theorem or a brute-force-checked fact unless marked numerical):
- No (1/2−ε)k² construction from copy models, poly-many collapses, monotone-run/residue zigzags, merged halves, identical
  blocks (all ≥ k²/2 asymptotically; W2/W8). The 23/30 witnesses are NOT tie-broken words over [k+1] (W2).
- sp(7) = 22? SAT/CEGAR too slow (70 min–2 h per solve; still running, W6).
- Entropy statement (E) is FALSE (W14). The family 𝓕 defeats every chain-based hypothesis in all dihedral images (W15).
- The lag lemma is FALSE: coalescence costs e^{−O(lag)}, not e^{−lag²/k}; polylog threads at m = Ck cannot give
  n = O(k²) — He–Kwan's k log log k barrier reproduced for the thread framework (W18).
- κ cannot be pushed below 2.279 uniformly by canonical-copy/transfer methods; mixed leftmost/lowest rules are worse; RSK
  route inapplicable (W16). Level-2 lex-min gives 2.24 for the identity only (numerical).
- Renewal/greedy rules for c_21 cap at ≈ 0.84 (W17 Prop 4); the last 20% to c_21 = 1 needs block-to-block correlation.
- The corner greedy does NOT extend verbatim to arbitrary π (strips must be chains; W19 Prop 3.1). Every greedy or repaired
  greedy has failure speed ≤ min(k, strip height): cannot deliver the e^{−k ln k} per pattern the union bound needs (W19).
- NUMERICAL (W21, k ≤ 40, decided as far as numerics can): identity is the HARDEST pattern; random-π n_1/2/k² → ≈0.22±0.02
  (< 1/4), ratio rand/id .959→.881 decreasing, excess over k²/4 stops growing, log-log slope test; layered as hard as
  identity, tilted grids as easy as random. ⇒ 1/4 is the max over patterns; κ_univ ≈ 2.13 > 2.
- Certificate counting (W23): identity Dilworth bound (N+k)^k (e(k−1)²/(N−k+1))^N (rate ln(C/e), loss 0.60 at C=e);
  periodic word/block-grids fixed model: speed N/(3r²) at threshold 9r ln(3er) (factor r better than Thm 9).
  NEGATIVE: any bad-box-tolerance lemma has f ≤ 1/r ⇒ threshold ≥ ln r (Mirsky grids); fixed-model rate ≤ 1/r for all C;
  canonical covers don't beat e. Residual class still k² polylog k.
- W26 (Thm 13): speed-N bound for (12)^h via alternating-chain certificates: Pr ≤ e^{−ρ(C)N}, ρ>0 iff C>27.63 (k-uniform;
  first speed-N beyond monotone/box patterns). NEGATIVE: relaxation threshold 9/16 vs 1/4; exact Pareto coarse-graining
  costs e^{Θ(k³)}; r strips: C_0(r) ≈ 3.5 r³; nothing for the union bound over S_k.
- W27 (Thm 14, theory verified; numerics pending): coarse-graining + Mirsky on cells ⇒ speed-N tails for direct sums of
  bounded blocks ((21)^{k/2}: e^{−0.122N} for N ≥ 24k²; identity e^{−0.277N} for N ≥ 48k²) and for ALL of 𝒢(r,h) with
  rigid rows (rate N/(2.74 r²(2 ln r+2)) for N ≥ 16(2 ln r+2)k²) — but rate ∝ 1/(r² ln r), so e^{−Θ(k)} at r=h=√k.
  Barrier isolated: Mirsky needs a CHAIN of O(1)-cost gadgets; a grid with min(r,h)→∞ is a LATTICE. Exact facts: block
  splitting (bound at one N=C_0k² with exponent ≫ k ln k suffices); CP(1) false at k=4 (Av_7(1324)=2762>2761); CP(K>1)
  vacuous at fixed k ⇒ only per-point rates I_π(C) at N≍k² matter; relabelling identity p_π = constrained-LIS tail.
- W27 numerics (COMPLETED): hardest pattern at k ≤ 8 is 1⊕dec_{k−2}⊕1 (exact by my enumeration at n ≤ 10); patterns harder
  than id = ⊕-sums with a decreasing block (family of size e^{O(k)}); excess sub-linear in k ⇒ conjecture
  p_π(N) ≤ e^{ak} p_id(N) (rate deficit O(1/k)). CAVEAT: W27's SMC excess values are biased upward (Wilf-equivalent
  patterns 15432, 123654 show +0.3/+1.2) — magnitudes unreliable, signs at small n confirmed exactly.
- W24 (numerics, k=6 re-sampled by me): union-bound slack ln R at t(k) = 1.93, 2.59, 3.27, 3.98 (k=6..9), ≈0.7k ≈ 0.23 ln k!;
  ln R ≈ 0.4–0.5 at n=k², R→1 by 1.1k². Missing set heavy-tailed and clustered (adjacent transpositions ρ≈160–230 at
  t(7); dihedral 20–25; random pairs 12–16; reverse/complement of identity never co-miss). First moment off by e^{Θ(k)}
  at threshold — a hard-core / clustering correction is what a proof of the constant needs (→ W28).
- W28 (Prop 15, verified): witness reduction R ≤ E M²/μ = Σ p_π Λ_π/μ ≤ max_π Λ_π (Λ_π = E[M | π⊄σ_n]); if R = e^{o(k²)}
  (and ln μ drops Ω(1) per unit n — numerical/speed-N) the threshold constant IS the first-moment constant. Janson and
  Bonferroni are void at k=6,7 (Δ/μ = 20–430). NEGATIVE: no hard core (p_π within ×4; layered patterns hardest, not id);
  missing set is one diffuse cluster, NOT up-sets of missing (k−1)-patterns; R made in the far tail; M driven by local
  emptiness of σ (Spearman +0.42 with largest empty rectangle; +0.11 with LIS). id/rev co-miss impossible for
  n ≥ (k−1)²+1 (Erdős–Szekeres) — factor 2 only. Needed: #patterns killed by one empty rectangle of area ≍ 1/k² is e^{O(k)}.
- W29 (Thm 16): gap-reserve greedy (strips carry ARBITRARY sub-patterns; window = gap minus reserve β per unplaced
  value; leftmost point). Reduction proved for every π; for uniformly random π strips are i.i.d. uniform ⇒ threshold
  ≤ Ω_h k² with Ω_64 = 0.527, Ω_1024 = 0.515 (recomputed by me: 0.5265) — first typical-vs-worst separation (0.757).
  BARRIER: value-blind gap-window rules have Ω_h ≥ ½+1/(2h) (proved; the value-aware rule used respects it numerically
  but the proof's rank-independence step does not cover it — gap noted in w29 proof.md). Below ½ needs x-lookahead
  or a 2-D argument. Dead ends: diamond scores, absolute row targets, single strip h=k, HK-quasirandom, second moment.
- W30 (verified; mostly NEGATIVE): "patterns killed by an empty rectangle" is not defect-specific — random new point
  revives exactly 1−μ(n+1)/μ(n) ≈ 0.4 of M (exact identity), centre of largest empty rectangle ≈ 0.75 regardless of
  area/aspect, 9-point grid 0.96. Question = tail of M itself. PROVED: completion-cell characterisation; strip deletion
  E[M | Q empty] ≤ μ(n − min(w,h)); p_π(n−1) ≤ n p_π(n) ⇒ only e^{O(k ln^{3/2} k)} (e^{O(k√ln k)} if slope O(1), open).
  Deterministic version false (sp(6) witness + 1 point revives 0.88·6! of missing 7-patterns).
- W31 (Thm 17, verified; recursion re-implemented by me): value-aware x-lookahead inside the gap with exact mean-field
  cost-to-go Φ = V_{m_b}/(y−y_L)+V_{m_a}/(y_R−y), safe clock for freshness ⇒ random π contained at 0.465k² (certified
  Bellman constant; 0.4765 at h=64). ½ barrier FALSE for value-aware rules (h ≥ 20); all in-gap rules capped at
  ≈0.4623 in the fresh-window model (Bellman optimality). Next: information outside the current gap / 2-D construction.
- W37 (Thm 21, verified; exact Av_n tables and bubble-edge counts recomputed by my own brute force w37check.c).
  AGENT DIED MID-RUN (API credits) — proof.md is complete, results.md was never written (tables live in data/ +
  analyze.py). STRIP-REARRANGEMENT REFORMULATION (Lemma 1): π ⊆ Π_N ⇔ ∪_c E_c where E_c is a transversal increasing
  chain of the strip-restacked process; each T_{c,π} is measure preserving so Pr(E_c) = Pr(Σ γ_j/w_j < N) is
  π-INDEPENDENT — all the π-dependence is in the joint law of {E_c}; identity = perfectly correlated member.
  Lemma 5 (elementary): Av_n(id_a) ≤ (a−1)^{2n} by RSK column words ⇒ p_{id_a}(M) ≤ e^{−M+2(a−1)√M}, speed k² for
  every C > 4 with no LDP input. Thm 6/Cor 7 (box comparison): π = τ_1⊕ρ⊕τ_2 ⇒ p_π(N) ≤ p_ρ(N(1−2ε)²)+p_{τ_1}(Nε²)
  +p_{τ_2}(Nε²); so the empirically hardest π* = 1⊕dec_{k−2}⊕1 obeys the rate form vs the identity. THM 9 (folded as
  Thm 21(d)): for the class 𝒞_k of ⊕/⊖-sums of runs ≥ √k ln k with defects ≤ ln k/(8 ln ln k), total ≤ δk/3, count
  ≤ k^{1/4}: Pr(π ⊄ Π_N) ≤ e^{−c(δ)k ln²k} at N ≥ (1/4+δ)k² (conditional on Deuschel–Zeitouni; unconditional at
  (16+δ)k² via Lemma 5) — first class at Alon's constant where the union bound over k! CLOSES.
  Prop 10 (verified by my brute force): complementation is an involution on bubble-step edges reversing every strict
  comparison ⇒ #violations = #confirmations exactly at every k, n (I recomputed 12 = 12 at k=4 and 108 = 108 at k=5,
  n = 8, 9) — no inversion-monotone difficulty measure can exist; "towards id" = "away from dec" and dec ≡ id.
  DEAD ENDS recorded: FKG gives the wrong direction; no Slepian for indicator families (must saturate on Wilf
  classes); pathwise bubble merging FALSE (1324→1234 strict reverse for n ≥ 7); middle defects blocked by the
  window-area problem (thinning forces area Ω(1) ⇒ constant-factor N loss).
- W38 (negative, verified independently; agent DIED MID-RUN on API credits with §2 table "TBD"): the pattern-averaged
  PLAIN second moment on copies fails at Alon's constant. E_π E M_π²/μ² = k!·Pr(two random k-subsets collide) =: R_avg;
  my own MC reproduces their table (ln R_avg = 3.454/3.763/3.840/4.123/4.263 at k = 6..10, C = 0.25 vs their
  3.45/3.76/3.85/4.13/4.32), slope 0.167 per unit k ⇒ R_avg = e^{Θ(k)}, dominated by overlaps j/k ≈ 0.6–0.7.
  Heuristic rate function ⇒ C₂(plain) ≈ 1/2 (my check at C = 0.5 is noisy: slope 0.08 ± 0.04 over k = 6..10, so
  "marginal at 1/2" is NOT established). My earlier 1/(e²−1) ≈ 0.157 clustering heuristic was WRONG. Promising and
  UNFINISHED: leftmost-canonical copies Y_π give E[Y²]/(EY)² ≈ 20.6–24.2 for random π and 21.4 for the identity at
  k = 8, C = 0.25 (nearly pattern-uniform, mostly diagonal 1/EY), and the j = k−1 overlap term vanishes identically.
- W36 (Thm 20, verified line by line; Burke law, E K_n and certified constants recomputed by my own DP/simulator):
  BURKE PROPERTY of the cross-strip recursion G_s(a)=min_{x_p>a}[y_p+G_{s+1}(x_p)]. The compound-Poisson boundaries
  G^ρ (jump rate ρ, i.i.d. Exp(1/ρ) jumps, slope ρ²) are exactly stationary under one strip step, with per-strip cost
  Exp(1/ρ) (mean ρ) — proved by: D(a)=G'(a)−G^ρ(a) ~ Exp(1/ρ) (renewal equation + Grönwall; forces rate ρ ↔ mean ρ),
  D read leftward is a Markov jump process (rate ρ+x, up Exp(1/ρ), down uniform (0,x)) satisfying detailed balance
  against π(x)=ρ^{-1}e^{-x/ρ} iff ρθ=1, hence reversible; reversal swaps input and output jumps. Sandwiching the true
  boundary B_0(x)=x between G^ρ, ρ≷1, with Lundberg exponent |ρ−1/ρ| gives n−√(2n) ≤ E K_n ≤ n+√(2n)+1/2, so
  γ_∞ = 1 EXACTLY (W34 Conj 5.1 proved, both directions); subadditivity+Fekete sharpen this to E K_n ≥ n for every n,
  so C_b, C^mix_b ≥ 1/4 always (block lookahead of any depth is capped at 1/4 — a second barrier alongside Thm 19).
  Certified C^mix_b ≤ (1/2+(√(2b)+√(2b+2)+1)/(2(2b+1)))² ↓ 1/4 (0.3504 at b=64, 0.2507 at 10⁶) replaces W34's MC values.
  CONSEQUENCE: every tilted grid (12⋯r)^h and every 𝒢(r,h)-pattern with bounded strip revisits, min(r,h) ≥ (ln k)³, is
  contained at (1/4+ε)k² for every ε>0 — first non-monotone family at Alon's constant; closes the π/8 → 1/4 gap of
  Thms 10/12/18. CAVEAT (agent flagged it itself): no matching LOWER bound — grid LIS is only r+h−1 ≈ 2√k, so LIS-type
  lower bounds do not apply and the best valid one is the universal 0.1925k²; "exactly 1/4" holds for the mean-field
  fixed-strip full-lookahead model only. My checks: E K_n = 10.96/51.50/203.0 at n=10/50/200 (inside the bounds,
  E K_n−n ≈ 0.21√n); D(0) ~ Exp(ρ) for ρ=0.5,1,2 (KS p = 0.47/0.72/0.20); jumps of T_Ψ G^ρ: rate ρ ±0.5%, sizes
  Exp(mean ρ) (KS ≤ 0.010 on 10⁴–3.6·10⁴ jumps), gaps Exp(1/ρ), lag-1 correlations ≤ 0.027; E G^ρ_1(0) = nρ within 1.2 s.e.
- W35 (Lean, verified by my own lake build + axiom audit): Prop 15 (witness reduction), block-splitting core, Erdős–Szekeres
  disjointness formalised sorry-free. Not done: probabilistic block splitting p_π(N) ≤ p_π(M)^{⌊N/M⌋}.
- W34 (Thm 18, verified; constants re-simulated): CROSS-STRIP x-lookahead (block rule, blocks of b/b+1 visits, stationary
  renewal partition) gives block-grid/tilted-grid threshold ≤ C^mix_b = 0.345 (b=2) … 0.266 (b=64) < π/8, for min(r,h) ≥ ln³k.
  Round cost telescopes to a first-passage problem; scaling ⇒ x-part = y-part = E K/2. Full lookahead: γ_∞ = 1.000±0.002
  ⇒ mean-field fixed model threshold = 1/4 exactly (numerical) — W20 Conj 4.6 false for large h. Open: prove γ_∞ = 1
  (Burke-type stationarity). y-lookahead alone = W20 Bellman, capped at π/8. Typo caught: "n ≥ 2C k²" should be (1+ε)Ck².
- W32 (Thm 19, verified; NEGATIVE, decisive): EVERY sequential fresh-search rule (positions in order, point inside its
  value gap, conditionally-Poisson region), whatever it looks at, has E[consumption] ≥ V_k/(Ck) ⇒ cap ≈ 0.4623 for
  random π; anticipation of π worth 4e-5. Below 0.46 needs non-sequential (global/Hammersley-type) arguments.
- W33 (verified): exact one-point identities (slots / S_max / J_π); s_π ≤ ln(n/(k−1)); uniform lower bound on slope
  over a k²-window ⇔ speed-k² tails (as hard as the conjecture; false for μ); window-average of s_μ ≤ H_0(1/√C) = O(1);
  identity slope closed form ln((4C+1)²/(16C)) from DZ (checked against DZ's H_0); slope at TW-type threshold
  Θ((ln k/k)^{2/3}) ⇒ Prop 15 window O(a k^{5/3}); pointwise O(1) slope still open.
- Alon–Spencer toolbox (W22 review): Janson/extended Janson/Suen exponent ≤ C/2 at N=Ck² for ANY copy-event family
  (Δ ≥ μ²/C, single-point overlaps); Talagrand ≤ C/4; Azuma ≤ C/2; Kim–Vu vacuous; LLL only positivity. NOT capped:
  certificate counting (Dilworth cover ⇒ Pr(LIS<k) ≤ (e/C)^N, speed N) → try antichain-cover certificates for
  block-grid/periodic patterns; and measuring the union-bound slack R = E#missing / Pr(#missing>0).
- Tilted grids (W20, done): Thm 12 mean-field theorem — fixed-strip C^fix(r,h) ≤ C_mf(h) as r→∞, C_mf ↓ π/8; every
  fresh-quadrant rule capped at π/8 (Prop 3.1). NEGATIVE: no rigorous constant below π/8 for min(r,h)→∞; 2-strip DP is
  a Pareto front, no Hammersley structure. NUMERICAL: (12)^h fixed threshold 0.254 at k=256 (→≈0.22–0.23 < 1/4), free
  0.272 vs identity 0.291 at k=64 ⇒ identity is NOT the easiest pattern; diagonal r×r fixed 0.335 at 8×8.

## Files
lit/1810.08252.txt Engen–Vatter survey; lit/2004.02375.txt CKS lower bound; lit/2108.05474.txt Hunter small alphabets; lit/1710.04240.txt universal layered perms; lit/1308.0403.txt Bannister et al (321/132-avoiding superpatterns); lit/2602.09072.txt circular superpatterns (2026).
Bóna, Combinatorics of Permutations 3rd ed: Ch.5 Ex.19–23, Problems Plus 14–17, 20.
- W9 (2026-08-29, experiments/w9-alon-threads/): He–Kwan's thread overlap bound L_Δ·log²k refined to W_Δ(z) = max over Δ-shift chains of the leader's actual zero-runs (proof.md Lemma 3, tested numerically). Theorem 8: n = 72k² suffices w.h.p. for all π with L_Δ(π) ≤ k/(3 ln²k) for all but < k/(3 ln k) shifts Δ (exceptional set k!·e^{−Θ(k/ln k)}, vs k!·e^{−Θ(√k)} for HK's Q_k). log log k NOT removed: remaining gap = unions of r ∈ [C, ln⁴k] increasing runs on value intervals (count e^{Θ(k log log k)}, chains ≈ 1.3k/√r). Per-π chain accounting is capped at e^{−m ln 2} (log.md §4); cross-direction (row/column) threads are rigorously ≈independent but useless asymptotically.
- W13 (2026-08-29, experiments/w13-global-event/): the (qm)^L union bound of W9's global event replaced by a count of
  "ρ-staircase sets" (unions of ≤ ρ monotone chains; the leader's start cells along a shift chain form one with
  ρ = LDS(π|_A)): count (2e²Cρ²(k/L)²)^L, no log k (proof.md Lemma 1–3, Theorem 4). Theorem 5: n = 800k² w.h.p.
  contains every union of r increasing runs on value intervals (any r ≤ k/(2 ln k)) whose interleaving is
  "run-quasirandom" (fewer than k/(2ℓ_r) shifts with chains > k/λ_r, ℓ_r = ⌈(ln r+1)/29⌉, λ_r = O(ln² r)); no
  condition for r ≤ e^{28}; numerically random interleavings have F = ∅ (max_Δ L_Δ ≤ 1.5k/√r). Same for LDS(π) ≤ r
  with ℓ'_r = ⌈(2 ln r+1)/29⌉, up to r = k (= W9 Thm 8 with threshold 14.5k/ln²k). Exact gap (log.md §4): an entropy
  lemma (E) bounding #{π ∈ 𝓛_r with ≥ k/(2ℓ_r) long-chain shifts} ≤ e^{(29(ℓ_r−1)−1)k} (near-periodic interleavings),
  plus HK-structured maps whose chains have large LDS. "Shifts spaced by k/r" idea refuted numerically (Δ = h is the
  worst shift: thread coalescence for periodic words).

## Manjunath–D'Souza, Circular superpatterns (arXiv 2602.09072, v2 Aug 2026) — reviewed 2026-08-29
Circular k-superpatterns (patterns up to rotation). Results: L_circ(k) ≤ sp(k−1)+1 (Thm 3.1); zigzag over [k+1] with k−1 runs, length (k−1)(k+1)/2 (Thms 4.12/4.13; circular score S^c(σ)+S^c(σ⁺)=0, S^c≠0 for odd k); tie-broken permutation of length ⌈((k−1)²+1)/2⌉+1 for odd k (Thm 5.6). Closed form of Miller's score: C_xy = δ_xy − ½(p_x p_y+1) sgn(x−y) p_x (equivalent to W2's run-change identity). No new linear bounds, no lower bounds, no post-2021 refs. Our sp(7)≤23, sp(8)≤30 give L_circ(8)≤24, L_circ(9)≤31 (their 25, 34).
