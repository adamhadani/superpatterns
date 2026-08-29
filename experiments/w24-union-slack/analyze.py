#!/usr/bin/env python3
"""Post-process out/k*_n*_s*.txt dumps from mslack.  Usage: analyze.py [tables|fits|pairs|struct|all]"""
import glob, math, os, re, sys, random
from collections import defaultdict, Counter
from patlib import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')

def load():
    """returns {(k,n): {'M': [...], 'miss': {sample_index: [codes]}, 'samples': int}} pooled over seeds"""
    data = defaultdict(lambda: {'M': [], 'miss': {}})
    for f in sorted(glob.glob(os.path.join(OUT, 'k*_n*_s*.txt'))):
        m = re.match(r'.*/k(\d+)_n(\d+)_s(\d+)\.txt', f)
        k, n = int(m.group(1)), int(m.group(2))
        d = data[(k, n)]
        with open(f) as fh:
            for line in fh:
                if line.startswith('#'): continue
                parts = line.split()
                if not parts: continue
                M = int(parts[0]); idx = len(d['M']); d['M'].append(M)
                if M > 0 and len(parts) > 1: d['miss'][idx] = [int(c) for c in parts[1:]]
    return data

def quant(xs, q):
    if not xs: return float('nan')
    xs = sorted(xs); i = min(len(xs)-1, int(q*len(xs)))
    return xs[i]

def stats(M):
    S = len(M); pos = [x for x in M if x > 0]; P = len(pos)/S
    EM = sum(M)/S
    R = (sum(pos)/len(pos)) if pos else float('nan')
    # bootstrap SE for ln R
    lnRs = []
    rnd = random.Random(1)
    if pos and P < 1:
        for b in range(200):
            bs = [M[rnd.randrange(S)] for _ in range(S)]; bp = [x for x in bs if x > 0]
            if bp: lnRs.append(math.log(sum(bp)/len(bp)))
    se = (sum((x-sum(lnRs)/len(lnRs))**2 for x in lnRs)/(len(lnRs)-1))**0.5 if len(lnRs) > 2 else float('nan')
    EM2 = sum(x*x for x in M)/S
    return dict(S=S, P=P, npos=len(pos), EM=EM, R=R, lnR=math.log(R) if pos else float('nan'), se=se,
                med=quant(pos, .5), q10=quant(pos, .1), q90=quant(pos, .9), q99=quant(pos, .99), mx=max(M),
                geo=math.exp(sum(math.log(x) for x in pos)/len(pos)) if pos else float('nan'),
                ratio2=EM2/EM**2 if EM > 0 else float('nan'))

def table(data):
    print('### Task 1: distribution of M = #missing k-patterns (pooled over seeds)')
    print('Columns: samples; Pr(M>0) (#events); E[M]; R=E[M|M>0]; ln R (± bootstrap SE); median, q10, q90, q99 of M|M>0; max M; geometric mean of M|M>0; E[M²]/E[M]².')
    for k in sorted({k for k, n in data}):
        print(f'\n#### k = {k}  (k! = {math.factorial(k)}, k² = {k*k})')
        print('| n | n/k² | samples | Pr(M>0) | #M>0 | E[M] | R | ln R | med | q10 | q90 | q99 | max | geo | E[M²]/E[M]² |')
        print('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
        for (kk, n) in sorted(data):
            if kk != k: continue
            s = stats(data[(k, n)]['M'])
            print(f"| {n} | {n/k/k:.2f} | {s['S']} | {s['P']:.4f} | {s['npos']} | {s['EM']:.4g} | {s['R']:.4g} | {s['lnR']:.3f}±{s['se']:.3f} | {s['med']} | {s['q10']} | {s['q90']} | {s['q99']} | {s['mx']} | {s['geo']:.3g} | {s['ratio2']:.3g} |")

def hist(data):
    print('\n### Histograms of ln M given M>0 (bins of width 1 in ln M; counts)')
    for (k, n) in sorted(data):
        pos = [x for x in data[(k, n)]['M'] if x > 0]
        if not pos: continue
        c = Counter(int(math.log(x)) for x in pos)
        print(f"k={k} n={n}: " + ' '.join(f"[{b},{b+1}):{c[b]}" for b in sorted(c)))

def interp(xs, ys, x):
    """linear interpolation of y at x from sorted xs"""
    for i in range(len(xs)-1):
        if xs[i] <= x <= xs[i+1]:
            t = (x-xs[i])/(xs[i+1]-xs[i]); return ys[i]+t*(ys[i+1]-ys[i])
    return float('nan')

def fits(data):
    print('\n### Task 2: ln R vs k at fixed n/k² and at n = t(k) (Pr(M>0)=1/2)')
    ks = sorted({k for k, n in data})
    rows = {}
    for k in ks:
        pts = sorted((n, stats(data[(k, n)]['M'])) for (kk, n) in data if kk == k)
        ns = [n for n, s in pts]; lnR = [s['lnR'] for n, s in pts]; P = [s['P'] for n, s in pts]
        # t(k): n where P crosses 1/2 (P decreasing in n)
        tk = float('nan')
        for i in range(len(ns)-1):
            if P[i] >= .5 >= P[i+1] and P[i] != P[i+1]:
                tk = ns[i] + (P[i]-.5)/(P[i]-P[i+1])*(ns[i+1]-ns[i]); break
        rows[k] = dict(tk=tk, lnR_t=interp(ns, lnR, tk), lnEM_t=interp(ns, [math.log(s['EM']) if s['EM']>0 else float('nan') for n, s in pts], tk))
        for a in (0.65, 0.75, 0.85, 1.0, 1.2):
            rows[k][a] = interp(ns, lnR, a*k*k)
        # also at fixed Pr(M>0) = 0.1 and 0.9
        for p in (0.9, 0.1, 0.02):
            npx = float('nan')
            for i in range(len(ns)-1):
                if P[i] >= p >= P[i+1] and P[i] != P[i+1]:
                    npx = ns[i] + (P[i]-p)/(P[i]-P[i+1])*(ns[i+1]-ns[i]); break
            rows[k][f'P{p}'] = (npx, interp(ns, lnR, npx))
    print('| k | t(k) (interp.) | ln R at t(k) | ln E[M] at t(k) | ln R @0.65k² | @0.75k² | @0.85k² | @1.0k² | @1.2k² | n,lnR @P=.9 | @P=.1 | @P=.02 | k ln k | k | √k |')
    print('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for k in ks:
        r = rows[k]
        print(f"| {k} | {r['tk']:.1f} | {r['lnR_t']:.3f} | {r['lnEM_t']:.3f} | {r[0.65]:.2f} | {r[0.75]:.2f} | {r[0.85]:.2f} | {r[1.0]:.2f} | {r[1.2]:.2f} | {r['P0.9'][0]:.1f},{r['P0.9'][1]:.2f} | {r['P0.1'][0]:.1f},{r['P0.1'][1]:.2f} | {r['P0.02'][0]:.1f},{r['P0.02'][1]:.2f} | {k*math.log(k):.2f} | {k} | {k**.5:.2f} |")
    # slopes of ln R vs ln k, vs k
    print('\nGrowth diagnostics (successive k):')
    for key, name in [('lnR_t', 'ln R at t(k)'), (0.75, 'ln R at 0.75k²'), (1.0, 'ln R at 1.0k²'), ('P0.1', 'ln R at P=.1'), ('P0.02', 'ln R at P=.02')]:
        vals = [(k, rows[k][key] if not isinstance(rows[k][key], tuple) else rows[k][key][1]) for k in ks]
        vals = [(k, v) for k, v in vals if v == v]
        s = []
        for (k1, v1), (k2, v2) in zip(vals, vals[1:]):
            s.append(f"k{k1}→{k2}: Δ={v2-v1:+.3f}, d lnR/d ln k={(v2-v1)/math.log(k2/k1):.2f}, ratio to Δ(k ln k)={(v2-v1)/(k2*math.log(k2)-k1*math.log(k1)):.3f}, to Δk={(v2-v1)/(k2-k1):.3f}, to Δ√k={(v2-v1)/(k2**.5-k1**.5):.3f}")
        print(f"- {name}: " + '; '.join(s))

def pairs(data, which=None):
    print('\n### Task 3: pairwise correlation ratios  ρ(π,π\') = Pr(A_π ∧ A_π\') / (Pr A_π · Pr A_π\')')
    print('Pooled estimators over all pairs of the given type: ρ_pool = (Σ_pairs #co-miss / S) / (Σ_pairs m_π m_π\' / S²).')
    print('Also E[M²]/E[M]² ≈ ρ for a uniformly random pair (plus the diagonal 1/E[M] term).')
    for (k, n) in sorted(data):
        if which and (k, n) not in which: continue
        d = data[(k, n)]; S = len(d['M']); kf = math.factorial(k)
        if not d['miss'] or S < 1000 and k < 9: continue
        P = len([1 for x in d['M'] if x > 0])/S
        if P < 0.02 or P > 0.995: continue
        cnt = Counter(); 
        for idx, codes in d['miss'].items():
            for c in codes: cnt[c] += 1
        # sample-level sets for pair counting
        sets = [set(c) for c in d['miss'].values()]
        pats = {c: decode(c, k) for c in cnt}
        def comiss(c1, c2): return sum(1 for s in sets if c1 in s and c2 in s)
        # pooled over pair types
        def pooled(pairfun, label):
            num = 0; den = 0.0; npairs = 0
            seen = set()
            for c1 in cnt:
                p = pats[c1]
                for p2 in pairfun(p):
                    c2 = encode(p2)
                    if c2 == c1 or (c2, c1) in seen: continue
                    seen.add((c1, c2)); npairs += 1
                    den += cnt[c1]*cnt.get(c2, 0)/S/S
                    if cnt.get(c2, 0): num += comiss(c1, c2)/S
            return f"{label}: ρ_pool = {num/den if den else float('nan'):.2f} (pairs with both missed: {npairs}, Σco-miss={round(num*S)})"
        def adj(p):  # adjacent transposition of positions and of values
            k = len(p); res = []
            for i in range(k-1):
                q = list(p); q[i], q[i+1] = q[i+1], q[i]; res.append(tuple(q))
                q = list(p); a, b = q.index(i+1), q.index(i+2); q[a], q[b] = q[b], q[a]; res.append(tuple(q))
            return res
        def dih(p): return [reverse(p), complement(p), inverse(p), reverse(complement(p)), inverse(reverse(p)), inverse(complement(p)), reverse(complement(inverse(p)))]
        rnd = random.Random(3)
        allc = list(range(kf))
        def rnd_pairs(p): return [decode(rnd.choice(allc), k) for _ in range(6)]
        s = stats(d['M'])
        print(f"\n**k={k}, n={n}** (S={S}, Pr(M>0)={P:.3f}, E[M]={s['EM']:.3g}, R={s['R']:.3g}, E[M²]/E[M]²={s['ratio2']:.3g})")
        print('- ' + pooled(adj, 'π vs π∘(adjacent transposition), positions and values'))
        print('- ' + pooled(dih, 'π vs dihedral images (rev/comp/inv/…)'))
        print('- ' + pooled(rnd_pairs, 'π vs 6 uniformly random π\''))
        # specific pairs: identity and its neighbours, most-missed pattern
        ident = tuple(range(1, k+1)); ci = encode(ident)
        top = cnt.most_common(3)
        specials = [('id', ident)] + [(f'top{i+1}={"".join(map(str,pats[c]))}', pats[c]) for i, (c, _) in enumerate(top)]
        for name, p in specials:
            c1 = encode(p); m1 = cnt.get(c1, 0)
            if m1 < 5: continue
            outs = []
            for lab, p2 in [('swap pos 1,2', adj(p)[0]), ('swap pos mid', adj(p)[2*(k//2-1)]), ('reverse', reverse(p)), ('complement', complement(p)), ('inverse', inverse(p)), ('rev∘comp', reverse(complement(p)))]:
                c2 = encode(p2); m2 = cnt.get(c2, 0)
                if c2 == c1: outs.append(f"{lab}: same"); continue
                cm = comiss(c1, c2) if m2 else 0
                rho = cm*S/(m1*m2) if m1*m2 else float('nan')
                outs.append(f"{lab}: ρ={rho:.1f} (m1={m1}, m2={m2}, co={cm})")
            print(f"- {name} [miss rate {m1/S:.4f}, {m1/S/(s['EM']/kf):.2f}× avg]: " + '; '.join(outs))

def struct(data, which=None):
    print('\n### Task 4: which patterns are missing (LIS, LDS, monotone runs, decomposability) — missing vs population')
    for (k, n) in sorted(data):
        if which and (k, n) not in which: continue
        d = data[(k, n)]; S = len(d['M']); kf = math.factorial(k)
        P = len([1 for x in d['M'] if x > 0])/S
        if not d['miss'] or P < 0.02 or P > 0.995: continue
        if k >= 9 and n < 55: continue
        cnt = Counter()
        for codes in d['miss'].values():
            for c in codes: cnt[c] += 1
        tot = sum(cnt.values())
        pop = [decode(c, k) for c in range(kf)]
        def avg(f, weighted):
            if weighted: return sum(f(decode(c, k))*w for c, w in cnt.items())/tot
            return sum(f(p) for p in pop)/kf
        feats = [('LIS', lis), ('LDS', lds), ('max(LIS,LDS)', lambda p: max(lis(p), lds(p))), ('#monotone runs', runs), ('#ascending runs', asc_runs),
                 ('⊕-decomposable', lambda p: 1.0*sum_decomposable(p)), ('⊖-decomposable', lambda p: 1.0*skew_decomposable(p)),
                 ('indecomposable (neither)', lambda p: 1.0*(not sum_decomposable(p) and not skew_decomposable(p)))]
        print(f"\n**k={k}, n={n}** (S={S}, Pr(M>0)={P:.3f}, distinct patterns ever missed: {len(cnt)} of {kf}, total misses {tot})")
        print('| feature | missing (weighted by miss count) | population S_k |')
        print('|---|---|---|')
        for name, f in feats:
            print(f"| {name} | {avg(f, True):.3f} | {avg(f, False):.3f} |")
        # distribution of max(LIS,LDS)
        cm = Counter(); cp = Counter()
        for c, w in cnt.items(): cm[max(lis(decode(c, k)), lds(decode(c, k)))] += w
        for p in pop: cp[max(lis(p), lds(p))] += 1
        print('max(LIS,LDS) distribution, missing vs population: ' + ', '.join(f"{v}: {cm[v]/tot:.3f} vs {cp[v]/kf:.3f}" for v in sorted(cp)))
        cm = Counter(); cp = Counter()
        for c, w in cnt.items(): cm[runs(decode(c, k))] += w
        for p in pop: cp[runs(p)] += 1
        print('#monotone runs distribution, missing vs population: ' + ', '.join(f"{v}: {cm[v]/tot:.3f} vs {cp[v]/kf:.3f}" for v in sorted(cp)))
        print('top-12 missed patterns (miss count, ×avg): ' + ', '.join(f"{''.join(map(str, decode(c, k)))} ({w}, {w/(tot/kf):.1f}×)" for c, w in cnt.most_common(12)))
        # is the typical failing sigma missing a *cluster*? fraction of samples with M>0 whose missing set contains a dihedral pair / adjacent-transposition pair
        npos = 0; nadj = 0; ndih = 0
        for codes in d['miss'].values():
            st = set(codes); npos += 1
            ps = [decode(c, k) for c in codes[:200]]
            if any(encode(q) in st for p in ps for q in [reverse(p), complement(p), inverse(p)] if q != p): ndih += 1
            def adjs(p):
                for i in range(len(p)-1):
                    q = list(p); q[i], q[i+1] = q[i+1], q[i]; yield tuple(q)
            if any(encode(q) in st for p in ps for q in adjs(p)): nadj += 1
        print(f"among σ with M>0: fraction whose missing set contains an adjacent-transposition pair: {nadj/npos:.3f}; a dihedral-image pair: {ndih/npos:.3f}")
        # cluster structure: components of the missing set under adjacent transpositions (positions and values)
        comps = []; bigfrac = []
        for codes in d['miss'].values():
            st = set(codes)
            if len(st) > 3000: continue
            seen = set(); ncomp = 0; big = 0
            for c0 in codes:
                if c0 in seen: continue
                ncomp += 1; stack = [c0]; seen.add(c0); size = 0
                while stack:
                    c = stack.pop(); size += 1; p = decode(c, k)
                    for i in range(k-1):
                        q = list(p); q[i], q[i+1] = q[i+1], q[i]; cq = encode(q)
                        if cq in st and cq not in seen: seen.add(cq); stack.append(cq)
                        q = list(p); a, b = q.index(i+1), q.index(i+2); q[a], q[b] = q[b], q[a]; cq = encode(q)
                        if cq in st and cq not in seen: seen.add(cq); stack.append(cq)
                big = max(big, size)
            comps.append(ncomp); bigfrac.append(big/len(st))
        Mpos = [len(v) for v in d['miss'].values() if len(v) <= 3000]
        print(f"cluster structure (adjacent-transposition graph on the missing set, σ with 0<M≤3000, {len(comps)} σ): mean M={sum(Mpos)/len(Mpos):.2f}, mean #components={sum(comps)/len(comps):.2f}, mean fraction of M in largest component={sum(bigfrac)/len(bigfrac):.3f}; among σ with M≥10: mean #components={(lambda L: sum(L)/len(L) if L else float('nan'))([c for c, m in zip(comps, Mpos) if m >= 10]):.2f}, mean M={(lambda L: sum(L)/len(L) if L else float('nan'))([m for m in Mpos if m >= 10]):.1f}")

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    data = load()
    if what in ('tables', 'all'): table(data); hist(data)
    if what in ('fits', 'all'): fits(data)
    if what in ('pairs', 'all'): pairs(data)
    if what in ('struct', 'all'): struct(data)
