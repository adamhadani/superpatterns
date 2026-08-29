#!/usr/bin/env python3
"""W32: the anticipating (known-order) Bellman value.  For a gap whose n values arrive in a KNOWN order sigma,
the optimal fresh-window cost is V(T) = W(V(T_L), V(T_R)), T = binary search tree of sigma (insert values in
position order), W as in W31 dp.py.  For uniform sigma, T is a random BST: E V_n^ant = E_T V(T) <= V_n.
Exact computation over all BST shapes (Catalan(n) atoms) for n <= NMAX; then a quantised version (K atoms,
merged by V-value) for larger n.  Usage: python3 bst.py NMAX_exact NMAX_quant K
"""
import sys, math, itertools
sys.path.insert(0, "../w31-lookahead")
from dp import W
from collections import defaultdict

nexact = int(sys.argv[1]); nq = int(sys.argv[2]); K = int(sys.argv[3])
V = [0.0]
with open("../w31-lookahead/dp_V.txt") as fh:
    for line in fh:
        if line.startswith("#"): continue
        V.append(float(line.split()[1]))
# dist[n] = dict value -> probability (over random BST of size n)
dist = [{0.0: 1.0}]
cacheW = {}
def Wc(A, B):
    key = (round(A, 9), round(B, 9))
    if key not in cacheW: cacheW[key] = W(A, B)
    return cacheW[key]
print("# n  E V^ant_n   V_n   ratio   E V^ant/n^2   V_n/n^2   atoms", flush=True)
for n in range(1, nq + 1):
    d = defaultdict(float)
    for m in range(n):
        dl, dr = dist[m], dist[n - 1 - m]
        for vl, pl in dl.items():
            for vr, pr in dr.items():
                d[Wc(vl, vr)] += pl * pr / n
    if n > nexact and len(d) > K:
        # quantise: sort by value, merge into K groups of equal probability mass, keep the group mean
        items = sorted(d.items())
        tot = 1.0; grp = defaultdict(float); acc = 0.0; gi = 0; mass = 0.0; sm = 0.0
        merged = {}
        target = 1.0 / K
        for v, p in items:
            mass += p; sm += v * p
            if mass >= target - 1e-12:
                merged[sm / mass] = merged.get(sm / mass, 0.0) + mass; mass = 0.0; sm = 0.0
        if mass > 0: merged[sm / mass] = merged.get(sm / mass, 0.0) + mass
        d = merged
    dist.append(dict(d))
    ev = sum(v * p for v, p in d.items())
    print("%3d %14.6f %14.6f %.6f %.6f %.6f %d" % (n, ev, V[n], ev / V[n], ev / n**2, V[n] / n**2, len(d)), flush=True)
