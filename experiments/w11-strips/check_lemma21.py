# Sanity check of Lemma 2.1: grid n0=2m column groups, n1=2(r+1)m rows/strip, boxes (a,j,b) with a in [r*n0], b in [n1];
# B<=2m^2 bad boxes placed adversarially-ish (random, or clustered), verify molecule poset has chain >= m.
import random, itertools, sys
def height(r,m,bad):
    n0=2*m; n1=2*(r+1)*m
    good=lambda a,j,b: (a,j,b) not in bad
    # molecules per c: product of good rows per strip; DP over c increasing: h[c][b-tuple] = longest chain ending there
    # use DP: for each molecule (c,b), best = 1 + max over molecules (c',b') with c'<c, b'<b componentwise. Brute force (small).
    mols=[]
    for c in range(n0):
        G=[[b for b in range(1,n1+1) if good(r*c+j,j,b)] for j in range(r)]
        for bs in itertools.product(*G): mols.append((c,bs))
    best={}
    H=0
    for c,bs in mols:
        v=1
        for (c2,bs2),h in best.items():
            if c2<c and all(x<y for x,y in zip(bs2,bs)): v=max(v,h+1)
        best[(c,bs)]=v; H=max(H,v)
    return H
random.seed(1)
worst=None
for r,m in [(2,1),(2,2),(3,1),(2,3)]:
    n0=2*m; n1=2*(r+1)*m; boxes=[(a,j,b) for a in range(r*n0) for j in range(r) for b in range(1,n1+1)]
    hmin=10**9
    for trial in range(60 if m<3 else 12):
        B=2*m*m
        mode=trial%3
        if mode==0: bad=set(random.sample(boxes,B))
        elif mode==1: # cluster: fill rows of one strip in a few columns
            bad=set(); j=random.randrange(r); 
            for a in range(r*n0):
                if a%r!=j: continue
                for b in range(1,n1+1):
                    if len(bad)<B: bad.add((a,j,b))
        else: # anti-diagonal-ish
            bad=set()
            for a in range(r*n0):
                j=a%r
                for b in range(1,n1+1):
                    if len(bad)<B and (a//r + b) % (n0+1) in (n0//2, n0//2+1): bad.add((a,j,b))
        h=height(r,m,bad); hmin=min(hmin,h)
        assert h>=m, (r,m,mode,h)
    print(f"r={r} m={m}: min height over trials = {hmin} (need >= {m}) OK")
