#!/usr/bin/env python3
"""Aggregate out/hybrid_n*_s*.txt (hybrid_profile.c): cost of converting the first i blocks 12 -> 21."""
import glob, re, math
from collections import defaultdict
for n in (10000, 100000):
    agg = defaultdict(list)
    for f in sorted(glob.glob('out/hybrid_n%d_s*.txt' % n)):
        for line in open(f):
            m = re.match(r'n=(\d+) S=(\d+) i=(\d+) E\[LIS-N_i\]=(-?[\d.]+) \+- ([\d.]+)', line)
            if m: agg[int(m.group(3))].append((int(m.group(2)), float(m.group(4)), float(m.group(5))))
    if not agg: continue
    print("n=%d:  i   samples   E[LIS-N_i]      se     per block = E/(i-1)" % n)
    for i in sorted(agg):
        r = agg[i]; S = sum(x[0] for x in r); m = sum(x[0] * x[1] for x in r) / S
        se = math.sqrt(sum((x[0] * x[2]) ** 2 for x in r)) / S
        print("   %5d  %7d  %10.5f  %8.5f   %s" % (i, S, m, se, ("%.5f +- %.5f" % (m / (i - 1), se / (i - 1))) if i > 1 else "-"))
