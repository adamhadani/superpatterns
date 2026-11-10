#!/usr/bin/env python3
# review-2: aggregate out/est_T*_s*.txt ("raw T S sumL sumL2 sumLIS sumLIS2 sumD sumD2") into tables.
import glob, math, collections
acc = collections.defaultdict(lambda: [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
for f in glob.glob('out/est_T*_s*.txt'):
    for line in open(f):
        if line.startswith('raw'):
            p = line.split(); T = float(p[1]); a = acc[T]; a[0] += int(p[2])
            for i in range(6): a[i+1] += float(p[3+i])
def ms(s, s2, n):
    m = s/n; return m, math.sqrt(max(s2/n - m*m, 0)/(n-1))
res = {}
print("| T | samples | l(T)=E L21 | s.e. | l(T)/T | E LIS | s.e. | E LIS/T | E LIS - 2 E L21 (paired) | s.e. |")
print("|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
for T in sorted(acc):
    n, sa, sa2, sb, sb2, sd, sd2 = acc[T]
    l, le = ms(sa, sa2, n); L, Le = ms(sb, sb2, n); d, de = ms(sd, sd2, n); res[T] = (l, le, L, Le, d, de, n)
    print(f"| {T:g} | {n} | {l:.4f} | {le:.4f} | {l/T:.5f} | {L:.4f} | {Le:.4f} | {L/T:.5f} | {d:.4f} | {de:.4f} |")
print()
print("| T | l(2T) - 2 l(T) | s.e. | sqrt(T ln T) | 45 sqrt(T ln T) (Lemma R) | ratio to T^(1/3) | E LIS(2T) - 2 E LIS(T) | s.e. |")
print("|--:|--:|--:|--:|--:|--:|--:|--:|")
for T in sorted(res):
    if 2*T in res:
        l, le, L, Le = res[T][:4]; l2, le2, L2, Le2 = res[2*T][:4]
        d = l2 - 2*l; de = math.sqrt(le2**2 + 4*le**2); r = math.sqrt(T*math.log(T))
        print(f"| {T:g} | {d:.4f} | {de:.4f} | {r:.2f} | {45*r:.1f} | {d/T**(1/3):.4f} | {L2-2*L:.4f} | {math.sqrt(Le2**2+4*Le**2):.4f} |")
