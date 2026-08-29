"""Exp 3: numerical check of
  Lemma W : |T_t cap T_{t+D}| <= W_D(z) := max over D-shift chains A of sum_{a in A} (z_a + 1),
            z_a = zero-run of the LEADER (thread t) at element a  (deterministic claim).
  Lemma HV: |T_H cap T_V| <= min(#rows visited by H, #cols visited by V) <= k.
Also compares W_D(z) with He-Kwan's L_D * (Z+1) and with the actual overlap, on many random instances,
including small m where the leader often fails (the regime that matters)."""
import numpy as np
from threads import *

rng = np.random.default_rng(3)


def leader_profile(T, k):
    """zero-run z_a of a thread at each element a (elements not reached get z=0 and are excluded)."""
    z = {}
    for c, v, e in zip(T['cells'], T['vals'], T['elems']):
        z[e] = z.get(e, 0) + (1 - v)   # count zeros; the +1 (the one) is added separately
    return z


def W_delta(pi, d, z):
    """max over D-shift chains A (pairs (a,b), pi(a)=pi(b)+D, a's and b's increasing) of sum (z_a+1)
    over a in A, restricted to elements a reached by the leader.  Weighted LIS via O(k^2) DP."""
    k = len(pi)
    inv = np.empty(k, dtype=int); inv[pi] = np.arange(k)
    pairs = [(a, inv[pi[a] - d]) for a in range(k) if pi[a] - d >= 0 and a in z]
    pairs.sort()
    best = 0
    f = []
    for i, (a, b) in enumerate(pairs):
        w = z[a] + 1
        m = w
        for j in range(i):
            if pairs[j][1] < b and f[j] + w > m:
                m = f[j] + w
        f.append(m); best = max(best, m)
    return best


violW = violHV = 0
rows = []
for rep in range(400):
    k = int(rng.integers(6, 60))
    m = int(rng.integers(int(1.5 * k), 6 * k))
    q = 2 * k
    kind = rep % 4
    if kind == 0:
        pi = rng.permutation(k)
    elif kind == 1:
        pi = np.arange(k)
    elif kind == 2:
        pi, _ = runs_pattern(k, int(rng.integers(2, 8)), rng)
    else:
        r = int(rng.integers(2, 6)); pi, _ = runs_pattern(k, r, rng, word=periodic_word(k, r))
    M = rng.integers(0, 2, size=(q, m))
    d = int(rng.integers(1, k))
    t = int(rng.integers(0, k - d + 1))
    T1 = run_thread(M, pi, 'H', t); T2 = run_thread(M, pi, 'H', t + d)
    st = overlap_stats(T1, T2)
    z = leader_profile(T1, k)
    W = W_delta(pi, d, z)
    LD = L_delta(pi, d); Z = max_zero_run(M)
    if st['shared'] > W:
        violW += 1; print("VIOL W", k, m, d, st, W)
    rows.append((kind, k, m, int(not T1['ok']), st['shared'], W, LD * (Z + 1), m))
    # HV lemma
    s = int(rng.integers(0, m - k + 1))
    TV = run_thread(M, pi, 'V', s)
    hv = overlap_stats(T1, TV)
    nrowsH = len(set(y for y, x in T1['cells'])); ncolsV = len(set(x for y, x in TV['cells']))
    if hv['shared'] > min(nrowsH, ncolsV):
        violHV += 1; print("VIOL HV", k, m, hv, nrowsH, ncolsV)
print("violations: Lemma W", violW, " Lemma HV", violHV, " (over 400 random instances)")
rows = np.array(rows)
names = ['uniform', 'identity', 'runs-rand', 'runs-periodic']
print("kind            n   leader-fail  mean shared  mean W   mean L_D(Z+1)  mean m   | given leader fails: shared, W")
for kd in range(4):
    R = rows[rows[:, 0] == kd]
    F = R[R[:, 3] == 1]
    print(f"{names[kd]:<14} {len(R):4}   {R[:,3].mean():.2f}      {R[:,4].mean():7.1f}  {R[:,5].mean():7.1f}   {R[:,6].mean():9.1f}   {R[:,7].mean():6.1f}   |  "
          f"{F[:,4].mean() if len(F) else float('nan'):7.1f}  {F[:,5].mean() if len(F) else float('nan'):7.1f}   (n={len(F)})")
