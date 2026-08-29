// brute-force cross-check: count distinct n-patterns in random sigma in S_m, unpruned, print nfound; same RNG/perm generation as sp.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static int N,M,sigma[128]; static uint64_t *found; static long fact[12],nfound; static int vals[12];
static void dfs(int j,int last,long code){ if(j==N){ if(!((found[code>>6]>>(code&63))&1)){found[code>>6]|=1ULL<<(code&63);nfound++;} return;}
 for(int q=last+1;q<=M-(N-j);q++){int v=sigma[q],r=0;for(int i=0;i<j;i++)r+=vals[i]<v;vals[j]=v;dfs(j+1,q,code*(j+1)+r);} }
static uint64_t rng_s=88172645463325252ULL; static inline uint64_t rng(){ rng_s^=rng_s<<7; rng_s^=rng_s>>9; return rng_s; }
int main(int argc,char**argv){N=atoi(argv[1]);M=atoi(argv[2]);int samples=atoi(argv[3]);unsigned seed=atoi(argv[5]);rng_s^=(uint64_t)seed*0x9E3779B97F4A7C15ULL;rng();
 fact[0]=1;for(int j=1;j<=11;j++)fact[j]=fact[j-1]*j; found=calloc((fact[N]+63)/64,8);
 for(int s=0;s<samples;s++){ for(int i=0;i<M;i++)sigma[i]=i; for(int i=M-1;i>0;i--){int j=rng()%(i+1);int t=sigma[i];sigma[i]=sigma[j];sigma[j]=t;}
  memset(found,0,((fact[N]+63)/64)*8);nfound=0;dfs(0,-1,0);printf("%ld ",nfound);} printf("\n");}
