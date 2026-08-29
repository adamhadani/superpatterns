"""Exp 4: amplification of failure for l H-threads (shifts t, t+D, ..., t+(l-1)D) and for H+V,
in a regime where single-thread failure is common (m ~ 2k), for identity / runs / uniform pi.
Reports P(all fail) / P(fail)^l : 1 = independent, >1 = positively correlated (riding)."""
import sys
import numpy as np
from threads import *

rng = np.random.default_rng(4)
k = int(sys.argv[1]) if len(sys.argv) > 1 else 30
m = int(sys.argv[2]) if len(sys.argv) > 2 else 60
N = int(sys.argv[3]) if len(sys.argv) > 3 else 6000
q = 2 * k
print(f"k={k} m={m} q={q} samples={N}")
pats = [('identity', np.arange(k)),
        ('runs r=2 rand', runs_pattern(k, 2, rng)[0]),
        ('runs r=5 rand', runs_pattern(k, 5, rng)[0]),
        ('runs r=5 periodic', runs_pattern(k, 5, rng, word=periodic_word(k, 5))[0]),
        ('tilted grid', tilted_grid(int(round(k ** 0.5)))) if int(round(k ** 0.5)) ** 2 == k else ('uniform2', rng.permutation(k)),
        ('uniform', rng.permutation(k))]
for name, pi in pats:
    kk = len(pi)
    for D in [1, 3, 8]:
        l = 4
        if (l - 1) * D + kk > q:
            continue
        cnt = np.zeros(l); allf = 0; hv = 0; hf = 0; vf = 0
        for rep in range(N):
            M = rng.integers(0, 2, size=(q, m))
            t = int(rng.integers(0, q - kk - (l - 1) * D + 1))
            f = [not run_thread(M, pi, 'H', t + i * D)['ok'] for i in range(l)]
            cnt += f; allf += all(f)
            if D == 1:
                s = int(rng.integers(0, m - kk + 1))
                v = not run_thread(M, pi, 'V', s)['ok']
                hf += f[0]; vf += v; hv += (f[0] and v)
        p = cnt / N
        line = f"  {name:<18} D={D}: P(fail)={p.mean():.3f}  P(all {l} fail)={allf/N:.5f}  ratio to prod={allf/N/np.prod(p):.2f}"
        if D == 1:
            line += f"   | H&V: {hv/N:.4f} vs prod {hf*vf/N/N:.4f} ratio {hv/N/(hf*vf/N/N+1e-12):.2f}"
        print(line, flush=True)
