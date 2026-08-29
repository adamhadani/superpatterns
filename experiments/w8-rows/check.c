/* k-superpattern checker for words over [m] (permutations are a special case).
   Usage: check k n w1 w2 ... wn   -> prints count of k-patterns contained and total k!
   Enumerates all k-subsets of positions with distinct letters (pruned), computes pattern rank. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int k,n,w[200];
static unsigned char *seen; static long fact[13];
static int sel[16]; static long cnt=0;
static void rec(int d,int start){
  if(d==k){ /* rank pattern of sel */
    long r=0; for(int i=0;i<k;i++){int c=0;for(int j=i+1;j<k;j++) if(sel[j]<sel[i]) c++; r+=c*fact[k-1-i];}
    if(!seen[r]){seen[r]=1;cnt++;} return; }
  for(int p=start;p<=n-(k-d);p++){ int v=w[p],ok=1; for(int j=0;j<d;j++) if(sel[j]==v){ok=0;break;}
    if(!ok) continue; sel[d]=v; rec(d+1,p+1);} }
int main(int argc,char**argv){ k=atoi(argv[1]); n=atoi(argv[2]); for(int i=0;i<n;i++) w[i]=atoi(argv[3+i]);
  fact[0]=1; for(int i=1;i<13;i++) fact[i]=fact[i-1]*i; seen=calloc(fact[k],1); rec(0,0);
  printf("%ld %ld\n",cnt,fact[k]); return 0;}
