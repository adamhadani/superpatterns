"""W36 numerical certification of the Burke/stationarity argument for the first-passage functional
   K_n = min { x_n + sum_s y_s : p_s in Psi_s, x_1 < ... < x_n },  Psi_s i.i.d. Poisson(1) on (0,inf)^2.

Checks (all independent of W34's code; own suffix-minimum DP):
  A. law of D = G'(0) - G(0) when G is compound Poisson (rate rho, Exp(1/rho) jumps): Exp(1/rho), mean rho.
  B. Burke: jumps of G' form Poisson(rho) x Exp(1/rho): count mean/variance, size mean/second moment,
     lag-1 correlation of sizes and of gaps.
  C. iterated: E G^rho_1(0) = n*rho with stationary boundary; and n - sqrt(2n) <= E K_n <= n + sqrt(2n) + 1/2
     with the true boundary G_{n+1}(x) = x.
  D. general rho: E Z with Z = sup_x (x - G(x)) has mean 1/kappa, kappa = rho - 1/rho (rho>1).
Usage: python verify.py [seed]
"""
import numpy as np, sys

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 1)

def step(bx, bv, X, Y):
    """One strip of the backward recursion.  Boundary G given as a step function:
    G(x) = bv[i] for bx[i] <= x < bx[i+1]  (bx sorted, bx[0] = -inf convention handled by caller).
    Returns the new step function G'(a) = min_{x_p>a}[y_p + G(x_p)] on the points of a fresh Poisson(1)
    process on [0,X]x[0,Y]; represented on the grid of the strip's own x-coordinates: G'(a) for a in
    [x_(i-1), x_(i)) equals suffmin_i."""
    m = rng.poisson(X * Y)
    x = np.sort(rng.uniform(0, X, m)); y = rng.uniform(0, Y, m)
    idx = np.searchsorted(bx, x, side='right') - 1          # G(x_p) = bv[idx]
    w = y + bv[idx]
    suff = np.minimum.accumulate(w[::-1])[::-1]
    # G'(a) for a < x[0] is suff[0]; for x[i-1] <= a < x[i] is suff[i]; for a >= x[-1] is +inf
    nbx = np.concatenate(([-np.inf], x))
    nbv = np.concatenate((suff, [np.inf]))
    return nbx, nbv, x, suff

def comp_poisson(rho, X):
    """two-sided not needed: G on [0,X] with G(0)=0, jumps Exp(1/rho) at rate rho.  Step function repr."""
    m = rng.poisson(rho * X)
    t = np.sort(rng.uniform(0, X, m)); J = rng.exponential(rho, m)
    bx = np.concatenate(([-np.inf], t)); bv = np.concatenate(([0.0], np.cumsum(J)))
    return bx, bv

def testA_B(rho, X=4000.0, Y=None, reps=60):
    theta = 1.0 / rho
    Y = Y or 12 * rho
    Ds = []; cnt = []; sizes = []; gaps = []; c1 = []; g1 = []; sg = []
    for _ in range(reps):
        bx, bv = comp_poisson(rho, X)
        nbx, nbv, x, suff = step(bx, bv, X, Y)
        # D(0) = G'(0) - G(0) = suff[0] - 0
        Ds.append(suff[0])
        # jumps of G' in the bulk window [X/4, 3X/4]: where suff changes
        up = suff[1:] > suff[:-1]                 # G' jumps at x_i from suff[i] to suff[i+1]
        jump_pos = x[:-1][up]
        jump_sz = (suff[1:] - suff[:-1])[up]
        sel = (jump_pos > X / 4) & (jump_pos < 3 * X / 4)
        jp, js = jump_pos[sel], jump_sz[sel]
        cnt.append(len(jp)); sizes.append(js); gaps.append(np.diff(jp))
        c1.append(np.corrcoef(js[:-1], js[1:])[0, 1]); g1.append(np.corrcoef(np.diff(jp)[:-1], np.diff(jp)[1:])[0, 1]); sg.append(np.corrcoef(js[:-1], np.diff(jp))[0, 1])
    Ds = np.array(Ds); sizes = np.concatenate(sizes); gaps = np.concatenate(gaps); cnt = np.array(cnt)
    L = X / 2
    print(f"rho={rho}: A: D(0) mean={Ds.mean():.3f} (pred {rho}); "
          f"B: jump count mean/L={cnt.mean()/L:.4f} var/mean={cnt.var()/cnt.mean():.3f} (pred rho={rho}, 1); "
          f"size mean={sizes.mean():.4f} E[s^2]/2mean^2={sizes.mean()**2*2/np.mean(sizes**2):.3f} (pred {rho}, 1); "
          f"gap mean={gaps.mean():.4f} E[g^2]/2mean^2={gaps.mean()**2*2/np.mean(gaps**2):.3f} (pred {1/rho:.4f},1); "
          f"lag1 corr sizes={np.mean(c1):+.4f} gaps={np.mean(g1):+.4f}; corr(size,next gap)={np.mean(sg):+.4f}")
    # finer test of the size law: KS-like max deviation of empirical tail from exp(-theta z)
    z = np.sort(sizes); emp = 1 - np.arange(1, len(z) + 1) / len(z)
    print(f"        max|F_emp - Exp({theta:.3f})| over sizes = {np.max(np.abs(emp - np.exp(-theta*z))):.4f} (N={len(z)})")
    z = np.sort(Ds); emp = 1 - np.arange(1, len(z) + 1) / len(z)

def testA_law(rho, X=400.0, reps=4000):
    Y = 12 * rho; theta = 1 / rho
    Ds = []
    for _ in range(reps):
        bx, bv = comp_poisson(rho, X)
        _, _, _, suff = step(bx, bv, X, Y)
        Ds.append(suff[0])
    z = np.sort(np.array(Ds)); emp = 1 - np.arange(1, len(z) + 1) / len(z)
    print(f"rho={rho}: law of D: mean={z.mean():.4f} (pred {rho}), max|F_emp-Exp(1/rho)|={np.max(np.abs(emp-np.exp(-theta*z))):.4f} "
          f"(KS 95% ~ {1.36/np.sqrt(reps):.4f})")

def iterate(n, boundary, X, Y):
    bx, bv = boundary
    for s in range(n):
        bx, bv, _, _ = step(bx, bv, X, Y)
    # G_1(0): value for a = 0: index of last breakpoint <= 0
    i = np.searchsorted(bx, 0.0, side='right') - 1
    return bv[i]

def true_boundary(X):
    # G_{n+1}(x) = x as a fine step function (lower staircase -> slight underestimate; use exact via dense grid)
    t = np.linspace(0, X, int(X * 200) + 1)
    return np.concatenate(([-np.inf], t)), np.concatenate(([0.0], t))

def testC_run(n, rho, reps):
    X = 1.6 * n * max(1.0, rho) + 60; Y = 10.0
    stat = np.array([iterate(n, comp_poisson(rho, X), X, Y) for _ in range(reps)])
    true = np.array([iterate(n, true_boundary(X), X, Y) for _ in range(reps)])
    se_s = stat.std() / np.sqrt(reps); se_t = true.std() / np.sqrt(reps)
    extra = (f"E K_n <= n rho + rho/(rho^2-1) = {n*rho + rho/(rho**2-1):.2f}" if rho > 1 else
             f"E K_n >= n rho - rho/(1-rho^2) = {n*rho - rho/(1-rho**2):.2f}" if rho < 1 else "")
    print(f"n={n} rho={rho}: E G^rho_1(0) = {stat.mean():.3f} ± {se_s:.3f} (pred n*rho = {n*rho:.3f});  "
          f"E K_n = {true.mean():.3f} ± {se_t:.3f}  bounds [{n-np.sqrt(2*n):.2f}, {n+np.sqrt(2*n)+0.5:.2f}]  {extra}")

def testD(rho, X=2000.0, reps=2000):
    Z = []
    for _ in range(reps):
        bx, bv = comp_poisson(rho, X)
        # sup_x (x - G(x)): attained just before jumps: x = t_i-, G = bv[i-1]
        t = bx[1:]; g = bv[:-1]
        Z.append(max(0.0, (t - g).max() if len(t) else 0.0, X - bv[-1]))
    Z = np.array(Z); kappa = rho - 1 / rho
    print(f"rho={rho}: E Z = {Z.mean():.4f} ± {Z.std()/np.sqrt(reps):.4f} (pred 1/kappa = {1/kappa:.4f}); "
          f"P(Z>1) = {np.mean(Z>1):.4f} (pred e^-kappa = {np.exp(-kappa):.4f})")

if __name__ == '__main__':
    print("== A/B: single strip, stationary compound-Poisson boundary ==")
    for rho in (0.5, 1.0, 2.0):
        testA_B(rho)
    for rho in (0.5, 1.0, 2.0):
        testA_law(rho)
    print("== D: Lundberg sup ==")
    for rho in (1.5, 2.0):
        testD(rho)
    print("== C: iterated recursion, stationary vs true boundary ==")
    for n, rho, reps in ((10, 1.0, 400), (10, 1.5, 400), (10, 0.7, 400), (50, 1.0, 100), (50, 1.2, 100), (200, 1.0, 20)):
        testC_run(n, rho, reps)
