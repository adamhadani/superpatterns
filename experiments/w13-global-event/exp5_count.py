"""Exp 5 (W13): sanity check of Lemma S1's encoding: #{sigma in S_j : LDS(sigma) <= rho} <= rho^{2j}."""
import sys, itertools
sys.path.insert(0, '../w9-alon-threads')
from threads import lis_length
for j in range(1, 9):
    cnt = {}
    for s in itertools.permutations(range(j)):
        d = lis_length([-v for v in s])
        cnt[d] = cnt.get(d, 0) + 1
    out = []
    for rho in [1, 2, 3]:
        c = sum(v for d, v in cnt.items() if d <= rho)
        out.append(f"rho={rho}: {c} <= {rho**(2*j)}  {'OK' if c <= rho**(2*j) else 'FAIL'}")
    print(f"j={j}: " + " | ".join(out))
