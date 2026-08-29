"""Exp 3 (W15): is the block-perturbed grid F(r,h,eps) hard for the THREADS or only for the chain BOUND?
For pi in F and the tilted grid, run H-threads at shifts t and t+Delta in a random 2k x m matrix and
record the actual overlap |T_t cap T_{t+Delta}| versus the chain bound L_Delta and versus the 'lag'
(number of elements the follower is behind the leader along the chain: Delta = d*h + e -> lag ~ e*r + d).
Also the joint failure ratio Pr(both fail)/Pr(fail)^2 at m ~ 2k (where single-thread failure is common)."""
import sys, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import run_thread, overlap_stats, tilted_grid, L_delta
from exp1_symmetry import block_perturbed_grid, inv
rng = np.random.default_rng(3)

def overlap_profile(pi, deltas, m, trials):
    k = len(pi); q = 2*k
    out = {}
    for D in deltas:
        sh = []
        for _ in range(trials):
            M = rng.integers(0, 2, size=(q, m), dtype=np.int8)
            T1 = run_thread(M, pi, 'H', 0); T2 = run_thread(M, pi, 'H', D)
            sh.append(overlap_stats(T1, T2)['shared'])
        out[D] = (np.mean(sh), np.max(sh), L_delta(pi, D))
    return out

r = h = 20; k = r*h; m = 4*k
for name, pi in [("tilted grid 20x20", tilted_grid(20)),
                 ("block-perturbed eps=0.2", block_perturbed_grid(r, h, 0.2, rng)),
                 ("block-perturbed eps=0.45", block_perturbed_grid(r, h, 0.45, rng))]:
    print(f"== {name}: k={k}, m={m}; overlap of threads 0 and Delta (mean/max over 40 trials), chain bound L_Delta, lag=e*r+d")
    deltas = [1, 2, 3, 5, 10, 19, 20, 21, 25, 40, 41, 60, 100, 140, 200, 201, 300]
    prof = overlap_profile(pi, deltas, m, 40)
    for D in deltas:
        d, e = divmod(D, h)
        mu, mx, L = prof[D]
        print(f"  Delta={D:4d} (d={d:2d},e={e:2d}, lag={e*r+d:4d})  overlap mean={mu:7.1f} max={mx:4d}   L_Delta={L:4d}")

# joint failure at small m for 3 shifts
print("\n== joint failure: Pr(all 3 threads fail)/Pr(fail)^3, m=2k, shifts (0,D,2D)")
for name, pi in [("tilted grid 20x20", tilted_grid(20)), ("block-perturbed eps=0.2", block_perturbed_grid(r, h, 0.2, rng))]:
    for D in [1, 20, 21, 100, 105]:
        trials = 400; m2 = int(1.6*k); q = 2*k
        f = 0; f3 = 0
        for _ in range(trials):
            M = rng.integers(0, 2, size=(q, m2), dtype=np.int8)
            oks = [run_thread(M, pi, 'H', s)['ok'] for s in (0, D, 2*D)]
            f += sum(1 for o in oks if not o); f3 += all(not o for o in oks)
        pf = f/(3*trials); p3 = f3/trials
        print(f"  {name:<26} D={D:3d}: P(fail)={pf:.3f} P(all3 fail)={p3:.3f} ratio={p3/pf**3 if pf>0 else float('nan'):.2f}")
