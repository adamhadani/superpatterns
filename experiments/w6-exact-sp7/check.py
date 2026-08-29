#!/usr/bin/env python3
"""Independent brute-force k-superpattern checker: enumerate all k-subsets."""
import sys, itertools
def missing(perm, k):
    seen = set()
    for sub in itertools.combinations(perm, k):
        srt = sorted(sub); seen.add(tuple(srt.index(x) for x in sub))
    return [tuple(x+1 for x in p) for p in itertools.permutations(range(k)) if p not in seen]
if __name__ == "__main__":
    k = int(sys.argv[1]); perm = [int(x) for x in sys.argv[2].split()]
    m = missing(perm, k); print(f"n={len(perm)} k={k} missing={len(m)}"); print(m[:20])
