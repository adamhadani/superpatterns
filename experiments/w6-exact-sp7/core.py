#!/usr/bin/env python3
"""UNSAT-core hunting: all k-patterns with selector literals; iteratively shrink the core."""
import sys, itertools, time
sys.argv, argv = sys.argv[:1], sys.argv
from spsat import Enc
k, n = int(argv[1]), int(argv[2])
E = Enc(n, k)
E.S.add_clause([E.less(0, n-1)])
sel = {}
for pi in itertools.permutations(range(1, k+1)):
    s = E.new(); sel[pi] = s
    # add pattern clauses guarded by selector: temporarily wrap add_clause
    orig = E.S.add_clause
    E.S.add_clause = lambda c, orig=orig, s=s: orig(c + [-s])
    E.add_pattern(pi)
    E.S.add_clause = orig
core = list(sel)
t0 = time.time()
assert not E.S.solve(assumptions=[sel[p] for p in core])
core = [p for p in core if sel[p] in set(E.S.get_core())]
print(f"first core {len(core)} in {time.time()-t0:.1f}s", flush=True)
# deletion-based minimisation
i = 0
while i < len(core):
    trial = core[:i] + core[i+1:]
    if not E.S.solve(assumptions=[sel[p] for p in trial]):
        core = [p for p in trial if sel[p] in set(E.S.get_core())]
    else:
        i += 1
    print(f"core size {len(core)} t={time.time()-t0:.0f}s", flush=True)
print("MINIMAL CORE (no %d-superpattern of length %d with sigma(1)<sigma(n) contains all of these):" % (k, n))
for p in core: print(" ", "".join(map(str, p)))
