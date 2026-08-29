import math
def H(b): return 0 if b in (0,1) else -b*math.log(b)-(1-b)*math.log(1-b)
def rho(C,r):
    cap=math.log(r/(r-1))
    bs=[i/20000 for i in range(1,20001)]
    return cap-max(H(b)+b*cap+b*math.log(r*math.e/(b*C)) for b in bs)
for r in [2,3,4,6,8]:
    lo,hi=1.0,1e7
    for _ in range(80):
        mid=(lo*hi)**.5
        if rho(mid,r)>0: hi=mid
        else: lo=mid
    print("r=",r,"C_0(r)=",round(hi,1),"rho at 2C_0, 10C_0:",round(rho(2*hi,r),4),round(rho(10*hi,r),4),"cap",round(math.log(r/(r-1)),4))
