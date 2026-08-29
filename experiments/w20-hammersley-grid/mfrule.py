# mfrule.py — Monte Carlo of the mean-field rule (proof.md §4) for h=2 on the real FIXED model (no artificial
import sys, os; sys.path=[p for p in sys.path if p not in ("", os.getcwd(), os.path.dirname(os.path.abspath(__file__)))]
# fill, no window): strips = independent Poisson(C) on [0,k]x[0,2); round 1: min u + 1/(C(2-y)); round 2: min u.
# Prints success probability vs r at given C.  usage: python3 mfrule.py C r reps
import numpy as np, sys
C=float(sys.argv[1]); r=int(sys.argv[2]); reps=int(sys.argv[3]); h=2; k=r*h
rng=np.random.default_rng(1)
succ=0
for rep in range(reps):
    strips=[]
    for s in range(r):
        n=rng.poisson(C*k*h); xs=np.sort(rng.random(n)*k); ys=rng.random(n)*h
        strips.append((xs,ys))
    a=0.0; lev=np.zeros(r); ok=True
    for t in range(k):
        s=t%r; m=t//r; xs,ys=strips[s]
        i=np.searchsorted(xs,a,side='right'); xx=xs[i:]-a; yy=ys[i:]
        mask=yy>lev[s]
        if not mask.any(): ok=False; break
        xx=xx[mask]; yy=yy[mask]
        val = xx + (1.0/(C*(h-yy)) if m==0 else 0.0)
        j=np.argmin(val); a+=xx[j]; lev[s]=yy[j]
        if a>k: ok=False; break
    succ+=ok
print(f"mfrule h=2 C={C} r={r} reps={reps} success={succ/reps:.3f}")
