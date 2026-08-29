import numpy as np, math
from scipy import integrate, optimize
# 1. exact identity: geometric gaps P(a)=(1-x)x^{a-1}; E min(1, k/(a+a'-1)) = 1 - x^k
for x,k in [(0.9,20),(0.99,300),(0.995,1000)]:
    s = 0.0
    for t in range(2, 20000):
        p = (t-1)*(1-x)**2*x**(t-2)
        s += p*min(1.0, k/(t-1))
    print(f"x={x} k={k}: sum={s:.12f}  1-x^k={1-x**k:.12f}")
# 2. finite-k explicit bound B(x)=x^{-(n+1)}(x/(1-x))^{k+1}(1-x^k)^{(k-1)/2} vs k!, n=floor(lam k^2/e^2)
def logB(x, n, k): return -(n+1)*math.log(x)+(k+1)*math.log(x/(1-x))+((k-1)/2)*math.log(1-x**k)
for k in [101, 1001, 10001, 100001]:
    for lam in [1.0002, 1.00031, 1.00032]:
        n = int(lam*k*k/math.e**2)
        r = optimize.minimize_scalar(lambda th: logB(math.exp(-th/k), n, k), bounds=(5,10), method='bounded')
        print(f"k={k} lam={lam}: min_x log(B/k!) /k = {(r.fun-math.lgamma(k+1))/k:+.3e}  theta*={r.x:.4f}")
# 3. Track B single-index Jensen gain: E_T[N/(b-1)] <= 1 - E[exp(-e^2/(lam G))] + o(1), G~Gamma(2)
lam=1.0
val = integrate.quad(lambda g: np.exp(-math.e**2/(lam*g))*g*np.exp(-g), 0, np.inf)[0]
print("Track B: E[e^{-e^2/G}] =", val, " -> single-index factor <=", 1-val)
g = integrate.quad(lambda g: -np.log(1-np.exp(-math.e**2/g))*g*np.exp(-g), 0, np.inf)[0]
print("per-index log-gain E[-log(1-e^{-e^2/G})] =", g, " heuristic multi-index rate ~ g^2/(4*1.85) =", g*g/(4*1.85))
