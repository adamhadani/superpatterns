# Asymptotic rate of the slot-refined bound (Theorem C).  Continuum limit k->inf:
#  x=e^{-theta/k}, theta = tau e^2/lambda; even widths b = (k/theta) B, B~Gamma(2);
#  m(b)/k ~ (b/k)(1-e^{-tau k/b});  selection: b >= beta k  <=>  B >= theta*beta.
#  rate(pat/k!) <= P0 + max(Rgood, Rbad),
#   P0    = tau-1-log tau+log lambda
#   Rgood = max_s [ -ctil s^2/2 + (1/2) log( P(B<theta beta) + e^s (1+eps) E[(1-e^{-tau theta/B}); B>=theta beta] ) ]
#           ctil = (1+eps) beta (1-e^{-tau/beta})     (from the "+j-1" slot cost, r^2/(2 c_min) via duality)
#   Rbad  = -beta (1-e^{-tau/beta}) h(eps),  h(eps)=(1+eps)log(1+eps)-eps
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, minimize
def h(e): return (1+e)*np.log(1+e)-e
def rate(lam,tau,beta,eps):
    th=tau*np.e**2/lam; a=th*beta
    Pbelow=1-np.exp(-a)*(1+a)
    Eg=quad(lambda B:B*np.exp(-B)*(1-np.exp(-tau*th/B)),a,np.inf,limit=200)[0]*(1+eps)
    ct=(1+eps)*beta*(1-np.exp(-tau/beta))
    f=lambda s: ct*s*s/2-0.5*np.log(Pbelow+np.exp(s)*Eg)
    s0=minimize_scalar(f,bounds=(0,5),method='bounded').x
    Rgood=-f(s0)
    Rbad=-beta*(1-np.exp(-tau/beta))*h(eps)
    P0=tau-1-np.log(tau)+np.log(lam)
    return P0+max(Rgood,Rbad), P0+Rgood, P0+Rbad, s0
def best(lam):
    bestv=(9,None)
    for beta in [0.15,0.2,0.25,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.3]:
        for eps in [0.03,0.05,0.08,0.1,0.15,0.2,0.3]:
            for tau in [0.9,0.95,0.97,1.0,1.03,1.05,1.1]:
                v=rate(lam,tau,beta,eps)
                if v[0]<bestv[0]: bestv=(v[0],(tau,beta,eps,v))
    # local refine
    t,b,e,_=bestv[1]
    res=minimize(lambda p:rate(lam,*p)[0],[t,b,e],method='Nelder-Mead',options={'xatol':1e-5,'fatol':1e-9})
    return res.fun,res.x,rate(lam,*res.x)
for lam in [1.0,1.0003125,1.001,1.002,1.003,1.004,1.005]:
    v,p,full=best(lam)
    print(f"lambda={lam:.5f}: rate={v:+.6f}  tau={p[0]:.4f} beta={p[1]:.4f} eps={p[2]:.4f}  (good={full[1]:+.6f}, bad={full[2]:+.6f}, s={full[3]:.3f})",flush=True)
# bisection for lambda_C
lo,hi=1.0,1.01
for _ in range(25):
    mid=(lo+hi)/2
    if best(mid)[0]<0: lo=mid
    else: hi=mid
print("lambda_C =",lo, best(lo)[1])
