# level-2 gain E^{(2)}/E_lc for larger k at N where E_lc ~ 1-3 (identity vs random patterns)
import numpy as np, random, math, sys
from level2_mc import E2
def pats(k, seed):
    random.seed(seed); out=[("id", list(range(1,k+1)))]
    for j in range(3):
        p=list(range(1,k+1)); random.shuffle(p); out.append(("rand%d"%j,p))
    return out
for k,N in [(20,115),(24,150),(32,250)]:
    for name,p in pats(k,100+k):
        e1,e2,se,n2,ns=E2(p,N,M=400000)
        print("k=%d N=%d %-6s E_lc=%.3f E_level2=%.3f (+-%.3f) ratio=%.3f log-ratio/k=%.4f [%d two-cell, %d same-cell]"%(k,N,name,e1,e2,se,e2/e1,math.log(e2/e1)/k,n2,ns)); sys.stdout.flush()
