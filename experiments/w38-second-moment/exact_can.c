// W38 exact_can.c: like exact.c but also counts leftmost-canonical copies Y_pi. Usage: exact_can K N SAMPLES SEED
// Outputs plain R_avg and canonical R_can = k! E[sum Y_pi^2]/(E sum Y_pi)^2, q = Pr(A canonical), and quenched ratios.
#include "common.h"
#include "canon.h"
static int K,N; static int sigma[128],sigma1[130]; static uint32_t *cnt,*cntc; static int vals[16],pos[16];
typedef struct{ long code; uint64_t mask; } CC;
static CC *cc; static long ncc, capcc;
static int cmpcc(const void*x,const void*y){ long a=((CC*)x)->code,b=((CC*)y)->code; return a<b?-1:a>b; }
static double Whist[16]; // E[# ordered same-pattern canonical pairs with overlap j] accumulators
static double sumY, sumY2, sumM2; static long ndist,ndistc;
static void dfs(int j,int last,long code){
  if(j==K){ cnt[code]++; if(is_canonical(pos,vals,K,N)){ cntc[code]++;
      if(ncc==capcc){capcc=capcc?2*capcc:1024; cc=realloc(cc,capcc*sizeof(CC));}
      uint64_t mk=0; for(int i=0;i<K;i++) mk|=1ULL<<pos[i]; cc[ncc].code=code; cc[ncc].mask=mk; ncc++; } return; }
  for(int q=last+1;q<=N-K+j+1;q++){ int v=sigma1[q],r=0; for(int i=0;i<j;i++) r+=vals[i]<v; vals[j]=v; pos[j]=q; dfs(j+1,q,code*(j+1)+r); }
}
int main(int argc,char**argv){
  K=atoi(argv[1]); N=atoi(argv[2]); long S=atol(argv[3]); seed_rng(atol(argv[4])); init_fact();
  long KF=fact_[K]; cnt=calloc(KF,4); cntc=calloc(KF,4); P_=malloc(sizeof(int)*(N+1)*(N+1));
  double binom=exp(lbinom(N,K)), mu=binom/KF;
  int NQ=6; long qcode[6]; int p[16]; for(int i=0;i<K;i++) p[i]=i; qcode[0]=pat_code(p,K);
  uint64_t save[4]; memcpy(save,rs,32); seed_rng(12345); for(int q=1;q<NQ;q++){ again: shuffle(p,K); qcode[q]=pat_code(p,K); for(int t=0;t<q;t++) if(qcode[t]==qcode[q]) goto again; } memcpy(rs,save,32);
  double s1=0,s2=0,y1=0,y1sq=0,y2=0,y2sq=0,dc=0; double qy1[6]={0},qy2[6]={0},qm2[6]={0},qc[6]={0};
  for(long s=0;s<S;s++){
    for(int i=0;i<N;i++) sigma[i]=i; shuffle(sigma,N); for(int i=0;i<N;i++) sigma1[i+1]=sigma[i]+1; build_prefix(sigma1,N);
    memset(cnt,0,KF*4); memset(cntc,0,KF*4); ncc=0; dfs(0,0,0);
    qsort(cc,ncc,sizeof(CC),cmpcc);
    for(long i=0;i<ncc;i++){ Whist[K]+=1; for(long t=i+1;t<ncc&&cc[t].code==cc[i].code;t++){ int ov=__builtin_popcountll(cc[i].mask&cc[t].mask); Whist[ov]+=2; } }
    double m2=0,yy=0,yy2=0; long ndc=0; for(long c=0;c<KF;c++){ double m=cnt[c],y=cntc[c]; m2+=m*m; yy+=y; yy2+=y*y; ndc+=cntc[c]>0; }
    double r=KF*m2/(binom*binom); s1+=r; s2+=r*r; y1+=yy; y1sq+=yy*yy; y2+=yy2; y2sq+=yy2*yy2; dc+=(double)ndc/KF;
    for(int q=0;q<NQ;q++){ double m=cnt[qcode[q]], y=cntc[qcode[q]]; qm2[q]+=m*m/(mu*mu); qy1[q]+=y; qy2[q]+=y*y; qc[q]+=cnt[qcode[q]]>0; }
  }
  double m1=s1/S, se=sqrt((s2/S-m1*m1)/S);
  double EY=y1/S, EYse=sqrt((y1sq/S-EY*EY)/S), EY2=y2/S, EY2se=sqrt((y2sq/S-EY2*EY2)/S);
  double Rc=KF*EY2/(EY*EY), Rcse=Rc*sqrt(pow(EY2se/EY2,2)+4*pow(EYse/EY,2));
  printf("k=%d N=%d C=%.4f samples=%ld mu=%.4g | plain R_avg=%.5f +- %.5f lnR=%.4f | canonical: q=E[Y_tot]/binom=%.5g EY_pi=%.5g R_can=%.5f +- %.5f lnRcan=%.4f | Edistinct_can/k!=%.4f\n",
    K,N,(double)N/K/K,S,mu,m1,se,log(m1),EY/binom,EY/KF,Rc,Rcse,log(Rc),dc/S);
  for(int q=0;q<NQ;q++){ double a=qm2[q]/S, ey=qy1[q]/S, ey2=qy2[q]/S; printf("  quenched %s code=%ld: plain E[M^2]/mu^2=%.4f  canonical EY=%.4g EY^2/(EY)^2=%.4f  Pr(contained)=%.4f\n",q==0?"identity":"random  ",qcode[q],a,ey,ey2/(ey*ey),qc[q]/S); }
  { double EYtot=y1/S; printf("  canonical overlap decomposition: term_j = k! E[W_j]/(E Y_tot)^2 (sum = R_can)\n");
    for(int j=0;j<=K;j++) if(Whist[j]>0) printf("    j=%2d  E[W_j]=%.5g  term=%.5g\n",j,Whist[j]/S,KF*(Whist[j]/S)/(EYtot*EYtot)); }
  return 0;
}
