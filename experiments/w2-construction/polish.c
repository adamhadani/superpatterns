/* 1-opt then 2-opt polish for tie-broken words. usage: polish k n m dirmask word... */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int k,n,m,w[256],perm[256]; static unsigned dirmask; static unsigned char *seen; static long fact[13]; static int sel[16]; static long cnt;
static void rec(int d,int start){
  if(d==k){ long r=0; for(int i=0;i<k;i++){int c=0;for(int j=i+1;j<k;j++) if(sel[j]<sel[i]) c++; r+=c*fact[k-1-i];}
    if(!seen[r]){seen[r]=1;cnt++;} return; }
  for(int p=start;p<=n-(k-d);p++){ sel[d]=perm[p]; rec(d+1,p+1);} }
static void build(void){ int idx[256]; for(int i=0;i<n;i++) idx[i]=i;
  for(int a=1;a<n;a++){ int x=idx[a],b=a-1; while(b>=0){ int y=idx[b]; int lx=w[x],ly=w[y]; int less;
      if(lx!=ly) less=lx<ly; else { int inc=(dirmask>>(lx-1))&1; less= inc? x<y : x>y; }
      if(less){ idx[b+1]=y; b--; } else break; } idx[b+1]=x; }
  for(int r=0;r<n;r++) perm[idx[r]]=r+1; }
static long score(void){ build(); memset(seen,0,fact[k]); cnt=0; rec(0,0); return cnt; }
static void show(long s){ printf("%ld/%ld dirmask=%u :",s,fact[k],dirmask); for(int i=0;i<n;i++) printf(" %d",w[i]); printf("\n"); fflush(stdout); }
int main(int argc,char**argv){ k=atoi(argv[1]); n=atoi(argv[2]); m=atoi(argv[3]); dirmask=strtoul(argv[4],0,10);
  for(int i=0;i<n;i++) w[i]=atoi(argv[5+i]);
  fact[0]=1; for(int i=1;i<13;i++) fact[i]=fact[i-1]*i; seen=malloc(fact[k]);
  long cur=score(); show(cur);
  while(cur<fact[k]){
    long best=cur; int bp=-1,bv=0; unsigned bmask=dirmask;
    /* 1-opt: letter changes and direction flips */
    for(int p=0;p<n;p++){ int old=w[p]; for(int v=1;v<=m;v++){ if(v==old) continue; w[p]=v; long s=score(); if(s>best){best=s;bp=p;bv=v;bmask=dirmask;} } w[p]=old; }
    for(int l=0;l<m;l++){ dirmask^=1u<<l; long s=score(); if(s>best){best=s;bp=-2;bmask=dirmask;} dirmask^=1u<<l; }
    if(best>cur){ if(bp>=0) w[bp]=bv; dirmask=bmask; cur=best; show(cur); continue; }
    /* 2-opt: pairs of letter changes */
    int b1=-1,b2=-1,v1=0,v2=0;
    for(int p=0;p<n;p++){ int o1=w[p]; for(int v=1;v<=m;v++){ if(v==o1) continue; w[p]=v;
        for(int q=p+1;q<n;q++){ int o2=w[q]; for(int u=1;u<=m;u++){ if(u==o2) continue; w[q]=u; long s=score(); if(s>best){best=s;b1=p;b2=q;v1=v;v2=u;} } w[q]=o2; } }
      w[p]=o1; }
    if(best>cur){ w[b1]=v1; w[b2]=v2; cur=best; show(cur); continue; }
    printf("stuck at %ld\n",cur); break; }
  return 0; }
