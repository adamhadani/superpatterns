import numpy as np
from math import lgamma, log, exp
from finite_check import bound_rate
for k in [10001,30001,100001]:
    for lam in [1.004,1.0048]:
        n=int(lam*k*k/np.e**2); th=0.9774*np.e**2/lam; x=exp(-th/k)
        logpref=-(n+1)*log(x)+(k+1)*log(x/(1-x)); P0=(logpref-lgamma(k+1))/k
        P0cont=0.9774-1-log(0.9774)+log(lam)
        r,info=bound_rate(k,lam,0.9774,0.5936,0.149)
        print(f"k={k} lam={lam}: P0={P0:+.6f} (cont {P0cont:+.6f})  logEWgood/k={log(info['EWgood'])/k:+.6f}  logBad/k={log(info['Bad'])/k:+.6f}  total={r:+.6f}",flush=True)
