# Check: E#{leftmost-canonical copies of pi} in Pi_N equals N^k * int_{pattern pi} exp(-N sum |S_p|) (pattern-independent after Laplace bound;
# here we check the exact integral and the simulation for pi=12 and pi=21 at N=5).  Also check the two integrals are NOT equal
# before the Chernoff step (the pattern-independence is only of the bound), and the E1-based closed forms.
import numpy as np, math
rng=np.random.default_rng(1)
N=5; reps=200000
def sim(pattern):
    tot=0
    for _ in range(reps):
        n=rng.poisson(N); P=rng.random((n,2)); x=P[:,0]; y=P[:,1]
        for i in range(n):
            for j in range(n):
                if i==j or x[i]>=x[j]: continue
                if pattern=='12' and not y[i]<y[j]: continue
                if pattern=='21' and not y[i]>y[j]: continue
                # first point p=i, second q=j (x-order). regions: left-strip of p within its box, left-strip of q within its box
                if pattern=='12':
                    ok = not np.any((x<x[i])&(y<y[j])) and not np.any((x>x[i])&(x<x[j])&(y>y[i]))
                else:
                    ok = not np.any((x<x[i])&(y>y[j])) and not np.any((x>x[i])&(x<x[j])&(y<y[i]))
                tot+=ok
    return tot/reps
def integral(pattern,M=400000):
    P=rng.random((M,4)); xa,xb=np.sort(P[:,:2],axis=1).T; y1,y2=np.sort(P[:,2:],axis=1).T
    if pattern=='12': ya,yb=y1,y2; area=xa*yb+(xb-xa)*(1-ya)
    else: ya,yb=y2,y1; area=xa*(1-yb)+(xb-xa)*ya
    # ordered pairs: prob 1/2 * 1/2 for the x- and y-orders -> weight N^2 * (1/4)... integrate over unit square^2 with indicator = 1/4 of volume
    return N*N*np.mean(np.exp(-N*area))/4
for pat in ('12','21'):
    print(pat, "sim E#canonical = %.4f   integral = %.4f"%(sim(pat), integral(pat)))
