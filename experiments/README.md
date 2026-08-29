# Experiments / workstreams

Each folder is one workstream. Convention: `log.md` = chronology, numerics and dead ends (with reasons);
`proof.md` = theorem statements with complete proofs (only what has been verified by the coordinating
session appears in the paper); tools are C (`cc -O2`) or Python 3; raw outputs are `*.txt`/`*.out`.

| Folder | Topic | Outcome |
|:--|:--|:--|
| `w1-search` | Simulated-annealing search for short k-superpatterns; fast containment checker `sp` | sp(7) ≤ 23, sp(8) ≤ 30 witnesses (Thm 2) |
| `w2-construction` | Structured / zigzag / tie-broken-word constructions; can anything beat k²/2? | Structured 7-superpattern of length 24; Arnarson's 17 explained; rigorous negatives N1–N3 |
| `w3-lowerbound` | Stable encodings + exponential tilt: sp(k) ≥ λk²/e² | Theorem A (λ = 1.0003125), Lean-verified |
| `w4-alphabet-rosary` | SAT for words over [k+1] and Gupta rosaries | f(k;k+1) = (k²+k)/2 for k ≤ 5 (Thm 3); rosaries n ≤ 11 (Thm 4) |
| `w5-random` | t(n) sampling; c_τ numerics | t(7) = 37, t(9) ≈ 60, t(10) ≈ 70–72 |
| `w6-exact-sp7` | SAT/CEGAR for sp(7) = 22? | Running (iteration 4); re-proves sp(4) = 9, sp(5) = 13 |
| `w7-slots` | Value-slot refinement of Theorem A | Theorem C (λ = 1.00483); first draft's lemma was false — corrected |
| `w8-rows` | Identical-block / row constructions | Identical blocks cap at 5039/5040 (theorem) |
| `w9-alon-threads` | He–Kwan threads sharpened | Theorem 8 (72k², exceptional set k!e^{−Θ(k/ln k)}) |
| `w10-alon-numerics` | c_τ = 2/|τ| numerics | Supported for all τ of length ≤ 5 |
| `w11-strips` | Unions of runs, strip models; block-grid patterns | Theorem 9 (speed N, fixed r); **Theorem 10**: every block-grid pattern has threshold ≤ (π/8)k² |
| `w12-c21` | Canonical copies, Mecke formula, transfer operator | 0.598 ≤ c₂₁ ≤ 1.140; universal κ = 2.279 |
| `w13-global-event` | Staircase global event | Theorem 5 (800k², unions of ≤ e^28 runs) |
| `w14-entropy` | Entropy lemma (E) for structured interleavings | (E) is false; Prop 3 (range r ≤ e^57) |
| `w15-symmetry` | Dihedral images; hard family 𝓕 | 𝓕 defeats all chain-based hypotheses |
| `w16-universal` | Push κ toward 2; is the identity the easiest pattern? | No improvement; identity is *hardest* at k ≤ 20 (numerics) |
| `w17-hammersley` | c₂₁ via renewal sweeps | c₂₁ ≥ 0.7866; c_τ ≥ 0.535 (S₃), ≥ 0.385 (S₄); method capped at ≈ 0.84 |
| `w18-lag` | Lag lemma for thread overlap | **False**: linear loss in lag; thread framework capped on tilted grids |
| `w19-general-greedy` | Corner greedy for arbitrary π; speed of greedy embeddings | Verbatim extension is false (works iff strips are chains); reserve greedy gives universal per-pattern threshold 0.757k² for all of S_k (numerical constant, reduction proved); rigid rows: every π at k², union bound at (1+o(1))k²(ln k+ln ln k); two-phase repair; greedy/repair barrier: speed ≤ min(k,h) |
| `w20-hammersley-grid` | Tilted grids: mean-field / Hammersley coupling | Theorem 12 (C_mf(h) ↓ π/8; fresh-quadrant barrier) |
| `w21-threshold-numerics` | n_{1/2}(π)/k² for random vs identity, k ≤ 40 | Identity is the hardest pattern; random limit ≈ 0.22 ± 0.02 |
| `w22-probabilistic-method-review` | Alon–Spencer toolbox vs. our gap | Janson/Talagrand/Azuma all capped at O(C) exponent; certificate counting uncapped |
| `w23-certificates` | Dilworth/Mirsky certificate counting | Identity (e/C)^N; periodic word speed N/(3r²); box tolerance f ≤ 1/r (negative) |
| `w24-union-slack` | Union-bound slack R = E[M]/Pr(M>0), k = 5–9 | ln R ≈ 0.7k at threshold; missing patterns cluster |
| `w25-asymptopia-review` | Spencer's *Asymptopia* vs. our tools | Theorem C′ (λ = 1.00734 via exact Bernoulli tail) |
| `w26-pareto-ld` | Pareto-front / alternating-chain certificates for (12)^h | Theorem 13 (speed N for C > 27.63) |
| `w27-comparison` | Comparison principle "identity hardest" | Theorem 14 (Mirsky on cells: speed N for bounded-block sums and 𝒢(r,h)); CP(1) false at k = 4; rate-form CP* |
