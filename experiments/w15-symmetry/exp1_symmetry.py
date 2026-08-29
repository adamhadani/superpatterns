"""Exp 1 (W15): dihedral images and shift chains.
For each pattern family compute, for pi and for pi^{-1} (reverse/complement leave the chain-length
profile invariant -- checked below), the profile L_Delta, the number of "bad" shifts at the W9 threshold
k/(3 ln^2 k) and at a looser threshold k/(3 ln k), and LDS / LIS of pi restricted to the longest chain.
Also checks the symmetry claims: L_Delta(pi^r) = L_Delta(pi^c) = L_Delta(pi), and
LDS(pi^c|A) = LIS(pi|A) etc."""
import sys, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import runs_pattern, periodic_word, tilted_grid, lis_length, L_delta

rng = np.random.default_rng(15)

def inv(pi):
    out = np.empty(len(pi), dtype=int); out[pi] = np.arange(len(pi)); return out
def rev(pi): return pi[::-1].copy()
def comp(pi): return len(pi) - 1 - pi

def chain(pi, d):
    """a maximum Delta-shift chain A (leader side: pi(a) >= d, b(a) = pi^{-1}(pi(a)-d) increasing)."""
    k = len(pi); iv = inv(pi)
    A = [a for a in range(k) if pi[a] >= d]
    seq = [iv[pi[a] - d] for a in A]
    # LIS with reconstruction
    tails, tidx, prev = [], [], [-1]*len(seq)
    from bisect import bisect_left
    for i, v in enumerate(seq):
        j = bisect_left(tails, v)
        if j == len(tails): tails.append(v); tidx.append(i)
        else: tails[j] = v; tidx[j] = i
        prev[i] = tidx[j-1] if j > 0 else -1
    out = []; i = tidx[-1] if tidx else -1
    while i >= 0: out.append(A[i]); i = prev[i]
    return out[::-1]

def lds_length(seq): return lis_length([-v for v in seq])

def profile(pi):
    k = len(pi); return np.array([L_delta(pi, d) for d in range(1, k)])

def report(name, pi):
    k = len(pi); lnk = np.log(k)
    thr1, thr2 = k/(3*lnk**2), k/(3*lnk)
    for lab, p in [('pi', pi), ('pi^-1', inv(pi))]:
        L = profile(p)
        d = int(np.argmax(L)) + 1
        A = chain(p, d)
        pa = [p[a] for a in A]
        print(f"{name:<34} {lab:<6} k={k} maxL/k={L.max()/k:.3f} (D={d}) L_1/k={L[0]/k:.3f} "
              f"#bad(k/3ln^2k)={int((L>thr1).sum()):4d} #bad(k/3lnk)={int((L>thr2).sum()):4d} "
              f"LDS(p|A)={lds_length(pa):3d} LIS(p|A)={lis_length(pa):3d}")

def perm_rows_grid(r, h, tau):
    """pi(i*r + s) = tau(s)*h + i, i<h, s<r  (value blocks of size h indexed by tau(s))."""
    k = r*h; pi = np.empty(k, dtype=int)
    for i in range(h):
        for s in range(r):
            pi[i*r + s] = tau[s]*h + i
    return pi

def block_perturbed_grid(r, h, eps, rng):
    """pi(i*r + s) = tau_i(s)*h + i with tau_i in S_r fixing a random (1-eps)-fraction of letters."""
    k = r*h; pi = np.empty(k, dtype=int)
    for i in range(h):
        tau = np.arange(r)
        idx = np.flatnonzero(rng.random(r) < eps)
        tau[idx] = tau[rng.permutation(idx)]
        for s in range(r):
            pi[i*r + s] = tau[s]*h + i
    return pi

def affine(k, a):
    return np.array([(a*i) % k for i in range(k)])

if __name__ == "__main__":
    # ---- symmetry checks on a random pattern
    k = 60; pi = rng.permutation(k)
    for d in [1, 2, 5, 13]:
        assert L_delta(pi, d) == L_delta(rev(pi), d) == L_delta(comp(pi), d) == L_delta(comp(rev(pi)), d)
        A = chain(pi, d); pa = [pi[a] for a in A]
        # complement: chain (A,B) of pi becomes chain with leader B = b(A) of pi^c; pi(b) = pi(a)-d, same pattern
        B = [int(inv(pi)[pi[a]-d]) for a in A]
        assert B == sorted(B)
        assert lds_length([comp(pi)[b] for b in B]) == lis_length(pa)
        # reverse: k-1-A is a chain of pi^r; LDS(pi^r|_{k-1-A}) = LIS(pi|A)
        Ar = sorted(k-1-a for a in A)
        assert lds_length([rev(pi)[a] for a in Ar]) == lis_length(pa)
    print("symmetry checks passed (L_Delta invariant under r, c, rc; LDS<->LIS as claimed)")

    # ---- families
    for l in [20, 30]:
        report(f"tilted grid {l}x{l}", tilted_grid(l))
    for (r, h) in [(20, 20), (10, 40), (40, 10), (30, 30)]:
        tau = rng.permutation(r)
        report(f"grid rows permuted r={r} h={h}", perm_rows_grid(r, h, tau))
    for (r, h) in [(20, 20), (30, 30), (10, 60), (60, 10)]:
        for eps in [0.2, 0.45]:
            report(f"block-perturbed r={r} h={h} eps={eps}", block_perturbed_grid(r, h, eps, rng))
    for k, a in [(401, 7), (401, 123), (907, 31)]:
        report(f"affine k={k} a={a}", affine(k, a))
    # random unions of decreasing runs on value intervals (complement of L_r)
    for k, r in [(400, 8), (400, 32), (600, 24)]:
        pi, w = runs_pattern(k, r, rng)
        report(f"random L_{r} (inc runs)", pi)
        report(f"random L_{r}^c (dec runs)", comp(pi))
        pi2, w2 = runs_pattern(k, r, rng, word=periodic_word(k, r))
        report(f"periodic L_{r}", pi2)
    # HK-type: pi(i) = (a*i + b*(i mod s)) mod k
    for k, a, b, s in [(400, 21, 7, 20), (401, 20, 1, 20), (900, 31, 29, 30)]:
        seq = [(a*i + b*(i % s)) % k for i in range(k)]
        if len(set(seq)) == k:
            report(f"HK-type a={a} b={b} s={s}", np.array(seq))
        else:
            print(f"HK-type a={a} b={b} s={s} k={k}: not a permutation, skipped")
    # random permutation baseline
    for k in [400, 900]:
        report("uniform random", rng.permutation(k))
