# identity thresholds from the LIS: n_half(k) with 1e5 samples (lis.c), logistic fit
import subprocess, json, sys
from fit import fit_ci
out={}
for k in [8,10,12,14,16,20,24,28,32,36,40,48]:
    c=0.34*k*k+0.0; ns=sorted(set(int(round(c*(1+f))) for f in [-0.14,-0.1,-0.06,-0.03,0,0.03,0.06,0.1,0.14]))
    S=100000; hits=[]
    for n in ns:
        o=subprocess.run(["./lis",str(n),str(S),str(n),str(k)],capture_output=True,text=True).stdout
        hits.append(int(o.split("hits=")[1]))
    m,w,lo,hi=fit_ci(ns,hits,S,B=200)
    out[k]={"ns":ns,"hits":hits,"S":S,"n_half":m,"lo":lo,"hi":hi}
    print("k=%2d n_half(id)=%8.2f [%.2f,%.2f] n/k2=%.4f  ns=%s p=%s"%(k,m,lo,hi,m/k/k,ns," ".join("%.3f"%(h/S) for h in hits)),flush=True)
json.dump(out,open("lis_thr.json","w"),indent=1)
