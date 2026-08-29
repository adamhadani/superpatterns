// Random-permutation superpattern checker.
// For sigma in S_m, compute the set of n-patterns contained (bitset over n! codes).
// Code of pattern: mixed radix, code_j = code_{j-1}*j + r_j, r_j = #earlier values < current value.
// DFS over subsets with pruning: cnt[j][prefixcode] == n!/j!  => every completion already found.
// Seed with random subsets first so pruning is effective.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

static int N, M;
static int sigma[128];
static uint64_t *found; static long nfact;
static long fact[12];
static int *cnt[12];        // cnt[j] indexed by code in [0, j!)
static long nfound;
static int vals[12], codes[12];

static inline int getbit(long c){ return (found[c>>6]>>(c&63))&1; }
static inline void setbit(long c){ found[c>>6] |= 1ULL<<(c&63); }

static void record(long code){ // code is a full n-code; codes[] holds prefix codes
    if(getbit(code)) return;
    setbit(code); nfound++;
    for(int j=1;j<=N;j++) cnt[j][codes[j]]++;
}

static void dfs(int j, int last, long code){
    // j items chosen, codes[j]=code
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
    int pos[12];
    for(long t=0;t<trials && nfound<nfact;t++){
        // random n-subset of [0,M) via partial shuffle-free selection
        int c=0; 
        for(int q=0;q<M && c<N;q++){ // reservoir-like: choose q with prob (N-c)/(M-q)
            if( (rng2()%(M-q)) < (uint64_t)(N-c) ) pos[c++]=q;
        }
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

static void decode(long code,int *p){ // to 1-line notation
    int r[12]; for(int j=N;j>=1;j--){ r[j-1]=code%j; code/=j; }
    // build: p[j] rank r[j] among earlier: values are relative; construct by inserting
    // Use standard: value of item j = r[j]+1, then shift earlier items >= that value up.
    for(int j=0;j<N;j++){ int v=r[j]+1; for(int i=0;i<j;i++) if(p[i]>=v) p[i]++; p[j]=v; }
}

int main(int argc,char**argv){
    N=atoi(argv[1]); M=atoi(argv[2]); int samples=atoi(argv[3]); int hist = argc>4? atoi(argv[4]):0;
    unsigned seed = argc>5? atoi(argv[5]) : (unsigned)time(NULL); rng_s ^= (uint64_t)seed*0x9E3779B97F4A7C15ULL; rng();
    fact[0]=1; for(int j=1;j<=11;j++) fact[j]=fact[j-1]*j; nfact=fact[N];
    found=calloc((nfact+63)/64,8);
    for(int j=1;j<=N;j++) cnt[j]=calloc(fact[j],sizeof(int));
    long *miss = hist? calloc(nfact,sizeof(long)):0;
    int nsuper=0; double totmiss=0;
    for(int s=0;s<samples;s++){
        for(int i=0;i<M;i++) sigma[i]=i;
        for(int i=M-1;i>0;i--){ int j=rng()%(i+1); int t=sigma[i];sigma[i]=sigma[j];sigma[j]=t; }
        run_perm();
        if(nfound==nfact) nsuper++; if(hist<0) printf("%ld ",nfound);
        totmiss += nfact-nfound;
        if(hist) for(long c=0;c<nfact;c++) if(!getbit(c)) miss[c]++;
    }
    printf("n=%d m=%d samples=%d frac_super=%.4f mean_missing=%.3f\n",N,M,samples,(double)nsuper/samples,totmiss/samples);
    if(hist){
        { char fn[64]; sprintf(fn,"out/missall_n%d_m%d.txt",N,M); FILE*f=fopen(fn,"w"); for(long c=0;c<nfact;c++){int p[12];decode(c,p);fprintf(f,"%ld",miss[c]);for(int j=0;j<N;j++)fprintf(f," %d",p[j]);fprintf(f,"\n");} fclose(f);} 
        // print top patterns by missing count
        long *idx=malloc(nfact*sizeof(long)); for(long c=0;c<nfact;c++) idx[c]=c;
        // partial selection of top `hist`
        for(int t=0;t<hist && t<nfact;t++){ long b=t; for(long c=t;c<nfact;c++) if(miss[idx[c]]>miss[idx[b]]) b=c; long tmp=idx[t];idx[t]=idx[b];idx[b]=tmp;
            if(miss[idx[t]]==0) break;
            int p[12]; decode(idx[t],p); printf("  miss=%ld  ",miss[idx[t]]); for(int j=0;j<N;j++) printf("%d ",p[j]); printf("\n"); }
    }
    return 0;
}
