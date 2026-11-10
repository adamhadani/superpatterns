// W90: longest prefix of a periodic LAYERED pattern  J_{d_0} (+) J_{d_1} (+) ... (layer sizes periodic with period P)
// contained in a uniform random permutation, paired with LIS on the same permutation.
//
// Sweep left to right.  F[j] = least possible "top" (largest value used) of a copy of the first j layers among the
// points seen so far (F[0] = -1).  A partial layer at level j is (t, lo, cur, top): t points of layer j+1 chosen,
// decreasing, all above lo (= F[j] at the time its first point arrived), cur = its last (lowest) value, top = its
// first (highest) value.  A new value v extends it iff lo < v < cur.  A partial at level j can only matter while
// top < F[j+1], so every window (lo,cur) lies inside (F[j],F[j+1]) and a new value only interacts with its own level.
// Dominance: (t,lo,cur,top) is dominated by (t,lo',cur',top') if lo'<=lo, cur'>=cur, top'<=top.
//
// usage: layered_paired <sizes e.g. 2 | 3 | 1,2 | 2,3> n samples seed [v]     (v = validate against brute force, n<=20)
//        layered_paired <sizes> --stdin    (reads "n p_1 .. p_n" blocks, prints "layers total_length LIS")
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
static uint64_t s[4];
static inline uint64_t rotl(const uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static inline uint64_t rnd(void){uint64_t r=rotl(s[1]*5,7)*9,t=s[1]<<17;s[2]^=s[0];s[3]^=s[1];s[1]^=s[2];s[0]^=s[3];s[2]^=t;s[3]=rotl(s[3],45);return r;}
static void seed(uint64_t x){for(int i=0;i<4;i++){x+=0x9e3779b97f4a7c15ULL;uint64_t z=x;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;s[i]=z^(z>>31);}}
#define INF 0x7fffffff
static int P, SZ[64];
typedef struct {int t,lo,cur,top;} Pa;
typedef struct {Pa *a;int n,cap;} Vec;
static inline void vpush(Vec*v,Pa x){if(v->n==v->cap){v->cap=v->cap?2*v->cap:8;v->a=realloc(v->a,v->cap*sizeof(Pa));}v->a[v->n++]=x;}
static inline int dominates(Pa p,Pa q){return p.t==q.t && p.lo<=q.lo && p.cur>=q.cur && p.top<=q.top;}
static void add_filtered(Vec*v,Pa c){
  for(int i=0;i<v->n;i++) if(dominates(v->a[i],c)) return;
  int w=0; for(int i=0;i<v->n;i++) if(!dominates(c,v->a[i])) v->a[w++]=v->a[i]; v->n=w;
  vpush(v,c);
}
static long long maxpend;
int layered_fast(const int*y,int n){
  int cap=1024,L=0; int*F=malloc(cap*sizeof(int)); Vec*Q=calloc(cap,sizeof(Vec)); F[0]=-1;
  Pa *cand=malloc(sizeof(Pa)*1024); int ccap=1024;
  for(int i=0;i<n;i++){
    int v=y[i]; int lo=0,hi=L; while(lo<hi){int md=(lo+hi+1)/2; if(F[md]<v)lo=md;else hi=md-1;}
    int j=lo, d=SZ[j%P]; Vec*pv=&Q[j]; int best=INF, nc=0;
    if(d==1) best=v;
    else {
      for(int t=0;t<pv->n;t++){Pa p=pv->a[t]; if(p.lo<v && v<p.cur){ if(p.t+1==d){ if(p.top<best)best=p.top; } else { if(nc==ccap){ccap*=2;cand=realloc(cand,sizeof(Pa)*ccap);} Pa c={p.t+1,p.lo,v,p.top}; cand[nc++]=c; } } }
      Pa c={1,F[j],v,v}; if(nc==ccap){ccap*=2;cand=realloc(cand,sizeof(Pa)*ccap);} cand[nc++]=c;
    }
    if(best!=INF){
      if(j==L){ if(L+2>=cap){int oc=cap;cap*=2;F=realloc(F,cap*sizeof(int));Q=realloc(Q,cap*sizeof(Vec));memset(Q+oc,0,(cap-oc)*sizeof(Vec));pv=&Q[j];} L++; F[L]=best; }
      else if(best<F[j+1]) F[j+1]=best;
      int w=0; for(int t=0;t<pv->n;t++) if(pv->a[t].top<F[j+1]) pv->a[w++]=pv->a[t]; pv->n=w;
    }
    int lim = (j<L)? F[j+1] : INF;
    for(int t=0;t<nc;t++) if(cand[t].top<lim) add_filtered(pv,cand[t]);
    if(pv->n>maxpend) maxpend=pv->n;
  }
  for(int t=0;t<cap;t++) free(Q[t].a);
  free(Q);free(F);free(cand); return L;
}
int lis(const int*y,int n){int*t=malloc(n*sizeof(int));int len=0;for(int i=0;i<n;i++){int lo=0,hi=len;while(lo<hi){int md=(lo+hi)/2;if(t[md]<y[i])lo=md+1;else hi=md;}t[lo]=y[i];if(lo==len)len++;}free(t);return len;}
// ---------- brute force (n <= 24): G[i][j] = least top of a copy of the first j layers inside positions < i
static int bf_n; static const int*bf_y; static int bf_G[26][26];
static void bf_rec(int e,int pos,int need,int lastval,int j,int *out){
  // choose earlier elements of the layer going leftwards: positions decreasing, values increasing
  if(need==0){ // pos = position of first element p_1, lastval = its value (top); need chain of j layers left of pos with top < y[e]
    if(bf_G[pos][j] < bf_y[e] && lastval < *out) *out=lastval; return; }
  for(int q=pos-1;q>=0;q--) if(bf_y[q]>lastval) bf_rec(e,q,need-1,bf_y[q],j,out);
}
int layered_brute(const int*y,int n){
  bf_n=n;bf_y=y; for(int j=0;j<=n;j++) bf_G[0][j]=(j==0)?-1:INF;
  for(int e=0;e<n;e++){
    for(int j=0;j<=n;j++) bf_G[e+1][j]=bf_G[e][j];
    for(int j=0;j<n;j++){ if(bf_G[e][j]==INF && j>0) break; int d=SZ[j%P]; int out=INF; bf_rec(e,e,d-1,y[e],j,&out); if(out<bf_G[e+1][j+1]) bf_G[e+1][j+1]=out; }
  }
  int L=0; while(L<n && bf_G[n][L+1]<INF) L++; return L;
}
static long long preflen(int L){ long long per=0; for(int i=0;i<P;i++)per+=SZ[i]; long long k=(L/P)*per; for(int i=0;i<L%P;i++)k+=SZ[i]; return k; }
static int layers_fit(long long len){ int L=0; long long k=0; while(k+SZ[L%P]<=len){k+=SZ[L%P];L++;} return L; }
int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage: sizes n samples seed [v] | sizes --stdin\n");return 1;}
  char label[256]; strncpy(label,argv[1],255); label[255]=0;
  { char*tok=strtok(argv[1],","); P=0; while(tok){SZ[P++]=atoi(tok);tok=strtok(0,",");} }
  if(!strcmp(argv[2],"--stdin")){ int n; while(scanf("%d",&n)==1){int*y=malloc(n*sizeof(int));for(int i=0;i<n;i++) if(scanf("%d",y+i)!=1) return 2; int L=layered_fast(y,n); printf("%d %lld %d\n",L,preflen(L),lis(y,n)); free(y);} return 0; }
  int n=atoi(argv[2]);int S=atoi(argv[3]);seed(strtoull(argv[4],0,10)); int validate=argc>5;
  int*y=malloc(n*sizeof(int)); double sd=0,sd2=0,sl=0,sk=0,sD=0,sD2=0; long long bad=0;
  for(int it=0;it<S;it++){
    for(int i=0;i<n;i++)y[i]=i;
    for(int i=n-1;i>0;i--){uint64_t r=rnd()%(uint64_t)(i+1);int t=y[i];y[i]=y[r];y[r]=t;}
    int L=layered_fast(y,n); int b=lis(y,n); long long K=preflen(L), KI=preflen(layers_fit(b));
    if(validate){int c=layered_brute(y,n); if(c!=L)bad++;}
    double d=(double)K-b; sd+=d;sd2+=d*d; sl+=b; sk+=K; double D=(double)(KI-K); sD+=D; sD2+=D*D;
  }
  double md=sd/S,vd=sd2/S-md*md,mD=sD/S,vD=sD2/S-mD*mD;
  printf("sizes=%s n=%d S=%d E[LIS]=%.4f E[K]=%.4f E[K-LIS]=%.4f +- %.4f (sd %.3f) D=E[K_I-K]=%.4f +- %.4f D/sqrt(n)=%.5f +- %.5f maxpending=%lld",label,n,S,sl/S,sk/S,md,sqrt(vd/S),sqrt(vd),mD,sqrt(vD/S),mD/sqrt(n),sqrt(vD/S)/sqrt(n),maxpend);
  if(validate)printf(" MISMATCHES=%lld",bad);
  printf("\n"); return 0;
}
