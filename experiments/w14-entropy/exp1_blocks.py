"""W14 exp1: (a) verify the block formula for L_Delta on run-unions:
   L_Delta(pi) = LIS of the sequence (p(v-Delta))_{v in [Delta,k)} listed in increasing p(v),
   and the free lower bound  L_Delta >= max_{j,j'} |V_j cap (V_{j'}+Delta)|.
   (b) tall-run family: r' tall runs of height h at sparse-ruler offsets, rest random small runs;
   compute F at threshold k/lam, and the max mutually-good set (max clique)."""
import sys, numpy as np, itertools
sys.path.insert(0, '../w9-alon-threads')
from threads import lis_length, L_delta
rng = np.random.default_rng(11)

def pattern_from_word(w, heights):
    """w in [r]^k with counts = heights; run j occupies value interval [S_j, S_j+h_j)."""
    k = len(w); r = len(heights)
    S = np.concatenate([[0], np.cumsum(heights)[:-1]])
    cnt = np.zeros(r, dtype=int); pi = np.empty(k, dtype=int)
    for a in range(k):
        j = w[a]; pi[a] = S[j] + cnt[j]; cnt[j] += 1
    return pi, S

def free_bound(heights, S, d):
    best = 0
    for j in range(len(heights)):
        for jp in range(j+1):
            lo = max(S[j], S[jp] + d); hi = min(S[j] + heights[j], S[jp] + heights[jp] + d)
            best = max(best, hi - lo)
    return best

def max_good_set(G, k):
    """max size of a set T subset {0..k} with all pairwise differences in G (G subset of [1,k])."""
    Gs = set(G)
    best = [1]
    def rec(T, cands):
        if len(T) + len(cands) <= best[0]: return
        if not cands:
            best[0] = max(best[0], len(T)); return
        for idx, c in enumerate(cands):
            newc = [x for x in cands[idx+1:] if (x - c) in Gs]
            rec(T + [c], newc)
            if len(T) + len(cands) - idx - 1 <= best[0]: return
    for t0 in range(0, k+1):
        cands = [x for x in range(t0+1, k+1) if (x - t0) in Gs]
        rec([t0], cands)
        if best[0] >= k+1 - t0: break
    return best[0]

# (a) random heights, random word; check formula and free bound
print("== (a) block formula / free bound check ==")
viol = 0; tight = 0; N = 0
for k, r in [(60, 5), (100, 8), (120, 3), (80, 40)]:
    for trial in range(5):
        cuts = np.sort(rng.choice(np.arange(1, k), r-1, replace=False))
        heights = np.diff(np.concatenate([[0], cuts, [k]]))
        w = np.repeat(np.arange(r), heights); rng.shuffle(w)
        pi, S = pattern_from_word(w, heights)
        for d in range(1, k):
            L = L_delta(pi, d); fb = free_bound(heights, S, d)
            N += 1
            if L < fb: viol += 1
            if L == fb: tight += 1
print(f"instances {N}: violations of L_Delta >= free bound: {viol}; equality: {tight}")

# (b) tall-run family
print("== (b) tall-run family ==")
def tall_family(k, r, rprime, h, ruler, rng):
    """tall runs of height h whose value-starts are ruler[i]*g (g = 2h - 2*thr... chosen by caller);
    the remaining values are split into r - rprime runs of near-equal height, random interleaving."""
    starts = ruler
    # build the value line: tall intervals at given starts (must be disjoint), gaps filled by small runs
    heights = []; kinds = []
    pos = 0
    small_total = k - rprime*h
    nsmall = r - rprime
    gaps = []
    for s in list(starts) + [k]:
        gaps.append(s - pos); pos = s + h
    # distribute small runs over gaps proportionally
    for gi, glen in enumerate(gaps):
        if glen == 0: 
            if gi < len(starts): heights.append(h); kinds.append('T')
            continue
        ns = max(1, round(nsmall * glen / small_total))
        cuts = np.linspace(0, glen, ns+1).astype(int)
        for c in np.diff(cuts):
            if c > 0: heights.append(int(c)); kinds.append('s')
        if gi < len(starts): heights.append(h); kinds.append('T')
    heights = np.array(heights); assert heights.sum() == k, (heights.sum(), k)
    w = np.repeat(np.arange(len(heights)), heights); rng.shuffle(w)
    pi, S = pattern_from_word(w, heights)
    return pi, heights, S, kinds

for (k, lam, ratio) in [(400, 24, 3), (400, 24, 2), (400, 40, 2), (600, 30, 2)]:
    thr = k // lam                     # chain threshold k/lambda
    h = ratio * thr + 1                # tall height
    halfw = h - thr - 1                # |Delta - offset| <= halfw  => chain >= thr+1
    unit = 2*halfw + 1                 # consecutive differences at distance <= unit are covered contiguously
    # sparse ruler marks (in units) covering [0, U] with U*unit >= k/2: use a simple Wichmann-like greedy? use classical ruler
    U = int(np.ceil((k/2) / unit))
    # find a small set of marks in [0, U] with all differences 1..U (sparse ruler) by brute force search over small sizes
    marks = None
    for mcount in range(2, 12):
        for comb in itertools.combinations(range(1, U+1), mcount-1):
            ms = (0,) + comb
            diffs = set(b - a for a in ms for b in ms if b > a)
            if all(d in diffs for d in range(1, U+1)):
                marks = ms; break
        if marks: break
    if marks is None: print("no ruler found", k, lam, ratio); continue
    starts = [m*unit for m in marks]
    # tall runs must be disjoint: unit >= h ?
    ok = all(starts[i+1]-starts[i] >= h for i in range(len(starts)-1)) and starts[-1] + h <= k
    r_total = 60
    pi, heights, S, kinds = tall_family(k, r_total, len(marks), h, starts, rng)
    Ls = np.array([L_delta(pi, d) for d in range(1, k+1)])
    F = [d for d in range(1, k+1) if Ls[d-1] > thr]
    G = [d for d in range(1, k+1) if Ls[d-1] <= thr]
    j = max_good_set(G, k)
    tallpos = len(marks)*h
    print(f"k={k} lam={lam} thr={thr} h={h} unit={unit} U={U} marks={marks} disjoint={ok} "
          f"r'={len(marks)} r={len(heights)} tall positions={tallpos} ({tallpos/k:.3f}k)  "
          f"|F|={len(F)} F covers [1,{max(d for d in range(1,k+1) if all(x in set(F) for x in range(1,d+1)))}]  max good set j={j}")
