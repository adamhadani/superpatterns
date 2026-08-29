# Variant: width-dependent eps(b) chosen so that m(b) h(eps(b)) = m(beta k) h(eps0) for all selected b (flat Chernoff exponent).
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, minimize, brentq
def h(e): return (1+e)*np.log(1+e)-e
def rate(lam,tau,beta,eps0):
    th=tau*np.e**2/lam; a=th*beta
    mb=lambda B: (B/th)*(1-np.exp(-tau*th/B))      # m(b)/k as function of B=theta b/k
    m0=mb(a); H0=h(eps0)*m0
    def epsb(B):
        target=H0/mb(B)
        return brentq(lambda e:h(e)-target,1e-9,10)
    Pbelow=1-np.exp(-a)*(1+a)
    Eg=quad(lambda B:B*np.exp(-B)*(1-np.exp(-tau*th/B))*(1+epsb(B)),a,np.inf,limit=200)[0]
    ct=(1+eps0)*beta*(1-np.exp(-tau/beta))   # c_min: (1+eps(b))m(b) >= (1+eps0) m(beta k) since m increasing and h(eps)m const => (1+eps)m increasing? check
    f=lambda s: ct*s*s/2-0.5*np.log(Pbelow+np.exp(s)*Eg)
    s0=minimize_scalar(f,bounds=(0,5),method='bounded').x
    Rgood=-f(s0); Rbad=-H0
    P0=tau-1-np.log(tau)+np.log(lam)
    return P0+max(Rgood,Rbad),P0+Rgood,P0+Rbad
def best(lam):
    res=minimize(lambda p:rate(lam,*p)[0],[0.977,0.59,0.15],method='Nelder-Mead',options={'xatol':1e-5,'fatol':1e-9})
    return res.fun,res.x
lo,hi=1.0,1.02
for _ in range(20):
    mid=(lo+hi)/2
    if best(mid)[0]<0: lo=mid
    else: hi=mid
print("lambda_C' (eps(b) variant) =",lo,best(lo))
