# Spectral radii + Collatz-Wielandt certificates.  Scaled units N=1, s=t=sigma.
# Universal (leftmost-canonical copy of ANY pattern):  Tu(h,h') = e^{-s h'}/(s+h+h')
# 21-specific (a leftmost, b lowest):                 T21(d,d') = e^{-s d'} e^{x}E1(x)/(s+d), x=s(s+d+d')
import numpy as np, math, sys
from scipy.special import exp1
from scipy.integrate import quad
def Tu(s,h,hp): return np.exp(-s*hp)/(s+h+hp)
def T21(s,d,dp):
    x=s*(s+d+dp); return np.exp(-s*dp)*np.exp(x)*exp1(x)/(s+d)
def rho(T,s,M=20.0,n=3000):
    h=M/n; xs=np.linspace(0,M,n+1); w=np.full(n+1,h); w[0]=w[-1]=h/2
    K=T(s,xs[:,None],xs[None,:])*w[None,:]; v=np.ones(n+1); lam=0
    for it in range(3000):
        w2=K@v; lam2=w2.max(); v=w2/lam2
        if abs(lam2-lam)<1e-13: break
        lam=lam2
    return lam2
def cw(T,s,phi,grid):
    # sup over grid of (T phi)(h)/phi(h) with adaptive quadrature
    best=0;arg=None
    for h in grid:
        val=quad(lambda hp: T(s,h,hp)*phi(hp),0,np.inf,limit=400,epsabs=1e-13,epsrel=1e-11)[0]/phi(h)
        if val>best: best,arg=val,h
    return best,arg
if __name__=="__main__":
    for name,T,srange in (("universal",Tu,np.arange(1.6,3.01,0.1)),("21",T21,np.arange(1.3,2.21,0.1))):
        print("==",name)
        for s in srange:
            r=rho(T,s); print("  s=%.2f rho=%.6f  c=%.5f"%(s,r,2*s/(-math.log(r))))
