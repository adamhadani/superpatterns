from zig import count, tiebreak
import sys
def compress(k,p,name):
    n=len(p); full=count(k,p)[1]
    print(f"{name}: n={n}")
    # per-position loss
    loss=[full-count(k,p[:i]+p[i+1:])[0] for i in range(n)]
    print("  patterns lost by deleting position i:",loss)
    # greedy merge of adjacent value pairs v,v+1 -> same letter (as a word with ties, order of ties = as in p)
    w=list(p)
    merged=True
    while merged:
        merged=False
        vals=sorted(set(w))
        for a,b in zip(vals,vals[1:]):
            w2=[a if x==b else x for x in w]
            if count(k,w2)[0]==full:
                w=w2; merged=True; break
    vals=sorted(set(w)); relabel={v:i+1 for i,v in enumerate(vals)}
    w=[relabel[x] for x in w]
    print(f"  compressible to alphabet {len(vals)}: word = {' '.join(map(str,w))}")
    # tie structure: for each letter, the pattern of its copies in p
    for v in range(1,len(vals)+1):
        pos=[i for i in range(n) if w[i]==v]
        if len(pos)>1:
            pv=[p[i] for i in pos]; print(f"    letter {v}: positions {[i+1 for i in pos]} original values {pv}")
    return w
A=[6,14,10,2,13,17,5,8,3,12,9,16,1,7,11,4,15]
compress(6,A,"Arnarson")
from zig import zeta
compress(7,zeta(7),"zeta_7")
