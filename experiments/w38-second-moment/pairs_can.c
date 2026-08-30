// W38 pairs_can.c: stratified MC of p_j^can = Pr(A,B both leftmost-canonical and same pattern | |A∩B|=j), q = Pr(A canonical).
// R_can = k! sum_j P(J=j) p_j^can / q^2.   Usage: pairs_can K N SAMPLES_PER_J SEED
#include "common.h"
#include "canon.h"
int main(int argc,char**argv){
  int K=atoi(argv[1]),N=atoi(argv[2]); long S=atol(argv[3]); seed_rng(atol(argv[4])); init_fact();
  long KF=fact_[K]; int sigma[1024],sigma1[1026],perm[1024],comp[1024],A[16],B[16],vA[16],vB[16],idx[16];
  P_=malloc(sizeof(int)*(N+1)*(N+1));
  double R=0,Rvar=0,Rp=0,Rpvar=0; long canA=0,totA=0;
  printf("k=%d N=%d C=%.4f samples/j=%ld\n",K,N,(double)N/K/K,S);
  double PJ_[64],pc_[64],pcse_[64];
  for(int j=0;j<=K;j++){
    double PJ=(K-j>N-K)?0:exp(lbinom(K,j)+lbinom(N-K,K-j)-lbinom(N,K)); PJ_[j]=PJ;
    if(PJ==0){printf("  j=%2d P(J=j)=0\n",j);pc_[j]=0;pcse_[j]=0;continue;}
    long hit=0,hitc=0;
    for(long s=0;s<S;s++){
      for(int i=0;i<N;i++) sigma[i]=i; shuffle(sigma,N); for(int i=0;i<N;i++) sigma1[i+1]=sigma[i]+1; build_prefix(sigma1,N);
      for(int i=0;i<N;i++) perm[i]=i+1; shuffle(perm,N);
      for(int i=0;i<K;i++) A[i]=perm[i]; int nc=0; for(int i=K;i<N;i++) comp[nc++]=perm[i];
      for(int i=0;i<K;i++) idx[i]=i; shuffle(idx,K);
      for(int i=0;i<j;i++) B[i]=A[idx[i]];
      shuffle(comp,nc); for(int i=j;i<K;i++) B[i]=comp[i-j];
      isort(A,K); isort(B,K);
      for(int i=0;i<K;i++){vA[i]=sigma1[A[i]];vB[i]=sigma1[B[i]];}
      int cA=is_canonical(A,vA,K,N); canA+=cA; totA++;
      if(pat_code(vA,K)==pat_code(vB,K)){ hit++; if(cA && is_canonical(B,vB,K,N)) hitc++; }
    }
    double pj=(double)hit/S, se=sqrt(pj*(1-pj)/S), pc=(double)hitc/S, sec=sqrt(pc*(1-pc)/S); pc_[j]=pc; pcse_[j]=sec;
    printf("  j=%2d P(J=j)=%.4e  plain k!p_j=%.5g +- %.3g  can k!p_j=%.5g +- %.3g\n",j,PJ,KF*pj,KF*se,KF*pc,KF*sec);
    Rp+=PJ*KF*pj; Rpvar+=pow(PJ*KF*se,2);
  }
  double q=(double)canA/totA;
  for(int j=0;j<=K;j++){ R+=PJ_[j]*KF*pc_[j]/(q*q); Rvar+=pow(PJ_[j]*KF*pcse_[j]/(q*q),2); }
  printf("  plain R_avg=%.5f +- %.5f lnR=%.4f | q=%.5g  R_can=%.5f +- %.5f lnRcan=%.4f\n",Rp,sqrt(Rpvar),log(Rp),q,R,sqrt(Rvar),log(R));
  for(int j=0;j<=K;j++) if(PJ_[j]>0) printf("    canonical term j=%d: %.5g\n",j,PJ_[j]*KF*pc_[j]/(q*q));
  return 0;
}
