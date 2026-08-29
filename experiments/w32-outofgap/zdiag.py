import sys, bisect, math, numpy as np
from single_strip import load_V
from twosided import gap_of, search
k=512; C=0.6; m=1; h=k
V=load_V(k); rng=np.random.default_rng(5)
N=rng.poisson(C*k*k); P=rng.random((N,2)); xs=P[:,0]*k; ys=P[:,1]*k
o=np.argsort(xs); X=xs[o]; Y=ys[o]; us=np.zeros(N,bool)
pi=rng.permutation(k); placed=[dict()]; sv=[[]]
a=0.0; b=float(k); pl=0; pr=k-1
ZL=[];ZR=[];ZC=[];TT=[];UU=[]; phisum=0.0; chk=[]
while pl<=pr:
    cands=[]
    for side,p in ((+1,pl),(-1,pr)):
        if side<0 and pl==pr: continue
        v=int(pi[p]); yL,yR,mb,ma=gap_of(v,0,h,sv,placed)
        best,bq=search(X,Y,us,a,b,side,yL,yR,mb,ma,V[mb],V[ma],C,0.0)
        n=mb+ma+1; Z=best-V[n]/(C*(yR-yL))
        cands.append((best,side,p,v,bq,Z))
    cands.sort(); best,side,p,v,bq,Z=cands[0]
    chk.append(Z)
    if bq<0: print("fail"); break
    if len(cands)==2:
        zl=[c[5] for c in cands if c[1]>0][0]; zr=[c[5] for c in cands if c[1]<0][0]
        ZL.append(zl); ZR.append(zr); ZC.append(min(zl,zr)); TT.append(len(sv[0]))
    us[bq]=True; placed[0][v]=Y[bq]; bisect.insort(sv[0],v)
    if side>0: UU.append(X[bq]-a); a=X[bq]; pl+=1
    else: UU.append(b-X[bq]); b=X[bq]; pr-=1
print('sum chosen Z (all steps)/k', sum(chk)/k)
ZL=np.array(ZL);ZR=np.array(ZR);ZC=np.array(ZC);TT=np.array(TT);UU=np.array(UU)
print("consumption/k %.4f implied %.4f; V_k/(Ck)/k = %.4f"%(UU.sum()/k, C*UU.sum()/k, V[k]/(C*k)/k))
print("sum Z chosen/k = %.4f ; mean ZL %.4f ZR %.4f min %.4f  sd ZL %.4f  mean|ZL-ZR| %.4f"%(ZC.sum()/k,ZL.mean(),ZR.mean(),ZC.mean(),ZL.std(),np.abs(ZL-ZR).mean()))
UU=UU[:len(TT)]
for lo in np.arange(0,1,0.2):
    s=(TT>=lo*k)&(TT<(lo+.2)*k)
    print("t/k [%.1f,%.1f): mean ZL %.3f  sd ZL %.3f  mean min %.3f  mean u %.3f"%(lo,lo+.2,ZL[s].mean(),ZL[s].std(),ZC[s].mean(),UU[s].mean() if s.sum() else 0))
