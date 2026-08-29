# Monte-Carlo check of rate_both(theta) = lim (1/k) log E[W], W = prod_{i in I} min(1, theta/B_i),
# I = stable even/odd rule on iid Exp(1) gaps (continuum, product measure). Compare to first-order formula.
import numpy as np, sys
from trackA import Ef, Efo
rng = np.random.default_rng(1)
theta = np.e**2; k = 4000; reps = 40; batch = 2000
logs = []
for r in range(reps):
    a = rng.exponential(size=(batch, k+1))
    B = a[:, :-1] + a[:, 1:]                       # B[:, i-1] = width of index i, i=1..k
    large = B > theta
    f = np.minimum(1.0, theta / B)
    idx = np.arange(1, k+1)
    even = (idx % 2 == 0); odd = ~even
    Ie = large & even
    # odd i included iff large and neighbours i-1,i+1 not in Ie
    nb = np.zeros_like(Ie); nb[:, 1:] |= Ie[:, :-1]; nb[:, :-1] |= Ie[:, 1:]
    Io = large & odd & ~nb
    I = Ie | Io
    logW = np.where(I, np.log(f), 0.0).sum(axis=1)
    logs.append(logW)
logW = np.concatenate(logs)
m = logW.max(); EW = np.exp(m) * np.exp(logW - m).mean()
se = np.exp(m) * np.exp(logW - m).std() / np.sqrt(len(logW))
rate = np.log(EW) / k
print(f"MC   rate_both = {rate:.4e}  (rel. se of E[W] {se/EW:.3f}, -> abs err ~{se/EW/k:.1e})")
print(f"1st-order      = {(np.log(Ef(theta)) + np.log(Efo(theta)))/2:.4e}")
print(f"mean logW/k    = {logW.mean()/k:.4e}   (Jensen: -E[S]/k)")
print(f"even-only      = {np.log(Ef(theta))/2:.4e}")
