#!/usr/bin/env python3
# review-2: check the sweep algorithm of l21rev.c (ported line by line) against the definition of pattern containment
# (subset enumeration with itertools) on ALL permutations of S_n, n <= 8.
import itertools, sys, math
def contains(perm, pat):
    k = len(pat); n = len(perm)
    for idx in itertools.combinations(range(n), k):
        vals = [perm[i] for i in idx]
        order = sorted(range(k), key=lambda t: vals[t])
        rank = [0]*k
        for r, t in enumerate(order): rank[t] = r+1
        if rank == pat: return True
    return False
def l21_def(perm):
    m = 0
    while 2*(m+1) <= len(perm):
        pat = []
        for j in range(m+1): pat += [2*j+2, 2*j+1]
        if contains(perm, pat): m += 1
        else: break
    return m
def l21_sweep(y):
    n = len(y); Y = [-math.inf]; head = [-1]; th = [0.0]*n; prv = [0]*n; L = 0
    for i in range(n):
        v = y[i]; lo, hi = 0, L
        while lo < hi:
            md = (lo+hi+1)//2
            if Y[md] < v: lo = md
            else: hi = md-1
        k = lo; best = math.inf; j = head[k]
        while j >= 0 and th[j] < v:
            if y[j] > v and y[j] < best: best = y[j]
            j = prv[j]
        if best < math.inf:
            if k == L: L += 1; Y.append(best); head.append(-1)
            elif best < Y[k+1]: Y[k+1] = best
        th[i] = Y[k]; prv[i] = head[k]; head[k] = i
    return L
for n in range(1, int(sys.argv[1])+1):
    bad = 0; tot = 0; hist = {}
    for p in itertools.permutations(range(1, n+1)):
        a = l21_def(list(p)); b = l21_sweep(list(p)); tot += 1; hist[a] = hist.get(a, 0)+1
        if a != b: bad += 1
    print(f"n={n}: {tot} permutations, mismatches={bad}, distribution of L21 = {sorted(hist.items())}")
