import numpy as np, math
from certify import Tu
from scipy.integrate import quad
from scipy.optimize import minimize
# test function phi(u) = eps + (1+u/a)^(-kappa); certificate: sup_u (Tu phi)(u)/phi(u)
def Tphi(s,u,phi): return quad(lambda v: Tu(s,u,v)*phi(v),0,np.inf,limit=500,epsabs=1e-14,epsrel=1e-12)[0]
grid=np.concatenate([np.linspace(0,10,401),np.linspace(10,60,101),[80,100,150,200,400,800,1600]])
def sup_ratio(s,a,kap,eps,grid=grid):
    phi=lambda v: eps+(1+v/a)**(-kap)
    return max(Tphi(s,u,phi)/phi(u) for u in grid)
s=1.5
r0=None
for a in (1.0,1.5,2.0,2.5,3.0):
    for kap in (0.8,1.0,1.2,1.4):
        r=sup_ratio(s,a,kap,1e-3,grid[::8]); print("a=%.1f kap=%.1f sup=%.6f"%(a,kap,r))
