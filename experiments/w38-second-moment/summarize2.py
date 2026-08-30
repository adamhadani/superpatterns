# W38 summarize2.py: canonical exact grid (exact_can2) — R_can, EY_pi, diagonal 1/EY, off-diagonal D.
import re
from math import log
ks=range(4,11)
print("CANONICAL exact (exact_can2): lnR_can | EY_pi | D = off-diagonal sum | Pr(pi in sigma) | 1/R_can")
for C in ['0.15','0.2','0.25','0.3','0.5','1']:
    print(f"C={C}:")
    for k in ks:
        fn=f"out/exactcan_k{k}_C{C}.txt"
        try: s=open(fn).read()
        except: continue
        m=re.search(r"samples=(\d+).*R_can=([\d.]+) \+- ([\d.]+)",s); m2=re.search(r"EY_pi=([\d.e+-]+)",s); m3=re.search(r"Edistinct_can/k!=([\d.]+)",s)
        if not m: continue
        S=int(m.group(1)); Rc=float(m.group(2)); Rcse=float(m.group(3)); EY=float(m2.group(1)); Pr=float(m3.group(1))
        terms=dict((int(a),float(b)) for a,b in re.findall(r"j=\s*(\d+)\s+E\[W_j\]=[\d.e+-]+\s+term=([\d.e+-]+)",s))
        D=Rc-terms.get(k,0)
        print(f"  k={k:<2} lnR_can={log(Rc):6.3f}±{Rcse/Rc:.3f}  EY_pi={EY:9.3g}  D={D:7.3f}  Pr={Pr:.4f}  1/R_can={1/Rc:.4f}  (S={S})")
print()
print("Off-diagonal terms (j<k) at C=0.25:")
for k in ks:
    try: s=open(f"out/exactcan_k{k}_C0.25.txt").read()
    except: continue
    t=[(int(a),float(b)) for a,b in re.findall(r"j=\s*(\d+)\s+E\[W_j\]=[\d.e+-]+\s+term=([\d.e+-]+)",s)]
    print(f"k={k}: "+"  ".join(f"j={a}:{b:.3g}" for a,b in t))
