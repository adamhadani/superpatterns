import sys
def zeta(k, prepend_max=True):
    runs=[]
    for j in range(1,k+1):
        if j%2==1: runs.append([x for x in range(1,k+2,2)])
        else: runs.append([x for x in range(k+1,0,-1) if x%2==0])
    w=[x for r in runs for x in r if x<=k]
    # ties: equal letters decreasing -> later occurrences smaller
    idx=sorted(range(len(w)), key=lambda i:(w[i], -i))
    p=[0]*len(w)
    for r,i in enumerate(idx): p[i]=r+1
    if k%2==0 and prepend_max: p=[len(p)+1]+p
    return p
k=int(sys.argv[1]); print(' '.join(map(str,zeta(k))))
