#!/usr/bin/env python3
"""CEGAR SAT search for a k-superpattern of length n.

Encoding: order matrix lt[p][q] (p<q) = "sigma(p) < sigma(q)", with transitivity
clauses (a total order on positions <-> a permutation).  For each pattern pi
(added lazily): position-choice vars with monotone prefix chains, and for every
pair of pattern entries consecutive in VALUE the corresponding lt literal.
Loop: solve; decode sigma; find missing patterns with the C checker (sp -c);
add them; repeat.  UNSAT => no k-superpattern of length n (given the extra
symmetry-breaking assumption stated in --sym).
"""
import sys, subprocess, itertools, time, argparse, random
from pysat.solvers import Cadical195

SP = "/Users/adamhadani/Development/math-proofs/superpatterns/work/w1-search/sp"

def missing_patterns(k, perm):
    out = subprocess.run([SP, "-k", str(k), "-c", "-p", " ".join(map(str, perm))],
                         capture_output=True, text=True).stdout
    miss = []
    for line in out.splitlines():
        if line.startswith("missing:"):
            miss.append(tuple(int(x) for x in line.split()[1:]))
    return miss

class Enc:
    def __init__(self, n, k, enc="lt"):
        self.n, self.k, self.enc = n, k, enc
        self.nv = 0
        self.S = Cadical195()
        self.lt = {}
        for p in range(n):
            for q in range(p+1, n):
                self.lt[(p, q)] = self.new()
        # transitivity
        for p, q, r in itertools.combinations(range(n), 3):
            a, b, c = self.lt[(p, q)], self.lt[(q, r)], self.lt[(p, r)]
            self.S.add_clause([-a, -b, c])
            self.S.add_clause([a, b, -c])
        self.npat = 0
        self.ncl = 0
        if enc == "pv":
            # permutation matrix x[p][v], linked to lt: x[p][v] & x[q][w] -> lt[p][q] iff v<w
            self.x = [[self.new() for v in range(n)] for p in range(n)]
            from pysat.card import CardEnc, EncType
            for p in range(n):
                self.S.add_clause(self.x[p])
                for v in range(n):
                    for w in range(v+1, n):
                        self.S.add_clause([-self.x[p][v], -self.x[p][w]])
            for v in range(n):
                self.S.add_clause([self.x[p][v] for p in range(n)])
                for p in range(n):
                    for q in range(p+1, n):
                        self.S.add_clause([-self.x[p][v], -self.x[q][v]])
            # value-prefix vars y[p][v] = sigma(p) <= v
            self.y = [[self.new() for v in range(n)] for p in range(n)]
            for p in range(n):
                for v in range(n):
                    if v+1 < n: self.S.add_clause([-self.y[p][v], self.y[p][v+1]])
                    self.S.add_clause([-self.x[p][v], self.y[p][v]])
                    if v > 0: self.S.add_clause([-self.x[p][v], -self.y[p][v-1]])
                    # y[p][v] & -y[p][v-1] -> x[p][v]
                    self.S.add_clause([-self.y[p][v], self.x[p][v]] + ([self.y[p][v-1]] if v > 0 else []))
            # link lt with y: lt[p][q] <-> exists v: y[p][v] & -y[q][v]; encode both directions via
            # x[p][v] & y[q][v] -> -lt[p][q]  ; x[p][v] & -y[q][v] -> lt[p][q]
            for p in range(n):
                for q in range(p+1, n):
                    for v in range(n):
                        self.S.add_clause([-self.x[p][v], -self.y[q][v], -self.lt[(p, q)]])
                        self.S.add_clause([-self.x[p][v], self.y[q][v], self.lt[(p, q)]])

    def new(self):
        self.nv += 1
        return self.nv

    def less(self, p, q):  # literal for sigma(p) < sigma(q)
        return self.lt[(p, q)] if p < q else -self.lt[(q, p)]

    def add_pattern(self, pi):
        if self.enc == "pv": return self.add_pattern_pv(pi)
        n, k, S = self.n, self.k, self.S
        # a[i][p] : position of pattern entry i is <= p  (p in range(n))
        a = [[self.new() for p in range(n)] for i in range(k)]
        cl = 0
        for i in range(k):
            for p in range(n-1):
                S.add_clause([-a[i][p], a[i][p+1]]); cl += 1
            S.add_clause([a[i][n-1]]); cl += 1
            # position >= i  and <= n-k+i
            if i > 0:
                S.add_clause([-a[i][i-1]]); cl += 1
        for i in range(k-1):
            for p in range(n):
                # entry i+1 at position <= p  => entry i at position <= p-1
                if p == 0:
                    S.add_clause([-a[i+1][0]])
                else:
                    S.add_clause([-a[i+1][p], a[i][p-1]])
                cl += 1
        def e(i, p):  # literals whose conjunction = "entry i at position p"
            return [a[i][p]] + ([-a[i][p-1]] if p > 0 else [])
        # value constraints for consecutive values
        order = sorted(range(k), key=lambda i: pi[i])
        for t in range(k-1):
            i, j = order[t], order[t+1]   # pi[i] < pi[j]
            for p in range(n):
                for q in range(n):
                    if p == q: continue
                    if (i < j) != (p < q): continue   # positions consistent with index order
                    S.add_clause([-x for x in e(i, p)] + [-x for x in e(j, q)] + [self.less(p, q)])
                    cl += 1
        self.npat += 1
        self.ncl += cl

    def add_pattern_pv(self, pi):
        n, k, S = self.n, self.k, self.S
        # a[i][p]: entry i at position <= p ; b[i][v]: entry i has value <= v
        a = [[self.new() for p in range(n)] for i in range(k)]
        b = [[self.new() for v in range(n)] for i in range(k)]
        cl = 0
        order = sorted(range(k), key=lambda i: pi[i])  # by value
        for chain, seq in ((a, list(range(k))), (b, order)):
            for t, i in enumerate(seq):
                for p in range(n-1):
                    S.add_clause([-chain[i][p], chain[i][p+1]]); cl += 1
                S.add_clause([chain[i][n-1]]); cl += 1
                if t > 0: S.add_clause([-chain[i][t-1]]); cl += 1
            for t in range(k-1):
                i, j = seq[t], seq[t+1]
                S.add_clause([-chain[j][0]]); cl += 1
                for p in range(1, n):
                    S.add_clause([-chain[j][p], chain[i][p-1]]); cl += 1
        # consistency: entry i at position p with value v -> x[p][v]
        for i in range(k):
            for p in range(i, n-k+i+1):
                for v in range(pi[i]-1, n-k+pi[i]):
                    S.add_clause([-a[i][p]] + ([a[i][p-1]] if p > 0 else []) +
                                 [-b[i][v]] + ([b[i][v-1]] if v > 0 else []) + [self.x[p][v]]); cl += 1
        self.npat += 1; self.ncl += cl

    def decode(self, model):
        n = self.n
        m = set(x for x in model if x > 0)
        rank = [0]*n
        for p in range(n):
            for q in range(n):
                if p != q and (self.less(q, p) in m if self.less(q, p) > 0 else -self.less(q, p) not in m):
                    rank[p] += 1
        return [r+1 for r in rank]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("k", type=int); ap.add_argument("n", type=int)
    ap.add_argument("--sym", default="none", help="none | first (sigma(0)<sigma(n-1): breaks complement/reverse) | pos1 (value 1 in left half)")
    ap.add_argument("--init", default="layered", help="initial pattern set: layered|mono|all|none")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--enc", default="lt")
    ap.add_argument("--batch", type=int, default=100000, help="max patterns added per iteration")
    ap.add_argument("--extra", default="", help="extra unit constraints, e.g. 'v1<=3' (value 1 at position <=3, 1-based)")
    args = ap.parse_args()
    k, n = args.k, args.n
    E = Enc(n, k, args.enc)
    if args.sym in ("first", "both"):
        E.S.add_clause([E.less(0, n-1)])
    if args.sym in ("pos1", "both"):
        # value 1 (minimum) at position <= ceil(n/2)-1 (0-based): "sigma(p) is min" = all others greater
        # encode: OR over p<=h of min_p, min_p -> less(p,q) for all q
        h = (n+1)//2 - 1
        ms = []
        for p in range(h+1):
            m = E.new(); ms.append(m)
            for q in range(n):
                if q != p: E.S.add_clause([-m, E.less(p, q)])
        E.S.add_clause(ms)
    if args.sym == "rc":
        # (i) sigma(1) < sigma(n)  [complement]  and (iv) pos(1)+pos(n) <= n+1  [reverse-complement, preserves (i)]
        E.S.add_clause([E.less(0, n-1)])
        mins, maxs = [], []
        for p in range(n):
            m = E.new(); mins.append(m)
            for q in range(n):
                if q != p: E.S.add_clause([-m, E.less(p, q)])
            M = E.new(); maxs.append(M)
            for q in range(n):
                if q != p: E.S.add_clause([-M, E.less(q, p)])
        E.S.add_clause(mins); E.S.add_clause(maxs)
        for p in range(n):
            for q in range(n):
                if p != q and (p+1)+(q+1) > n+1: E.S.add_clause([-mins[p], -maxs[q]])
    for ex in args.extra.split(",") if args.extra else []:
        # v1<=P : value 1 at position <= P (1-based)
        assert ex.startswith("v1<=")
        P = int(ex[4:])
        ms = []
        for p in range(P):
            m = E.new(); ms.append(m)
            for q in range(n):
                if q != p: E.S.add_clause([-m, E.less(p, q)])
        E.S.add_clause(ms)
    added = set()
    def add(pi):
        if pi not in added:
            added.add(pi); E.add_pattern(pi)
    if args.init in ("layered", "all", "near"):
        # layered perms: compositions of k
        for comp in itertools.product([0, 1], repeat=k-1):
            cuts = [i+1 for i, b in enumerate(comp) if b]
            parts, prev = [], 0
            for c in cuts + [k]:
                parts.append(list(range(prev+1, c+1))); prev = c
            pi = tuple(x for part in parts for x in reversed(part))
            add(pi)
            # also reverse-layered (co-layered)
            add(tuple(k+1-x for x in pi))
    if args.init in ("mono",):
        add(tuple(range(1, k+1))); add(tuple(range(k, 0, -1)))
    if args.init == "near":
        for pi in itertools.permutations(range(1, k+1)):
            inv = sum(1 for i in range(k) for j in range(i+1, k) if pi[i] > pi[j])
            if inv <= 3 or inv >= k*(k-1)//2 - 3: add(pi)
    if args.init == "all":
        for pi in itertools.permutations(range(1, k+1)): add(pi)
    t0 = time.time()
    it = 0
    rng = random.Random(args.seed)
    while True:
        it += 1
        ok = E.S.solve()
        el = time.time()-t0
        if not ok:
            print(f"UNSAT k={k} n={n} sym={args.sym} extra='{args.extra}' after {it} iterations, {len(added)} patterns, {E.ncl} pattern clauses, {E.nv} vars, {el:.1f}s", flush=True)
            return 20
        perm = E.decode(E.S.get_model())
        miss = missing_patterns(k, perm)
        print(f"it={it} t={el:.1f}s pats={len(added)} vars={E.nv} missing={len(miss)} perm={' '.join(map(str,perm))}", flush=True)
        if not miss:
            print(f"FOUND k={k} n={n}: {' '.join(map(str,perm))}", flush=True)
            return 10
        rng.shuffle(miss)
        for pi in miss[:args.batch]: add(pi)

if __name__ == "__main__":
    sys.exit(main())
