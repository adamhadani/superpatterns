# W31 — value-aware x-lookahead for a random pattern: threshold < ½·k²

Result: for a uniformly random π ∈ S_k, Pr(π ⊆ Π_{Ck²}) → 1 for every C > 0.4649 (certified; 0.4765 with
strips of 64 values).  Reduction PROVED (proof.md Thm 2.1), constant certified by a monotone quadrature
(proof.md Lemma 3.2, dp_cert.py).  The class of gap rules is capped at ≈ 0.4623 (proof.md Thm 4.1).

Files
- proof.md     — theorems with complete proofs (rule definition, reduction, certified constants, Bellman optimality).
- results.md   — all numbers (Bellman values, certified bounds, end-to-end simulation).
- log.md       — chronology, ideas, dead ends.
- dp.py        — Bellman recursion V_n (ε = 0), Gauss–Legendre; writes dp_V.txt; `python3 dp.py 2000` (≈ 4 min).
- dp_cert.py   — certified upper bounds V̄_n for the margin rule; `python3 dp_cert.py NMAX EPS 40000`
                 (writes dp_cert_eps{EPS}.txt; n ≤ 512 at ε = 0.02 ≈ 6 min).  Outputs: cert_eps*.out.
- validate2d.py — end-to-end run on a real Poisson process and a real random π:
                 `python3 validate2d.py h m C trials eps [seed]` (reads dp_cert_eps{eps}.txt).  Outputs: val_h*.out.
- freeshape_lb.py — Monte-Carlo of the free-shaping lower bound (heuristic), `python3 freeshape_lb.py h samples`.

Rerun everything (≤ 3 cores, ≈ 15 min):
    python3 dp.py 2000
    python3 dp_cert.py 160 0 40000; python3 dp_cert.py 160 0.05 40000; python3 dp_cert.py 512 0.02 40000
    for C in 0.46 0.48 0.50 0.52 0.55; do python3 validate2d.py 64 32 $C 10 0.05 7; done
    for h in 16 64 256; do python3 freeshape_lb.py $h 2000; done
Dependencies: python3 + numpy only.
