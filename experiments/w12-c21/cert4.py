import numpy as np, math
from certify import Tu
from scipy.integrate import quad
from scipy.optimize import minimize
def Tphi(s,u,phi): return quad(lambda v: Tu(s,u,v)*phi(v),0,np.inf,limit=800,epsabs=1e-15,epsrel=1e-13)[0]
coarse=np.concatenate([np.linspace(0,8,81),np.linspace(8,40,33),[60,100,200,500,1000,3000]])
fine=np.concatenate([np.linspace(0,12,1201),np.linspace(12,80,341),[100,150,200,300,500,1000,2000,5000,20000]])
def sup_ratio(s,a,kap,eps,grid):
    phi=lambda v: eps+(1+v/a)**(-kap); return max((Tphi(s,u,phi)/phi(u),u) for u in grid)
res=minimize(lambda z: sup_ratio(1.5,z[0],z[1],1e-3,coarse)[0], x0=[1.7,0.9], method='Nelder-Mead',options={'xatol':1e-3,'fatol':1e-6,'maxiter':60})
a,kap=res.x; print("opt a=%.4f kap=%.4f coarse sup=%.7f"%(a,kap,res.fun))
for s in (1.45,1.5,1.55,1.6):
    r,u=sup_ratio(s,a,kap,1e-3,fine); print("s=%.2f  certified rho_bar=%.7f at u=%.3f  -> kappa* <= %.5f"%(s,r,u,2*s/(-math.log(r))))
