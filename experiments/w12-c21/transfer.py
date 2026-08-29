# (C) full canonical regions. Scaled units (N=1, s=t=sigma).
# T(d,d') = e^{s^2+s d} E1(s(s+d+d')) / (s+d).   rate = 2s + c log rho(T);  c_UB = min_s 2s/log(1/rho).
import numpy as np, math
from scipy.special import exp1, expi
from scipy.integrate import quad
def T(s,d,dp):
    x=s*(s+d+dp); return np.exp(s*s+s*d + x)*exp1(x)/(s+d)   # e^{x}E1(x) stable
def T2(s,d,dp):   # same, log-stable via exp(x)*exp1(x)
    x=s*(s+d+dp); return np.exp(-s*dp)*np.exp(x)*exp1(x)/(s+d)
def rho_numeric(s, M=15.0, n=1500):
    h=M/n; xs=np.linspace(0,M,n+1); w=np.full(n+1,h); w[0]=w[-1]=h/2
    K=T2(s,xs[:,None],xs[None,:])*w[None,:]
    v=np.ones(n+1)
    for it in range(2000):
        w2=K@v; lam=w2.max(); v=w2/lam
    return lam, xs, v
if __name__=="__main__":
    for s in (1.6,1.8,1.9,2.0,2.1,2.2):
        lam,xs,v=rho_numeric(s)
        print("s=%.2f  rho_num=%.6f  c=%.5f   eigvec(0)/eigvec(1)/eigvec(3)=%.3f %.3f %.3f"%(s,lam,2*s/(-math.log(lam)),v[0],v[100],v[300]))
