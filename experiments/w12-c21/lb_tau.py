# c_tau >= max_delta g(p_tau(delta^2))/delta,  p_tau(lam) >= sum_{k<=10} P(Pois=k) q_k + P(Pois>10) q_10,  q_k = P(tau in S_k) (exact, pat.out)
import math, collections
q=collections.defaultdict(dict)
for line in open('pat.out'):
    k,t,c,pr=line.split(); q[t][int(k)]=float(pr)
def g(p): return 2*math.sqrt(p)/(1+math.sqrt(p))
def plow(t,lam,K=10):
    tot=0; cum=0
    for k in range(0,K+1):
        pk=math.exp(-lam)*lam**k/math.factorial(k); cum+=pk; tot+=pk*q[t].get(k,0.0)
    return tot+(1-cum)*q[t][K]
def pexact21(lam):
    # 1 - e^{-lam} I0(2 sqrt lam)
    s=0; x=lam
    for k in range(60): s+=x**k/(math.factorial(k)**2)
    return 1-math.exp(-lam)*s
def best(pf):
    b=(0,0)
    for i in range(20,600):
        d=i/100; v=g(pf(d*d))/d
        if v>b[0]: b=(v,d)
    return b
print("21 exact p:   c_21 >= %.4f at delta=%.2f"%best(pexact21))
print("21 truncated: c_21 >= %.4f at delta=%.2f"%best(lambda l: plow('21',l)))
for t in ('123','132','1234','1243','2143','1342','1324','12345','21345','25314','13254'):
    b=best(lambda l: plow(t,l)); j=len(t)
    print("tau=%-6s j=%d  c_tau >= %.4f at delta=%.2f   (2/j=%.4f, ratio %.3f)"%(t,j,b[0],b[1],2/j,b[0]*j/2))
# thresholded version for 21: use cells containing (21)^{+t}, weight t
for t,name in ((2,'2143'),(3,'214365')):
    b=best(lambda l: plow(name,l)); print("21 with cell weight %d (pattern %s): c_21 >= %.4f at delta=%.2f"%(t,name,t*b[0],b[1]))
# universal Arratia-grid bound: p_tau(lam) >= (1-exp(-lam/j^2))^j
for j in (2,3,4,5,8,16,64):
    b=best(lambda l: (1-math.exp(-l/j/j))**j); print("universal j=%d: c_tau >= %.4f  (= %.3f * 2/j)"%(j,b[0],b[0]*j/2))
