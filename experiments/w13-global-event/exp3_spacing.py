"""Exp 3 (W13): does spacing shifts by >= h = k/r (run height) kill overlaps for pi in L_k^{(r)}?
Measures for two threads t, t+D: shared cells (mean, max), P(shared>0), and the conditional
overlap given the leader fails (rejection sampling at small m), for D < h and D >= h; random
and periodic w.  Then joint failure ratio Pr(all ell fail)/Pr(fail)^ell for shifts spaced by D."""
import sys, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import runs_pattern, periodic_word, run_thread, L_delta

rng = np.random.default_rng(5)
k = 48; q = 2 * k
for r in [4, 8, 12]:
    h = k // r
    for wtype in ['rand', 'per']:
        word = periodic_word(k, r) if wtype == 'per' else None
        pi, w = runs_pattern(k, r, rng, word=word)
        for m in [3 * k, 6 * k]:
            for D in [1, h // 2, h, h + 1, 2 * h + 1, 5 * h + 2]:
                if D >= k // 2: continue
                sh = []; shf = []; nf = 0; N = 600
                for rep in range(N):
                    M = rng.integers(0, 2, size=(q, m))
                    t = int(rng.integers(0, k // 2 - D + 1)) if k//2 - D >= 0 else 0
                    T1 = run_thread(M, pi, 'H', t); T2 = run_thread(M, pi, 'H', t + D)
                    S2 = set(T2['cells'])
                    s = sum(1 for c in T1['cells'] if c in S2)
                    sh.append(s)
                    if not T1['ok']:
                        shf.append(s); nf += 1
                sh = np.array(sh)
                print(f"r={r:<2} h={h:<2} w={wtype:<4} m={m:<3} D={D:<3} L_D={L_delta(pi,D):<3} "
                      f"shared mean={sh.mean():6.2f} max={sh.max():3d} P(>0)={np.mean(sh>0):.2f} "
                      f"| leader-fail n={nf:3d} mean shared|fail={np.mean(shf) if shf else float('nan'):6.2f} max={max(shf) if shf else 0}")
