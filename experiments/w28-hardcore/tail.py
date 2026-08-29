#!/usr/bin/env python3
"""W28: tail of M | M>0 and Lambda_pi = E[M | pi missing] statistics at n ~ t(k), k = 6..9 (M lists only)."""
import math, numpy as np
from hardcore import load
for k, n in [(6,28),(7,37),(8,48),(9,60)]:
    M, sets = load(k, n); K = math.factorial(k); S = len(M)
    pos = M[M > 0]; mu = M.mean(); P = len(pos)/S; R = pos.mean(); EM2 = np.mean(M.astype(float)**2)
    cnt = np.zeros(K); csum = np.zeros(K)
    for m, s in zip(M, sets):
        if m > 0: cnt[s] += 1; csum[s] += m
    lam = csum/np.maximum(cnt,1); ok = cnt >= 20
    q = lambda x: np.mean(pos >= x)
    print(f'k={k} n={n} S={S} P(M>0)={P:.3f} mu={mu:.3g} R={R:.3g} lnR={math.log(R):.2f} EM2/mu={EM2/mu:.3g} ln={math.log(EM2/mu):.2f} '
          f'maxΛ(≥20ev)={lam[ok].max() if ok.any() else float("nan"):.3g} #ok={ok.sum()} medΛ={np.median(lam[ok]) if ok.any() else float("nan"):.3g} '
          f'| tail P(M≥m|M>0): m=2:{q(2):.3f} 4:{q(4):.3f} 8:{q(8):.3f} 16:{q(16):.3f} 32:{q(32):.3f} 64:{q(64):.3f} 128:{q(128):.3f} 256:{q(256):.3f} 512:{q(512):.3f} 1024:{q(1024):.3f} 2048:{q(2048):.4f} '
          f'| share of ΣM from M≥64: {pos[pos>=64].sum()/pos.sum():.3f}, from M≥256: {pos[pos>=256].sum()/pos.sum():.3f}; max M {pos.max()}; ln(k!)={math.log(K):.1f}')
