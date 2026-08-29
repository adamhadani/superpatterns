# rate function of Theorem A (iid model): rho(C) = ln2 - sup_b [H(b) + b ln(4e/(bC))]
import math
def H(b): return 0 if b in (0,1) else -b*math.log(b)-(1-b)*math.log(1-b)
def g(b,C): return H(b)+b*math.log(4*math.e/(b*C)) if b>0 else 0.0
def sup(C):
    bs=[i/100000 for i in range(1,100000)]+[1.0]
    return max(g(b,C) for b in bs)
def rho(C): return math.log(2)-sup(C)
# threshold
lo,hi=1.0,1000.0
for _ in range(60):
    mid=(lo*hi)**.5
    if rho(mid)>0: hi=mid
    else: lo=mid
print("C_0 =",hi)
for C in [20,27.4,30,40,50,75,100,200,500,1000,1e4]:
    print(C, round(rho(C),4))
