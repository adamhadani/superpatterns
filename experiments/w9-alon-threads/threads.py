"""
W9 simulator: greedy threads in a Bernoulli(1/2) matrix M (q rows x m cols).

Matrix convention: M[y, x], y = row (value coordinate), x = column (position coordinate).
A copy of pi in M: columns x_1 < ... < x_k with M[y_j, x_j] = 1 and y ordered as pi.

Thread types
  H  : rows pi(j)+t (t = row shift), elements j = 1..k, scan columns left-to-right.
  Hr : same rows, elements j = k..1, scan columns right-to-left.
  V  : columns pi^{-1}(v)+s (s = column shift), values v = 1..k, scan rows bottom-to-top.
  Vr : same columns, values v = k..1, scan rows top-to-bottom.
Each thread exposes at most one cell per scanned line; it fails if it runs out of lines
before finding k ones.
"""
import numpy as np
from bisect import bisect_left


# ---------- patterns ----------
def runs_pattern(k, r, rng=None, word=None, sizes=None):
    """pi in L_k^{(r)}: values split into r intervals V_1..V_r (sizes ~ k/r);
    the positions with letter j (interleaving word w) get the values of V_j increasingly.
    Returns pi as 0-indexed array pi[pos] = value, and the word w."""
    if sizes is None:
        base, extra = divmod(k, r)
        sizes = [base + (1 if j < extra else 0) for j in range(r)]
    if word is None:
        # random word with exactly sizes[j] copies of letter j
        word = np.concatenate([np.full(sizes[j], j) for j in range(r)])
        rng.shuffle(word)
    word = np.asarray(word)
    starts = np.cumsum([0] + list(sizes[:-1]))
    pi = np.empty(k, dtype=int)
    cnt = [0] * r
    for pos in range(k):
        j = word[pos]
        pi[pos] = starts[j] + cnt[j]
        cnt[j] += 1
    return pi, word


def periodic_word(k, r):
    return np.array([i % r for i in range(k)])


def tilted_grid(l):
    """He-Kwan tilted grid on k = l^2: a*l + b -> b*l + a."""
    k = l * l
    pi = np.empty(k, dtype=int)
    for a in range(l):
        for b in range(l):
            pi[a * l + b] = b * l + a
    return pi


def lis_length(seq):
    tails = []
    for v in seq:
        i = bisect_left(tails, v)
        if i == len(tails):
            tails.append(v)
        else:
            tails[i] = v
    return len(tails)


def L_delta(pi, d):
    """He-Kwan L_Delta(pi): LIS of i -> pi^{-1}(pi(i)+Delta) over i with pi(i)+Delta < k."""
    k = len(pi)
    inv = np.empty(k, dtype=int)
    inv[pi] = np.arange(k)
    seq = [inv[pi[i] + d] for i in range(k) if pi[i] + d < k]
    return lis_length(seq)


# ---------- threads ----------
def run_thread(M, pi, kind, shift, max_ones=None):
    """Run one greedy thread. Returns dict with
       cells: list of (y, x) exposed in order, vals: list of bits, ok: found k ones?,
       elem: list of element index (0..k-1 in scanning order) active at each exposed cell."""
    q, m = M.shape
    k = len(pi)
    inv = np.empty(k, dtype=int)
    inv[pi] = np.arange(k)
    cells, vals, elems = [], [], []
    ones = 0
    if kind == 'H':
        x = 0
        for j in range(k):
            y = pi[j] + shift
            while x < m and M[y, x] == 0:
                cells.append((y, x)); vals.append(0); elems.append(j); x += 1
            if x >= m:
                return dict(cells=cells, vals=vals, elems=elems, ok=False, ones=ones)
            cells.append((y, x)); vals.append(1); elems.append(j); ones += 1; x += 1
        return dict(cells=cells, vals=vals, elems=elems, ok=True, ones=ones)
    if kind == 'Hr':
        x = m - 1
        for j in range(k - 1, -1, -1):
            y = pi[j] + shift
            while x >= 0 and M[y, x] == 0:
                cells.append((y, x)); vals.append(0); elems.append(j); x -= 1
            if x < 0:
                return dict(cells=cells, vals=vals, elems=elems, ok=False, ones=ones)
            cells.append((y, x)); vals.append(1); elems.append(j); ones += 1; x -= 1
        return dict(cells=cells, vals=vals, elems=elems, ok=True, ones=ones)
    if kind == 'V':
        y = 0
        for v in range(k):
            x = inv[v] + shift
            while y < q and M[y, x] == 0:
                cells.append((y, x)); vals.append(0); elems.append(v); y += 1
            if y >= q:
                return dict(cells=cells, vals=vals, elems=elems, ok=False, ones=ones)
            cells.append((y, x)); vals.append(1); elems.append(v); ones += 1; y += 1
        return dict(cells=cells, vals=vals, elems=elems, ok=True, ones=ones)
    if kind == 'Vr':
        y = q - 1
        for v in range(k - 1, -1, -1):
            x = inv[v] + shift
            while y >= 0 and M[y, x] == 0:
                cells.append((y, x)); vals.append(0); elems.append(v); y -= 1
            if y < 0:
                return dict(cells=cells, vals=vals, elems=elems, ok=False, ones=ones)
            cells.append((y, x)); vals.append(1); elems.append(v); ones += 1; y -= 1
        return dict(cells=cells, vals=vals, elems=elems, ok=True, ones=ones)
    raise ValueError(kind)


def overlap_stats(T1, T2):
    """Shared cells between two threads; shared zeros/ones; number of coincidence
    intervals (maximal runs of shared cells consecutive in T1's exposure order)."""
    S1 = {c: v for c, v in zip(T1['cells'], T1['vals'])}
    shared = [(i, c) for i, c in enumerate(T2['cells']) if c in S1]
    n_shared = len(shared)
    zeros = sum(1 for i, c in shared if S1[c] == 0)
    # coincidence intervals: consecutive in T2's order and also consecutive in T1's order
    pos1 = {c: i for i, c in enumerate(T1['cells'])}
    intervals = 0
    prev = None
    for i, c in shared:
        if prev is None or i != prev[0] + 1 or pos1[c] != pos1[prev[1]] + 1:
            intervals += 1
        prev = (i, c)
    return dict(shared=n_shared, zeros=zeros, ones=n_shared - zeros, intervals=intervals)


def max_zero_run(M):
    best = 0
    for row in M:
        run = 0
        for v in row:
            run = run + 1 if v == 0 else 0
            best = max(best, run)
    return best
