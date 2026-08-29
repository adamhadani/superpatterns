# k=20 (and 24) thresholds with contain_mrv (contain_gen has MAXK=16 and is invalid beyond k=16).
import subprocess, random, sys, math, json, time
from concurrent.futures import ThreadPoolExecutor
import random
def pats(k, seed):
    random.seed(seed); out=[("id", list(range(1,k+1)))]
    for j in range(4):
        p=list(range(1,k+1)); random.shuffle(p); out.append(("rand%d"%j,p))
    return out
def run(n,k,samples,seed,plist):
    args=["./contain_mrv",str(n),str(samples),str(seed)]+[",".join(map(str,p)) for _,p in plist]
    o=subprocess.run(args,capture_output=True,text=True).stdout.split("\n")
    return [float(l.split()[1]) for l in o if l.strip()]
if __name__!="__main__": raise SystemExit
k=int(sys.argv[1]); samples=int(sys.argv[2]); ns=[int(x) for x in sys.argv[3].split(",")]
plist=pats(k,100+k)
t0=time.time()
with ThreadPoolExecutor(8) as ex:
    rows=list(ex.map(lambda n: run(n,k,samples,17,plist), ns))
print("k=%d n:"%k, ns, "samples=%d  (%.0fs)"%(samples,time.time()-t0))
for j,(name,p) in enumerate(plist):
    col=[r[j] for r in rows]; thr=None
    for i in range(len(ns)-1):
        if col[i]<0.5<=col[i+1]:
            thr=ns[i]+(0.5-col[i])/(col[i+1]-col[i])*(ns[i+1]-ns[i]); break
    print("  %-6s %s  n_half=%s  %s"%(name," ".join("%.3f"%v for v in col), "%.1f"%thr if thr else "?", p))
json.dump({"k":k,"ns":ns,"pats":plist,"rows":rows},open("thresholds_k%d.json"%k,"w"))
