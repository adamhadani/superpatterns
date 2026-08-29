# Monte Carlo of the RESERVE corner rule in a strip of h rows (scaled height h):
# the m-th point (m=1..h) searches {u>0, 0<v<rho_eff}, rho_eff = rho - beta*(h-m), minimising u + lam*v;
# rho is the remaining height. Outputs E[total x]/h and the Chernoff exponent proxy. Independent of gg.c.
import numpy as np, math, sys
rng=np.random.default_rng(11)
def strip_total(C,h,beta,lam,n=300000):
    rho=np.full(n,float(h)); T=np.zeros(n)
    for m in range(1,h+1):
        re=rho-beta*(h-m)           # effective height (>= beta when m<h ... >= beta for the last as well)
        E=rng.exponential(size=n)/C # A(t)=E ; A(t)=t^2/(2 lam) for t<=lam*re, else re*t - lam*re^2/2
        t=np.where(E<=lam*re**2/2, np.sqrt(2*lam*E), (E+lam*re**2/2)/re)
        v=rng.random(n)*np.minimum(re,t/lam); u=t-lam*v
        T+=u; rho=rho-v
    return T
# run-length distribution of the non-overlapping monotone segmentation of a random permutation (k=100)
def runs(pinv):
    k=len(pinv); v=0; out=[]
    while v<k:
        s=v; e=v; d=0
        while e+1<k:
            dd=1 if pinv[e+1]>pinv[e] else -1
            if d==0: d=dd
            if dd!=d: break
            e+=1
        out.append(e-s+1); v=e+1
    return out
from collections import Counter
cnt=Counter()
for _ in range(3000): cnt.update(runs(rng.permutation(100)))
tot=sum(h*c for h,c in cnt.items())
freq={h:h*c/tot for h,c in cnt.items()}   # fraction of VALUES lying in runs of length h
print("value-fraction by run length:",{h:round(f,3) for h,f in sorted(freq.items())})
best=None
for C in [0.8,0.85,0.9,0.95,1.0]:
    for beta in [0.5,0.7,0.85,1.0]:
        for lam in [0.5,0.75,1.0,1.5]:
            means={h:strip_total(C,h,beta,lam,100000).mean()/h for h in range(1,8)}
            pred=sum(f*means[h] for h,f in freq.items() if h<=7)+sum(f for h,f in freq.items() if h>7)*means[7]
            print("C=%.2f beta=%.2f lam=%.2f  E[T_h]/h: %s  random-pi mean/value=%.4f"%(C,beta,lam," ".join("%.3f"%means[h] for h in range(1,8)),pred))
            if best is None or pred<best[0]: best=(pred,C,beta,lam)
    print()
print("best",best)
