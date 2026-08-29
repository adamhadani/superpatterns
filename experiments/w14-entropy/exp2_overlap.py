"""W14 exp2: actual thread overlap for the tall-run family vs the chain bound, and the
closed form L_{dh+e} = max((h-e)(r-d), e(r-d-1)) for periodic words."""
import sys, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import run_thread, overlap_stats, L_delta, periodic_word, runs_pattern
from exp1_blocks import pattern_from_word, tall_family
rng = np.random.default_rng(5)

# closed form check
print("== periodic closed form ==")
bad = 0; tot = 0
for k, r in [(60, 5), (120, 8), (200, 4), (200, 40)]:
    h = k // r
    pi, w = runs_pattern(k, r, rng, word=periodic_word(k, r))
    for D in range(1, k):
        d, e = divmod(D, h)
        cf = max((h - e) * (r - d), e * (r - d - 1))
        tot += 1
        if cf != L_delta(pi, D): bad += 1
print(f"closed form mismatches: {bad}/{tot}")

# overlap for tall family, k=200, m = 6k (failure regime-ish), Delta in the covered range
print("== overlap: tall-run family, k=200 ==")
k = 200; lam = 24; thr = k // lam; h = 2 * thr + 1; halfw = h - thr - 1; unit = 2 * halfw + 1
marks = (0, 1, 2, 4); starts = [m * unit for m in marks]
pi, heights, S, kinds = tall_family(k, 40, len(marks), h, starts, rng)
m = 6 * k; q = 2 * k
for D in [1, 4, unit, 2 * unit, 3 * unit, 4 * unit, 100]:
    L = L_delta(pi, D)
    sh = []; W = []
    for trial in range(40):
        M = rng.integers(0, 2, size=(q, m))
        T1 = run_thread(M, pi, 'H', 0); T2 = run_thread(M, pi, 'H', D)
        sh.append(overlap_stats(T1, T2)['shared'])
    print(f"Delta={D:3d} L_Delta={L:3d} (thr {thr}) mean shared cells={np.mean(sh):6.2f} max={max(sh)}  (m={m})")
