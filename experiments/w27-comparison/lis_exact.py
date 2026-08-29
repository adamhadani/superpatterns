# exact Pr(LIS(sigma_n) < k) = sum over shapes with lambda_1 <= k-1 of (f^lambda)^2 / n!
import sys
from fractions import Fraction
from math import factorial
from functools import lru_cache
def parts(n,maxpart,maxlen=None):
    if n==0: yield (); return
    for p in range(min(n,maxpart),0,-1):
        for rest in parts(n-p,p): yield (p,)+rest
def hook(lam):
    n=sum(lam); conj=[sum(1 for l in lam if l>j) for j in range(lam[0])]
    h=1
    for i,l in enumerate(lam):
        for j in range(l): h*= (l-j-1)+(conj[j]-i-1)+1
    return factorial(n)//h
k=int(sys.argv[1]); nmax=int(sys.argv[2])
import math
for n in range(1,nmax+1):
    tot=sum(hook(l)**2 for l in parts(n,k-1))
    p=Fraction(tot,factorial(n))
    print(n, float(p), math.log(p) if p>0 else float('-inf'))
