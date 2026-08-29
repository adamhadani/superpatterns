"""W14 exp3: verify the explicit construction of proof.md Theorem 2:
T = chain threshold, tall height h = 2T+2, start spacing unit g = 2T+3, ruler marks
{0..a-1} u {2a-1, 3a-1, ..., a^2-1}, a = ceil(sqrt(U+1)), U = ceil((k/2 - T - 1)/g).
Check: L_Delta >= T+1 for all Delta in [1, k/2] (any interleaving!), hence no 3 mutually good shifts."""
import sys, math, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import L_delta
from exp1_blocks import pattern_from_word, max_good_set
rng = np.random.default_rng(3)

def construct(k, T, r_small, rng):
    h = 2*T + 2; g = 2*T + 3
    U = math.ceil((k/2 - T - 1) / g)
    a = math.ceil(math.sqrt(U + 1))
    marks = sorted(set(list(range(a)) + [j*a - 1 for j in range(2, a+1)]))
    starts = [m*g for m in marks]
    assert starts[-1] + h <= k
    heights, kinds = [], []
    pos = 0
    for s in starts + [k]:
        gap = s - pos
        if gap > 0:
            ns = max(1, round(r_small * gap / (k - len(starts)*h)))
            cuts = np.linspace(0, gap, ns + 1).astype(int)
            for c in np.diff(cuts):
                if c > 0: heights.append(int(c)); kinds.append('s')
        if s < k: heights.append(h); kinds.append('T')
        pos = s + h
    heights = np.array(heights); assert heights.sum() == k
    w = np.repeat(np.arange(len(heights)), heights); rng.shuffle(w)
    pi, S = pattern_from_word(w, heights)
    return pi, heights, marks, h, g, U, a

for k, lam in [(400, 20), (600, 30), (800, 40), (1000, 50)]:
    T = math.ceil(k / lam)
    for trial in range(3):
        pi, heights, marks, h, g, U, a = construct(k, T, 50, rng)
        Ls = np.array([L_delta(pi, d) for d in range(1, k+1)])
        bad = Ls > T
        cover = all(bad[:k//2])
        G = [d for d in range(1, k+1) if not bad[d-1]]
        j = max_good_set(G, k) if trial == 0 else None
        rp = len(marks)
        print(f"k={k} lam={lam} T={T} h={h} g={g} U={U} a={a} r'={rp} r={len(heights)} tall frac={rp*h/k:.3f} "
              f"F contains [1,k/2]: {cover}  |F|={bad.sum()}  min L on [1,k/2]={Ls[:k//2].min()}  max good set={j}")
