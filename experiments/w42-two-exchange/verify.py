#!/usr/bin/env python3
"""Independently enumerate replacement neighbourhoods to check selection."""
from itertools import combinations,permutations
import random
from selection import copies,selected


def pattern(sigma,positions):
    values=[sigma[p] for p in sorted(positions)]
    return tuple(sum(w<v for w in values) for v in values)


def local_minimum(sigma,a,k,d):
    wanted=pattern(sigma,a); aset=set(a)
    outside=set(range(len(sigma)))-aset
    for size in range(1,d+1):
        for removed in combinations(a,size):
            for added in combinations(outside,size):
                b=tuple(sorted((aset-set(removed))|set(added)))
                if b<a and pattern(sigma,b)==wanted:
                    return False
    return True


def leftmost(sigma,a):
    wanted=pattern(sigma,a)
    for r,p in enumerate(a):
        start=a[r-1]+1 if r else 0
        for q in range(start,p):
            b=list(a);b[r]=q
            if pattern(sigma,b)==wanted:return False
    return True


if __name__=='__main__':
    cases=[(p,k) for n in range(3,7)
           for p in permutations(range(1,n+1))
           for k in range(2,min(4,n)+1)]
    rng=random.Random(20260910)
    for n,k in [(7,4),(8,4),(8,5),(10,6)]:
        for _ in range(20):
            p=list(range(1,n+1));rng.shuffle(p);cases.append((tuple(p),k))
    count=0
    for sigma,k in cases:
        for group in copies(sigma,k).values():
            for d in (1,2):
                kept={a for a,mask in selected(group,k,d)}
                direct={a for a,mask in group if local_minimum(sigma,a,k,d)}
                assert kept==direct,(sigma,k,d)
                if d==1:
                    assert kept=={a for a,mask in group if leftmost(sigma,a)}
                count+=len(group)
    print(f'PASS: {len(cases)} host/target-length cases, {count} local selection decisions')
    print('PASS: one-exchange selection equals direct leftmost-canonical selection')
