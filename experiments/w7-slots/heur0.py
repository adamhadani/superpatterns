# eps=0, no Bad term (pure heuristic ceiling of the same rate computation)
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, minimize
def rate(lam,tau,beta):
    th=tau*np.e**2/lam; a=th*beta
    Pbelow=1-np.exp(-a)*(1+a)
    Eg=quad(lambda B:B*np.exp(-B)*(1-np.exp(-tau*th/B)),a,np.inf,limit=200)[0]
    ct=beta*(1-np.exp(-tau/beta))
    f=lambda s: ct*s*s/2-0.5*np.log(Pbelow+np.exp(s)*Eg)
    s0=minimize_scalar(f,bounds=(0,5),method='bounded').x
    return tau-1-np.log(tau)+np.log(lam)-f(s0)
def best(lam):
    return minimize(lambda p:rate(lam,*p),[0.98,0.5],method='Nelder-Mead',options={'xatol':1e-5,'fatol':1e-9}).fun
lo,hi=1.0,1.05
for _ in range(20):
    mid=(lo+hi)/2
    if best(mid)<0: lo=mid
    else: hi=mid
print("heuristic (eps=0, no Bad) lambda =",lo)
# monotonicity of m(b) on [beta, n/2] at k=30001, lam=1.004
from math import exp,log
k=30001; lam=1.004; n=int(lam*k*k/np.e**2); th=0.9774*np.e**2/lam; x=exp(-th/k)
b=np.arange(3,n//2+1,dtype=float); m=(b-2)*(1-np.exp((n-b-1)/(b-2)*log(x)))
print("m increasing on [3,n/2]:", bool((np.diff(m)>=0).all()), " m(beta k)/k=",m[int(0.5936*k)-3]/k, " min m/k=",m.min()/k)
