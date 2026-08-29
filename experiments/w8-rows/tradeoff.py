# I(rho) = max over S subset [m] of asc(S) = #{consecutive-in-S pairs a<b with a before b in rho};  D(rho) similarly (b before a).
# Theorem (identical blocks rho^B, ANY row patterns): cost(id) = min_psi (1+wdes) = k - asc(S)  => cost(id) >= k - I(rho); cost(dec) >= k - D(rho).
import itertools
def ID(rho):
    m=len(rho); pos={v:i for i,v in enumerate(rho)}
    I=[0]*m; D=[0]*m
    for b in range(m):
        for a in range(b):
            I[b]=max(I[b],I[a]+(1 if pos[a]<pos[b] else 0))
            D[b]=max(D[b],D[a]+(1 if pos[a]>pos[b] else 0))
    return max(I),max(D)
for m in range(3,10):
    best=0; arg=None; hist={}; mm=0; marg=None
    for rho in itertools.permutations(range(m)):
        i,d=ID(rho); s=i+d; hist[s]=hist.get(s,0)+1
        if s>best: best=s; arg=rho
        if min(i,d)>mm: mm=min(i,d); marg=rho
    print(f"m={m}: max I+D = {best} (m-1={m-1}) e.g. rho={[x+1 for x in arg]}; max min(I,D) = {mm} e.g. {[x+1 for x in marg]}; hist(I+D)={dict(sorted(hist.items()))}")
