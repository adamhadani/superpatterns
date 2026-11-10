#!/usr/bin/env python3
"""Brute-force verification of the W90 block-flip theorem and the exact fibre identity.

For patterns alpha, beta (possibly empty) and all sigma in S_n:
  U = {z : the points of sigma strictly SW of z contain alpha},  S = {z : the points strictly NE of z contain beta},
  inside points = points of sigma lying in U and S; D = the cells (x,y), x an inside column, y an inside row, in U∩S.
Checks, for every n up to nmax:
  (T1) #{sigma contains alpha(+)21(+)beta} <= #{sigma contains alpha(+)12(+)beta};
  (F1) fibres: permutations sharing the same outside points form exactly the set of valid fillings of D
       (so the fibre is determined by the outside points alone);
  (F2) each fibre contains exactly one filling with no increasing pair (the decreasing one) and a >= 1 fillings with
       no D-inversion (a NW of b with SW corner (x_a,y_b) in U and NE corner (x_b,y_a) in S);
  (F3) #contains(12) - #contains(21) = sum over fibres of (a - 1);
  and reports the fibres with a >= 2 (the "defect lenses").
usage: verify_fibers.py [nmax=8]
"""
import sys, itertools
from collections import defaultdict

def contains(points, pat):
    """points: list of (x,y) with distinct coords; pat: tuple (1-based values). True iff some subset is order-isomorphic."""
    k = len(pat)
    if k == 0: return True
    pts = sorted(points)
    if len(pts) < k: return False
    for sub in itertools.combinations(pts, k):
        ys = [p[1] for p in sub]
        if all((ys[i] < ys[j]) == (pat[i] < pat[j]) for i in range(k) for j in range(i + 1, k)):
            return True
    return False

def dsum(*pats):
    out = []
    for p in pats:
        off = len(out); out += [v + off for v in p]
    return tuple(out)

def run(alpha, beta, nmax):
    ok = True
    for n in range(1, nmax + 1):
        c12 = c21 = 0
        fibres = defaultdict(list)
        P12, P21 = dsum(alpha, (1, 2), beta), dsum(alpha, (2, 1), beta)
        for sig in itertools.permutations(range(1, n + 1)):
            pts = [(i + 1, sig[i]) for i in range(n)]
            inU = lambda x, y, pool: contains([p for p in pool if p[0] < x and p[1] < y], alpha)
            inS = lambda x, y, pool: contains([p for p in pool if p[0] > x and p[1] > y], beta)
            inside = [p for p in pts if inU(p[0], p[1], pts) and inS(p[0], p[1], pts)]
            outside = tuple(p for p in pts if p not in inside)
            h12 = contains(pts, P12); h21 = contains(pts, P21)
            c12 += h12; c21 += h21
            # predictions from the fibre picture
            X = sorted(p[0] for p in inside); ins = sorted(inside)
            has_inc = any(a[1] < b[1] for a, b in itertools.combinations(ins, 2))
            cellU = lambda x, y: inU(x, y, outside); cellS = lambda x, y: inS(x, y, outside)
            has_dinv = any(a[1] > b[1] and cellU(a[0], b[1]) and cellS(b[0], a[1]) for a, b in itertools.combinations(ins, 2))
            assert has_inc == h12, (sig, "12")
            assert has_dinv == h21, (sig, "21")
            fibres[outside].append((tuple(ins), has_inc, has_dinv))
        tot = 0; lenses = defaultdict(int)
        for outside, members in fibres.items():
            ins0 = members[0][0]
            X = sorted(p[0] for p in ins0); Y = sorted(p[1] for p in ins0)
            inU = lambda x, y: contains([p for p in outside if p[0] < x and p[1] < y], alpha)
            inS = lambda x, y: contains([p for p in outside if p[0] > x and p[1] > y], beta)
            valid = [f for f in itertools.permutations(Y) if all(inU(x, y) and inS(x, y) for x, y in zip(X, f))]
            assert sorted(tuple(zip(X, f)) for f in valid) == sorted(m[0] for m in members), "F1 fails"
            assert sum(1 for m in members if not m[1]) == 1, "F2 fails (decreasing filling)"
            a = sum(1 for m in members if not m[2])
            assert a >= 1, "F2 fails (no inversion-free filling)"
            tot += a - 1
            if a >= 2: lenses[(len(X), len(valid), a)] += 1
        assert tot == c12 - c21, "F3 fails"
        assert c21 <= c12, "T1 fails"
        print(f"  n={n}: contains 12-version {c12}, 21-version {c21}, difference {c12 - c21} = sum over {len(fibres)} fibres of (a-1); "
              f"defect fibres (inside pts, #fillings, a): {dict(lenses)}")
    return ok

nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
CASES = [((1,), (1,)), ((2, 1), (2, 1)), ((1, 2), (1, 2)), ((1,), (2, 1)), ((1, 3, 2), (1,)), ((2, 3, 1), (2, 1)), ((), (1,))]
if len(sys.argv) > 2:  # e.g. verify_fibers.py 9 21:21   -> only that case, up to n=9
    a, b = sys.argv[2].split(':'); CASES = [(tuple(int(c) for c in a), tuple(int(c) for c in b))]
for alpha, beta in CASES:
    m = nmax if (len(sys.argv) > 2 or len(alpha) + len(beta) <= 2) else min(nmax, 8)
    print(f"alpha={alpha} beta={beta}")
    run(alpha, beta, m)
print("ALL CHECKS PASSED")
