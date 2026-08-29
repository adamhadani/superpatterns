#!/usr/bin/env python3
"""W32: TWO-SIDED in-gap Bellman rule.  Positions are consumed from both ends: at each step the rule computes
the fresh in-gap minimiser for the leftmost unplaced position (search to the right of the left clock a) and
for the rightmost unplaced position (search to the left of the right clock b), scores = x-consumption +
Phi/C with the W31 potentials V_n, and takes the cheaper of the two.  Success iff all k values are placed with
a < b (consumption a + (k-b) < k).  Value strips of height h = k/m (m = 1: single strip).

Usage: python3 twosided.py k m C T seed [eps]
"""
import sys, bisect, math
import numpy as np
from single_strip import load_V

def gap_of(v, j, h, sorted_vals, placed):
    sv = sorted_vals[j]
    i = bisect.bisect_left(sv, v)
    if i > 0:
        L = sv[i - 1]; yL = placed[j][L]; mb = v - L - 1
    else:
        yL = 0.0; mb = v - j * h
    if i < len(sv):
        R = sv[i]; yR = placed[j][R]; ma = R - v - 1
    else:
        yR = float(h); ma = (j + 1) * h - 1 - v
    return yL, yR, mb, ma

def search(X, Y, us, a, b, side, yL, yR, mb, ma, A, B, C, eps):
    """side=+1: minimise (x-a)+Phi/C over a<x<b; side=-1: minimise (b-x)+Phi/C over a<x<b."""
    G = yR - yL
    lo = yL + (eps * G if mb > 0 else 0.0)
    hi = yR - (eps * G if ma > 0 else 0.0)
    # scan cap: x-excess above 60 units beyond the score minimum never wins
    if mb > 0 and ma > 0:
        ys = yL + G * math.sqrt(A) / (math.sqrt(A) + math.sqrt(B)); ys = min(max(ys, lo), hi)
        pmin = A / (ys - yL) + B / (yR - ys)
    elif mb > 0: pmin = A / (hi - yL)
    elif ma > 0: pmin = B / (yR - lo)
    else: pmin = 0.0
    best = pmin / C + 60.0; bq = -1
    if side > 0:
        idx = bisect.bisect_right(X, a)
        while idx < len(X) and X[idx] < b and X[idx] - a < best:
            if not us[idx]:
                y = Y[idx]
                if lo < y < hi:
                    phi = (A / (y - yL) if mb > 0 else 0.0) + (B / (yR - y) if ma > 0 else 0.0)
                    s = X[idx] - a + phi / C
                    if s < best: best = s; bq = idx
            idx += 1
    else:
        idx = bisect.bisect_left(X, b) - 1
        while idx >= 0 and X[idx] > a and b - X[idx] < best:
            if not us[idx]:
                y = Y[idx]
                if lo < y < hi:
                    phi = (A / (y - yL) if mb > 0 else 0.0) + (B / (yR - y) if ma > 0 else 0.0)
                    s = b - X[idx] + phi / C
                    if s < best: best = s; bq = idx
            idx -= 1
    return best, bq

def run_one(k, m, C, V, rng, eps=0.0, onesided=False):
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
    placed = [dict() for _ in range(m)]
    sorted_vals = [[] for _ in range(m)]
    a = 0.0; b = float(k)
    pl, pr = 0, k - 1
    nleft = 0
    while pl <= pr:
        cands = []
        for side, p in ((+1, pl), (-1, pr)):
            if onesided and side < 0: continue
            if side < 0 and pl == pr: continue
            v = int(pi[p]); j = v // h
            yL, yR, mb, ma = gap_of(v, j, h, sorted_vals, placed)
            best, bq = search(SX[j], SY[j], used[j], a, b, side, yL, yR, mb, ma, V[mb], V[ma], C, eps)
            cands.append((best, side, p, v, j, bq))
        cands.sort()
        best, side, p, v, j, bq = cands[0]
        if bq < 0:
            return dict(ok=False, cons=math.inf)
        used[j][bq] = True
        placed[j][v] = SY[j][bq]; bisect.insort(sorted_vals[j], v)
        if side > 0:
            a = SX[j][bq]; pl += 1; nleft += 1
        else:
            b = SX[j][bq]; pr -= 1
    cons = (a + (k - b)) / k
    return dict(ok=(a < b), cons=cons, nleft=nleft)

if __name__ == "__main__":
    k, m, C, T, seed = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    eps = float(sys.argv[6]) if len(sys.argv) > 6 else 0.0
    onesided = len(sys.argv) > 7 and sys.argv[7] == "one"
    V = load_V(k // m)
    rng = np.random.default_rng(seed)
    cons = []; ok = 0; nl = []
    for t in range(T):
        r = run_one(k, m, C, V, rng, eps, onesided)
        ok += r["ok"]
        if r["cons"] < math.inf: cons.append(r["cons"]); nl.append(r.get("nleft", 0))
    fin = np.array(cons)
    print("%s k=%d m=%d h=%d C=%.3f eps=%g runs=%d: success %d/%d, mean consumption/k %.4f (sd %.4f), implied constant %.4f, "
          "mean-field one-sided V_h/h^2 = %.4f, left share %.3f"
          % ("ONE-SIDED" if onesided else "TWO-SIDED", k, m, k // m, C, eps, T, ok, T, fin.mean(), fin.std(), C * fin.mean(),
             V[k // m] / (k // m) ** 2, np.mean(nl) / k), flush=True)
