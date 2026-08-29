import sys
from zig import count
def inverse(p):
    inv=[0]*len(p)
    for i,v in enumerate(p): inv[v-1]=i+1
    return inv
def min_mono_partition(seq, allow=("inc","dec")):
    """greedy min partition of seq into contiguous monotone pieces (directions in allow). returns list of (len,dir)"""
    res=[]; i=0; n=len(seq)
    while i<n:
        best=1; bd="inc"
        for d in allow:
            j=i+1
            while j<n and ((seq[j]>seq[j-1]) if d=="inc" else (seq[j]<seq[j-1])): j+=1
            if j-i>best or (j-i==best and bd=="inc"): best=j-i; bd=d
        res.append((best,bd)); i+=best
    return res
def word_of(p, parts):
    """letters = interval index; returns word and direction per letter"""
    lab=[0]*(len(p)+1); v=1
    dirs=[]
    for L,d in parts:
        for t in range(L): lab[v+t]=len(dirs)+1
        dirs.append(d); v+=L
    return [lab[x] for x in p], dirs
def blocks(word):
    """greedy split into maximal segments with distinct letters"""
    out=[]; cur=[]
    for x in word:
        if x in cur: out.append(cur); cur=[x]
        else: cur.append(x)
    out.append(cur); return out
def syms(p):
    n=len(p); rev=p[::-1]; comp=[n+1-x for x in p]; rc=[n+1-x for x in rev]
    base={"id":p,"rev":rev,"comp":comp,"rc":rc}
    out={}
    for name,q in base.items():
        out[name]=q; out[name+"^-1"]=inverse(q)
    return out
def analyze(k,p,label):
    n=len(p); print(f"=== {label}: k={k}, n={n}")
    best=None
    for name,q in syms(p).items():
        inv=inverse(q)
        for allow in (("dec",),("inc",),("inc","dec")):
            parts=min_mono_partition(inv,allow)
            w,dirs=word_of(q,parts)
            bl=blocks(w)
            key=(len(parts),len(bl))
            print(f"  {name:8s} allow={'/'.join(allow):7s} letters={len(parts):2d} sizes={[L for L,_ in parts]} blocks(distinct-letter greedy)={[len(b) for b in bl]}")
            if best is None or key<best[0]: best=(key,name,allow,w,dirs,bl)
    key,name,allow,w,dirs,bl=best
    print(f"  BEST: {name} allow={allow} letters={key[0]} word={' '.join(map(str,w))} dirs={''.join(d[0] for d in dirs)}")
    print(f"        blocks: {bl}")
W={
 "sp7a":(7,[7,20,13,10,2,18,23,4,12,16,8,5,19,15,1,9,22,14,6,17,11,3,21]),
 "sp7b":(7,[7,18,12,2,15,23,6,19,13,4,8,11,22,17,3,20,10,5,14,1,21,9,16]),
 "sp7c":(7,[10,16,2,22,6,11,19,15,5,21,12,1,9,18,4,13,23,7,17,3,14,20,8]),
 "sp8_30":(8,[13,4,25,18,8,30,12,22,1,28,19,10,6,14,24,27,3,16,21,11,5,20,29,15,7,23,2,17,26,9]),
 "sp8_31":(8,[25,21,11,4,27,8,17,19,1,13,31,5,23,16,26,10,6,29,15,20,28,3,9,14,24,2,12,30,18,7,22]),
 "arnarson":(6,[6,14,10,2,13,17,5,8,3,12,9,16,1,7,11,4,15]),
 "mine24":(7,[9,21,3,15,6,24,12,18,5,11,23,2,14,8,17,20,4,10,19,13,1,22,7,16]),
}
for lab,(k,p) in W.items():
    if lab.startswith("sp7") or lab=="sp8_30": print(lab,"verify:",count(k,p))
    analyze(k,p,lab)
