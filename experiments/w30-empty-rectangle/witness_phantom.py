"""Deterministic test of Prop. 4 (proof.md): take a minimal (k-1)-superpattern sigma (sp(6)=17 witness for k=7),
add ONE point x at every slot, and count K_x = #{pi in S_k : pi ⊂ sigma+x, pi ⊄ sigma}.  Compares with the bound
K_x >= N_{k-1}(sigma)/k - N_k(sigma)  (N_j = number of j-patterns contained)."""
import itertools, sys, math
sys.path.insert(0, '../w24-union-slack'); from patlib import standardise, encode
sig = [6,14,10,2,13,17,5,8,3,12,9,16,1,7,11,4,15]; k = 7; n = len(sig)
def contained(seq, k, through=None):
    s = set()
    idx = range(len(seq))
    if through is None:
        for c in itertools.combinations(idx, k): s.add(encode(standardise([seq[i] for i in c])))
    else:
        others = [i for i in idx if i != through]
        for c in itertools.combinations(others, k-1):
            cc = sorted(c + (through,)); s.add(encode(standardise([seq[i] for i in cc])))
    return s
Nk = contained(sig, k); Nk1 = contained(sig, k-1)
print('sigma = sp(6)=17 witness, k=%d: N_6=%d (of 720), N_7=%d (of 5040), bound N_6/k - N_7 = %.1f' % (k, len(Nk1), len(Nk), len(Nk1)/k - len(Nk)))
best = (0, None); tot = 0; cnt = 0; vals = []
for s in range(n+1):
    for t in range(n+1):
        sp = sig[:s] + [t+0.5] + sig[s:]
        K = len(contained(sp, k, through=s) - Nk); vals.append(K); tot += K; cnt += 1
        if K > best[0]: best = (K, (s, t))
vals.sort()
print('K_x over all %d slots: mean %.1f, median %d, min %d, max %d at slot %s; quantiles 10/90: %d %d' % (cnt, tot/cnt, vals[cnt//2], vals[0], best[0], best[1], vals[cnt//10], vals[9*cnt//10]))
print('K_max/(k-1)! = %.3f, ln K_max / k = %.2f, ln K_max / (k ln k) = %.2f' % (best[0]/720, math.log(best[0])/k, math.log(best[0])/(k*math.log(k))))
