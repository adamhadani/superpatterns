// W30: empty rectangles vs missing k-patterns of a random permutation.
// Usage: erect K N SAMPLES SEED R  -> per sample one line:
//  M | sigma... | for r=1..R: a b c d area Kc_r | Kany_1 Kunion_R  (rects = R largest maximal empty rectangles)
// Kc_r  = # missing patterns that become contained when one point is inserted at the centre slot of rect r.
// Kany_1= # missing patterns that become contained for SOME point of rect 1 (union over completion cells).
// Kunion_R = # missing patterns revived by at least one of the R centre phantoms.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#define MAXN 64
#define MAXR 32
#define NG 3
static int N, M;               // N = k, M = n
static int sigma[MAXN], pos[MAXN];
static uint64_t *found, *killed[MAXR], *kany, *kunion; static long nfact;
static long fact[13];
static int *cnt[13];
static long nfound;
static int vals[13], codes[13];
static inline int getbit(uint64_t*b,long c){ return (b[c>>6]>>(c&63))&1; }
static inline void setbit(uint64_t*b,long c){ b[c>>6] |= 1ULL<<(c&63); }
static long popc(uint64_t*b){ long s=0; for(long i=0;i<(nfact+63)/64;i++) s+=__builtin_popcountll(b[i]); return s; }
static void record(long code){ if(getbit(found,code)) return; setbit(found,code); nfound++; for(int j=1;j<=N;j++) cnt[j][codes[j]]++; }
static void dfs(int j, int last, long code){
    if(j==N){ record(code); return; }
    for(int q=last+1; q<=M-(N-j); q++){
        int v=sigma[q], r=0; for(int i=0;i<j;i++) r+= vals[i]<v;
        long nc=code*(j+1)+r; if(cnt[j+1][nc]==fact[N]/fact[j+1]) continue;
        vals[j]=v; codes[j+1]=nc; dfs(j+1,q,nc); if(nfound==nfact) return;
    }
}
static uint64_t rng_s=88172645463325252ULL; static inline uint64_t rng(){ rng_s^=rng_s<<7; rng_s^=rng_s>>9; return rng_s; }
static uint64_t rng2_s=0x1234567887654321ULL; static inline uint64_t rng2(){ rng2_s^=rng2_s<<7; rng2_s^=rng2_s>>9; return rng2_s; }
static void seed_random(long trials){ int p[13];
    for(long t=0;t<trials && nfound<nfact;t++){ int c=0;
        for(int q=0;q<M && c<N;q++){ if( (rng2()%(M-q)) < (uint64_t)(N-c) ) p[c++]=q; }
        long code=0; for(int j=0;j<N;j++){ int v=sigma[p[j]], r=0; for(int i=0;i<j;i++) r+= vals[i]<v; vals[j]=v; code=code*(j+1)+r; codes[j+1]=code; }
        record(code); } }
static void run_perm(){ memset(found,0,((nfact+63)/64)*8); for(int j=1;j<=N;j++) memset(cnt[j],0,fact[j]*sizeof(int));
    nfound=0; codes[0]=0; seed_random((long)M*M*200); if(nfound<nfact) dfs(0,-1,0); }

// ---- empty rectangles ----
static int P[MAXN+1][MAXN+1];
static inline int rc(int a,int b,int c,int d){ return P[b+1][d+1]-P[a][d+1]-P[b+1][c]+P[a][c]; }
typedef struct { int a,b,c,d,area; } Rect;
static Rect rects[MAXN*MAXN*MAXN]; static int nrects;
static int cmp(const void*x,const void*y){ return ((Rect*)y)->area-((Rect*)x)->area; }
static void find_rects(){
    for(int i=0;i<=M;i++) for(int v=0;v<=M;v++){ P[i][v]= (i>0&&v>0)? P[i-1][v]+P[i][v-1]-P[i-1][v-1]+(sigma[i-1]==v-1) : 0; }
    nrects=0;
    for(int a=0;a<M;a++) for(int b=a;b<M;b++){
        for(int c=0;c<M;c++){
            // largest d with [a,b]x[c,d] empty
            if(rc(a,b,c,c)) continue;
            int d=c; while(d+1<M && rc(a,b,c,d+1)==0) d++;
            // maximal? vertical: c==0 or column of value c-1 inside [a,b] (else could extend down) -> need pos[c-1] in [a,b]
            int okdown = (c==0) || (pos[c-1]>=a && pos[c-1]<=b);
            int okup   = (d==M-1) || (pos[d+1]>=a && pos[d+1]<=b);
            int okleft = (a==0) || (sigma[a-1]>=c && sigma[a-1]<=d);
            int okright= (b==M-1) || (sigma[b+1]>=c && sigma[b+1]<=d);
            if(okdown&&okup&&okleft&&okright){ Rect r={a,b,c,d,(b-a+1)*(d-c+1)}; rects[nrects++]=r; }
            c=d; // next c beyond d (loop increments)
        }
    }
    qsort(rects,nrects,sizeof(Rect),cmp);
}
// ---- phantom enumeration over (k-1)-subsets ----
static int R, Rrect; static int ps[MAXR], pt[MAXR]; // phantom slots: insert before index ps, value rank pt (phantom value pt-0.5)
static int sub[13], subv[13], rk[13];
static inline long code_with(int i,int j){ // insert phantom at position rank i, value rank j-0.5 (j = # subset values below)
    long code=0; int m=0;
    for(int q=0;q<N;q++){
        int r;
        if(q==i){ r=0; for(int t=0;t<i;t++) r+= rk[t]<j; }
        else { int t=(q<i)?q:q-1; r=0; for(int u=0;u<t;u++) r+= rk[u]<rk[t]; if(q>i && rk[t]>=j) r++; }
        code=code*(q+1)+r; m++;
    }
    return code;
}
static int Q1a,Q1b,Q1c,Q1d;
static void process_subset(){
    // ranks in position order
    for(int t=0;t<N-1;t++){ int r=0; for(int u=0;u<N-1;u++) r+= subv[u]<subv[t]; rk[t]=r; }
    for(int r=0;r<R;r++){
        int i=0; while(i<N-1 && sub[i]<ps[r]) i++;
        int j=0; for(int t=0;t<N-1;t++) j+= subv[t]<pt[r];
        long c=code_with(i,j); if(getbit(found,c)==0){ setbit(killed[r],c); if(r<Rrect) setbit(kunion,c); }
    }
    // any-point variant for rect 1: position gaps i with p_{i-1}<=Q1b and p_i>=Q1a ; value gaps j with q_{j-1}<=Q1d and q_j>=Q1c
    int sv[13]; for(int t=0;t<N-1;t++) sv[t]=subv[t];
    // sort values
    for(int x=1;x<N-1;x++){ int v=sv[x],y=x; while(y>0&&sv[y-1]>v){sv[y]=sv[y-1];y--;} sv[y]=v; }
    for(int i=0;i<N;i++){
        int pl = (i==0)? -1 : sub[i-1]; int pr = (i==N-1)? M : sub[i];
        if(!(pl<=Q1b && pr>=Q1a)) continue;
        for(int j=0;j<N;j++){
            int ql=(j==0)?-1:sv[j-1]; int qr=(j==N-1)?M:sv[j];
            if(!(ql<=Q1d && qr>=Q1c)) continue;
            long c=code_with(i,j); if(getbit(found,c)==0) setbit(kany,c);
        }
    }
}
static void enum_subsets(int j,int last){
    if(j==N-1){ process_subset(); return; }
    for(int q=last+1;q<=M-(N-1-j);q++){ sub[j]=q; subv[j]=sigma[q]; enum_subsets(j+1,q); }
}
int main(int argc,char**argv){
    if(argc<6){ fprintf(stderr,"usage: erect K N SAMPLES SEED R\n"); return 1; }
    N=atoi(argv[1]); M=atoi(argv[2]); int samples=atoi(argv[3]); unsigned seed=(unsigned)atoi(argv[4]); R=atoi(argv[5]); if(R>MAXR)R=MAXR;
    rng_s ^= (uint64_t)seed*0x9E3779B97F4A7C15ULL; rng(); rng2_s ^= (uint64_t)seed*0xD1B54A32D192ED03ULL; rng2();
    fact[0]=1; for(int j=1;j<=12;j++) fact[j]=fact[j-1]*j; nfact=fact[N];
    long W=(nfact+63)/64; found=calloc(W,8); kany=calloc(W,8); kunion=calloc(W,8); for(int r=0;r<MAXR;r++) killed[r]=calloc(W,8);
    for(int j=1;j<=N;j++) cnt[j]=calloc(fact[j],sizeof(int));
    clock_t t0=clock();
    for(int s=0;s<samples;s++){
        for(int i=0;i<M;i++) sigma[i]=i;
        for(int i=M-1;i>0;i--){ int j=rng()%(i+1); int t=sigma[i];sigma[i]=sigma[j];sigma[j]=t; }
        for(int i=0;i<M;i++) pos[sigma[i]]=i;
        run_perm(); long miss=nfact-nfound;
        find_rects();
        int Ruse = R<nrects? R: nrects;
        printf("%ld |",miss); for(int i=0;i<M;i++) printf(" %d",sigma[i]+1); printf(" |");
        if(miss>0){
            memset(kany,0,W*8); memset(kunion,0,W*8);
            for(int r=0;r<Ruse;r++){ memset(killed[r],0,W*8); Rect q=rects[r]; ps[r]=(q.a+q.b+2)/2; pt[r]=(q.c+q.d+2)/2; }
            Q1a=rects[0].a;Q1b=rects[0].b;Q1c=rects[0].c;Q1d=rects[0].d;
            int Rsave=R; R=Ruse; Rrect=Ruse;
            ps[R]=rng()%(M+1); pt[R]=rng()%(M+1); memset(killed[R],0,W*8); R++;
            for(int gi=0;gi<NG;gi++) for(int gj=0;gj<NG;gj++){ ps[R]=((M+1)*(2*gi+1))/(2*NG); pt[R]=((M+1)*(2*gj+1))/(2*NG); memset(killed[R],0,W*8); R++; }
            int Rtot=R; enum_subsets(0,-1); R=Rsave;
            for(int r=0;r<Ruse;r++){ Rect q=rects[r]; printf(" %d %d %d %d %d %ld",q.a,q.b,q.c,q.d,q.area,popc(killed[r])); }
            printf(" | %ld %ld %ld |",popc(kany),popc(kunion),popc(killed[Ruse]));
            for(int r=Ruse+1;r<Rtot;r++) printf(" %ld",popc(killed[r]));
            long hist[NG*NG+1]; memset(hist,0,sizeof hist);
            for(long c=0;c<nfact;c++){ if(getbit(found,c)) continue; int m=0; for(int r=Ruse+1;r<Rtot;r++) m+=getbit(killed[r],c); hist[m]++; }
            printf(" |"); for(int m=0;m<=NG*NG;m++) printf(" %ld",hist[m]); printf("\n");
        } else {
            for(int r=0;r<Ruse;r++){ Rect q=rects[r]; printf(" %d %d %d %d %d 0",q.a,q.b,q.c,q.d,q.area); }
            printf(" | 0 0 0 | | \n");
        }
        if((s+1)%20==0) fflush(stdout);
    }
    fprintf(stderr,"# k=%d n=%d samples=%d seed=%u secs=%.1f\n",N,M,samples,seed,(double)(clock()-t0)/CLOCKS_PER_SEC);
    return 0;
}
