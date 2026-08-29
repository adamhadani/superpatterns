// lis n samples seed k1 k2 ... : fraction of uniform random sigma_n with LIS >= k (same RNG/sample stream as contain_bc)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static uint64_t rng_s[2];
static inline uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static uint64_t rnd(void){uint64_t s0=rng_s[0],s1=rng_s[1],r=s0+s1;s1^=s0;rng_s[0]=rotl(s0,55)^s1^(s1<<14);rng_s[1]=rotl(s1,36);return r;}
int main(int argc,char**argv){
    int n=atoi(argv[1]); int samples=atoi(argv[2]); uint64_t seed=atoll(argv[3]);
    rng_s[0]=seed*0x9E3779B97F4A7C15ULL+1; rng_s[1]=seed^0xD1B54A32D192ED03ULL; for(int i=0;i<20;i++)rnd();
    int nk=argc-4; long *hits=calloc(nk,sizeof(long)); int *sig=malloc(n*sizeof(int)),*tail=malloc((n+1)*sizeof(int));
    for(int t=0;t<samples;t++){
        for(int i=0;i<n;i++)sig[i]=i;
        for(int i=n-1;i>0;i--){int j=rnd()%(i+1);int tmp=sig[i];sig[i]=sig[j];sig[j]=tmp;}
        int L=0;
        for(int i=0;i<n;i++){int lo=0,hi=L; while(lo<hi){int m=(lo+hi)>>1; if(tail[m]<sig[i]) lo=m+1; else hi=m;} tail[lo]=sig[i]; if(lo==L) L++;}
        printf("%d\n",L>=atoi(argv[4]));
    }
    
    return 0;
}
