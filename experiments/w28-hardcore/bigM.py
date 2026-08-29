#!/usr/bin/env python3
"""W28: anatomy of the events by size of M: are large missing sets up-sets of fully-missing (k-1)-patterns? Usage: bigM.py K n"""
import sys, math, numpy as np
from hardcore import *
k = int(sys.argv[1]); n = int(sys.argv[2]); K = math.factorial(k)
pats, st = pattern_table(k); nb1, ch = onepoint_neighbors(k, pats)
U = {}
for c, s in enumerate(ch):
    for t in s: U.setdefault(t, set()).add(c)
M, sets = load(k, n)
print(f'# k={k} n={n}: |U(tau)| (extensions of a (k-1)-pattern): mean {np.mean([len(v) for v in U.values()]):.1f}, max {max(len(v) for v in U.values())}; number of tau = {len(U)}')
print('| M range | #events | share of Σ M (=share of R) | mean #fully-missing τ (U(τ)⊆miss) | mean frac of M inside fully-missing U(τ) | mean #τ with |U(τ)∩miss| ≥ |U(τ)|/2 | frac M in those | E_miss[maxmono] | frac maxmono ≥ k−1 | mean greedy cover | cover/M |')
print('|' + '---|'*11)
tot = M.sum()
for lo, hi in [(1,1),(2,3),(4,9),(10,29),(30,99),(100,299),(300,100000)]:
    ev = [s for m, s in zip(M, sets) if lo <= m <= hi]
    if not ev: continue
    full = []; ffrac = []; half = []; hfrac = []; mm = []; f1 = []; cov = []
    for s in ev:
        S = set(s.tolist()); taus = set().union(*[ch[c] for c in S])
        fm = [t for t in taus if U[t] <= S]; hm = [t for t in taus if 2*len(U[t] & S) >= len(U[t])]
        full.append(len(fm)); ffrac.append(len(set().union(*[U[t] for t in fm]) & S)/len(S) if fm else 0)
        half.append(len(hm)); hfrac.append(len(set().union(*[U[t] for t in hm]) & S)/len(S) if hm else 0)
        mm.append(st['maxmono'][s].mean()); f1.append(np.mean(st['maxmono'][s] >= k-1)); cov.append(greedy_cover(s, ch))
    Ms = [len(s) for s in ev]
    print(f'| {lo}–{hi} | {len(ev)} | {sum(Ms)/tot:.3f} | {np.mean(full):.2f} | {np.mean(ffrac):.3f} | {np.mean(half):.2f} | {np.mean(hfrac):.3f} | {np.mean(mm):.2f} | {np.mean(f1):.3f} | {np.mean(cov):.1f} | {np.mean(np.array(cov)/np.array(Ms)):.3f} |')
