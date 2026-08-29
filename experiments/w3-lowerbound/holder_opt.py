# Rigorous both-parity bound via Hölder: E[We*Wo] <= E[We^p]^{1/p} E[Wo^q]^{1/q}, 1/p+1/q=1.
# Wo = prod over odd i of f_o, 2-dependent; split i=1 mod 4 / 3 mod 4 (each iid): E[Wo^q] <= E[f_o^{2q}]^{k/4}
# -> per-k rate:  (1/(2p)) log E f^p + (1/(4q)) log E f_o^{2q}.
import numpy as np
from scipy import integrate, optimize
from trackA import Phi, e2, _odd_deficit
def Efp(th, p):  # E min(1, theta/B)^p
    return 1 - np.exp(-th)*(1+th) + th**p*integrate.quad(lambda b: b**(1-p)*np.exp(-b), th, np.inf)[0]
def Rh(th, p):
    q = p/(p-1)
    return np.log(Efp(th, p))/(2*p) + np.log(1-_odd_deficit(th, 2*q))/(4*q)
best = None
for p in [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 2.0, 2.2, 2.5]:
    Rf = lambda th, p=p: Rh(th, p)
    def minPhi(lam):
        r = optimize.minimize_scalar(lambda t: Phi(t, lam, Rf), bounds=(0.95, 1.05), method='bounded', options={'xatol':1e-12}); return r.fun
    lam = optimize.brentq(minPhi, 1.00001, 1.01, xtol=1e-13)
    print(f"p={p:.2f} q={p/(p-1):.3f}  lambda*={lam:.9f}  log={np.log(lam):.4e}")
    if best is None or lam > best[1]: best = (p, lam)
print("best", best)
