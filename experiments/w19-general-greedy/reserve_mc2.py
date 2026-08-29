import numpy as np
exec(open('reserve_mc.py').read().split('best=None')[0])
for C in [0.6,0.7,0.75,0.8]:
    for beta in [0.3,0.5,0.7]:
        for lam in [0.25,0.5,0.75]:
            means={h:strip_total(C,h,beta,lam,100000).mean()/h for h in range(1,8)}
            pred=sum(f*means[h] for h,f in freq.items() if h<=7)+sum(f for h,f in freq.items() if h>7)*means[7]
            print("C=%.2f beta=%.2f lam=%.2f  E[T_h]/h: %s  random-pi mean/value=%.4f"%(C,beta,lam," ".join("%.3f"%means[h] for h in range(1,8)),pred))
