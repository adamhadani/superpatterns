"""Exp 2: cross-direction threads (H, Hr, V, Vr).
(a) deterministic checks: |T_H cap T_Hr| <= 1, |T_V cap T_Vr| <= 1, shared zeros between an
    H-type and a V-type thread <= min(ones)+1 (each shared zero is followed by a fresh one of both).
(b) joint failure rates at small k, m, q vs. products of marginals."""
import sys
import numpy as np
from threads import *

rng = np.random.default_rng(2)

# (a) deterministic checks on many random pi (uniform and structured) and M
viol = 0
maxHV = 0
maxHVz = 0
for rep in range(300):
    k = int(rng.integers(5, 40))
    q = int(rng.integers(k + 2, 4 * k))
    m = int(rng.integers(k + 2, 4 * k))
    if rep % 3 == 0:
        pi = rng.permutation(k)
    elif rep % 3 == 1:
        pi, _ = runs_pattern(k, int(rng.integers(1, 5)), rng)
    else:
        pi = np.arange(k)
    M = rng.integers(0, 2, size=(q, m))
    t = int(rng.integers(0, q - k + 1))
    s = int(rng.integers(0, m - k + 1))
    TH = run_thread(M, pi, 'H', t); THr = run_thread(M, pi, 'Hr', t)
    TV = run_thread(M, pi, 'V', s); TVr = run_thread(M, pi, 'Vr', s)
    a = overlap_stats(TH, THr); b = overlap_stats(TV, TVr)
    if a['shared'] > 1 or b['shared'] > 1:
        viol += 1
    for A in (TH, THr):
        for B in (TV, TVr):
            st = overlap_stats(A, B)
            maxHV = max(maxHV, st['shared'])
            maxHVz = max(maxHVz, st['zeros'])
            if st['zeros'] > min(A['ones'], B['ones']) + 1:
                viol += 1
                print("VIOLATION", k, q, m, st, A['ones'], B['ones'])
print(f"(a) violations of deterministic lemmas: {viol};  max |H-type cap V-type| = {maxHV}, max shared zeros = {maxHVz}")

# (b) joint failure rates
k = int(sys.argv[1]) if len(sys.argv) > 1 else 12
q = m = int(sys.argv[2]) if len(sys.argv) > 2 else 30
N = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
print(f"(b) k={k} q=m={m} samples={N}")
for name, pi in [('identity', np.arange(k)), ('runs r=2 rand', runs_pattern(k, 2, rng)[0]),
                 ('runs r=3 periodic', runs_pattern(k, 3, rng, word=periodic_word(k, 3))[0]),
                 ('uniform random', rng.permutation(k))]:
    cnt = np.zeros(4, dtype=int)   # marginal failures H, Hr, V, Vr
    joint = {'H&Hr': 0, 'H&V': 0, 'H&Vr': 0, 'all4': 0, 'H&H+3': 0, 'H&H+k/2': 0}
    for rep in range(N):
        M = rng.integers(0, 2, size=(q, m))
        t = int(rng.integers(0, q - k - k // 2))
        s = int(rng.integers(0, m - k))
        f = [not run_thread(M, pi, kd, sh)['ok'] for kd, sh in (('H', t), ('Hr', t), ('V', s), ('Vr', s))]
        f2 = not run_thread(M, pi, 'H', t + 3)['ok']
        f3 = not run_thread(M, pi, 'H', t + k // 2)['ok']
        cnt += np.array(f, dtype=int)
        joint['H&Hr'] += f[0] and f[1]; joint['H&V'] += f[0] and f[2]; joint['H&Vr'] += f[0] and f[3]
        joint['all4'] += all(f); joint['H&H+3'] += f[0] and f2; joint['H&H+k/2'] += f[0] and f3
    p = cnt / N
    print(f"  {name:<18} P(H fail)={p[0]:.4f} P(V fail)={p[2]:.4f}  "
          f"H&Hr={joint['H&Hr']/N:.5f} (prod {p[0]*p[1]:.5f})  H&V={joint['H&V']/N:.5f} (prod {p[0]*p[2]:.5f})  "
          f"H&Vr={joint['H&Vr']/N:.5f}  all4={joint['all4']/N:.6f} (prod {np.prod(p):.6f})  "
          f"H&H+3={joint['H&H+3']/N:.5f}  H&H+k/2={joint['H&H+k/2']/N:.5f}")
