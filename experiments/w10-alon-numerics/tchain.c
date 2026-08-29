// tchain.c — exact longest tau-chain in N uniform random points (W10).
// L_tau(P) = max L such that tau^{(+)L} (direct sum of L copies of tau) is contained in P.
//
// Algorithm (exact):  F(x,y) = max number of copies in a chain whose boxes lie in [0,x) x [0,y).
// A copy C (box [xmin,xmax] x [ymin,ymax]) has value val(C) = 1 + F(xmin, ymin); chain length = max val.
// Copies are enumerated by "runs": for every point p1 (in x order) we build all copies whose leftmost point is p1,
// sweeping the points to the right and keeping partial copies as states.  A state S (placed y's; ymin,ymax so far;
// vposs = 1+F(x_p1, ymin) an upper bound for the final value) can only complete into copies with value <= vposs,
// x_max >= x_cur, y_max >= ymax(S); so S is discarded as soon as some completed copy C' of the same run has
// val(C') >= vposs, y_max(C') <= ymax(S)  (all copies completed so far have x_max <= x_cur).  This is exact.
// The root state {p1} is discarded when a copy with value >= v0 = 1+F(x_p1,y_p1), x_max <= x_cur, y_max <= y_p1
// exists (global per-column suffix-min tables).  F is a Fenwick prefix-max over y_max, fed column by column.
//
// Modes:  tchain N reps tau seed          fast exact algorithm; prints per-sample "N tau seed L LIS"
//         tchain -bf N reps tau seed      brute force: enumerate all copies, O(#copies^2) DP  (small N only)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>

static uint64_t rs = 0x9E3779B97F4A7C15ULL;
static inline uint64_t rng(void){ uint64_t z=(rs+=0x9E3779B97F4A7C15ULL); z=(z^(z>>30))*0xBF58476D1CE4E5B9ULL; z=(z^(z>>27))*0x94D049BB133111EBULL; return z^(z>>31); }

static int N, J; static int tau[12]; static int loIdx[12], hiIdx[12];
static int *Y;

static void setup_tau(const char *s){
    J = (int)strlen(s);
    for(int i=0;i<J;i++) tau[i] = s[i]-'0';
    for(int i=0;i<J;i++){
        loIdx[i]=-1; hiIdx[i]=-1; int lo=0, hi=J+1;
        for(int p=0;p<i;p++){
            if(tau[p]<tau[i] && tau[p]>lo){lo=tau[p];loIdx[i]=p;}
            if(tau[p]>tau[i] && tau[p]<hi){hi=tau[p];hiIdx[i]=p;}
        }
    }
}
static void gen_perm(void){
    for(int i=0;i<N;i++)Y[i]=i;
    for(int i=N-1;i>0;i--){int j=(int)(rng()%(uint64_t)(i+1));int t=Y[i];Y[i]=Y[j];Y[j]=t;}
}
static int lis(void){
    int *tails=malloc(N*sizeof(int)); int m=0;
    for(int i=0;i<N;i++){ int lo=0,hi=m; while(lo<hi){int mid=(lo+hi)/2; if(tails[mid]<Y[i])lo=mid+1; else hi=mid;} tails[lo]=Y[i]; if(lo==m)m++; }
    free(tails); return m;
}

/* ---------------- fast exact algorithm (right-anchored runs) ----------------
   tv[x][v] = min y_max over chains of value >= v whose last copy has x_max < x  (N+1 columns, W values); F(x,y)=max{v: tv[x][v]<y}.
   Run for the point p_J at column xj: build copies whose RIGHTMOST point is p_J by scanning leftwards, placing tau positions J-1,J-2,...,0.
   State S: eventual value <= vb(S)=1+F(x_cur, ymin(S)), corner (xj, >= ymax(S)).  Killed (exactly) when a chain of value >= vb(S)
   already ends at corner <= (xj, ymax(S)): either from this run (runSuf) or from copies with x_max < xj (tv[xj]).
   States with identical relevant placed values (value-adjacent to an unplaced element) are merged (exact). */
typedef struct { int ys[10]; int cnt, ymin, ymax, vb; } State;
static int W; static int *tv;   // (N+1)*W
static int relPos[12][12], nRel[12], minPl[12], maxPl[12]; // per stage cnt=i (positions J-i..J-1 placed)
static int rloIdx[12], rhiIdx[12];
static inline int Fq(int x,int y){ const int *t=tv+(size_t)x*W; int v=0; while(v+1<W && t[v+1]<y) v++; return v; }
static inline int Fq_from(int x,int y,int v){ const int *t=tv+(size_t)x*W; while(v>0 && t[v]>=y) v--; return v; } // v is an upper bound
static void setup_rev(void){
    for(int i=0;i<J;i++){ rloIdx[i]=-1; rhiIdx[i]=-1; int lo=0,hi=J+1;
        for(int p=i+1;p<J;p++){ if(tau[p]<tau[i]&&tau[p]>lo){lo=tau[p];rloIdx[i]=p;} if(tau[p]>tau[i]&&tau[p]<hi){hi=tau[p];rhiIdx[i]=p;} } }
    for(int c=1;c<J;c++){ // placed positions J-c..J-1 ; unplaced 0..J-c-1
        nRel[c]=0; minPl[c]=0; maxPl[c]=0;
        for(int p=J-c;p<J;p++){ if(tau[p]==1)minPl[c]=1; if(tau[p]==J)maxPl[c]=1;
            int rel=0; for(int u=0;u<J-c;u++){ if(rloIdx[u]==p||rhiIdx[u]==p) rel=1; }
            if(rel) relPos[c][nRel[c]++]=p; }
    }
}
static int fast_chain(void){
    int Lmax=lis(); W=Lmax+2;
    tv=malloc((size_t)(N+1)*W*sizeof(int)); for(int v=0;v<W;v++) tv[v]=(v==0?-1:N);
    int *runSuf=malloc(W*sizeof(int));
    int cap=4096; State *st=malloc(cap*sizeof(State));
    int best=0;
    for(int xj=0;xj<N;xj++){
        int yj=Y[xj]; int *tvj=tv+(size_t)xj*W;
        for(int v=0;v<W;v++) runSuf[v]=N;
        int ns=0;
        if(xj>=J-1){
        State root; root.cnt=1; root.ys[J-1]=yj; root.ymin=yj; root.ymax=yj; root.vb=1+Fq(xj,yj);
        int rootAlive=1; int Fj_yj=Fq(xj,yj+1);
        for(int x=xj-1;x>=0 && (ns>0||rootAlive);x--){
            int q=Y[x];
            // refresh bounds (F(x,.) decreases as x decreases) and kill
            if(rootAlive){ root.vb=1+Fq_from(x,yj,root.vb-1); if(Fj_yj>=root.vb || runSuf[root.vb]<=yj) rootAlive=0; }
            for(int si=0;si<ns;){ State*S=&st[si]; S->vb=1+Fq_from(x,S->ymin,S->vb-1);
                if(runSuf[S->vb]<=S->ymax || Fq(xj,S->ymax+1)>=S->vb){ st[si]=st[--ns]; } else si++; }
            int nOld=ns;
            for(int si=-1;si<nOld;si++){
                State *S=(si<0)?&root:&st[si]; if(si<0&&!rootAlive) continue;
                int i=J-1-S->cnt; // position to place
                int lo=rloIdx[i]>=0?S->ys[rloIdx[i]]:-1, hi=rhiIdx[i]>=0?S->ys[rhiIdx[i]]:N;
                if(q<=lo||q>=hi) continue;
                int ymin=q<S->ymin?q:S->ymin, ymax=q>S->ymax?q:S->ymax;
                int vb=1+Fq_from(x,ymin,S->vb-1);
                if(runSuf[vb]<=ymax || Fq(xj,ymax+1)>=vb) continue;
                if(i==0){ // completed: value exact = vb (x_min=x, ymin final)
                    if(vb>best)best=vb;
                    for(int v=vb;v>=1&&runSuf[v]>ymax;v--) runSuf[v]=ymax;
                } else {
                    int c=S->cnt+1; State T=*S; T.ys[i]=q; T.cnt=c; T.ymin=ymin; T.ymax=ymax; T.vb=vb;
                    // signature merge
                    int drop=0;
                    for(int k=0;k<ns;k++){ State*U=&st[k]; if(U->cnt!=c) continue; int same=1;
                        for(int r=0;r<nRel[c];r++) if(U->ys[relPos[c][r]]!=T.ys[relPos[c][r]]){same=0;break;}
                        if(!same) continue;
                        int Udom=1, Tdom=1; // U dominates T?  T dominates U?
                        if(minPl[c]){ if(U->ymin<T.ymin)Udom=0; if(T.ymin<U->ymin)Tdom=0; }
                        if(maxPl[c]){ if(U->ymax>T.ymax)Udom=0; if(T.ymax>U->ymax)Tdom=0; }
                        if(Udom){drop=1;break;}
                        if(Tdom){ *U=T; drop=1; break; }   // replace (T may dominate others too; harmless)
                    }
                    if(drop) continue;
                    if(ns>=cap){cap*=2;st=realloc(st,cap*sizeof(State));}
                    st[ns++]=T;
                }
            }
        }
        }
        int *tvn=tv+(size_t)(xj+1)*W; for(int v=0;v<W;v++){ int a=tvj[v], b=runSuf[v]; tvn[v]= a<b?a:b; }
    }
    free(tv); free(runSuf); free(st);
    return best;
}

/* ---------------- brute force ---------------- */
typedef struct { int xmin,ymin,xmax,ymax; } Copy;
static Copy *cp; static int ncp, capcp;
static int sel[12];
static void dfs(int i,int from){
    if(i==J){ int ymin=N,ymax=-1; for(int t=0;t<J;t++){int y=Y[sel[t]]; if(y<ymin)ymin=y; if(y>ymax)ymax=y;}
        if(ncp>=capcp){capcp*=2;cp=realloc(cp,capcp*sizeof(Copy));}
        cp[ncp].xmin=sel[0];cp[ncp].xmax=sel[J-1];cp[ncp].ymin=ymin;cp[ncp].ymax=ymax;ncp++; return; }
    for(int x=from;x<N;x++){
        int q=Y[x]; int lo=loIdx[i]>=0?Y[sel[loIdx[i]]]:-1, hi=hiIdx[i]>=0?Y[sel[hiIdx[i]]]:N;
        if(q>lo && q<hi){ sel[i]=x; dfs(i+1,x+1); }
    }
}
static int cmpc(const void*a,const void*b){ return ((Copy*)a)->xmax-((Copy*)b)->xmax; }
static int bf_chain(void){
    capcp=1024; cp=malloc(capcp*sizeof(Copy)); ncp=0; dfs(0,0);
    qsort(cp,ncp,sizeof(Copy),cmpc);
    int *val=malloc(ncp*sizeof(int)); int best=0;
    for(int i=0;i<ncp;i++){ int v=1;
        for(int k=0;k<i;k++) if(cp[k].xmax<cp[i].xmin && cp[k].ymax<cp[i].ymin && val[k]+1>v) v=val[k]+1;
        val[i]=v; if(v>best)best=v; }
    free(val); free(cp); return best;
}

int main(int argc,char**argv){
    int bf=0, a=1; if(argc>1 && strcmp(argv[1],"-bf")==0){bf=1;a=2;}
    if(argc<a+4){fprintf(stderr,"usage: tchain [-bf] N reps tau seed\n");return 1;}
    N=atoi(argv[a]); int reps=atoi(argv[a+1]); const char*ts=argv[a+2]; int seed=atoi(argv[a+3]);
    rs = 0x1234567ULL + (uint64_t)seed*0xD1B54A32D192ED03ULL;
    setup_tau(ts); setup_rev();
    Y=malloc(N*sizeof(int));
    for(int r=0;r<reps;r++){
        gen_perm();
        int L = bf? bf_chain() : fast_chain();
        printf("%d %s %d %d %d\n",N,ts,seed*100000+r,L,lis());
    }
    return 0;
}
