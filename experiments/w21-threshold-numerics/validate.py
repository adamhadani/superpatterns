# per-sample agreement of contain_bc vs contain_gen (k<=12) on random patterns
import subprocess, random, os, sys
random.seed(2026); env=dict(os.environ,VERBOSE="1")
tot=0; mism=0
for k in [6,8,10,12]:
    pats=[]
    for j in range(6):
        p=list(range(1,k+1)); random.shuffle(p); pats.append(",".join(map(str,p)))
    pats.append(",".join(map(str,range(1,k+1))))
    for n in {6:[10,14],8:[18,26],10:[28,38],12:[40,52]}[k]:
        for seed in [1,2]:
            a=subprocess.run(["./contain_bc",str(n),"500",str(seed)]+pats,capture_output=True,text=True,env=env).stdout
            b=subprocess.run(["./contain_gen",str(n),"500",str(seed)]+pats,capture_output=True,text=True,env=env).stdout
            A=[l for l in a.split("\n") if l.startswith("S ")]; B=[l for l in b.split("\n") if l.startswith("S ")]
            assert len(A)==len(B)==500*len(pats)
            m=sum(x!=y for x,y in zip(A,B)); mism+=m; tot+=len(A)
            print("k=%d n=%d seed=%d comparisons=%d mismatches=%d"%(k,n,seed,len(A),m))
print("TOTAL comparisons=%d mismatches=%d"%(tot,mism))
