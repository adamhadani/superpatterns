# sweep.py tag k samples n1,n2,... name=pat name=pat ...   -> runs contain_bc for each n (parallel, W workers), writes tag.json
import subprocess, sys, json, time, os
from concurrent.futures import ThreadPoolExecutor
tag=sys.argv[1]; k=int(sys.argv[2]); samples=int(sys.argv[3]); ns=[int(x) for x in sys.argv[4].split(",")]
names=[a.split("=")[0] for a in sys.argv[5:]]; pats=[a.split("=")[1] for a in sys.argv[5:]]
W=int(os.environ.get("W","3"))
def run(n):
    t0=time.time()
    o=subprocess.run(["./contain_bc",str(n),str(samples),str(1000+n)]+pats,capture_output=True,text=True).stdout
    res={}
    for l in o.split("\n"):
        if not l.strip(): continue
        f=l.split(); res[names[pats.index(f[0])]]={"p":float(f[1]),"hits":int(f[2][5:]),"nodes":int(f[3][6:]),"sec":float(f[4][4:])}
    print("n=%d done %.0fs"%(n,time.time()-t0),flush=True)
    return res
with ThreadPoolExecutor(W) as ex: rows=list(ex.map(run,ns))
json.dump({"tag":tag,"k":k,"samples":samples,"ns":ns,"names":names,"pats":pats,"rows":rows},open(tag+".json","w"),indent=1)
for j,nm in enumerate(names):
    print("%-8s"%nm," ".join("%.3f"%r[nm]["p"] for r in rows)," sec=%.0f"%sum(r[nm]["sec"] for r in rows))
