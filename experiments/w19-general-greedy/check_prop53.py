# Brute-force check of Prop 5.3: greedy lowest-above chain through ordered windows exists iff any chain exists.
import random, itertools
random.seed(2); bad=0; tot=0; ex=0
for trial in range(3000):
    h=random.randint(2,5); wins=[[random.random() for _ in range(random.randint(0,4))] for _ in range(h)]  # y-values of points in window i
    top=random.random()*1.2
    # greedy
    b=-1; ok=True
    for w in wins:
        c=[y for y in w if y>b]
        if not c: ok=False; break
        b=min(c)
    g= ok and b<top
    # exhaustive: chain q_i in window i with increasing y, all < top
    e=any(all(ch[i]<ch[i+1] for i in range(h-1)) and ch[-1]<top for ch in itertools.product(*[[y for y in w] for w in wins])) if all(wins) else False
    tot+=1; ex+=e
    if g!=e: bad+=1
print("Prop 5.3 check: trials=%d chains_exist=%d violations=%d"%(tot,ex,bad))
