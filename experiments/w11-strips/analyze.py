import glob,os,math,collections,sys
# aggregate out/name_k_N_seed.txt (line: N k r reps cnt_free cnt_fixed)
agg=collections.defaultdict(lambda:[0,0,0])
for f in glob.glob('out/*.txt'):
    b=os.path.basename(f)[:-4].split('_'); name,k,N,seed=b[0],int(b[1]),int(b[2]),b[3]
    t=open(f).read().split()
    if len(t)<6: continue
    reps,cf,cx=int(t[3]),int(t[4]),int(t[5])
    a=agg[(name,k,N)]; a[0]+=reps;a[1]+=cf;a[2]+=cx
names=sorted(set(k[0] for k in agg)); 
rows=collections.defaultdict(list)
for (name,k,N),(reps,cf,cx) in sorted(agg.items()):
    rows[(name,k)].append((N,reps,cf,cx))
def fmt(p,reps):
    if p==0: return f"<{1/reps:.0e}"
    return f"{p:.4f}" if p>=1e-3 else f"{p:.1e}"
for (name,k),L in sorted(rows.items(), key=lambda t:(t[0][1],t[0][0])):
    print(f"## {name} k={k}")
    print("  N      N/(k^2/4)  reps    Pfail_free   Pfail_fixed   -ln Pfree  -ln Pfixed")
    for N,reps,cf,cx in sorted(L):
        pf=1-cf/reps; px=1-cx/reps
        lf = f"{-math.log(pf):6.2f}" if pf>0 else "  inf "
        lx = f"{-math.log(px):6.2f}" if px>0 else "  inf "
        print(f"  {N:4d}   {N/(k*k/4):6.2f}  {reps:6d}   {fmt(pf,reps):>10s}   {fmt(px,reps):>10s}   {lf}   {lx}")
