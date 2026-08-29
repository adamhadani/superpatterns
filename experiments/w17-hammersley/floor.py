# Floor for any renewal rule: E[min over descent pairs (a,b) in the quadrant of x_b + y_a], unit Poisson.
import numpy as np
rng=np.random.default_rng(1); R=7.0; S=200000; tot=0.0; tot2=0.0
for _ in range(S):
    n=rng.poisson(R*R); x=rng.uniform(0,R,n); y=rng.uniform(0,R,n)
    # pairs a,b with x_a<x_b, y_a>y_b: cost x_b+y_a.  min over pairs: for each a, min x_b over b with x_b>x_a,y_b<y_a
    o=np.argsort(x); x=x[o]; y=y[o]
    best=1e9
    # suffix: for each index i (as a), need min x_j (j>i) with y_j<y_i -> scan from right keeping sorted structure; brute force O(n^2) ok for n~50
    for i in range(n):
        m=np.where(y[i+1:]<y[i])[0]
        if m.size: best=min(best,x[i+1+m[0]]+y[i])
    if best>=R: best=2*R  # cap (rare)
    tot+=best; tot2+=best*best
m=tot/S; print("E min cost over all descent pairs = %.4f (se %.4f); 2/E = %.4f"%(m, ((tot2/S-m*m)/S)**.5, 2/m))
