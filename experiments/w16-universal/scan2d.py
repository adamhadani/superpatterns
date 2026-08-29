import pot2d, math, sys, time
n=int(sys.argv[1])
for lam in [1e-3,0.5,1.0,2.0]:
    for s in [1.3,1.5,1.7]:
        t0=time.time(); r=pot2d.rho(lam,s,s,n=n); print("n=%d lam=%.3f s=t=%.2f rho=%.6f kappa=%.5f (%.0fs)"%(n,lam,s,r,2*s/(-math.log(r)),time.time()-t0)); sys.stdout.flush()
