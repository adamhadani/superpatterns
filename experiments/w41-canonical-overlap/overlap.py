#!/usr/bin/env python3
"""Exact canonical overlap types and finite-host moments; no floating point.

Positions and values are one-based. Matrices index the m+1 open gaps,
including the gaps before the first and after the last union point.
"""
from collections import defaultdict
from itertools import combinations, permutations
from math import factorial


def pattern(rho, positions):
    values = [rho[p-1] for p in positions]
    rank = {v: i for i, v in enumerate(sorted(values))}
    return tuple(rank[v] for v in values)


def rectangles(rho, positions):
    m = len(rho)
    values = sorted(rho[p-1] for p in positions)
    bounds = [0] + values + [m+1]
    rank = {v: i+1 for i, v in enumerate(values)}
    previous = 0
    result = []
    for p in positions:
        r = rank[rho[p-1]]
        result.append((previous, p, bounds[r-1], bounds[r+1]))
        previous = p
    return result


def canonical_in_union(rho, rects):
    return not any(left < p < right and low < y < high
                   for left, right, low, high in rects
                   for p, y in enumerate(rho, 1))


def allowed_matrix(m, rects):
    allowed = [[1]*(m+1) for _ in range(m+1)]
    for left, right, low, high in rects:
        for i in range(left, right):
            for j in range(low, high):
                allowed[i][j] = 0
    return tuple(tuple(row) for row in allowed)


def union_types(k, overlap):
    """Yield each ordered compatible (rho,A,B) exactly once."""
    m = 2*k-overlap
    subsets = list(combinations(range(1, m+1), k))
    full = set(range(1, m+1))
    for rho in permutations(range(1, m+1)):
        copies = defaultdict(list)
        for positions in subsets:
            rects = rectangles(rho, positions)
            if canonical_in_union(rho, rects):
                copies[pattern(rho, positions)].append((positions, rects))
        for group in copies.values():
            for a, ra in group:
                for b, rb in group:
                    if set(a) | set(b) == full:
                        yield rho, a, b, allowed_matrix(m, ra+rb)


def extension_numerators(allowed, degree):
    """Return n! times a type's contribution, n=m,...,m+degree.

    Integrate x gaps first; the polynomial is the complete homogeneous
    symmetric polynomial in a_i(h)=sum_j allowed[i,j]*h_j.
    All operations below are integer polynomial operations.
    """
    size = len(allowed)
    zero = (0,)*size
    dp = [defaultdict(int) for _ in range(degree+1)]
    dp[0][zero] = 1
    for row in allowed:
        columns = [j for j, entry in enumerate(row) if entry]
        for d in range(1, degree+1):
            for alpha, coefficient in dp[d-1].items():
                for j in columns:
                    beta = list(alpha)
                    beta[j] += 1
                    dp[d][tuple(beta)] += coefficient
    result = []
    for polynomial in dp:
        total = 0
        for alpha, coefficient in polynomial.items():
            weight = coefficient
            for a in alpha:
                weight *= factorial(a)
            total += weight
        result.append(total)
    return result


def moment_numerators(k, overlap, largest_n):
    m = 2*k-overlap
    assert largest_n >= m
    types = 0
    fixed_common = 0
    sums = [0]*(largest_n-m+1)
    examples = {}
    matrices = defaultdict(int)
    for rho, a, b, allowed in union_types(k, overlap):
        types += 1
        common = set(a) & set(b)
        fixes = all(a.index(p) == b.index(p) for p in common)
        fixed_common += fixes
        examples.setdefault('fixed_common' if fixes else 'shifted_common',
                            dict(rho=rho, a=a, b=b))
        # Gap coordinates may be permuted independently under integration.
        # Only identical matrices are grouped here; no conjectural symmetry.
        matrices[allowed] += 1
    for allowed, multiplicity in matrices.items():
        values = extension_numerators(allowed, largest_n-m)
        sums = [x + multiplicity*y for x, y in zip(sums, values)]
    return dict(k=k, overlap=overlap, union_size=m, types=types,
                fixed_common=fixed_common, distinct_matrices=len(matrices),
                numerators=sums, denominators=[factorial(n) for n in range(m, largest_n+1)],
                examples=examples)
