import math,collections
def H(x): return -1 + x*x/4 + 2*math.log(x/2) - (2 + x*x/2)*math.log(2*x*x/(4+x*x))
rows=collections.defaultdict(dict)
for f in ['out/fix.txt','out/fix2.txt']:
    for l in open(f):
        r,h,N,reps,found,nf,unk=map(int,l.split()); k=r*h; C=round(N/(k*k),2)
        p,n=rows[(r,k)].get(C,(0,0)); rows[(r,k)][C]=(p+nf,n+reps)
Cs=[0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.7]
print("Pr(absent) [fixed strips, tilted grid r x (k/r)]; columns C =",Cs)
for (r,k) in sorted(rows):
    d=rows[(r,k)]
    print(f"r={r} k={k:2d} |"," ".join(f"{d[C][0]/d[C][1]:8.2e}" if C in d and d[C][0]>0 else f"<{1/d[C][1]:.0e}   " if C in d else "   --   " for C in Cs))
print("\nrate -ln P / N  (nan if P=0);  last columns: DZ rate H(1/sqrt C) for the identity, cap 1/r")
for (r,k) in sorted(rows):
    d=rows[(r,k)]
    out=[]
    for C in Cs:
        if C in d and d[C][0]>0: out.append(f"{-math.log(d[C][0]/d[C][1])/(C*k*k):7.4f}")
        else: out.append("   --  ")
    print(f"r={r} k={k:2d} |"," ".join(out),"| 1/r=%.3f"%(1/r))
print("DZ H     |"," ".join(f"{H(1/math.sqrt(C)):7.4f}" for C in Cs))
