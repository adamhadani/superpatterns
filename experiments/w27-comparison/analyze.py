import sys, os, glob, math
k=int(sys.argv[1]); d=sys.argv[2]; ns=[int(x) for x in sys.argv[3].split(',')]
ident=''.join(str(i) for i in range(1,k+1))
data={}
for f in glob.glob(d+'/*.txt'):
    p=os.path.basename(f)[:-4]; L={}
    for line in open(f):
        a=line.split()
        if len(a)==3 and a[2]!='-inf': L[int(a[0])]=float(a[2])
    if L: data[p]=L
w={l.split()[0]:int(l.split()[1]) for l in open(f'classes{k}.txt')}
idl=data[ident]
print(f"k={k} dir={d} patterns={len(data)}  ln p_id(n): "+' '.join(f"{n}:{idl[n]:.3f}" for n in ns if n in idl))
# ranking at each n
for n in ns:
    rows=[(data[p][n]-idl[n],p) for p in data if n in data[p] and n in idl]
    rows.sort(reverse=True)
    nh=sum(1 for r,p in rows if r>0); wh=sum(w[p] for r,p in rows if r>0)
    print(f"n={n} ({n/k**2:.2f}k^2): #classes with ln p_pi > ln p_id: {nh} (patterns {wh}/{sum(w.values())}); top5: "+
          ', '.join(f"{p}:{r:+.3f}" for r,p in rows[:5])+" | bottom: "+', '.join(f"{p}:{r:+.3f}" for r,p in rows[-3:]))
# crossover: first n where ratio>0 and stays
print("crossovers (first n from which ln p_pi - ln p_id > 0.02 for all later n):")
for p in sorted(data, key=lambda p:-max(data[p][n]-idl[n] for n in data[p] if n in idl)):
    ratios=[(n,data[p][n]-idl[n]) for n in sorted(data[p]) if n in idl]
    nx=None
    for i,(n,r) in enumerate(ratios):
        if r>0.02 and all(rr>0.02 for _,rr in ratios[i:]): nx=n; break
    mx=max(r for _,r in ratios)
    if nx is not None: print(f"  {p} w={w[p]} n_x={nx} ({nx/k**2:.2f}k^2) max excess {mx:+.3f} at n={max(ratios,key=lambda t:t[1])[0]}")
