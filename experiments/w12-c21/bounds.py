# W12: explicit bounds on c_21.
import math
try:
    import mpmath as mp
    E1 = lambda x: float(mp.e1(x)); I0 = lambda x: float(mp.besseli(0,x))
    quad = lambda f,a,b: float(mp.quad(f,[a,b]))
except ImportError:
    raise SystemExit("need mpmath")

# ---------- lower bound: Bernoulli grid + Seppalainen ----------
def p21(lam):           # P(a Poisson(lam) cloud in a square contains a 21) = 1 - e^{-lam} I0(2 sqrt lam)
    return 1.0 - math.exp(-lam)*I0(2*math.sqrt(lam))
def g(p):               # Seppalainen 1997: strict LIS of Bernoulli(p) sites on n x n ~ n * 2 sqrt p/(1+sqrt p)
    return 2*math.sqrt(p)/(1+math.sqrt(p))
best=(0,0)
for i in range(1,400):
    d=i/100; v=g(p21(d*d))/d
    if v>best[0]: best=(v,d)
print("LB 21: max_delta g(p(delta^2))/delta = %.5f at delta=%.2f  (p=%.4f)"%(best[0],best[1],p21(best[1]**2)))
for d in (0.8,1.0,1.1,1.2,1.5,2.0): print("  delta=%.1f p=%.4f g/delta=%.4f"%(d,p21(d*d),g(p21(d*d))/d))

# ---------- upper bounds: sharpened first moment ----------
# (A) corner boxes: count a-chains of length L with all corner boxes nonempty.
#     P(L_21 >= c sqrt N) <= exp(sqrt N [2 s + c log k(s)]) ,  k(s)=1/s^2 - e^{s^2}E1(s^2)
def kA(s): return 1/s**2 - math.exp(s*s)*E1(s*s)
def cA(s): return 2*s/(-math.log(kA(s)))
# (B) canonical chains, decoupled regions:  alpha_i delta_{i-1} + beta_i delta_{i-1} + beta_{i-1} gamma_i
#     w(s) = int int e^{-s(u+v)} /((s+u)(s+u+v)) du dv = e^{s^2} int_s^inf E1(s r)/r dr
def wB(s): return math.exp(s*s)*quad(lambda r: E1(s*r)/r, s, mp.inf)
def cB(s): return 2*s/(-math.log(wB(s)))
# (C) full canonical regions, transfer operator in delta with test function phi==1:
#     rho <= (1/s) * int_0^inf r e^{-s r}/(s+r) dr  (per block, in scaled units), rate 2s + c log rho
def rC(s): return (1/s)*quad(lambda r: r*math.exp(-s*r)/(s+r), 0, mp.inf)
def cC(s): return 2*s/(-math.log(rC(s)))
# sanity: first moment F(u)=u gives k=1/s^2 -> c = s/log s, min = e/2 at s=e
print("first moment check: min s/log s =", min(s/math.log(s) for s in [x/1000 for x in range(1500,5000)]), "e/2=",math.e/2)
for name,f in (("A corner",cA),("B decoupled",cB),("C coupled,phi=1",cC)):
    bs=min(((f(x/100),x/100) for x in range(120,400)))
    print("UB %-18s min_s = %.5f at s=%.2f"%(name,bs[0],bs[1]))
