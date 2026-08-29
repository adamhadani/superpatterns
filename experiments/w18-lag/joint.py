"""W18: EXACT joint failure probability of two (or three) H-threads.

Column-by-column Markov chain: at column x thread i is seeking element a_i (0..k, k = done)
and reads cell (pi(a_i)+t_i, x).  Two threads read the SAME cell at column x iff
pi(a_i)+t_i == pi(a_j)+t_j; otherwise the cells are distinct fresh coins (each thread reads exactly
one cell per column, so no other coincidences are possible).  This makes the process on (a_1,..,a_l)
an exact Markov chain, and Pr(all fail) = mass on {all a_i < k} after m columns.
Pr(fail) = Pr(Bin(m,1/2) <= k-1) for a single thread.  Work in log scale via per-column rescaling.
"""
import numpy as np
from math import lgamma, log, exp
import sys
sys.path.insert(0, '../w9-alon-threads')
from threads import tilted_grid, L_delta

def log_binom_tail(m, K):
    """log Pr(Bin(m,1/2) <= K)"""
    terms = [lgamma(m+1)-lgamma(j+1)-lgamma(m-j+1) - m*log(2) for j in range(K+1)]
    mx = max(terms)
    return mx + log(sum(exp(t-mx) for t in terms))

def joint2(pi, t1, t2, m):
    """log Pr(thread t1 fails AND thread t2 fails), exact.  States (a,b) with a,b<k only
    (a thread that completes never returns), so the total mass is Pr(both still active)."""
    k = len(pi)
    rows1 = pi + t1; rows2 = pi + t2
    same = rows1[:, None] == rows2[None, :]
    P = np.zeros((k, k)); P[0, 0] = 1.0
    logscale = 0.0
    for x in range(m):
        S = P * same; D = P - S
        N = 0.5 * S + 0.25 * D
        N[1:, 1:] += 0.5 * S[:-1, :-1] + 0.25 * D[:-1, :-1]
        N[1:, :] += 0.25 * D[:-1, :]
        N[:, 1:] += 0.25 * D[:, :-1]
        s = N.sum()
        if s == 0: return -np.inf
        N /= s; logscale += log(s); P = N
    return logscale

def joint3(pi, ts, m):
    k = len(pi)
    rows = [pi + t for t in ts]
    # pairwise same masks
    s01 = rows[0][:, None, None] == rows[1][None, :, None]
    s02 = rows[0][:, None, None] == rows[2][None, None, :]
    s12 = rows[1][None, :, None] == rows[2][None, None, :]
    s01 = np.broadcast_to(s01, (k,)*3); s02 = np.broadcast_to(s02, (k,)*3); s12 = np.broadcast_to(s12, (k,)*3)
    # classes: all distinct; 0=1 != 2; 0=2 != 1; 1=2 != 0; all same
    allsame = s01 & s02
    c01 = s01 & ~allsame; c02 = s02 & ~allsame; c12 = s12 & ~allsame
    dist = ~(s01 | s02 | s12)
    P = np.zeros((k,)*3); P[0,0,0] = 1.0; logscale = 0.0
    def shift(A, adv):
        """move mass of A to states advanced in the coordinates listed in adv; a coordinate at k stays."""
        B = A.copy()
        for ax in adv:
            C = np.zeros_like(B)
            idx = [slice(None)]*3
            src = [slice(None)]*3
            idx[ax] = slice(1, None); src[ax] = slice(0, -1)
            C[tuple(idx)] += B[tuple(src)]
            B = C
        return B
    import itertools
    for x in range(m):
        N = np.zeros_like(P)
        # all distinct: 3 independent coins
        A = P * dist
        for adv in itertools.product([0,1], repeat=3):
            N += (1/8) * shift(A, [i for i in range(3) if adv[i]])
        for mask, pair, other in ((c01,(0,1),2), (c02,(0,2),1), (c12,(1,2),0)):
            A = P * mask
            for cp in (0,1):
                for co in (0,1):
                    adv = (list(pair) if cp else []) + ([other] if co else [])
                    N += 0.25 * shift(A, adv)
        A = P * allsame
        N += 0.5 * shift(A, []) + 0.5 * shift(A, [0,1,2])
        s = N.sum()
        if s == 0: return -np.inf
        N /= s; logscale += log(s); P = N
    return logscale

if __name__ == "__main__":
    # sanity: two threads far apart in rows should be exactly independent
    k = 20; m = 80
    pi = tilted_grid(4)  # k=16
    k = 16
    lf = log_binom_tail(m, k-1)
    print("single log Pr(fail)", lf)
    print("joint(0, k) - 2 single (must be 0):", joint2(pi, 0, k, m) - 2*lf)
    print("joint3(0,k,?)", )
