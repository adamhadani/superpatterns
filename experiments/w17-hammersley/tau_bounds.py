# Rigorous lower bounds c_tau >= 2/E[cost] for the square-sweep and strip first-copy rules, |tau| <= 4.
# Input: enum_<tau>.out (m, cnt_m, sumTop_m for m <= M=11), exact by enumeration (enum3.c).
#   cnt_m = #{(sigma in Av_{m-1}(tau), y-rank r)} such that inserting the new rightmost point creates a copy
#         = m*Av_{m-1} - Av_m ;   P(N = m-1) = cnt_m/m! = a_{m-1} - a_m,  a_m := Av_m/m!.
#   sumTop_m = sum over those of min_{copies} (max y-rank of copy).
# Square rule:  E cost = sum_m G(m) [ (cnt_m(t)+cnt_m(t^-1))/(2 m!) + (sumTop_m(t)+sumTop_m(t^-1))/(2 (m+1) m!) ],
#   G(m) = Gamma(m+1/2)/Gamma(m) = E[r_m] for r_m^2 ~ Gamma(m,1).
#   Tail m > M:  term <= 2 G(m) (a_{m-1}-a_m)   (since minTop <= m).
# Strip rule:   E n = sum_{m>=0} a_m,  E top = sum_m sumTop_m/((m+1) m!) <= (exact part) + a_M;  cost = 2 sqrt(E n E top).
from mpmath import mp, mpf, gamma, factorial, binomial, sqrt
from math import comb
mp.dps = 30
M = 11
def read(t):
    d = {}
    for line in open(f"enum_{t}.out"):
        p = line.split(); d[int(p[1])] = (int(p[3]), int(p[5]))
    return d
def av_counts(t, d):
    j = len(t); av = {j-1: comb(j-1, 0) and __import__('math').factorial(j-1)}
    for m in range(j, M+1): av[m] = m*av[m-1] - d[m][0]
    return av
def gessel(n):  # Av_n(1234)
    return sum(comb(2*k,k)*comb(n+1,k+1)*comb(n+2,k+1) for k in range(n+1)) // ((n+1)**2*(n+2))
def bona(n):    # Av_n(1342)
    from fractions import Fraction
    s = Fraction((-1)**(n-1)*(7*n*n-3*n-2), 2)
    for i in range(2, n+1):
        s += 3*Fraction((-1)**(n-i)*2**(i+1)*__import__('math').factorial(2*i-4), __import__('math').factorial(i)*__import__('math').factorial(i-2))*comb(n-i+2, 2)
    assert s.denominator == 1; return int(s)
def catalan(n): return comb(2*n, n)//(n+1)
def inv(t):
    q=[0]*len(t)
    for i,v in enumerate(t): q[int(v)-1]=str(i+1)
    return ''.join(q)
G = lambda m: gamma(m+mpf(1)/2)/gamma(m)
def a_seq(t, av, formula):
    """a_m for m up to 400: exact where a verified formula exists, else block bound a_m <= a_M a_M^{floor((m-M)/M)}"""
    j=len(t); a={}
    for m in range(0, M+1): a[m] = mpf(1) if m < j else mpf(av[m])/factorial(m)
    for m in range(M+1, 401):
        if formula: a[m] = mpf(formula(m))/factorial(m)
        else: a[m] = a[M]*a[M]**((m-M)//M)
    return a
rows=[]
for line in open("classes.txt"):
    t = line.split()[0]; ti = inv(t); j=len(t)
    d, di = read(t), read(ti)
    av = av_counts(t, d); avi = av_counts(ti, di); assert av == avi
    formula=None
    if j==3: formula=catalan
    elif j==4:
        if all(av[m]==gessel(m) for m in av): formula=gessel
        elif all(av[m]==bona(m) for m in av): formula=bona
    if formula: assert all(av[m]==formula(m) for m in av)
    a = a_seq(t, av, formula)
    # square rule
    exact = sum(G(m)*((mpf(d[m][0])+di[m][0])/(2*factorial(m)) + (mpf(d[m][1])+di[m][1])/(2*(m+1)*factorial(m))) for m in range(j, M+1))
    tail = sum(2*G(m)*(a[m-1]-a[m]) for m in range(M+1, 401))
    csq = exact+tail
    # strip rule (tau and tau^-1; take better)
    best=None
    for (tt,dd) in ((t,d),(ti,di)):
        En = sum(a[m] for m in range(0, 401))
        Etop = sum(mpf(dd[m][1])/((m+1)*factorial(m)) for m in range(j, M+1)) + a[M]
        cst = 2*sqrt(En*Etop)
        if best is None or cst < best[0]: best=(cst,En,Etop,tt)
    rows.append((t, ti, 'formula' if formula else 'block', float(exact), float(tail), float(csq), float(2/csq), float(best[0]), float(2/best[0]), float(best[1]), float(best[2]), float(a[M])))
print("tau   inv   tail-type  square:exact  tail   Ecost   c>=   | strip: Ecost  c>=  (E n, E top)   a_11")
for r in rows: print("%-5s %-5s %-8s %8.4f %8.4f %8.4f  %.4f | %8.4f %.4f  (%.4f, %.4f)  %.4g"%r)
