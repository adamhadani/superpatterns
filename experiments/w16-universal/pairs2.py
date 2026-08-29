# same-grid comparison of level 1 vs level 2 (identity: both parts of the pair condition are NOT included, only the
# same-cell part; decreasing: only the B-part), to separate discretization error from the true gain.
import pairs, numpy as np, math, sys
n=int(sys.argv[1]); nd=int(sys.argv[2])
for s,t in [(1.4,1.4),(1.5,1.5),(1.4,1.5),(1.5,1.4)]:
    r1=pairs.rho_pairs(pairs.ident_level1(s,t),s,t,n=n); r2=pairs.rho_pairs(pairs.ident_level2(s,t),s,t,n=n)
    print("identity n=%d s=%.2f t=%.2f  level1 kappa=%.5f  level2 kappa=%.5f"%(n,s,t,(s+t)/-math.log(r1),(s+t)/-math.log(r2))); sys.stdout.flush()
for s,t in [(1.4,1.5),(1.5,1.5),(1.4,1.4)]:
    r1=pairs.rho_pairs(pairs.ident_level1(s,t),s,t,n=nd)
    K=pairs.dec_level2_kernel(s,t,n=nd); r2=pairs.rho_from_K(K)
    print("decreasing n=%d s=%.2f t=%.2f  level1 kappa=%.5f  level2(B-part) kappa=%.5f"%(nd,s,t,(s+t)/-math.log(r1),(s+t)/-math.log(r2))); sys.stdout.flush()
