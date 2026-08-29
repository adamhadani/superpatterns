// contain.c — exact containment test of a fixed (+)-decomposable pattern pi in N uniform random points (W10 task 4).
// pi = B_1 (+) B_2 (+) ... (+) B_r (blocks = (+)-indecomposable components).  Staircase DP:
//   S_0 = {(-1,-1)};  S_i = Pareto-minimal (x_max,y_max) over copies C of B_i whose SW corner (x_min,y_min) strictly
//   dominates some point of S_{i-1}.  pi is contained iff S_r nonempty.  (Exact: a copy of pi is a sequence of block copies
//   with strictly increasing boxes, and only Pareto-minimal corners matter for what can follow.)
// usage: contain N reps seed "pi as space-separated values"      -> prints "N k reps count fraction"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static uint64_t rs; static inline uint64_t rng(void){ uint64_t z=(rs+=0x9E3779B97F4A7C15ULL); z=(z^(z>>30))*0xBF58476D1CE4E5B9ULL; z=(z^(z>>27))*0x94D049BB133111EBULL; return z^(z>>31); }
static int N,K; static int pi[64]; static int *Y;
static int nb, bstart[64], blen[64];
typedef struct{int x,y;} Pt;
static Pt *S,*S2; static int nS,nS2;
static int cur[64]; static int bs, bl; static int blo[64], bhi[64]; // current block gap indices
static int cmp(const void*a,const void*b){ const Pt*p=a,*q=b; return p->x!=q->x? p->x-q->x : p->y-q->y; }
static int corner_ok(int xmin,int ymin){ // exists s in S with s.x<xmin, s.y<ymin ; S sorted by x asc (y desc)
    int lo=0,hi=nS-1,best=-1; while(lo<=hi){int m=(lo+hi)/2; if(S[m].x<xmin){best=m;lo=m+1;} else hi=m-1;}
    return best>=0 && S[best].y<ymin; }
static int *bestY; // bestY[x] = min y_max over copies of the current block with x_max = x
static void addS2(int x,int y){ if(y<bestY[x]){ bestY[x]=y; nS2++; } }
static void dfs(int i,int from,int ymin,int ymax){
    if(i==bl){ addS2(cur[bl-1], ymax); return; }
    for(int x=from;x<N;x++){ int q=Y[x];
        int lo=blo[i]>=0?Y[cur[blo[i]]]:-1, hi=bhi[i]>=0?Y[cur[bhi[i]]]:N;
        if(q<=lo||q>=hi) continue;
        int nmin=q<ymin?q:ymin, nmax=q>ymax?q:ymax;
        if(i==0){ if(!corner_ok(x,q)) continue; } // block's ymin is fixed only at the end; prune with the partial min below
        else if(!corner_ok(cur[0],nmin)) continue;
        cur[i]=x; dfs(i+1,x+1,nmin,nmax);
    }
}
static int nlo[64],nhi[64],bsel[64];
static int naive(int i,int from){ if(i==K) return 1;
    for(int x=from;x<N;x++){ int q=Y[x]; int lo=nlo[i]>=0?Y[bsel[nlo[i]]]:-1, hi=nhi[i]>=0?Y[bsel[nhi[i]]]:N;
        if(q>lo&&q<hi){ bsel[i]=x; if(naive(i+1,x+1)) return 1; } } return 0; }
static int contained_bf(void){ for(int i=0;i<K;i++){ nlo[i]=-1;nhi[i]=-1;int lo=0,hi=K+1; for(int p=0;p<i;p++){ if(pi[p]<pi[i]&&pi[p]>lo){lo=pi[p];nlo[i]=p;} if(pi[p]>pi[i]&&pi[p]<hi){hi=pi[p];nhi[i]=p;} } } return naive(0,0); }
static int contained(void){
    nS=1; S[0].x=-1; S[0].y=-1;
    for(int b=0;b<nb;b++){
        bs=bstart[b]; bl=blen[b];
        for(int i=0;i<bl;i++){ blo[i]=-1;bhi[i]=-1; int lo=0,hi=K+1;
            for(int p=0;p<i;p++){ int v=pi[bs+p]; if(v<pi[bs+i]&&v>lo){lo=v;blo[i]=p;} if(v>pi[bs+i]&&v<hi){hi=v;bhi[i]=p;} } }
        nS2=0; for(int x=0;x<N;x++) bestY[x]=N; dfs(0,0,N,-1);
        if(nS2==0) return 0;
        nS=0; int by=N; for(int x=0;x<N;x++){ if(bestY[x]<by){ S[nS].x=x; S[nS].y=bestY[x]; nS++; by=bestY[x]; } }
    }
    return 1;
}
int main(int argc,char**argv){
    int bf=0; if(argc>1&&strcmp(argv[1],"-bf")==0){bf=1;argv++;argc--;}
    if(argc<5){fprintf(stderr,"usage: contain [-bf] N reps seed \"pi\"\n");return 1;}
    N=atoi(argv[1]); int reps=atoi(argv[2]); rs=0x1234567ULL+(uint64_t)atoi(argv[3])*0xD1B54A32D192ED03ULL;
    K=0; { char*s=strdup(argv[4]); for(char*t=strtok(s," ");t;t=strtok(NULL," ")) pi[K++]=atoi(t); }
    // blocks
    nb=0; int mx=0,st=0; for(int i=0;i<K;i++){ if(pi[i]>mx)mx=pi[i]; if(mx==i+1){ bstart[nb]=st; blen[nb]=i+1-st; nb++; st=i+1; } }
    Y=malloc(N*sizeof(int)); S=malloc((N+8)*sizeof(Pt)); bestY=malloc((N+8)*sizeof(int));
    int cnt=0;
    for(int r=0;r<reps;r++){
        for(int i=0;i<N;i++)Y[i]=i; for(int i=N-1;i>0;i--){int j=(int)(rng()%(uint64_t)(i+1));int t=Y[i];Y[i]=Y[j];Y[j]=t;}
        cnt+= bf? contained_bf() : contained();
    }
    printf("%d %d %d %d %.4f\n",N,K,reps,cnt,(double)cnt/reps);
    return 0;
}
