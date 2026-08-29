import math,collections
rows=collections.defaultdict(dict)
for l in open('out/fix.txt'):
    r,h,N,reps,found,nf,unk=map(int,l.split()); k=r*h; C=N/(k*k)
    p=nf/reps; rows[(r,k)][round(C,2)]=(p,reps)
Cs=[0.5,0.75,1.0,1.5,2.0,3.0]
print("r k | Pr(absent) at C =",Cs,"| -lnP/N at those C | 1/r")
for (r,k) in sorted(rows):
    d=rows[(r,k)]; N=[C*k*k for C in Cs]
    ps=[d.get(C,(None,0))[0] for C in Cs]
    rate=[(-math.log(p)/n if (p and p>0) else float('nan')) for p,n in zip(ps,N)]
    print(r,k,'|',' '.join(f"{p:.2e}" if p else ' <1e-5 ' for p in ps),'|',' '.join(f"{x:.4f}" for x in rate),'|',f"{1/r:.3f}")
