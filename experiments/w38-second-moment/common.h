// W38 common: RNG, factorials, pattern codes.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
static uint64_t rs[4];
static inline uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static uint64_t rng(void){ // xoshiro256**
  uint64_t r=rotl(rs[1]*5,7)*9, t=rs[1]<<17;
  rs[2]^=rs[0]; rs[3]^=rs[1]; rs[1]^=rs[2]; rs[0]^=rs[3]; rs[2]^=t; rs[3]=rotl(rs[3],45); return r;}
static void seed_rng(uint64_t s){ for(int i=0;i<4;i++){ s+=0x9e3779b97f4a7c15ULL; uint64_t z=s; z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL; z=(z^(z>>27))*0x94d049bb133111ebULL; rs[i]=z^(z>>31);} }
static inline int rnd(int n){ return (int)(rng()%(uint64_t)n); }
static void shuffle(int *a,int n){ for(int i=n-1;i>0;i--){int j=rnd(i+1);int t=a[i];a[i]=a[j];a[j]=t;} }
static void isort(int *a,int n){ for(int i=1;i<n;i++){int v=a[i],j=i-1;while(j>=0&&a[j]>v){a[j+1]=a[j];j--;}a[j+1]=v;} }
static long fact_[14];
static void init_fact(void){ fact_[0]=1; for(int i=1;i<14;i++) fact_[i]=fact_[i-1]*i; }
// mixed-radix code of the pattern of values v[0..k-1] (in position order): code = sum over j of (#i<j with v[i]<v[j]) in radix j+1
static long pat_code(const int *v,int k){ long c=0; for(int j=0;j<k;j++){int r=0;for(int i=0;i<j;i++) r+=v[i]<v[j]; c=c*(j+1)+r;} return c; }
static double lbinom(int n,int k){ return lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1); }
