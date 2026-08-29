# Track B numerics: P(n,k) = max over sigma in S_n of number of distinct k-patterns (Bona's quantity).
# Exhaustive for n<=8; hill-climb (random restarts + adjacent/random transpositions) for larger n.
import itertools, random, math, sys, time
def npat(sig, k):
    n = len(sig); seen = set()
    for T in itertools.combinations(range(n), k):
        vals = [sig[t] for t in T]
        srt = sorted(vals); rk = {v:i for i,v in enumerate(srt)}
        seen.add(tuple(rk[v] for v in vals))
    return len(seen)
def exhaustive(n, k):
    best = 0; arg = None
    for sig in itertools.permutations(range(n)):
        if sig[0] > sig[-1]: continue   # reverse symmetry
        c = npat(sig, k)
        if c > best: best, arg = c, sig
    return best, arg
def hill(n, k, restarts=6, steps=3000, seed=0):
    rng = random.Random(seed); best = 0; arg = None
    for r in range(restarts):
        sig = list(range(n)); rng.shuffle(sig); cur = npat(sig, k)
        for s in range(steps):
            i, j = rng.sample(range(n), 2); sig[i], sig[j] = sig[j], sig[i]
            c = npat(sig, k)
            if c >= cur: cur = c
            else: sig[i], sig[j] = sig[j], sig[i]
        if cur > best: best, arg = cur, tuple(sig)
    return best, arg
print("n k C(n,k) k! maxpat ratio=maxpat/C(n,k) method sigma", flush=True)
for n in range(4, 9):
    for k in range(3, n):
        if math.comb(n, k) < 3: continue
        b, a = exhaustive(n, k)
        print(n, k, math.comb(n,k), math.factorial(k), b, f"{b/math.comb(n,k):.4f}", "exh", "".join(str(x+1) for x in a), flush=True)
for n, k in [(9,4),(9,5),(10,4),(10,5),(11,5),(12,5),(12,6),(13,6),(14,6),(15,6),(16,6),(17,6),(16,7),(18,7),(20,7)]:
    t=time.time(); b, a = hill(n, k, restarts=4, steps=1500 if n<=13 else 600)
    print(n, k, math.comb(n,k), math.factorial(k), b, f"{b/math.comb(n,k):.4f}", f"hill({time.time()-t:.0f}s)", "".join(chr(ord('a')+x) for x in a), flush=True)
