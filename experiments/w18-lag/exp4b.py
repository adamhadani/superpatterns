import sys, numpy as np; sys.path.insert(0,'../w9-alon-threads')
from threads import L_delta
from joint import joint2, log_binom_tail
rng=np.random.default_rng(18); k=100
for C in (4,6):
    m=C*k; lf=log_binom_tail(m,k-1); pi=rng.permutation(k)
    out=[joint2(pi,0,D,m)-2*lf for D in range(1,k+1)]
    print(f"random pi, C={C}: -logPfail={-lf:.2f}; logratio over D=1..k: min {min(out):.3f} mean {np.mean(out):.3f} max {max(out):.3f}; max L_D={max(L_delta(pi,D) for D in range(1,k))}", flush=True)
