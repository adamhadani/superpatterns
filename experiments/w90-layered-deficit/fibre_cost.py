#!/usr/bin/env python3
"""W90: evaluate the exact fibre formula stage by stage and compare it with the directly measured deficit.

Pattern: W = 2 1 4 3 6 5 ...; hybrid N_I = longest contained prefix of 21^{(+)I} (+) 1 (+) 1 (+) ...  (N_0 = LIS).
Stage i (i >= 1) flips block i+1 with alpha = 21^{(+)i}, beta = I_b.  Theorem 1 gives
    E[N_i - N_{i+1}] = sum_b E[(a_b - 1)/F_b] = E[ sum_{b : realised level-b filling has no D-inversion} (1 - 1/a_b) ],
where the level-b inside set is {q : SW(q) contains 21^{(+)i}, LIS strictly NE of q >= b} and a_b is the number of
valid fillings of its board without a D-inversion.  This script computes the right-hand side by brute force over
fillings and N_I directly, on the same permutations.

usage: fibre_cost.py exact n            (all of S_n, exact rational check of  sum_i c_i == LIS - N_full)
       fibre_cost.py mc n samples seed Imax [Nmax=9]
"""
import sys, itertools, random
from bisect import bisect_left
from fractions import Fraction
from collections import Counter

def analyse(y, Imax=None, Nmax=9, exact=False, stats=None):
    n = len(y)
    # ---- forward sweep: thresholds F (F[0] = -1), level of each point at arrival, snapshots
    F = [-1]; P = [[]]; lev = [0] * n; snaps = [None] * n
    for t, v in enumerate(y):
        snaps[t] = F[:]
        j = bisect_left(F, v) - 1
        lev[t] = j
        pv = P[j]; best = None
        for lo, hi in pv:
            if lo < v < hi and (best is None or hi < best): best = hi
        if best is not None:
            if j == len(F) - 1: F.append(best); P.append([])
            elif best < F[j + 1]: F[j + 1] = best
            pv = [a for a in pv if a[1] < F[j + 1]]; P[j] = pv
        pv.append((F[j], v))
    L = len(F) - 1
    # ---- backward: g[t] = longest increasing subsequence starting at t; h = g - 1
    tails = []; g = [0] * n
    for t in range(n - 1, -1, -1):
        c = bisect_left(tails, -y[t]); g[t] = c + 1
        if c == len(tails): tails.append(-y[t])
        elif -y[t] < tails[c]: tails[c] = -y[t]
    lis = len(tails)
    bucket = {}
    for t in range(n): bucket.setdefault(g[t] - 1, []).append(t)
    maxg = [0] * (L + 2)
    for t in range(n):
        if g[t] > maxg[lev[t]]: maxg[lev[t]] = g[t]
    for l in range(L - 1, -1, -1):
        if maxg[l + 1] > maxg[l]: maxg[l] = maxg[l + 1]
    def N(I):                      # hybrid length: first I blocks 21, then increasing
        if I <= L and maxg[I] > 0: return 2 * I + maxg[I]
        return 2 * L + (1 if maxg[L] > 0 else 0)
    top = L if Imax is None else min(Imax, L)
    total = Fraction(0) if exact else 0.0
    per_stage = []
    for i in range(1, top + 1):
        X = maxg[i]; ci = Fraction(0) if exact else 0.0
        b = X - 1
        while b >= 1:
            ins = [t for v in range(b, X) for t in bucket.get(v, ()) if lev[t] >= i]
            Nn = len(ins)
            if Nn > Nmax:
                if stats is not None: stats['overflow'] += 1
                break
            ins.sort(); xs = ins; ys = sorted(y[t] for t in ins); rk = {v: r for r, v in enumerate(ys)}
            f0 = [rk[y[t]] for t in xs]
            low = bucket.get(b - 1, ())
            okU = [[bisect_left(snaps[x], yy) - 1 >= i for yy in ys] for x in xs]
            okS = [[any(s > x and y[s] > yy for s in low) for yy in ys] for x in xs]
            def dinv(f):
                for c1 in range(Nn):
                    for c2 in range(c1 + 1, Nn):
                        if f[c1] > f[c2] and okU[c1][f[c2]] and okS[c2][f[c1]]: return True
                return False
            if dinv(f0): break
            # count valid fillings without D-inversion (backtracking)
            cnt = 0; f = [0] * Nn; used = [False] * Nn
            def rec(c):
                nonlocal cnt
                if c == Nn: cnt += 1; return
                for r in range(Nn):
                    if used[r] or not (okU[c][r] and okS[c][r]): continue
                    bad = False
                    for c1 in range(c):
                        if f[c1] > r and okU[c1][r] and okS[c][f[c1]]: bad = True; break
                    if bad: continue
                    used[r] = True; f[c] = r; rec(c + 1); used[r] = False
            rec(0)
            assert cnt >= 1
            if cnt >= 2:
                ci += (Fraction(cnt - 1, cnt) if exact else 1.0 - 1.0 / cnt)
                if stats is not None: stats[('a', Nn, cnt, X - 1 - b)] += 1
            b -= 1
        per_stage.append(ci); total += ci
    return lis, N, L, total, per_stage

def main():
    mode = sys.argv[1]
    if mode == 'exact':
        n = int(sys.argv[2]); lhs = Fraction(0); rhs = 0; st = Counter()
        for sig in itertools.permutations(range(n)):
            lis, N, L, tot, _ = analyse(list(sig), None, 12, True, st)
            lhs += tot; rhs += lis - N(L + 1)
        print(f"n={n}: sum over S_n of fibre formula = {lhs}; sum of (LIS - N_full) = {rhs}; equal: {lhs == rhs}; "
              f"defect levels (inside pts, a, levels below top): { {k[1:]: v for k, v in st.items() if k != 'overflow'} }")
    else:
        n, S, seed, Imax = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
        Nmax = int(sys.argv[6]) if len(sys.argv) > 6 else 9
        rng = random.Random(seed); st = Counter()
        sA = sA2 = sB = sB2 = sD = sD2 = 0.0; stage_sum = [0.0] * Imax; used = 0
        for _ in range(S):
            y = list(range(n)); rng.shuffle(y)
            lis, N, L, tot, ps = analyse(y, Imax - 1, Nmax, False, st)
            if L < Imax: continue
            used += 1
            A = tot; B = lis - N(Imax)
            sA += A; sA2 += A * A; sB += B; sB2 += B * B; sD += A - B; sD2 += (A - B) ** 2
            for k, c in enumerate(ps): stage_sum[k + 1] += c
        m = lambda s: s / used; se = lambda s, s2: ((s2 / used - (s / used) ** 2) / used) ** 0.5
        print(f"n={n} S={used} Imax={Imax} fibre_formula={m(sA):.5f} +- {se(sA, sA2):.5f}  direct E[LIS-N_I]={m(sB):.5f} +- {se(sB, sB2):.5f}  "
              f"paired_diff={m(sD):.5f} +- {se(sD, sD2):.5f}  overflow={st['overflow']}")
        print("defect levels (inside pts, a, levels below top) -> count:", sorted(((k[1:], v) for k, v in st.items() if k != 'overflow'), key=lambda kv: -kv[1])[:12])
        q = max(1, (Imax - 1) // 4)
        print("mean contribution per stage, by quarter of the stage range:", [round(sum(stage_sum[1 + a * q:1 + (a + 1) * q]) / used / q, 5) for a in range(4)])

if __name__ == '__main__':
    main()
