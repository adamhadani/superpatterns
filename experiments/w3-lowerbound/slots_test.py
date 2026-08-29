# For a given sigma and k: over all k-subsets T and each middle index i, compute
#   N = #distinct value-slots (w.r.t. the other k-1 values) hit by sigma(J), J=(t_{i-1},t_{i+1});
#   compare mean N/(b-1) with min(k,b-1)/(b-1) [CKS-type] and with Jensen bound 1+(b-2)(1-exp(-k/(b-2))).
import itertools, math, sys, random
def stats(sig, k):
    n = len(sig); pos = {v:p for p,v in enumerate(sig)}
    tot = cnt = totCKS = totJ = 0.0
    for T in itertools.combinations(range(n), k):
        for i in range(1, k-1):
            lo, hi = T[i-1], T[i+1]; b = hi - lo
            others = sorted(sig[t] for j,t in enumerate(T) if j != i)
            import bisect
            slots = {bisect.bisect(others, sig[p]) for p in range(lo+1, hi)}
            N = len(slots)
            tot += N/(b-1); cnt += 1
            totCKS += min(k, b-1)/(b-1)
            totJ += min(1.0, (1 + (b-2)*(1-math.exp(-(k-1)/max(b-2,1e-9))))/(b-1)) if b>2 else 1.0
    return tot/cnt, totCKS/cnt, totJ/cnt
sp6 = [6,14,10,2,13,17,5,8,3,12,9,16,1,7,11,4,15]
sp4 = [5,1,9,4,7,2,6,8,3]
sp5_zig = None
tests = [("sp(6)=17 Arnarson", sp6, 6), ("sp(6) sigma, k=5", sp6, 5), ("sp(4)=9 Smith", sp4, 4),
         ("identity17,k=6", list(range(1,18)), 6)]
random.seed(3)
r17 = list(range(1,18)); random.shuffle(r17); tests.append(("random17,k=6", r17, 6))
# Miller zigzag-like Engen-Vatter for k=7? use a simple grid perm n=16,k=4
grid = [ (r)*4 + c + 1 for c in range(4) for r in range(4)]
tests.append(("grid16,k=4", grid, 4))
for name, sig, k in tests:
    a, b, c = stats(sig, k)
    print(f"{name:22s} k={k} n={len(sig)}  mean N/(b-1)={a:.4f}   CKS min(k,b-1)/(b-1)={b:.4f}   Jensen-bound={c:.4f}", flush=True)
