# W33: per-pattern slopes from SMC dumps (smcK/PAT_sS.txt: "n p lnp") and exact dumps (exact/PAT.txt: "n Av_n p")
import glob, math, os, sys, collections
def load(fn):
    d={}
    for l in open(fn):
        a=l.split()
        if len(a)>=3: d[int(a[0])]=float(a[2]) if 'exact' not in fn else math.log(float(a[1]))-math.lgamma(int(a[0])+1)
    return d
def slopes(d): return {n: d[n-1]-d[n] for n in d if n-1 in d}
out=[]
for k in [4,5,6,7]:
    files=sorted(glob.glob(f'smc{k}/*_s*.txt'))
    pats=sorted(set(os.path.basename(f).split('_')[0] for f in files))
    if not pats: continue
    Cs=[0.5,0.75,1.0,1.25,1.5]
    out.append(f"\n### k={k}: slope s(n)=ln p(n-1)-ln p(n) from SMC (mean over seeds), at n=round(C k^2)")
    out.append("| π | " + " | ".join(f"C={C}" for C in Cs) + " | rate -ln p/n at C=1 | max_n s (n≤2k²) |")
    out.append("|---|"+"---|"*(len(Cs)+2))
    for p in pats:
        ss=collections.defaultdict(list); lp=collections.defaultdict(list)
        for f in glob.glob(f'smc{k}/{p}_s*.txt'):
            d=load(f); 
            for n,v in slopes(d).items(): ss[n].append(v)
            for n,v in d.items(): lp[n].append(v)
        row=[]
        for C in Cs:
            n=round(C*k*k)
            row.append(f"{sum(ss[n])/len(ss[n]):.3f}" if ss.get(n) else "-")
        n1=k*k; rate=-sum(lp[n1])/len(lp[n1])/n1 if lp.get(n1) else float('nan')
        mx=max((sum(v)/len(v),n) for n,v in ss.items() if n<=2*k*k)
        out.append(f"| {p} | "+" | ".join(row)+f" | {rate:.3f} | {mx[0]:.3f} (n={mx[1]}) |")
# exact small n
out.append("\n### exact slopes (generating tree enumeration), k=4 (n≤11) and k=5 (n≤10)")
for k,nm in [(4,11),(5,10)]:
    fs=sorted(glob.glob('exact/*.txt')); fs=[f for f in fs if len(os.path.basename(f))==k+4]
    if not fs: continue
    ns=list(range(k+1,nm+1))
    out.append(f"| π | "+" | ".join(f"n={n}" for n in ns)+" |"); out.append("|---|"+"---|"*len(ns))
    for f in fs:
        d=load(f); s=slopes(d)
        out.append(f"| {os.path.basename(f)[:-4]} | "+" | ".join(f"{s[n]:.3f}" for n in ns if n in s)+" |")
print("\n".join(out))
