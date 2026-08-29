"""Exact f(k;r): shortest word over [r] containing every k-permutation as a pattern.
SAT encoding (pysat/CaDiCaL). Usage: python fkr_sat.py k r [nmin] [nmax]"""
import sys, itertools, time
from pysat.solvers import Cadical153
from pysat.card import CardEnc

def contains_all(w, k, r):
    """independent checker: word w over [r] contains all pi in S_k as patterns"""
    for pi in itertools.permutations(range(1,k+1)):
        ok=False
        for s in itertools.combinations(range(1,r+1), k):
            t=[s[p-1] for p in pi]; j=0
            for c in w:
                if j<k and c==t[j]: j+=1
            if j==k: ok=True; break
        if not ok: return False, pi
    return True, None

def solve(k, r, n, symbreak=True):
    perms=list(itertools.permutations(range(1,k+1)))
    injs=list(itertools.combinations(range(1,r+1), k))
    cnt=[0]
    def new():
        cnt[0]+=1; return cnt[0]
    x=[[new() for l in range(r+1)] for i in range(n)]  # x[i][l], l in 1..r
    S=Cadical153()
    for i in range(n):
        lits=[x[i][l] for l in range(1,r+1)]
        S.add_clause(lits)
        for a in range(len(lits)):
            for b in range(a+1,len(lits)): S.add_clause([-lits[a],-lits[b]])
    if symbreak:
        # complement symmetry: first letter <= ceil(r/2)
        for l in range((r+1)//2+1, r+1): S.add_clause([-x[0][l]])
    TRUE=new(); S.add_clause([TRUE])
    for pi in perms:
        finals=[]
        for s in injs:
            t=[s[p-1] for p in pi]
            # R[i][j]: t[:j] embeds in w[:i]; only j in [max(0,k-(n-i)), min(i,k)]
            prev={0:TRUE}
            for i in range(1,n+1):
                cur={}
                lo=max(0,k-(n-i)); hi=min(i,k)
                for j in range(lo,hi+1):
                    if j==0: cur[0]=TRUE; continue
                    v=new(); cur[j]=v
                    a=prev.get(j); b=prev.get(j-1)
                    # v -> a or (b and x[i-1][t[j-1]])
                    c1=[-v]; c2=[-v]
                    if a is not None: c1.append(a); c2.append(a)
                    if b is not None:
                        c1.append(b); c2.append(x[i-1][t[j-1]])
                    S.add_clause(c1); S.add_clause(c2)
                prev=cur
            finals.append(prev[k])
        S.add_clause(finals)
    t0=time.time(); res=S.solve(); dt=time.time()-t0
    w=None
    if res:
        m=set(v for v in S.get_model() if v>0)
        w=[next(l for l in range(1,r+1) if x[i][l] in m) for i in range(n)]
    S.delete()
    return res, w, dt, cnt[0]

if __name__=="__main__":
    k=int(sys.argv[1]); r=int(sys.argv[2])
    nmin=int(sys.argv[3]) if len(sys.argv)>3 else k
    nmax=int(sys.argv[4]) if len(sys.argv)>4 else 100
    for n in range(nmin,nmax+1):
        res,w,dt,nv=solve(k,r,n)
        print(f"k={k} r={r} n={n}: {'SAT' if res else 'UNSAT'} ({dt:.1f}s, {nv} vars)", flush=True)
        if res:
            ok,bad=contains_all(w,k,r)
            print("  witness:", "".join(map(str,w)) if r<10 else w, "verified" if ok else f"CHECK FAILED {bad}", flush=True)
            break
