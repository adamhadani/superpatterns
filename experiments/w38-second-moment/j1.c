// W38 j1.c: k!p_1 (pairs sharing exactly one point) via restriction sampling: 2k-1 distinct positions,
// 2k-1 distinct values from [N] (or continuum N=0), uniform bijection. Usage: j1 K N SAMPLES SEED
#include "common.h"
static int cmpd(const void*a,const void*b){double x=*(double*)a-*(double*)b;return x<0?-1:x>0;}
int main(int argc,char**argv){
  int K=atoi(argv[1]); long N=atol(argv[2]); long S=atol(argv[3]); seed_rng(atol(argv[4])); init_fact();
  int n=2*K-1; double xs[64],ys[64]; long hit=0;
  int idx[64],vA[32],vB[32]; double ax[32],ay[32],bx[32],by[32];
  for(long s=0;s<S;s++){
    if(N==0){ for(int i=0;i<n;i++){xs[i]=(double)rng()/1.8446744e19; ys[i]=(double)rng()/1.8446744e19;} }
    else { // distinct integers
      for(int i=0;i<n;i++){ again1:; xs[i]=1+rnd(N); for(int t=0;t<i;t++) if(xs[t]==xs[i]) goto again1; }
      for(int i=0;i<n;i++){ again2:; ys[i]=1+rnd(N); for(int t=0;t<i;t++) if(ys[t]==ys[i]) goto again2; }
    }
    for(int i=0;i<n;i++) idx[i]=i; shuffle(idx,n); // bijection: point i has (xs[i], ys[idx[i]])
    // A = points 0..K-1 ; B = point 0 + points K..2K-2
    for(int i=0;i<K;i++){ ax[i]=xs[i]; ay[i]=ys[idx[i]]; }
    bx[0]=xs[0]; by[0]=ys[idx[0]]; for(int i=1;i<K;i++){ bx[i]=xs[K-1+i]; by[i]=ys[idx[K-1+i]]; }
    // patterns: sort by x, code from y-ranks
    // insertion sort pairs by x
    for(int i=1;i<K;i++){double px=ax[i],py=ay[i];int t=i-1;while(t>=0&&ax[t]>px){ax[t+1]=ax[t];ay[t+1]=ay[t];t--;}ax[t+1]=px;ay[t+1]=py;}
    for(int i=1;i<K;i++){double px=bx[i],py=by[i];int t=i-1;while(t>=0&&bx[t]>px){bx[t+1]=bx[t];by[t+1]=by[t];t--;}bx[t+1]=px;by[t+1]=py;}
    long ca=0,cb=0;
    for(int j2=0;j2<K;j2++){int r=0;for(int i=0;i<j2;i++)r+=ay[i]<ay[j2];ca=ca*(j2+1)+r;}
    for(int j2=0;j2<K;j2++){int r=0;for(int i=0;i<j2;i++)r+=by[i]<by[j2];cb=cb*(j2+1)+r;}
    hit+= ca==cb;
  }
  double p=(double)hit/S; printf("k=%d N=%ld: k!p_1 = %.4f +- %.4f\n",K,N,fact_[K]*p,fact_[K]*sqrt(p/S));
  return 0;
}
