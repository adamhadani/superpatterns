# Deterministic quadrature for the reserve corner rule in a strip of h=2 rows (scaled height 2):
# step 1: region {u>0, 0<v<re}, re = 2-beta, score u + lam*v; step 2: leftmost in height 2-V1 (mean 1/(C(2-V1))).
# E X | re = int_0^inf C e^{-C A(t)} (s t - lam s^2/2) dt, s = min(re, t/lam), A(t) = int_0^t s(t')dt'.
# E[g(2-V1)] = int_0^inf C e^{-C A(t)} int_0^s g(2-v) dv dt.
import numpy as np, math
def EX_and_EG(C,re,lam,g,n=200000,tmax=60.0):
    t=np.linspace(1e-9,tmax,n); dt=t[1]-t[0]
    if lam>0:
        s=np.minimum(re,t/lam); A=np.where(t<=lam*re, t*t/(2*lam), re*t-lam*re*re/2)
    else:
        s=np.full_like(t,re); A=re*t
    w=C*np.exp(-C*A)
    EX=np.sum(w*(s*t-lam*s*s/2))*dt
    # inner integral of g(2-v) over v in (0,s): g(rho)=1/(C rho): int_0^s dv/(C(2-v)) = (1/C) ln(2/(2-s))
    EG=np.sum(w*g(s))*dt
    return EX,EG
def ET2(C,beta,lam):
    re=2-beta
    EX1,EG=EX_and_EG(C,re,lam,lambda s: np.log(2/(2-s))/C)
    return EX1+EG
best={}
for C in [0.7,0.75,0.78,0.8,0.82,0.85,0.9,1.0]:
    b=min(((ET2(C,beta,lam)/2,beta,lam) for beta in np.arange(0.0,1.01,0.1) for lam in np.arange(0.0,2.01,0.1)))
    best[C]=b; print("C=%.2f  min E[T2]/2 = %.4f at beta=%.1f lam=%.1f   (beta=0.7,lam=0.75: %.4f; beta=1,lam=1: %.4f)"%(C,b[0],b[1],b[2],ET2(C,0.7,0.75)/2,ET2(C,1,1)/2))
# root C_2: min E[T2]/2 = 1
lo,hi=0.5,1.0
for _ in range(30):
    m=(lo+hi)/2; v=min(ET2(m,beta,lam)/2 for beta in np.arange(0.0,1.01,0.05) for lam in np.arange(0.0,2.01,0.05))
    if v<1: hi=m
    else: lo=m
print("C_univ(h=2) = %.4f"%((lo+hi)/2))
# MC cross-check of the quadrature at C=0.8, beta=0.7, lam=0.75
rng=np.random.default_rng(3); n=2000000; C=0.8; beta=0.7; lam=0.75; re=2-beta
E=rng.exponential(size=n)/C; t=np.where(E<=lam*re**2/2, np.sqrt(2*lam*E), (E+lam*re**2/2)/re)
v=rng.random(n)*np.minimum(re,t/lam); u=t-lam*v; x2=rng.exponential(size=n)/(C*(2-v))
print("MC E[T2]/2 at C=0.8,beta=0.7,lam=0.75: %.4f  quadrature: %.4f"%(((u+x2).mean())/2, ET2(0.8,0.7,0.75)/2))
