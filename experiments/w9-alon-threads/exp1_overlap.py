"""Exp 1: H-H overlaps for structured pi (unions of r increasing runs on value intervals).
Compares |T_t cap T_t'| with He-Kwan's bound L_Delta * Z and the refined bound (#intervals)*Z."""
import sys
import numpy as np
from threads import *

rng = np.random.default_rng(1)
k = int(sys.argv[1]) if len(sys.argv) > 1 else 200
C = 5
m = C * k
q = 2 * k
print(f"k={k} m={m} q={q}")
print("r   word  Delta  L_D   Z   shared(mean,max)  zeros  intervals(mean,max)  L_D*Z  int*Z   fail1 fail2")
for r in [1, 2, 3, 5, 10, 20, 50]:
    for wtype in ['rand', 'per']:
        if r == 1 and wtype == 'per':
            continue
        word = periodic_word(k, r) if wtype == 'per' else None
        pi, w = runs_pattern(k, r, rng, word=word)
        for d in [1, 3, max(1, k // (4 * r)), k // 3]:
            LD = L_delta(pi, d)
            sh, zs, its, f1, f2 = [], [], [], 0, 0
            Zs = []
            for rep in range(20):
                M = rng.integers(0, 2, size=(q, m))
                t = rng.integers(0, k - d)
                T1 = run_thread(M, pi, 'H', t)
                T2 = run_thread(M, pi, 'H', t + d)
                st = overlap_stats(T1, T2)
                sh.append(st['shared']); zs.append(st['zeros']); its.append(st['intervals'])
                Zs.append(max_zero_run(M)); f1 += (not T1['ok']); f2 += (not T2['ok'])
            Z = int(np.mean(Zs))
            print(f"{r:<3} {wtype:<5} {d:<6} {LD:<5} {Z:<3} {np.mean(sh):7.1f} {max(sh):5}  {np.mean(zs):6.1f} "
                  f"{np.mean(its):7.1f} {max(its):4}   {LD*Z:6} {int(np.mean(its))*Z:6}   {f1:3} {f2:3}")
