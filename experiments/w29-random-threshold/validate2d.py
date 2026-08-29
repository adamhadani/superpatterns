"""W29 end-to-end check of Theorem 2.1/3.2: random pi in S_k, Poisson(C k^2) points in [0,1]^2,
run the gap-reserve greedy (mode 1 band, leftmost) on the actual points, verify the output is a copy of pi.
usage: python3 validate2d.py k h C w beta nrep seed"""
import sys, numpy as np
k,h=int(sys.argv[1]),int(sys.argv[2]); C=float(sys.argv[3]); w=float(sys.argv[4]); beta=float(sys.argv[5]); nrep=int(sys.argv[6]); rng=np.random.default_rng(int(sys.argv[7]))
def isect(lo,hi,y0,sh): return min(hi,y0+sh)-max(lo,y0-sh)
succ=0; costs=[]
for rep in range(nrep):
    pi=rng.permutation(k)                      # pi[p] = value at position p
    N=rng.poisson(C*k*k); X=rng.random(N); Y=rng.random(N); order=np.argsort(X); X=X[order]; Y=Y[order]
    a=-1.0; ystrip={}; ok=True; chosen=[]
    for p in range(k):
        v=pi[p]; j=v//h; base=j*h; vv=v-base
        placed=ystrip.setdefault(j,{})            # local value -> scaled y' in [0,h)
        L=vv-1
        while L>=0 and L not in placed: L-=1
        R=vv+1
        while R<h and R not in placed: R+=1
        yL=0.0 if L<0 else placed[L]; yR=float(h) if R>=h else placed[R]
        mb=vv-L-1; ma=R-vv-1; lo=yL+beta*mb; hi=yR-beta*ma
        y0=yL+(yR-yL)*(mb+0.5)/(mb+ma+1); sh=w/2
        if isect(lo,hi,y0,sh)<beta:
            s1,s2=sh,(hi-lo)+abs(y0-lo)+abs(hi-y0)+1
            for _ in range(60):
                sm=0.5*(s1+s2)
                if isect(lo,hi,y0,sm)<beta: s1=sm
                else: s2=sm
            sh=s2
        wa=max(lo,y0-sh); wb=min(hi,y0+sh)
        # window in unscaled y: strip bottom j*h/k, y' = k*y - j*h
        ya=(wa+j*h)/k; yb=(wb+j*h)/k
        i0=np.searchsorted(X,a,side='right')
        idx=np.nonzero((Y[i0:]>ya)&(Y[i0:]<yb))[0]
        if len(idx)==0: ok=False; break
        q=i0+idx[0]; a=X[q]; placed[vv]=Y[q]*k-j*h; chosen.append(q)
    if ok:
        ys=np.array([Y[q] for q in chosen]); xs=np.array([X[q] for q in chosen])
        assert np.all(np.diff(xs)>0)
        # y-order must equal pi: rank of ys == pi
        assert np.array_equal(np.argsort(np.argsort(ys)),pi), "NOT A COPY"
        succ+=1
print(f"k={k} h={h} C={C} w={w} beta={beta}: success {succ}/{nrep}")
