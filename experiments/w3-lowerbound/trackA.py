"""Track A numerics (float64): refined CKS encoding, exact per-index factors.
Continuum model: gaps=(m/tau)*xi, xi~Exp(1) iid (geometric tilt), m=n/k=lam*k/e^2.
Factor for i in I: f=min(1,k/(b_i-1)) -> min(1,theta/B), B=xi+xi'~Gamma(2), theta=tau*e^2/lam.
Bound: (1/k) log(#pat/k!) <= Phi(tau,lam) = tau-1-log tau + log lam + R(theta).
"""
import numpy as np
from scipy import integrate, optimize, special
e2 = np.e**2

def Ef(th):   return 1 - np.exp(-th)                                   # E min(1,theta/B), closed form
def Ef2(th):  return 1 - np.exp(-th)*(1+th) + th**2*special.exp1(th)
def Ef4(th):  return 1 - np.exp(-th)*(1+th) + th**4*integrate.quad(lambda b: np.exp(-b)/b**3, th, np.inf)[0]
def _odd_deficit(th, pw):
    # odd i: factor min(1,theta/B)^pw applied iff both even neighbours have width <= theta.
    # Given the two gaps (a,a') of b_i, P(b_{i-1}<=theta | a) = 1-exp(-(theta-a)) for a<theta.
    g = lambda ap, a: (1-(th/(a+ap))**pw)*(1-np.exp(-(th-a)))*(1-np.exp(-(th-ap)))*np.exp(-a-ap)
    return integrate.dblquad(g, 0, th, lambda a: th-a, lambda a: th, epsabs=1e-13, epsrel=1e-11)[0]
def Efo(th):  return 1 - _odd_deficit(th, 1)
def Efo4(th): return 1 - _odd_deficit(th, 4)

R = {
 "even-only (rigorous)":                 lambda th: np.log(Ef(th))/2,
 "both, Hölder split (rigorous)":        lambda th: np.log(Ef2(th))/4 + np.log(Efo4(th))/8,
 "both, first-order (2-dep. ignored)":   lambda th: (np.log(Ef(th)) + np.log(Efo(th)))/2,
 "both, iid-approx  log(1-e^-th)":       lambda th: np.log(Ef(th)),
}
def Phi(tau, lam, Rf): return tau-1-np.log(tau)+np.log(lam)+Rf(tau*e2/lam)
def minPhi(lam, Rf):
    r = optimize.minimize_scalar(lambda t: Phi(t, lam, Rf), bounds=(0.9, 1.1), method='bounded', options={'xatol':1e-12})
    return r.fun, r.x
if __name__ == "__main__":
    for name, Rf in R.items():
        lam = optimize.brentq(lambda l: minPhi(l, Rf)[0], 1.00001, 1.01, xtol=1e-13)
        tau = minPhi(lam, Rf)[1]
        print(f"{name:40s} lambda*={lam:.9f}  (log lam={np.log(lam):.3e})  tau*={tau:.6f}  theta*={tau*e2/lam:.5f}")
    th = e2
    print(f"theta=e^2: e^-th={np.exp(-th):.6e}  p=P(B>th)={np.exp(-th)*(1+th):.6e}  even deficit={1-Ef(th):.6e}  odd deficit={1-Efo(th):.6e}")
    print("CKS: c log(d/e^2)/(1-c) =", 0.00075*np.log(8.18/e2)/(1-0.00075))
