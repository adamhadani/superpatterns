# For the family sigma = rho^B, rho in S_{ck}: sigma contains tau iff exists k-subset Y of letters
# with des(pi^{-1} tau) < B where pi = pattern of rho|Y.  So #patterns(sigma) <= C(ck,k) * sum_{d<B} A(k,d).
# Counting lower bound on B, hence on length ckB, as function of c.
from math import lgamma, log, exp
import sys
def logC(n,r): return lgamma(n+1)-lgamma(r+1)-lgamma(n-r+1)
def eulerian_logs(k):
    # A(k,d) via recurrence, in logs
    import numpy as np
    A=[0.0]  # log A(1,0)=0
    for n in range(2,k+1):
        new=[]
        for d in range(n):
            terms=[]
            if d<len(A): terms.append(log(d+1)+A[d])
            if d-1>=0 and d-1<len(A): terms.append(log(n-d)+A[d-1])
            m=max(terms); new.append(m+log(sum(exp(t-m) for t in terms)))
        A=new
    return A
k=int(sys.argv[1]) if len(sys.argv)>1 else 300
A=eulerian_logs(k); lk=lgamma(k+1)
# cumulative log sums
cum=[]; m=None
import math
s=0.0
for d in range(k):
    s = A[d] if d==0 else (max(s,A[d])+log(1+exp(min(s,A[d])-max(s,A[d]))))
    cum.append(s)
for c in [1.0,1.1,1.25,1.5,2,3,4,6,8,16,32,64]:
    m=int(round(c*k)); lc=logC(m,k)
    B=next(B for B in range(1,k+1) if lc+cum[B-1]>=lk-1e-6)
    print(f"c={c:5}: m={m:5} minimal B={B:4}  B/k={B/k:.4f}  length coeff c*B/k = {c*B/k:.4f}")
