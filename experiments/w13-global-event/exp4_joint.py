"""Exp 4 (W13): joint failure of ell=3 threads spaced by D vs product, pi in L_k^{(r)},
k=36, m=q=72 (single failure ~0.45).  D = 1, h/2, h, h+1, 2h+1."""
import sys, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import runs_pattern, periodic_word, run_thread
rng = np.random.default_rng(3)
k = 36; q = 72; m = 72; ell = 3; N = 4000
for r in [3, 6, 9]:
    h = k // r
    for wtype in ['rand', 'per']:
        word = periodic_word(k, r) if wtype == 'per' else None
        pi, w = runs_pattern(k, r, rng, word=word)
        for D in [1, max(1, h // 2), h, h + 1, 2 * h + 1]:
            if D * (ell - 1) > k: continue
            allf = 0; single = 0
            for rep in range(N):
                M = rng.integers(0, 2, size=(q, m))
                t0 = int(rng.integers(0, k - D * (ell - 1) + 1))
                fails = [not run_thread(M, pi, 'H', t0 + i * D)['ok'] for i in range(ell)]
                single += fails[0]; allf += all(fails)
            p = single / N; pa = allf / N
            print(f"r={r} h={h:<2} w={wtype:<4} D={D:<2} P(fail)={p:.3f} P(all {ell} fail)={pa:.4f} ratio={pa/p**ell if p>0 else 0:.2f}")
