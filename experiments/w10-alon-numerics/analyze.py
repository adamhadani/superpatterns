#!/usr/bin/env python3
"""Aggregate out/chain_{tau}_{N}.txt (lines: N tau seed L LIS) and fit
   L_tau(N)        = c sqrt(N) - a N^{1/6} + b            (KPZ-type, as for LIS)
   j L_tau - LIS   = alpha sqrt(N) + beta N^{1/6} + gamma (paired: alpha/j = c_tau - 2/j with small error)
Errors: weighted LSQ with per-N standard errors; parameter errors from the covariance (chi^2-scaled if chi2/dof>1).
"""
import glob, re, sys, math
import numpy as np
from collections import defaultdict

def wlsq(X, y, w):
    # weighted least squares; returns beta, stderr, chi2/dof
    W = np.sqrt(w)
    A = X * W[:, None]; b = y * W
    beta, *_ = np.linalg.lstsq(A, b, rcond=None)
    dof = max(len(y) - X.shape[1], 1)
    res = b - A @ beta
    chi2 = float(res @ res)
    cov = np.linalg.inv(A.T @ A) * max(chi2 / dof, 1.0)
    return beta, np.sqrt(np.diag(cov)), chi2 / dof

data = defaultdict(lambda: defaultdict(list))   # data[tau][N] -> list of (L, LIS)
for f in glob.glob('out/chain_*_*.txt'):
    for line in open(f):
        p = line.split()
        if len(p) != 5: continue
        N, tau, seed, L, LIS = int(p[0]), p[1], int(p[2]), int(p[3]), int(p[4])
        data[tau][N].append((L, LIS))

rows = []
for tau in sorted(data, key=lambda t: (len(t), t)):
    j = len(tau)
    Ns = sorted(data[tau])
    if len(Ns) < 2: continue
    two = len(Ns) < 3   # only 2 N values: drop the constant term
    means, ses, dmeans, dses, ns = [], [], [], [], []
    for N in Ns:
        arr = np.array(data[tau][N], dtype=float)
        L, LIS = arr[:, 0], arr[:, 1]
        n = len(L)
        means.append(L.mean()); ses.append(L.std(ddof=1) / math.sqrt(n) if n > 1 else 1.0)
        D = j * L - LIS
        dmeans.append(D.mean()); dses.append(D.std(ddof=1) / math.sqrt(n) if n > 1 else 1.0)
        ns.append(n)
    Na = np.array(Ns, float)
    cols = [np.sqrt(Na), -Na ** (1 / 6)] + ([] if two else [np.ones_like(Na)])
    X = np.stack(cols, 1)
    bb, ee, chi = wlsq(X, np.array(means), 1 / np.maximum(np.array(ses), 1e-3) ** 2)
    c, a = bb[0], bb[1]; ec, ea = ee[0], ee[1]; b = bb[2] if not two else 0.0
    cols2 = [np.sqrt(Na), Na ** (1 / 6)] + ([] if two else [np.ones_like(Na)])
    X2 = np.stack(cols2, 1)
    bb2, ee2, chi2 = wlsq(X2, np.array(dmeans), 1 / np.maximum(np.array(dses), 1e-3) ** 2)
    al, be = bb2[0], bb2[1]; eal, ebe = ee2[0], ee2[1]; ga = bb2[2] if not two else 0.0
    rows.append(dict(tau=tau, j=j, Ns=Ns, ns=ns, means=means, ses=ses, dmeans=dmeans, dses=dses,
                     c=c, ec=ec, a=a, b=b, chi=chi, al=al, eal=eal, be=be, ebe=ebe, ga=ga, chi2=chi2))

mode = sys.argv[1] if len(sys.argv) > 1 else 'table'
if mode == 'table':
    print('| tau | j | 2/j | c_tau (fit) | c_tau - 2/j (paired fit alpha/j) | a | z-score of (c_tau-2/j) | samples/N |')
    print('|---|---|---|---|---|---|---|---|')
    for r in rows:
        dev = r['al'] / r['j']; edev = r['eal'] / r['j']
        print(f"| {r['tau']} | {r['j']} | {2/r['j']:.4f} | {r['c']:.4f} ± {r['ec']:.4f} | {dev:+.4f} ± {edev:.4f} | {r['a']:.2f} | {dev/edev:+.1f} | {'/'.join(map(str,r['ns']))} |")
elif mode == 'raw':
    for r in rows:
        print(f"tau={r['tau']}  (j={r['j']})  fit L = {r['c']:.4f} sqrt(N) - {r['a']:.3f} N^(1/6) + {r['b']:.3f}   chi2/dof={r['chi']:.2f}")
        print("   N     n    mean L   se     j*L-LIS   se")
        for N, n, m, s, d, ds in zip(r['Ns'], r['ns'], r['means'], r['ses'], r['dmeans'], r['dses']):
            print(f"  {N:6d} {n:4d}  {m:8.3f} {s:6.3f}   {d:+7.3f} {ds:6.3f}")
        print(f"   paired fit: jL-LIS = {r['al']:+.4f} sqrt(N) {r['be']:+.3f} N^(1/6) {r['ga']:+.3f}   (chi2/dof={r['chi2']:.2f})")
elif mode == 'md':
    import datetime
    out = []
    out.append('# W10 results — c_τ estimates for all τ ∈ S_2…S_5 (symmetry classes under ⟨inverse, reverse-complement⟩)\n')
    out.append(f'Generated {datetime.date.today()} by analyze.py from out/chain_*.txt.  L_τ(N) = longest τ-chain, LIS on the same permutation.\n')
    out.append('Fits: (F1) L = c√N − a N^{1/6} + b;  (F2) paired jL − LIS = α√N + βN^{1/6} + γ, dev := α/j = c_τ − 2/j (much smaller error).\n')
    out.append('Rigorous LB: c_τ ≥ 0.9987·E L_τ(N′)/√(N′+3√N′) with N′ = the largest N run (superadditivity, Poissonized; MC error ≈ se).\n')
    out.append('| τ | j | 2/j | c_τ (F1) | dev = c_τ−2/j (F2) | z | β (N^{1/6} coeff of jL−LIS) | a (F1) | rigorous LB on c_τ | LB/(2/j) | samples per N |')
    out.append('|---|---|---|---|---|---|---|---|---|---|---|')
    worst = []
    for r in rows:
        dev = r['al'] / r['j']; edev = r['eal'] / r['j']
        Nmax = r['Ns'][-1]; i = len(r['Ns']) - 1
        # use the largest N with >= 20 samples for the LB
        while i > 0 and r['ns'][i] < 20: i -= 1
        Np = r['Ns'][i]; lam = Np + 3 * math.sqrt(Np)
        lb = 0.9987 * (r['means'][i] - 2 * r['ses'][i]) / math.sqrt(lam)   # 2 se margin
        worst.append((dev / edev, r['tau']))
        out.append(f"| {r['tau']} | {r['j']} | {2/r['j']:.4f} | {r['c']:.4f} ± {r['ec']:.4f} | {dev:+.4f} ± {edev:.4f} | {dev/edev:+.1f} | {r['be']:+.2f} ± {r['ebe']:.2f} | {r['a']:.2f} | {lb:.4f} (N′={Np}) | {lb/(2/r['j']):.3f} | {'/'.join(map(str,r['ns']))} |")
    out.append('\nN values: ' + ', '.join(map(str, sorted({N for r in rows for N in r['Ns']}))) + ' (samples per N in the last column, same order; N=100000 only for 6 patterns).\n')
    worst.sort()
    out.append('Most negative z-scores (candidates for c_τ < 2/j): ' + ', '.join(f'{t} (z={z:+.1f})' for z, t in worst[:6]) + '\n')
    out.append('Most positive: ' + ', '.join(f'{t} (z={z:+.1f})' for z, t in worst[-6:]) + '\n')
    out.append('\n## Raw means of jL_τ − LIS by N\n')
    allN = sorted({N for r in rows for N in r['Ns']})
    out.append('| τ | ' + ' | '.join(f'N={N}' for N in allN) + ' |')
    out.append('|---|' + '---|' * len(allN))
    for r in rows:
        dd = {N: (d, s, n) for N, d, s, n in zip(r['Ns'], r['dmeans'], r['dses'], r['ns'])}
        out.append(f"| {r['tau']} | " + ' | '.join((f'{dd[N][0]:+.2f}±{dd[N][1]:.2f} (n={dd[N][2]})' if N in dd else '') for N in allN) + ' |')
    try:
        out.append('\n## Task 4 — containment thresholds N_π (Pr = 1/2) for hybrid ⊕-patterns (thresholds.py, 400 samples per N)\n')
        out.append(open('out/thresholds.md').read())
    except Exception as e:
        out.append(f'(thresholds table missing: {e})')
    open('results.md', 'w').write('\n'.join(out) + '\n')
    print('wrote results.md', len(rows), 'patterns')
