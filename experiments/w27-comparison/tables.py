# usage: tables.py k dir n1,n2,... [topM]  -> markdown table of excess ln p_pi - ln p_id for the topM hardest classes
import sys, os, glob
k=int(sys.argv[1]); d=sys.argv[2]; ns=[int(x) for x in sys.argv[3].split(',')]; M=int(sys.argv[4]) if len(sys.argv)>4 else 8
ident=''.join(str(i) for i in range(1,k+1)); data={}
for f in glob.glob(d+'/*.txt'):
    p=os.path.basename(f)[:-4]; L={}
    for line in open(f):
        a=line.split()
        if len(a)==3 and a[2]!='-inf': L[int(a[0])]=float(a[2])
    if L: data[p]=L
w={l.split()[0]:int(l.split()[1]) for l in open(f'classes{k}.txt')}
idl=data[ident]; nmax=max(n for n in ns if n in idl)
rank=sorted([p for p in data if nmax in data[p] and p!=ident], key=lambda p:-(data[p][nmax]-idl[nmax]))
print("| n | n/k² | ln p_id | "+" | ".join(rank[:M])+" | … | "+" | ".join(rank[-2:])+" | #harder (orbit-weighted) | median excess |")
print("|"+"---|"*(len(rank[:M])+7))
import statistics
for n in ns:
    if n not in idl: continue
    ex={p:data[p][n]-idl[n] for p in data if n in data[p] and p!=ident}
    nh=sum(w[p] for p in ex if ex[p]>0.0)
    print(f"| {n} | {n/k**2:.2f} | {idl[n]:.2f} | "+" | ".join(f"{ex[p]:+.2f}" if p in ex else "" for p in rank[:M])+" | … | "+" | ".join(f"{ex[p]:+.2f}" if p in ex else "" for p in rank[-2:])+f" | {nh}/{sum(w.values())-1} | {statistics.median(ex.values()):+.2f} |")
