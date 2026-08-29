import numpy as np, sys
sys.path.insert(0,'../w9-alon-threads')
from threads import tilted_grid, run_thread
from joint import joint2, joint3, log_binom_tail
from math import exp
rng = np.random.default_rng(1)
pi = tilted_grid(4); k=16; m=28; q=2*k
for D in (1,4,5):
    ex = exp(joint2(pi,0,D,m))
    f=0; T=40000
    for _ in range(T):
        M = rng.integers(0,2,size=(q,m),dtype=np.int8)
        f += (not run_thread(M,pi,'H',0)['ok']) and (not run_thread(M,pi,'H',D)['ok'])
    print(f"D={D}: exact {ex:.4f}  MC {f/T:.4f} +- {np.sqrt(ex*(1-ex)/T):.4f}")
# joint3 consistency
lf = log_binom_tail(m,k-1)
print("joint3(0,4,k) - joint2(0,4) - single:", joint3(pi,(0,4,k),m) - joint2(pi,0,4,m) - lf)
ex3 = exp(joint3(pi,(0,4,8),m)); f=0; T=40000
for _ in range(T):
    M = rng.integers(0,2,size=(q,m),dtype=np.int8)
    f += all(not run_thread(M,pi,'H',s)['ok'] for s in (0,4,8))
print(f"3 threads (0,4,8): exact {ex3:.4f} MC {f/T:.4f}")
