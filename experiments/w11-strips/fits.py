# Speed analysis: at fixed f = N/(k^2/4), fit -ln Pfail = a * k^beta over k (beta=2 <-> speed N, beta=1 <-> speed k).
# Also local N-slope d(-ln P)/dN at fixed k between consecutive f values.
import glob,os,math,collections
agg=collections.defaultdict(lambda:[0,0,0])
for f in glob.glob('out/*.txt'):
    b=os.path.basename(f)[:-4].split('_'); name,k,N=b[0],int(b[1]),int(b[2])
    t=open(f).read().split()
    if len(t)<6: continue
    a=agg[(name,k,N)]; a[0]+=int(t[3]);a[1]+=int(t[4]);a[2]+=int(t[5])
def P(name,k,f,which):
    N=int(round(k*k/4*f)); a=agg.get((name,k,N))
    if not a: return None
    reps,cf,cx=a; c=cf if which=='free' else cx
    fails=reps-c
    if fails==0: return (None,reps)
    return (fails/reps, reps, fails)
print("Speed exponents beta from -ln P = a k^beta (least squares in log-log over available k with >=5 failures):")
for which in ('free','fixed'):
    print(f"\n### {which} strips")
    for fam,ks in [('id',(8,12,16,20)),('r2per',(8,12,16,20)),('r2rnd',(8,12,16,20)),('r2blk',(8,12,16,20)),('r2sum',(8,12,16,20)),('r3per',(9,12,15)),('r3rnd',(9,12,15)),('r3blk',(9,12,15)),('r3sum',(9,12,15))]:
        for f in (1.5,1.75,2.0,2.25,2.5):
            pts=[]
            for k in ks:
                r=P(fam,k,f,which)
                if r and r[0] and r[2]>=5: pts.append((k,-math.log(r[0]),r[2]))
            if len(pts)>=3:
                xs=[math.log(k) for k,_,_ in pts]; ys=[math.log(v) for _,v,_ in pts]
                n=len(pts); mx=sum(xs)/n; my=sum(ys)/n
                beta=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
                print(f"  {fam:6s} f={f:4.2f}: beta={beta:5.2f}   points (k, -lnP, #fails): "+", ".join(f"({k},{v:.2f},{nf})" for k,v,nf in pts))
