import itertools,sys
def sym(p):
    j=len(p); out=set()
    inv=[0]*j
    for i,v in enumerate(p): inv[v-1]=i+1
    for q in (p,tuple(inv)):
        out.add(q); out.add(tuple(j+1-v for v in q[::-1]))   # inverse, reverse-complement: the symmetries preserving (+)-chains
    return out
reps={}
for j in (2,3,4,5):
    seen=set(); cl=[]
    for p in itertools.permutations(range(1,j+1)):
        if p in seen: continue
        o=sym(p); seen|=o; cl.append((min(o),len(o)))
    reps[j]=cl
    print(j,len(cl),' '.join(''.join(map(str,c))+f'({n})' for c,n in cl))
with open('reps.txt','w') as f:
    for j in reps:
        for c,n in reps[j]: f.write(''.join(map(str,c))+'\n')
