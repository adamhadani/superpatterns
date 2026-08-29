// W24: missing-pattern counter for random permutations.
// For each random sigma in S_n, compute M = #{pi in S_k : pi not contained in sigma}
// and dump M followed by the codes of the missing patterns (if M <= DUMPMAX).
// Algorithm = w5-random/sp.c (bitset over k! mixed-radix codes; DFS over k-subsets with
// prefix-completion pruning; random seeding first).
// Usage: mslack K N SAMPLES SEED [DUMPMAX]   -> stdout: one line per sample "M c1 c2 ...", then a summary line.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

static int N, M;               // N = k (pattern length), M = n (permutation length) -- keep w5 names
static int sigma[256];
static uint64_t *found; static long nfact;
static long fact[13];
static int *cnt[13];
static long nfound;
static int vals[13], codes[13];

static inline int getbit(long c){ return (found[c>>6]>>(c&63))&1; }
static inline void setbit(long c){ found[c>>6] |= 1ULL<<(c&63); }

static void record(long code){
    if(getbit(code)) return;
    setbit(code); nfound++;
    for(int j=1;j<=N;j++) cnt[j][codes[j]]++;
}

static void dfs(int j, int last, long code){
    if(j==N){ record(code); return; }
    for(int q=last+1; q<=M-(N-j); q++){
        int v=sigma[q], r=0;
        for(int i=0;i<j;i++) r+= vals[i]<v;
        long nc=code*(j+1)+r;
        if(cnt[j+1][nc]==fact[N]/fact[j+1]) continue;
        vals[j]=v; codes[j+1]=nc;
        dfs(j+1,q,nc);
        if(nfound==nfact) return;
    }
}

static uint64_t rng_s=88172645463325252ULL;
static inline uint64_t rng(){ rng_s^=rng_s<<7; rng_s^=rng_s>>9; return rng_s; }
static uint64_t rng2_s=0x1234567887654321ULL;
static inline uint64_t rng2(){ rng2_s^=rng2_s<<7; rng2_s^=rng2_s>>9; return rng2_s; }
static void seed_random(long trials){
    int pos[13];
    for(long t=0;t<trials && nfound<nfact;t++){
        int c=0;
        for(int q=0;q<M && c<N;q++){ if( (rng2()%(M-q)) < (uint64_t)(N-c) ) pos[c++]=q; }
        long code=0;
        for(int j=0;j<N;j++){ int v=sigma[pos[j]], r=0; for(int i=0;i<j;i++) r+= vals[i]<v; vals[j]=v; code=code*(j+1)+r; codes[j+1]=code; }
        record(code);
    }
}

static void run_perm(){
    memset(found,0,((nfact+63)/64)*8);
    for(int j=1;j<=N;j++) memset(cnt[j],0,fact[j]*sizeof(int));
    nfound=0; codes[0]=0;
    seed_random( (long)M*M*200 );
    if(nfound<nfact) dfs(0,-1,0);
}

int main_orig(int argc,char**argv){
    if(argc<5){ fprintf(stderr,"usage: mslack K N SAMPLES SEED [DUMPMAX]\n"); return 1; }
    N=atoi(argv[1]); M=atoi(argv[2]); int samples=atoi(argv[3]);
    unsigned seed=(unsigned)atoi(argv[4]); long dumpmax = argc>5? atol(argv[5]) : 100000;
    rng_s ^= (uint64_t)seed*0x9E3779B97F4A7C15ULL; rng(); rng2_s ^= (uint64_t)seed*0xD1B54A32D192ED03ULL; rng2();
    fact[0]=1; for(int j=1;j<=12;j++) fact[j]=fact[j-1]*j; nfact=fact[N];
    found=calloc((nfact+63)/64,8);
    for(int j=1;j<=N;j++) cnt[j]=calloc(fact[j],sizeof(int));
    long nsuper=0; double totmiss=0; clock_t t0=clock();
    for(int s=0;s<samples;s++){
        for(int i=0;i<M;i++) sigma[i]=i;
        for(int i=M-1;i>0;i--){ int j=rng()%(i+1); int t=sigma[i];sigma[i]=sigma[j];sigma[j]=t; }
        run_perm();
        long miss=nfact-nfound; if(miss==0) nsuper++; totmiss+=miss;
        printf("%ld",miss);
        if(miss>0 && miss<=dumpmax) for(long c=0;c<nfact;c++) if(!getbit(c)) printf(" %ld",c);
        printf("\n");
        if((s+1)%50==0) fflush(stdout);
    }
    double secs=(double)(clock()-t0)/CLOCKS_PER_SEC;
    printf("# k=%d n=%d samples=%d seed=%u frac_super=%.5f mean_missing=%.4f secs=%.1f\n",N,M,samples,seed,(double)nsuper/samples,totmiss/samples,secs);
    return 0;
}
int main(int argc,char**argv){
    N=atoi(argv[1]); fact[0]=1; for(int j=1;j<=12;j++) fact[j]=fact[j-1]*j; nfact=fact[N];
    M=0; int x; while(scanf("%d",&x)==1) sigma[M++]=x;
    found=calloc((nfact+63)/64,8); for(int j=1;j<=N;j++) cnt[j]=calloc(fact[j],sizeof(int));
    run_perm(); long miss=nfact-nfound; printf("%ld",miss);
    for(long c=0;c<nfact;c++) if(!getbit(c)) printf(" %ld",c);
    printf("\n"); return 0;
}
