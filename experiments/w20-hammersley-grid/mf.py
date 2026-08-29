# mf.py — mean-field Bellman values (proof.md Prop 4.3) for the FIXED tilted grid at fixed h, r -> infinity.
# Scaled strip: Poisson intensity C on (0,inf) x (0,h).  V_0 = 0;
#   V_m(v) = E[ min over points (u,y), y in (v,h), of u + V_{m-1}(y) ]  (fresh half-strip at each visit)
#          = int_0^inf exp(-C*A(s)) ds,   A(s) = int_v^h (s - V_{m-1}(y))_+ dy.
# Discretisation: V_{m-1} is piecewise constant on n cells of height dy = h/n (value at cell midpoint);
# V_m at a midpoint v_j uses only the cells strictly above (conservative: the true value is smaller),
# V_m(0) uses all cells.  The s-integral is exact for the piecewise-constant profile (piecewise linear A).
# C_mf(h) = root of V_h(0;C) = h.  usage: python3 mf.py [n] [hmax]
import numpy as np, sys, math
def Emin(g, dy, C):
    # E[min_{points} u + g(y)] for a Poisson process of intensity C on (0,inf) x (cells with values g)
    g=np.asarray(g,dtype=float); g=np.sort(g[np.isfinite(g)]); J=len(g)
    if J==0: return math.inf
    cs=np.cumsum(g); tot=g[0]
    for j in range(1,J+1):            # segment s in [g_(j), g_(j+1)) with j cells active: A(s)=dy*(j*s - cs[j-1])
        a=-dy*cs[j-1]; b=dy*j; lo=g[j-1]; hi=g[j] if j<J else math.inf
        # int_lo^hi exp(-C(a+b s)) ds = exp(-C(a+b lo))*(1-exp(-C b (hi-lo)))/(C b)
        e0=math.exp(-C*(a+b*lo)); 
        tot+= e0*(1-(math.exp(-C*b*(hi-lo)) if hi<math.inf else 0.0))/(C*b)
    return tot
def bellman(C,h,n=400):
    dy=h/n
    V=np.zeros(n)                     # V_0 on midpoints
    for m in range(1,h):
        Vn=np.empty(n)
        for j in range(n):
            Vn[j]=Emin(V[j+1:],dy,C) if j<n-1 else math.inf
        V=Vn
    return Emin(V,dy,C)               # V_h(0)  (last round from level 0, all cells)
def Cmf(h,n=400):
    lo,hi=0.3,1.2
    for _ in range(25):
        C=(lo+hi)/2
        if bellman(C,h,n)<h: hi=C
        else: lo=C
    return (lo+hi)/2
if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 400; hmax=int(sys.argv[2]) if len(sys.argv)>2 else 12
    print("n=",n,"pi/8=",round(math.pi/8,4))
    for h in list(range(1,hmax+1)):
        print(h, round(Cmf(h,n),4), flush=True)
