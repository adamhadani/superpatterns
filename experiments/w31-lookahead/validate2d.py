#!/usr/bin/env python3
"""W31 end-to-end validation: run the margin/lookahead rule (proof.md Theorem 2.1) on a real Poisson process
of intensity N = C k^2 on [0,1]^2 and a real uniformly random pi in S_k, k = m*h; check that the chosen points
form a copy of pi and report success (all chosen x < 1), the cost fraction a/k, and the collision statistics.
Usage: python3 validate2d.py h m C trials eps [seed]
Potentials Vbar_n are read from dp_cert_eps{eps}.txt (certified upper bounds, dp_cert.py).
"""
import sys, bisect, math
import numpy as np

def load_V(eps, need):
    V = [0.0]
    with open("dp_cert_eps%g.txt" % eps) as fh:
        for line in fh:
            if line.startswith("#"): continue
            n, v, _ = line.split()
            V.append(float(v))
    assert len(V) > need, "dp_cert file too short"
    return V

def phi_window_min(A, B, mb, ma, yL, yR, lo, hi):
    def phi(y):
        f = 0.0
        if mb > 0: f += A / (y - yL)
        if ma > 0: f += B / (yR - y)
        return f
    if mb == 0 and ma == 0: return 0.0
    if mb > 0 and ma > 0:
        ys = yL + (yR - yL) * math.sqrt(A) / (math.sqrt(A) + math.sqrt(B))
        ys = min(max(ys, lo), hi)
        return phi(ys)
    return phi(hi) if mb > 0 else phi(lo)

def run_one(h, m, C, eps, V, rng):
    k = m * h
    N = rng.poisson(C * k * k)
    P = rng.random((N, 2))
    xs = P[:, 0] * k                   # scaled x'
    ys = P[:, 1] * k                   # scaled y' (global); strip j holds y' in [jh, (j+1)h)
    strip = np.minimum((ys // h).astype(int), m - 1)
    order = np.lexsort((xs, strip))
    xs, ys, strip = xs[order], ys[order], strip[order]
    starts = np.searchsorted(strip, np.arange(m + 1))
    SX = [xs[starts[j]:starts[j + 1]] for j in range(m)]
    SY = [ys[starts[j]:starts[j + 1]] - j * h for j in range(m)]
    pi = rng.permutation(k)
    placed = [dict() for _ in range(m)]      # value -> y'
    sorted_vals = [[] for _ in range(m)]     # placed values sorted
    edge = [0.0] * m                         # right edge of explored sets (x' units)
    a = 0.0
    collisions = 0; extra = 0.0
    chosen = []
    for p in range(k):
        v = int(pi[p]); j = v // h
        sv = sorted_vals[j]
        i = bisect.bisect_left(sv, v)
        if i > 0:
            L = sv[i - 1]; yL = placed[j][L]; mb = v - L - 1
        else:
            L = None; yL = 0.0; mb = v - j * h
        if i < len(sv):
            R = sv[i]; yR = placed[j][R]; ma = R - v - 1
        else:
            R = None; yR = float(h); ma = (j + 1) * h - 1 - v
        G = yR - yL
        lo = yL + (eps * G if mb > 0 else 0.0)
        hi = yR - (eps * G if ma > 0 else 0.0)
        A = V[mb]; B = V[ma]
        a_safe = max(a, edge[j])
        if a_safe > a:
            collisions += 1; extra += a_safe - a
        X = SX[j]; Y = SY[j]
        idx = bisect.bisect_right(X, a_safe)
        best = math.inf; bq = -1
        while idx < len(X) and X[idx] - a_safe < best:
            y = Y[idx]
            if lo < y < hi:
                phi = 0.0
                if mb > 0: phi += A / (y - yL)
                if ma > 0: phi += B / (yR - y)
                s = X[idx] - a_safe + phi / C
                if s < best:
                    best = s; bq = idx
            idx += 1
        if bq < 0:
            return dict(ok=False, frac=math.inf, collisions=collisions, extra=extra, p=p)
        # explored set = {x - a_safe + phi(y)/C <= best}: right edge = a_safe + best - phi_min/C
        phi_min = phi_window_min(A, B, mb, ma, yL, yR, lo, hi)
        edge[j] = a_safe + best - phi_min / C
        a = X[bq]
        placed[j][v] = Y[bq]; bisect.insort(sv, v)
        chosen.append((a, Y[bq] + j * h, v))
    # check copy: x increasing (by construction), y order == value order
    ys_ = [c[1] for c in chosen]; vs_ = [c[2] for c in chosen]
    okcopy = all((ys_[s] < ys_[t]) == (vs_[s] < vs_[t]) for s in range(0, k, 7) for t in range(k))
    return dict(ok=(a < k) and okcopy, frac=a / k, collisions=collisions, extra=extra, copy=okcopy)

if __name__ == "__main__":
    h, m, C, T, eps = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
    seed = int(sys.argv[6]) if len(sys.argv) > 6 else 1
    V = load_V(eps, h)
    rng = np.random.default_rng(seed)
    succ = 0; fr = []; col = []; ex = []
    for t in range(T):
        r = run_one(h, m, C, eps, V, rng)
        succ += r["ok"]; fr.append(r["frac"]); col.append(r["collisions"]); ex.append(r["extra"])
    fin = [f for f in fr if f < math.inf]
    print("h=%d m=%d k=%d C=%.3f eps=%g Omega_h(eps)=%.4f: success %d/%d, mean cost/k %.4f (finished runs %d), "
          "collisions mean %.1f (extra x' mean %.2f of k=%d)" % (h, m, m * h, C, eps, V[h] / h**2, succ, T,
          (sum(fin) / len(fin)) if fin else float('nan'), len(fin), sum(col) / T, sum(ex) / T, m * h), flush=True)
