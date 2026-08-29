"""Exact r(n): shortest cyclic word over [n] such that every permutation of [n] is a
subsequence of some rotation. SAT (CaDiCaL). Usage: python rosary_sat.py n [rmin] [rmax]"""
import sys, itertools, time
from pysat.solvers import Cadical153

def is_rosary(w, n):
    r=len(w); ww=w+w
    for pi in itertools.permutations(range(1,n+1)):
        ok=False
        for j in range(r):
            if ww[j]!=pi[0]: continue
            m=1
            for i in range(j+1,j+r):
                if m<n and ww[i]==pi[m]: m+=1
            if m==n: ok=True; break
        if not ok: return False, pi
    return True, None

def solve(n, r, symbreak=True):
    perms=list(itertools.permutations(range(1,n+1)))
    cnt=[0]
    def new():
        cnt[0]+=1; return cnt[0]
    x=[[new() for l in range(n+1)] for i in range(r)]
    S=Cadical153()
    for i in range(r):
        lits=[x[i][l] for l in range(1,n+1)]
        S.add_clause(lits)
        for a in range(n):
            for b in range(a+1,n): S.add_clause([-lits[a],-lits[b]])
    if symbreak:
        # relabeling symmetry: letters first appear in order 1,2,...,n ; rotation: w[0]=1
        S.add_clause([x[0][1]])
        for i in range(r):
            for l in range(2,n+1):
                S.add_clause([-x[i][l]]+[x[ip][l-1] for ip in range(i)])
    TRUE=new(); S.add_clause([TRUE])
    for pi in perms:
        t=pi[1:]; k=n-1
        finals=[]
        for j in range(r):
            # embed t in w[j+1..j+r-1] cyclic (length r-1), conditioned on x[j][pi[0]]
            prev={0:TRUE}; L=r-1
            for i in range(1,L+1):
                pos=(j+i)%r
                cur={}
                lo=max(0,k-(L-i)); hi=min(i,k)
                for m in range(lo,hi+1):
                    if m==0: cur[0]=TRUE; continue
                    v=new(); cur[m]=v
                    a=prev.get(m); b=prev.get(m-1)
                    c1=[-v]; c2=[-v]
                    if a is not None: c1.append(a); c2.append(a)
                    if b is not None: c1.append(b); c2.append(x[pos][t[m-1]])
                    S.add_clause(c1); S.add_clause(c2)
                prev=cur
            f=new(); S.add_clause([-f, x[j][pi[0]]]); S.add_clause([-f, prev[k]])
            finals.append(f)
        S.add_clause(finals)
    t0=time.time(); res=S.solve(); dt=time.time()-t0
    w=None
    if res:
        m=set(v for v in S.get_model() if v>0)
        w=[next(l for l in range(1,n+1) if x[i][l] in m) for i in range(r)]
    S.delete()
    return res,w,dt,cnt[0]

if __name__=="__main__":
    n=int(sys.argv[1])
    rmin=int(sys.argv[2]) if len(sys.argv)>2 else n
    rmax=int(sys.argv[3]) if len(sys.argv)>3 else 200
    for r in range(rmin,rmax+1):
        res,w,dt,nv=solve(n,r)
        print(f"n={n} r={r}: {'SAT' if res else 'UNSAT'} ({dt:.1f}s, {nv} vars)", flush=True)
        if res:
            ok,bad=is_rosary(w,n)
            print("  witness:", "".join(map(str,w)), "verified" if ok else f"CHECK FAILED {bad}", flush=True)
            break
