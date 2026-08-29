#!/usr/bin/env python3
"""W32: the W31 in-gap Bellman rule on m strips of height h = k/m (m = 1: no artificial partition),
searching from the TRUE clock (no safe clock; explored sublevel sets contain no unused points, so the
minimiser over the process in {x'>a} x W is the minimiser over (that region minus the explored sets)).

Records, per step, the clock advance since the gap of the current value was created (D) and the step cost (u),
to measure the cost share of steps that a lookahead L could have informed (D < L).

Usage: python3 single_strip.py k m C T seed  -> one line per run + summary; writes stale_k{k}_m{m}_C{C}.txt
"""
import sys, bisect, math
import numpy as np

def load_V(need):
    V = [0.0]
    with open("../w31-lookahead/dp_V.txt") as fh:
        for line in fh:
            if line.startswith("#"): continue
            n, v, _, _ = line.split()
            V.append(float(v))
    assert len(V) > need
    return V

def run_one(k, m, C, V, rng, eps=0.0):
    h = k // m
    N = rng.poisson(C * k * k)
    P = rng.random((N, 2))
    xs = P[:, 0] * k; ys = P[:, 1] * k
    strip = np.minimum((ys // h).astype(int), m - 1)
    order = np.lexsort((xs, strip))
    xs, ys, strip = xs[order], ys[order], strip[order]
    starts = np.searchsorted(strip, np.arange(m + 1))
    SX = [xs[starts[j]:starts[j + 1]] for j in range(m)]
    SY = [ys[starts[j]:starts[j + 1]] - j * h for j in range(m)]
    used = [np.zeros(len(SX[j]), dtype=bool) for j in range(m)]
    pi = rng.permutation(k)
    placed = [dict() for _ in range(m)]       # value -> (y', clock when placed)
    sorted_vals = [[] for _ in range(m)]
    a = 0.0
    D = np.empty(k); U = np.empty(k); T = np.empty(k, dtype=int)
    for p in range(k):
        v = int(pi[p]); j = v // h
        sv = sorted_vals[j]
        i = bisect.bisect_left(sv, v)
        tcreated = 0.0
        if i > 0:
            L = sv[i - 1]; yL, cL = placed[j][L]; mb = v - L - 1; tcreated = max(tcreated, cL)
        else:
            yL = 0.0; mb = v - j * h
        if i < len(sv):
            R = sv[i]; yR, cR = placed[j][R]; ma = R - v - 1; tcreated = max(tcreated, cR)
        else:
            yR = float(h); ma = (j + 1) * h - 1 - v
        G = yR - yL
        lo = yL + (eps * G if mb > 0 else 0.0)
        hi = yR - (eps * G if ma > 0 else 0.0)
        A = V[mb]; B = V[ma]
        X = SX[j]; Y = SY[j]; us = used[j]
        idx = bisect.bisect_right(X, a)
        best = math.inf; bq = -1
        while idx < len(X) and X[idx] - a < best:
            if not us[idx]:
                y = Y[idx]
                if lo < y < hi:
                    phi = 0.0
                    if mb > 0: phi += A / (y - yL)
                    if ma > 0: phi += B / (yR - y)
                    s = X[idx] - a + phi / C
                    if s < best:
                        best = s; bq = idx
            idx += 1
        if bq < 0:
            return None
        us[bq] = True
        D[p] = a - tcreated; U[p] = X[bq] - a; T[p] = len(sv)
        a = X[bq]
        placed[j][v] = (Y[bq], a); bisect.insort(sv, v)
    return dict(cost=a / k, D=D, U=U, T=T)

if __name__ == "__main__":
    k, m, C, T, seed = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    V = load_V(k // m)
    rng = np.random.default_rng(seed)
    costs = []; allD = []; allU = []
    for t in range(T):
        r = run_one(k, m, C, V, rng)
        if r is None:
            print("run %d: FAILED (no point)" % t); continue
        costs.append(r["cost"]); allD.append(r["D"]); allU.append(r["U"])
        print("run %d: cost/k = %.4f  => implied constant C*cost/k = %.4f" % (t, r["cost"], C * r["cost"]), flush=True)
    D = np.concatenate(allD); U = np.concatenate(allU)
    tot = U.sum()
    print("k=%d m=%d h=%d C=%.3f runs=%d: mean cost/k %.4f (sd %.4f), implied constant %.4f, mean-field V_h/h^2 = %.4f"
          % (k, m, k // m, C, len(costs), np.mean(costs), np.std(costs), C * np.mean(costs), V[k // m] / (k // m) ** 2))
    with open("stale_k%d_m%d_C%g.txt" % (k, m, C), "w") as fh:
        fh.write("# L/k  share of step-cost with (clock advance since gap creation) < L\n")
        for f in [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]:
            Lk = f * k
            share = U[D < Lk].sum() / tot
            fh.write("%.3f %.5f\n" % (f, share))
            print("  L = %.3f k: cost share of informable steps = %.4f  (C*L/k = %.4f)" % (f, share, C * f))
