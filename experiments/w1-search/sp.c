// Superpattern search: universality checker + simulated annealing.
// Usage: sp -n N -k K [-s seed] [-i iters] [-T temp] [-S sym] [-p "perm"] [-c]
//   -c : just check the given perm (-p) and print #missing k-patterns
//   -S : symmetry 0=none, 1=reverse-complement fixed, 2=inverse fixed (involution)
// Permutations given/printed 1-based, space separated.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
#include <unistd.h>

static int n, k; static long RH=3000000; static double ALPHA=0.999;
static int sig[64], pos[64];
static uint32_t cnt[40320]; static double W[40320]; static double E; static double PBIG=0.1; static long STUCK=20000; static double WINC=1.0;
static int fact[10];
static long missing, singles; static double LAM=0.3;

static inline int pc(uint64_t x){ return __builtin_popcountll(x); }

static void dfs_full(int p0, int m, uint64_t mask, int code){
    if(m==k){ cnt[code]++; return; }
    int lim = n-(k-m);
    for(int p=p0;p<=lim;p++){
        int v=sig[p];
        int r=pc(mask & ((1ULL<<v)-1));
        dfs_full(p+1,m+1,mask|(1ULL<<v),code+r*fact[m]);
    }
}
static void full_count(void){
    memset(cnt,0,sizeof(uint32_t)*fact[k]);
    dfs_full(0,0,0,0);
    missing=0; singles=0; E=0;
    for(int i=0;i<fact[k];i++){ if(!cnt[i]){ missing++; E+=W[i]; } else if(cnt[i]==1) singles++; }
}

// pair swap of positions a<b: enumerate subsets containing both; cnt[old]--, cnt[new]++.
static int PA,PB;
static void dfs_pair(int p0,int m,uint64_t mask,uint64_t mask2,int c1,int c2){
    if(m==k){
        if(c1!=c2){
            { uint32_t c=--cnt[c1]; if(c==0){missing++;singles--;E+=W[c1];} else if(c==1) singles++; }
            { uint32_t c=cnt[c2]++; if(c==0){missing--;singles++;E-=W[c2];} else if(c==1) singles--; }
        }
        return;
    }
    int forced=(p0<=PA)+(p0<=PB);
    if(k-m<forced) return;
    int lim=n-(k-m);
    int start=p0;
    if(k-m==forced) start=(p0<=PA)?PA:PB;
    for(int p=start;p<=lim;p++){
        int v=sig[p];
        int v2 = (p==PA)? sig[PB] : (p==PB)? sig[PA] : v;
        int r=pc(mask&((1ULL<<v)-1));
        int r2=pc(mask2&((1ULL<<v2)-1));
        dfs_pair(p+1,m+1,mask|(1ULL<<v),mask2|(1ULL<<v2),c1+r*fact[m],c2+r2*fact[m]);
        if(p==PA||p==PB) break;
    }
}
static void swap_pos(int a,int b){
    if(a==b) return;
    if(a>b){int t=a;a=b;b=t;}
    PA=a;PB=b;
    dfs_pair(0,0,0,0,0,0);
    int t=sig[a]; sig[a]=sig[b]; sig[b]=t;
    pos[sig[a]]=a; pos[sig[b]]=b;
}

static uint64_t rng_s[2];
static inline uint64_t rnd(void){
    uint64_t s1=rng_s[0], s0=rng_s[1];
    rng_s[0]=s0; s1^=s1<<23; rng_s[1]=s1^s0^(s1>>17)^(s0>>26);
    return rng_s[1]+s0;
}
static inline double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }

static void print_perm(FILE*f){
    for(int i=0;i<n;i++) fprintf(f,"%d ",sig[i]+1);
    fprintf(f,"\n");
}

// composite move: list of pair swaps
static int mv[4][2], nmv;
static void gen_move(int sym){
    nmv=0;
    int type=rnd()&1;
    if(sym==0){
        if(type==0){ int i=rnd()%(n-1); mv[0][0]=i; mv[0][1]=i+1; nmv=1; }
        else { int v=rnd()%(n-1); mv[0][0]=pos[v]; mv[0][1]=pos[v+1]; nmv=1; }
    } else if(sym==1){ // reverse-complement: sig[n-1-i]=n-1-sig[i]
        if(type==0){
            int i=rnd()%(n-1); int j=n-2-i;
            mv[0][0]=i; mv[0][1]=i+1; nmv=1;
            if(j!=i){ mv[1][0]=j; mv[1][1]=j+1; nmv=2; }
        } else {
            int v=rnd()%(n-1); int w=n-2-v;
            mv[0][0]=pos[v]; mv[0][1]=pos[v+1]; nmv=1;
            if(w!=v){ mv[1][0]=pos[w]; mv[1][1]=pos[w+1]; nmv=2; }
        }
    } else { // involution: conjugate by (i i+1): swap positions i,i+1 then values i,i+1
        int i=rnd()%(n-1);
        mv[0][0]=i; mv[0][1]=i+1; nmv=1;
        mv[1][0]=-1; mv[1][1]=i; nmv=2; // marker: value swap computed after first
    }
}
static void apply_moves(void){
    for(int t=0;t<nmv;t++){
        if(mv[t][0]==-1){ int v=mv[t][1]; int a=pos[v],b=pos[v+1]; mv[t][0]=a; mv[t][1]=b; swap_pos(a,b); }
        else swap_pos(mv[t][0],mv[t][1]);
    }
}
static void undo_moves(void){
    for(int t=nmv-1;t>=0;t--) swap_pos(mv[t][0],mv[t][1]);
}

static void make_symmetric(int sym){
    if(sym==1){ for(int i=0;i<n/2;i++){ int v=sig[i]; // set mirror
            int w=n-1-v; int j=n-1-i; // put w at position j: swap pos[w] and j
            int a=pos[w]; int t=sig[a]; sig[a]=sig[j]; sig[j]=t; pos[sig[a]]=a; pos[sig[j]]=j; }
        if(n%2==1){ /* middle must be fixed value (n-1)/2 */ int i=n/2; int a=pos[(n-1)/2]; int t=sig[a]; sig[a]=sig[i]; sig[i]=t; pos[sig[a]]=a; pos[sig[i]]=i; }
        // may have broken earlier pairs; iterate a few times
    }
    if(sym==2){ // make involution: random involution
        int used[64]={0};
        for(int i=0;i<n;i++) if(!used[i]){
            if(rnd()%3==0){ sig[i]=i; used[i]=1; continue; }
            int tries=0; int j;
            do{ j=rnd()%n; tries++; }while((used[j]||j==i)&&tries<50);
            if(used[j]||j==i){ sig[i]=i; used[i]=1; continue; }
            sig[i]=j; sig[j]=i; used[i]=used[j]=1;
        }
        for(int i=0;i<n;i++) pos[sig[i]]=i;
    }
}
static int check_sym(int sym){
    if(sym==1){ for(int i=0;i<n;i++) if(sig[n-1-i]!=n-1-sig[i]) return 0; }
    if(sym==2){ for(int i=0;i<n;i++) if(sig[sig[i]]!=i) return 0; }
    return 1;
}

int main(int argc,char**argv){
    n=0;k=0; uint64_t seed=(uint64_t)time(NULL)^((uint64_t)getpid()<<20); long iters=100000000; double T0=0.5; int sym=0; int check=0; const char*pstr=NULL;
    double Tmin=0.15; long report=0;
    for(int i=1;i<argc;i++){
        if(!strcmp(argv[i],"-n")) n=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-k")) k=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-s")) seed=strtoull(argv[++i],0,10);
        else if(!strcmp(argv[i],"-i")) iters=atol(argv[++i]);
        else if(!strcmp(argv[i],"-T")) T0=atof(argv[++i]);
        else if(!strcmp(argv[i],"-t")) Tmin=atof(argv[++i]);
        else if(!strcmp(argv[i],"-S")) sym=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-p")) pstr=argv[++i];
        else if(!strcmp(argv[i],"-c")) check=1;
        else if(!strcmp(argv[i],"-B")) PBIG=atof(argv[++i]);
        else if(!strcmp(argv[i],"-K")) STUCK=atol(argv[++i]);
        else if(!strcmp(argv[i],"-W")) WINC=atof(argv[++i]);
        else if(!strcmp(argv[i],"-L")) LAM=atof(argv[++i]);
        else if(!strcmp(argv[i],"-R")) RH=atol(argv[++i]);
        else if(!strcmp(argv[i],"-a")) ALPHA=atof(argv[++i]);
        else if(!strcmp(argv[i],"-r")) report=atol(argv[++i]);
    }
    for(int i=0;i<40320;i++) W[i]=1.0;
    fact[0]=1; for(int i=1;i<10;i++) fact[i]=fact[i-1]*i;
    rng_s[0]=seed*0x9E3779B97F4A7C15ULL+1; rng_s[1]=seed^0xDEADBEEFCAFEULL; for(int i=0;i<20;i++) rnd();
    if(pstr){
        int m=0; const char*s=pstr; char*e;
        while(1){ long v=strtol(s,&e,10); if(e==s) break; sig[m++]=(int)v-1; s=e; }
        if(n==0) n=m; if(m!=n){fprintf(stderr,"perm length %d != n %d\n",m,n);return 1;}
    } else {
        for(int i=0;i<n;i++) sig[i]=i;
        for(int i=n-1;i>0;i--){ int j=rnd()%(i+1); int t=sig[i];sig[i]=sig[j];sig[j]=t; }
    }
    for(int i=0;i<n;i++) pos[sig[i]]=i;
    if(sym) PBIG=0;
    if(sym && !check_sym(sym)){ make_symmetric(sym); make_symmetric(sym); make_symmetric(sym); for(int i=0;i<n;i++) pos[sig[i]]=i; if(!check_sym(sym)){fprintf(stderr,"could not symmetrize\n"); return 1;} }
    full_count();
    if(check){ printf("n=%d k=%d missing=%ld of %d\n",n,k,missing,fact[k]); print_perm(stdout);
        // decode missing codes: code = sum r_m * m!, r_m = rank of m-th element among first m
        for(int c=0;c<fact[k];c++) if(!cnt[c]){ int r[10]; int x=c; for(int m=0;m<k;m++){ r[m]=x%(m+1); x/=(m+1);} 
            // rebuild pattern: insert elements; element m has r[m] smaller predecessors
            int pat[10]; for(int m=0;m<k;m++){ pat[m]=r[m]; for(int j=0;j<m;j++) if(pat[j]>=r[m]) pat[j]++; }
            // pat now: values 0..k-1? pat[j] adjusted upward when later smaller inserted -> yes gives final ranks
            printf("missing:"); for(int m=0;m<k;m++) printf(" %d",pat[m]+1); printf("\n"); }
        return missing!=0; }
    fprintf(stderr,"start n=%d k=%d sym=%d missing=%ld seed=%llu\n",n,k,sym,missing,(unsigned long long)seed);
    long best=missing; int bestsig[64]; memcpy(bestsig,sig,sizeof(sig));
    double T=T0;
    long since=0;
    for(long it=0; it<iters; it++){
        if(missing==0){
            printf("FOUND n=%d k=%d sym=%d seed=%llu it=%ld: ",n,k,sym,(unsigned long long)seed,it); print_perm(stdout); fflush(stdout);
            full_count(); if(missing!=0){ fprintf(stderr,"BUG: recheck missing=%ld\n",missing); return 2; }
            return 0;
        }
        double old=E+LAM*singles;
        int big = (urand()<PBIG);
        static uint32_t savecnt[40320]; static int savesig[64]; long sm,ss; double sE;
        if(big){
            memcpy(savecnt,cnt,sizeof(uint32_t)*fact[k]); memcpy(savesig,sig,sizeof(sig)); sm=missing; ss=singles; sE=E;
            int typ=rnd()%2;
            if(typ==0){ int a=rnd()%n, b=rnd()%n; int t=sig[a];sig[a]=sig[b];sig[b]=t; }
            else { int a=rnd()%n, b=rnd()%n; int v=sig[a]; if(a<b){ for(int q=a;q<b;q++) sig[q]=sig[q+1]; } else { for(int q=a;q>b;q--) sig[q]=sig[q-1]; } sig[b]=v; }
            if(sym==1){ for(int q=0;q<n;q++) {} /* big moves break symmetry: skip when sym */ }
            for(int q=0;q<n;q++) pos[sig[q]]=q;
            full_count();
        } else {
            gen_move(sym);
            apply_moves();
        }
        double d=E+LAM*singles-old;
        if(d>0 && urand()>=exp(-d/T)) {
            if(big){ memcpy(cnt,savecnt,sizeof(uint32_t)*fact[k]); memcpy(sig,savesig,sizeof(sig)); for(int q=0;q<n;q++) pos[sig[q]]=q; missing=sm; singles=ss; E=sE; }
            else undo_moves();
        }
        if(STUCK && since>0 && since%STUCK==0){ for(int c=0;c<fact[k];c++) if(!cnt[c]){ W[c]+=WINC; E+=WINC; } }
        if(missing<best){ best=missing; memcpy(bestsig,sig,sizeof(sig)); since=0;
            fprintf(stderr,"it=%ld T=%.3f best=%ld: ",it,T,best); print_perm(stderr); }
        else since++;
        // annealing: cool geometrically, reheat if stuck
        if((it&1023)==0){ T*=ALPHA; if(T<Tmin) T=Tmin; }
        if(since>RH){ T=T0; since=0; memcpy(sig,bestsig,sizeof(sig)); for(int i=0;i<n;i++) pos[sig[i]]=i; for(int c=0;c<fact[k];c++) W[c]=1.0; full_count(); fprintf(stderr,"reheat at it=%ld\n",it);} 
        if(report && it%report==0 && it){ long m1=missing,s1=singles; full_count(); if(m1!=missing||s1!=singles) fprintf(stderr,"MISMATCH it=%ld inc=%ld/%ld full=%ld/%ld\n",it,m1,s1,missing,singles); fprintf(stderr,"it=%ld T=%.3f cur=%ld (s%ld) best=%ld\n",it,T,missing,singles,best); }
    }
    memcpy(sig,bestsig,sizeof(sig)); full_count();
    printf("BEST n=%d k=%d sym=%d seed=%llu missing=%ld: ",n,k,sym,(unsigned long long)seed,missing); print_perm(stdout);
    return 1;
}
