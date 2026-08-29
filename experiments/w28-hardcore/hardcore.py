#!/usr/bin/env python3
"""W28: hard-core / cluster analysis of the missing set of random sigma_n, from the W24 dumps.
Usage: hardcore.py K [n1 n2 ...]   (default: all n for that k).  Writes out/k{K}_*.txt tables to stdout.
"""
import sys, os, glob, re, math, itertools
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'w24-union-slack'))
from patlib import decode, encode, lis, lds, runs, standardise, reverse, complement, inverse

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'w24-union-slack', 'out')

def load(k, n):
    Ms, sets = [], []
    for f in sorted(glob.glob(os.path.join(OUT, f'k{k}_n{n}_s*.txt'))):
        for line in open(f):
            if line.startswith('#') or not line.strip(): continue
            p = line.split(); M = int(p[0]); Ms.append(M)
            sets.append(np.array([int(c) for c in p[1:]], dtype=np.int32) if M > 0 else np.zeros(0, np.int32))
    return np.array(Ms), sets

def binom_moments(M, jmax=4):
    """E C(M,j) for j=1..jmax"""
    return [np.mean([math.comb(int(m), j) for m in M]) for j in range(1, jmax+1)]

def inv_count(p):
    return sum(1 for i in range(len(p)) for j in range(i+1, len(p)) if p[i] > p[j])

def pattern_table(k):
    K = math.factorial(k)
    pats = [decode(c, k) for c in range(K)]
    st = dict(lis=np.array([lis(p) for p in pats]), lds=np.array([lds(p) for p in pats]),
              runs=np.array([runs(p) for p in pats]), inv=np.array([inv_count(p) for p in pats]))
    st['dmono'] = np.minimum(st['inv'], k*(k-1)//2 - st['inv'])  # adj-transposition distance to nearer of id/rev
    st['maxmono'] = np.maximum(st['lis'], st['lds'])
    return pats, st

def children(p):
    """(k-1)-patterns obtained by deleting one entry (as codes)"""
    return {encode(standardise(p[:i]+p[i+1:])) for i in range(len(p))}

def onepoint_neighbors(k, pats):
    """graph on S_k: pi ~ pi' iff they share a (k-1)-child (one point moved). returns list of neighbor arrays"""
    K = len(pats); ch = [children(p) for p in pats]
    bychild = {}
    for c, s in enumerate(ch):
        for t in s: bychild.setdefault(t, []).append(c)
    nb = [set() for _ in range(K)]
    for t, lst in bychild.items():
        for a in lst:
            nb[a].update(lst)
    for a in range(K): nb[a].discard(a)
    return [np.array(sorted(s), dtype=np.int32) for s in nb], ch

def adj_neighbors(k, pats):
    nb = []
    for c, p in enumerate(pats):
        s = []
        for i in range(k-1):
            q = list(p); q[i], q[i+1] = q[i+1], q[i]; s.append(encode(tuple(q)))
        nb.append(np.array(sorted(s), dtype=np.int32))
    return nb

def components(S, nb):
    """number of connected components of the induced subgraph on set S (array of codes)"""
    Sset = set(S.tolist()); seen = set(); ncomp = 0; sizes = []
    for s in S.tolist():
        if s in seen: continue
        ncomp += 1; stack = [s]; seen.add(s); sz = 0
        while stack:
            u = stack.pop(); sz += 1
            for v in nb[u].tolist():
                if v in Sset and v not in seen: seen.add(v); stack.append(v)
        sizes.append(sz)
    return ncomp, max(sizes)

def greedy_cover(S, ch):
    """greedy number of (k-1)-patterns tau whose up-sets cover the missing set S"""
    rem = set(S.tolist()); cnt = 0
    while rem:
        best = {}
        for s in rem:
            for t in ch[s]: best[t] = best.get(t, 0) + 1
        t = max(best, key=best.get); cnt += 1
        rem = {s for s in rem if t not in ch[s]}
    return cnt

def main():
    k = int(sys.argv[1]); K = math.factorial(k)
    ns = [int(x) for x in sys.argv[2:]] or sorted({int(re.match(r'.*_n(\d+)_', f).group(1)) for f in glob.glob(os.path.join(OUT, f'k{k}_n*_s*.txt'))})
    pats, st = pattern_table(k)
    nb1, ch = onepoint_neighbors(k, pats); nbA = adj_neighbors(k, pats)
    idc = encode(tuple(range(1, k+1))); revc = encode(tuple(range(k, 0, -1)))
    uni = {key: np.bincount(v) / K for key, v in st.items()}
    print(f'# k={k}, |S_k|={K}, uniform means: ' + ', '.join(f'{key}={st[key].mean():.3f}' for key in st))
    print('\n## Task 1: law of M, Janson/Bonferroni quantities')
    print('| n | n/k² | S | Pr(M=0) | μ=EM | Δ=E M(M-1) | Δ/μ | ln Pr(M=0)/(−μ) | e^{−μ+Δ/2}>1? | Bonf2: μ−EC(M,2) | Bonf3: +EC(M,3) | μ²/EM² | R | EM²/μ | max_π E[M|π⊄σ] | E[M|id⊄σ] | #id⊄ |')
    print('|' + '---|'*17)
    rows2 = []
    for n in ns:
        M, sets = load(k, n); S = len(M)
        if S == 0: continue
        P0 = np.mean(M == 0); mu = M.mean(); EM2 = np.mean(M.astype(float)**2)
        b = binom_moments(M, 3); Delta = EM2 - mu
        # per-pattern counts and conditional sums
        cnt = np.zeros(K); csum = np.zeros(K)
        for m, s in zip(M, sets):
            if m > 0: cnt[s] += 1; csum[s] += m
        p = cnt / S
        with np.errstate(divide='ignore', invalid='ignore'):
            condE = np.where(cnt > 0, csum / np.maximum(cnt, 1), np.nan)
        lnP0 = math.log(P0) if P0 > 0 else float('-inf')
        ratio = lnP0 / (-mu) if mu > 0 and P0 > 0 else float('nan')
        R = mu / (1 - P0) if P0 < 1 else float('nan')
        print(f'| {n} | {n/k/k:.2f} | {S} | {P0:.4f} | {mu:.4g} | {Delta:.4g} | {Delta/mu if mu>0 else float("nan"):.3g} | {ratio:.3f} | {"yes" if -mu+Delta/2>0 else "no"} | {b[0]-b[1]:.3g} | {b[0]-b[1]+b[2]:.3g} | {mu*mu/EM2 if EM2>0 else float("nan"):.4f} | {R:.3g} | {EM2/mu if mu>0 else float("nan"):.3g} | {np.nanmax(condE) if cnt.sum()>0 else float("nan"):.3g} | {condE[idc]:.3g} | {int(cnt[idc])} |')
        rows2.append((n, M, sets, p, cnt, condE))
    print('\n## Task 2: structure of the missing set (weights p_π = Pr(π⊄σ_n))')
    um = {key: st[key].mean() for key in st}
    print(f"| n | events | top1% share of μ | top10% share | #π with p>0 | p_id/mean p | p_id/max p | E_p[LIS] | E_p[LDS] | E_p[maxmono] (unif {um['maxmono']:.2f}) | E_p[runs] (unif {um['runs']:.2f}) | E_p[dmono] (unif {um['dmono']:.2f}) | frac μ from maxmono≥k−1 (unif {np.mean(st['maxmono']>=k-1):.3f}) | maxmono≥k−2 (unif {np.mean(st['maxmono']>=k-2):.3f}) |")
    print('|' + '---|'*14)
    for n, M, sets, p, cnt, condE in rows2:
        mu = p.sum()
        if mu == 0: continue
        w = p / mu; srt = np.sort(p)[::-1]
        t1 = srt[:max(1, K//100)].sum() / mu; t10 = srt[:K//10].sum() / mu
        print(f'| {n} | {int((M>0).sum())} | {t1:.3f} | {t10:.3f} | {int((p>0).sum())} | {p[idc]/p.mean():.3g} | {p[idc]/p.max():.3g} | {w@st["lis"]:.2f} | {w@st["lds"]:.2f} | {w@st["maxmono"]:.2f} | {w@st["runs"]:.2f} | {w@st["dmono"]:.2f} | {w[st["maxmono"]>=k-1].sum():.3f} | {w[st["maxmono"]>=k-2].sum():.3f} |')
    print('\n### p_π by max(LIS,LDS) class: mean p in class / overall mean p (and class share of μ)')
    for n, M, sets, p, cnt, condE in rows2:
        mu = p.sum()
        if mu == 0: continue
        parts = []
        for v in range(k, 1, -1):
            sel = st['maxmono'] == v
            if sel.sum() == 0: continue
            parts.append(f'{v}:{p[sel].mean()/p.mean():.2f}({p[sel].sum()/mu:.2f},N={sel.sum()})')
        print(f'n={n}: ' + ' '.join(parts))
    print('\n### Conditional structure given M>0: components under adjacent transpositions / one-point moves; greedy (k−1)-cover')
    print('| n | events | mean #comp adj | mean #comp 1pt | mean largest 1pt comp / M | mean cover# | P(cover=1) | E[M|cover=1] | E[M|cover≥2] | max M |')
    print('|' + '---|'*10)
    for n, M, sets, p, cnt, condE in rows2:
        ev = [(m, s) for m, s in zip(M, sets) if m > 0]
        if not ev: continue
        ca = []; c1 = []; frac = []; cov = []
        for m, s in ev:
            a, _ = components(s, nbA); b1, mx = components(s, nb1)
            ca.append(a); c1.append(b1); frac.append(mx / m); cov.append(greedy_cover(s, ch))
        cov = np.array(cov); Ms = np.array([m for m, s in ev])
        print(f'| {n} | {len(ev)} | {np.mean(ca):.2f} | {np.mean(c1):.2f} | {np.mean(frac):.3f} | {cov.mean():.2f} | {np.mean(cov==1):.3f} | {Ms[cov==1].mean() if (cov==1).any() else float("nan"):.3g} | {Ms[cov>=2].mean() if (cov>=2).any() else float("nan"):.3g} | {Ms.max()} |')
    print('\n### Task 3(ii): distribution over π of E[M | π⊄σ_n] (patterns with ≥ 20 conditioning events)')
    print('| n | #π (≥20 ev) | min | median | mean (p-weighted = EM²/μ) | max | argmax pattern | E[M|id⊄] | E[M|maxmono=k−1 ⊄] avg | corr(p_π, E[M|π⊄]) |')
    print('|' + '---|'*10)
    for n, M, sets, p, cnt, condE in rows2:
        ok = cnt >= 20
        if ok.sum() == 0: continue
        c = condE[ok]; am = np.nanargmax(np.where(ok, condE, -1))
        sel = ok & (st['maxmono'] == k-1)
        corr = np.corrcoef(p[ok], c)[0, 1]
        print(f'| {n} | {ok.sum()} | {c.min():.3g} | {np.median(c):.3g} | {(p*np.nan_to_num(condE)).sum()/p.sum():.3g} | {c.max():.3g} | {pats[am]} | {condE[idc]:.3g} | {np.nanmean(condE[sel]) if sel.any() else float("nan"):.3g} | {corr:.3f} |')
    print('\n### Task 3(iii): identity vs reverse / complement-type pairs: co-miss counts (ES bound (k−1)²+1 = %d)' % ((k-1)**2+1))
    for n, M, sets, p, cnt, condE in rows2:
        both = sum(1 for m, s in zip(M, sets) if m > 0 and idc in set(s.tolist()) and revc in set(s.tolist()))
        # LIS<k and LDS<k among all missing pairs: pairs (π,π') with LIS(π)=k... only id; generalise: π with lis=k-1 vs π' with lds=k-1
        print(f'n={n}: #σ with id⊄: {int(cnt[idc])}, rev⊄: {int(cnt[revc])}, both: {both}, independence expectation: {cnt[idc]*cnt[revc]/len(M):.2f}')

if __name__ == '__main__':
    main()
