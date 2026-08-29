// strips.c — exact containment of a "union of r increasing runs on value intervals" pattern in N uniform points.
// Pattern: word w in [r]^k (position i must go to strip w[i]); strips are value intervals ordered 1<2<...<r,
// each strip's points form an increasing chain (in x, hence in y).  This is exactly the pattern pi with
// pi(i) = (#letters < w[i] in w) + (#occurrences of w[i] among w[0..i]).
// Two containment notions, computed on the same samples:
//   FREE  : true pattern containment (strip boundaries are free).
//   FIXED : strip j is the fixed value interval [B_{j-1}, B_j) of the N ranks, B_j = round(N * cum height_j).
// Both by DP over points sorted by x; state = (i = #positions matched, per strip: last y (l_j), and for FREE
// also first y (f_j)); Pareto pruning per i (l smaller is better, f larger is better).  Exact (no heuristics).
// -bf: brute force (naive DFS on the permutation, independent code path) for validation.
// usage: strips [-bf] N reps seed "w (letters 1..r, space separated)" [-h "h1 h2 ... hr" | -eq]
//   default heights: proportional to run lengths k_j/k.   -eq: equal heights 1/r.
// output: N k r reps cnt_free cnt_fixed  (counts of samples in which the pattern IS contained)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static uint64_t rs, rs2=77; static inline uint64_t rng2(void){ uint64_t z=(rs2+=0x9E3779B97F4A7C15ULL); z=(z^(z>>30))*0xBF58476D1CE4E5B9ULL; z=(z^(z>>27))*0x94D049BB133111EBULL; return z^(z>>31); }
static inline uint64_t rng(void){ uint64_t z=(rs+=0x9E3779B97F4A7C15ULL); z=(z^(z>>30))*0xBF58476D1CE4E5B9ULL; z=(z^(z>>27))*0x94D049BB133111EBULL; return z^(z>>31); }
static int N,K,R; static int w[64]; static int pi[64]; static int *Y; static int B[65]; // strip bounds B[0]=0..B[R]=N
static int kj[64];

// ---------- Pareto-front DP ----------
#define D_MAX 16
typedef struct { int v[D_MAX]; } St;
static St *front[65]; static int nf[65], cap[65]; static int D;
static int dominates(const St*a,const St*b,int free){ // a at least as good as b
    for(int j=0;j<R;j++){ if(a->v[j]>b->v[j]) return 0; }
    if(free) for(int j=R;j<2*R;j++){ if(a->v[j]<b->v[j]) return 0; }
    return 1; }
static void insert(int i,const St*s,int free){
    St *F=front[i]; int n=nf[i];
    for(int t=0;t<n;t++) if(dominates(&F[t],s,free)) return;
    int m=0; for(int t=0;t<n;t++){ if(!dominates(s,&F[t],free)) F[m++]=F[t]; }
    if(m>=cap[i]){ cap[i]=cap[i]*2+8; front[i]=realloc(front[i],cap[i]*sizeof(St)); F=front[i]; }
    F[m++]=*s; nf[i]=m; }
static int stripof(int y){ for(int j=0;j<R;j++) if(y<B[j+1]) return j; return R-1; }
// run the DP; free=1: true containment, free=0: fixed strips. returns 1 if contained
static int dp(int free){
    D = free? 2*R : R;
    for(int i=0;i<=K;i++) nf[i]=0;
    St s0; for(int j=0;j<R;j++){ s0.v[j]=-1; s0.v[R+j]=N; } insert(0,&s0,free);
    for(int x=0;x<N;x++){ int y=Y[x]; int sy = free? -1 : stripof(y);
        for(int i=K-1;i>=0;i--){ int s=w[i]; if(!free && s!=sy) continue; if(nf[i]==0) continue;
            int n=nf[i]; St *F=front[i];
            for(int t=0;t<n;t++){ St st=F[t]; // copy: insert may realloc front[i+1] only, but be safe
                if(y<=st.v[s]) continue;
                if(free){ int ok=1; for(int j=0;j<s;j++) if(y<=st.v[j]){ok=0;break;} if(!ok) continue;
                          for(int j=s+1;j<R;j++) if(y>=st.v[R+j]){ok=0;break;} if(!ok) continue; }
                St ns=st; ns.v[s]=y; if(free && ns.v[R+s]==N) ns.v[R+s]=y;
                if(i+1==K) return 1;
                insert(i+1,&ns,free);
            }
        }
    }
    return 0; }


// ---------- heuristic certificate (windowed greedy, fixed strips; a found copy proves containment) ----------
static int greedy(int M){ int l[64]; for(int j=0;j<R;j++) l[j]=-1; int x=0;
    for(int i=0;i<K;i++){ int s=w[i]; int best=-1,bx=-1,seen=0;
        for(; x<N && seen<M; x++){ int y=Y[x]; if(stripof(y)!=s || y<=l[s]) continue; seen++; if(best<0||y<best){best=y;bx=x;} }
        if(best<0) return 0; l[s]=best; x=bx+1; }
    return 1; }
static int heuristic(void){ static const int Ms[]={1,2,3,4,6,8,12,16,24,32,48,64}; for(int t=0;t<12;t++) if(greedy(Ms[t])) return 1; return 0; }


// randomized windowed greedy: window size random per step
static int greedy_rand(void){ int l[64]; for(int j=0;j<R;j++) l[j]=-1; int x=0;
    for(int i=0;i<K;i++){ int s=w[i]; int best=-1,bx=-1,seen=0; int M=1+(int)(rng2()%12); if(rng2()%4==0) M=1;
        for(; x<N && seen<M; x++){ int y=Y[x]; if(stripof(y)!=s || y<=l[s]) continue; seen++; if(best<0||y<best){best=y;bx=x;} }
        if(best<0) return 0; l[s]=best; x=bx+1; }
    return 1; }
// Greene necessary condition: lambda_1+...+lambda_R (RSK shape of Y) >= K, else not contained (free or fixed)
static int greene_ok(void){ // RSK row insertion on first R rows only (rows beyond R are not needed: lambda_1..lambda_R exact)
    static int *rows[64]; static int len[64]; static int alloc=0; if(!alloc){ for(int j=0;j<R;j++) rows[j]=malloc(N*sizeof(int)); alloc=1; }
    for(int j=0;j<R;j++) len[j]=0;
    for(int x=0;x<N;x++){ int y=Y[x]; for(int j=0;j<R;j++){ int lo=0,hi=len[j]; while(lo<hi){int m=(lo+hi)/2; if(rows[j][m]<y) lo=m+1; else hi=m;}
            if(lo==len[j]){ rows[j][lo]=y; len[j]++; y=-1; break; } int t=rows[j][lo]; rows[j][lo]=y; y=t; } }
    int tot=0; for(int j=0;j<R;j++) tot+=len[j]; return tot>=K; }
static int heuristic2(void){ if(heuristic()) return 1; for(int t=0;t<40;t++) if(greedy_rand()) return 1; return 0; }

// ---------- brute force (independent): naive DFS on pi ----------
static int nlo[64],nhi[64],bsel[64]; static int bf_fixed;
static int naive(int i,int from){ if(i==K) return 1;
    for(int x=from;x<N;x++){ int q=Y[x]; int lo=nlo[i]>=0?Y[bsel[nlo[i]]]:-1, hi=nhi[i]>=0?Y[bsel[nhi[i]]]:N;
        if(q>lo&&q<hi){ if(bf_fixed && stripof(q)!=w[i]) continue; bsel[i]=x; if(naive(i+1,x+1)) return 1; } } return 0; }
static int contained_bf(int fixed){ bf_fixed=fixed;
    for(int i=0;i<K;i++){ nlo[i]=-1;nhi[i]=-1;int lo=0,hi=K+1; for(int p=0;p<i;p++){ if(pi[p]<pi[i]&&pi[p]>lo){lo=pi[p];nlo[i]=p;} if(pi[p]>pi[i]&&pi[p]<hi){hi=pi[p];nhi[i]=p;} } }
    return naive(0,0); }

int main(int argc,char**argv){
    int bf=0; if(argc>1&&strcmp(argv[1],"-bf")==0){bf=1;argv++;argc--;}
    if(argc<5){fprintf(stderr,"usage: strips [-bf] N reps seed \"w\" [-h \"h1..hr\" | -eq]\n");return 1;}
    N=atoi(argv[1]); int reps=atoi(argv[2]); rs=0x1234567ULL+(uint64_t)atoi(argv[3])*0xD1B54A32D192ED03ULL;
    K=0; R=0; { char*s=strdup(argv[4]); for(char*t=strtok(s," ");t;t=strtok(NULL," ")){ w[K]=atoi(t)-1; if(w[K]+1>R) R=w[K]+1; K++; } }
    if(R>D_MAX/2){fprintf(stderr,"r too large\n");return 1;}
    for(int j=0;j<R;j++) kj[j]=0; for(int i=0;i<K;i++) kj[w[i]]++;
    double h[64]; for(int j=0;j<R;j++) h[j]=(double)kj[j]/K;
    if(argc>5){ if(strcmp(argv[5],"-eq")==0){ for(int j=0;j<R;j++) h[j]=1.0/R; }
                else if(strcmp(argv[5],"-h")==0 && argc>6){ char*s=strdup(argv[6]); int j=0; double tot=0; for(char*t=strtok(s," ");t&&j<R;t=strtok(NULL," ")){ h[j++]=atof(t);} for(j=0;j<R;j++) tot+=h[j]; for(j=0;j<R;j++) h[j]/=tot; } }
    B[0]=0; { double c=0; for(int j=0;j<R;j++){ c+=h[j]; B[j+1]=(int)(c*N+0.5); } B[R]=N; }
    // pi from w
    { int cnt[64]={0}; int base[64]; base[0]=0; for(int j=1;j<R;j++) base[j]=base[j-1]+kj[j-1];
      for(int i=0;i<K;i++){ pi[i]=base[w[i]]+cnt[w[i]]+1; cnt[w[i]]++; } }
    Y=malloc(N*sizeof(int)); for(int i=0;i<=K;i++){front[i]=NULL;cap[i]=0;nf[i]=0;}
    int cf=0,cx=0;
    for(int r=0;r<reps;r++){
        for(int i=0;i<N;i++)Y[i]=i; for(int i=N-1;i>0;i--){int j=(int)(rng()%(uint64_t)(i+1));int t=Y[i];Y[i]=Y[j];Y[j]=t;}
        if(bf){ cf+=contained_bf(0); cx+=contained_bf(1); } else { int h=getenv("NOHEUR")?0:heuristic2(); if(h){cf++;cx++;} else if(!getenv("NOHEUR") && !greene_ok()){ } else { if(!getenv("NOFREE")) cf+=dp(1); if(!getenv("NOFIXED")) cx+=dp(0); } }
    }
    printf("%d %d %d %d %d %d\n",N,K,R,reps,cf,cx);
    return 0;
}
