import random
def ident(k): return list(range(1,k+1))
def randpats(k,m=8):
    random.seed(100+k); out=[]
    for j in range(m):
        p=list(range(1,k+1)); random.shuffle(p); out.append(("r%d_%d"%(k,j),p))
    return out
def layered(k):  # (21)^{k/2}
    p=[]
    for i in range(k//2): p+=[2*i+2,2*i+1]
    return p
def tilted(r):   # r x r grid rotated 45 deg: pos a*r+b -> value b*r+(r-1-a)+1 ; LIS = LDS = r
    return [b*r+(r-1-a)+1 for a in range(r) for b in range(r)]
def dechalf(k):  # first k/2 elements decreasing (values k..k/2+1), then a random permutation of 1..k/2 (seed k)
    random.seed(1000+k); rest=list(range(1,k//2+1)); random.shuffle(rest)
    return list(range(k,k//2,-1))+rest
def dec(k): return list(range(k,0,-1))
def s(p): return ",".join(map(str,p))
