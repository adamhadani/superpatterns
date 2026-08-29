# W25: Theorem C rate with (i) width-dependent eps(b) (flat bad exponent, as in w7-slots/rate2.py) and
# (ii) the exact Bernoulli (Cramer) tail exp(-(b-2) D((1+eps)p_b || p_b)), p_b = 1 - x^{(n-b-1)/(b-2)},
# in place of the Poisson-type exp(-m(b) h(eps)).  mode='poisson' reproduces rate2.py (1.00501).
# Limit variables: B = theta*b/k ~ Gamma(2,1); beta' = B/theta; p(B) = 1 - exp(-tau*theta/B); m(b)/k = beta' p.
import numpy as np, sys
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, minimize, brentq
def h(e): return (1+e)*np.log(1+e)-e
def KL(a,p): return a*np.log(a/p)+(1-a)*np.log((1-a)/(1-p))
def rate(lam,tau,beta,R,mode):
    th=tau*np.e**2/lam; a=th*beta
    p=lambda B: 1-np.exp(-tau*th/B)
    def eps_of(B):
        bp=B/th; pB=p(B)
        if mode=='poisson':
            return brentq(lambda e: bp*pB*h(e)-R,1e-12,50)
        emax=1/pB-1-1e-12
        if bp*KL(1-1e-12,pB)<R: return emax          # tail identically zero; no gain
        return brentq(lambda e: bp*KL((1+e)*pB,pB)-R,1e-12,emax)
    Pbelow=1-np.exp(-a)*(1+a)
    Eg=quad(lambda B:B*np.exp(-B)*p(B)*(1+eps_of(B)),a,np.inf,limit=200)[0]
    grid=np.linspace(a,a+40,400)
    ct=min((1+eps_of(B))*(B/th)*p(B) for B in grid)
    f=lambda s: ct*s*s/2-0.5*np.log(Pbelow+np.exp(s)*Eg)
    s0=minimize_scalar(f,bounds=(0,5),method='bounded').x
    Rgood=-f(s0); Rbad=-R
    P0=tau-1-np.log(tau)+np.log(lam)
    return P0+max(Rgood,Rbad),P0+Rgood,P0+Rbad,s0,ct
def best(lam,mode,x0):
    res=minimize(lambda q:rate(lam,*q,mode)[0],x0,method='Nelder-Mead',options={'xatol':1e-6,'fatol':1e-10,'maxiter':600})
    return res.fun,res.x
for mode,x0 in [('poisson',[0.977,0.59,0.005]),('bernoulli',[0.966,0.53,0.008])]:
    print("mode",mode,flush=True)
    x=x0
    for lam in [1.0,1.005,1.008,1.010]:
        v,x=best(lam,mode,x)
        full=rate(lam,*x,mode)
        print(f"  lambda={lam:.4f}: rate={v:+.6f} tau={x[0]:.4f} beta={x[1]:.4f} R={x[2]:.5f} (good={full[1]:+.6f}, bad={full[2]:+.6f}, s={full[3]:.3f}, cbar={full[4]:.4f})",flush=True)
    lo,hi=1.0,1.02
    for _ in range(18):
        mid=(lo+hi)/2
        v,xm=best(mid,mode,x)
        if v<0: lo=mid; x=xm
        else: hi=mid
    print("  lambda root =",lo,x,flush=True)
