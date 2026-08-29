import sys; sys.path.insert(0,'../w9-alon-threads')
from threads import tilted_grid
from joint import joint2, log_binom_tail
from math import log
pi=tilted_grid(10); k=100; h=10
for C in (16,24):
    m=C*k; lf=log_binom_tail(m,k-1)
    pos=[(-lf-(joint2(pi,0,e,m)-2*lf))/(10*e) for e in (1,2,3,4)]
    neg=[(-lf-(joint2(pi,0,h-e,m)-2*lf))/(10*e-1) for e in (1,2,3)]
    print(f"C={C} -lf={-lf:.1f} pos rate {['%.3f'%x for x in pos]} neg rate {['%.3f'%x for x in neg]} lnC={log(C):.3f}")
