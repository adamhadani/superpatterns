import itertools, sys
def sym(p):
    k=len(p); p=tuple(p)
    inv=[0]*k
    for i,v in enumerate(p): inv[v-1]=i+1
    out=set()
    for q in (p,tuple(inv)):
        for r in range(2):
            for c in range(2):
                t=q[::-1] if r else q
                t=tuple(k+1-x for x in t) if c else t
                out.add(t)
    return out
k=int(sys.argv[1]); seen=set(); reps=[]
for p in itertools.permutations(range(1,k+1)):
    if p in seen: continue
    s=sym(p); seen|=s; reps.append((''.join(map(str,p)),len(s)))
for r,w in reps: print(r,w)
