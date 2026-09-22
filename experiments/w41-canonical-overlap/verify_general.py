#!/usr/bin/env python3
"""Additional checks for disjoint, diagonal and intermediate overlap formulas."""
from itertools import permutations
from overlap import moment_numerators
from verify import host_pairs


if __name__ == '__main__':
    checks=0
    for k in (2,3):
        by_n={n:[host_pairs(p,k) for p in permutations(range(1,n+1))]
              for n in range(k,7)}
        for j in range(k+1):
            m=2*k-j
            result=moment_numerators(k,j,6)
            for n in range(m,7):
                direct=sum(row[j] for row in by_n[n])
                assert direct==result['numerators'][n-m],(k,j,n)
                checks+=1
    print(f'PASS: {checks} exact moment numerators across every overlap for k=2,3 and n<=6')
