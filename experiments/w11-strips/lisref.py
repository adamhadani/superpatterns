import random,bisect,sys
def lis(N):
    t=[]
    for _ in range(N):
        y=random.random(); i=bisect.bisect_left(t,y)
        if i==len(t): t.append(y)
        else: t[i]=y
    return len(t)
random.seed(1)
for k in [8,16,32,36,49,64,100,144,256]:
    # find C with Pr(LIS_N >= k) ~ 1/2 by bisection on C with 400 samples
    lo,hi=0.15,0.6
    for it in range(9):
        C=(lo+hi)/2; N=int(C*k*k); reps=300 if k<=100 else 150
        p=sum(lis(N)>=k for _ in range(reps))/reps
        if p<0.5: lo=C
        else: hi=C
    print(f"identity k={k}: C_1/2 ~ {(lo+hi)/2:.3f}",flush=True)
