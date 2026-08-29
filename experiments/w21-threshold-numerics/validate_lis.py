import subprocess, os
env=dict(os.environ,VERBOSE="1"); tot=mism=0
for k,n in [(20,135),(24,190),(28,255),(32,330)]:
    idp=",".join(map(str,range(1,k+1)))
    a=subprocess.run(["./contain_bc",str(n),"300","5",idp],capture_output=True,text=True,env=env).stdout
    A=[int(l.split()[3]) for l in a.split("\n") if l.startswith("S ")]
    # lis prints only totals; recompute per-sample via samples=1 would be slow; instead compare hit totals AND per-sample using a per-sample lis variant
    b=subprocess.run(["./lis_v",str(n),"300","5",str(k)],capture_output=True,text=True).stdout
    B=[int(x) for x in b.split()]
    m=sum(x!=y for x,y in zip(A,B)); tot+=len(A); mism+=m
    print("k=%d n=%d: %d samples, mismatches=%d, frac=%.3f"%(k,n,len(A),m,sum(A)/len(A)))
print("TOTAL",tot,"mismatches",mism)
