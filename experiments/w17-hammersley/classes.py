import itertools
def inv(p):
    q=[0]*len(p)
    for i,v in enumerate(p): q[v-1]=i+1
    return tuple(q)
def rc(p):
    n=len(p); return tuple(n+1-v for v in reversed(p))
for n in (3,4):
    seen=set(); reps=[]
    for p in itertools.permutations(range(1,n+1)):
        if p in seen: continue
        orb={p,inv(p),rc(p),inv(rc(p)),rc(inv(p))}
        # closure
        changed=True
        while changed:
            changed=False
            for q in list(orb):
                for r in (inv(q),rc(q)):
                    if r not in orb: orb.add(r); changed=True
        seen|=orb; reps.append((p,sorted(orb)))
    for p,orb in reps: print(''.join(map(str,p)), ''.join(map(str,inv(p))), len(orb), ' '.join(''.join(map(str,q)) for q in orb))
