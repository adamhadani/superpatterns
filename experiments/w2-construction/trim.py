from zig import *
import sys
for k in [5,6,7,8]:
    p=zeta(k); n=len(p)
    single=[i for i in range(n) if count(k,p[:i]+p[i+1:])[0]==count(k,p)[1]]
    print(f"k={k} n={n}: singly-deletable positions (1-based): {[i+1 for i in single]}  letters {[p[i] for i in single]}")
    # greedy: delete as many as possible, left to right and right to left
    for order in ["ltr","rtl"]:
        q=list(p); i_list=list(range(n)) if order=="ltr" else list(range(n-1,-1,-1))
        cur=list(p); removed=[]
        for i in i_list:
            trial=[x for j,x in enumerate(cur) if j!=i] if False else None
        # simpler: iterate over original positions, maintain mask
        mask=[True]*n
        for i in i_list:
            mask[i]=False
            w=[p[j] for j in range(n) if mask[j]]
            if count(k,w)[0]!=count(k,p)[1]: mask[i]=True
            else: removed.append(i+1)
        print(f"   greedy {order}: removed {len(removed)} positions {removed}; final length {n-len(removed)}")
    sys.stdout.flush()
