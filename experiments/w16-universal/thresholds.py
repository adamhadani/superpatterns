# half-probability containment thresholds n_pi for id_k vs random pi (uniform permutations sigma_n), via contain_gen
import subprocess, random, sys, math, json
from concurrent.futures import ThreadPoolExecutor
def pats(k, seed):
    random.seed(seed); out=[("id", list(range(1,k+1)))]
    for j in range(4):
        p=list(range(1,k+1)); random.shuffle(p); out.append(("rand%d"%j,p))
    return out
def run(n,k,samples,seed,plist):
    args=["./contain_gen",str(n),str(samples),str(seed)]+[",".join(map(str,p)) for _,p in plist]
    o=subprocess.run(args,capture_output=True,text=True).stdout.split("\n")
    return [float(l.split()[1]) for l in o if l.strip()]
res={}
for k in [8,10,12,14,16]:
    plist=pats(k,100+k)
    c=(k/2+1.2*(k/2)**(1/3))**2
    ns=sorted(set(int(round(c*f)) for f in [0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.3]))
    samples=1000 if k<=12 else 400
    with ThreadPoolExecutor(6) as ex:
        rows=list(ex.map(lambda n: run(n,k,samples,17,plist), ns))
    res[k]={"ns":ns,"pats":[(a,b) for a,b in plist],"rows":rows}
    print("k=%d n:"%k, ns)
    for j,(name,p) in enumerate(plist):
        col=[r[j] for r in rows]
        # interpolate half-probability
        thr=None
        for i in range(len(ns)-1):
            if col[i]<0.5<=col[i+1]:
                thr=ns[i]+(0.5-col[i])/(col[i+1]-col[i])*(ns[i+1]-ns[i]); break
        print("  %-6s %s  n_half=%s  %s"%(name," ".join("%.3f"%v for v in col), "%.1f"%thr if thr else "?", "".join(map(str,p)) if k<10 else p))
    sys.stdout.flush()
json.dump(res,open("thresholds.json","w"))
