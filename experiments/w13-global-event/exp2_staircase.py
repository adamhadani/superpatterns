"""Exp 2 (W13): check Lemma S numerically.  For pi in L_k^{(r)} and two H-threads t, t+D:
the leader's elements A whose intervals contain shared cells form a D-shift chain (W9 Lemma 3);
claim: the start cells X_a (a in A), listed in leader order, have strictly increasing columns and
their row sequence has LDS <= r (in fact rows increase within each run), i.e. {X_a} is a union
of <= r monotone (row & column increasing) chains.  Also report LDS of the full row sequence of
the chain and the sum of zero-runs along the chain vs shared cells."""
import sys, numpy as np
sys.path.insert(0, '../w9-alon-threads')
from threads import runs_pattern, periodic_word, run_thread, lis_length

rng = np.random.default_rng(11)
viol = 0; tests = 0
rows = []
for k in [40, 80, 160]:
    for r in [2, 4, 8, 16]:
        for wtype in ['rand', 'per']:
            word = periodic_word(k, r) if wtype == 'per' else None
            pi, w = runs_pattern(k, r, rng, word=word)
            for rep in range(15):
                m = int(k * rng.uniform(1.5, 6)); q = 2 * k
                M = rng.integers(0, 2, size=(q, m))
                D = int(rng.integers(1, k // 2 + 1)); t = int(rng.integers(0, k - D))
                T1 = run_thread(M, pi, 'H', t); T2 = run_thread(M, pi, 'H', t + D)
                S2 = set(T2['cells'])
                # leader's elements whose intervals contain a shared cell
                A = sorted({e for c, e in zip(T1['cells'], T1['elems']) if c in S2})
                if not A: continue
                tests += 1
                first = {}
                for c, e in zip(T1['cells'], T1['elems']):
                    first.setdefault(e, c)
                X = [first[a] for a in A]
                cols = [c[1] for c in X]; rws = [c[0] for c in X]
                # LDS of row sequence = min number of increasing chains
                lds = lis_length([-y for y in rws])
                incr_cols = all(cols[i] < cols[i+1] for i in range(len(cols)-1))
                # within each run rows must increase
                ok_runs = True
                for j in range(r):
                    rr = [pi[a] + t for a in A if w[a] == j]
                    ok_runs &= all(rr[i] < rr[i+1] for i in range(len(rr)-1))
                if not (incr_cols and ok_runs and lds <= r):
                    viol += 1
                # sum of zero-runs along the chain (leader's z_a) vs shared
                z = {}
                for c, v, e in zip(T1['cells'], T1['vals'], T1['elems']):
                    z[e] = z.get(e, 0) + (1 - v)
                W = sum(z[a] + 1 for a in A)
                shared = sum(1 for c in T1['cells'] if c in S2)
                rows.append((k, r, wtype, len(A), lds, W, shared))
print(f"tests={tests} violations={viol}")
import collections
agg = collections.defaultdict(list)
for k, r, wt, la, lds, W, sh in rows:
    agg[(r, wt)].append((la, lds, W, sh))
print("r  w     mean|A|  max|A|  meanLDS maxLDS  meanW  meanShared")
for key in sorted(agg):
    a = np.array(agg[key])
    print(f"{key[0]:<2} {key[1]:<5} {a[:,0].mean():7.1f} {a[:,0].max():6.0f} {a[:,1].mean():7.2f} {a[:,1].max():6.0f} {a[:,2].mean():7.1f} {a[:,3].mean():8.1f}")
