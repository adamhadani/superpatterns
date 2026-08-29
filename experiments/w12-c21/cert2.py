import numpy as np, math
from certify import Tu, T21, rho, cw
from scipy.integrate import quad
print("universal scan:")
best=(9,0)
for s in np.arange(0.8,1.7,0.1):
    r=rho(Tu,s,M=40,n=4000); c=2*s/(-math.log(r)); best=min(best,(c,s)); print("  s=%.2f rho=%.6f c=%.5f"%(s,r,c))
print("min",best)
# convergence check at the best s
s=best[1]
for M,n in ((40,4000),(80,8000),(120,6000)): print("  M=%d n=%d rho=%.7f"%(M,n,rho(Tu,s,M,n)))
