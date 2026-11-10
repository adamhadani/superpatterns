// review-2: independent L21 / LIS code for Poisson squares, and test of the cutting inequality of Lemma R.
// Written from scratch for the review (not derived from w90 l21_paired.c; cross-checked against it via `perm` mode).
//
// L21(P) = largest m such that P contains 21 (+) 21 (+) ... (+) 21 (m blocks).
// Sweep points by increasing x. Y[k] = min over copies of 21^{(+)k} among swept points of the top height
// (height of the last 'a' point). A new point b (height v) can only be the last point of a copy; it closes a
// block opened by an earlier point a (y_a > v) provided some k-copy lies entirely to the left of a and below v,
// i.e. Yk(at arrival of a) < v. Only k = level(a) = max{k: Yk(arrival of a) < y_a} and only level(a)=level(b)
// can improve Y (see review-2.md, section 3.1). Per level, the arrival thresholds are non-increasing in time.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>

static uint64_t S4[4];
static inline uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static inline uint64_t nxt(void){ // xoshiro256++
  uint64_t r=rotl(S4[0]+S4[3],23)+S4[0],t=S4[1]<<17;
  S4[2]^=S4[0];S4[3]^=S4[1];S4[1]^=S4[2];S4[0]^=S4[3];S4[2]^=t;S4[3]=rotl(S4[3],45);return r;}
static void seedrng(uint64_t x){for(int i=0;i<4;i++){x+=0x9e3779b97f4a7c15ULL;uint64_t z=x;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;S4[i]=z^(z>>31);}}
static inline double unif(void){return ((nxt()>>11)+0.5)*(1.0/9007199254740992.0);} // (0,1)

typedef struct {double *Y,*th; int *head,*prv; int cap;} Work;
static void wreserve(Work*w,int n){ if(n+2<=w->cap) return; w->cap=2*n+16;
  w->Y=realloc(w->Y,w->cap*sizeof(double)); w->th=realloc(w->th,w->cap*sizeof(double));
  w->head=realloc(w->head,w->cap*sizeof(int)); w->prv=realloc(w->prv,w->cap*sizeof(int)); }

// y[0..n-1]: heights of the points in order of increasing x (all distinct).
static int l21(const double*y,int n,Work*w){
  wreserve(w,n); double*Y=w->Y,*th=w->th; int*head=w->head,*prv=w->prv;
  int L=0; Y[0]=-INFINITY; head[0]=-1;
  for(int i=0;i<n;i++){
    double v=y[i];
    int lo=0,hi=L; while(lo<hi){int md=(lo+hi+1)/2; if(Y[md]<v) lo=md; else hi=md-1;}
    int k=lo; double best=INFINITY;
    for(int j=head[k]; j>=0 && th[j]<v; j=prv[j]) if(y[j]>v && y[j]<best) best=y[j];
    if(best<INFINITY){ if(k==L){L++; Y[L]=best; head[L]=-1;} else if(best<Y[k+1]) Y[k+1]=best; }
    th[i]=Y[k]; prv[i]=head[k]; head[k]=i;
  }
  return L;
}
// reference: O(n^3) DP straight from the definition. v = permutation of 0..n-1 (heights by x-order), n<=200.
// best[i][t] = max #blocks using points of index >= i and height > t-1 (t = 0..n).
static int l21_ref(const int*v,int n){
  static int best[202][202]; for(int t=0;t<=n;t++) best[n][t]=0; for(int t=0;t<=n;t++) best[n+1][t]=0;
  for(int i=n-1;i>=0;i--) for(int t=0;t<=n;t++){
    int b=best[i+1][t];
    if(v[i]>=t){ for(int q=i+1;q<n;q++) if(v[q]>=t && v[q]<v[i]){ int c=1+best[q+1][v[i]+1]; if(c>b) b=c; } }
    best[i][t]=b; }
  return best[0][0];
}
static int lis(const double*y,int n,double*tmp){int len=0;for(int i=0;i<n;i++){int lo=0,hi=len;while(lo<hi){int md=(lo+hi)/2;if(tmp[md]<y[i])lo=md+1;else hi=md;}tmp[lo]=y[i];if(lo==len)len++;}return len;}

// Poisson process of intensity 1 on [0,S]^2, returned sorted by x.
static int poisson_square(double S,double**px,double**py,int*cap){
  int n=0; double x=0;
  for(;;){ x+=-log(unif())/S; if(x>S) break;
    if(n==*cap){*cap=*cap?2*(*cap):1024; *px=realloc(*px,*cap*sizeof(double)); *py=realloc(*py,*cap*sizeof(double));}
    (*px)[n]=x; (*py)[n]=S*unif(); n++; }
  return n;
}
static int cmpd(const void*a,const void*b){double x=*(const double*)a,y=*(const double*)b;return (x>y)-(x<y);}
typedef struct {double x; int type;} Bp; // type 0 = entry, 1 = exit
static int cmpbp(const void*a,const void*b){double x=((const Bp*)a)->x,y=((const Bp*)b)->x;return (x>y)-(x<y);}

int main(int argc,char**argv){
  if(argc<2){fprintf(stderr,"usage: est T samples seed | cut T samples seed | validate n samples seed | perm n samples seed\n");return 1;}
  Work w={0};
  if(!strcmp(argv[1],"validate")){ // fast vs reference DP on uniform permutations
    int n=atoi(argv[2]),S=atoi(argv[3]); seedrng(strtoull(argv[4],0,10));
    int*v=malloc(n*sizeof(int)); double*y=malloc(n*sizeof(double)); long bad=0; double sum=0;
    for(int it=0;it<S;it++){ for(int i=0;i<n;i++)v[i]=i; for(int i=n-1;i>0;i--){int r=nxt()%(uint64_t)(i+1);int t=v[i];v[i]=v[r];v[r]=t;}
      for(int i=0;i<n;i++)y[i]=v[i]; int a=l21(y,n,&w),b=l21_ref(v,n); sum+=a; if(a!=b){bad++; if(bad<=5){printf("MISMATCH fast=%d ref=%d perm:",a,b);for(int i=0;i<n;i++)printf(" %d",v[i]);printf("\n");}}}
    printf("validate n=%d samples=%d mismatches=%ld meanL21=%.4f\n",n,S,bad,sum/S); return 0; }
  if(!strcmp(argv[1],"perm")){ // print permutations (1-based) and my L21, LIS: for cross-check with w90 l21_paired --stdin
    int n=atoi(argv[2]),S=atoi(argv[3]); seedrng(strtoull(argv[4],0,10));
    int*v=malloc(n*sizeof(int)); double*y=malloc(n*sizeof(double)),*tmp=malloc(n*sizeof(double));
    FILE*fp=fopen(argv[5],"w"),*fo=fopen(argv[6],"w");
    for(int it=0;it<S;it++){ for(int i=0;i<n;i++)v[i]=i; for(int i=n-1;i>0;i--){int r=nxt()%(uint64_t)(i+1);int t=v[i];v[i]=v[r];v[r]=t;}
      for(int i=0;i<n;i++)y[i]=v[i]; fprintf(fp,"%d",n); for(int i=0;i<n;i++)fprintf(fp," %d",v[i]+1); fprintf(fp,"\n");
      fprintf(fo,"%d %d\n",l21(y,n,&w),lis(y,n,tmp)); }
    fclose(fp);fclose(fo); return 0; }
  if(!strcmp(argv[1],"est")){
    double T=atof(argv[2]); int S=atoi(argv[3]); seedrng(strtoull(argv[4],0,10));
    double*px=0,*py=0,*tmp=0; int cap=0,tcap=0; double sa=0,sa2=0,sb=0,sb2=0,sd=0,sd2=0,sn=0;
    for(int it=0;it<S;it++){ int n=poisson_square(T,&px,&py,&cap); if(n>tcap){tcap=2*n+16;tmp=realloc(tmp,tcap*sizeof(double));}
      int a=l21(py,n,&w),b=lis(py,n,tmp); double d=b-2.0*a; sa+=a;sa2+=(double)a*a;sb+=b;sb2+=(double)b*b;sd+=d;sd2+=d*d;sn+=n; }
    double ma=sa/S,mb=sb/S,md=sd/S;
    printf("est T=%g samples=%d seed=%s meanN=%.2f L21=%.5f se=%.5f sd=%.4f LIS=%.5f se=%.5f D=LIS-2L21=%.5f se=%.5f\n",T,S,argv[4],sn/S,
      ma,sqrt((sa2/S-ma*ma)/(S-1)),sqrt(sa2/S-ma*ma),mb,sqrt((sb2/S-mb*mb)/(S-1)),md,sqrt((sd2/S-md*md)/(S-1)));
    printf("raw %g %d %.17g %.17g %.17g %.17g %.17g %.17g\n",T,S,sa,sa2,sb,sb2,sd,sd2);
    return 0; }
  if(!strcmp(argv[1],"cut")){ // configuration on [0,2T]^2; m vs 1+M+M'
    double T=atof(argv[2]); int S=atoi(argv[3]); seedrng(strtoull(argv[4],0,10)); double Sd=2*T;
    double*px=0,*py=0; int cap=0; double*sub=0; Bp*bp=0; int scap=0;
    long viol=0,violg=0,incons=0; double sm=0,sM=0,sM2=0,sMp=0,sMg=0,sMgp=0,sslack=0; int minslack=1<<30,maxslack=-1;
    long K=(long)ceil(4*T*T-1e-9); double delta=1.0/(2*T);
    for(int it=0;it<S;it++){
      int n=poisson_square(Sd,&px,&py,&cap); if(n+2>scap){scap=2*n+16; sub=realloc(sub,scap*sizeof(double)); bp=realloc(bp,2*scap*sizeof(Bp));}
      int m=l21(py,n,&w);
      // exact M = sup_x L21([0,x] x [0,2T-x]): entries at x_i, exits just after 2T-y_i
      int M=0,Mp=0;
      for(int side=0;side<2;side++){
        int nb=0; for(int i=0;i<n;i++){ bp[nb].x=px[i]; bp[nb].type=(side==0)?0:1; nb++; bp[nb].x=Sd-py[i]; bp[nb].type=(side==0)?1:0; nb++; }
        qsort(bp,nb,sizeof(Bp),cmpbp);
        // intervals: (-,bp[0]), (bp[j],bp[j+1]), (bp[nb-1],+); evaluate those with left = entry (or start) and right = exit (or end)
        for(int j=-1;j<nb;j++){
          int lt=(j<0)?0:bp[j].type, rt=(j+1>=nb)?1:bp[j+1].type; if(!(lt==0 && rt==1)) continue;
          double xl=(j<0)?0:bp[j].x, xr=(j+1>=nb)?Sd:bp[j+1].x, x=0.5*(xl+xr); int c=0;
          if(side==0){ for(int i=0;i<n && px[i]<=x;i++) if(py[i]<=Sd-x) sub[c++]=py[i]; }
          else { for(int i=0;i<n;i++) if(px[i]>=x && py[i]>=Sd-x) sub[c++]=py[i]; }
          int v=l21(sub,c,&w); if(side==0){if(v>M)M=v;} else {if(v>Mp)Mp=v;}
        }
      }
      // grid rectangles of the proof: R~_k = [0,(k+1)d] x [0,2T-kd], R~'_k = reflection
      int Mg=0,Mgp=0;
      for(long k=0;k<K;k++){ double a=(k+1)*delta,b=Sd-k*delta; int c=0;
        for(int i=0;i<n && px[i]<=a;i++) if(py[i]<=b) sub[c++]=py[i];
        int v=l21(sub,c,&w); if(v>Mg)Mg=v;
        c=0; for(int i=0;i<n;i++) if(px[i]>=Sd-a && py[i]>=Sd-b) sub[c++]=py[i];
        v=l21(sub,c,&w); if(v>Mgp)Mgp=v; }
      int slack=1+M+Mp-m; if(slack<0){viol++; printf("VIOLATION sample=%d m=%d M=%d M'=%d n=%d\n",it,m,M,Mp,n);}
      if(1+Mg+Mgp<m){violg++; printf("VIOLATION(grid) sample=%d m=%d Mg=%d Mg'=%d\n",it,m,Mg,Mgp);}
      if(Mg<M||Mgp<Mp){incons++; printf("INCONSISTENT grid<exact sample=%d M=%d Mg=%d M'=%d Mg'=%d\n",it,M,Mg,Mp,Mgp);}
      if(slack<minslack)minslack=slack; if(slack>maxslack)maxslack=slack;
      sm+=m;sM+=M;sM2+=(double)M*M;sMp+=Mp;sMg+=Mg;sMgp+=Mgp;sslack+=slack;
    }
    printf("cut T=%g (square side %g) samples=%d seed=%s gridK=%ld  mean m=%.4f  mean M=%.4f (sd %.3f)  mean M'=%.4f  mean Mgrid=%.4f  mean M'grid=%.4f  slack 1+M+M'-m: mean=%.4f min=%d max=%d  violations(exact)=%ld violations(grid)=%ld grid<exact=%ld\n",
      T,Sd,S,argv[4],K,sm/S,sM/S,sqrt(sM2/S-(sM/S)*(sM/S)),sMp/S,sMg/S,sMgp/S,sslack/S,minslack,maxslack,viol,violg,incons);
    return 0; }
  return 1;
}
