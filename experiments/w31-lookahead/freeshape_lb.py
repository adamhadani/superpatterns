#!/usr/bin/env python3
"""W31 §4.3: the 'free-shaping' lower bound  LB_h = (1/h^2) sum_t E[(sum_j sqrt(p_{t,j}))^2]
for uniform sigma in S_h: at time t the t-1 placed values are a uniform (t-1)-subset, the t gaps hold n_j
unplaced values, p_j = n_j/(h-t+1); min_G sum p_j/G_j s.t. sum G_j = h is (sum sqrt p_j)^2/h.
Monte Carlo (exact expectation is a spacing computation; MC is enough for a heuristic).  Usage: freeshape_lb.py h samples"""
import sys, numpy as np
h, S = int(sys.argv[1]), int(sys.argv[2])
rng = np.random.default_rng(0)
tot = 0.0
for _ in range(S):
    perm = rng.permutation(h)             # sigma: values in position order
    placed = np.zeros(h + 2, bool); placed[0] = placed[h + 1] = True  # sentinels at 0 and h+1 (values 1..h)
    for t in range(1, h + 1):
        # gaps between consecutive placed sentinels/values: counts of unplaced values
        idx = np.flatnonzero(placed)
        n = np.diff(idx) - 1
        rem = h - t + 1
        tot += (np.sqrt(n / rem).sum()) ** 2 / h
        placed[perm[t - 1] + 1] = True
print("h=%d  free-shaping LB on Omega_h = %.5f   (pi/8 = 0.39270; blind barrier %.5f)" % (h, tot / S / h, (h + 1) / (2 * h)))
