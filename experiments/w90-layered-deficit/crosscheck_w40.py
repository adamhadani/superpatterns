#!/usr/bin/env python3
"""Independent cross-check of the W90 paired statistic.

L21 is computed by TWO independently written programs on identical inputs:
  (a) experiments/w40-c21-frontier/pruned.c  (segment-tree frontier, written 2026-09-10)
  (b) experiments/w90-layered-deficit/l21_paired.c --stdin  (threshold/pending-apex sweep, this workstream)
LIS is computed here in pure Python (bisect).  Permutations come from numpy's PCG64 generator,
i.e. a different RNG from the xoshiro256** used inside l21_paired.c.

usage: crosscheck_w40.py <w40_binary> <w90_binary> n samples seed
"""
import sys, subprocess, bisect, math
import numpy as np

def lis(a):
    t = []
    for v in a:
        k = bisect.bisect_left(t, v)
        if k == len(t): t.append(v)
        else: t[k] = v
    return len(t)

w40, w90, n, S, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
rng = np.random.default_rng(seed)
B = max(1, min(S, 2_000_000 // n))
mism = 0; sd = 0.0; sd2 = 0.0; sfl = 0.0; done = 0; mismlis = 0
while done < S:
    b = min(B, S - done)
    perms = [rng.permutation(n) + 1 for _ in range(b)]
    text = "".join(str(n) + "\n" + " ".join(map(str, p.tolist())) + "\n" for p in perms).encode()
    o40 = subprocess.run([w40], input=text, capture_output=True, check=True).stdout.split()
    o90 = subprocess.run([w90, "--stdin"], input=text, capture_output=True, check=True).stdout.split()
    for i, p in enumerate(perms):
        a = int(o40[i]); a2 = int(o90[2 * i]); l2 = int(o90[2 * i + 1]); l = lis(p.tolist())
        mism += (a != a2); mismlis += (l != l2)
        d = 2 * a - l; sd += d; sd2 += d * d; sfl += 2 * (l // 2) - 2 * a
    done += b
m = sd / S; v = sd2 / S - m * m
print(f"n={n} S={S} seed={seed} L21_mismatch(w40 vs w90)={mism} LIS_mismatch(py vs C)={mismlis} "
      f"E[2L21-LIS]={m:.4f} +- {math.sqrt(v / S):.4f}  D=E[2floor(LIS/2)-2L21]={sfl / S:.4f} +- {math.sqrt(v / S):.4f} "
      f"D/sqrt(n)={sfl / S / math.sqrt(n):.5f}")
