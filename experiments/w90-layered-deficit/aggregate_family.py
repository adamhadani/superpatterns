#!/usr/bin/env python3
"""Aggregate out/fam_*.txt (layered_paired.c) and out/cross_*.txt (crosscheck_w40.py)."""
import glob, re, math
from collections import defaultdict
pat = re.compile(r'sizes=(\S+) n=(\d+) S=(\d+) E\[LIS\]=([\d.]+) E\[K\]=([\d.]+) E\[K-LIS\]=(-?[\d.]+) \+- ([\d.]+) \(sd ([\d.]+)\) D=E\[K_I-K\]=(-?[\d.]+) \+- ([\d.]+)')
agg = defaultdict(list)
for f in sorted(glob.glob('out/fam_*.txt')):
    for line in open(f):
        m = pat.match(line)
        if m:
            g = m.groups()
            agg[(g[0], int(g[1]))].append((int(g[2]), float(g[8]), float(g[9])))
print("%-10s %9s %8s %10s %9s %22s" % ("sizes", "n", "samples", "D", "se", "D/sqrt(n) +- se"))
def key(k):
    return (len(k[0].split(',')), k[0], k[1])
for (sz, n) in sorted(agg, key=key):
    rows = agg[(sz, n)]; S = sum(r[0] for r in rows)
    D = sum(r[0] * r[1] for r in rows) / S
    se = math.sqrt(sum((r[0] * r[2]) ** 2 for r in rows)) / S
    print("%-10s %9d %8d %10.4f %9.4f %12.5f +- %.5f" % (sz, n, S, D, se, D / math.sqrt(n), se / math.sqrt(n)))
cross = defaultdict(list)
cp = re.compile(r'n=(\d+) S=(\d+) seed=\d+ L21_mismatch\(w40 vs w90\)=(\d+) LIS_mismatch\(py vs C\)=(\d+) .*D=E\[2floor\(LIS/2\)-2L21\]=(-?[\d.]+) \+- ([\d.]+)')
for f in sorted(glob.glob('out/cross_*.txt')):
    for line in open(f):
        m = cp.match(line)
        if m:
            g = m.groups(); cross[int(g[0])].append((int(g[1]), int(g[2]), int(g[3]), float(g[4]), float(g[5])))
if cross: print("\nindependent cross-check (numpy PCG64, W40 pruned.c, Python LIS):")
for n in sorted(cross):
    rows = cross[n]; S = sum(r[0] for r in rows)
    D = sum(r[0] * r[3] for r in rows) / S; se = math.sqrt(sum((r[0] * r[4]) ** 2 for r in rows)) / S
    print("  n=%d samples=%d L21 mismatches=%d LIS mismatches=%d  D=%.4f +- %.4f  D/sqrt(n)=%.5f +- %.5f" % (n, S, sum(r[1] for r in rows), sum(r[2] for r in rows), D, se, D / math.sqrt(n), se / math.sqrt(n)))
