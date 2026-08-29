import sys, itertools, statistics
def is_layered(p):  # sum of decreasing blocks
    n=len(p); i=0
    while i<n:
        j=i
        while j+1<n and p[j+1]==p[j]-1: j+=1
        if p[i]!=j+1: return False   # block must be values j+1 ... i+1 descending in positions i..j
        i=j+1
    return True
def comp(p): return [len(p)+1-x for x in p]
def sum_indec(p):
    n=len(p); mx=0
    for i in range(n-1):
        mx=max(mx,p[i])
        if mx==i+1: return False
    return True
def classify(p):
    n=len(p)
    if p==sorted(p) or p==sorted(p,reverse=True): return 'monotone'
    if is_layered(p): return 'layered'
    if is_layered(comp(p)): return 'co-layered'
    if not sum_indec(p): return 'sum-decomp (other)'
    if not sum_indec(comp(p)): return 'skew-decomp (other)'
    return 'indecomposable'
for fn in sys.argv[1:]:
    rows=[]
    for line in open(fn):
        a=line.split(); rows.append((int(a[0]),tuple(int(x) for x in a[1:])))
    tot=sum(c for c,_ in rows); N=len(rows)
    print("==",fn," patterns=",N," total misses=",tot, " mean=",tot/N)
    byc={}
    for c,p in rows: byc.setdefault(classify(p),[]).append(c)
    for k,v in sorted(byc.items(), key=lambda kv:-statistics.mean(kv[1])):
        print(f"  {k:22s} count={len(v):5d}  mean_miss={statistics.mean(v):8.2f}  ratio_to_avg={statistics.mean(v)/(tot/N):5.2f}")
    rows.sort(key=lambda r:-r[0])
    print("  top 25:")
    for c,p in rows[:25]: print("   ",c," ".join(map(str,p)),"  ",classify(p))
    # rank of monotone
    for i,(c,p) in enumerate(rows):
        if classify(p)=='monotone': print("   monotone",p,"rank",i+1,"miss",c)
