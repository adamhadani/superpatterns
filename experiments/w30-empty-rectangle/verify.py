"""Brute-force cross-check of erect.c: recompute M, the largest maximal empty rectangles, Kc (centre phantom) and
Kany (phantom anywhere in Q1) from scratch with itertools, for the lines produced by ./erect."""
import sys, itertools, subprocess
sys.path.insert(0, '../w24-union-slack'); from patlib import standardise, encode
def missing(seq, k):
    kf = 1
    for i in range(2, k+1): kf *= i
    seen = set(encode(standardise([seq[i] for i in idx])) for idx in itertools.combinations(range(len(seq)), k))
    return set(range(kf)) - seen
def rects(sig):
    n = len(sig); pos = {v: i for i, v in enumerate(sig)}; out = []
    for a in range(n):
        for b in range(a, n):
            for c in range(n):
                for d in range(c, n):
                    if any(c <= sig[i] <= d for i in range(a, b+1)): continue
                    ok = (c == 0 or a <= pos[c-1] <= b) and (d == n-1 or a <= pos[d+1] <= b) and (a == 0 or c <= sig[a-1] <= d) and (b == n-1 or c <= sig[b+1] <= d)
                    if ok: out.append((a, b, c, d, (b-a+1)*(d-c+1)))
    return sorted(out, key=lambda r: -r[4])
k, n, S, seed, R = map(int, sys.argv[1:6])
lines = subprocess.run(['./erect', str(k), str(n), str(S), str(seed), str(R)], capture_output=True, text=True).stdout.splitlines()
bad = 0
for ln in lines:
    p = ln.split('|'); Mc = int(p[0]); sig = [int(x)-1 for x in p[1].split()]; rr = list(map(int, p[2].split())); kk = list(map(int, p[3].split()))
    miss = missing(sig, k); assert len(miss) == Mc, (len(miss), Mc)
    rs = rects(sig)
    top = [tuple(rr[6*i:6*i+5]) for i in range(len(rr)//6)]
    assert sorted(r[4] for r in top) == sorted(r[4] for r in rs[:len(top)]), (top, rs[:len(top)])
    if Mc == 0: continue
    union = set()
    for i, (a, b, c, d, ar) in enumerate(top):
        s = (a+b+2)//2; t = (c+d+2)//2
        sp = sig[:s] + [t-0.5] + sig[s:]
        kc = miss - missing(sp, k); union |= kc
        assert len(kc) == rr[6*i+5], (i, len(kc), rr[6*i+5])
    assert len(union) == kk[1], (len(union), kk[1])
    a, b, c, d, ar = top[0]; anyk = set()
    for s in range(a, b+2):
        for t in range(c, d+2):
            sp = sig[:s] + [t-0.5] + sig[s:]; anyk |= (miss - missing(sp, k))
    assert len(anyk) == kk[0], (len(anyk), kk[0])
print("verify OK:", len(lines), "samples k=%d n=%d" % (k, n))
