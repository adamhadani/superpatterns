"""W34: block rule constants.  K_b = min over x_1<...<x_b (x_s in strip s, strips iid Poisson(1) on [0,X]x[0,Y])
of x_b + sum y_s.  Blocks are iid, so gamma_b := E K_b / b and C*_b := (E K_b/(2b))^2.
Also returns the mean x-part and y-part of the optimal path (should be equal by the envelope argument)."""
import numpy as np, sys, time
from fpp import run

def main(b, M, seed0, X=None, Y=8.0):
    if X is None: X = 2.0 * b + 12
    K = []; U = []; V = []
    for i in range(M):
        G, us, vs = run(b, X, Y, seed0 + i)
        K.append(G); U.append(us.sum()); V.append(vs.sum())
    K = np.array(K); U = np.array(U); V = np.array(V)
    m = K.mean(); se = K.std(ddof=1) / np.sqrt(M)
    print(f"b={b:4d} M={M:6d}  E K_b={m:.5f} ± {se:.5f}   E K_b/b={m/b:.5f}   E u/b={U.mean()/b:.4f}  E v/b={V.mean()/b:.4f}"
          f"   C*_b=(E K_b/2b)^2={(m/(2*b))**2:.5f}  [+2se: {((m+2*se)/(2*b))**2:.5f}]", flush=True)

if __name__ == '__main__':
    b = int(sys.argv[1]); M = int(sys.argv[2]); seed0 = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
    main(b, M, seed0)
