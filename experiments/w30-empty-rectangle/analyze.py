"""Tables for results.md from out/k{K}_n{N}_s*.txt (format: see erect.c header)."""
import sys, glob, math, re
from collections import defaultdict
import numpy as np

def load(k, n):
    rows = []
    for f in glob.glob('out/k%d_n%d_s*.txt' % (k, n)):
        for ln in open(f):
            if not ln.strip() or ln.startswith('#'): continue
            p = ln.split('|')
            if len(p) < 4: continue
            M = int(p[0]); rr = list(map(int, p[2].split())); kk = list(map(int, p[3].split()))
            rects = [tuple(rr[6*i:6*i+6]) for i in range(len(rr)//6)]  # a b c d area Kc
            grid = list(map(int, p[4].split())) if len(p) > 4 else []; hist = list(map(int, p[5].split())) if len(p) > 5 else []
            rows.append((M, rects, kk[0], kk[1], kk[2] if len(kk) > 2 else 0, grid, hist))
    return rows

def mu_w24(k):
    """mean M per n from the W24 dumps (first column)."""
    out = {}
    for f in glob.glob('../w24-union-slack/out/k%d_n*_s*.txt' % k):
        n = int(re.search(r'_n(\d+)_', f).group(1)); s = 0; c = 0
        for ln in open(f):
            if ln[0] == '#' or not ln.strip(): continue
            s += int(ln.split()[0]); c += 1
        if c: out.setdefault(n, []).append((s, c))
    d = {n: sum(a for a, b in v)/sum(b for a, b in v) for n, v in out.items()}
    for ln in open('out/mu_small.txt'):
        kk, n, m = ln.split(); 
        if int(kk) == k and int(n) not in d: d[int(n)] = float(m)
    return d

def spearman(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    rx = x.argsort().argsort(); ry = y.argsort().argsort()
    return float(np.corrcoef(rx, ry)[0, 1])

def table(k, n):
    rows = load(k, n); S = len(rows)
    pos = [r for r in rows if r[0] > 0]
    print('\n## k=%d n=%d  (%d samples, P(M>0)=%.3f, E M=%.2f, E[M|M>0]=%.2f)' % (k, n, S, len(pos)/S, sum(r[0] for r in rows)/S, sum(r[0] for r in pos)/max(1, len(pos))))
    # attribution to the largest defect
    M = np.array([r[0] for r in pos]); Kc1 = np.array([r[1][0][5] for r in pos]); Kany = np.array([r[2] for r in pos]); Kun = np.array([r[3] for r in pos])
    A1 = np.array([r[1][0][4] for r in pos]); w1 = np.array([r[1][0][1]-r[1][0][0]+1 for r in pos]); h1 = np.array([r[1][0][3]-r[1][0][2]+1 for r in pos])
    Kr = np.array([r[4] for r in pos]); G = np.array([r[5] for r in pos]); H = np.array([r[6] for r in pos])
    print('Attribution (M>0): mean Kc1/M=%.3f  mean Kany1/M=%.3f  mean Kunion_R/M=%.3f  mean Krand/M=%.3f | sum Kc1/sum M=%.3f  sum Kany1/sum M=%.3f  sum Kunion/sum M=%.3f  sum Krand/sum M=%.3f | P(Kany1=M)=%.3f P(Kc1=M)=%.3f P(Kc1=0)=%.3f P(Krand=0)=%.3f' % (
        (Kc1/M).mean(), (Kany/M).mean(), (Kun/M).mean(), (Kr/M).mean(), Kc1.sum()/M.sum(), Kany.sum()/M.sum(), Kun.sum()/M.sum(), Kr.sum()/M.sum(), (Kany == M).mean(), (Kc1 == M).mean(), (Kc1 == 0).mean(), (Kr == 0).mean()))
    if G.size:
        print('3x3 grid phantoms: sum K_g / sum M per grid point (rows = position thirds, cols = value thirds):')
        gs = G.sum(0)/M.sum()
        for i in range(3): print('    ' + ' '.join('%.3f' % gs[3*i+j] for j in range(3)))
        print('  mean over grid points %.3f (corner mean %.3f, centre %.3f); best-of-9 / M (mean of ratio) = %.3f; P(best-of-9 = M) = %.3f' % (gs.mean(), gs[[0,2,6,8]].mean(), gs[4], (G.max(1)/M).mean(), (G.max(1) == M).mean()))
        hs = H.sum(0); print('  revival multiplicity histogram over missing patterns (#grid phantoms out of 9 reviving π), fractions: ' + ' '.join('%.3f' % (h/hs.sum()) for h in hs) + '  mean = %.2f' % (sum(i*h for i, h in enumerate(hs))/hs.sum()))
        for lo, hi in [(1, 3), (4, 29), (30, 10**9)]:
            s = (M >= lo) & (M <= hi)
            if s.sum(): hs = H[s].sum(0); print('    M in %d–%d: ' % (lo, hi) + ' '.join('%.3f' % (h/hs.sum()) for h in hs) + '  mean = %.2f' % (sum(i*h for i, h in enumerate(hs))/hs.sum()))
    print('| M bin | #σ | mean M | mean Kc1 | mean Kany1 | mean Kunion_R | mean Krand | Kc1/M (mean of ratio) | Krand/M | Kunion/M | mean area Q1 | mean min(w,h) |')
    print('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for lo, hi in [(1, 1), (2, 3), (4, 9), (10, 29), (30, 99), (100, 299), (300, 10**9)]:
        s = (M >= lo) & (M <= hi)
        if s.sum() == 0: continue
        print('| %d–%d | %d | %.1f | %.1f | %.1f | %.1f | %.1f | %.3f | %.3f | %.3f | %.0f | %.1f |' % (lo, hi, s.sum(), M[s].mean(), Kc1[s].mean(), Kany[s].mean(), Kun[s].mean(), Kr[s].mean(), (Kc1[s]/M[s]).mean(), (Kr[s]/M[s]).mean(), (Kun[s]/M[s]).mean(), A1[s].mean(), np.minimum(w1, h1)[s].mean()))
    # M and K vs area of Q1 (all σ)
    Mall = np.array([r[0] for r in rows]); Aall = np.array([r[1][0][4] for r in rows]); wall = np.array([r[1][0][1]-r[1][0][0]+1 for r in rows]); hall = np.array([r[1][0][3]-r[1][0][2]+1 for r in rows])
    Kall = np.array([r[2] for r in rows]); mn = np.minimum(wall, hall); mx = np.maximum(wall, hall)
    mu = mu_w24(k)
    print('Spearman over all σ: (M, area Q1)=%.3f  (M, min(w,h))=%.3f  (M, max(w,h))=%.3f' % (spearman(Mall, Aall), spearman(Mall, mn), spearman(Mall, mx)))
    print('| area Q1 / n² | #σ | P(M>0) | E M | E[M|M>0] | E Kany1 | E[Kany1|M>0] | mean min(w,h) | μ_W24(n−min(w,h)) (interp.) |')
    print('|---|---|---|---|---|---|---|---|---|')
    qs = np.quantile(Aall, [0, .2, .4, .6, .8, .9, .97, 1.0]); qs[-1] += 1
    for i in range(len(qs)-1):
        s = (Aall >= qs[i]) & (Aall < qs[i+1]); sp = s & (Mall > 0)
        if s.sum() == 0: continue
        mnm = mn[s].mean(); nn = n - mnm
        ns = sorted(mu); import bisect
        j = bisect.bisect_left(ns, nn); mub = float('nan')
        if 0 < j < len(ns):
            n0, n1 = ns[j-1], ns[j]; mub = math.exp(math.log(mu[n0]) + (nn-n0)/(n1-n0)*(math.log(mu[n1])-math.log(mu[n0])))
        print('| %.3f–%.3f | %d | %.3f | %.2f | %.1f | %.2f | %.1f | %.1f | %.1f |' % (qs[i]/n**2, qs[i+1]/n**2, s.sum(), (Mall[s] > 0).mean(), Mall[s].mean(), Mall[sp].mean() if sp.sum() else 0, Kall[s].mean(), Kall[sp].mean() if sp.sum() else 0, mnm, mub))
    # K_c vs area for ALL top-R rectangles of σ with M>0 (per-rectangle scaling)
    ar = []; kc = []; asp = []; mm = []
    for r in pos:
        for q in r[1]:
            ar.append(q[4]); kc.append(q[5]); asp.append(min(q[1]-q[0]+1, q[3]-q[2]+1)/max(q[1]-q[0]+1, q[3]-q[2]+1)); mm.append(r[0])
    ar = np.array(ar); kc = np.array(kc); asp = np.array(asp); mm = np.array(mm)
    print('Per-rectangle (top-R rects of σ with M>0, %d rects): Spearman(Kc, area)=%.3f Spearman(Kc/M, area)=%.3f Spearman(Kc/M, aspect)=%.3f' % (len(ar), spearman(kc, ar), spearman(kc/mm, ar), spearman(kc/mm, asp)))
    print('| area/n² bin | #rects | mean Kc | P(Kc>0) | mean Kc/M | mean Kc | Kc=M frac |')
    print('|---|---|---|---|---|---|---|')
    qs = np.quantile(ar, [0, .1, .3, .5, .7, .9, .97, 1.0]); qs[-1] += 1
    for i in range(len(qs)-1):
        s = (ar >= qs[i]) & (ar < qs[i+1])
        if s.sum() == 0: continue
        print('| %.3f–%.3f | %d | %.2f | %.3f | %.3f | %.2f | %.3f |' % (qs[i]/n**2, qs[i+1]/n**2, s.sum(), kc[s].mean(), (kc[s] > 0).mean(), (kc[s]/mm[s]).mean(), kc[s].mean(), (kc[s] == mm[s]).mean()))
    print('| aspect min/max bin | #rects | mean Kc/M | P(Kc>0) |'); print('|---|---|---|---|')
    for lo, hi in [(0, .2), (.2, .4), (.4, .6), (.6, .8), (.8, 1.01)]:
        s = (asp >= lo) & (asp < hi)
        if s.sum(): print('| %.1f–%.1f | %d | %.3f | %.3f |' % (lo, hi, s.sum(), (kc[s]/mm[s]).mean(), (kc[s] > 0).mean()))
    # distribution of Kany1 (tail) -- is K e^{O(k)}?
    print('Kany1 quantiles (M>0): 50/90/99/max = %s ; Kc1: %s ; log(max Kany1)/k = %.2f, log(mean Kany1|M>0)/k=%.2f' % (
        np.quantile(Kany, [.5, .9, .99, 1]).tolist(), np.quantile(Kc1, [.5, .9, .99, 1]).tolist(), math.log(max(1, Kany.max()))/k, math.log(max(1e-9, Kany.mean()))/k))

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        k, n = map(int, arg.split(','))
        table(k, n)
