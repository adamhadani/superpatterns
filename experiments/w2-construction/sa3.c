/* SA over words = concatenation of B blocks, each a permutation of [m]; dec tie-break; maximize #k-patterns.
   usage: sa3 k m B iters seed [init word of length m*B] */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int k,n,m,B,w[256],perm[256]; static unsigned char *seen; static long fact[13]; static int sel[16]; static long cnt;
static void rec(int d,int start){
  if(d==k){ long r=0; for(int i=0;i<k;i++){int c=0;for(int j=i+1;j<k;j++) if(sel[j]<sel[i]) c++; r+=c*fact[k-1-i];}
    if(!seen[r]){seen[r]=1;cnt++;} return; }
  for(int p=start;p<=n-(k-d);p++){ sel[d]=perm[p]; rec(d+1,p+1);} }
static void build(void){ int idx[256]; for(int i=0;i<n;i++) idx[i]=i;
  for(int a=1;a<n;a++){ int x=idx[a],b=a-1; while(b>=0){ int y=idx[b]; int less; if(w[x]!=w[y]) less=w[x]<w[y]; else less= x>y; if(less){ idx[b+1]=y; b--; } else break; } idx[b+1]=x; }
  for(int r=0;r<n;r++) perm[idx[r]]=r+1; }
static long score(void){ build(); memset(seen,0,fact[k]); cnt=0; rec(0,0); return cnt; }
static unsigned long long rs; static inline unsigned long long rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
int main(int argc,char**argv){ k=atoi(argv[1]); m=atoi(argv[2]); B=atoi(argv[3]); long iters=atol(argv[4]); rs=atoll(argv[5])*2654435761ULL+1; n=m*B;
  fact[0]=1; for(int i=1;i<13;i++) fact[i]=fact[i-1]*i; seen=malloc(fact[k]);
  if(argc>=6+n) for(int i=0;i<n;i++) w[i]=atoi(argv[6+i]);
  else for(int b=0;b<B;b++){ for(int i=0;i<m;i++) w[b*m+i]=i+1; for(int i=m-1;i>0;i--){ int j=rnd()%(i+1); int t=w[b*m+i]; w[b*m+i]=w[b*m+j]; w[b*m+j]=t; } }
  long cur=score(), best=cur; int bw[256]; memcpy(bw,w,sizeof(w));
  double T0=4.0, T1=0.1;
  for(long it=0;it<iters && best<fact[k];it++){
    double T=T0*pow(T1/T0,(double)it/iters);
    int b=rnd()%B, p=b*m+rnd()%m, q=b*m+rnd()%m; if(p==q) continue;
    int mv=rnd()%2; int save[256]; memcpy(save,w,sizeof(w));
    if(mv==0){ int t=w[p]; w[p]=w[q]; w[q]=t; }
    else { int t=w[p]; if(q>p){ for(int i=p;i<q;i++) w[i]=w[i+1]; } else { for(int i=p;i>q;i--) w[i]=w[i-1]; } w[q]=t; }
    long s=score();
    if(s>=cur || exp((s-cur)/T)*4294967296.0 > (double)(rnd()&0xffffffff)){ cur=s; if(s>best){best=s; memcpy(bw,w,sizeof(w)); fprintf(stderr,"it %ld best %ld/%ld\n",it,best,fact[k]);} }
    else memcpy(w,save,sizeof(w));
  }
  printf("%ld/%ld :",best,fact[k]); for(int i=0;i<n;i++) printf(" %d",bw[i]); printf("\n"); return 0; }
