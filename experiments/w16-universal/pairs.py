# Second level of the lex-min hierarchy (two-point moves), scaled units N = 1, cells: column c = (x_{c-1},x_c),
# band b = (y_(b-1), y_(b)) of height h_{b-1}.  Strips (level 1) = cells (c,c),(c,c+1) empty, factor e^{-g_c(h_{c-1}+h_c)}
# after the Prop-3 relabelling g'_m = g_{pi^{-1}(m)}.
#
# IDENTITY: level 2 = cell (r, r+2) contains no increasing pair, factor F(mu) = e^{-mu} I0(2 sqrt mu), mu = g_r h_{r+1}.
#   Integrating g_r against e^{-s g} gives Phi(u,v,w) = e^{w/(s+u+v+w)}/(s+u+v+w)   (u,v,w = h_{r-1},h_r,h_{r+1}),
#   transfer on pairs (u,v)->(v,w): K = e^{-t w} Phi(u,v,w).      [level 1 only: 1/(s+u+v), W12]
# DECREASING (pi(r) = k+1-r): level 2 for ranks (m,m+1): no q' in cell (pi^{-1}(m+1), m), q in cell (pi^{-1}(m-1), m)
#   with y_q < y_q'.  Factor G(mu,mu') = e^{-mu-mu'} (mu e^mu - mu' e^mu')/(mu - mu'), mu = g'_{m+1} h_{m-1}, mu' = g'_{m-1} h_{m-1}.
#   Integrating h_{m-1} against e^{-t h - (g'_{m-1}+g'_m) h} gives a transfer on pairs (g'_{m-1},g'_m) -> (g'_m,g'_{m+1}).
import numpy as np, math, sys


def grid(M, n):
    x = np.concatenate([np.linspace(0, 3, 2*n//3, endpoint=False), np.linspace(3, M, n - 2*n//3)])
    w = np.empty_like(x); w[1:-1] = (x[2:] - x[:-2]) / 2; w[0] = (x[1] - x[0]) / 2; w[-1] = (x[-1] - x[-2]) / 2
    return x, w

def rho_pairs(kernel3, s, t, M=14.0, n=60, iters=3000):
    # kernel3(u,v,w) -> value of the transition (u,v)->(v,w) (arrays broadcast), includes the Chernoff weight of w
    x, w = grid(M, n)
    U = x[:, None, None]; V = x[None, :, None]; W = x[None, None, :]
    K = kernel3(U, V, W) * w[None, None, :]        # K[i,j,l]: (x_i,x_j) -> (x_j,x_l)
    f = np.ones((n, n)); lam = 0.0
    for it in range(iters):
        f2 = np.einsum('ijl,jl->ij', K, f); l2 = f2.max(); f = f2 / l2
        if abs(l2 - lam) < 1e-12: break
        lam = l2
    return l2

def ident_level1(s, t):
    return lambda u, v, w: np.exp(-t * w) / (s + u + v) * np.ones_like(w)
def ident_level2(s, t):
    return lambda u, v, w: np.exp(-t * w) * np.exp(w / (s + u + v + w)) / (s + u + v + w)

def Gfac(mu, mup):
    # e^{-mu-mu'} (mu e^mu - mu' e^mu')/(mu-mu'), stable
    d = mu - mup
    out = np.where(np.abs(d) > 1e-9, (mu * np.exp(-mup) - mup * np.exp(-mu)) / np.where(np.abs(d) > 1e-9, d, 1.0), (1 + mu) * np.exp(-mu))
    return out
def dec_level2_kernel(s, t, M=14.0, n=60, nh=400):
    # transfer on (a,b)=(g'_{m-1},g'_m) -> (b,c)=(g'_m,g'_{m+1}):  e^{-s c} * int_0^inf dh e^{-t h - (a+b) h} G(c h, a h)
    x, w = grid(M, n)
    hx, hw = grid(40.0, nh)
    A = x[:, None, None, None]; B = x[None, :, None, None]; C = x[None, None, :, None]; H = hx[None, None, None, :]
    integrand = np.exp(-(t + A + B) * H) * Gfac(C * H, A * H) * hw
    K = integrand.sum(axis=3) * np.exp(-s * x)[None, None, :] * w[None, None, :]
    return K
def rho_from_K(K, iters=3000):
    n = K.shape[0]; f = np.ones((n, n)); lam = 0
    for it in range(iters):
        f2 = np.einsum('ijl,jl->ij', K, f); l2 = f2.max(); f = f2 / l2
        if abs(l2 - lam) < 1e-12: break
        lam = l2
    return l2

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    print("identity, level 1 (check vs W12 0.268059 at s=t=1.5):")
    for s in [1.5]:
        r = rho_pairs(ident_level1(s, s), s, s, n=n); print("  s=%.2f rho=%.6f kappa=%.5f" % (s, r, 2 * s / -math.log(r)))
    print("identity, level 2 (strips + no increasing pair in cells (r,r+2)):")
    best = (9, 0)
    for s in np.arange(1.2, 2.61, 0.1):
        for t in [s - 0.2, s - 0.1, s, s + 0.1, s + 0.2]:
            r = rho_pairs(ident_level2(s, t), s, t, n=n); kap = (s + t) / -math.log(r)
            if kap < best[0]: best = (kap, (s, t, r))
        print("  s=%.2f best over t so far: kappa=%.5f (s=%.2f,t=%.2f,rho=%.6f)" % (s, best[0], *best[1])); sys.stdout.flush()
    print("BEST identity level 2:", best)
    print("decreasing, level 2 (n=%d):" % (n // 2))
    best = (9, 0)
    for s in np.arange(1.3, 2.21, 0.1):
        for t in [s - 0.1, s, s + 0.1]:
            K = dec_level2_kernel(s, t, n=n // 2); r = rho_from_K(K); kap = (s + t) / -math.log(r)
            if kap < best[0]: best = (kap, (s, t, r))
        print("  s=%.2f best so far: kappa=%.5f (s=%.2f,t=%.2f,rho=%.6f)" % (s, best[0], *best[1])); sys.stdout.flush()
    print("BEST decreasing level 2:", best)
