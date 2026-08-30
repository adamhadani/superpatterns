# W38 rate.py: k->infinity rate function r(theta) of the relaxed heuristic (proof.md §3); C2_plain where max r = 0.
from math import log
def r(th,C):
    l=1-th
    if th<=0: return -log(C)-2
    if th>=1: th=1-1e-12; l=1-th
    phi=th*log(4)+th+l*log(l)+(l/2+th)*log(l/2+th)-(l+2*th)*log(l+2*th)-(l/2)*log(l/2)
    return -1+l*(log(C)-log(l)+1)+2*th*log(C)+2*phi-th*log(th)+th-2*log(C)-2
def rho(C):
    best=max((r(i/2000.0,C),i/2000.0) for i in range(0,2001))
    return best
for C in [0.15,0.2,0.25,0.295,0.3,0.35,0.4,0.45,0.5,0.6,0.8,1.0]:
    v,t=rho(C); print(f"C={C}: max_theta r = {v:.4f} at theta*={t:.3f}   [ln((1+4C)/e^2C)={log((1+4*C)/(7.389056*C)):.4f}]")
lo,hi=0.25,1.0
for _ in range(60):
    mid=(lo+hi)/2
    if rho(mid)[0]>1e-12: lo=mid
    else: hi=mid
print(f"C2_plain (relaxed heuristic) = {hi:.5f}")
