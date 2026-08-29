import glob,os,collections
rows=collections.defaultdict(dict)
for f in sorted(glob.glob('out2/*.txt')):
    t=open(f).read().split()
    if not t or t[0]=='TIMEOUT': continue
    kind=os.path.basename(f).split('_')[0]
    if kind=='greedy':
        r,h,N,reps,succ=map(int,t); found=succ; notf=reps-succ; unk=0
    else:
        r,h,N,reps,found,notf,unk=map(int,t)
    k=r*h; C=N/k/k
    rows[(kind,r,h)][round(C,3)]=(found,notf,unk,reps)
print("Pr(contained) at N = C k^2; entries found/reps (unknown = beam-truncated, not found, counted as failures);")
print("fix = exact fixed-strip, free = exact free, beam = free with beam (found is certified, lower bound on Pr), greedy = rigid-grid corner greedy")
for key in sorted(rows, key=lambda x:(x[0],x[1]*x[2],x[1])):
    kind,r,h=key; d=rows[key]
    line=f"{kind:6s} r={r:3d} h={h:3d} k={r*h:5d}: "
    for C in sorted(d):
        found,notf,unk,reps=d[C]
        line+=f" C={C:.2f}:{found/reps:.3f}"+(f"({unk}?)" if unk else "")
    print(line)
