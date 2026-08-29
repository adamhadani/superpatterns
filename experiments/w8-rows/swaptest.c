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
static int n, k, m, rowmode=2, period=0;
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
static int valid(const State*s){
    int c[MAXM]={0}; for(int p=0;p<n;p++) c[s->w[p]]++;
    for(int l=0;l<m;l++){ if(c[l]!=s->mult[l]) return 0; if(s->mult[l]<1) return 0;
        int seen[MAXMULT]={0}; for(int j=0;j<s->mult[l];j++){ int r=s->rp[l][j]; if(r<0||r>=s->mult[l]||seen[r]) return 0; seen[r]=1; }
        if(rowmode==0){ for(int j=0;j<s->mult[l];j++) if(s->rp[l][j]!=s->mult[l]-1-j) return 0; }
        if(rowmode==1){ int inc=1,dec=1; for(int j=0;j<s->mult[l];j++){ if(s->rp[l][j]!=j) inc=0; if(s->rp[l][j]!=s->mult[l]-1-j) dec=0; } if(!inc&&!dec) return 0; }
    }
    return 1;
}
// apply transition sig -> target as transpositions; record them
static int tlog[2*MAXN][2], ntl;
static void goto_sigma(const int*target){
    ntl=0;
    for(int p=0;p<n;p++) while(sig[p]!=target[p]){ int q=pos[target[p]]; tlog[ntl][0]=p; tlog[ntl][1]=q; ntl++; swap_pos(p,q); }
}
static void undo_sigma(void){ for(int t=ntl-1;t>=0;t--) swap_pos(tlog[t][0],tlog[t][1]); }

static void set_row_random(State*s,int l){
    int t=s->mult[l];
    if(rowmode==0){ for(int j=0;j<t;j++) s->rp[l][j]=t-1-j; return; }
    if(rowmode==1){ int d=rnd()&1; for(int j=0;j<t;j++) s->rp[l][j]= d? t-1-j : j; return; }
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
        if(rnd()&1){ int x=Tr.rp[l][a]; Tr.rp[l][a]=Tr.rp[l][b]; Tr.rp[l][b]=x; }
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
        int p=rnd()%n, q; if(rnd()&1){ int d=1+rnd()%3; q=(rnd()&1)? p+d : p-d; if(q<0||q>=n) return 0; } else q=rnd()%n;
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
      if(rowmode<2){ set_row_random(&Tr,a); set_row_random(&Tr,b); }
      return 1; }
}


int main(int argc,char**argv){ n=atoi(argv[1]); k=atoi(argv[2]); fact[0]=1; for(int i=1;i<11;i++) fact[i]=fact[i-1]*i; for(int i=0;i<fact[k];i++) W[i]=1;
  rng_s[0]=12345; rng_s[1]=999; for(int i=0;i<n;i++) sig[i]=i; for(int i=n-1;i>0;i--){int j=rnd()%(i+1);int t=sig[i];sig[i]=sig[j];sig[j]=t;} for(int i=0;i<n;i++) pos[sig[i]]=i;
  full_count(); int bad=0;
  for(int it=0;it<300;it++){ int a,b; if(getenv("ADJP")){a=rnd()%(n-1);b=a+1;} else if(getenv("ADJV")){int v=rnd()%(n-1);a=pos[v];b=pos[v+1];} else {a=rnd()%n;b=rnd()%n;} if(a==b) continue; int va=sig[a],vb=sig[b]; swap_pos(a,b); long mi=missing; static uint32_t c2[362880]; memcpy(c2,cnt,sizeof(uint32_t)*fact[k]); full_count(); int d=0; for(int c=0;c<fact[k];c++) if(c2[c]!=cnt[c]) d++; if(d){ bad++; if(bad<5) printf("swap a=%d b=%d va=%d vb=%d: bad codes %d inc=%ld full=%ld\n",a,b,va,vb,d,mi,missing);} }
  printf("bad=%d\n",bad); return 0; }
