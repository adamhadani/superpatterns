"""Exp 2 (W15): number of shifts Delta with L_Delta > k/lam for lam in {4, 8, 16}, for pi and pi^{-1}.
Uniform random permutations have max L_Delta ~ 2.5 sqrt(k) (k/lam >> sqrt k is the asymptotic regime)."""
import sys, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import runs_pattern, periodic_word, tilted_grid, L_delta
from exp1_symmetry import inv, comp, perm_rows_grid, block_perturbed_grid, affine, profile
rng = np.random.default_rng(99)

def rep(name, pi):
    k = len(pi)
    row = f"{name:<36} k={k:4d}"
    for lab, p in [('pi', pi), ('pi^-1', inv(pi))]:
        L = profile(p)
        row += f" | {lab:<5} max={L.max()/k:.2f} #>k/4={int((L>k/4).sum()):4d} #>k/8={int((L>k/8).sum()):4d} #>k/16={int((L>k/16).sum()):4d}"
    print(row)

for k in [400, 900]: rep("uniform random", rng.permutation(k))
for l in [20, 30]: rep(f"tilted grid {l}x{l}", tilted_grid(l))
for (r, h) in [(20, 20), (10, 40), (40, 10), (30, 30), (8, 100)]:
    rep(f"grid rows permuted(random tau) r={r} h={h}", perm_rows_grid(r, h, rng.permutation(r)))
for (r, h) in [(20, 20), (30, 30), (10, 60), (60, 10)]:
    for eps in [0.2, 0.45, 0.6]:
        rep(f"block-perturbed r={r} h={h} eps={eps}", block_perturbed_grid(r, h, eps, rng))
for k, a in [(401, 7), (401, 123), (907, 31)]: rep(f"affine k={k} a={a}", affine(k, a))
for k, r in [(400, 8), (400, 32), (900, 30)]:
    pi, w = runs_pattern(k, r, rng); rep(f"random L_{r}", pi); rep(f"random L_{r}^c", comp(pi))
    pi2, _ = runs_pattern(k, r, rng, word=periodic_word(k, r)); rep(f"periodic L_{r}", pi2)
