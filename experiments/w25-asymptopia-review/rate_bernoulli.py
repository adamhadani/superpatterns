# W25: Theorem C rate with the Poisson-type Chernoff bound exp(-m(b) h(eps)) for the slot count
# replaced by the exact Bernoulli (Cramer) rate exp(-(b-2) D((1+eps) pbar || pbar)),
# pbar = 1 - x^{(n-b-1)/(b-2)} -> 1 - e^{-tau/beta} at b = beta*k.  (Spencer, Asymptopia, Ch. 8: "very large
# deviations: lambda constant, optimise the Laplace transform exactly".)  Everything else identical to
# experiments/w7-slots/rate.py (which reproduces lambda_C = 1.00483).
import numpy as np, sys
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, minimize
def h(e): return (1+e)*np.log(1+e)-e
def KL(a,p):
    if a>=1: return np.inf
    return a*np.log(a/p)+(1-a)*np.log((1-a)/(1-p))
def rate(lam,tau,beta,eps,mode):
    th=tau*np.e**2/lam; a=th*beta
    Pbelow=1-np.exp(-a)*(1+a)
    Eg=quad(lambda B:B*np.exp(-B)*(1-np.exp(-tau*th/B)),a,np.inf,limit=200)[0]*(1+eps)
    pbar=1-np.exp(-tau/beta)
    ct=(1+eps)*beta*pbar
    f=lambda s: ct*s*s/2-0.5*np.log(Pbelow+np.exp(s)*Eg)
    s0=minimize_scalar(f,bounds=(0,5),method='bounded').x
    Rgood=-f(s0)
    if mode=='poisson': Rbad=-beta*pbar*h(eps)
    else:               Rbad=-beta*KL((1+eps)*pbar,pbar)
    P0=tau-1-np.log(tau)+np.log(lam)
    return P0+max(Rgood,Rbad), P0+Rgood, P0+Rbad, s0
def best(lam,mode):
    bestv=(9,None)
    for beta in [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.5,2.0]:
        for eps in [0.01,0.02,0.03,0.05,0.08,0.1,0.15,0.2,0.3]:
            for tau in [0.9,0.95,0.97,1.0,1.03,1.05,1.1]:
                v=rate(lam,tau,beta,eps,mode)
                if v[0]<bestv[0]: bestv=(v[0],(tau,beta,eps,v))
    t,b,e,_=bestv[1]
    res=minimize(lambda p:rate(lam,*p,mode)[0],[t,b,e],method='Nelder-Mead',options={'xatol':1e-6,'fatol':1e-10})
    return res.fun,res.x,rate(lam,*res.x,mode)
for mode in ['poisson','bernoulli']:
    print("mode",mode)
    for lam in [1.0,1.004,1.006,1.008,1.010,1.012]:
        v,p,full=best(lam,mode)
        print(f"  lambda={lam:.4f}: rate={v:+.6f} tau={p[0]:.4f} beta={p[1]:.4f} eps={p[2]:.4f} (good={full[1]:+.6f}, bad={full[2]:+.6f}, s={full[3]:.3f})",flush=True)
    lo,hi=1.0,1.02
    for _ in range(22):
        mid=(lo+hi)/2
        if best(mid,mode)[0]<0: lo=mid
        else: hi=mid
    print("  lambda root =",lo, best(lo,mode)[1],flush=True)
