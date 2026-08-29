"""Exp5: three threads, tilted grid 8x8 (k=64), C=8: exact log Pr(all 3 fail) - 3 logPfail, and comparison
with pairwise losses (is the loss of thread 3 ~ min over earlier threads?)."""
import sys; sys.path.insert(0,'../w9-alon-threads')
from threads import tilted_grid
from joint import joint2, joint3, log_binom_tail
pi=tilted_grid(8); k=64; h=r=8; C=8; m=C*k; lf=log_binom_tail(m,k-1)
print(f"k=64 m={m} -logPfail={-lf:.2f}")
def pair(a,b): return joint2(pi,min(a,b),abs(b-a)+min(a,b),m) if False else joint2(pi,a,b,m)-2*lf
print(" shifts        gain2(t2|t1)  gain3(t3|t1,t2)  [gain = increase of -log P when adding the thread]   pair losses: L(1,2) L(1,3) L(2,3)")
for ts in [(0,4,8),(0,4,32),(0,32,64),(0,2,4),(0,4,12),(0,20,40),(0,28,36),(0,3,6),(0,36,64),(0,30,60)]:
    j2=joint2(pi,ts[0],ts[1],m); j3=joint3(pi,ts,m)
    g2=-(j2-lf)-(-lf); g3=-(j3-j2)
    L=[-lf-(joint2(pi,a,b,m)-2*lf) for a,b in ((ts[0],ts[1]),(ts[0],ts[2]),(ts[1],ts[2]))]
    print(f" {str(ts):14s} {g2:10.2f} {g3:12.2f}      pair losses {L[0]:7.2f} {L[1]:7.2f} {L[2]:7.2f}   min(L13,L23)={min(L[1],L[2]):7.2f}  -> predicted gain3 = -lf - min = {-lf-min(L[1],L[2]):7.2f}", flush=True)
