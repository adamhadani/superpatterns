import numpy as np, itertools
from fpp import run
# brute force: regenerate the same strips with the same rng sequence as run() and enumerate all paths
def brute(n, X, Y, seed):
    rng = np.random.default_rng(seed)
    strips = []
    for s in range(n, 0, -1):
        m = rng.poisson(X*Y); x = np.sort(rng.uniform(0, X, m)); y = rng.uniform(0, Y, m)
        strips.append((x, y))
    strips.reverse()
    best = np.inf
    def rec(s, a, acc):
        nonlocal best
        if s == n:
            best = min(best, acc + a); return
        x, y = strips[s]
        for i in range(len(x)):
            if x[i] > a: rec(s+1, x[i], acc + y[i])
    rec(0, 0.0, 0.0)
    return best
bad = 0
for seed in range(300):
    n = 1 + seed % 4
    G, us, vs = run(n, 3.0, 2.0, seed)
    B = brute(n, 3.0, 2.0, seed)
    if not (np.isinf(G) and np.isinf(B)) and abs(G - B) > 1e-9: bad += 1; print("MISMATCH", seed, n, G, B)
    if not np.isinf(G) and abs(us.sum() + vs.sum() - G) > 1e-9: bad += 1; print("PATH MISMATCH", seed, n, G, us.sum()+vs.sum())
print("mismatches:", bad)
