import sys, itertools
from zig import tiebreak
def contained(tau, sig):
    k=len(tau); n=len(sig)
    # DP: for each prefix, set of position tuples is too big; use recursive search with pruning
    # simple: order-isomorphic subsequence search via recursion over positions with value constraints
    import functools
    idx=sorted(range(k), key=lambda i:tau[i])
    # brute force over subsets using itertools would be C(24,7)=346k -- fine
    for comb in itertools.combinations(range(n),k):
        vals=[sig[i] for i in comb]
        ok=True
        for a in range(k):
            for b in range(a+1,k):
                if (vals[a]<vals[b]) != (tau[a]<tau[b]): ok=False;break
            if not ok: break
        if ok: return True
    return False
k=int(sys.argv[1]); w=[int(x) for x in sys.argv[2:]]
p=tiebreak(w,dec=True)
# faster: enumerate all subsets once, mark patterns
seen=set()
n=len(p)
for comb in itertools.combinations(range(n),k):
    vals=[p[i] for i in comb]; s=sorted(vals); pat=tuple(s.index(v)+1 for v in vals); seen.add(pat)
miss=[t for t in itertools.permutations(range(1,k+1)) if t not in seen]
print(len(seen),"missing:",miss)
