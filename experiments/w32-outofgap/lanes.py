#!/usr/bin/env python3
"""W32: r LANES, each two-sided.  Positions are cut into r contiguous blocks; block i owns the x'-interval
[i k/r, (i+1) k/r] (budget k/r).  Each block has a left clock a_i and a right clock b_i and two candidates
(its leftmost and rightmost unplaced positions).  At each step the rule evaluates the fresh in-gap minimiser
(score = x-consumption + Phi/C, W31 potentials) for all 2r candidates and takes the cheapest.  Success iff every
block finishes with a_i < b_i.  Value strips of height h = k/m.  Usage: python3 lanes.py k m r C T seed [eps]
"""
import sys, bisect, math
import numpy as np
from single_strip import load_V
from twosided import gap_of, search

def run_one(k, m, r, C, V, rng, eps=0.0):
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
    bnd = [round(i * k / r) for i in range(r + 1)]          # position blocks
    xb = [i * k / r for i in range(r + 1)]                   # x' budgets
    a = [xb[i] for i in range(r)]; b = [xb[i + 1] for i in range(r)]
    pl = [bnd[i] for i in range(r)]; pr = [bnd[i + 1] - 1 for i in range(r)]
    cons = 0.0; ok = True
    remaining = k
    cache = {}   # (i, side) -> (best, side, p, v, j, bq, i, yL, yR)
    def recompute(i):
        for side, p in ((+1, pl[i]), (-1, pr[i])):
            key = (i, side)
            if pl[i] > pr[i] or (side < 0 and pl[i] == pr[i]):
                cache.pop(key, None); continue
            v = int(pi[p]); j = v // h
            yL, yR, mb, ma = gap_of(v, j, h, sorted_vals, placed)
            best, bq = search(SX[j], SY[j], used[j], a[i], b[i], side, yL, yR, mb, ma, V[mb], V[ma], C, eps)
            cache[key] = (best, side, p, v, j, bq, i, yL, yR)
    for i in range(r): recompute(i)
    while remaining > 0:
        best_all = None
        for val in cache.values():
            if val[5] >= 0 and (best_all is None or val[0] < best_all[0]): best_all = val
        if best_all is None:
            return dict(ok=False, cons=math.inf)
        best, side, p, v, j, bq, i, yL, yR = best_all
        used[j][bq] = True
        placed[j][v] = SY[j][bq]; bisect.insort(sorted_vals[j], v)
        if side > 0:
            cons += SX[j][bq] - a[i]; a[i] = SX[j][bq]; pl[i] += 1
        else:
            cons += b[i] - SX[j][bq]; b[i] = SX[j][bq]; pr[i] -= 1
        remaining -= 1
        placed_y = SY[j][bq]
        recompute(i)
        for key, val in list(cache.items()):
            if key[0] != i and val[4] == j and val[7] < placed_y < val[8]:
                recompute(key[0])
    return dict(ok=True, cons=cons / k)

if __name__ == "__main__":
    k, m, r, C, T, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    eps = float(sys.argv[7]) if len(sys.argv) > 7 else 0.0
    V = load_V(k // m)
    rng = np.random.default_rng(seed)
    cons = []; ok = 0
    for t in range(T):
        res = run_one(k, m, r, C, V, rng, eps)
        ok += res["ok"]
        if res["cons"] < math.inf: cons.append(res["cons"])
    fin = np.array(cons)
    print("LANES r=%d k=%d m=%d h=%d C=%.3f eps=%g runs=%d: success %d/%d, mean consumption/k %.4f (sd %.4f) over %d finished, implied constant %.4f"
          % (r, k, m, k // m, C, eps, T, ok, T, fin.mean() if len(fin) else float('nan'), fin.std() if len(fin) else 0, len(fin), C * fin.mean() if len(fin) else float('nan')), flush=True)
