"""W34: exact first-passage DP for the mean-field infinite-lookahead round problem.

Strips s = 1..n, each an independent Poisson process of intensity 1 on [0, X] x [0, Y].
G_s(a) = min_{p in strip s, x_p > a} [ y_p + G_{s+1}(x_p) ],   G_{n+1}(x) = x.
gamma_inf ~ G_1(0)/n  (cost per strip = x-increment + y-increment, intensity 1).
Also records the optimal path's mean x-increment and y-increment separately.
"""
import numpy as np, sys, time

def run(n, X, Y, seed, keep_path=True):
    rng = np.random.default_rng(seed)
    # G_{n+1}(x) = x : represent as breakpoints=None meaning identity
    bx = None; bv = None
    # to recover the path we store per strip the arrays (x sorted, best value, argmin index in next strip)
    store = []
    for s in range(n, 0, -1):
        m = rng.poisson(X * Y)
        x = np.sort(rng.uniform(0, X, m)); y = rng.uniform(0, Y, m)
        if bx is None:
            val = y + x
            nxt = None
        else:
            idx = np.searchsorted(bx, x, side='right')  # first breakpoint > x
            g = np.where(idx < len(bx), bv[np.minimum(idx, len(bx) - 1)], np.inf)
            val = y + g
            nxt = idx
        # suffix minimum over points with x_p > a: G_s(a) = suffmin[first index with x > a]
        suff = np.minimum.accumulate(val[::-1])[::-1]
        arg = np.empty(m, dtype=np.int64)
        # argmin of suffix: compute via reversed cumulative argmin
        best = np.inf; bi = -1
        rv = val[::-1]
        ra = np.empty(m, dtype=np.int64)
        # vectorised: indices where suffix min changes
        # simpler loop-free approach: use np.minimum.accumulate positions
        chg = np.r_[True, rv[1:] < np.minimum.accumulate(rv)[:-1]]
        pos = np.where(chg, np.arange(m), 0)
        pos = np.maximum.accumulate(pos)
        ra = pos
        arg = (m - 1 - ra)[::-1]
        if keep_path:
            store.append((x, y, arg, nxt))
        bx, bv = x, suff
    # G_1(0)
    G = bv[0] if len(bv) else np.inf
    # recover path
    us = []; vs = []
    if keep_path and np.isfinite(G):
        store.reverse()
        a = 0.0
        # first strip: index arg[0] (first breakpoint > 0 is index 0)
        j = store[0][2][0]
        for s in range(n):
            x, y, arg, nxt = store[s]
            us.append(x[j] - a); vs.append(y[j]); a = x[j]
            if s + 1 < n:
                j2 = nxt[j]  # first index in next strip with x > x[j]
                j = store[s + 1][2][j2]
    return G, np.array(us), np.array(vs)

if __name__ == '__main__':
    n = int(sys.argv[1]); X = float(sys.argv[2]); Y = float(sys.argv[3]); seed = int(sys.argv[4])
    t = time.time()
    G, us, vs = run(n, X, Y, seed)
    b = n // 10
    print(f"n={n} X={X} Y={Y} seed={seed}  G1(0)/n={G/n:.5f}  "
          f"mean u={us.mean():.4f} mean v={vs.mean():.4f}  (interior u={us[b:-b].mean():.4f} v={vs[b:-b].mean():.4f}) "
          f"gamma_int={(us[b:-b]+vs[b:-b]).mean():.5f}  max x={us.sum():.1f}  C*=gamma^2/4={(G/n)**2/4:.5f}  t={time.time()-t:.1f}s")
