# MC for strips of h=2,3 with the rule: step m<h: region height rho - beta*(h-m), score u+lam_m v; last step: leftmost.
import numpy as np, itertools
rng=np.random.default_rng(17)
def T(C,h,beta,lams,n=400000):
    rho=np.full(n,float(h)); tot=np.zeros(n)
    for m in range(1,h+1):
        if m==h: tot+=rng.exponential(size=n)/(C*rho); break
        re=rho-beta*(h-m); lam=lams[m-1]
        E=rng.exponential(size=n)/C
        t=np.where(E<=lam*re**2/2, np.sqrt(2*lam*E), (E+lam*re**2/2)/re)
        v=rng.random(n)*np.minimum(re,t/lam); u=t-lam*v; tot+=u; rho=rho-v
    return tot
for C in [0.76,0.8,0.85,0.9,1.0]:
    b2=min((T(C,2,b,[l],100000).mean()/2,b,l) for b in np.arange(0.2,0.81,0.1) for l in np.arange(0.7,1.51,0.1))
    b3=min((T(C,3,b,[l1,l2],60000).mean()/3,b,l1,l2) for b in np.arange(0.2,0.81,0.15) for l1 in np.arange(0.6,1.61,0.2) for l2 in np.arange(0.6,1.61,0.2))
    print("C=%.2f  h=2: E[T]/2=%.4f (beta=%.2f lam=%.2f)   h=3: E[T]/3=%.4f (beta=%.2f lams=%.2f,%.2f)"%(C,b2[0],b2[1],b2[2],b3[0],b3[1],b3[2],b3[3]))
# Chernoff exponents with fixed rule beta=0.4, lam=1.1 (h=2) / beta=0.35, lams=(1.0,1.0) (h=3)
print("Chernoff exponent eta(C) >= sup_theta min_h (theta - ln M_h(theta)/h):")
for C in [0.8,0.85,0.9,1.0,1.2]:
    T2=T(C,2,0.4,[1.1],400000); T3=T(C,3,0.35,[1.0,1.0],400000)
    best=0
    for th in np.arange(0.005,C*0.35,0.005):
        v=min(th-np.log(np.mean(np.exp(th*T2)))/2, th-np.log(np.mean(np.exp(th*T3)))/3)
        best=max(best,v)
    print("  C=%.2f  E[T2]/2=%.4f E[T3]/3=%.4f  eta>=%.4f   (rigid rows: C-1-lnC=%.4f)"%(C,T2.mean()/2,T3.mean()/3,best,C-1-np.log(C) if C>1 else 0))
