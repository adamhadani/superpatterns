"""Exp3: tilted grid 20x20 (k=400), C=8: loss vs lag; k-independence of the per-lag rate."""
import sys; sys.path.insert(0,'../w9-alon-threads')
from threads import tilted_grid, L_delta
from joint import joint2, log_binom_tail
pi = tilted_grid(20); k=400; r=h=20; C=8; m=C*k; lf=log_binom_tail(m,k-1)
print(f"k=400 m={m} -logPfail={-lf:.2f}")
print(" Delta  d  e  lag+   lag-   L_D   logratio   loss=-lf-logratio   loss/minlag")
for D in (1,2,3,4,5,8,10,12,15,17,18,19,20,21,40,41,60,100,200,201,210,300,399,400):
    d,e=divmod(D,h); lp=e*r+d; lm=(h-e)*r-d-1; mn=min(lp,lm) if e>0 else lp
    lr=joint2(pi,0,D,m)-2*lf
    print(f" {D:5d} {d:2d} {e:2d} {lp:5d} {lm:5d} {L_delta(pi,D):4d} {lr:9.2f} {(-lf-lr):9.2f}  {(-lf-lr)/mn if mn>0 else float('nan'):7.3f}", flush=True)
