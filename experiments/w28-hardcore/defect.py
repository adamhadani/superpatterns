#!/usr/bin/env python3
"""W28: local-defect statistics of sigma vs M. Input: out/k{K}_n{N}_sigma_s*.txt from msigma ("M | s1 s2 ...")."""
import sys, glob, math, numpy as np
sys.path.insert(0, '../w24-union-slack'); from patlib import lis, lds
k = int(sys.argv[1]); n = int(sys.argv[2])
rows = []
for f in glob.glob(f'out/k{k}_n{n}_sigma_s*.txt'):
    for line in open(f):
        if line.startswith('#') or '|' not in line: continue
        a, b = line.split('|'); sig = [int(x) for x in b.split()]
        if len(sig) == n and sorted(sig) == list(range(1, n+1)): rows.append((int(a), sig))
def max_empty_rect(s):
    n = len(s); best = 0
    for a in range(n):
        vals = [0, n+1]
        for b in range(a, n):
            # insert s[b]
            import bisect; bisect.insort(vals, s[b])
            w = b - a + 1
            # empty rectangles spanning positions a..b fully: value gaps
            g = max(vals[i+1]-vals[i]-1 for i in range(len(vals)-1))
            best = max(best, w*g)
    return best
def max_empty_rect_all(s):
    """largest empty rectangle anywhere: positions [a,b] x values [c,d] with no point; includes those touching the boundary"""
    n = len(s); best = 0
    for a in range(n+1):
        vals = [0, n+1]
        for b in range(a, n+1):
            w = b - a  # positions strictly between a and b (0..n indexing of gaps): use half-integer boundaries
            if b > a: 
                import bisect; bisect.insort(vals, s[b-1])
            g = max(vals[i+1]-vals[i]-1 for i in range(len(vals)-1))
            best = max(best, w*g)
    return best
def mincell(s, g):
    n = len(s); c = np.zeros((g, g), int)
    for i, v in enumerate(s): c[i*g//n, (v-1)*g//n] += 1
    return c.min()
stats = []
for M, s in rows:
    stats.append((M, max_empty_rect(s), mincell(s, 3), mincell(s, 4), lis(s), lds(s)))
A = np.array(stats, float)
print(f'# k={k} n={n} samples={len(A)}; Pr(M>0)={np.mean(A[:,0]>0):.3f}, E M={A[:,0].mean():.3g}')
print('| M | #σ | mean max-empty-rect area (cells) | q90 | mean min cell count 3×3 | P(min3=0) | mean min cell 4×4 | P(min4≤0) | mean LIS | mean LDS | min(LIS,LDS) mean |')
print('|' + '---|'*11)
for lo, hi, name in [(0,0,'0'),(1,3,'1–3'),(4,9,'4–9'),(10,29,'10–29'),(30,99,'30–99'),(100,10**9,'≥100')]:
    B = A[(A[:,0]>=lo)&(A[:,0]<=hi)]
    if len(B)==0: continue
    print(f'| {name} | {len(B)} | {B[:,1].mean():.1f} | {np.quantile(B[:,1],.9):.0f} | {B[:,2].mean():.2f} | {np.mean(B[:,2]==0):.3f} | {B[:,3].mean():.2f} | {np.mean(B[:,3]==0):.3f} | {B[:,4].mean():.2f} | {B[:,5].mean():.2f} | {np.minimum(B[:,4],B[:,5]).mean():.2f} |')
def spearmanr(x, y):
    rx = np.argsort(np.argsort(x, kind='stable')).astype(float); ry = np.argsort(np.argsort(y, kind='stable')).astype(float)
    # average ranks for ties
    def avg(v, r):
        out = r.copy()
        for u in np.unique(v): m = v == u; out[m] = r[m].mean()
        return out
    rx = avg(x, rx); ry = avg(y, ry)
    class R: pass
    o = R(); o.correlation = np.corrcoef(rx, ry)[0,1]; return o
pos = A[A[:,0]>0]
for j, nm in [(1,'max empty rect'),(2,'min cell 3x3'),(3,'min cell 4x4'),(4,'LIS'),(5,'LDS')]:
    r_all = spearmanr(A[:,0], A[:,j]).correlation; r_pos = spearmanr(pos[:,0], pos[:,j]).correlation
    print(f'Spearman(M, {nm}): all σ {r_all:+.3f}; given M>0 {r_pos:+.3f}')
