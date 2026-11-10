#!/usr/bin/env python3
"""Exact check on all of S_n of the bookkeeping in W91 section 1: (F3) incl. odd prefix lengths, and Lemma 1.1
(telescoping identity  sum_sigma [LIS - N_{W_S}] = sum_{i in S} Cost_S(i) ), by direct containment.
Usage: python3 section1_exact.py N"""
import sys, itertools
from lemma23_containment import prefix_blocks, ranks, dp_array

n = int(sys.argv[1])
SETS = [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (2, 4), (1, 2, 3), (1, 2, 3, 4)]

def word(S, m):
    B = []
    for i in range(1, m + 1):
        B += [2] if i in S else [1, 1]
    return tuple(B)

m = n // 2 + 1
pats = set()
for S in SETS:
    for t in range(1, n + 1):
        pats.add(tuple(prefix_blocks(word(S, m), t)))
    for i in S:
        alpha = prefix_blocks(word(tuple(j for j in S if j < i), m), 2 * i - 2)
        for b in range(0, n + 1):
            if 2 * i + b <= n:
                pats.add(tuple(alpha + [1, 1] + [1] * b)); pats.add(tuple(alpha + [2] + [1] * b))
pats = sorted(pats)
count = {p: 0 for p in pats}
for perm in itertools.permutations(range(1, n + 1)):
    pts = list(enumerate(perm))
    xr, yr = ranks(pts)
    for p in pats:
        if dp_array(xr, yr, list(p))[n, n]:
            count[p] += 1

def cnt(S, t):
    return count[tuple(prefix_blocks(word(S, m), t))]

bad = 0
ncmp = 0
for S in SETS:
    for S2 in SETS:
        if set(S) < set(S2):
            for t in range(1, n + 1):
                ncmp += 1
                if cnt(S2, t) > cnt(S, t):
                    bad += 1; print("F3 VIOLATION", S, S2, t, cnt(S, t), cnt(S2, t))
print(f"n={n}: (F3) checked for {ncmp} triples (S subset S', t <= {n}, odd t included): {bad} violations")
for S in SETS[1:]:
    lhs = sum(cnt((), t) - cnt(S, t) for t in range(1, n + 1))      # sum over sigma of LIS - N_{W_S}
    rhs = 0
    terms = []
    for i in S:
        alpha = prefix_blocks(word(tuple(j for j in S if j < i), m), 2 * i - 2)
        c = sum(count[tuple(alpha + [1, 1] + [1] * b)] - count[tuple(alpha + [2] + [1] * b)]
                for b in range(0, n + 1) if 2 * i + b <= n)
        terms.append(c); rhs += c
    print(f"n={n}: S={S}: sum_sigma (LIS - N_W_S) = {lhs} ; sum of stage costs = {rhs} {terms} ; {'OK' if lhs == rhs else 'MISMATCH'}; all stage costs >= 0: {all(c >= 0 for c in terms)}")
