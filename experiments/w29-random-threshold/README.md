# W29 — containment threshold of a uniformly random pattern (gap-reserve greedy)

Files
- proof.md    — Theorem 2.1 (reduction, every π), Theorem 3.2 (random π: threshold ≤ Ω_h k², annealed + quenched),
                Theorem 4.1 (½ barrier for all gap-window rules).  PROVED except the numerical value of Ω_h.
- results.md  — tables of Ω_h(β, w, rule) from strip.c, Chernoff exponents, 2-D end-to-end validation.
- log.md      — chronology, dead ends.
- strip.c     — y-only simulation of one strip with a uniformly random sub-pattern; prints Ω_h = E[Σ 1/W_t]/h,
                sd, and (optional 8th arg C) the Chernoff exponent per point from the window-MGF.
                usage: ./strip h w beta mode wmin nsamp seed [C]   (mode 0 row-centre band, 1 proportional band, 2 no band)
- validate2d.py — the actual 2-D greedy on Poisson points with a random π; asserts the output is a copy of π.
- sweep1.sh, sweep2.sh, sweep3.sh — parameter sweeps (outputs sweep*.out); validate2d.out.

Rerun:  gcc -O2 -o strip strip.c -lm; ./sweep2.sh; ./sweep3.sh (≈ 10 min on 3 cores);
        python3 validate2d.py 400 40 0.6 3 0.8 20 2
