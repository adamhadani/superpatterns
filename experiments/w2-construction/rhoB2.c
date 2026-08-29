/* exhaustive: all rho in S_m, sigma = rho^B, count k-patterns; print best. usage: rhoB k m B */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int k,n,m,B,w[256],perm[256];
static void build(void){ int idx[256]; for(int i=0;i<n;i++) idx[i]=i;
  for(int a=1;a<n;a++){ int x=idx[a],b=a-1; while(b>=0){ int y=idx[b]; int less; if(w[x]!=w[y]) less=w[x]<w[y]; else less= x>y; if(less){ idx[b+1]=y; b--; } else break; } idx[b+1]=x; }
  for(int r=0;r<n;r++) perm[idx[r]]=r+1; } static unsigned char *seen; static long fact[13]; static int sel[16]; static long cnt;
static void rec(int d,int start){
  if(d==k){ long r=0; for(int i=0;i<k;i++){int c=0;for(int j=i+1;j<k;j++) if(sel[j]<sel[i]) c++; r+=c*fact[k-1-i];}
    if(!seen[r]){seen[r]=1;cnt++;} return; }
  for(int p=start;p<=n-(k-d);p++){ int v=perm[p],ok=1;
    if(!ok) continue; sel[d]=v; rec(d+1,p+1);} }
static long score(void){ memset(seen,0,fact[k]); cnt=0; rec(0,0); return cnt; }
int main(int argc,char**argv){ k=atoi(argv[1]); m=atoi(argv[2]); B=atoi(argv[3]); n=m*B;
  fact[0]=1; for(int i=1;i<13;i++) fact[i]=fact[i-1]*i; seen=malloc(fact[k]);
  int rho[16]; for(int i=0;i<m;i++) rho[i]=i+1; long best=0; long total=0;
  /* iterate permutations with rho[0] < m+1-rho[0]... use full enumeration but skip reverse-complement duplicates: require rho[0] <= (m+1)/2 */
  while(1){
    if(rho[0]<=(m+1)/2){ for(int b=0;b<B;b++) for(int i=0;i<m;i++) w[b*m+i]=rho[i]; build();
      long s=score(); total++;
      if(s>=best){ best=s; printf("%ld/%ld :",s,fact[k]); for(int i=0;i<m;i++) printf(" %d",rho[i]); printf("\n"); fflush(stdout);} }
    /* next permutation */
    int i=m-2; while(i>=0 && rho[i]>rho[i+1]) i--; if(i<0) break;
    int j=m-1; while(rho[j]<rho[i]) j--; int t=rho[i]; rho[i]=rho[j]; rho[j]=t;
    for(int a=i+1,b=m-1;a<b;a++,b--){ t=rho[a]; rho[a]=rho[b]; rho[b]=t; }
  }
  fprintf(stderr,"done %ld perms, best %ld\n",total,best); return 0; }
