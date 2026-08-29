"""Row-structure analysis of record superpatterns.
Rows = intervals of values.  Row pattern rho_l = pattern of the values of row l read in position order.
1. DP: for m = k+1..k+5 rows (size cap S), the minimum number of NON-monotone rows over all interval partitions.
2. For the chosen partition (fewest rows subject to size cap), run ./fibres to get for every k-pattern
   tot / mono embedding counts; report the patterns that have NO all-monotone-fibre embedding.
3. For hard patterns, list the fibre patterns actually used.
usage: python3 rows.py            (analyses the witness table W)
"""
import sys, subprocess, itertools
from math import factorial
W={
 "sp7a":(7,[7,20,13,10,2,18,23,4,12,16,8,5,19,15,1,9,22,14,6,17,11,3,21]),
 "sp7b":(7,[7,18,12,2,15,23,6,19,13,4,8,11,22,17,3,20,10,5,14,1,21,9,16]),
 "sp7c":(7,[10,16,2,22,6,11,19,15,5,21,12,1,9,18,4,13,23,7,17,3,14,20,8]),
 "sp8_30":(8,[13,4,25,18,8,30,12,22,1,28,19,10,6,14,24,27,3,16,21,11,5,20,29,15,7,23,2,17,26,9]),
 "arnarson17":(6,[6,14,10,2,13,17,5,8,3,12,9,16,1,7,11,4,15]),
}
def pattern(seq):
    s=sorted(seq); return tuple(s.index(x)+1 for x in seq)
def is_mono(seq):
    return all(a<b for a,b in zip(seq,seq[1:])) or all(a>b for a,b in zip(seq,seq[1:]))
def row_pattern(p,a,b):
    """values a..b of permutation p: pattern of these values in position order"""
    pos={v:i for i,v in enumerate(p)}
    seq=sorted(range(a,b+1),key=lambda v:pos[v])
    return pattern(seq)
def dp_partitions(p,S):
    n=len(p); INF=10**9
    # f[m][b]: min #nonmono rows partitioning values 1..b into m intervals of size<=S
    f=[[INF]*(n+1) for _ in range(n+2)]; back=[[None]*(n+1) for _ in range(n+2)]
    f[0][0]=0
    for m in range(1,n+1):
        for b in range(1,n+1):
            for a in range(max(1,b-S+1),b+1):
                if f[m-1][a-1]<INF:
                    c=f[m-1][a-1]+(0 if is_mono(rowseq(p,a,b)) else 1)
                    if c<f[m][b]: f[m][b]=c; back[m][b]=a
    def recover(m):
        rows=[]; b=n
        while m>0:
            a=back[m][b]; rows.append((a,b)); b=a-1; m-=1
        return rows[::-1]
    return f,recover
def rowseq(p,a,b):
    pos={v:i for i,v in enumerate(p)}
    return sorted(range(a,b+1),key=lambda v:pos[v])
def unrank(r,k):
    # Lehmer code c_i = #later smaller, r = sum c_i (k-1-i)!
    c=[];
    for i in range(k):
        f=factorial(k-1-i); c.append(r//f); r%=f
    avail=list(range(1,k+1)); out=[]
    for ci in c: out.append(avail.pop(ci))
    return tuple(out)
def rank(t):
    k=len(t); return sum(sum(1 for j in range(i+1,k) if t[j]<t[i])*factorial(k-1-i) for i in range(k))
def hard_patterns(k):
    H={}
    H["id"]=tuple(range(1,k+1)); H["dec"]=tuple(range(k,0,-1))
    ud=[];
    for i in range(k): ud.append(i+1)
    # alternating up-down 1 3 2 5 4 ...
    a=list(range(1,k+1))
    for i in range(1,k-1,2): a[i],a[i+1]=a[i+1],a[i]
    H["alt_ud"]=tuple(a)
    b=list(range(1,k+1))
    for i in range(0,k-1,2): b[i],b[i+1]=b[i+1],b[i]
    H["alt_du"]=tuple(b)
    # layered: layers of size 2, of size 3, and (k-1,1),(1,k-1)
    def layered(sizes):
        out=[]; v=1
        for s in sizes: out+= list(range(v+s-1,v-1,-1)); v+=s
        return tuple(out)
    H["lay2"]=layered([2]*(k//2)+([1] if k%2 else []))
    H["lay3"]=layered([3]*(k//3)+([k%3] if k%3 else []))
    H["lay_k-1,1"]=layered([k-1,1]); H["lay_1,k-1"]=layered([1,k-1])
    return H
def embeddings(k,p,tau):
    """all index tuples of p order-isomorphic to tau (DFS with pruning)"""
    n=len(p); res=[]
    inv=sorted(range(k),key=lambda i:tau[i])  # not needed
    def rec(i,chosen):
        if i==k: res.append(tuple(chosen)); return
        start=chosen[-1]+1 if chosen else 0
        for q in range(start,n-(k-i)+1):
            v=p[q]; ok=True
            for j,c in enumerate(chosen):
                if (p[c]<v)!=(tau[j]<tau[i]): ok=False; break
            if ok: rec(i+1,chosen+[q])
    rec(0,[]); return res
def analyse(name,k,p,S=4,mlist=None):
    n=len(p); print(f"\n===== {name}: k={k} n={n}  (row size cap S={S})")
    f,recover=dp_partitions(p,S)
    # unconstrained monotone-only min rows (S=n) for reference
    fm,_=dp_partitions(p,n)
    mono_min=min(m for m in range(1,n+1) if fm[m][n]==0)
    print(f"  min #rows with ALL rows monotone (any size): {mono_min}   [k+1={k+1}]")
    print("  m rows -> min #non-monotone rows (size<=%d):"%S, {m:f[m][n] for m in range(max(1,(n+S-1)//S),mono_min+1) if f[m][n]<10**9})
    if mlist is None: mlist=[k+2]
    for m in mlist:
        if f[m][n]>=10**9: print(f"  m={m}: infeasible with S={S}"); continue
        rows=recover(m); pats=[row_pattern(p,a,b) for a,b in rows]
        rowid=[0]*(n+1)
        for l,(a,b) in enumerate(rows):
            for v in range(a,b+1): rowid[v]=l+1
        word=[rowid[v] for v in p]
        print(f"  m={m}: rows={rows}")
        print(f"        row patterns={[''.join(map(str,x)) for x in pats]}  nonmono={f[m][n]}")
        print(f"        word over [{m}] = {' '.join(map(str,word))}")
        out=subprocess.run(["./fibres",str(k),str(n)]+[str(x) for x in p]+[str(rowid[v]) for v in range(1,n+1)],capture_output=True,text=True).stdout.splitlines()
        print("        fibres:",out[0])
        need=[];
        for line in out[1:]:
            r,t,mo=map(int,line.split())
            if t>0 and mo==0: need.append(unrank(r,k))
        print(f"        #patterns whose EVERY embedding uses a non-monotone fibre: {len(need)}")
        if need: print("        e.g.:",[''.join(map(str,t)) for t in need[:12]])
        # hard patterns
        H=hard_patterns(k)
        for hn,tau in H.items():
            E=embeddings(k,p,tau)
            fibstats={}
            nonmono_needed=True
            for e in E:
                vals=[p[q] for q in e]
                groups={}
                for q in e: groups.setdefault(rowid[p[q]],[]).append(p[q])
                fps=tuple(sorted(''.join(map(str,pattern(g))) for g in groups.values() if len(g)>1))
                fibstats[fps]=fibstats.get(fps,0)+1
                if all(is_mono(g) for g in groups.values()): nonmono_needed=False
            top=sorted(fibstats.items(),key=lambda x:-x[1])[:4]
            print(f"        {hn:10s} {''.join(map(str,tau))}: {len(E):5d} embeddings; needs nonmono fibre: {nonmono_needed}; fibre-multisets(top): {top}")
if __name__=="__main__":
    names=sys.argv[1:] or list(W)
    for nm in names:
        k,p=W[nm]
        analyse(nm,k,p,S=4,mlist=[k+1,k+2,k+3])
