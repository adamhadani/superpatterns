/* boxes.c -- Poisson(N) points in the unit square; LIS path by patience sorting (a maximal chain);
   for chain points p_1<...<p_L count the boxes U_i = (x_{i-1},x_i) x (y_i,y_{i+1}) that contain a point
   (each nonempty box gives a descent pair (q,p_i); using every other index they are stacked), plus the greedy
   maximal set of pairwise stackable nonempty boxes (indices i with gap >= 2).  Also L_21 lower bound = that count.
   Usage: ./boxes N samples [seed] */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static unsigned long long s[4];
static inline unsigned long long rotl(unsigned long long x,int k){return (x<<k)|(x>>(64-k));}
static unsigned long long nxt(void){unsigned long long r=rotl(s[1]*5,7)*9,t=s[1]<<17;s[2]^=s[0];s[3]^=s[1];s[1]^=s[2];s[0]^=s[3];s[2]^=t;s[3]=rotl(s[3],45);return r;}
static inline double U(void){return (nxt()>>11)*(1.0/9007199254740992.0);}
static int cmpd(const void*a,const void*b){double x=*(double*)a,y=*(double*)b;return x<y?-1:x>y;}
int main(int argc,char**argv){
  long N=atol(argv[1]); int S=atoi(argv[2]); unsigned long long seed=argc>3?atoll(argv[3]):1;
  s[0]=seed^0x9E3779B97F4A7C15ULL;s[1]=seed*7+1;s[2]=seed*13+5;s[3]=seed*31+9; for(int i=0;i<20;i++)nxt();
  double *xs=malloc(N*sizeof(double)),*ys=malloc(N*sizeof(double)); int *pile=malloc(N*sizeof(int)),*prev=malloc(N*sizeof(int)),*top=malloc(N*sizeof(int));
  double *topy=malloc(N*sizeof(double)); int *chain=malloc(N*sizeof(int));
  double sumL=0,sumNE=0,sumG=0;
  for(int it=0;it<S;it++){
    /* Poisson(N) points: use exactly N points (binomial version; same asymptotics) */
    for(long i=0;i<N;i++){xs[i]=U();ys[i]=U();}
    /* sort by x: sort indices */
    /* simple: generate x sorted via uniform spacings: just sort */
    { /* sort pairs by x */
      double *pr=malloc(2*N*sizeof(double)); for(long i=0;i<N;i++){pr[2*i]=xs[i];pr[2*i+1]=ys[i];}
      qsort(pr,N,2*sizeof(double),cmpd); for(long i=0;i<N;i++){xs[i]=pr[2*i];ys[i]=pr[2*i+1];} free(pr);
    }
    int L=0;
    for(long i=0;i<N;i++){ /* patience: first pile with top > y */
      int lo=0,hi=L; while(lo<hi){int m=(lo+hi)/2; if(topy[m]>ys[i])hi=m; else lo=m+1;}
      pile[i]=lo; prev[i]=lo>0?top[lo-1]:-1; top[lo]=i; topy[lo]=ys[i]; if(lo==L)L++;
    }
    /* recover chain */
    int k=L; int cur=top[L-1]; while(cur>=0){chain[--k]=cur;cur=prev[cur];}
    /* boxes: U_i = (x_{i-1},x_i) x (y_i,y_{i+1}) for i=1..L-2 (0-based: chain[i-1],chain[i],chain[i+1]) */
    int ne=0,g=0,last=-10;
    for(int i=1;i<L-1;i++){
      double x0=xs[chain[i-1]],x1=xs[chain[i]],y0=ys[chain[i]],y1=ys[chain[i+1]];
      int found=0;
      for(long j=chain[i-1]+1;j<chain[i];j++) if(ys[j]>y0&&ys[j]<y1){found=1;break;}
      if(found){ne++; if(i-last>=2){g++;last=i;}}
    }
    sumL+=L; sumNE+=ne; sumG+=g;
  }
  double sq=sqrt((double)N);
  printf("N %ld S %d: LIS/sqrtN %.4f  nonempty boxes/L %.4f  greedy stacked/L %.4f  => L21/sqrtN >= %.4f\n",N,S,sumL/S/sq,sumNE/sumL,sumG/sumL,sumG/S/sq);
  return 0;
}
