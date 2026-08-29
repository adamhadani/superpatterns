# Level-2 bound E^{(2)}(pi,N) >= Pr(pi in Pi_N): Mecke integral with the strip factors AND the two-point-move factors
# of proof.md Lemma 2 (two-cell part F, or same-cell part e^{-mu} I0(2 sqrt mu) when the two-cell part is vacuous),
# using only pairs whose cells are pairwise disjoint and disjoint from the strips.  Monte Carlo on the gap simplices.
# Columns c=1..k+1 (g_c), bands b=0..k (h_b).  pi given 1-based as list.
import numpy as np, math, sys, json
from numpy import i0
rng=np.random.default_rng(2)
def F2(a,b):
    d=a-b; safe=np.where(np.abs(d)>1e-9,d,1.0)
    return np.where(np.abs(d)>1e-9,(a*np.exp(-b)-b*np.exp(-a))/safe,(1+a)*np.exp(-a))
def pairs_for(pi):
    k=len(pi); inv={pi[i]:i+1 for i in range(k)}   # rank -> position (1-based)
    used=set(); out=[]
    for r0 in range(1,k+1): used.add((r0,pi[r0-1]-1)); used.add((r0,pi[r0-1]))   # strip cells (col, band)
    for m in range(1,k):
        r=inv[m]; j=inv[m+1]
        if r<j:
            b=m+1; c1=r; c2=j+1; vac=(j+1<=k and pi[j]==m+2); adj=(j==r+1)
        else:
            b=m-1; c1=j; c2=r+1; vac=(r+1<=k and pi[r]==m-1); adj=(r==j+1)
        if not vac:
            cells=[(c1,b),(c2,b)]
            if any(c in used for c in cells): continue
            used.update(cells); out.append(("two",c1,c2,b))
        elif adj:
            if (c1,b) in used: continue
            used.add((c1,b)); out.append(("same",c1,None,b))
    return out
def E2(pi,N,M=300000):
    k=len(pi); P=pairs_for(pi)
    g=rng.exponential(size=(M,k+1)); g/=g.sum(1,keepdims=True)      # g[:,c-1] = column c, c=1..k+1
    h=rng.exponential(size=(M,k+1)); h/=h.sum(1,keepdims=True)      # h[:,b] = band b
    logw=np.zeros(M)
    for r in range(1,k+1):
        m=pi[r-1]; logw-=N*g[:,r-1]*(h[:,m-1]+h[:,m])
    logw2=logw.copy()
    for typ,c1,c2,b in P:
        if typ=="two": logw2+=np.log(F2(N*g[:,c1-1]*h[:,b],N*g[:,c2-1]*h[:,b]))
        else:
            mu=N*g[:,c1-1]*h[:,b]; logw2+=-mu+np.log(i0(2*np.sqrt(mu)))
    pref=k*math.log(N)-2*math.lgamma(k+1)
    w1=np.exp(logw+pref); w2=np.exp(logw2+pref)
    return w1.mean(), w2.mean(), w2.std()/math.sqrt(M), sum(1 for p in P if p[0]=="two"), sum(1 for p in P if p[0]=="same")
if __name__=="__main__":
    d=json.load(open("thresholds.json"))
    for k,N in [(12,48),(16,78),(16,86)]:
        for name,p in d[str(k)]["pats"]:
            e1,e2,se,n2,ns=E2(p,N)
            print("k=%d N=%d %-6s E_lc=%.3f  E_level2=%.3f (+-%.3f)  ratio=%.3f  [%d two-cell, %d same-cell pairs]"%(k,N,name,e1,e2,se,e2/e1,n2,ns)); sys.stdout.flush()
