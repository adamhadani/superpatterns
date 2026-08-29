# logistic fit of containment probability vs n, n_half + parametric bootstrap CI
import math, random, json, sys
def logit_fit(ns, hits, S):
    # maximize binomial log-likelihood of p(n)=1/(1+exp(-(n-m)/w)) over (m,w) by Newton/grid; returns (m,w)
    ns=[float(n) for n in ns]
    # init: interpolate crossing
    m0=ns[0]; 
    for i in range(len(ns)-1):
        p0,p1=hits[i]/S,hits[i+1]/S
        if p0<0.5<=p1: m0=ns[i]+(0.5-p0)/(p1-p0)*(ns[i+1]-ns[i]); break
    else:
        m0=ns[-1] if hits[-1]/S<0.5 else ns[0]
    w0=(ns[-1]-ns[0])/6
    def nll(m,w):
        t=0.0
        for n,h in zip(ns,hits):
            z=(n-m)/w; p=1/(1+math.exp(-z)); p=min(max(p,1e-12),1-1e-12)
            t-=h*math.log(p)+(S-h)*math.log(1-p)
        return t
    m,w=m0,w0; best=nll(m,w)
    step_m,step_w=2.0,0.5
    for it in range(200):
        improved=False
        for dm,dw in [(step_m,0),(-step_m,0),(0,step_w),(0,-step_w)]:
            m2,w2=m+dm,max(w+dw,0.3); v=nll(m2,w2)
            if v<best: best,m,w=v,m2,w2; improved=True
        if not improved:
            step_m/=2; step_w/=2
            if step_m<1e-3: break
    return m,w
def fit_ci(ns,hits,S,B=400,seed=1):
    m,w=logit_fit(ns,hits,S); rng=random.Random(seed); ms=[]
    for b in range(B):
        hb=[]
        for n in ns:
            p=1/(1+math.exp(-(n-m)/w))
            if S<=300: hb.append(sum(1 for _ in range(S) if rng.random()<p))
            else: hb.append(min(S,max(0,int(round(rng.gauss(S*p,math.sqrt(S*p*(1-p))))))))
        ms.append(logit_fit(ns,hb,S)[0])
    ms.sort(); return m,w,ms[int(0.025*B)],ms[int(0.975*B)]
if __name__=="__main__":
    d=json.load(open(sys.argv[1])); S=d["samples"]
    print("k=%d samples=%d ns=%s"%(d["k"],S,d["ns"]))
    for nm in d["names"]:
        allh=[r[nm]["hits"] for r in d["rows"]]
        sel=[i for i,h in enumerate(allh) if 0.1*S<h<0.9*S]
        ns=[d["ns"][i] for i in sel]; hits=[allh[i] for i in sel]
        m,w,lo,hi=fit_ci(ns,hits,S)
        print("%-8s n_half=%7.2f [%7.2f,%7.2f] w=%.2f n/k2=%.4f  p: %s"%(nm,m,lo,hi,w,m/d["k"]**2," ".join("%.3f"%(h/S) for h in hits)))
