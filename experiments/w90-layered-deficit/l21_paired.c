// Fast exact L21 (longest 21-chain: copy of 21^{(+)m}) and LIS on the same uniform random permutation.
// Sweep left to right. F[j] = min top height of a j-chain among seen points (F[0] = -inf).
// Pending apex at level j: (lo, hi) with lo = F[j] at arrival, hi = own height; a later point y with
// lo < y < hi completes pair j+1 with top hi.  Only the top level of each apex matters.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
static uint64_t s[4];
static inline uint64_t rotl(const uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static inline uint64_t rnd(void){uint64_t r=rotl(s[1]*5,7)*9,t=s[1]<<17;s[2]^=s[0];s[3]^=s[1];s[1]^=s[2];s[0]^=s[3];s[2]^=t;s[3]=rotl(s[3],45);return r;}
static void seed(uint64_t x){for(int i=0;i<4;i++){x+=0x9e3779b97f4a7c15ULL;uint64_t z=x;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;s[i]=z^(z>>31);}}
typedef struct {int lo,hi;} Ap;
typedef struct {Ap *a;int n,cap;} Vec;
static inline void vpush(Vec*v,Ap x){if(v->n==v->cap){v->cap=v->cap?2*v->cap:4;v->a=realloc(v->a,v->cap*sizeof(Ap));}v->a[v->n++]=x;}
int l21_fast(const int*y,int n,long long*maxpend){
  int cap=1024;int L=0; // F[1..L]
  int *F=malloc(cap*sizeof(int)); Vec *P=calloc(cap,sizeof(Vec)); // P[j]: pending apexes at level j (0..L)
  F[0]=-1; long long mp=0;
  for(int i=0;i<n;i++){
    int v=y[i];
    // level j = #{t>=1: F[t]<v}
    int lo=0,hi=L; while(lo<hi){int md=(lo+hi+1)/2; if(F[md]<v)lo=md;else hi=md-1;}
    int j=lo;
    Vec*pv=&P[j]; int best=0x7fffffff;
    for(int t=0;t<pv->n;t++){Ap a=pv->a[t]; if(a.lo<v && v<a.hi && a.hi<best) best=a.hi;}
    if(best!=0x7fffffff){
      if(j==L){ // new threshold
        if(L+2>=cap){cap*=2;F=realloc(F,cap*sizeof(int));P=realloc(P,cap*sizeof(Vec));memset(P+cap/2,0,(cap/2)*sizeof(Vec));}
        L++; F[L]=best;
      } else if(best<F[j+1]) F[j+1]=best;
      // prune level j apexes with hi >= F[j+1]
      int w=0; for(int t=0;t<pv->n;t++) if(pv->a[t].hi<F[j+1]) pv->a[w++]=pv->a[t]; pv->n=w;
    }
    Ap na={F[j],v}; vpush(pv,na); if(pv->n>mp)mp=pv->n;
  }
  for(int t=0;t<cap;t++) free(P[t].a);
  free(P);free(F); if(maxpend)*maxpend=mp; return L;
}
int lis(const int*y,int n){int*t=malloc(n*sizeof(int));int len=0;for(int i=0;i<n;i++){int lo=0,hi=len;while(lo<hi){int md=(lo+hi)/2;if(t[md]<y[i])lo=md+1;else hi=md;}t[lo]=y[i];if(lo==len)len++;}free(t);return len;}
// brute force for validation
int l21_brute(const int*s_,int n){int m=n/2;int G[64][34];for(int j=0;j<=m;j++)G[0][j]=(j==0)?-1:1000000;for(int i=0;i<n;i++){for(int j=0;j<=m;j++)G[i+1][j]=G[i][j];for(int a=0;a<i;a++)if(s_[a]>s_[i]){int j=0;while(j<m&&G[a][j+1]<s_[i])j++;if(j<m&&s_[a]<G[i+1][j+1])G[i+1][j+1]=s_[a];}}int j=0;while(j<m&&G[n][j+1]<1000000)j++;return j;}
int main(int argc,char**argv){
  if(argc==2 && !strcmp(argv[1],"--stdin")){ // same input format as w40 pruned.c: n then a permutation of 1..n; prints "L21 LIS"
    int n; while(scanf("%d",&n)==1){int*y=malloc(n*sizeof(int));for(int i=0;i<n;i++){if(scanf("%d",y+i)!=1)return 2;}
      printf("%d %d\n",l21_fast(y,n,0),lis(y,n));free(y);} return 0; }
  if(argc<4){fprintf(stderr,"usage: n samples seed [validate]  |  --stdin\n");return 1;}
  int n=atoi(argv[1]);int S=atoi(argv[2]);seed(strtoull(argv[3],0,10));
  int validate=argc>4;
  int*y=malloc(n*sizeof(int));
  double sd=0,sd2=0,sl=0,sl2=0,sL=0,sL2=0,sf=0; long long mpmax=0; long long bad=0;
  for(int it=0;it<S;it++){
    for(int i=0;i<n;i++)y[i]=i;
    for(int i=n-1;i>0;i--){uint64_t r=rnd()%(uint64_t)(i+1);int t=y[i];y[i]=y[r];y[r]=t;}
    long long mp;int a=l21_fast(y,n,&mp);int b=lis(y,n);
    if(validate){int c=l21_brute(y,n);if(c!=a)bad++;}
    if(mp>mpmax)mpmax=mp;
    double d=2.0*a-b; sd+=d;sd2+=d*d;sl+=b;sl2+=(double)b*b;sL+=a;sL2+=(double)a*a; sf+= 2.0*a-2*(b/2);
    if(!validate && S<=64) {printf("%d %d\n",a,b);}
  }
  double md=sd/S,vd=sd2/S-md*md,ml=sl/S,vl=sl2/S-ml*ml,mL=sL/S,vL=sL2/S-mL*mL;
  printf("n=%d S=%d  E[LIS]=%.4f (sd %.3f)  E[L21]=%.4f (sd %.3f)  E[2L21-LIS]=%.4f +- %.4f (sd %.3f)  E[2L21-2floor(LIS/2)]=%.4f  maxpending=%lld",n,S,ml,sqrt(vl),mL,sqrt(vL),md,sqrt(vd/S),sqrt(vd),sf/S,mpmax);
  if(validate)printf("  MISMATCHES=%lld",bad);
  printf("\n");
  return 0;
}
