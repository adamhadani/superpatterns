import subprocess, sys, itertools
def z_word(k, m=None, runs=None):
    """first `runs` runs of infinite zigzag restricted to [m]. default m=k, runs=k (EV z_k)."""
    m = m or k; runs = runs or k
    w=[]
    for r in range(1,runs+1):
        if r%2==1: w += [x for x in range(1,m+1,2)]
        else: w += [x for x in range(m - (m%2==1), 0, -2)]   # evens descending
    return w
def tiebreak(w, dec=True):
    """turn word into permutation: equal letters -> decreasing subsequence (EV) if dec else increasing"""
    n=len(w); idx=sorted(range(n), key=lambda i:(w[i], -i if dec else i))
    p=[0]*n
    for rank,i in enumerate(idx): p[i]=rank+1
    return p
def count(k, w):
    out=subprocess.run(["./check",str(k),str(len(w))]+[str(x) for x in w],capture_output=True,text=True).stdout.split()
    return int(out[0]), int(out[1])
def zeta(k):
    w=z_word(k); p=tiebreak(w)
    if k%2==0: p=[len(p)+1]+p   # prepend a new maximum
    return p
if __name__=="__main__":
    for k in range(3,9):
        p=zeta(k); c,t=count(k,p); print(k,len(p),c,t)
