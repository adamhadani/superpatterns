"""Exp2: cost per unit lag vs C (tilted grid 10x10), positive lags (Delta=e<h/2) and negative lags (Delta=h-e')."""
import sys; sys.path.insert(0,'../w9-alon-threads')
from threads import tilted_grid
from joint import joint2, log_binom_tail
from math import log
pi = tilted_grid(10); k=100; r=h=10
print("C   m    -logPfail   | positive lag (Delta=e, lag=10e): loss/lag for e=1,2,3,4 | negative (Delta=h-e', lag=10e'-1): loss/lag e'=1,2,3 | predicted 2ln(C^2/4(C-1)), ln(C-1)")
for C in (3,4,5,6,8,12,16,24):
    m=int(C*k); lf=log_binom_tail(m,k-1)
    pos=[]; neg=[]
    for e in (1,2,3,4):
        lr=joint2(pi,0,e,m)-2*lf; pos.append((-lf-lr)/(10*e))
    for e in (1,2,3):
        lr=joint2(pi,0,h-e,m)-2*lf; neg.append((-lf-lr)/(10*e-1))
    print(f"{C:4.0f} {m:5d} {-lf:9.2f}   | " + " ".join(f"{x:6.3f}" for x in pos) + "  | " + " ".join(f"{x:6.3f}" for x in neg) + f"   | {2*log(C*C/(4*(C-1))):6.3f} {log(C-1):6.3f}", flush=True)
