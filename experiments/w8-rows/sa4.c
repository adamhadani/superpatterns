// sa4: simulated annealing over ROW-STRUCTURED permutations.
//   state = word w over [m] of length n  +  for each letter l a row pattern rp[l] (a permutation of its multiplicity)
//   sigma = tie-broken permutation: letter l owns the value interval base[l]..base[l]+mult[l]-1, and the j-th
//           occurrence (left to right) of l gets value base[l]+rp[l][j].
//   Incremental k-pattern counting = sp.c machinery (pair swaps), a move is applied as a sequence of transpositions.
// Usage: sa4 -n N -k K -m M [-R rowmode] [-P B] [-s seed] [-i iters] [-T T0] [-t Tmin] [-o outfile]
//   -R 0: all rows decreasing (tie-broken word, EV family); 1: rows monotone (either direction); 2: free row patterns
//   -P B: periodic word = B copies of one permutation rho of [m] (n = m*B); letter moves act on rho
//   -w "word" -r "rowpats" : initial state (word 1-based; rowpats = concatenation of per-letter patterns, 1-based)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
#include <unistd.h>

#define MAXN 64
#define MAXM 40
#define MAXMULT 12
static int n, k, m, rowmode=2, period=0, Q=0;
static int sig[MAXN], pos[MAXN];
static uint32_t cnt[362880]; static double W[362880]; static double E; static long STUCK=20000; static double WINC=1.0; static long RH=400000; static double ALPHA=0.999;
static int fact[11];
static long missing, singles; static double LAM=0.3;

static inline int pc(uint64_t x){ return __builtin_popcountll(x); }
static void dfs_full(int p0, int m_, uint64_t mask, int code){
    if(m_==k){ cnt[code]++; return; }
    int lim = n-(k-m_);
    for(int p=p0;p<=lim;p++){ int v=sig[p]; int r=pc(mask & ((1ULL<<v)-1)); dfs_full(p+1,m_+1,mask|(1ULL<<v),code+r*fact[m_]); }
}
static void full_count(void){
    memset(cnt,0,sizeof(uint32_t)*fact[k]); dfs_full(0,0,0,0);
    missing=0; singles=0; E=0;
    for(int i=0;i<fact[k];i++){ if(!cnt[i]){ missing++; E+=W[i]; } else if(cnt[i]==1) singles++; }
}
static int PA,PB;
static void dfs_pair(int p0,int m_,uint64_t mask,uint64_t mask2,int c1,int c2){
    if(m_==k){
        if(c1!=c2){
            { uint32_t c=--cnt[c1]; if(c==0){missing++;singles--;E+=W[c1];} else if(c==1) singles++; }
            { uint32_t c=cnt[c2]++; if(c==0){missing--;singles++;E-=W[c2];} else if(c==1) singles--; }
        }
        return;
    }
    int forced=(p0<=PA)+(p0<=PB);
    if(k-m_<forced) return;
    int lim=n-(k-m_);
    int start=p0;
    if(k-m_==forced) start=(p0<=PA)?PA:PB;
    for(int p=start;p<=lim;p++){
        int v=sig[p]; int v2 = (p==PA)? sig[PB] : (p==PB)? sig[PA] : v;
        int r=pc(mask&((1ULL<<v)-1)); int r2=pc(mask2&((1ULL<<v2)-1));
        dfs_pair(p+1,m_+1,mask|(1ULL<<v),mask2|(1ULL<<v2),c1+r*fact[m_],c2+r2*fact[m_]);
        if(p==PA||p==PB) break;
    }
}
static void swap_pos(int a,int b){
    if(a==b) return; if(a>b){int t=a;a=b;b=t;}
    PA=a;PB=b; dfs_pair(0,0,0,0,0,0);
    int t=sig[a]; sig[a]=sig[b]; sig[b]=t; pos[sig[a]]=a; pos[sig[b]]=b;
}
static uint64_t rng_s[2];
static inline uint64_t rnd(void){ uint64_t s1=rng_s[0], s0=rng_s[1]; rng_s[0]=s0; s1^=s1<<23; rng_s[1]=s1^s0^(s1>>17)^(s0>>26); return rng_s[1]+s0; }
static inline double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }

// ---------- row-structured state ----------
typedef struct { int w[MAXN]; int mult[MAXM]; int rp[MAXM][MAXMULT]; } State;
static State S, Tr;
static void build_sigma(const State*s, int*out){
    int base[MAXM], occ[MAXM]; int b=0;
    for(int l=0;l<m;l++){ base[l]=b; b+=s->mult[l]; occ[l]=0; }
    for(int p=0;p<n;p++){ int l=s->w[p]; out[p]=base[l]+s->rp[l][occ[l]++]; }
}
static int maxrow=0;
static int valid(const State*s){
    int c[MAXM]={0}; int nonmono=0; for(int p=0;p<n;p++) c[s->w[p]]++;
    for(int l=0;l<m;l++){ if(c[l]!=s->mult[l]) return 0; if(s->mult[l]<1) return 0;
        int seen[MAXMULT]={0}; for(int j=0;j<s->mult[l];j++){ int r=s->rp[l][j]; if(r<0||r>=s->mult[l]||seen[r]) return 0; seen[r]=1; }
        if(rowmode==0){ for(int j=0;j<s->mult[l];j++) if(s->rp[l][j]!=s->mult[l]-1-j) return 0; }
        if(rowmode==1||rowmode==3){ int inc=1,dec=1; for(int j=0;j<s->mult[l];j++){ if(s->rp[l][j]!=j) inc=0; if(s->rp[l][j]!=s->mult[l]-1-j) dec=0; } if(!inc&&!dec){ if(rowmode==1) return 0; nonmono++; } }
        if(maxrow && s->mult[l]>maxrow) return 0;
    }
    if(rowmode==3 && nonmono>Q) return 0;
    return 1;
}
// apply transition sig -> target. Incremental (sp.c pair DFS) ONLY when the change is an adjacent-position swap
// or an adjacent-value swap (the DFS is only valid for those); otherwise full recount with save/restore.
static int tlog[2][2], ntl, usedfull; static uint32_t savecnt[362880]; static long sm,ss; static double sE;
static void goto_sigma(const int*target){
    int diff[MAXN], nd=0; for(int p=0;p<n;p++) if(sig[p]!=target[p]) diff[nd++]=p;
    ntl=0; usedfull=0; if(nd==0) return;
    if(nd==2 && (diff[1]==diff[0]+1 || abs(sig[diff[0]]-sig[diff[1]])==1)){ tlog[0][0]=diff[0]; tlog[0][1]=diff[1]; ntl=1; swap_pos(diff[0],diff[1]); return; }
    usedfull=1; memcpy(savecnt,cnt,sizeof(uint32_t)*fact[k]); sm=missing; ss=singles; sE=E;
    for(int p=0;p<n;p++){ sig[p]=target[p]; pos[sig[p]]=p; } full_count();
}
static void undo_sigma(void){
    if(usedfull){ memcpy(cnt,savecnt,sizeof(uint32_t)*fact[k]); missing=sm; singles=ss; E=sE; /* sig restored by caller from S */ return; }
    for(int t=ntl-1;t>=0;t--) swap_pos(tlog[t][0],tlog[t][1]);
}
static void set_row_random(State*s,int l){
    int t=s->mult[l];
    if(rowmode==0){ for(int j=0;j<t;j++) s->rp[l][j]=t-1-j; return; }
    if(rowmode==1||rowmode==3){ int d=rnd()&1; for(int j=0;j<t;j++) s->rp[l][j]= d? t-1-j : j; return; }
    for(int j=0;j<t;j++) s->rp[l][j]=j; for(int j=t-1;j>0;j--){ int q=rnd()%(j+1); int x=s->rp[l][j]; s->rp[l][j]=s->rp[l][q]; s->rp[l][q]=x; }
}
static void print_state(FILE*f,const State*s){
    fprintf(f,"word:"); for(int p=0;p<n;p++) fprintf(f," %d",s->w[p]+1);
    fprintf(f,"  rows:"); for(int l=0;l<m;l++){ fprintf(f," "); for(int j=0;j<s->mult[l];j++) fprintf(f,"%d",s->rp[l][j]+1); }
    fprintf(f,"  perm:"); int o[MAXN]; build_sigma(s,o); for(int p=0;p<n;p++) fprintf(f," %d",o[p]+1); fprintf(f,"\n");
}
// generate a trial state in Tr from S. returns 0 if move impossible.
static int gen_move(void){
    Tr=S;
    int typ=rnd()%100;
    if(rowmode==0) typ = typ%70; // no row moves
    if(typ<40){ // row pattern move
        int l=rnd()%m; int t=Tr.mult[l]; if(t<2) return 0;
        if(rowmode==1){ for(int j=0;j<t;j++) Tr.rp[l][j]=t-1-Tr.rp[l][j]; return 1; }
        int a=rnd()%t, b=rnd()%t; if(a==b) return 0;
        if(rnd()%4==0){ int x=Tr.rp[l][a]; Tr.rp[l][a]=Tr.rp[l][b]; Tr.rp[l][b]=x; }
        else if(rowmode==3 && rnd()%3==0){ for(int j=0;j<t;j++) Tr.rp[l][j]=t-1-Tr.rp[l][j]; }
        else { // adjacent-rank swap: swap ranks r and r+1
            int r=rnd()%(t-1); for(int j=0;j<t;j++){ if(Tr.rp[l][j]==r) Tr.rp[l][j]=r+1; else if(Tr.rp[l][j]==r+1) Tr.rp[l][j]=r; } }
        return 1;
    }
    if(period){ // letter moves on rho
        int a=rnd()%m, b=rnd()%m; if(a==b) return 0;
        if(rnd()%3==0){ // move letter at rho position a to position b
            int rho[MAXM]; for(int i=0;i<m;i++) rho[i]=Tr.w[i]; int v=rho[a]; if(a<b) for(int i=a;i<b;i++) rho[i]=rho[i+1]; else for(int i=a;i>b;i--) rho[i]=rho[i-1]; rho[b]=v;
            for(int B_=0;B_<period;B_++) for(int i=0;i<m;i++) Tr.w[B_*m+i]=rho[i];
        } else { for(int B_=0;B_<period;B_++){ int x=Tr.w[B_*m+a]; Tr.w[B_*m+a]=Tr.w[B_*m+b]; Tr.w[B_*m+b]=x; } }
        return 1;
    }
    if(typ<70){ // swap two positions with different letters (prefer nearby half the time)
        int p=rnd()%n, q; if(rnd()%4){ q=p+1; if(q>=n) return 0; } else q=rnd()%n;
        if(Tr.w[p]==Tr.w[q]) return 0; int x=Tr.w[p]; Tr.w[p]=Tr.w[q]; Tr.w[q]=x; return 1;
    }
    if(typ<85){ // shift a letter by up to 3 places
        int p=rnd()%n; int d=1+rnd()%3; int q=(rnd()&1)? p+d : p-d; if(q<0||q>=n) return 0;
        int v=Tr.w[p]; if(p<q) for(int i=p;i<q;i++) Tr.w[i]=Tr.w[i+1]; else for(int i=p;i>q;i--) Tr.w[i]=Tr.w[i-1]; Tr.w[q]=v; return 1;
    }
    // relabel one occurrence of letter a to adjacent letter b (changes multiplicities)
    { int p=rnd()%n; int a=Tr.w[p]; int b= (rnd()&1)? a+1 : a-1; if(b<0||b>=m) return 0; if(Tr.mult[a]<2 || Tr.mult[b]>=MAXMULT-1) return 0;
      // remove occurrence index j of a
      int j=0; for(int q=0;q<p;q++) if(Tr.w[q]==a) j++;
      int r=Tr.rp[a][j]; for(int i=j;i<Tr.mult[a]-1;i++) Tr.rp[a][i]=Tr.rp[a][i+1]; Tr.mult[a]--; for(int i=0;i<Tr.mult[a];i++) if(Tr.rp[a][i]>r) Tr.rp[a][i]--;
      // insert into b at occurrence index jb with rank rb
      Tr.w[p]=b; int jb=0; for(int q=0;q<p;q++) if(Tr.w[q]==b) jb++;
      int tb=Tr.mult[b]; int rb=(int)(rnd()%(tb+1));
      for(int i=0;i<tb;i++) if(Tr.rp[b][i]>=rb) Tr.rp[b][i]++;
      for(int i=tb;i>jb;i--) Tr.rp[b][i]=Tr.rp[b][i-1]; Tr.rp[b][jb]=rb; Tr.mult[b]++;
      if(rowmode<2 || rowmode==3){ /* keep sigma: monotone rows only if consistent; else random monotone */ }
      return 1; }
}

int main(int argc,char**argv){
    n=0;k=0;m=0; uint64_t seed=(uint64_t)time(NULL)^((uint64_t)getpid()<<20); long iters=100000000; double T0=0.6, Tmin=0.15; const char*wstr=NULL,*rstr=NULL; const char*outf=NULL; long report=0;
    for(int i=1;i<argc;i++){
        if(!strcmp(argv[i],"-n")) n=atoi(argv[++i]); else if(!strcmp(argv[i],"-k")) k=atoi(argv[++i]); else if(!strcmp(argv[i],"-m")) m=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-R")) rowmode=atoi(argv[++i]); else if(!strcmp(argv[i],"-P")) period=atoi(argv[++i]);
        else if(!strcmp(argv[i],"-s")) seed=strtoull(argv[++i],0,10); else if(!strcmp(argv[i],"-i")) iters=atol(argv[++i]);
        else if(!strcmp(argv[i],"-T")) T0=atof(argv[++i]); else if(!strcmp(argv[i],"-t")) Tmin=atof(argv[++i]);
        else if(!strcmp(argv[i],"-w")) wstr=argv[++i]; else if(!strcmp(argv[i],"-r")) rstr=argv[++i]; else if(!strcmp(argv[i],"-o")) outf=argv[++i];
        else if(!strcmp(argv[i],"-K")) STUCK=atol(argv[++i]); else if(!strcmp(argv[i],"-L")) LAM=atof(argv[++i]); else if(!strcmp(argv[i],"-a")) ALPHA=atof(argv[++i]);
        else if(!strcmp(argv[i],"-RH")) RH=atol(argv[++i]); else if(!strcmp(argv[i],"-Q")) Q=atoi(argv[++i]); else if(!strcmp(argv[i],"-X")) maxrow=atoi(argv[++i]); else if(!strcmp(argv[i],"-rep")) report=atol(argv[++i]);
    }
    if(period){ n=m*period; }
    if(n<=0||k<=0||m<=0||n>MAXN||m>MAXM){ fprintf(stderr,"bad args\n"); return 1; }
    fact[0]=1; for(int i=1;i<11;i++) fact[i]=fact[i-1]*i; for(int i=0;i<fact[k];i++) W[i]=1.0;
    rng_s[0]=seed*0x9E3779B97F4A7C15ULL+1; rng_s[1]=seed^0xDEADBEEFCAFEULL; for(int i=0;i<20;i++) rnd();
    // initial state
    memset(&S,0,sizeof(S));
    if(wstr){ int c=0; const char*s=wstr; char*e; while(1){ long v=strtol(s,&e,10); if(e==s) break; S.w[c++]=(int)v-1; s=e; } if(c!=n){fprintf(stderr,"word len %d != n\n",c); return 1;} }
    else if(period){ int rho[MAXM]; for(int i=0;i<m;i++) rho[i]=i; for(int i=m-1;i>0;i--){ int j=rnd()%(i+1); int t=rho[i]; rho[i]=rho[j]; rho[j]=t; } for(int b=0;b<period;b++) for(int i=0;i<m;i++) S.w[b*m+i]=rho[i]; }
    else { for(int p=0;p<n;p++) S.w[p]=p%m; for(int i=n-1;i>0;i--){ int j=rnd()%(i+1); int t=S.w[i]; S.w[i]=S.w[j]; S.w[j]=t; } }
    for(int p=0;p<n;p++) S.mult[S.w[p]]++;
    for(int l=0;l<m;l++) if(S.mult[l]<1){ fprintf(stderr,"letter %d unused\n",l+1); return 1; }
    if(rstr){ const char*s=rstr; char*e; for(int l=0;l<m;l++) for(int j=0;j<S.mult[l];j++){ long v=strtol(s,&e,10); if(e==s){fprintf(stderr,"rowpats short\n");return 1;} S.rp[l][j]=(int)v-1; s=e; } }
    else for(int l=0;l<m;l++) set_row_random(&S,l);
    if(!valid(&S)){ fprintf(stderr,"invalid initial state\n"); return 1; }
    build_sigma(&S,sig); for(int p=0;p<n;p++) pos[sig[p]]=p;
    full_count();
    fprintf(stderr,"start n=%d k=%d m=%d R=%d P=%d missing=%ld seed=%llu\n",n,k,m,rowmode,period,missing,(unsigned long long)seed);
    long best=missing; State bestS=S; double T=T0; long since=0;
    FILE*fo = outf? fopen(outf,"a") : stdout;
    for(long it=0; it<iters; it++){
        if(missing==0){
            full_count(); if(missing!=0){ fprintf(stderr,"BUG recheck missing=%ld\n",missing); return 2; }
            fprintf(fo,"FOUND n=%d k=%d m=%d R=%d P=%d seed=%llu it=%ld ",n,k,m,rowmode,period,(unsigned long long)seed,it); print_state(fo,&S); fflush(fo);
            return 0;
        }
        if(!gen_move()) continue;
        if(!valid(&Tr)) continue;
        double old=E+LAM*singles;
        int target[MAXN]; build_sigma(&Tr,target); goto_sigma(target);
        double d=E+LAM*singles-old;
        if(0){ long mi=missing; uint32_t c2[362880]; memcpy(c2,cnt,sizeof(uint32_t)*fact[k]); int sv[MAXN]; memcpy(sv,sig,sizeof(sig)); full_count();
            int bad=0; for(int c=0;c<fact[k];c++) if(c2[c]!=cnt[c]) bad++; if(bad||mi!=missing){ fprintf(stderr,"DBG it=%ld ntl=%d inc=%ld full=%ld badcodes=%d sigOK=%d\n",it,ntl,mi,missing,bad,!memcmp(sv,sig,sizeof(sig))); for(int t=0;t<ntl;t++) fprintf(stderr,"  swap %d %d\n",tlog[t][0],tlog[t][1]); }
            memcpy(cnt,c2,sizeof(uint32_t)*fact[k]); missing=mi; }
        if(d>0 && urand()>=exp(-d/T)){ undo_sigma(); if(usedfull){ build_sigma(&S,sig); for(int p=0;p<n;p++) pos[sig[p]]=p; } } else S=Tr;
        if(STUCK && since>0 && since%STUCK==0){ for(int c=0;c<fact[k];c++) if(!cnt[c]){ W[c]+=WINC; E+=WINC; } }
        if(missing<best){ best=missing; bestS=S; since=0; fprintf(stderr,"it=%ld T=%.3f best=%ld ",it,T,best); print_state(stderr,&S); }
        else since++;
        if((it&255)==0){ T*=ALPHA; if(T<Tmin) T=Tmin; }
        if(since>RH){ T=T0; since=0; S=bestS; build_sigma(&S,sig); for(int p=0;p<n;p++) pos[sig[p]]=p; for(int c=0;c<fact[k];c++) W[c]=1.0; full_count(); fprintf(stderr,"reheat at it=%ld\n",it); }
        if(report && it%report==0 && it){ long m1=missing; full_count(); if(m1!=missing) fprintf(stderr,"MISMATCH it=%ld inc=%ld full=%ld\n",it,m1,missing); fprintf(stderr,"it=%ld T=%.3f cur=%ld best=%ld\n",it,T,missing,best); }
    }
    S=bestS; build_sigma(&S,sig); for(int p=0;p<n;p++) pos[sig[p]]=p; full_count();
    fprintf(fo,"BEST n=%d k=%d m=%d R=%d P=%d seed=%llu missing=%ld ",n,k,m,rowmode,period,(unsigned long long)seed,missing); print_state(fo,&S); fflush(fo);
    return 1;
}
