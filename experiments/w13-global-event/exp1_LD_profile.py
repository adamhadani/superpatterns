"""Exp 1 (W13): for pi in L_k^{(r)} (r runs on value intervals), profile of L_Delta over all Delta.
Question: how many Delta have L_Delta(pi) > k/(K ln^2 r)?  (hypothesis of Theorem 8' needs
|F| < k/(4 ell), ell ~ ln r).  Random w vs periodic w vs periodic-with-defects."""
import sys, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import runs_pattern, periodic_word, L_delta

rng = np.random.default_rng(7)

def profile(pi):
    k = len(pi)
    return np.array([L_delta(pi, d) for d in range(1, k)])

def defect_word(k, r, eps, rng):
    """periodic word with a fraction eps of positions randomly permuted (stays balanced)."""
    w = periodic_word(k, r).copy()
    idx = np.flatnonzero(rng.random(k) < eps)
    w[idx] = w[rng.permutation(idx)]
    return w

for k in [200, 400]:
    for r in [4, 8, 16, 32, 64]:
        h = k // r
        for wtype in ['rand', 'per', 'def0.1', 'def0.3']:
            if wtype == 'rand':
                pi, w = runs_pattern(k, r, rng)
            elif wtype == 'per':
                pi, w = runs_pattern(k, r, rng, word=periodic_word(k, r))
            else:
                eps = float(wtype[3:])
                pi, w = runs_pattern(k, r, rng, word=defect_word(k, r, eps, rng))
            L = profile(pi)
            lnr = np.log(r)
            thr1 = k / (3 * lnr**2)
            thr2 = 1.5 * k / np.sqrt(r)
            print(f"k={k} r={r} h={h} w={wtype:<6} maxL/k={L.max()/k:.3f} L_1/k={L[0]/k:.3f} "
                  f"L_h/k={L[h-1]/k:.3f} mean/k={L.mean()/k:.3f} "
                  f"#D:L>k/(3ln^2 r)={int((L>thr1).sum()):4d} #D:L>1.5k/sqrt r={int((L>thr2).sum()):4d} "
                  f"#D<h with L>1.5k/sqrt r={int((L[:h]>thr2).sum())}")
