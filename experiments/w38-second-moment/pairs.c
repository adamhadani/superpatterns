// W38 pairs.c: stratified Monte Carlo of p_j = Pr(pat(A)=pat(B) | |A∩B|=j) in a uniform sigma_N.
// R_avg = sum_j P(J=j) k! p_j, P(J=j) hypergeometric. Usage: pairs K N SAMPLES_PER_J SEED
#include "common.h"
int main(int argc,char**argv){
  int K=atoi(argv[1]),N=atoi(argv[2]); long S=atol(argv[3]); seed_rng(atol(argv[4])); init_fact();
  long KF=fact_[K]; int sigma[1024],perm[1024],comp[1024],A[16],B[16],vA[16],vB[16],idx[16];
  double R=0,Rvar=0; printf("k=%d N=%d C=%.4f samples/j=%ld\n",K,N,(double)N/K/K,S);
  for(int j=0;j<=K;j++){
    double PJ=(K-j>N-K)?0:exp(lbinom(K,j)+lbinom(N-K,K-j)-lbinom(N,K));
    if(PJ==0){printf("  j=%2d P(J=j)=0\n",j);continue;}
    double pj,se;
    if(j==0){pj=1.0/KF;se=0;} else if(j==K){pj=1;se=0;} else {
      long hit=0;
      for(long s=0;s<S;s++){
        for(int i=0;i<N;i++) sigma[i]=i; shuffle(sigma,N);
        for(int i=0;i<N;i++) perm[i]=i; shuffle(perm,N);
        for(int i=0;i<K;i++) A[i]=perm[i]; int nc=0; for(int i=K;i<N;i++) comp[nc++]=perm[i];
        for(int i=0;i<K;i++) idx[i]=i; shuffle(idx,K);
        for(int i=0;i<j;i++) B[i]=A[idx[i]];
        shuffle(comp,nc); for(int i=j;i<K;i++) B[i]=comp[i-j];
        isort(A,K); isort(B,K);
        for(int i=0;i<K;i++){vA[i]=sigma[A[i]];vB[i]=sigma[B[i]];}
        hit+= pat_code(vA,K)==pat_code(vB,K);
      }
      pj=(double)hit/S; se=sqrt(pj*(1-pj)/S);
    }
    printf("  j=%2d P(J=j)=%.4e  k!p_j=%.5g +- %.3g  term=%.5g\n",j,PJ,KF*pj,KF*se,PJ*KF*pj);
    R+=PJ*KF*pj; Rvar+=pow(PJ*KF*se,2);
  }
  printf("  R_avg=%.5f +- %.5f  lnR=%.4f\n",R,sqrt(Rvar),log(R));
  return 0;
}
