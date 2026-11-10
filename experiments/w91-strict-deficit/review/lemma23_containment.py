#!/usr/bin/env python3
"""
Independent check of W91 Lemma 2.3 ("the gadget") through direct pattern containment.

Written from experiments/w91-strict-deficit/proof.md sections 1-2 only, WITHOUT reading gadget_check.py.
Nothing here uses fibres, fillings or the level formulas of Lemma 2.1 to decide containment:

  * contains_dp(points, blocks): decides containment of a direct sum of blocks 1 / 21 by a corner
    dynamic programme (f[i][j] = "the points with x-rank <= i and y-rank <= j contain the prefix").
  * contains_generic(points, perm): plain backtracking matcher for an arbitrary pattern (no direct-sum
    structure used); used on a subsample and in the self-test.
  * contains_brute(points, perm): itertools subset enumeration, used in the self-test only.

Levels   l(q) = 1 + max{t : SW(q) contains Pi[1..t]}     (definition, via contains_dp arrays)
Heights  h(q) = longest increasing chain starting at q    (definition, O(n^2) DP)

Modes
  selftest                     cross-validation of the three containment routines + known counts on S_7, S_8
  plant SEED TRIALS MAXPAIRS   main test of Lemma 2.3 (i), (ii), (iii) + negative controls
  canon SEED TRIALS            Lemma 2.5 from the definitions (bonus)
  canonplant SEED TRIALS       plant into the steps of the leftmost optimal copy; Lemma 2.2 for (O1)-(O6), |G| = 1 (bonus)
"""
import sys, random, itertools, time, collections
import numpy as np

PI = {0: [3, 4, 1, 6, 7, 2, 5], 1: [1, 4, 5, 2, 7, 8, 3, 6]}
BLOCKWORDS = [(), (2,), (2, 2), (1, 2), (2, 1, 1, 2), (1, 1, 2, 2)]   # 1 = single point, 2 = block 21


# ----------------------------------------------------------------------------------------- patterns
def blocks_to_perm(blocks):
    perm, base = [], 0
    for b in blocks:
        if b == 1:
            perm.append(base + 1); base += 1
        else:
            perm += [base + 2, base + 1]; base += 2
    return perm


def standardise(seq):
    order = sorted(seq)
    return [order.index(v) + 1 for v in seq]


def prefix_blocks(B, t):
    """Pi_B[1..t] as a list of direct-sum blocks (Pi_B = B_1 + ... + B_r + 1 + 1 + ...)."""
    out, used = [], 0
    for blk in B:
        if used >= t:
            break
        if blk == 1:
            out.append(1); used += 1
        elif used + 2 <= t:
            out.append(2); used += 2
        else:                      # first entry of an incomplete block 21: a new maximum, i.e. a block 1
            out.append(1); used += 1
    while used < t:
        out.append(1); used += 1
    return out


# ----------------------------------------------------------------------------------------- geometry
def ranks(points):
    n = len(points)
    assert len({p[0] for p in points}) == n and len({p[1] for p in points}) == n, "coordinates not distinct"
    xo = sorted(range(n), key=lambda i: points[i][0])
    yo = sorted(range(n), key=lambda i: points[i][1])
    xr, yr = [0] * n, [0] * n
    for r, i in enumerate(xo):
        xr[i] = r + 1
    for r, i in enumerate(yo):
        yr[i] = r + 1
    return xr, yr


def step1(f, xr, yr):
    n = len(xr)
    g = np.zeros((n + 1, n + 1), dtype=bool)
    for a, b in zip(xr, yr):
        if f[a - 1, b - 1]:
            g[a, b] = True
    g = np.logical_or.accumulate(g, axis=0)
    return np.logical_or.accumulate(g, axis=1)


def step21(f, xr, yr):
    n = len(xr)
    g = np.zeros((n + 1, n + 1), dtype=bool)
    pts = sorted(zip(xr, yr))
    for i in range(n):
        xa, ya = pts[i]
        for j in range(i + 1, n):
            xb, yb = pts[j]
            if ya > yb and f[xa - 1, yb - 1]:      # a NW of b, earlier blocks strictly below-left of both
                g[xb, ya] = True
    g = np.logical_or.accumulate(g, axis=0)
    return np.logical_or.accumulate(g, axis=1)


def dp_array(xr, yr, blocks):
    n = len(xr)
    f = np.ones((n + 1, n + 1), dtype=bool)
    for b in blocks:
        f = step1(f, xr, yr) if b == 1 else step21(f, xr, yr)
        if not f[n, n]:
            return np.zeros((n + 1, n + 1), dtype=bool)
    return f


def contains_dp(points, blocks):
    xr, yr = ranks(points)
    return bool(dp_array(xr, yr, blocks)[len(points), len(points)])


def contains_generic(points, pat, node_limit=None):
    """Backtracking matcher for an arbitrary pattern. Returns True/False (or None if node_limit hit)."""
    xr, yr = ranks(points)
    n, k = len(points), len(pat)
    ys = [0] * n
    for i in range(n):
        ys[xr[i] - 1] = yr[i]
    lo_idx, hi_idx = [], []
    for j in range(k):
        lo = hi = None
        for i in range(j):
            if pat[i] < pat[j] and (lo is None or pat[i] > pat[lo]):
                lo = i
            if pat[i] > pat[j] and (hi is None or pat[i] < pat[hi]):
                hi = i
        lo_idx.append(lo); hi_idx.append(hi)
    chosen = [0] * k
    nodes = [0]

    def rec(j, start):
        if j == k:
            return True
        lo = ys[chosen[lo_idx[j]]] if lo_idx[j] is not None else 0
        hi = ys[chosen[hi_idx[j]]] if hi_idx[j] is not None else n + 1
        for i in range(start, n - (k - j) + 1):
            if lo < ys[i] < hi:
                nodes[0] += 1
                if node_limit is not None and nodes[0] > node_limit:
                    raise TimeoutError
                chosen[j] = i
                if rec(j + 1, i + 1):
                    return True
        return False

    try:
        return rec(0, 0)
    except TimeoutError:
        return None


def contains_brute(points, pat):
    pts = sorted(points)
    k = len(pat)
    for sub in itertools.combinations(pts, k):
        if standardise([p[1] for p in sub]) == list(pat):
            return True
    return False


def heights(xr, yr):
    n = len(xr)
    order = sorted(range(n), key=lambda i: -xr[i])
    h = [1] * n
    for pos, i in enumerate(order):
        best = 0
        for j in order[:pos]:
            if yr[j] > yr[i] and h[j] > best:
                best = h[j]
        h[i] = best + 1
    return h


def analyse(points, B):
    """levels, heights and N = N_Pi(P), all from the definitions."""
    n = len(points)
    xr, yr = ranks(points)
    F = [np.ones((n + 1, n + 1), dtype=bool)]
    cur = F[0]
    for blk in B:
        if blk == 1:
            cur = step1(cur, xr, yr); F.append(cur)
        else:
            F.append(step1(cur, xr, yr))          # Pi[1..t] ending inside a block 21 = (complete blocks) + 1
            cur = step21(cur, xr, yr); F.append(cur)
    while F[-1][n, n]:
        cur = step1(cur, xr, yr); F.append(cur)
    N = max(t for t in range(len(F)) if F[t][n, n])
    lev = [1 + max(t for t in range(len(F)) if F[t][xr[i] - 1, yr[i] - 1]) for i in range(n)]
    return xr, yr, lev, heights(xr, yr), N


def lt(xr, yr, a, b):
    return xr[a] < xr[b] and yr[a] < yr[b]


def in_rect(xr, yr, k, e, x):
    return xr[e] < xr[k] < xr[x] and yr[e] < yr[k] < yr[x]


def conds_O1234(xr, yr, lev, hgt, e, x, s, T0):
    """(O1)-(O4) exactly as in section 2; points inside R(e,x) are skipped (they are in no class)."""
    n = len(xr)
    o1 = lev[e] >= T0 + 1
    o2 = o3 = o4 = True
    for r in range(n):
        if r == e or r == x or in_rect(xr, yr, r, e, x):
            continue
        below_x = lt(xr, yr, r, x)
        above_e = lt(xr, yr, e, r)
        assert not (below_x and above_e)
        if below_x:                                   # class (a)
            if lev[r] > lev[e]:
                o2 = False
        elif above_e:                                 # class (b)
            if hgt[r] > hgt[x]:
                o3 = False
        else:                                         # class (c)
            assert (xr[r] > xr[x] and yr[r] < yr[e]) or (xr[r] < xr[e] and yr[r] > yr[x])
            if lev[r] >= lev[e] + s + 2 and hgt[r] >= hgt[x] + 2:
                o4 = False
    return o1, o2, o3, o4


def conds_O56(xr, yr, lev, hgt, e, x):
    n = len(xr)
    o5 = o6 = True
    for q in range(n):
        if q == e or q == x or in_rect(xr, yr, q, e, x):
            continue
        # (O5): q = e' of class (a), same level as e, NW of e, (R(e',x) \ R) cap P empty
        if lt(xr, yr, q, x) and lev[q] == lev[e] and xr[q] < xr[e] and yr[q] > yr[e]:
            if not any(in_rect(xr, yr, z, q, x) and not in_rect(xr, yr, z, e, x) for z in range(n)):
                o5 = False
        # (O6): q = x' of class (b), same height as x, NW of x, (R(e,x') \ R) cap P empty
        if lt(xr, yr, e, q) and hgt[q] == hgt[x] and xr[q] < xr[x] and yr[q] > yr[x]:
            if not any(in_rect(xr, yr, z, e, q) and not in_rect(xr, yr, z, e, x) for z in range(n)):
                o6 = False
    return o5, o6


def plant(points, e, x, s, rng):
    (xe, ye), (xx, yx) = points[e], points[x]
    m = 7 + s
    xs = sorted(rng.uniform(xe, xx) for _ in range(m))
    ysv = sorted(rng.uniform(ye, yx) for _ in range(m))
    assert xe < xs[0] and xs[-1] < xx and ye < ysv[0] and ysv[-1] < yx
    new = [(xs[k], ysv[PI[s][k] - 1]) for k in range(m)]
    return points + new, list(range(len(points), len(points) + m))


def inside_set(points, alpha, b):
    """indices q with SW(q) containing alpha and NE(q) containing I_b (definition of inside point)."""
    xr, yr = ranks(points)
    fa = dp_array(xr, yr, alpha)
    h = heights(xr, yr)
    return [q for q in range(len(points)) if fa[xr[q] - 1, yr[q] - 1] and h[q] >= b + 1]


def board(points, inside, alpha, b):
    """Board of W90 section 1 from the definition: cells (x,y) in X x Y lying in U_alpha(O) and S_beta(O)."""
    O = [p for i, p in enumerate(points) if i not in set(inside)]
    X = sorted(points[i][0] for i in inside)
    Y = sorted(points[i][1] for i in inside)
    xr, yr = ranks(O)
    fa = dp_array(xr, yr, alpha)
    inU = [[False] * len(Y) for _ in X]
    inS = [[False] * len(Y) for _ in X]
    for i, cx in enumerate(X):
        for j, cy in enumerate(Y):
            ix = sum(1 for o in O if o[0] < cx)
            iy = sum(1 for o in O if o[1] < cy)
            inU[i][j] = bool(fa[ix, iy])
            ne = [o for o in O if o[0] > cx and o[1] > cy]
            if b == 0:
                inS[i][j] = True
            elif ne:
                nxr, nyr = ranks(ne)
                inS[i][j] = max(heights(nxr, nyr)) >= b
    return inU, inS


def is_lens(points, alpha, b):
    ins = inside_set(points, alpha, b)
    if len(ins) != 3:
        return False, ins
    inU, inS = board(points, ins, alpha, b)
    ok = True
    for i in range(3):
        for j in range(3):
            cell = inU[i][j] and inS[i][j]
            if (i, j) == (0, 0):
                ok &= (not inU[0][0])
            elif (i, j) == (2, 2):
                ok &= (not inS[2][2])
            else:
                ok &= cell
    return ok, ins



def order_type_in_rect(points, xr, yr, e, x):
    inside = sorted((xr[k], yr[k]) for k in range(len(points)) if in_rect(xr, yr, k, e, x))
    return standardise([p[1] for p in inside])


def injectivity_counts(P1, B, p, s):
    """|G_{p,s}(P1)| with (O1)-(O6), the same count with (O1)-(O4) only, and the number of lens levels b
    for alpha = Pi[1..p]; everything from the definitions."""
    T0 = sum(B)
    n = len(P1)
    xr, yr, lev, hgt, N = analyse(P1, B)
    g6 = g4 = 0
    for e in range(n):
        if lev[e] != p - s - 1:
            continue
        for x in range(n):
            if not lt(xr, yr, e, x):
                continue
            if order_type_in_rect(P1, xr, yr, e, x) != PI[s]:
                continue
            if all(conds_O1234(xr, yr, lev, hgt, e, x, s, T0)):
                g4 += 1
                if all(conds_O56(xr, yr, lev, hgt, e, x)):
                    g6 += 1
    alpha = prefix_blocks(B, p)
    lens_levels = [b for b in range(0, max(hgt) + 1) if is_lens(P1, alpha, b)[0]]
    return g6, g4, lens_levels


ARR_FIBRE = ["231", "312", "321"]
ARR_OTHER = ["123", "132", "213"]


def gadget_test(points, B, e, x, s, rng, do_generic=False):
    """Plant pi_s into R(e,x) and test the conclusions of Lemma 2.3 by direct containment."""
    T0 = sum(B)
    P1, idx = plant(points, e, x, s, rng)
    xr, yr, lev, hgt, N1 = analyse(P1, B)
    res = {"P1": P1, "idx": idx}
    res["O_after"] = conds_O1234(xr, yr, lev, hgt, e, x, s, T0)
    res["lev_e"], res["h_x"] = lev[e], hgt[x]
    p, b = lev[e] + s + 1, hgt[x] + 1
    res["p"], res["b"] = p, b
    alpha = prefix_blocks(B, p)
    A12 = alpha + [1, 1] + [1] * b
    A21 = alpha + [2] + [1] * b
    lens_idx = [idx[1 + s], idx[3 + s], idx[5 + s]]                # p1, p2, p3 (x-order)
    X = [P1[i][0] for i in lens_idx]
    Y = sorted(P1[i][1] for i in lens_idx)
    assert [Y.index(P1[i][1]) + 1 for i in lens_idx] == [2, 3, 1]   # planted arrangement is 231
    res["cont"] = {}
    res["inside3"] = {}
    for arr in ARR_FIBRE + ARR_OTHER:
        P2 = list(P1)
        for k, i in enumerate(lens_idx):
            P2[i] = (X[k], Y[int(arr[k]) - 1])
        c12, c21 = contains_dp(P2, A12), contains_dp(P2, A21)
        res["cont"][arr] = (c12, c21)
        ins = set(inside_set(P2, alpha, b))
        res["inside3"][arr] = tuple(i in ins for i in lens_idx)
        if arr == "231":
            res["inside_is_lens_points"] = (ins == set(lens_idx))
            res["lens"] = is_lens(P2, alpha, b)[0]
        if do_generic:
            g12 = contains_generic(P2, blocks_to_perm(A12), node_limit=3_000_000)
            g21 = contains_generic(P2, blocks_to_perm(A21), node_limit=3_000_000)
            res.setdefault("generic", {})[arr] = (g12, g21)
    return res


def verdict(res):
    """dict of pass/fail for (i), (ii) and the from-definitions lens check."""
    c = res["cont"]
    v = {}
    v["i"] = (c["231"] == (True, False))
    v["ii"] = (sum(c[a][0] for a in ARR_FIBRE) == 2 and sum(c[a][1] for a in ARR_FIBRE) == 1)
    v["inside"] = res["inside_is_lens_points"]
    v["lens"] = res["lens"]
    return v


def dump(points, B, e, x, s, res, tag):
    print("=" * 20, tag)
    print("block word (1 = point, 2 = block 21):", B, " s =", s)
    print("e index", e, points[e], " x index", x, points[x])
    print("base points:", repr(points))
    print("planted config:", repr(res["P1"]))
    print("p, b =", res["p"], res["b"], " containment (a+12+I_b, a+21+I_b) per arrangement:", res["cont"])
    print("inside flags of the three lens points per arrangement:", res["inside3"])
    sys.stdout.flush()


# ----------------------------------------------------------------------------------------- modes
def mode_selftest():
    rng = random.Random(1)
    # 1. prefix_blocks against "first t entries of the infinite pattern, standardised"
    cnt = 0
    for B in BLOCKWORDS + [(2, 2, 2), (1, 2, 1, 2, 2)]:
        full = blocks_to_perm(list(B) + [1] * 12)
        for t in range(0, 12):
            assert blocks_to_perm(prefix_blocks(B, t)) == standardise(full[:t]), (B, t)
            cnt += 1
    print(f"selftest 1: prefix_blocks == standardised prefix in {cnt} cases")
    # 2. DP and generic matcher against subset enumeration
    cnt = mism = 0
    for _ in range(4000):
        n = rng.randint(1, 9)
        pts = [(rng.random(), rng.random()) for _ in range(n)]
        blocks = [rng.choice([1, 1, 2]) for _ in range(rng.randint(0, 4))]
        pat = blocks_to_perm(blocks)
        a, b, c = contains_dp(pts, blocks), contains_generic(pts, pat), contains_brute(pts, pat)
        cnt += 1
        mism += (a != c) + (b != c)
    print(f"selftest 2: DP / generic / brute force on {cnt} random (config, direct-sum pattern) pairs: {mism} mismatches")
    cnt = mism = 0
    for _ in range(3000):
        n = rng.randint(1, 9)
        pts = [(rng.random(), rng.random()) for _ in range(n)]
        k = rng.randint(1, 5)
        pat = list(range(1, k + 1)); rng.shuffle(pat)
        cnt += 1
        mism += contains_generic(pts, pat) != contains_brute(pts, pat)
    print(f"selftest 3: generic matcher / brute force on {cnt} random arbitrary patterns: {mism} mismatches")
    # 3. known counts: |Av_n(1324)| - |Av_n(1234)| = 1 (n=7), 26 (n=8)
    for n, want in ((7, 1), (8, 26)):
        c1234 = c1324 = 0
        for perm in itertools.permutations(range(1, n + 1)):
            pts = list(enumerate(perm))
            c1234 += contains_dp(pts, [1, 1, 1, 1])
            c1324 += contains_dp(pts, [1, 2, 1])
        print(f"selftest 4: S_{n}: #contain 1234 - #contain 1324 = {c1234 - c1324} (expected {want})")
    # 4. the smallest instance quoted in section 8
    pts = list(enumerate([1, 4, 5, 2, 7, 8, 3, 6, 9]))
    print("selftest 5: 145278369 contains 123456:", contains_dp(pts, [1] * 6), " contains 124356:",
          contains_dp(pts, [1, 1, 2, 1, 1]), " (generic:", contains_generic(pts, [1, 2, 3, 4, 5, 6]),
          contains_generic(pts, [1, 2, 4, 3, 5, 6]), ")")


def mode_plant(seed, trials, maxpairs, generic_every=25):
    rng = random.Random(seed)
    t0 = time.time()
    C = collections.Counter()
    slack_hist = collections.Counter()
    other = {a: collections.Counter() for a in ARR_OTHER}
    fibre_detail = collections.Counter()
    neg = collections.Counter()
    nfail_printed = 0
    ntest = 0
    for trial in range(trials):
        n = rng.randint(20, 40)
        pts = [(rng.random(), rng.random()) for _ in range(n)]
        for B in BLOCKWORDS:
            T0 = sum(B)
            xr, yr, lev, hgt, N = analyse(pts, B)
            good = {0: [], 1: []}
            bad = []
            for e in range(n):
                for x in range(n):
                    if not lt(xr, yr, e, x):
                        continue
                    if any(in_rect(xr, yr, k, e, x) for k in range(n)):
                        continue
                    for s in (0, 1):
                        o = conds_O1234(xr, yr, lev, hgt, e, x, s, T0)
                        if all(o):
                            good[s].append((e, x))
                        elif sum(o) == 3:
                            bad.append((e, x, s, o.index(False) + 1))
            for s in (0, 1):
                C[("candidates", s)] += len(good[s])
                for (e, x) in rng.sample(good[s], min(maxpairs, len(good[s]))):
                    ntest += 1
                    res = gadget_test(pts, B, e, x, s, rng, do_generic=(ntest % generic_every == 0))
                    v = verdict(res)
                    key = "identity" if not B else "with21"
                    C[("tests", key)] += 1
                    C[("tests_s", s)] += 1
                    C[("tests_B", B)] += 1
                    slack_hist[N - lev[e] - hgt[x]] += 1
                    # Lemma 2.2: values and conditions unchanged by the planting
                    C["lemma2.2_ok"] += (res["lev_e"] == lev[e] and res["h_x"] == hgt[x] and all(res["O_after"]))
                    C["i_ok"] += v["i"]; C["ii_ok"] += v["ii"]
                    C["inside_ok"] += v["inside"]; C["lens_ok"] += v["lens"]
                    fibre_detail[tuple(res["cont"][a] for a in ARR_FIBRE)] += 1
                    g6, g4, ll = injectivity_counts(res["P1"], B, res["p"], s)
                    C[("G6", g6)] += 1
                    C[("G4", min(g4, 3))] += 1
                    C[("lenslevels", len(ll))] += 1
                    C["lens_level_is_b"] += (ll == [res["b"]])
                    C["inj_ok"] += (g6 <= 1 and g6 <= len(ll) and len(ll) <= 1)
                    if not (g6 <= 1 and g6 <= len(ll) and len(ll) <= 1) and nfail_printed < 10:
                        nfail_printed += 1
                        dump(pts, B, e, x, s, res, f"COUNTEREXAMPLE to Lemma 2.4 / Remark 2.6: |G|={g6}, lens levels {ll}")
                    for a in ARR_OTHER:
                        other[a][(res["inside3"][a], res["cont"][a])] += 1
                        C[("iii_some_point_not_inside", a)] += (not all(res["inside3"][a]))
                    if "generic" in res:
                        for a in ARR_FIBRE + ARR_OTHER:
                            g = res["generic"][a]
                            for which in (0, 1):
                                if g[which] is None:
                                    C["generic_timeout"] += 1
                                else:
                                    C["generic_compared"] += 1
                                    C["generic_mismatch"] += (g[which] != res["cont"][a][which])
                    if not (v["i"] and v["ii"] and v["inside"] and v["lens"]) and nfail_printed < 10:
                        nfail_printed += 1
                        dump(pts, B, e, x, s, res, "COUNTEREXAMPLE to Lemma 2.3 " + str(v))
            # negative controls: exactly one of (O1)-(O4) fails
            negsel = []
            for w in (1, 2, 3, 4):
                bw = [t for t in bad if t[3] == w]
                negsel += rng.sample(bw, min(maxpairs, len(bw)))
            for (e, x, s, which) in negsel:
                res = gadget_test(pts, B, e, x, s, rng)
                v = verdict(res)
                neg[(which, "tested")] += 1
                neg[(which, "i_fails")] += (not v["i"])
                neg[(which, "ii_fails")] += (not v["ii"])
                neg[(which, "lens_fails")] += (not v["lens"])
    T = sum(v for k, v in C.items() if isinstance(k, tuple) and k[0] == "tests")
    print(f"plant: seed={seed} trials={trials} maxpairs={maxpairs}: configurations of 20-40 random points, "
          f"{len(BLOCKWORDS)} block words each; {time.time() - t0:.0f}s")
    print(f"  candidate pairs with empty rectangle and (O1)-(O4): s=0: {C[('candidates', 0)]}, s=1: {C[('candidates', 1)]}")
    print(f"  plantings tested: {T}  (identity pattern: {C[('tests', 'identity')]}, patterns with 21-blocks: "
          f"{C[('tests', 'with21')]}; s=0: {C[('tests_s', 0)]}, s=1: {C[('tests_s', 1)]})")
    print("  per block word:", {str(B): C[("tests_B", B)] for B in BLOCKWORDS})
    print("  histogram of N - l(e) - h(x) over tested pairs (0 = pair lies on an optimal copy):",
          dict(sorted(slack_hist.items())))
    print(f"  Lemma 2.2 (l(e), h(x), (O1)-(O4) unchanged by planting): {C['lemma2.2_ok']}/{T}")
    print(f"  (i)   planted config contains a+12+I_b and avoids a+21+I_b: {C['i_ok']}/{T}")
    print(f"  (ii)  among 231/312/321 exactly two contain a+12+I_b and exactly one contains a+21+I_b: {C['ii_ok']}/{T}")
    print("        detail ((c12,c21) for 231, 312, 321):", dict(fibre_detail))
    print(f"  inside set for (Pi[1..p], I_b) equals {{p1,p2,p3}} (from the definition): {C['inside_ok']}/{T}")
    print(f"  board = 3x3 minus (x1,y1) not in U, (x3,y3) not in S (from the definition, on O): {C['lens_ok']}/{T}")
    print(f"  Lemma 2.4 / Remark 2.6 in the planted configuration (alpha = Pi[1..p]): |G_(p,s)| <= #lens levels <= 1 in "
          f"{C['inj_ok']}/{T}; the set of lens levels is exactly {{h(x)+1}} in {C['lens_level_is_b']}/{T}")
    print("        |G_(p,s)| with (O1)-(O6):", {k[1]: v for k, v in sorted(C.items(), key=str) if isinstance(k, tuple) and k[0] == 'G6'},
          " pairs with (O1)-(O4) only (3 = 3 or more):", {k[1]: v for k, v in sorted(C.items(), key=str) if isinstance(k, tuple) and k[0] == 'G4'},
          " #lens levels:", {k[1]: v for k, v in sorted(C.items(), key=str) if isinstance(k, tuple) and k[0] == 'lenslevels'})
    for a in ARR_OTHER:
        print(f"  (iii) arrangement {a}: some lens point no longer inside in {C[('iii_some_point_not_inside', a)]}/{T}; "
              f"breakdown (inside flags of (x1,.),(x2,.),(x3,.)) , (contains a+12+I_b, contains a+21+I_b)) -> count:")
        for k, v in sorted(other[a].items(), key=lambda kv: -kv[1]):
            print("          ", k, v)
    print(f"  generic backtracking matcher vs DP on a subsample: {C['generic_compared']} containment decisions compared, "
          f"{C['generic_mismatch']} mismatches, {C['generic_timeout']} node-limit timeouts")
    print("  negative controls (exactly one of (O1)-(O4) violated; conclusion need not hold):")
    for which in (1, 2, 3, 4):
        print(f"     (O{which}) violated: tested {neg[(which, 'tested')]}, (i) fails {neg[(which, 'i_fails')]}, "
              f"(ii) fails {neg[(which, 'ii_fails')]}, lens-from-definition fails {neg[(which, 'lens_fails')]}")
    sys.stdout.flush()


def mode_canon(seed, trials):
    """Lemma 2.5 from the definitions."""
    rng = random.Random(seed)
    C = collections.Counter()
    for trial in range(trials):
        n = rng.randint(20, 40)
        pts = [(rng.random(), rng.random()) for _ in range(n)]
        for B in BLOCKWORDS:
            T0 = sum(B)
            xr, yr, lev, hgt, N = analyse(pts, B)
            if N < T0 + 2:
                C["skipped_N_small"] += 1
                continue
            z = {}
            for i in range(T0 + 1, N + 1):
                G = [q for q in range(n) if lev[q] == i and hgt[q] == N - i + 1]
                if not G:
                    C["G_empty"] += 1
                    print("G_i EMPTY", B, i, N, repr(pts))
                    continue
                z[i] = min(G, key=lambda q: xr[q])
            for i in range(T0 + 1, N):
                if i not in z or i + 1 not in z:
                    continue
                e, x = z[i], z[i + 1]
                C["pairs"] += 1
                ok = lt(xr, yr, e, x) and not any(in_rect(xr, yr, k, e, x) for k in range(n))
                for s in (0, 1):
                    ok = ok and all(conds_O1234(xr, yr, lev, hgt, e, x, s, T0))
                ok = ok and all(conds_O56(xr, yr, lev, hgt, e, x))
                C["ok"] += ok
                if not ok and C["printed"] < 5:
                    C["printed"] += 1
                    print("COUNTEREXAMPLE to Lemma 2.5", B, "i =", i, "e", pts[e], "x", pts[x], repr(pts))
    print(f"canon: seed={seed} trials={trials}: {C['pairs']} consecutive pairs (z_i, z_i+1) of the leftmost optimal copy; "
          f"chain + empty rectangle + (O1)-(O6) for s=0,1 hold in {C['ok']}; empty G_i: {C['G_empty']}; "
          f"skipped (N < T0+2): {C['skipped_N_small']}")


def mode_canonplant(seed, trials):
    """Plant into every step (z_i, z_i+1) of the leftmost optimal copy (the pair actually used in Lemma 3.2):
    (O1)-(O6) must survive the planting (Lemma 2.2), the gadget conclusions must hold, and |G_(p,s)| must be 1."""
    rng = random.Random(seed)
    C = collections.Counter()
    t0 = time.time()
    for trial in range(trials):
        n = rng.randint(20, 40)
        pts = [(rng.random(), rng.random()) for _ in range(n)]
        for B in BLOCKWORDS:
            T0 = sum(B)
            xr, yr, lev, hgt, N = analyse(pts, B)
            if N < T0 + 2:
                continue
            z = {i: min((q for q in range(n) if lev[q] == i and hgt[q] == N - i + 1), key=lambda q: xr[q])
                 for i in range(T0 + 1, N + 1)}
            for i in range(T0 + 1, N):
                e, x = z[i], z[i + 1]
                for s in (0, 1):
                    res = gadget_test(pts, B, e, x, s, rng)
                    v = verdict(res)
                    P1 = res["P1"]
                    xr1, yr1, lev1, hgt1, N1 = analyse(P1, B)
                    o_all = all(conds_O1234(xr1, yr1, lev1, hgt1, e, x, s, T0)) and all(conds_O56(xr1, yr1, lev1, hgt1, e, x))
                    g6, g4, ll = injectivity_counts(P1, B, res["p"], s)
                    C["tests"] += 1
                    C["with21"] += bool(B)
                    C["p_is_i+s+1"] += (res["p"] == i + s + 1 and res["b"] == N - i + 1)
                    C["N1_is_N+s+4"] += (N1 == N + s + 4)
                    C["O1-6_after"] += o_all
                    C["gadget_ok"] += (v["i"] and v["ii"] and v["inside"] and v["lens"])
                    C["G_is_1"] += (g6 == 1)
                    C["lens_levels_ok"] += (ll == [res["b"]])
                    if not (o_all and v["i"] and v["ii"] and v["inside"] and v["lens"] and g6 == 1) and C["printed"] < 5:
                        C["printed"] += 1
                        dump(pts, B, e, x, s, res, f"COUNTEREXAMPLE (canonplant) i={i} |G|={g6} O1-6 after planting={o_all} {v}")
    T = C["tests"]
    print(f"canonplant: seed={seed} trials={trials}: {T} plantings into steps of the leftmost optimal copy "
          f"({C['with21']} with 21-blocks in the pattern); {time.time() - t0:.0f}s")
    print(f"  (p, b) = (i+s+1, N-i+1): {C['p_is_i+s+1']}/{T};  N of the planted configuration = N+s+4: {C['N1_is_N+s+4']}/{T}")
    print(f"  (O1)-(O6) still hold after planting (Lemma 2.2 for all six conditions): {C['O1-6_after']}/{T}")
    print(f"  (i), (ii), inside set, board all as in Lemma 2.3: {C['gadget_ok']}/{T}")
    print(f"  |G_(p,s)| = 1 exactly: {C['G_is_1']}/{T};  lens levels = {{b}}: {C['lens_levels_ok']}/{T}")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "selftest":
        mode_selftest()
    elif mode == "plant":
        mode_plant(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),
                   int(sys.argv[5]) if len(sys.argv) > 5 else 25)
    elif mode == "canon":
        mode_canon(int(sys.argv[2]), int(sys.argv[3]))
    elif mode == "canonplant":
        mode_canonplant(int(sys.argv[2]), int(sys.argv[3]))
