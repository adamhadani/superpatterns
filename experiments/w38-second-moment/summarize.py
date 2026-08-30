# W38 summarize.py: tables of ln R_avg (plain) and ln R_can (canonical) vs k, per C, from out/*.txt
import re,glob,sys
from math import log
Cs=['0.15','0.2','0.25','0.3','0.5','1']; ks=range(4,11)
def grab(fn,pat):
    try: s=open(fn).read()
    except FileNotFoundError: return None
    m=re.search(pat,s); return m.groups() if m else None
print("PLAIN: ln R_avg (pairs MC; exact in brackets)  [R = E_pi E M^2 / mu^2]")
print("k    "+"  ".join(f"C={C:>5}" for C in Cs))
for k in ks:
    row=[]
    for C in Cs:
        g=grab(f"out/pairs_k{k}_C{C}.txt",r"R_avg=([\d.]+) \+- ([\d.]+)")
        e=grab(f"out/exact_k{k}_C{C}.txt",r"R_avg=([\d.]+) \+- ([\d.]+)")
        if g: R,se=float(g[0]),float(g[1]); s=f"{log(R):5.2f}±{se/R:.2f}"
        else: s="   --    "
        if e: s+=f"[{log(float(e[0])):.2f}]"
        row.append(s)
    print(f"{k:<3}  "+"  ".join(f"{x:<16}" for x in row))
print("\nCANONICAL: ln R_can (pairs_can MC; exact_can in brackets)  [R_can = E_pi E Y^2/(E Y)^2]")
print("k    "+"  ".join(f"C={C:>5}" for C in Cs))
for k in ks:
    row=[]
    for C in Cs:
        g=grab(f"out/pairscan_k{k}_C{C}.txt",r"R_can=([\d.]+) \+- ([\d.]+)")
        e=grab(f"out/exactcan_k{k}_C{C}.txt",r"R_can=([\d.]+) \+- ([\d.]+)")
        if g: R,se=float(g[0]),float(g[1]); s=f"{log(R):5.2f}±{se/R:.2f}"
        else: s="   --    "
        if e: s+=f"[{log(float(e[0])):.2f}]"
        row.append(s)
    print(f"{k:<3}  "+"  ".join(f"{x:<16}" for x in row))
print("\nq = Pr(A canonical) and E Y_pi (exact_can) ; Pr(contained) = Edistinct/k! ; 1/R bounds")
for k in ks:
    for C in Cs:
        e=grab(f"out/exactcan_k{k}_C{C}.txt",r"mu=([\d.e+-]+) \| plain R_avg=([\d.]+).*q=E\[Y_tot\]/binom=([\d.e+-]+) EY_pi=([\d.e+-]+) R_can=([\d.]+).*Edistinct_can/k!=([\d.]+)")
        if e: print(f"k={k} C={C}: mu={float(e[0]):.3g} EY={float(e[3]):.3g} q={float(e[2]):.3g}  Pr(pi in sigma)={float(e[5]):.4f}  1/R_avg={1/float(e[1]):.4f}  1/R_can={1/float(e[4]):.4f}")
