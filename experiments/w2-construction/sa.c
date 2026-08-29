/* Simulated annealing over words sigma in [m]^n maximizing #distinct k-patterns contained.
   usage: sa k n m iters seed [init word...] */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int k,n,m,w[256]; static unsigned char *seen; static long fact[13]; static int sel[16]; static long cnt;
static void rec(int d,int start){
  if(d==k){ long r=0; for(int i=0;i<k;i++){int c=0;for(int j=i+1;j<k;j++) if(sel[j]<sel[i]) c++; r+=c*fact[k-1-i];}
    if(!seen[r]){seen[r]=1;cnt++;} return; }
  for(int p=start;p<=n-(k-d);p++){ int v=w[p],ok=1; for(int j=0;j<d;j++) if(sel[j]==v){ok=0;break;}
    if(!ok) continue; sel[d]=v; rec(d+1,p+1);} }
static long score(void){ memset(seen,0,fact[k]); cnt=0; rec(0,0); return cnt; }
static unsigned long long rs; static inline unsigned long long rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
int main(int argc,char**argv){ k=atoi(argv[1]); n=atoi(argv[2]); m=atoi(argv[3]); long iters=atol(argv[4]); rs=atoll(argv[5])*2654435761ULL+1;
  fact[0]=1; for(int i=1;i<13;i++) fact[i]=fact[i-1]*i; seen=malloc(fact[k]);
  if(argc>6+n-1) for(int i=0;i<n;i++) w[i]=atoi(argv[6+i]); else for(int i=0;i<n;i++) w[i]=1+rnd()%m;
  long cur=score(), best=cur; int bw[256]; memcpy(bw,w,sizeof(w));
  double T0=3.0, T1=0.05;
  for(long it=0;it<iters && best<fact[k];it++){
    double T=T0*pow(T1/T0,(double)it/iters);
    int p=rnd()%n, old=w[p], q=-1, oldq=0;
    int mv=rnd()%3;
    if(mv==0){ w[p]=1+rnd()%m; if(w[p]==old) continue; }
    else if(mv==1){ q=rnd()%n; if(q==p) continue; oldq=w[q]; w[p]=oldq; w[q]=old; if(old==oldq) continue; }
    else { /* shift a segment: remove position p, insert at q */ q=rnd()%n; if(q==p) continue; int tmp=w[p];
      if(q>p){ for(int i=p;i<q;i++) w[i]=w[i+1]; } else { for(int i=p;i>q;i--) w[i]=w[i-1]; } w[q]=tmp; }
    long s=score();
    if(s>=cur || exp((s-cur)/T)*4294967296.0 > (double)(rnd()&0xffffffff)){ cur=s; if(s>best){best=s; memcpy(bw,w,sizeof(w));
        fprintf(stderr,"it %ld best %ld/%ld\n",it,best,fact[k]);} }
    else { if(mv==0) w[p]=old; else if(mv==1){ w[p]=old; w[q]=oldq; } else { int tmp=w[q]; if(q>p){ for(int i=q;i>p;i--) w[i]=w[i-1]; } else { for(int i=q;i<p;i++) w[i]=w[i+1]; } w[p]=tmp; } }
  }
  printf("%ld/%ld :",best,fact[k]); for(int i=0;i<n;i++) printf(" %d",bw[i]); printf("\n"); return 0; }
