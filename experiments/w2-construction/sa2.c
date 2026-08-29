/* SA over words in [m]^n with per-letter tie-break direction; score = #k-patterns of tie-broken permutation.
   usage: sa2 k n m iters seed [dirmask] [init word...]   dirmask bit l-1 = 1 -> letter l increasing ties */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int k,n,m,w[256],perm[256]; static unsigned dirmask; static unsigned char *seen; static long fact[13]; static int sel[16]; static long cnt;
static void rec(int d,int start){
  if(d==k){ long r=0; for(int i=0;i<k;i++){int c=0;for(int j=i+1;j<k;j++) if(sel[j]<sel[i]) c++; r+=c*fact[k-1-i];}
    if(!seen[r]){seen[r]=1;cnt++;} return; }
  for(int p=start;p<=n-(k-d);p++){ sel[d]=perm[p]; rec(d+1,p+1);} }
static void build(void){ /* perm: value = rank by (letter, position with direction) */
  int idx[256]; for(int i=0;i<n;i++) idx[i]=i;
  /* sort indices by letter then by position asc if inc else desc */
  for(int a=1;a<n;a++){ int x=idx[a],b=a-1; while(b>=0){ int y=idx[b]; int lx=w[x],ly=w[y]; int less;
      if(lx!=ly) less=lx<ly; else { int inc=(dirmask>>(lx-1))&1; less= inc? x<y : x>y; }
      if(less){ idx[b+1]=y; b--; } else break; } idx[b+1]=x; }
  for(int r=0;r<n;r++) perm[idx[r]]=r+1; }
static long score(void){ build(); memset(seen,0,fact[k]); cnt=0; rec(0,0); return cnt; }
static unsigned long long rs; static inline unsigned long long rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
int main(int argc,char**argv){ k=atoi(argv[1]); n=atoi(argv[2]); m=atoi(argv[3]); long iters=atol(argv[4]); rs=atoll(argv[5])*2654435761ULL+1;
  fact[0]=1; for(int i=1;i<13;i++) fact[i]=fact[i-1]*i; seen=malloc(fact[k]); dirmask=0;
  if(argc>6) dirmask=strtoul(argv[6],0,10);
  if(argc>=7+n) for(int i=0;i<n;i++) w[i]=atoi(argv[7+i]); else for(int i=0;i<n;i++) w[i]=1+rnd()%m;
  long cur=score(), best=cur; int bw[256]; unsigned bd=dirmask; memcpy(bw,w,sizeof(w));
  double T0=3.0, T1=0.05;
  for(long it=0;it<iters && best<fact[k];it++){
    double T=T0*pow(T1/T0,(double)it/iters);
    int p=rnd()%n, old=w[p], q=-1, oldq=0; unsigned oldmask=dirmask;
    int mv=rnd()%4;
    if(mv==0){ w[p]=1+rnd()%m; if(w[p]==old) continue; }
    else if(mv==1){ q=rnd()%n; if(q==p) continue; oldq=w[q]; w[p]=oldq; w[q]=old; if(old==oldq) continue; }
    else if(mv==2){ q=rnd()%n; if(q==p) continue; int tmp=w[p];
      if(q>p){ for(int i=p;i<q;i++) w[i]=w[i+1]; } else { for(int i=p;i>q;i--) w[i]=w[i-1]; } w[q]=tmp; }
    else { dirmask ^= 1u<<(rnd()%m); }
    long s=score();
    if(s>=cur || exp((s-cur)/T)*4294967296.0 > (double)(rnd()&0xffffffff)){ cur=s; if(s>best){best=s; bd=dirmask; memcpy(bw,w,sizeof(w));
        fprintf(stderr,"it %ld best %ld/%ld\n",it,best,fact[k]);} }
    else { if(mv==0) w[p]=old; else if(mv==1){ w[p]=old; w[q]=oldq; } else if(mv==2){ int tmp=w[q]; if(q>p){ for(int i=q;i>p;i--) w[i]=w[i-1]; } else { for(int i=q;i<p;i++) w[i]=w[i+1]; } w[p]=tmp; } else dirmask=oldmask; }
  }
  printf("%ld/%ld dirmask=%u :",best,fact[k],bd); for(int i=0;i<n;i++) printf(" %d",bw[i]); printf("\n"); return 0; }
