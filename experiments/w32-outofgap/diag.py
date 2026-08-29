import sys, numpy as np
sys.argv=[sys.argv[0]]
from single_strip import load_V, run_one
k=int(sys.argv[1]) if len(sys.argv)>1 else 1024
k=1024; C=0.6
V=load_V(k); rng=np.random.default_rng(3)
r=run_one(k,1,C,V,rng)
D,U,T=r['D'],r['U'],r['T']
print("cost/k",r['cost'])
for lo in np.arange(0,1,0.1):
    sel=(T>=lo*k)&(T<(lo+0.1)*k)
    print("t/k in [%.1f,%.1f): cost share %.3f, mean u %.3f, median D/k %.4f, mean D/k %.4f, frac D<0.02k %.3f, cost frac D<0.02k %.3f"%(lo,lo+.1,U[sel].sum()/U.sum(),U[sel].mean(),np.median(D[sel])/k,D[sel].mean()/k,(D[sel]<0.02*k).mean(),U[sel][D[sel]<0.02*k].sum()/U[sel].sum()))
