# Exact series for the square-sweep first-descent rule (tau = 21):
#   E[cost] = sum_{n>=1} Gamma(n+3/2) * n*(3n+7) / (2*(n+2)*n!*(n+1)!)
from mpmath import mp, gamma, factorial, sqrt, e, mpf
mp.dps = 30
S = mpf(0)
for n in range(1, 60):
    T = gamma(n+mpf(3)/2)*n*(3*n+7)/(2*(n+2)*factorial(n)*factorial(n+1))
    S += T
    if n <= 10: print(n, mp.nstr(T, 12), mp.nstr(S, 15))
print("E cost (square) =", mp.nstr(S, 20), " c_21 >= 2/Ecost =", mp.nstr(2/S, 15))
Es = sqrt(2*e*(4-e)); print("E cost (strip)  =", mp.nstr(Es, 15), " c_21 >=", mp.nstr(2/Es, 15))
# probability check: sum_n n/(n+1)! = 1 ; E(#points) = e
print("sum P(N=n) =", mp.nstr(sum(mpf(n)/factorial(n+1) for n in range(1,60)),15))
print("ratio bound T_{n+1}/T_n at n=9:", mp.nstr((gamma(10+mpf(3)/2)*10*37/(2*12*factorial(10)*factorial(11)))/(gamma(9+mpf(3)/2)*9*34/(2*11*factorial(9)*factorial(10))),8))
