#!/usr/bin/env python3
"""Exact one- and two-exchange local minima among equal-pattern copies.

All earlier copies are considered, including those not retained. This is
local-minimum selection, not greedy packing of the retained copies.
"""
from collections import defaultdict
from itertools import combinations, permutations
import json
from math import factorial
from pathlib import Path


def copies(sigma,k):
    groups=defaultdict(list)
    for positions in combinations(range(len(sigma)),k):
        values=[sigma[i] for i in positions]
        rank={v:i for i,v in enumerate(sorted(values))}
        pattern=tuple(rank[v] for v in values)
        mask=sum(1<<i for i in positions)
        groups[pattern].append((positions,mask))
    return groups


def selected(group,k,d):
    return [a for i,a in enumerate(group)
            if not any((a[1]&b[1]).bit_count()>=k-d for b in group[:i])]


def census(k,n):
    patterns=list(permutations(range(k)))
    stats={p:dict(pattern=[v+1 for v in p],hits=0,y1=0,y2=0,
                  y1_squared=0,y2_squared=0,max_y2=0) for p in patterns}
    for sigma in permutations(range(1,n+1)):
        for p,group in copies(sigma,k).items():
            one=selected(group,k,1);two=selected(group,k,2)
            assert 1<=len(two)<=len(one)
            assert all((a[1]&b[1]).bit_count()<=k-3
                       for a,b in combinations(two,2))
            row=stats[p]
            row['hits']+=1
            row['y1']+=len(one);row['y2']+=len(two)
            row['y1_squared']+=len(one)**2
            row['y2_squared']+=len(two)**2
            row['max_y2']=max(row['max_y2'],len(two))
    return dict(k=k,n=n,hosts=factorial(n),patterns=list(stats.values()))


if __name__=='__main__':
    results=[]
    for k,n in [(3,6),(3,7),(4,6),(4,7),(4,8),(5,7),(5,8)]:
        result=census(k,n);results.append(result)
        y1=[r['y1'] for r in result['patterns']]
        y2=[r['y2'] for r in result['patterns']]
        print(f'k={k} n={n} hosts={result["hosts"]}: '
              f'Y1 sums {min(y1)}..{max(y1)}, '
              f'Y2 sums {min(y2)}..{max(y2)}',flush=True)
    Path(__file__).with_name('exact-census.json').write_text(json.dumps(results,indent=2)+'\n')
