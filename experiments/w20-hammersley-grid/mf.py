# mf.py — mean-field Bellman values for the fixed-strip tilted grid at fixed h, r -> infinity.
# Scaled strip: Poisson intensity C on (0,inf) x (0,h).  W_0 = 0;
# W_m(v) = E[ min over points (u,y), y in (v,h), of u + W_{m-1}(y) ]   (fresh half-strip at each visit)
# Pr(min > s) = exp(-C*A(s)),  A(s) = int_v^h (s - W_{m-1}(y))_+ dy ;  W_m(v) = int_0^inf exp(-C A(s)) ds.
# C_mf(h) = the C with W_h(0) = h.  Also the triangle-rule (uncapped, W(y)=y) value for reference.
import numpy as np, sys
def bellman(C,h,n=400,smax=None):
    ys=np.linspace(0,h,n+1); dy=h/n
    W=np.zeros(n+1)  # W_0
    hist=[]
    for m in range(1,h+1):
        Wn=np.zeros(n+1)
        for i in range(n):          # level v = ys[i]; y ranges over (v,h)
            g=W[i+1:]               # W_{m-1} on grid points above v (use right endpoints: conservative)
            gmin=g.min()
            # s grid: from gmin to gmin + enough
            svals=np.linspace(gmin, gmin+ 60.0/(C*max(h-ys[i],dy)) , 3000)
            A=np.array([np.maximum(s-g,0).sum()*dy for s in svals])
            Wn[i]=gmin+np.trapezoid(np.exp(-C*A),svals)
        Wn[n]=np.inf
        W=Wn
    return W
def Cmf(h,n=200):
    lo,hi=0.2,1.5
    for _ in range(30):
        C=(lo+hi)/2
        if bellman(C,h,n)[0] < h: hi=C
        else: lo=C
    return (lo+hi)/2
if __name__=='__main__':
    for h in [1,2,3,4,5,6,8,10,12,16]:
        n=100 if h>=8 else 200
        print(h, round(Cmf(h,n),4), flush=True)
