import subprocess, itertools, sys
def count_tb(k,w,mask=0):
    # tie-break with per-letter direction mask (bit l-1 set -> increasing ties)
    n=len(w); idx=sorted(range(n), key=lambda i:(w[i], i if (mask>>(w[i]-1))&1 else -i))
    p=[0]*n
    for r,i in enumerate(idx): p[i]=r+1
    out=subprocess.run(["./check",str(k),str(n)]+[str(x) for x in p],capture_output=True,text=True).stdout.split()
    return int(out[0])
k=7
for rho in ([1,3,7,5,4,2,6,8],[1,3,7,5,8,4,2,6]):
    w=rho*3
    best=max((count_tb(k,w,mask),mask) for mask in range(256))
    print("rho",rho,"best over masks:",best, flush=True)
    # move one letter: delete pos i, insert value v at pos j
    best2=(0,None)
    for i in range(24):
        w2=w[:i]+w[i+1:]
        for j in range(24):
            for v in range(1,9):
                w3=w2[:j]+[v]+w2[j:]
                c=count_tb(k,w3)
                if c>best2[0]: best2=(c,w3); 
                if c==5040: print("FOUND",w3,flush=True)
    print("rho",rho,"best over single move:",best2,flush=True)
