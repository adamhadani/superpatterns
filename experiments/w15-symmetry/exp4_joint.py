"""Exp 4 (W15): joint failure ratio Pr(all 3 fail)/Pr(fail)^3 for shifts (0, D, 2D), m = 2.3k, k = 400,
tilted grid vs block-perturbed grid. Lag = e*r + d for D = d*h + e (r = h = 20)."""
import sys, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import run_thread, tilted_grid
from exp1_symmetry import block_perturbed_grid
rng = np.random.default_rng(4)
r = h = 20; k = r*h; q = 2*k; m2 = 2*k + 28; trials = 400
for name, pi in [("tilted grid 20x20", tilted_grid(20)), ("block-perturbed eps=0.2", block_perturbed_grid(r, h, 0.2, rng))]:
    for D in [1, 5, 20, 21, 100, 105]:
        f = 0; f3 = 0
        for _ in range(trials):
            M = rng.integers(0, 2, size=(q, m2), dtype=np.int8)
            oks = [run_thread(M, pi, 'H', s)['ok'] for s in (0, D, 2*D)]
            f += sum(1 for o in oks if not o); f3 += all(not o for o in oks)
        pf = f/(3*trials); p3 = f3/trials
        d, e = divmod(D, h)
        print(f"  {name:<26} D={D:3d} (lag={e*r+d:3d}): P(fail)={pf:.3f} P(all3 fail)={p3:.3f} ratio={p3/pf**3 if pf>0 else float('nan'):.2f}")
