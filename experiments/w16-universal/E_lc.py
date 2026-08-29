# E_k(N) = E#leftmost-canonical copies (pattern-independent, W12 Prop 3) by Monte Carlo on the gap simplices.
import numpy as np, math, sys
rng=np.random.default_rng(1)
def Ek(k,N,M=400000):
    g=rng.exponential(size=(M,k+1)); g/=g.sum(1,keepdims=True); g=g[:,:k]
    h=rng.exponential(size=(M,k+1)); h/=h.sum(1,keepdims=True)
    Q=(g*(h[:,:-1]+h[:,1:])).sum(1)
    w=np.exp(-N*Q); m=w.mean(); se=w.std()/math.sqrt(M)
    logpref=k*math.log(N)-2*math.lgamma(k+1)
    return math.exp(logpref)*m, math.exp(logpref)*se, math.exp(logpref)
if __name__=="__main__":
    for k,Ns in [(8,[16,20,24,28,32]),(10,[26,30,34,38,42]),(12,[36,42,48,54,60]),(14,[50,56,62,68,74]),(16,[62,70,78,86,94]),(20,[100,110,120,130,140])]:
        for N in Ns:
            e,se,fm=Ek(k,N); print("k=%d N=%d  E_lc=%.4g (+-%.2g)   E#copies=%.4g"%(k,N,e,se,fm))
