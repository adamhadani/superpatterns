# Independent checks of the constants in proof.md (numpy only).
import numpy as np, math
rng=np.random.default_rng(5)
def sampleUV(C,n):
    T=np.sqrt(2*rng.exponential(size=n)/C); W=rng.random(n); return T*W, T*(1-W)
def cC(C,n=400000):
    U,_=sampleUV(C,n); best=0
    for th in np.linspace(0.01,20,2000):
        v=th-np.log(np.mean(np.exp(th*U)))
        if v>best: best=v
    return best
print("E U at C=1:",sampleUV(1,400000)[0].mean(),"theory",math.sqrt(math.pi/8))
for C in [0.5,0.6,0.8,1,1.5,2,4]: print("c(%g)=%.3f"%(C,cC(C)))
# threshold C*(alpha): alpha*sqrt(pi/(8C))+(1-alpha)/C=1
def brentq(f,a,b):
    for _ in range(100):
        m=(a+b)/2
        if f(a)*f(m)<=0: b=m
        else: a=m
    return (a+b)/2
for al in [0,0.25,0.5,0.75,1]: print("alpha=%.2f C*=%.4f"%(al,brentq(lambda C: al*math.sqrt(math.pi/(8*C))+(1-al)/C-1,0.3,1.5)))
# Cor 2.2 arithmetic: k! e^{-k(C-1-ln C)} at C=(1+eps)(ln k+lnln k)
for k in [100,1000,10**4,10**6]:
    L=math.log(k)+math.log(math.log(k)); C=1.1*L
    print("k=%d C=%.2f log(k! e^{-k(C-1-lnC)})=%.1f"%(k,C,math.lgamma(k+1)-k*(C-1-math.log(C))))
# restricted corner chain in a strip of h rows: E[total x]/h and the phase-1 corner rule comparison
def strip_total(C,h,n=200000,variant=0):
    rho=np.full(n,float(h)); T=np.zeros(n)
    for m in range(h):
        if variant and m==h-1:
            T+=rng.exponential(size=n)/(C*rho); break
        # sample (u,v) with density C exp(-C A_rho(u+v)) on u>0, 0<v<rho, A_rho(t)=t^2/2-((t-rho)_+)^2/2
        # method: sample t=u+v from density C*(dA/dt) exp(-C A(t)) via inversion on A, then v uniform on (0,min(t,rho))
        E=rng.exponential(size=n)/C   # A(t)=E
        # invert A: if E<=rho^2/2: t=sqrt(2E); else A(t)=rho t - rho^2/2 -> t=(E+rho^2/2)/rho
        t=np.where(E<=rho**2/2, np.sqrt(2*E), (E+rho**2/2)/rho)
        v=rng.random(n)*np.minimum(t,rho); u=t-v
        T+=u; rho=rho-v
    return T.mean()/h
for C in [0.7,0.8,1.0]:
    print("C=%g rows(Exp) 1/C=%.3f"%(C,1/C), " restricted corner E[T_h]/h:", ["h=%d: %.4f/%.4f"%(h,strip_total(C,h),strip_total(C,h,variant=1)) for h in [1,2,3,4,6]])
# run-length distribution of maximal monotone runs (non-overlapping segmentation) of a random permutation
def runs(pinv):
    k=len(pinv); v=0; out=[]
    while v<k:
        s=v; e=v; d=0
        while e+1<k:
            dd=1 if pinv[e+1]>pinv[e] else -1
            if d==0: d=dd
            if dd!=d: break
            e+=1
        out.append(e-s+1); v=e+1
    return out
from collections import Counter
cnt=Counter()
for _ in range(2000):
    p=rng.permutation(100); cnt.update(runs(p))
tot=sum(cnt.values()); print("run-length distribution (k=100):",{h:round(c/tot,3) for h,c in sorted(cnt.items())}, "mean length",100*2000/tot)
# predicted mean X per value for random pi at C=1 with L=2 (all runs corner, incl. length-1 tail as row)
for C in [0.7,0.8,1.0]:
    for var in [0,1]:
        pred=sum(c*h*strip_total(C,h,50000,var) for h,c in cnt.items() if h>=1)/ (100*2000)
        print("C=%g var=%d predicted meanX/value=%.4f"%(C,var,pred))
