#!/usr/bin/env python3
"""W31: certified (rigorous upper bound) Bellman values for the margin rule.

Rule class R(eps): in a gap of height G with m_b unplaced values below and m_a above the value to be placed,
the window is y in [y_L + eps_b G, y_R - eps_a G] with eps_b = eps*[m_b>0], eps_a = eps*[m_a>0] (relative
margins, so the problem stays self-similar), and the point chosen is the minimiser of
      x + Vbar_{m_b} / (y - y_L) + Vbar_{m_a} / (y_R - y)          (intensity 1)
over the fresh Poisson points in (a, inf) x window.  Vbar_n is an UPPER bound on the rule's cost for n values in a
unit gap, computed by the recursion Vbar_n = (1/n) sum_m Wbar_eps(Vbar_m, Vbar_{n-1-m}) where Wbar_eps >= W_eps :=
E min over the window of [x + A/y + B/(1-y)] = smin + int_{smin}^inf exp(-area_eps(s)) ds, bounded from ABOVE by
left-endpoint rectangles (exp(-area) is nonincreasing in s) plus an exponential tail bound.  Monotonicity of
W_eps in (A,B) makes the upper bounds propagate (proof.md Lemma 3.2).

Usage: python3 dp_cert.py NMAX EPS [PANELS]   -> dp_cert_eps{EPS}.txt with n, Vbar_n, Vbar_n/n^2
"""
import sys, math
import numpy as np

def roots(s, A, B):
    disc = (s + A - B) ** 2 - 4 * s * A
    ok = disc > 0
    sq = np.sqrt(np.where(ok, disc, 0.0))
    y1 = ((s + A - B) - sq) / (2 * s)
    y2 = ((s + A - B) + sq) / (2 * s)
    return ok, y1, y2

def area_eps(s, A, B, lo, hi):
    """int_{lo}^{hi} (s - A/y - B/(1-y))_+ dy, closed form (s array of positive numbers)."""
    s = np.asarray(s, dtype=float)
    if A == 0 and B == 0:
        return s * (hi - lo)
    ok, y1, y2 = roots(s, A, B)
    y1 = np.maximum(y1, lo)
    y2 = np.minimum(y2, hi)
    ok = ok & (y2 > y1)
    y1 = np.clip(y1, 1e-300, 1 - 1e-16)
    y2 = np.clip(y2, 1e-300, 1 - 1e-16)
    val = s * (y2 - y1)
    if A > 0:
        val = val - A * np.log(y2 / y1)
    if B > 0:
        val = val + B * np.log((1 - y2) / (1 - y1))
    out = np.zeros_like(s)
    out[ok] = val[ok]
    return np.maximum(out, 0.0)

def smin_eps(A, B, lo, hi):
    # f(y) = A/y + B/(1-y) is convex; unconstrained minimiser sqrt(A)/(sqrt A + sqrt B)
    if A == 0 and B == 0:
        return 0.0
    ys = math.sqrt(A) / (math.sqrt(A) + math.sqrt(B))
    ys = min(max(ys, lo), hi)
    f = 0.0
    if A > 0: f += A / ys
    if B > 0: f += B / (1 - ys)
    return f

def Wbar(A, B, eps, panels=4000, slack=1e-9):
    """Rigorous upper bound on W_eps(A,B)."""
    lo = eps if A > 0 else 0.0
    hi = 1 - eps if B > 0 else 1.0
    smin = smin_eps(A, B, lo, hi)
    # window height wh: the integrand exp(-area(s)) <= exp(-(s - smin) * ... )?  area(s) >= (s - smin)*0 only;
    # use rectangles up to s_T then the tail bound area(s) >= area(s_T) + (s - s_T) * width(s_T).
    # Choose s_T large enough that the tail is tiny: area grows at least like wh*(s - f_max) once the sublevel set
    # is the whole window; simplest: iterate doubling s_T until exp(-area(s_T)) < 1e-14 * width.
    wh = hi - lo
    sT = smin + 4.0 + 4.0 * smin
    for _ in range(60):
        a = float(area_eps(np.array([sT]), A, B, lo, hi)[0])
        ok, y1, y2 = roots(np.array([sT]), A, B) if (A > 0 or B > 0) else (np.array([True]), np.array([lo]), np.array([hi]))
        width = float(min(y2[0], hi) - max(y1[0], lo)) if ok[0] else 0.0
        if width > 0 and math.exp(-a) / width < 1e-15:
            break
        sT *= 1.5
    tail = math.exp(-a) / width  # int_{sT}^inf exp(-area(sT) - (s-sT) width) ds
    grid = np.linspace(smin, sT, panels + 1)
    f = np.exp(-area_eps(grid[:-1], A, B, lo, hi))  # left endpoints (upper bound, integrand nonincreasing)
    rect = float(np.sum(f) * (sT - smin) / panels)
    return (smin + rect + tail) * (1 + slack)

def run(nmax, eps, panels):
    V = [0.0]
    fn = "dp_cert_eps%g.txt" % eps
    with open(fn, "w") as fh:
        fh.write("# certified upper bounds; eps=%g panels=%d\n# n Vbar_n Vbar_n/n^2\n" % (eps, panels))
        for n in range(1, nmax + 1):
            acc = 0.0
            for m in range(n):
                acc += Wbar(V[m], V[n - 1 - m], eps, panels)
            V.append(acc / n)
            fh.write("%d %.9f %.9f\n" % (n, V[n], V[n] / n**2))
            fh.flush()
            if n <= 8 or n % 8 == 0:
                print("n=%4d  Vbar=%12.6f  Vbar/n^2=%.6f" % (n, V[n], V[n] / n**2), flush=True)
    return V

if __name__ == "__main__":
    nmax = int(sys.argv[1]); eps = float(sys.argv[2])
    panels = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
    print("check Wbar(0,0)=%.9f (>=1)  Wbar(1,0)=%.9f (>=3 at eps=0)" % (Wbar(0, 0, eps, panels), Wbar(1, 0, 0.0, panels)))
    run(nmax, eps, panels)
