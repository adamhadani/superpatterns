# Finite-k, fully explicit evaluation of Theorem C's bound:
#   pat(sigma) <= x^{-(n+1)} (x/(1-x))^{k+1} [ E W_good + Bad ]        for EVERY sigma in S_n.
# Even widths b iid, P(b)=(b-1) q^2 x^{b-2}, q=1-x, b>=2.  e=#even indices=floor((k-1)/2).
# m(b)=(b-2)(1-x^{(n-b-1)/(b-2)}) (b>=3), m(2)=0.
# Good weight for the j-th selected index (j=1..r, in index order): min((1+eps)m(b)+j+2, k)/(b-1), b>=beta;
# the product is additionally capped by 1 (|ext psi| = prod (b-1)); the DP drops that cap (upper bound), the cap is
# used only for the truncation errors (weights<=1).
# E W_good by DP over j (exact), truncated at j<=jmax with error P(Bin(e,p)>jmax) (weights<=1), widths truncated at bmax
# with error e*P(b>bmax).  Bad = e*n*q*sum_{b>=beta} q^2 (b-1) x^{b-2} exp(-m(b) h(eps)).
import numpy as np, sys
from math import lgamma, log, exp
def h(e): return (1+e)*log(1+e)-e
def bound_rate(k,lam,tau,beta_frac,eps,jfrac=0.08):
    n=int(lam*k*k/np.e**2); th=tau*np.e**2/lam; x=exp(-th/k); q=1-x
    e=(k-1)//2; beta=int(beta_frac*k)
    bmax=min(n, int(700*k/th))
    b=np.arange(2,bmax+1,dtype=float)
    logP=np.log(b-1)+2*log(q)+(b-2)*log(x); P=np.exp(logP)
    m=np.where(b>=3,(b-2)*(1-np.exp(((n-b-1)/np.maximum(b-2,1))*log(x))),0.0)
    sel=b>=beta; p=P[sel].sum(); Pbelow=P[~sel].sum()
    tail_b=exp((bmax-1)*log(x))*(1+(bmax-1)*q)   # exact P(b>bmax)=x^{bmax-1}(1+(bmax-1)q)
    jmax=int(jfrac*k)
    # weights w[j] = E[ min((1+eps)m+j+2,k,b-1)/(b-1) ; b>=beta ] for j=1..jmax
    J=np.arange(1,jmax+1)
    bs=b[sel]; ms=m[sel]; Ps=P[sel]
    b1=5*k; near=bs<=b1
    assert ((1+eps)*ms[~near]+3>=k).all()
    C=(Ps[~near]*k/(bs[~near]-1)).sum()
    bn=bs[near]; mn=ms[near]; Pn=Ps[near]
    w=np.empty(jmax+1)
    for j in J:
        w[j]=(Pn*np.minimum((1+eps)*mn+j+2,k)/(bn-1)).sum()+C   # corrected: no per-factor (b-1) cap
    # DP in log-scale-safe float (values <=1)
    F=np.zeros(jmax+1); F[0]=1.0
    for t in range(e):
        F=F*Pbelow+np.concatenate(([0.0],F[:-1]*w[1:]))
    EWgood=F.sum()
    # error terms
    # P(Bin(e,p)>jmax) via Chernoff: exp(-e*KL(jmax/e || p))
    a=jmax/e; KL=a*log(a/p)+(1-a)*log((1-a)/(1-p)); binom_tail=exp(-e*KL) if a>p else 1.0
    Bad=e*n*q*(Ps*np.exp(-ms*h(eps))).sum()
    Bad+=e*n*q*tail_b   # dropped widths b>bmax in the Bad sum (weight<=1 each)
    total=EWgood+binom_tail+e*tail_b+Bad
    logpref=-(n+1)*log(x)+(k+1)*log(x/(1-x))
    logkfact=lgamma(k+1)
    return (logpref+log(total)-logkfact)/k, dict(EWgood=EWgood,Bad=Bad,binom_tail=binom_tail,tail_b=tail_b,p=p,r_mean=e*p,n=n)
if __name__=="__main__":
    for k in [int(a) for a in sys.argv[1:]] or [10001,30001,100001]:
        for lam in [1.004,1.0048]:
            r,info=bound_rate(k,lam,0.9774,0.5936,0.149)
            print(f"k={k} lambda={lam}: (1/k)log(bound/k!) = {r:+.6f}   EWgood={info['EWgood']:.3e} Bad={info['Bad']:.3e} binTail={info['binom_tail']:.1e} r_mean={info['r_mean']:.0f} n={info['n']}",flush=True)
