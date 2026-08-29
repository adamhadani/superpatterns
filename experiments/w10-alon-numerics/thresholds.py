#!/usr/bin/env python3
# Estimate N_pi = N with Pr(pi in Pi_N) = 1/2 for hybrid patterns (identity + spaced adjacent transpositions).
import subprocess, math, sys, json
def frac(N, pi, reps=400, seed=1):
    out = subprocess.run(['./contain', str(N), str(reps), str(seed), ' '.join(map(str, pi))], capture_output=True, text=True).stdout.split()
    return int(out[3]) / int(out[2])
def hybrid(k, r):
    """identity of length k with r adjacent transpositions at (roughly) evenly spaced positions"""
    p = list(range(1, k + 1))
    if r == 0: return p
    for t in range(r):
        i = int((t + 0.5) * k / r) - 1; i = max(0, min(k - 2, i)); i -= i % 2 if False else 0
        p[i], p[i + 1] = p[i + 1], p[i]
    return p
def layered21(k): return [v for i in range(k // 2) for v in (2 * i + 2, 2 * i + 1)]
def find_half(pi, reps=400):
    k = len(pi); lo, hi = max(k, int(k * k / 8)), int(k * k)   # bracket
    flo, fhi = frac(lo, pi, reps), frac(hi, pi, reps)
    while fhi < 0.5: hi *= 2; fhi = frac(hi, pi, reps)
    while flo > 0.5: lo = max(k, lo // 2); flo = frac(lo, pi, reps)
    while hi - lo > max(1, lo // 40):
        m = (lo + hi) // 2; fm = frac(m, pi, reps)
        if fm < 0.5: lo, flo = m, fm
        else: hi, fhi = m, fm
    # linear interpolation on the final bracket
    if fhi == flo: return hi
    return lo + (0.5 - flo) / (fhi - flo) * (hi - lo)
fams = []
for k in (8, 12, 16, 20, 24, 32):
    fams.append((f'id_{k}', hybrid(k, 0)))
    for r in sorted({1, 2, k // 4, k // 2 - 1} if k>=12 else {1,2}):
        if 1 <= r <= k // 2: fams.append((f'H{k}_r{r}', hybrid(k, r)))
    fams.append((f'(21)^{k//2}', layered21(k)))
print('| pattern | k | blocks | N_pi (Pr=1/2) | N_pi/(k^2/4) | N_pi/N_id | sqrt(N_pi)-k/2 |'); print('|---|---|---|---|---|---|---|')
Nid = {}
for name, pi in fams:
    k = len(pi); Nh = find_half(pi)
    if name.startswith('id_'): Nid[k] = Nh
    nblk = sum(1 for i in range(k) if max(pi[:i+1]) == i + 1)
    print(f'| {name} | {k} | {nblk} | {Nh:.1f} | {Nh/(k*k/4):.3f} | {Nh/Nid[k]:.3f} | {math.sqrt(Nh)-k/2:.2f} |   <!-- {" ".join(map(str,pi))} -->', flush=True)
