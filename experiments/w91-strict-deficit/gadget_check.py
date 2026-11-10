#!/usr/bin/env python3
"""W91 -- brute-force checks of the deterministic lemmas behind the strict-deficit theorems.

Everything is computed from the definitions of W90 proof.md section 1 (U_alpha, S_beta, inside points,
board, valid fillings, D-inversions); nothing uses the level shortcuts that the lemmas assert.

Pattern Pi: a list `pat` of blocks (1 = single point, 2 = the block 21) followed by an infinite increasing
tail.  T0 = sum(pat).  Pi[1..t] is the prefix of length t (a prefix ending inside a 21-block ends with a
single maximal point).

Tests (python3 gadget_check.py <test> [args]):
  dp      n trials seed      V-table DP for "points below-left of a corner contain Pi[1..t]" vs brute force
  canon   n trials seed      Lemma 4: consecutive points of the leftmost optimal copy satisfy (O1)-(O6)
  plant   n trials seed      Lemma 2: (O1)-(O4) + planted pi_s  ==> the fibre at (p,b) is the 3-point lens
                             Lemma 3: pairs satisfying (O1)-(O6) + pi_s map injectively to lens levels b
  tie                        explicit configuration with two anchors: (O5) removes exactly one of them
  mecke   T samples seed     Monte Carlo check of the resampling identity with a one-point "plant"
"""
import sys, random, itertools, math

PI = {0: [3, 4, 1, 6, 7, 2, 5], 1: [1, 4, 5, 2, 7, 8, 3, 6]}   # planted order types, s = 0, 1

# ---------------------------------------------------------------- basic geometry on rank grids
def rank(pts):
    n = len(pts)
    xs = sorted(range(n), key=lambda i: pts[i][0]); ys = sorted(range(n), key=lambda i: pts[i][1])
    xr = [0] * n; yr = [0] * n
    for r, i in enumerate(xs): xr[i] = r
    for r, i in enumerate(ys): yr[i] = r
    return xr, yr

def prefix_or(M, n):
    for X in range(n + 1):
        row = M[X]
        for Y in range(n + 1):
            if not row[Y] and ((X and M[X - 1][Y]) or (Y and row[Y - 1])): row[Y] = 1
    return M

def vtables(n, xr, yr, use, pat, tmax):
    """V[t][X][Y] = 1 iff the used points with xr < X and yr < Y contain Pi[1..t]."""
    V = [[bytearray([1]) * (n + 1) for _ in range(n + 1)]]
    def single(Vp):
        M = [bytearray(n + 1) for _ in range(n + 1)]
        for q in use:
            if Vp[xr[q]][yr[q]]: M[xr[q] + 1][yr[q] + 1] = 1
        return prefix_or(M, n)
    def pair(Vp):
        M = [bytearray(n + 1) for _ in range(n + 1)]
        for a in use:
            for b in use:
                if xr[a] < xr[b] and yr[a] > yr[b] and Vp[xr[a]][yr[b]]: M[xr[b] + 1][yr[a] + 1] = 1
        return prefix_or(M, n)
    for blk in pat:
        if len(V) > tmax: break
        base = V[-1]
        V.append(single(base))
        if blk == 2: V.append(pair(base))
    while len(V) <= tmax:
        nxt = single(V[-1]); V.append(nxt)
        if not nxt[n][n]:
            while len(V) <= tmax: V.append([bytearray(n + 1) for _ in range(n + 1)])
    return V[:tmax + 1]

def hstart(n, xr, yr, use):
    """h[q] = longest increasing chain of used points starting at q (q included)."""
    order = sorted(use, key=lambda q: -xr[q]); h = {}
    for q in order:
        best = 0
        for r in h:
            if xr[r] > xr[q] and yr[r] > yr[q] and h[r] > best: best = h[r]
        h[q] = best + 1
    return h

def lt(pts, a, b): return pts[a][0] < pts[b][0] and pts[a][1] < pts[b][1]
def nw(pts, a, b): return pts[a][0] < pts[b][0] and pts[a][1] > pts[b][1]
def inrect(pts, e, x, r): return lt(pts, e, r) and lt(pts, r, x)

class Conf:
    def __init__(self, pts, pat):
        self.pts = pts; self.pat = pat; self.n = n = len(pts); self.T0 = sum(pat)
        self.xr, self.yr = rank(pts); self.all = list(range(n))
        self.V = vtables(n, self.xr, self.yr, self.all, pat, n)
        self.N = max(t for t in range(n + 1) if self.V[t][n][n])
        self.ell = [1 + max(t for t in range(n + 1) if self.V[t][self.xr[q]][self.yr[q]]) for q in self.all]
        self.h = hstart(n, self.xr, self.yr, self.all)

# ---------------------------------------------------------------- fibres, from the definitions
def fibre(C, p, b, maxN=8):
    """Fibre of the configuration for alpha = Pi[1..p], beta = I_b.  Returns (inside, F, a) or None."""
    n, xr, yr, pts = C.n, C.xr, C.yr, C.pts
    def ne_lis(h, use, X, Y):      # longest chain of used points strictly NE of the corner (X, Y)
        return max([h[r] for r in use if xr[r] >= X and yr[r] >= Y], default=0)
    inside = [q for q in C.all if C.V[p][xr[q]][yr[q]] and ne_lis(C.h, C.all, xr[q] + 1, yr[q] + 1) >= b]
    if not inside: return ([], 1, 1)
    if len(inside) > maxN: return None
    O = [q for q in C.all if q not in inside]
    VO = vtables(n, xr, yr, O, C.pat, p)[p]; hO = hstart(n, xr, yr, O)
    X = sorted(xr[q] for q in inside); Y = sorted(yr[q] for q in inside); m = len(X)
    inU = [[bool(VO[X[i]][Y[j]]) for j in range(m)] for i in range(m)]
    inS = [[ne_lis(hO, O, X[i] + 1, Y[j] + 1) >= b for j in range(m)] for i in range(m)]
    F = a = 0
    for f in itertools.permutations(range(m)):
        if all(inU[i][f[i]] and inS[i][f[i]] for i in range(m)):
            F += 1
            if not any(f[i] > f[k] and inU[i][f[k]] and inS[k][f[i]] for i in range(m) for k in range(i + 1, m)):
                a += 1
    return (inside, F, a)

def is_lens(res): return res is not None and len(res[0]) == 3 and res[1] == 3 and res[2] == 2

# ---------------------------------------------------------------- the outside conditions (O1)-(O6)
STRICT = False   # True: tie-breaks (O5'), (O6') without the emptiness clauses (simplified form used in the note)

def outside_ok(C, e, x, s, ties=True, which=None):
    pts, ell, h = C.pts, C.ell, C.h
    out = [r for r in C.all if not inrect(pts, e, x, r)]
    bad = []
    if not ell[e] >= C.T0 + 1: bad.append(1)
    for r in out:
        if r in (e, x): continue
        if lt(pts, r, x):
            if ell[r] > ell[e]: bad.append(2)
        elif lt(pts, e, r):
            if h[r] > h[x]: bad.append(3)
        else:
            if ell[r] >= ell[e] + s + 2 and h[r] >= h[x] + 2: bad.append(4)
    if ties:
        for r in out:
            if r in (e, x): continue
            if ell[r] == ell[e] and nw(pts, r, e) and lt(pts, r, x):
                if STRICT or not any(inrect(pts, r, x, q) for q in out if q != r): bad.append(5)
            if h[r] == h[x] and nw(pts, r, x) and lt(pts, e, r):
                if STRICT or not any(inrect(pts, e, r, q) for q in out if q != r): bad.append(6)
    if which is not None: which.extend(bad)
    return not bad

def content(C, e, x):
    ins = [r for r in C.all if inrect(C.pts, e, x, r)]
    ins.sort(key=lambda r: C.pts[r][0]); ys = sorted(C.pts[r][1] for r in ins)
    return [1 + ys.index(C.pts[r][1]) for r in ins]

def plant(pts, e, x, s, rng):
    m = len(PI[s])
    xs = sorted(rng.uniform(pts[e][0], pts[x][0]) for _ in range(m))
    ys = sorted(rng.uniform(pts[e][1], pts[x][1]) for _ in range(m))
    return pts + [(xs[i], ys[PI[s][i] - 1]) for i in range(m)]

def rand_conf(n, rng, nsw):
    pts = [(rng.random(), rng.random()) for _ in range(n)]
    pat = []
    for _ in range(nsw): pat += [1] * rng.randrange(0, 3) + [2]
    return pts, pat

# ---------------------------------------------------------------- tests
def brute_contains(pts, word):
    """word: list of values (a permutation pattern); brute force over subsets."""
    k = len(word); idx = sorted(range(len(pts)), key=lambda i: pts[i][0])
    for sub in itertools.combinations(idx, k):
        ys = [pts[i][1] for i in sub]; srt = sorted(ys)
        if [1 + srt.index(y) for y in ys] == word: return True
    return k == 0

def prefix_word(pat, t):
    w = []; 
    blocks = list(pat) + [1] * t
    for blk in blocks:
        if len(w) >= t: break
        m = len(w)
        if blk == 1: w.append(m + 1)
        else: w += [m + 2, m + 1]
    w = w[:t]
    srt = sorted(w); return [1 + srt.index(v) for v in w]

def test_dp(n, trials, seed):
    rng = random.Random(seed); checks = 0
    for _ in range(trials):
        pts, pat = rand_conf(n, rng, rng.randrange(0, 3)); C = Conf(pts, pat)
        for t in range(0, n + 1):
            want = brute_contains(pts, prefix_word(pat, t))
            assert bool(C.V[t][n][n]) == want, (pts, pat, t)
            checks += 1
        # also a random corner
        X = rng.randrange(n + 1); Y = rng.randrange(n + 1)
        sub = [pts[q] for q in C.all if C.xr[q] < X and C.yr[q] < Y]
        for t in range(0, len(sub) + 1):
            assert bool(C.V[t][X][Y]) == brute_contains(sub, prefix_word(pat, t)); checks += 1
    print(f"dp: n={n} trials={trials} seed={seed}: {checks} prefix-containment checks, 0 mismatches")

def canonical(C):
    """Leftmost optimal copy in the tail: z[i] for T0+1 <= i <= N (None if the tail is not reached)."""
    if C.N < C.T0 + 1: return {}
    z = {}
    for i in range(C.T0 + 1, C.N + 1):
        G = [q for q in C.all if C.ell[q] == i and C.h[q] == C.N - i + 1]
        assert G, "empty level"
        z[i] = min(G, key=lambda q: C.pts[q][0])
    return z

def test_canon(n, trials, seed):
    rng = random.Random(seed); pairs = 0
    for _ in range(trials):
        pts, pat = rand_conf(n, rng, rng.randrange(0, 4)); C = Conf(pts, pat); z = canonical(C)
        for i in sorted(z):
            if i + 1 not in z: continue
            e, x = z[i], z[i + 1]
            assert lt(pts, e, x) and not content(C, e, x)
            for s in (0, 1):
                w = []
                assert outside_ok(C, e, x, s, which=w), (pts, pat, i, s, w)
            pairs += 1
    print(f"canon: n={n} trials={trials} seed={seed}: {pairs} consecutive pairs of the leftmost optimal copy, "
          f"all chains, all empty rectangles, all satisfy (O1)-(O6) for s=0,1")

def test_plant(n, trials, seed):
    rng = random.Random(seed)
    planted = lens_ok = inj_checked = multi = good_total = withsw = 0
    for _ in range(trials):
        pts, pat = rand_conf(n, rng, rng.randrange(0, 4)); C = Conf(pts, pat)
        cands = [(e, x) for e in C.all for x in C.all if lt(pts, e, x) and not content(C, e, x)]
        rng.shuffle(cands); done = 0
        for e, x in cands:
            if done >= 3: break
            s = rng.randrange(2)
            if not outside_ok(C, e, x, s, ties=False): continue
            done += 1
            C2 = Conf(plant(pts, e, x, s, rng), pat)
            assert content(C2, e, x) == PI[s]
            p = C.ell[e] + s + 1; b = C.h[x] + 1
            res = fibre(C2, p, b); planted += 1; withsw += (C.T0 > 0)
            assert is_lens(res), (pts, pat, e, x, s, res)
            assert sorted(res[0]) == sorted(len(pts) + i for i in ((1, 3, 5) if s == 0 else (2, 4, 6)))
            lens_ok += 1
            # injectivity at this stage p, for both plant sizes
            lens_levels = [bb for bb in range(0, C2.n) if is_lens(fibre(C2, p, bb))]
            for s2 in (0, 1):
                good = []; good_noties = 0
                for e2 in C2.all:
                    if C2.ell[e2] != p - s2 - 1: continue
                    for x2 in C2.all:
                        if not lt(C2.pts, e2, x2) or content(C2, e2, x2) != PI[s2]: continue
                        if outside_ok(C2, e2, x2, s2, ties=False): good_noties += 1
                        if outside_ok(C2, e2, x2, s2): good.append(C2.h[x2] + 1)
                bs = sorted(good)
                assert len(set(bs)) == len(bs) and all(bb in lens_levels for bb in bs), (pts, pat, e, x, s, s2, bs)
                good_total += len(bs); inj_checked += 1
                if good_noties > len(bs): multi += 1
    print(f"plant: n={n} trials={trials} seed={seed}: {planted} plantings on pairs with (O1)-(O4) "
          f"({withsw} with a pattern containing 21-blocks); lens (N=3, F=3, a=2) "
          f"at (p,b)=(ell(e)+s+1, h(x)+1) in {lens_ok}; injectivity checked in {inj_checked} (stage, s) cases, "
          f"{good_total} pairs with (O1)-(O6), all on distinct lens levels; {multi} cases where dropping (O5),(O6) "
          f"gives extra pairs")

def test_tie():
    base = [(0.5, 1.5), (1.0, 1.0), (10.0, 10.0)]
    rng = random.Random(1)
    tmp = plant([base[0], (2.0, 2.0), base[2]], 1, 2, 0, rng)      # plant inside (2,10)^2, above both anchors
    pts = base + tmp[3:]; C = Conf(pts, [])
    p, b = C.ell[1] + 1, C.h[2] + 1
    assert is_lens(fibre(C, p, b))
    r = {}
    for e in (0, 1):
        assert content(C, e, 2) == PI[0]
        r[e] = (outside_ok(C, e, 2, 0, ties=False), outside_ok(C, e, 2, 0))
    assert r[0] == (True, True) and r[1] == (True, False), r
    print("tie: two anchors e'=(0.5,1.5), e=(1,1) below the same planted lens: both satisfy (O1)-(O4), "
          "only the north-west one satisfies (O5): OK")

def test_mecke(T, samples, seed):
    """E #{(e,x): outside conditions, exactly one point in R(e,x)} = E sum_{(e,x): outside, R empty} area(R)."""
    rng = random.Random(seed); lhs = []; rhs = []
    for _ in range(samples):
        k = 0; L = math.exp(-T * T); pr = rng.random()      # Poisson(T^2) by inversion on a product
        while pr > L: k += 1; pr *= rng.random()
        pts = [(rng.uniform(0, T), rng.uniform(0, T)) for _ in range(k)]
        if k < 2: lhs.append(0); rhs.append(0.0); continue
        C = Conf(pts, []); a = 0; bsum = 0.0
        for e in C.all:
            for x in C.all:
                if not lt(pts, e, x): continue
                c = sum(1 for r in C.all if inrect(pts, e, x, r))
                if c > 1 or not outside_ok(C, e, x, 0): continue
                if c == 1: a += 1
                else: bsum += (pts[x][0] - pts[e][0]) * (pts[x][1] - pts[e][1])
        lhs.append(a); rhs.append(bsum)
    def ms(v):
        m = sum(v) / len(v); sd = (sum((t - m) ** 2 for t in v) / (len(v) - 1)) ** 0.5
        return m, sd / len(v) ** 0.5
    d = [lhs[i] - rhs[i] for i in range(samples)]
    print(f"mecke: T={T} samples={samples} seed={seed}: E#(one point inside) = %.4f +- %.4f ; "
          f"E sum area over empty = %.4f +- %.4f ; difference %.4f +- %.4f" % (ms(lhs) + ms(rhs) + ms(d)))

if __name__ == "__main__":
    if sys.argv[1] == "strict":
        STRICT = True; sys.argv.pop(1); print("[strict tie-breaks (O5'), (O6')]", end=" ")
    t = sys.argv[1]
    if t == "dp": test_dp(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif t == "canon": test_canon(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif t == "plant": test_plant(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif t == "tie": test_tie()
    elif t == "mecke": test_mecke(float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
