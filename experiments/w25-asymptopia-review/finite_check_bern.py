# Finite-k evaluation of Theorem C with the Bernoulli (KL) bad term and width-dependent eps(b) (flat exponent R*k).
# Log-space version (no underflow); widths truncated at bmax = BM*k/theta with exact geometric tail x^{bmax-1}(1+(bmax-1)q).
import numpy as np, sys
from math import lgamma, log, exp, log1p
from scipy.special import logsumexp
def bound_rate(k,lam,tau,beta_frac,R,jfrac=0.14,BM=4000):
    n=int(lam*k*k/np.e**2); th=tau*np.e**2/lam; lx=-th/k; x=exp(lx); q=-np.expm1(lx)
    e=(k-1)//2; beta=int(beta_frac*k)
    bmax=min(n, int(BM*k/th))
    b=np.arange(2,bmax+1,dtype=float)
    logP=np.log(b-1)+2*log(q)+(b-2)*lx
    m=np.where(b>=3,(b-2)*(-np.expm1(((n-b-1)/np.maximum(b-2,1))*lx)),0.0)
    sel=b>=beta; logp=logsumexp(logP[sel]); p=exp(logp); logPbelow=logsumexp(logP[~sel]); Pbelow=exp(logPbelow)
    log_tail_b=(bmax-1)*lx+log1p((bmax-1)*q)
    jmax=int(jfrac*k)
    bs=b[sel]; ms=m[sel]; lPs=logP[sel]
    nb=bs-2; pb=np.clip(ms/nb,1e-300,1-1e-15)
    def KL(a,pp): return a*np.log(a/pp)+(1-a)*np.log((1-a)/(1-pp))
    emax=1/pb-1-1e-12
    full=nb*KL(np.minimum((1+emax)*pb,1-1e-12),pb) < R*k
    lo=np.zeros_like(pb); hi=emax.copy()
    for _ in range(60):
        mid=(lo+hi)/2; g=nb*KL((1+mid)*pb,pb)-R*k
        lo=np.where(g<0,mid,lo); hi=np.where(g<0,hi,mid)
    eps=np.where(full,emax,hi)
    badexp=nb*KL(np.minimum((1+eps)*pb,1-1e-15),pb)
    near=(1+eps)*ms+3<k
    C=exp(logsumexp(lPs[~near]+log(k)-np.log(bs[~near]-1))) if (~near).any() else 0.0
    bn=bs[near]; mn=ms[near]; Pn=np.exp(lPs[near]); en=eps[near]
    w=np.empty(jmax+1)
    for j in range(1,jmax+1):
        w[j]=(Pn*np.minimum((1+en)*mn+j+2,k)/(bn-1)).sum()+C
    # DP with rescaling: F_t = F_{t-1}*Pbelow + shift(F_{t-1})*w ; track log scale
    F=np.zeros(jmax+1); F[0]=1.0; logscale=0.0
    for t in range(e):
        F=F*Pbelow+np.concatenate(([0.0],F[:-1]*w[1:]))
        s=F.max()
        if s<1e-100: F/=s; logscale+=log(s)
    logEWgood=log(F.sum())+logscale
    a=jmax/e; KLb=a*log(a/p)+(1-a)*log((1-a)/(1-p)); log_binom_tail=-e*KLb if a>p else 0.0
    logpre=log(e)+log(n)+log(q)
    logBad=logsumexp([logpre+logsumexp(lPs-badexp), logpre+log_tail_b])
    logtotal=logsumexp([logEWgood,log_binom_tail,log(e)+log_tail_b,logBad])
    logpref=-(n+1)*lx+(k+1)*(lx-log(q))
    return (logpref+logtotal-lgamma(k+1))/k, dict(logEWgood=logEWgood/k,logBad=logBad/k,logbin=log_binom_tail/k,logtail=(log(e)+log_tail_b)/k,n=n,eps_at_beta=float(eps[0]))
if __name__=="__main__":
    ks=[int(a) for a in sys.argv[1:]] or [30001,100001]
    for k in ks:
        for lam in [1.0065,1.007]:
            r,info=bound_rate(k,lam,0.9681,0.5369,0.00783)
            print(f"k={k} lambda={lam}: (1/k)log(bound/k!) = {r:+.6f}  [per-k logs: EWgood={info['logEWgood']:+.5f} Bad={info['logBad']:+.5f} binTail={info['logbin']:+.5f} widthTail={info['logtail']:+.5f}] eps(beta)={info['eps_at_beta']:.3f}",flush=True)
