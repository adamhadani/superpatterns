# W38: relaxed cell-counting formula for E#pairs_j (see proof.md §3):
#   E#pairs_j ~ binom(N,j) N^{2m} Phi(L,m)^2 / m!,  L=j+1, m=k-j,  Phi = 4^m G(L)G(L/2+m)/(G(L+2m)G(L/2))
#   T_j = k! E#pairs_j / binom(N,k)^2 ;  R_relaxed = sum_j T_j.
import sys
from math import lgamma, log, exp
def lb(n,k): return lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
def terms(k,N):
    out=[]
    for j in range(0,k+1):
        m=k-j; L=j+1
        lphi = m*log(4)+lgamma(L)+lgamma(L/2+m)-lgamma(L+2*m)-lgamma(L/2)
        lt = lgamma(k+1)+lb(N,j)+2*m*log(N)+2*lphi-lgamma(m+1)-2*lb(N,k)
        out.append(lt)
    return out
if __name__=="__main__":
    k=int(sys.argv[1]); C=float(sys.argv[2]); N=round(C*k*k)
    t=terms(k,N); M=max(t); R=sum(exp(x-M) for x in t)*exp(M)
    print(f"k={k} N={N} C={C}: ln R_relaxed = {log(R):.4f}  (per k: {log(R)/k:.4f}); argmax j/k = {t.index(M)/k:.3f}")
    if k<=12: print("  ln T_j:", " ".join(f"{x:.2f}" for x in t))
