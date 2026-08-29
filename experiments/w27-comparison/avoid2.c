// W27 avoid2: same as avoid.c but the "does inserting the max create a copy" test uses the validated contain_bc
// solver (bc_core.h = lines 18-129 of ../w21-threshold-numerics/contain_bc.c) on the full sequence.
// usage: avoid2 exact pattern nmax | avoid2 smc pattern nmax pop seed
#include <math.h>
#include "bc_core.h"
#define MAXM 128
static int K;
static void build_base(int*s,int m){ // table for s (length m) with columns v=0..m+1
    N1=m+2; memcpy(sig,s,m*sizeof(int));
    for(int i=0;i<=m;i++){ for(int v=0;v<=m+1;v++) cnt[i*N1+v]= (i==0)?0: cnt[(i-1)*N1+v]+(sig[i-1]<v); }
}
static int tmp[MAXM];
static int bad_insert(int*s,int m,int p){ // s avoider of length m; insert value m at position p
    if(m<k-1) return 0;
    for(int i=0;i<p;i++)sig[i]=s[i]; sig[p]=m; for(int i=p;i<m;i++)sig[i+1]=s[i];
    n=m+1; insp=p; insm=m; for(int e=0;e<k;e++) pos[e]=-1;
    int r=dfs(0); insp=-1; return r;
}
static double cntn[MAXM]; static int cur[MAXM];
static void rec(int m,int nmax){
    cntn[m]+=1; if(m==nmax) return;
    for(int p=0;p<=m;p++){
        build_base(cur,m); if(!bad_insert(cur,m,p)){
            for(int i=m;i>p;i--) cur[i]=cur[i-1]; cur[p]=m;
            rec(m+1,nmax);
            for(int i=p;i<m;i++) cur[i]=cur[i+1];
        }
    }
}
static uint64_t rs=88172645463325252ULL; static inline uint64_t xr(){ rs^=rs<<7; rs^=rs>>9; return rs; }
int main(int argc,char**argv){
    if(argc<4){fprintf(stderr,"usage\n");return 1;}
    k=parse(argv[2],pi); K=k; for(int e=0;e<k;e++) pinv[pi[e]]=e;
    int nmax=atoi(argv[3]); cnt=malloc(sizeof(int)*(MAXM+2)*(MAXM+2));
    if(!strcmp(argv[1],"exact")){
        rec(0,nmax);
        for(int m=1;m<=nmax;m++) printf("%d %.0f %.6e\n",m,cntn[m],cntn[m]/exp(lgamma(m+1.0)));
        return 0;
    }
    int pop=atoi(argv[4]); rs^=atoll(argv[5])*0x9E3779B97F4A7C15ULL; for(int i=0;i<20;i++)xr();
    int *A=malloc((size_t)pop*MAXM*sizeof(int)), *B=malloc((size_t)pop*MAXM*sizeof(int));
    int *nc=malloc(pop*sizeof(int)); unsigned char *ok=malloc((size_t)pop*MAXM);
    double logp=0;
    for(int m=0;m<nmax;m++){
        double tot=0;
        for(int s=0;s<pop;s++){ int c=0; build_base(A+(size_t)s*MAXM,m);
            for(int p=0;p<=m;p++){ int b=bad_insert(A+(size_t)s*MAXM,m,p); ok[(size_t)s*MAXM+p]=!b; c+=!b; }
            nc[s]=c; tot+=c; }
        if(tot==0){ printf("%d 0 -inf\n",m+1); return 0; }
        logp += log(tot/pop) - log(m+1.0);
        double u=(xr()>>11)*(1.0/9007199254740992.0)*tot/pop, acc=0; int s=0;
        for(int t=0;t<pop;t++){
            while(acc+nc[s] < u) { acc+=nc[s]; s++; }
            int r=xr()%nc[s], p=0; for(p=0;p<=m;p++){ if(ok[(size_t)s*MAXM+p]){ if(r==0)break; r--; } }
            int *src=A+(size_t)s*MAXM,*dst=B+(size_t)t*MAXM;
            for(int i=0;i<p;i++)dst[i]=src[i]; dst[p]=m; for(int i=p;i<m;i++)dst[i+1]=src[i];
            u+=tot/pop;
        }
        int*T=A;A=B;B=T;
        printf("%d %.6e %.6f\n",m+1,exp(logp),logp); fflush(stdout);
    }
    return 0;
}
