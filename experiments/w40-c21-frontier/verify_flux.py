#!/usr/bin/env python3
"""Exact integer interval-union flux vs unpruned extension, on small states."""
from itertools import permutations
from verify_pruned import full_thresholds


def reduced_state(p):
    f = [0,float('inf')]
    active = {}
    for y in p:
        j = max(i for i,a in enumerate(f) if a<y)
        cover = [z for z,l in active.items() if l<y<z]
        if cover:
            z = min(cover); b=f[j+1]; f[j+1]=z
            active = {a:l for a,l in active.items() if not z<=a<b}
            if j+1==len(f)-1:
                f.append(float('inf'))
        active[y] = f[j]
    return f,active


def union_length(intervals):
    right = -float('inf'); total=0
    for low,high in sorted(intervals):
        total += max(0,high-max(low,right))
        right = max(right,high)
    return total


if __name__ == '__main__':
    checks=0
    for n in range(1,7):
        for p in permutations(range(1,n+1)):
            f,active=reduced_state(p)
            # Every event indicator is constant between consecutive integers.
            extensions=[full_thresholds(p+(a+.5,))[-1] for a in range(n+1)]
            for cut in range(n+1):
                u=cut+.5
                j=sum(a<=u for a in f[1:])
                rate=union_length([(l,z) for z,l in active.items() if f[j]<z<=u])
                direct=sum(sum(a<=u for a in fs)-j for fs in extensions)
                assert direct==rate,(p,u,rate,direct)
                checks+=1
    p,q=(3,2,4,1),(2,3,1,4)
    f,a=reduced_state(p); g,b=reduced_state(q)
    assert f==g and set(a)==set(b) and a!=b
    assert len(full_thresholds(p+(2.5,))[-1])==1
    assert len(full_thresholds(q+(2.5,))[-1])==2
    print(f'PASS: {checks} exact cut-flux checks on all S_n through n=6')
    print('PASS: reachable four-point counterexample to erasing activation marks')
