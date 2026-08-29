# Brute-force check of Prop 3.1: strip greedy output is a copy of pi iff each strip is a chain; output = pi' always.
import itertools, random
random.seed(1)
def greedy(pts,pi,strips):  # strips: list of (lo,hi) value intervals; lower corner rule restricted to strip & square
    k=len(pi); a=0.0; lev={j:lo/k for j,(lo,hi) in enumerate(strips)}; out=[]
    for p in range(k):
        j=[j for j,(lo,hi) in enumerate(strips) if lo<=pi[p]<=hi][0]; lo,hi=strips[j]; top=(hi+1)/k
        cand=[(x-a+y-lev[j],x,y) for x,y in pts if x>a and lev[j]<y<top]
        if not cand: return None
        _,x,y=min(cand); out.append((x,y)); a=x; lev[j]=y
    return out
def pattern(out):
    ys=sorted(range(len(out)),key=lambda i:out[i][1]); r=[0]*len(out)
    for rank,i in enumerate(ys): r[i]=rank
    return tuple(r)
def primed(pi,strips):
    k=len(pi); r=[0]*k; base=0
    for lo,hi in strips:
        pos=[p for p in range(k) if lo<=pi[p]<=hi]; vals=sorted(pi[p] for p in pos)
        for p,v in zip(pos,vals): r[p]=v
    return tuple(r)
bad=0; checked=0
for k,strips in [(4,[(0,1),(2,3)]),(5,[(0,2),(3,4)]),(5,[(0,1),(2,2),(3,4)]),(6,[(0,2),(3,5)])]:
    for pi in itertools.permutations(range(k)):
        chain=all(all(pi[p]<pi[q] for p,q in itertools.combinations([p for p in range(k) if lo<=pi[p]<=hi],2)) for lo,hi in strips)
        for t in range(6):
            n=3*k*k; pts=[(random.random(),random.random()) for _ in range(n)]
            out=greedy(pts,pi,strips)
            if out is None: continue
            checked+=1; pat=pattern(out)
            if (pat==tuple(pi))!=chain or pat!=primed(pi,strips): bad+=1
print("Prop 3.1 check: runs=%d violations=%d"%(checked,bad))
