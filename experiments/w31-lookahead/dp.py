#!/usr/bin/env python3
"""W31: Bellman recursion for the optimal fresh-window (mean-field) gap rule on one strip.

V_n = optimal expected x-cost of placing n values (uniform random order) in a gap of unit height,
Poisson intensity 1 in (x,y) in (0,inf) x (0,1), fresh window at every step; each step chooses one point (x,y),
pays x, and the n-1 remaining values split into m below / n-1-m above (m uniform on {0..n-1}), whose
cost-to-go is V_m / y + V_{n-1-m} / (1-y) (scaling).  So
   V_n = (1/n) sum_{m=0}^{n-1} W(V_m, V_{n-1-m}),
   W(A,B) = E min_{(x,y) in Psi} [x + A/y + B/(1-y)] = smin + int_{smin}^inf exp(-area(s)) ds,
   smin = (sqrt A + sqrt B)^2,  area(s) = int_0^1 (s - A/y - B/(1-y))_+ dy  (closed form).
The threshold constant of the strip rule is Omega_h = V_h / h^2 (see proof.md).
Usage: python3 dp.py [nmax]   -> prints n, V_n, V_n/n^2, barrier (n+1)/(2n), and writes dp_V.txt
"""
import sys, math
import numpy as np

def area(s, A, B):
    """int_0^1 (s - A/y - B/(1-y))_+ dy, closed form; s array."""
    s = np.asarray(s, dtype=float)
    out = np.zeros_like(s)
    if A == 0 and B == 0:
        return s.copy()
    # roots of s y^2 - (s + A - B) y + A = 0  (from A(1-y) + B y = s y (1-y))
    disc = (s + A - B) ** 2 - 4 * s * A
    ok = disc > 0
    sq = np.sqrt(np.where(ok, disc, 0.0))
    y1 = ((s + A - B) - sq) / (2 * s)
    y2 = ((s + A - B) + sq) / (2 * s)
    y1 = np.clip(y1, 1e-300, 1 - 1e-16)
    y2 = np.clip(y2, 1e-300, 1 - 1e-16)
    val = s * (y2 - y1)
    if A > 0:
        val = val - A * np.log(y2 / y1)
    if B > 0:
        val = val + B * np.log((1 - y2) / (1 - y1))
    out[ok] = val[ok]
    return np.maximum(out, 0.0)

# Gauss-Legendre nodes on [0,1]
_GL = np.polynomial.legendre.leggauss(64)
_GX = (_GL[0] + 1) / 2
_GW = _GL[1] / 2

def W(A, B):
    """E min (x + A/y + B/(1-y)) over a Poisson(1) process on (0,inf)x(0,1)."""
    smin = (math.sqrt(A) + math.sqrt(B)) ** 2
    # integrate exp(-area(s)) over s in (smin, inf); area grows ~ s, so tail is exponential.
    # panels of geometric growth, each with 64-point GL.
    total = 0.0
    a = smin
    width = max(0.5, 0.25 * (1.0 + smin))
    for _ in range(200):
        b = a + width
        x = a + (b - a) * _GX
        f = np.exp(-area(x, A, B))
        piece = (b - a) * float(np.dot(_GW, f))
        total += piece
        if f[-1] < 1e-18:
            break
        a = b
        width *= 1.3
    return smin + total

def run(nmax):
    V = [0.0]
    rows = []
    for n in range(1, nmax + 1):
        acc = 0.0
        for m in range(n):
            acc += W(V[m], V[n - 1 - m])
        V.append(acc / n)
        rows.append((n, V[n], V[n] / n**2, (n + 1) / (2 * n)))
        if n <= 20 or n % 10 == 0:
            print("n=%4d  V=%12.6f  V/n^2=%.6f  blind-barrier=%.6f" % rows[-1], flush=True)
    with open("dp_V.txt", "w") as fh:
        fh.write("# n V_n V_n/n^2 (n+1)/(2n)\n")
        for r in rows:
            fh.write("%d %.9f %.9f %.9f\n" % r)
    return V

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 64
    # sanity: W(0,0)=1, W(1,0)=3
    print("check W(0,0)=%.9f (1)  W(1,0)=%.9f (3)" % (W(0, 0), W(1, 0)))
    run(nmax)
