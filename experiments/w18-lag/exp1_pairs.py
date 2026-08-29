"""Exp1: exact log[Pr(E_0 & E_Delta)/Pr(E_0)^2] for the tilted grid, all Delta, several C."""
import numpy as np, sys, time
sys.path.insert(0,'../w9-alon-threads')
from threads import tilted_grid, L_delta
from joint import joint2, log_binom_tail
from math import log
l = int(sys.argv[1]) if len(sys.argv)>1 else 10
Cs = [float(c) for c in sys.argv[2].split(',')] if len(sys.argv)>2 else [4,8]
pi = tilted_grid(l); k = l*l; r=h=l
for C in Cs:
    m = int(C*k); lf = log_binom_tail(m, k-1)
    print(f"== tilted grid {l}x{l}, k={k}, m={m} (C={C}); log Pr(fail) = {lf:.2f} ; m ln2 = {m*log(2):.1f}")
    print("  Delta  d  e   lag+=e*r+d  lag-=(h-e)r-d-1   L_Delta   logratio=log[P(both)/P(fail)^2]   -logratio/min(lag)")
    deltas = sorted(set([1,2,3,4,5,6,7,8,9] + list(range(10, k+1, max(1,l//2))) + [h, h+1, 2*h, 2*h+1, 3*h, k//2, k//2+1, k-1, k]))
    for D in deltas:
        if D > k: continue
        d, e = divmod(D, h)
        lagp = e*r + d; lagm = (h-e)*r - d - 1
        t0=time.time(); lr = joint2(pi, 0, D, m) - 2*lf
        mn = min(lagp, lagm) if e>0 else lagp
        print(f"  {D:5d} {d:2d} {e:2d}   {lagp:5d}      {lagm:5d}        {L_delta(pi,D):4d}      {lr:9.3f}      {(-lr/mn if mn>0 else float('nan')):7.3f}   ({time.time()-t0:.1f}s)", flush=True)
