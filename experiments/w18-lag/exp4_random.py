"""Exp4: random pi and block-perturbed grids F(r,h,eps), k=100, C=8: logratio for all Delta."""
import sys, numpy as np; sys.path.insert(0,'../w9-alon-threads'); sys.path.insert(0,'../w15-symmetry')
from threads import tilted_grid, L_delta
from exp1_symmetry import block_perturbed_grid
from joint import joint2, log_binom_tail
rng=np.random.default_rng(18)
k=100; C=8; m=C*k; lf=log_binom_tail(m,k-1)
print(f"k=100 m={m} -logPfail={-lf:.2f}")
for name, pi in [("random pi", rng.permutation(k)), ("random pi #2", rng.permutation(k)),
                 ("F(10,10,0.2)", block_perturbed_grid(10,10,0.2,rng)), ("F(10,10,0.4)", block_perturbed_grid(10,10,0.4,rng))]:
    print(f"== {name}: max_D L_D = {max(L_delta(pi,D) for D in range(1,k))}")
    out=[]
    for D in range(1,k+1):
        lr=joint2(pi,0,D,m)-2*lf; out.append((D,lr,L_delta(pi,D)))
    big=[o for o in out if o[1]>1.0]
    print(f"  #Delta with logratio>1: {len(big)};  max logratio {max(o[1] for o in out):.2f} at D={max(out,key=lambda o:o[1])[0]}; mean {np.mean([o[1] for o in out]):.3f}")
    print("  D,logratio,L_D for logratio>1: " + " ".join(f"({o[0]},{o[1]:.1f},{o[2]})" for o in big[:60]), flush=True)
