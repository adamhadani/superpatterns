# Per-class brute-force check of Lemma 1' (corrected) and of the summed inequality.
# Classes: psi = (I, off-I positions), I = {i even (1-based), 2<=i<=k-1 : b_i >= beta}.
# Corrected per-class bound: N(psi) <= min( Prod_j min(M_j + j - 1, k),  Prod_j (b_j - 1) ).
# Old (WRONG) bound: Prod_j min(M_j + j - 1, k, b_j - 1).
import itertools, bisect, random, sys
from collections import defaultdict
def pat(sig,T):
    vals=[sig[t] for t in T]; return tuple(sorted(range(len(T)),key=lambda j:vals[j]))
def classes(sig,k,beta):
    n=len(sig); C=defaultdict(set)
    for T in itertools.combinations(range(n),k):
        I=tuple(i for i in range(1,k-1) if i%2==1 and T[i+1]-T[i-1]>=beta)  # 0-based odd = 1-based even
        off=tuple(T[j] for j in range(k) if j not in I)
        C[(I,off)].add(pat(sig,T))
    return C
def check(sig,k,beta):
    n=len(sig); C=classes(sig,k,beta)
    viol_new=viol_old=0; sum_new=sum_old=sum_cks=0.0; worst=None
    for (I,off),pats in C.items():
        V=sorted(sig[p] for p in off)
        # windows: I-index i has neighbours in T; reconstruct positions from off: T positions sorted = off + one per window
        # off-I positions in index order; window for I-index i lies between off entries.
        offl=list(off); Ms=[]; bs=[]
        # rebuild T-index -> position for off indices
        idx=0; posmap={}
        for j in range(k):
            if j in I: continue
            posmap[j]=offl[idx]; idx+=1
        for i in I:
            lo,hi=posmap[i-1],posmap[i+1]; b=hi-lo
            M=len({bisect.bisect(V,sig[p]) for p in range(lo+1,hi)})
            Ms.append(M); bs.append(b)
        prodM=1; prodb=1; old=1; cks=1
        for j,(M,b) in enumerate(zip(Ms,bs)):
            prodM*=min(M+j,k); prodb*=(b-1); old*=min(M+j,k,b-1); cks*=min(k,b-1)
        new=min(prodM,prodb); N=len(pats)
        if N>new: viol_new+=1
        if N>old:
            viol_old+=1
            if worst is None or N-old>worst[0]: worst=(N-old,I,off,V,Ms,bs,N,old)
        # This loop already aggregates by extension class. Division by the
        # extension count belongs only to a sum over individual occurrences.
        sum_new+=new; sum_old+=old; sum_cks+=min(cks,prodb)
    P=len(set().union(*C.values()))
    assert P <= sum_new, "The sum of valid class bounds must cover all patterns"
    return dict(pat=P,classes=len(C),viol_new=viol_new,viol_old=viol_old,sum_new=sum_new,sum_old=sum_old,sum_cks=sum_cks,worst=worst)
sp6=[6,14,10,2,13,17,5,8,3,12,9,16,1,7,11,4,15]
sp7=[7,20,13,10,2,18,23,4,12,16,8,5,19,15,1,9,22,14,6,17,11,3,21]
def zeta(k):
    w=[x for r in range(k) for x in (list(range(1,k+1,2)) if r%2==0 else list(range(k if k%2==0 else k-1,0,-2)))]
    order=sorted(range(len(w)),key=lambda p:(w[p],-p)); sig=[0]*len(w)
    for rank,p in enumerate(order): sig[p]=rank+1
    return sig
random.seed(1)
tests=[("sp6=17",sp6,6),("sp6 k=5",sp6,5),("sp7=23",sp7,7)]
r17=list(range(1,18)); random.shuffle(r17); tests.append(("random17 k=6",r17,6))
r14=list(range(1,15)); random.shuffle(r14); tests.append(("random14 k=5",r14,5))
tests.append(("zeta5",zeta(5),5)); tests.append(("zeta6",zeta(6),6))
tot_viol=0
for name,sig,k in tests:
    for beta in [2,3,k-1,k,k+2]:
        r=check(sig,k,beta); tot_viol+=r['viol_new']
        print(f"{name:13s} k={k} n={len(sig)} beta={beta:2d} pat={r['pat']} classes={r['classes']:6d} "
              f"VIOL(corrected)={r['viol_new']} viol(old)={r['viol_old']:4d}  sums: corrected={r['sum_new']:.0f} old={r['sum_old']:.0f} Lemma1={r['sum_cks']:.0f}",flush=True)
        if r['worst'] and beta==k-1: print("   worst old violation (excess,I,off,V,M,b,N,oldbound):",r['worst'])
print("TOTAL violations of corrected bound:",tot_viol)
