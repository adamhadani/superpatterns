// W38 exact.c: for each random sigma in S_N enumerate ALL k-subsets, bucket by pattern code.
// Outputs R_avg = k! * E[sum_pi M_pi^2] / binom(N,k)^2  (= E_pi E[M_pi^2]/mu^2), E[#distinct patterns]/k!,
// and quenched ratios E[M_pi^2]/mu^2 for the identity and a few random patterns.
// Usage: exact K N SAMPLES SEED
#include "common.h"
static int K,N; static int sigma[128]; static uint32_t *cnt; static int vals[16];
static void dfs(int j,int last,long code){
  if(j==K){ cnt[code]++; return; }
  for(int q=last+1;q<=N-(K-j);q++){ int v=sigma[q],r=0; for(int i=0;i<j;i++) r+=vals[i]<v; vals[j]=v; dfs(j+1,q,code*(j+1)+r); }
}
int main(int argc,char**argv){
  K=atoi(argv[1]); N=atoi(argv[2]); long S=atol(argv[3]); seed_rng(atol(argv[4])); init_fact();
  long KF=fact_[K]; cnt=calloc(KF,4);
  double binom=exp(lbinom(N,K)), mu=binom/KF;
  // quenched patterns: identity + 5 random (fixed seed 12345 for reproducibility)
  int NQ=6; long qcode[6]; int p[16]; for(int i=0;i<K;i++) p[i]=i; qcode[0]=pat_code(p,K);
  uint64_t save[4]; memcpy(save,rs,32); seed_rng(12345); for(int q=1;q<NQ;q++){ again: shuffle(p,K); qcode[q]=pat_code(p,K); for(int t=0;t<q;t++) if(qcode[t]==qcode[q]) goto again; } memcpy(rs,save,32);
  double s1=0,s2=0,d1=0,d2=0; double q1[6]={0},q2[6]={0},qm[6]={0};
  for(long s=0;s<S;s++){
    for(int i=0;i<N;i++) sigma[i]=i; shuffle(sigma,N);
    memset(cnt,0,KF*4); dfs(0,-1,0);
    double sum2=0; long nd=0; for(long c=0;c<KF;c++){ double m=cnt[c]; sum2+=m*m; nd+=cnt[c]>0; }
    double r=KF*sum2/(binom*binom); s1+=r; s2+=r*r; double dd=(double)nd/KF; d1+=dd; d2+=dd*dd;
    for(int q=0;q<NQ;q++){ double m=cnt[qcode[q]]; q1[q]+=m*m/(mu*mu); q2[q]+=pow(m*m/(mu*mu),2); qm[q]+=cnt[qcode[q]]>0; }
  }
  double m1=s1/S, se=sqrt((s2/S-m1*m1)/S), dm=d1/S, dse=sqrt((d2/S-dm*dm)/S);
  printf("k=%d N=%d C=%.4f samples=%ld mu=%.4g  R_avg=%.5f +- %.5f  lnR=%.4f  Edistinct/k!=%.4f +- %.4f  bound1/R=%.4f\n",K,N,(double)N/K/K,S,mu,m1,se,log(m1),dm,dse,1/m1);
  for(int q=0;q<NQ;q++){ double a=q1[q]/S, e=sqrt((q2[q]/S-a*a)/S); printf("  quenched %s code=%ld: E[M^2]/mu^2=%.4f +- %.4f  Pr(contained)=%.4f\n",q==0?"identity":"random  ",qcode[q],a,e,qm[q]/S); }
  return 0;
}
