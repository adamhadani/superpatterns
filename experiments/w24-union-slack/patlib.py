"""Decode/encode of the mixed-radix pattern codes used by mslack.c, plus pattern statistics."""
import itertools, math

def decode(code, k):
    r = [0]*k
    for j in range(k, 0, -1):
        r[j-1] = code % j; code //= j
    p = [0]*k
    for j in range(k):
        v = r[j]+1
        for i in range(j):
            if p[i] >= v: p[i] += 1
        p[j] = v
    return tuple(p)

def encode(p):
    code = 0
    for j, v in enumerate(p):
        r = sum(1 for i in range(j) if p[i] < v)
        code = code*(j+1) + r
    return code

def standardise(seq):
    order = sorted(range(len(seq)), key=lambda i: seq[i])
    pat = [0]*len(seq)
    for rank, i in enumerate(order): pat[i] = rank+1
    return tuple(pat)

def lis(p):
    import bisect
    t = []
    for x in p:
        i = bisect.bisect_left(t, x)
        if i == len(t): t.append(x)
        else: t[i] = x
    return len(t)

def lds(p): return lis([-x for x in p])

def runs(p):  # number of maximal monotone (ascending/descending) runs
    if len(p) < 2: return 1
    r = 1
    for i in range(1, len(p)-1):
        if (p[i] > p[i-1]) != (p[i+1] > p[i]): r += 1
    return r

def asc_runs(p):  # number of ascending runs = descents + 1
    return 1 + sum(1 for i in range(len(p)-1) if p[i] > p[i+1])

def reverse(p): return tuple(reversed(p))
def complement(p): k = len(p); return tuple(k+1-x for x in p)
def inverse(p):
    q = [0]*len(p)
    for i, v in enumerate(p): q[v-1] = i+1
    return tuple(q)

def sum_decomposable(p):
    m = 0
    for i, v in enumerate(p[:-1]):
        m = max(m, v)
        if m == i+1: return True
    return False
def skew_decomposable(p): return sum_decomposable(complement(p))

def missing_bruteforce(sigma, k):
    k_fact = math.factorial(k)
    seen = set()
    for idx in itertools.combinations(range(len(sigma)), k):
        seen.add(encode(standardise([sigma[i] for i in idx])))
    return sorted(set(range(k_fact)) - seen)
