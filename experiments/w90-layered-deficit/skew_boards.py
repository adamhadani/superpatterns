# Enumerate skew boards D = S ∩ U inside [N]x[N] (S down-set, U up-set; cells (col,row), 1-indexed),
# count transversal fillings and those with no "D-inversion" (a NW of b with SW corner (xa,yb) in D... i.e. in U,
# and NE corner (xb,ya) in S).  Report minimal boards with >= 2 D-inversion-free fillings.
import itertools, sys
def downsets(N):
    # down-set of [N]x[N] <-> weakly decreasing heights s[1..N] (column c has cells rows 1..s[c])
    for s in itertools.product(range(N+1), repeat=N):
        if all(s[i]>=s[i+1] for i in range(N-1)): yield s
def run(N):
    best=[]
    for s in downsets(N):
        for u in downsets(N):
            # up-set as complement-like: column c has cells rows > u'[c], with u' weakly decreasing (so U = {(c,r): r > t[c]}), t decreasing in c
            t=u
            cells={(c,r) for c in range(1,N+1) for r in range(1,N+1) if r<=s[c-1] and r>t[c-1]}
            fills=[p for p in itertools.permutations(range(1,N+1)) if all((c+1,p[c]) in cells for c in range(N))]
            if not fills: continue
            good=[]
            for p in fills:
                ok=True
                for i in range(N):
                    for j in range(i+1,N):
                        if p[i]>p[j]:
                            # a=(i+1,p[i]) NW of b=(j+1,p[j]); SW corner (i+1,p[j]) in U (i.e. in D since <= a in S), NE corner (j+1,p[i]) in S
                            if (i+1,p[j]) in cells and (j+1,p[i]) in cells: ok=False;break
                    if not ok:break
                if ok: good.append(p)
            dec=tuple(range(N,0,-1))
            assert dec in fills, (s,t,fills)           # sorting argument: f_dec valid iff any filling valid
            assert len(good)>=1, (s,t)
            if len(good)>=2: best.append((s,t,len(fills),good))
    return best
for N in range(1,7):
    b=run(N)
    print("N=%d: boards with >=2 inversion-free fillings: %d"%(N,len(b)))
    for (s,t,nf,good) in b[:6]:
        print("   S heights",s," U floors",t," #fillings",nf," inversion-free:",good)
    if b and N>=5: break
