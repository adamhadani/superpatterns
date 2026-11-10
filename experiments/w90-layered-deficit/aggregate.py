import glob,re,math
from collections import defaultdict
agg=defaultdict(list)
pat=re.compile(r'n=(\d+) S=(\d+)\s+E\[LIS\]=([\d.]+) \(sd ([\d.]+)\)\s+E\[L21\]=([\d.]+) \(sd ([\d.]+)\)\s+E\[2L21-LIS\]=(-?[\d.]+) \+- ([\d.]+) \(sd ([\d.]+)\)\s+E\[2L21-2floor\(LIS/2\)\]=(-?[\d.]+)')
for f in glob.glob('out/l21_n*_w*.txt'):
    for line in open(f):
        m=pat.match(line)
        if m:
            g=m.groups()
            agg[int(g[0])].append(dict(S=int(g[1]),lis=float(g[2]),l21=float(g[4]),d=float(g[6]),sd=float(g[8]),fl=float(g[9])))
print("%10s %8s %10s %10s %11s %8s %12s %22s"%("n","samples","E[LIS]","E[L21]","E[2L-LIS]","se","D=E[2fl-2L]","D/sqrt(n) +- se"))
for n in sorted(agg):
    rows=agg[n]; S=sum(r['S'] for r in rows)
    w=lambda k: sum(r['S']*r[k] for r in rows)/S
    sd=math.sqrt(sum(r['S']*r['sd']**2 for r in rows)/S); se=sd/math.sqrt(S)
    print("%10d %8d %10.4f %10.4f %11.4f %8.4f %12.4f %12.5f +- %.5f"%(n,S,w('lis'),w('l21'),w('d'),se,-w('fl'),-w('fl')/math.sqrt(n),se/math.sqrt(n)))
