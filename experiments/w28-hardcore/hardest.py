#!/usr/bin/env python3
"""W28: hardest patterns, and null (random-subset) comparison for component/cover statistics. Usage: hardest.py K n [nnull]"""
import sys, math, numpy as np, random
from hardcore import *
k = int(sys.argv[1]); n = int(sys.argv[2]); NN = int(sys.argv[3]) if len(sys.argv) > 3 else 300
K = math.factorial(k); pats, st = pattern_table(k); nb1, ch = onepoint_neighbors(k, pats); nbA = adj_neighbors(k, pats)
M, sets = load(k, n); S = len(M)
cnt = np.zeros(K); csum = np.zeros(K)
for m, s in zip(M, sets):
    if m > 0: cnt[s] += 1; csum[s] += m
p = cnt / S; condE = np.where(cnt > 0, csum/np.maximum(cnt,1), np.nan)
print(f'# k={k} n={n} samples={S} mu={p.sum():.4g}; uniform mean p = {p.mean():.3g}')
print('## 15 hardest patterns (p_pi = Pr(pi not in sigma_n)); LIS LDS runs inv; E[M | pi missing]')
for c in np.argsort(-p)[:15]:
    print(f'{pats[c]}  p={p[c]:.4f} ({p[c]/p.mean():.2f}x mean)  lis={st["lis"][c]} lds={st["lds"][c]} runs={st["runs"][c]} inv={st["inv"][c]}  E[M|miss]={condE[c]:.1f} (#ev {int(cnt[c])})')
print('## 8 easiest patterns with >= 20 events')
ok = cnt >= 20
for c in [c for c in np.argsort(p) if ok[c]][:8]:
    print(f'{pats[c]}  p={p[c]:.4f} ({p[c]/p.mean():.2f}x)  lis={st["lis"][c]} lds={st["lds"][c]} runs={st["runs"][c]}  E[M|miss]={condE[c]:.1f}')
print('## dihedral-class spread: max/min of p within the 8-element symmetry class, averaged over classes (>=20 events each)')
seen = set(); ratios = []
for c in range(K):
    if c in seen: continue
    q = pats[c]; cls = set()
    for a in [q, reverse(q), complement(q), reverse(complement(q))]:
        cls.add(encode(a)); cls.add(encode(inverse(a)))
    seen |= cls
    if all(cnt[x] >= 20 for x in cls): ratios.append(max(p[x] for x in cls)/min(p[x] for x in cls))
print(f'classes={len(ratios)} mean max/min = {np.mean(ratios):.2f}, median {np.median(ratios):.2f}, 90% {np.quantile(ratios,.9):.2f}')
print('## Null comparison: statistics of actual missing sets vs uniformly random subsets of S_k of the same size, and vs p-weighted random subsets')
rng = random.Random(5); ev = [(m, s) for m, s in zip(M, sets) if m > 0]; idx = list(range(len(ev))); rng.shuffle(idx); idx = idx[:NN]
def statsof(s):
    a, _ = components(s, nbA); b, mx = components(s, nb1); return a, b, mx/len(s), greedy_cover(s, ch)
act = []; nul = []; nulw = []
w = p / p.sum()
for i in idx:
    m, s = ev[i]; act.append(statsof(s))
    r = np.array(rng.sample(range(K), m), dtype=np.int32); nul.append(statsof(r))
    rw = np.random.default_rng(i).choice(K, size=m, replace=False, p=w).astype(np.int32); nulw.append(statsof(rw))
for name, L in [('actual', act), ('uniform null', nul), ('p-weighted null', nulw)]:
    A = np.array(L, dtype=float)
    print(f'{name:16s} (N={len(L)}, mean M={np.mean([ev[i][0] for i in idx]):.1f}): #comp adj {A[:,0].mean():.2f}, #comp 1pt {A[:,1].mean():.2f}, largest1pt/M {A[:,2].mean():.3f}, cover# {A[:,3].mean():.2f}')
print('## same, restricted to events with M >= 10')
big = [i for i in idx if ev[i][0] >= 10]
for name, L in [('actual', act), ('uniform null', nul), ('p-weighted null', nulw)]:
    A = np.array([L[j] for j, i in enumerate(idx) if ev[i][0] >= 10], dtype=float)
    if len(A): print(f'{name:16s} (N={len(A)}, mean M={np.mean([ev[i][0] for i in big]):.1f}): #comp adj {A[:,0].mean():.2f}, #comp 1pt {A[:,1].mean():.2f}, largest1pt/M {A[:,2].mean():.3f}, cover# {A[:,3].mean():.2f}')
