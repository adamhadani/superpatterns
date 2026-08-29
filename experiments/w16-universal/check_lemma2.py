# Brute-force check of Lemma 2 (proof.md) and of Theorem 3's inequality at small k: Poisson samples, all copies
# enumerated, lex-min copy checked against level-1 strips and the two-point-move conditions (ii)/(iii).
import numpy as np, itertools, math, sys
from level2_mc import E2, pairs_for
rng=np.random.default_rng(7)
def copies(pts,pi):
    k=len(pi); n=len(pts); order=np.argsort(pts[:,0]); P=pts[order]
    out=[]
    for idx in itertools.combinations(range(n),k):
        ys=P[list(idx),1]; ranks=np.argsort(np.argsort(ys))+1
        if all(ranks[i]==pi[i] for i in range(k)): out.append(P[list(idx)])
    return out
def check(pi,N,samples):
    k=len(pi); viol=0; contained=0
    for _ in range(samples):
        n=rng.poisson(N); pts=rng.random((n,2))
        C=copies(pts,pi)
        if not C: continue
        contained+=1
        P=min(C,key=lambda c: tuple(c[:,0]))
        xs=np.concatenate([[0],P[:,0],[1]]); ysort=np.concatenate([[0],np.sort(P[:,1]),[1]])
        def cell(c,b): return [q for q in pts if xs[c-1]<q[0]<xs[c] and ysort[b]<q[1]<ysort[b+1]]
        for r in range(1,k+1):
            if cell(r,pi[r-1]-1) or cell(r,pi[r-1]): viol+=1
        inv={pi[i]:i+1 for i in range(k)}
        for m in range(1,k):
            r=inv[m]; j=inv[m+1]
            if r<j:
                A=cell(r,m+1); Bc=cell(j+1,m+1)+([q for q in cell(r,m+1)] if j==r+1 else [])
                for q in A:
                    for q2 in Bc:
                        if q2[0]>q[0] and q2[1]>q[1]: viol+=1
            else:
                A=cell(j,m-1); Bc=cell(r+1,m-1)+([q for q in cell(j,m-1)] if r==j+1 else [])
                for q in A:
                    for q2 in Bc:
                        if q2[0]>q[0] and q2[1]<q[1]: viol+=1
    return contained, viol
for pi,N in [([1,2,3,4],8),([2,4,1,3],8),([3,1,4,2],8),([1,3,2,5,4],10),([2,5,3,1,4],10),([4,2,5,1,3],10)]:
    S=1500; c,v=check(pi,N,S)
    e1,e2,se,n2,ns=E2(pi,N,M=200000)
    print("pi=%s N=%d  Pr(contain)=%.3f  violations of Lemma 2 among lex-min copies: %d   E_lc=%.3f  E_level2=%.3f (%d two-cell, %d same-cell)"%(pi,N,c/S,v,e1,e2,n2,ns)); sys.stdout.flush()
