from zig import *
p=zeta(7); n=len(p)
best=None
for i in range(n):
    q=p[:i]+p[i+1:]; q=tiebreak(q)  # relabel to [24]
    c,_=count(7,q)
    if best is None or c>best[0]: best=(c,i,q)
print(best[0],best[1]+1," ".join(map(str,best[2])))
