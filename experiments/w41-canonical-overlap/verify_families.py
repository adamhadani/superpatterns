#!/usr/bin/env python3
"""Direct host checks of full shifts and exact descending-block clusters."""
from itertools import combinations
from math import comb
from overlap import canonical_in_union, pattern, rectangles
from verify import host_pairs


def pairs(n):
    return tuple(i+1 if i%2 else i-1 for i in range(1,n-n%2+1))+((n,) if n%2 else ())


if __name__ == '__main__':
    for k in range(2,101):
        rho=pairs(k+2)
        a=tuple(range(1,k+1)); b=tuple(range(3,k+3))
        assert pattern(rho,a)==pattern(rho,b)
        assert canonical_in_union(rho,rectangles(rho,a))
        assert canonical_in_union(rho,rectangles(rho,b))
        assert all(a.index(p)!=b.index(p) for p in set(a)&set(b))
    checks=0
    for r in range(1,7):
        for q in range(1,r+1):
            rho=pairs(2*r); target=tuple(x-1 for x in pairs(2*q))
            copies=[]
            for a in combinations(range(1,2*r+1),2*q):
                if pattern(rho,a)!=target:
                    continue
                assert canonical_in_union(rho,rectangles(rho,a))
                copies.append(set(a))
            assert len(copies)==comb(r,q)
            independent=host_pairs(rho,2*q,target)
            assert independent[2*q]==comb(r,q)
            for s in range(q+1):
                direct=sum(len(a&b)==2*s for a in copies for b in copies)
                wanted=comb(r,q)*comb(q,s)*(comb(r-q,q-s) if q-s<=r-q else 0)
                assert direct==wanted,(r,q,s,direct,wanted)
                assert independent[2*s]==wanted
                checks+=1
            assert all(independent[j]==0 for j in range(1,2*q,2))
    print('PASS: full-shift family for every k=2,...,100')
    print(f'PASS: {checks} exact canonical cluster overlap counts for r<=6')
