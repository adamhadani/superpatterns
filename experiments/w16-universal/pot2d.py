# Route (a): canonical copies w.r.t. the potential Psi(p) = x + lam*y, for the IDENTITY pattern.
# Scaled units N = 1 (gaps g_r, h_m of order 1).  Empty region of p_r (box (x_{r-1},x_{r+1}) x (y_{r-1},y_{r+1})):
#   {q in box : (x_q - x_r) + lam (y_q - y_r) < 0}, area = g_r h_{r-1} + L(g_r, h_r) + R(g_{r+1}, h_{r-1}),
#   L(g,h) = int_0^g min(t/lam, h) dt,  R(g',h) = int_0^{g'} max(0, h - t/lam) dt   (L + R = g h).
# Regions of different r are disjoint (E_r^right lies below y_r, E_{r+1}^left above y_r).  Chernoff with e^{-s g - t h}
# leaves the 2-D transfer kernel on states (g_r, h_{r-1}):
#   K((g,h),(g',h')) = exp(-s g' - t h') exp(-[g h + L(g,h') + R(g',h)]),   E_k <= C N^{-1/2} e^{(s+t) sqrt N} rho(K)^k,
# so kappa(lam) = min_{s,t} (s+t)/log(1/rho).   lam -> 0 must reproduce W12 (rho(1.5) = 0.26806).
import numpy as np, sys, math
def Lf(g,h,lam):  # int_0^g min(t/lam,h) dt
    a=np.minimum(g,lam*h); return a*a/(2*lam)+h*np.maximum(g-a,0)
def Rf(g,h,lam):  # int_0^g max(0,h-t/lam) dt
    a=np.minimum(g,lam*h); return h*a-a*a/(2*lam)
def rho(lam,s,t,M=10.0,n=48,iters=4000):
    # composite grid: denser near 0 (the mass sits at small gaps)
    x=np.concatenate([np.linspace(0,2,n//2,endpoint=False),np.linspace(2,M,n-n//2)])
    w=np.gradient(x); w[0]/=2; w[-1]/=2   # trapezoid-like weights
    # simpler: use midpoint weights
    w=np.empty_like(x); w[1:-1]=(x[2:]-x[:-2])/2; w[0]=(x[1]-x[0])/2; w[-1]=(x[-1]-x[-2])/2
    G,H=np.meshgrid(x,x,indexing="ij"); g=G.ravel(); h=H.ravel(); W=(w[:,None]*w[None,:]).ravel()
    m=len(g)
    # kernel matrix K[i,j] i=(g,h), j=(g',h')
    gp=g[None,:]; hp=h[None,:]; gg=g[:,None]; hh=h[:,None]
    K=np.exp(-s*gp-t*hp-(gg*hh+Lf(gg,hp,lam)+Rf(gp,hh,lam)))*W[None,:]
    v=np.ones(m); lamb=0
    for it in range(iters):
        v2=K@v; l2=v2.max(); v=v2/l2
        if abs(l2-lamb)<1e-12: break
        lamb=l2
    return l2
if __name__=="__main__":
    lam=float(sys.argv[1]) if len(sys.argv)>1 else 1.0
    n=int(sys.argv[2]) if len(sys.argv)>2 else 48
    best=(9,None)
    for s in np.arange(1.0,2.61,0.2):
        for t in np.arange(1.0,2.61,0.2):
            if abs(s-t)>0.61: continue
            r=rho(lam,s,t,n=n); kap=(s+t)/(-math.log(r))
            if kap<best[0]: best=(kap,(s,t,r))
            print("lam=%.3f s=%.2f t=%.2f rho=%.6f kappa=%.5f"%(lam,s,t,r,kap)); sys.stdout.flush()
    print("BEST",best)
