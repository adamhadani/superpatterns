"""W36: validate the suffix-minimum DP of verify.py against brute-force path enumeration on small instances.
K_n = min { x_n + sum y_s } over p_s in Psi_s, x_1 < ... < x_n.  Prints max |DP - brute| over R instances."""
import numpy as np, itertools, sys
import verify  # reuse step()

rng = np.random.default_rng(7)
verify.rng = rng


def brute(strips):
    best = np.inf
    def rec(s, a, acc):
        nonlocal best
        if s == len(strips):
            best = min(best, acc + a)
            return
        for (x, y) in strips[s]:
            if x > a:
                rec(s + 1, x, acc + y)
    rec(0, 0.0, 0.0)
    return best


def dp(strips, X):
    t = np.linspace(0, X, 2001)
    bx, bv = np.concatenate(([-np.inf], t)), np.concatenate(([0.0], t))
    # boundary G_{n+1}(x)=x is irrelevant here: K uses x_n directly; emulate by boundary = identity
    for pts in reversed(strips):
        if len(pts) == 0:
            return np.inf
        x = np.array(sorted(p[0] for p in pts)); y = np.array([p[1] for p in sorted(pts)])
        idx = np.searchsorted(bx, x, side='right') - 1
        w = y + bv[idx]
        suff = np.minimum.accumulate(w[::-1])[::-1]
        bx = np.concatenate(([-np.inf], x)); bv = np.concatenate((suff, [np.inf]))
    i = np.searchsorted(bx, 0.0, side='right') - 1
    return bv[i]


err = 0.0
R = 300
for _ in range(R):
    n = rng.integers(2, 5); X = 4.0; Y = 3.0
    strips = []
    for s in range(n):
        m = rng.poisson(X * Y * 0.5)
        strips.append([(rng.uniform(0, X), rng.uniform(0, Y)) for _ in range(m)])
    b = brute(strips); d = dp(strips, X)
    if np.isfinite(b) or np.isfinite(d):
        # dp boundary staircase underestimates x_n by <= X/2000
        if not (abs(b - d) <= X / 2000 + 1e-9):
            print("MISMATCH", b, d); sys.exit(1)
        err = max(err, abs(b - d))
print(f"OK: {R} instances, max |DP - brute| = {err:.2e} (allowed staircase error {4.0/2000:.2e})")
