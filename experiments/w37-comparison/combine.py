#!/usr/bin/env python3
"""W37 combine.py N: reconstruct Av_N(pi) for all patterns of length 3..min(7,N) from the
symmetry-reduced task outputs in data/nN/ (lt_*/eq_* files, see run_allpat.sh).
cnt[pi] = C<[pi]+C<[r pi]+C<[c pi]+C<[rc pi] + C=[pi]+C=[r pi];  Av = N! - cnt.
Writes data/avN.txt: lines "k pattern Av_N(pattern)"."""
import glob, math, sys, os
N = int(sys.argv[1])
here = os.path.dirname(os.path.abspath(__file__))
K = min(7, N)
JF = [math.factorial(j) for j in range(8)]

def rankp(p):
    j = len(p); r = 0
    for i in range(j):
        c = sum(1 for t in range(i + 1, j) if p[t] < p[i]); r = r * (j - i) + c
    return r

def unrankp(idx, j):
    code = [0] * j
    for i in range(j - 1, -1, -1):
        code[i] = idx % (j - i); idx //= (j - i)
    avail = list(range(j)); p = []
    for i in range(j):
        p.append(avail.pop(code[i]))
    return tuple(p)

def rev(p): return tuple(reversed(p))
def comp(p): j = len(p); return tuple(j - 1 - x for x in p)

Clt = {}; Ceq = {}
for f in glob.glob(f'{here}/data/n{N}/lt_*.txt'):
    for line in open(f):
        j, idx, c = map(int, line.split()); Clt[(j, idx)] = Clt.get((j, idx), 0) + c
for f in glob.glob(f'{here}/data/n{N}/eq_*.txt'):
    for line in open(f):
        j, idx, c = map(int, line.split()); Ceq[(j, idx)] = Ceq.get((j, idx), 0) + c

fN = math.factorial(N)
out = open(f'{here}/data/av{N}.txt', 'w')
for j in range(3, K + 1):
    for idx in range(JF[j]):
        p = unrankp(idx, j)
        tot = (Clt.get((j, idx), 0) + Clt.get((j, rankp(rev(p))), 0)
               + Clt.get((j, rankp(comp(p))), 0) + Clt.get((j, rankp(comp(rev(p)))), 0)
               + Ceq.get((j, idx), 0) + Ceq.get((j, rankp(rev(p))), 0))
        av = fN - tot
        pat = ''.join(str(x + 1) for x in p)
        out.write(f'{j} {pat} {av}\n')
out.close()
print('wrote', f'data/av{N}.txt')
