"""Brute-force verification of the combinatorial claims in proof.md Theorems 4-5 and Lemma 3."""
import numpy as np, sys
sys.path.insert(0,'../w9-alon-threads')
from threads import tilted_grid, run_thread
from joint import log_binom_tail
from math import exp, log, lgamma
rng = np.random.default_rng(7)

def f(N,K): return exp(log_binom_tail(N,K))
# Lemma 3
bad=0
for N in range(3,200):
    for K in range(1,N//3+1):
        if N>=3*K-1 and f(N-1,K-1) < (K/N)*f(N,K)-1e-12: bad+=1
print("Lemma 3 violations (N<200):", bad)

def prescribe_G(pi, r, h, e):
    """Theorem 4: cells of G, as dict (row,col)->val; checks consistency and count 4*lam-1."""
    lam = e*r; cells={}
    def put(y,x,v):
        if (y,x) in cells and cells[(y,x)]!=v: raise RuntimeError("inconsistent")
        cells[(y,x)]=v
    for a in range(2*lam): put(pi[a], a, 1)
    for b in range(lam): put(pi[b]+e, 2*b, 0); put(pi[b]+e, 2*b+1, 1)
    assert len(cells)==4*lam-1, (len(cells), 4*lam-1)
    return cells

def prescribe_Gp(pi, r, h, e):
    """Theorem 5: cells of G' ; count 2*mu+2."""
    mu=(h-e)*r-1; cells={}
    def put(y,x,v):
        if (y,x) in cells and cells[(y,x)]!=v: raise RuntimeError("inconsistent")
        cells[(y,x)]=v
    for b in range(mu+1): put(pi[b]+e, b, 1)
    put(pi[0],0,1)
    for x in range(1,mu+1): put(pi[1],x,0)
    assert pi[1]==h and pi[0]==0
    assert len(cells)==2*mu+2, (len(cells), 2*mu+2)
    return cells

viol=0; trials=0; both=0
for (r,h) in [(4,4),(4,8),(8,8),(6,12),(12,8)]:
    pi=tilted_grid(r) if r==h else None
    if pi is None:
        k=r*h; pi=np.empty(k,dtype=int)
        for i in range(h):
            for s in range(r): pi[i*r+s]=s*h+i
    k=r*h; q=2*k
    for e in range(1, h//4+1):
        cells=prescribe_G(pi,r,h,e); lam=e*r
        for C in (1.15,1.3,1.6):
            m=int(C*k)
            for _ in range(300):
                M=rng.integers(0,2,size=(q,m),dtype=np.int8)
                for (y,x),v in cells.items(): M[y,x]=v
                T0=run_thread(M,pi,'H',0); T1=run_thread(M,pi,'H',e)
                trials+=1
                # coalescence check: leader at column 2lam seeks element 2lam, follower seeks lam
                assert T0['cells'][2*lam]==(pi[2*lam],2*lam) and T0['elems'][2*lam]==2*lam
                assert T1['cells'][2*lam]==(pi[2*lam],2*lam) and T1['elems'][2*lam]==lam
                if not T0['ok']:
                    both+=1
                    if T1['ok']: viol+=1
print(f"Theorem 4: trials {trials}, leader failed {both}, follower succeeded while leader failed: {viol}")

viol=0; trials=0; both=0; cnt_fail_le=0
for (r,h) in [(4,4),(4,8),(8,8),(6,12),(12,8)]:
    k=r*h; pi=np.empty(k,dtype=int)
    for i in range(h):
        for s in range(r): pi[i*r+s]=s*h+i
    q=2*k
    for e in range((3*h)//4, h):
        mu=(h-e)*r-1; cells=prescribe_Gp(pi,r,h,e)
        for C in (1.15,1.3,1.6):
            m=int(C*k)
            for _ in range(300):
                M=rng.integers(0,2,size=(q,m),dtype=np.int8)
                for (y,x),v in cells.items(): M[y,x]=v
                # G'': at gap elements a = i*r (1<=i<=e-1) force leader's first cell and follower's first cell = 1.
                # These are read at column X_a; emulate by running the leader, then forcing, iteratively.
                # Simpler: force cells adaptively: run leader; for each gap element a, set M[pi[a], X_a]=1 and
                # M[pi[a+mu]+e, X_a]=1, rerun (X_a for earlier elements unchanged since forcing only affects later columns).
                for i in range(1,e):
                    a=i*r
                    T0=run_thread(M,pi,'H',0)
                    idx=[j for j,el in enumerate(T0['elems']) if el==a]
                    if not idx: break
                    Xa=T0['cells'][idx[0]][1]
                    M[pi[a],Xa]=1; M[pi[a+mu]+e,Xa]=1
                    assert pi[a+mu]+e>=k
                T0=run_thread(M,pi,'H',0); T1=run_thread(M,pi,'H',e)
                trials+=1
                # sync check: at column mu+1 both in row h
                assert T0['cells'][mu+1]==(h,mu+1) and T0['elems'][mu+1]==1
                assert T1['cells'][mu+1]==(h,mu+1) and T1['elems'][mu+1]==mu+1
                if T0['ones'] <= e*r-1:
                    cnt_fail_le+=1
                    if T1['ok'] or T0['ok']: viol+=1
print(f"Theorem 5: trials {trials}, leader had <= er-1 ones in {cnt_fail_le} cases, violations (either thread succeeded): {viol}")
