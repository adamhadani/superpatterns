// W27: exact avoider counts (generating tree) and SMC growth estimator for Pr(pi not contained in sigma_n).
// usage: avoid exact pattern nmax            -> prints n, A_n(pi), Pr(avoid)
//        avoid smc   pattern nmax pop seed   -> prints n, estimated Pr(avoid), log Pr
// pattern given as digits string e.g. 1324 (k<=9) ; values 1..k
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#define MAXN 128
#define MAXK 9
static int K, P[MAXK];           // pattern, 0-based values
static int jmax;                 // index of K-1 (max) in pattern
static int below[MAXK], above[MAXK]; // for pattern index j: index with next smaller/larger value (-1 none)
static int seq[MAXN];            // current sequence
static int M;                    // length of seq
static int posp;                 // position of the max in seq
static int asg[MAXK];            // assigned positions
// DFS: assign pattern index j (in position order) to position >= start
static int dfs(int j,int start){
    if(j==K) return 1;
    if(j==jmax){ // must be posp
        if(start>posp) return 0;
        // check value consistency: max is largest, automatically ok vs assigned (all assigned have smaller pattern values... not nec.)
        // assigned indices < j have pattern values < K-1 so must have seq values < seq[posp]=max: true.
        asg[j]=posp; return dfs(j+1,posp+1);
    }
    int last = M-(K-j); // last feasible start
    if(j<jmax && posp-1 < last) last = posp-1;
    int lo=-1, hi=M; // value bounds from assigned neighbours in value order
    for(int t=below[j]; t>=0; t=below[t]) if(t<j){ lo=seq[asg[t]]; break; }
    for(int t=above[j]; t>=0; t=above[t]) if(t<j){ hi=seq[asg[t]]; break; }
    int s = start; if(j>jmax && s<=posp) s=posp+1;
    for(int i=s;i<=last;i++){
        int v=seq[i]; if(v>lo && v<hi){ asg[j]=i; if(dfs(j+1,i+1)) return 1; }
    }
    return 0;
}
static int bad_insert(int m,int p){ // seq[0..m-1] is an avoider; insert max at position p; does it create a copy?
    // build seq of length m+1 with value m at position p
    for(int i=m;i>p;i--) seq[i]=seq[i-1];
    seq[p]=m; M=m+1; posp=p;
    int r=dfs(0,0);
    for(int i=p;i<m;i++) seq[i]=seq[i+1]; // restore
    return r;
}
static void setup(const char*s){
    K=strlen(s); for(int j=0;j<K;j++){P[j]=s[j]-'1'; if(P[j]==K-1) jmax=j;}
    for(int j=0;j<K;j++){ below[j]=-1; above[j]=-1;
        for(int t=0;t<K;t++){ if(P[t]==P[j]-1) below[j]=t; if(P[t]==P[j]+1) above[j]=t; } }
}
// exact enumeration
static double cnt[MAXN];
static int cur[MAXN];
static void rec(int m,int nmax){
    cnt[m]+=1; if(m==nmax) return;
    for(int p=0;p<=m;p++){
        memcpy(seq,cur,m*sizeof(int));
        if(!bad_insert(m,p)){
            // new cur
            for(int i=m;i>p;i--) cur[i]=cur[i-1]; cur[p]=m;
            rec(m+1,nmax);
            for(int i=p;i<m;i++) cur[i]=cur[i+1];
        }
    }
}
static uint64_t rs=88172645463325252ULL; static inline uint64_t rnd(){ rs^=rs<<7; rs^=rs>>9; return rs; }
static double lfact(int n){ return lgamma(n+1.0); }
int main(int argc,char**argv){
    if(argc<4){fprintf(stderr,"usage\n");return 1;}
    setup(argv[2]); int nmax=atoi(argv[3]);
    if(!strcmp(argv[1],"exact")){
        rec(0,nmax);
        for(int n=1;n<=nmax;n++) printf("%d %.0f %.6e\n",n,cnt[n],cnt[n]/exp(lfact(n)));
        return 0;
    }
    if(!strcmp(argv[1],"smc")){
        int pop=atoi(argv[4]); rs^=atoll(argv[5])*0x9E3779B97F4A7C15ULL; for(int i=0;i<20;i++)rnd();
        int *A=malloc((size_t)pop*MAXN*sizeof(int)), *B=malloc((size_t)pop*MAXN*sizeof(int));
        int *nc=malloc(pop*sizeof(int)); unsigned char *ok=malloc((size_t)pop*MAXN);
        double logp=0; // log Pr(avoid) at current m
        int m=0; // all population = empty
        for(int m=0;m<nmax;m++){
            double tot=0;
            for(int s=0;s<pop;s++){
                memcpy(seq,A+(size_t)s*MAXN,m*sizeof(int)); int c=0;
                for(int p=0;p<=m;p++){ int b= (m<K-1)?0:bad_insert(m,p); ok[(size_t)s*MAXN+p]=!b; c+=!b; }
                nc[s]=c; tot+=c;
            }
            logp += log(tot/pop) - log(m+1.0);
            // resample children proportional to nc (systematic)
            double u=(rnd()>>11)*(1.0/9007199254740992.0)*tot/pop, acc=0; int s=0;
            for(int t=0;t<pop;t++){
                while(acc+nc[s] < u) { acc+=nc[s]; s++; }
                // pick a random ok slot of parent s
                int r=rnd()%nc[s], p=0; for(p=0;p<=m;p++){ if(ok[(size_t)s*MAXN+p]){ if(r==0)break; r--; } }
                int *src=A+(size_t)s*MAXN,*dst=B+(size_t)t*MAXN;
                for(int i=0;i<p;i++)dst[i]=src[i]; dst[p]=m; for(int i=p;i<m;i++)dst[i+1]=src[i];
                u+=tot/pop;
            }
            int*T=A;A=B;B=T;
            printf("%d %.6e %.6f\n",m+1,exp(logp),logp); fflush(stdout);
        }
        return 0;
    }
    return 1;
}
