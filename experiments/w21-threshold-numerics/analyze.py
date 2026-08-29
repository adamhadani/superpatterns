# analyze.py: collect n_half per (k, pattern) from k*.json (logistic fits) and lis_thr.json; fit the k-dependence.
import json, glob, math, sys, os
from fit import fit_ci
import random
def fits(json_file):
    d=json.load(open(json_file)); S=d["samples"]; out={}
    for nm in d["names"]:
        allh=[r[nm]["hits"] for r in d["rows"]]
        sel=[i for i,h in enumerate(allh) if 0.1*S<h<0.9*S]
        ns=[d["ns"][i] for i in sel]; hits=[allh[i] for i in sel]
        m,w,lo,hi=fit_ci(ns,hits,S,B=200)
        # linear-interpolation crossing as a model-free check
        cross=None
        for i in range(len(ns)-1):
            p0,p1=hits[i]/S,hits[i+1]/S
            if p0<0.5<=p1: cross=ns[i]+(0.5-p0)/(p1-p0)*(ns[i+1]-ns[i]); break
        out[nm]=(m,lo,hi,w,cross)
    return d["k"],out
def lstsq(X,y):
    # solve normal equations for small design matrices
    import itertools
    p=len(X[0]); A=[[sum(X[i][a]*X[i][b] for i in range(len(X))) for b in range(p)] for a in range(p)]
    bvec=[sum(X[i][a]*y[i] for i in range(len(X))) for a in range(p)]
    # gaussian elimination
    M=[A[i]+[bvec[i]] for i in range(p)]
    for c in range(p):
        piv=max(range(c,p),key=lambda r:abs(M[r][c])); M[c],M[piv]=M[piv],M[c]
        for r in range(p):
            if r!=c:
                f=M[r][c]/M[c][c]; M[r]=[M[r][j]-f*M[c][j] for j in range(p+1)]
    return [M[i][p]/M[i][i] for i in range(p)]
def fit_forms(ks,ns,sig,label):
    # form A: sqrt(n) = a k + b k^{1/3};  form B: n = c k^2 + d k;  form C: n = c k^2 + d k^{4/3}
    # bootstrap over the per-k errors sig (gaussian)
    rng=random.Random(3); res={"A":[],"B":[],"C":[],"D":[]}
    def one(nv):
        a,b=lstsq([[k,k**(1/3)] for k in ks],[math.sqrt(n) for n in nv])
        c,d=lstsq([[k*k,k] for k in ks],nv)
        c2,d2=lstsq([[k*k,k**(4/3)] for k in ks],nv)
        c3,d3,e3=lstsq([[k*k,k**(4/3),k**(2/3)] for k in ks],nv)
        return (a,b),(c,d),(c2,d2),(c3,d3,e3)
    A,B,C,D=one(ns)
    for _ in range(400):
        nv=[n+rng.gauss(0,s) for n,s in zip(ns,sig)]
        r=one(nv); res["A"].append(r[0]); res["B"].append(r[1]); res["C"].append(r[2]); res["D"].append(r[3])
    def ci(lst,i): v=sorted(x[i] for x in lst); return v[int(0.025*len(v))],v[int(0.975*len(v))]
    def resid(pred): return math.sqrt(sum((p-n)**2 for p,n in zip(pred,ns))/len(ns))
    rA=resid([(A[0]*k+A[1]*k**(1/3))**2 for k in ks]); rB=resid([B[0]*k*k+B[1]*k for k in ks]); rC=resid([C[0]*k*k+C[1]*k**(4/3) for k in ks]); rD=resid([D[0]*k*k+D[1]*k**(4/3)+D[2]*k**(2/3) for k in ks])
    print("  %s  k=%s"%(label,ks))
    print("    A: sqrt(n)=a k+b k^(1/3):   a=%.4f [%.4f,%.4f]  b=%.3f [%.3f,%.3f]   a^2=%.4f  rms=%.2f"%(A[0],*ci(res["A"],0),A[1],*ci(res["A"],1),A[0]**2,rA))
    print("    B: n=c k^2+d k:             c=%.4f [%.4f,%.4f]  d=%.3f [%.3f,%.3f]   rms=%.2f"%(B[0],*ci(res["B"],0),B[1],*ci(res["B"],1),rB))
    print("    C: n=c k^2+d k^(4/3):       c=%.4f [%.4f,%.4f]  d=%.3f [%.3f,%.3f]   rms=%.2f"%(C[0],*ci(res["C"],0),C[1],*ci(res["C"],1),rC))
    print("    D: n=c k^2+d k^(4/3)+e k^(2/3): c=%.4f [%.4f,%.4f] d=%.3f e=%.3f  rms=%.2f"%(D[0],*ci(res["D"],0),D[1],D[2],rD))
    # fixed a=1/2 form: sqrt(n)-k/2 = b k^{1/3}: per-k b
    print("    per-k b with a=1/2 fixed: "+" ".join("%.3f"%((math.sqrt(n)-k/2)/k**(1/3)) for k,n in zip(ks,ns)))
    print("    per-k (n-k^2/4)/k^(4/3): "+" ".join("%.3f"%((n-k*k/4)/k**(4/3)) for k,n in zip(ks,ns)))
if __name__=="__main__":
    files=sorted(glob.glob("k[0-9]*.json"),key=lambda f:int(f[1:-5]))
    lis=json.load(open("lis_thr.json")) if os.path.exists("lis_thr.json") else {}
    table={}
    print("## per-(k, pattern) thresholds (logistic fit, 95% parametric bootstrap CI; 'cross' = linear interpolation)")
    for f in files:
        k,out=fits(f); table[k]=out
        print("k=%d"%k)
        for nm,(m,lo,hi,w,cross) in out.items():
            print("  %-8s n_half=%7.2f [%7.2f,%7.2f]  w=%5.2f  cross=%s  n/k2=%.4f"%(nm,m,lo,hi,w,"%.2f"%cross if cross else "-",m/k/k))
        rs=[v[0] for nm,v in out.items() if nm.startswith("r")]
        if rs:
            mean=sum(rs)/len(rs); sd=math.sqrt(sum((x-mean)**2 for x in rs)/(len(rs)-1)) if len(rs)>1 else 0
            print("  random mean=%.2f sd=%.2f (sem %.2f) n/k2=%.4f ; id(solver)=%.2f ; id(LIS 1e5)=%s ; ratio rand/id(LIS)=%.4f"%(
                mean,sd,sd/math.sqrt(len(rs)),mean/k/k,out["id"][0],("%.2f"%lis[str(k)]["n_half"]) if str(k) in lis else "-",
                mean/lis[str(k)]["n_half"] if str(k) in lis else float('nan')))
    print("\n## identity from LIS (1e5 samples)")
    for k,v in sorted(lis.items(),key=lambda kv:int(kv[0])): print("  k=%2s n_half=%8.2f [%.2f,%.2f] n/k2=%.4f"%(k,v["n_half"],v["lo"],v["hi"],v["n_half"]/int(k)**2))
    print("\n## fits of the k-dependence")
    ks=[k for k in sorted(lis,key=int) if int(k)>=12]
    fit_forms([int(k) for k in ks],[lis[k]["n_half"] for k in ks],[max(0.3,(lis[k]["hi"]-lis[k]["lo"])/4) for k in ks],"identity (LIS, k>=12)")
    ks=[k for k in sorted(table) if any(nm.startswith("r") for nm in table[k])]
    means=[]; sems=[]
    for k in ks:
        rs=[v[0] for nm,v in table[k].items() if nm.startswith("r")]; mean=sum(rs)/len(rs)
        sd=math.sqrt(sum((x-mean)**2 for x in rs)/(len(rs)-1)); means.append(mean); sems.append(max(sd/math.sqrt(len(rs)),0.3))
    fit_forms(ks,means,sems,"random pi (mean over patterns)")
    # include W16's k=8..16 random means? (contain_gen, fewer samples) -- optional, listed separately
