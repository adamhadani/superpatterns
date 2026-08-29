# exact evaluation of (1.2): B(N,k) = 2^-N sum_m C(N,m) m! [z^m] F(z)^{2(k-1)},  F = sum z^n/(n!)^2
import math, sys
def logB(N,k):
    L=2*(k-1)
    # log-domain polynomial power by repeated squaring/multiplication
    lf=[-2*math.lgamma(n+1) for n in range(N+1)]
    def mul(a,b):
        out=[-math.inf]*(N+1)
        for i,ai in enumerate(a):
            if ai==-math.inf: continue
            for j in range(N+1-i):
                bj=b[j]
                if bj==-math.inf: continue
                v=ai+bj; o=out[i+j]
                out[i+j]= v if o==-math.inf else max(o,v)+math.log1p(math.exp(-abs(o-v)))
        return out
    res=None; base=lf; e=L
    while e:
        if e&1: res=base if res is None else mul(res,base)
        e>>=1
        if e: base=mul(base,base)
    terms=[math.lgamma(N+1)-math.lgamma(m+1)-math.lgamma(N-m+1)+math.lgamma(m+1)+res[m] for m in range(N+1)]
    mx=max(terms); s=mx+math.log(sum(math.exp(t-mx) for t in terms))
    return s-N*math.log(2), max(range(N+1),key=lambda m:terms[m])/N
for k,C in [(10,30),(10,40),(10,60),(14,40),(14,60),(20,40),(20,60)]:
    N=int(C*k*k); lb,beta=logB(N,k); print(k,C,N,"-lnB/N =",round(-lb/N,4),"beta* =",round(beta,3))
