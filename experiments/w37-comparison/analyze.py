#!/usr/bin/env python3
"""W37 analyze.py — tasks 2 & 3 on the exact tables data/av{n}.txt.
usage: analyze.py rank K      -- hardest patterns vs identity per n; #harder; crossovers; shifts
       analyze.py sort K      -- bubble-step (adjacent-inversion sort) monotonicity: all violations
Output is plain text to stdout (results.md is assembled from it)."""
import sys, os, glob, math
from math import log, factorial

here = os.path.dirname(os.path.abspath(__file__))
AV = {}   # AV[n][pat-string] = Av_n(pat), for patterns of length K
NS = []

def load(K):
    global NS
    for f in sorted(glob.glob(f'{here}/data/av*.txt')):
        n = int(os.path.basename(f)[2:-4])
        if n < K: continue
        d = {}
        for line in open(f):
            k, pat, av = line.split()
            if int(k) == K: d[pat] = int(av)
        if d: AV[n] = d; NS.append(n)
    NS.sort()

def sym_class(p):
    k = len(p)
    inv = [0]*k
    for i, v in enumerate(p): inv[v-1] = i+1
    out = set()
    for q in (tuple(p), tuple(inv)):
        for r in range(2):
            for c in range(2):
                t = q[::-1] if r else q
                t = tuple(k+1-x for x in t) if c else t
                out.add(t)
    return min(out)

def s2p(s): return tuple(int(ch) for ch in s)
def p2s(p): return ''.join(map(str, p))

def rank(K):
    load(K)
    idp = ''.join(map(str, range(1, K+1)))
    print(f'== k={K}: identity vs the field (exact Av_n; excess = ln Av_n(pi) - ln Av_n(id) = ln p_pi - ln p_id) ==')
    print('n  Av_n(id)   #pi harder(>id)  #classes harder  hardest pattern (class rep)  max excess')
    hardest_by_n = {}
    for n in NS:
        d = AV[n]
        avid = d[idp]
        harder = [p for p in d if d[p] > avid]
        classes = sorted(set(sym_class(s2p(p)) for p in harder))
        best = max(d, key=lambda p: d[p])
        hardest_by_n[n] = best
        print(f'{n}  {avid}  {len(harder)}  {len(classes)}  {p2s(sym_class(s2p(best)))}  {log(d[best]/avid):+.6f}')
    # per-class excess trajectory for classes that are ever harder
    ever = set()
    for n in NS:
        d = AV[n]; avid = d[idp]
        for p in d:
            if d[p] > avid: ever.add(sym_class(s2p(p)))
    print(f'-- classes ever harder than id: {len(ever)}')
    print('class      ' + ' '.join(f'n={n}' for n in NS))
    rows = []
    for cl in sorted(ever):
        exc = [log(AV[n][p2s(cl)]/AV[n][idp]) for n in NS]
        rows.append((exc[-1], cl, exc))
    for _, cl, exc in sorted(rows, reverse=True):
        print(p2s(cl) + '  ' + ' '.join(f'{e:+.4f}' for e in exc))
    # crossover: first n from which excess stays > 0
    print('-- crossover n_x (first n with Av>Av(id) from which it stays): ')
    for _, cl, exc in sorted(rows, reverse=True):
        nx = None
        for i, n in enumerate(NS):
            if all(e > 0 for e in exc[i:]): nx = n; break
        print(f'{p2s(cl)}: n_x = {nx}  (n_x/k^2 = {nx/K**2:.2f})' if nx else f'{p2s(cl)}: none')
    # shift: s_pi(n) = n - max{m<=n : pbar_id(m) >= pbar_pi(n)}
    print('-- rate-form shift s(n) = n - max{m : p_id(m) >= p_pi(n)} for the hardest class:')
    pid = {n: AV[n][idp]/factorial(n) for n in NS}
    for _, cl, exc in sorted(rows, reverse=True)[:3]:
        line = []
        for n in NS:
            pp = AV[n][p2s(cl)]/factorial(n)
            m = max((mm for mm in NS if mm <= n and pid[mm] >= pp), default=None)
            line.append(f'n={n}:s={n-m}' if m is not None else f'n={n}:s>?')
        print(p2s(cl) + '  ' + ' '.join(line))

def bubble_ups(p):
    """all (i, p') with p' = p after sorting the adjacent inversion at positions i,i+1"""
    out = []
    for i in range(len(p)-1):
        if p[i] > p[i+1]:
            q = list(p); q[i], q[i+1] = q[i+1], q[i]
            out.append((i, tuple(q)))
    return out

def sortmono(K):
    load(K)
    print(f'== k={K}: bubble-step monotonicity test: pi\' = one adjacent-inversion sort of pi; '
          f'conjecture Av_n(pi\') >= Av_n(pi) ==')
    print('n  #edges  #violations(strict)  #equal  #ok(strict)')
    viol_by_edge = {}
    for n in NS:
        d = AV[n]
        nv = ne = nok = tot = 0
        for ps in d:
            p = s2p(ps)
            for i, q in bubble_ups(p):
                tot += 1
                a, b = d[p2s(q)], d[ps]
                if a < b:
                    nv += 1
                    viol_by_edge.setdefault((ps, p2s(q)), []).append(n)
                elif a == b: ne += 1
                else: nok += 1
        print(f'{n}  {tot}  {nv}  {ne}  {nok}')
    print(f'-- distinct violating edges (pi -> pi\'), with the n where they violate '
          f'(edge classes up to symmetry shown for the persistent ones):')
    persistent = [(e, ns) for e, ns in sorted(viol_by_edge.items()) if NS[-1] in ns]
    print(f'total distinct violating edges: {len(viol_by_edge)}; violating at n={NS[-1]}: {len(persistent)}')
    # group persistent by symmetry class of (pi, pi') pair
    seen = set(); reps = []
    for (ps, qs), ns in persistent:
        key = (sym_class(s2p(ps)), sym_class(s2p(qs)))
        if key in seen: continue
        seen.add(key); reps.append(((ps, qs), ns))
    print(f'persistent violating edges up to (class(pi),class(pi\')) symmetry: {len(reps)}')
    for (ps, qs), ns in reps:
        d = AV[NS[-1]]
        print(f'  {ps} -> {qs}: violates at n={ns}; at n={NS[-1]}: Av(pi)={d[ps]} > Av(pi\')={d[qs]} '
              f'(excess {log(d[ps]/d[qs]):+.5f})')

if __name__ == '__main__':
    mode, K = sys.argv[1], int(sys.argv[2])
    if mode == 'rank': rank(K)
    elif mode == 'sort': sortmono(K)
