p=[6,14,10,2,13,17,5,8,3,12,9,16,1,7,11,4,15]
n=len(p)
# plot
for v in range(n,0,-1):
    print(f"{v:3d} "+"".join(" #" if p[i]==v else " ." for i in range(n)))
print("    "+"".join(f"{i+1:2d}" for i in range(n)))
# ascending/descending runs
def runs(seq,cmp):
    r=[[seq[0]]]
    for x in seq[1:]:
        if cmp(r[-1][-1],x): r[-1].append(x)
        else: r.append([x])
    return r
print("asc runs:",runs(p,lambda a,b:a<b))
print("desc runs:",runs(p,lambda a,b:a>b))
# inverse
inv=[0]*(n+1)
for i,v in enumerate(p): inv[v]=i+1
print("inverse:",inv[1:])
print("reverse:",p[::-1]); print("complement:",[n+1-v for v in p])
# parity structure: values mod 2 by position, mod 3
print("val mod 2 by pos:",[v%2 for v in p])
print("val mod 3 by pos:",[v%3 for v in p])
print("pos mod 2 of value 1..n:", [ (inv[v])%2 for v in range(1,n+1)])
# longest increasing / decreasing subsequence
import itertools
def lis(s):
    best=[1]*len(s)
    for i in range(len(s)):
        for j in range(i):
            if s[j]<s[i]: best[i]=max(best[i],best[j]+1)
    return max(best)
print("LIS",lis(p),"LDS",lis([-x for x in p]))
# minimal number of monotone (either direction) runs covering positions consecutively
# dp
INF=99
dp=[INF]*(n+1); dp[0]=0
for i in range(1,n+1):
    for j in range(i):
        seg=p[j:i]
        if all(seg[t]<seg[t+1] for t in range(len(seg)-1)) or all(seg[t]>seg[t+1] for t in range(len(seg)-1)):
            dp[i]=min(dp[i],dp[j]+1)
print("min consecutive monotone pieces:",dp[n])
