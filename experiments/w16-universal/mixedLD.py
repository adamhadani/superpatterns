# Identity, mixed canonical rule: odd positions "leftmost" (x-strip empty), even positions "lowest" (y-strip empty).
# The minimiser of sum_{odd} x_r + sum_{even} y_r has all these strips empty; areas: odd r: g_r(h_{r-1}+h_r),
# even r: h_{r-1}(g_r+g_{r+1}); regions disjoint for the identity (y-strip of even r is in band r-1, x-strips of r-1,r+1
# in bands r-2..r+1 -> overlap!  x-strip of r+1 = col r+1 x bands r, r+1: band r-1 not included; x-strip of r-1 = col r-1
# x bands r-2, r-1; y-strip cols r, r+1 -> disjoint columns.  OK disjoint.)
# Integrating g: odd r -> 1/(s+h_{r-2}+h_{r-1}+h_r) (g_r also in y-strip of r-1), even r -> 1/(s+h_{r-1}).
# Two-step transfer on pairs (h_{2j-3},h_{2j-2}) -> (h_{2j-1},h_{2j}).
import numpy as np, math, sys
from pairs import grid
n=int(sys.argv[1])
x,w=grid(14.0,n)
def rho2(s,t):
    A=x[:,None,None,None]; B=x[None,:,None,None]; C=x[None,None,:,None]; D=x[None,None,None,:]
    K=np.exp(-t*(C+D))/((s+A+B+C)*(s+C))*(w[None,None,:,None]*w[None,None,None,:])
    K=K.reshape(n*n,n*n); f=np.ones(n*n); lam=0
    for it in range(5000):
        f2=K@f; l2=f2.max(); f=f2/l2
        if abs(l2-lam)<1e-12: break
        lam=l2
    return l2
# comparison: all-leftmost on same grid (pairs kernel level 1)
import pairs
for s,t in [(1.5,1.5),(1.4,1.5),(1.5,1.4),(1.3,1.6),(1.6,1.3),(1.2,1.7)]:
    r2=rho2(s,t); k_mixed=(s+t)/(-0.5*math.log(r2))
    r1=pairs.rho_pairs(pairs.ident_level1(s,t),s,t,n=n); k1=(s+t)/(-math.log(r1))
    print("n=%d s=%.2f t=%.2f  all-leftmost kappa=%.5f   mixed L/D kappa=%.5f"%(n,s,t,k1,k_mixed)); sys.stdout.flush()
