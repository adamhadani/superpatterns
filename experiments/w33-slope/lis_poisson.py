# W33: Poissonized LIS lower tail via Gessel's determinant  P(L<=l) = e^{-lam} det[I_{i-j}(2 sqrt lam)]_{l x l}
# prints x=l/sqrt(lam), rate=-ln P/lam, slope=-d ln P/d lam (per point), and candidate ln-of-safe-fraction.
import mpmath as mp, sys
def logP(l, lam, dps):
    mp.mp.dps = dps
    z = 2*mp.sqrt(lam)
    B = [mp.besseli(d, z) for d in range(-l+1, l)]
    A = mp.matrix(l, l)
    for i in range(l):
        for j in range(l):
            A[i,j] = B[i-j+l-1]
    return -lam + mp.log(mp.det(A))
for l in [int(a) for a in sys.argv[1].split(',')]:
    for x in [float(a) for a in sys.argv[2].split(',')]:
        lam = (l/x)**2
        dps = int(3*mp.sqrt(lam)*l/2.3) + 60
        h = lam*0.005
        lp0 = logP(l, mp.mpf(lam), dps); lpm = logP(l, mp.mpf(lam-h), dps); lpp = logP(l, mp.mpf(lam+h), dps)
        rate = -lp0/lam; slope = -(lpp-lpm)/(2*h)
        print(f"l={l} x={x:.3f} lam={lam:.1f} rate={mp.nstr(rate,6)} slope(-dlnP/dlam)={mp.nstr(slope,6)} 1-slope={mp.nstr(1-slope,6)}", flush=True)
