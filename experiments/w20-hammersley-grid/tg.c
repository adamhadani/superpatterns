// tg.c — containment of the tilted grid pi(i*r+j) = j*h+i (k = r*h; r strips/columns, h slabs/rows) in N
// uniform points.  Exact Pareto-front DP over the x-order; FIXED (equal strips of height 1/r, state
// l_0..l_{r-1}) or FREE (state l_0..l_{r-1}, f_1..f_{r-1}; f_j = y of the first point of column j).
// A beam limit B (0 = exact) truncates each front to its B states with smallest sum(l) (FREE: sum(l)-sum(f)):
// then "found" is still a certificate, but "not found" may be wrong; the third count is the number of
// truncated-and-not-found samples.  Optional -tau eps: random perturbation of the row order (family F(r,h,eps)),
// resampled per sample.  usage: tg r h N reps seed [-free] [-beam B] [-tau eps]
// output: r h N reps found exact_notfound unknown
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static uint64_t rs;
static inline uint64_t rng(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static int R,H,K,N,FREE,DIM,BEAM,IID;
typedef struct { int *v; int n, cap; } Front;
static Front *fr; static int *Y; static int *strip; static int *tau; // tau[i*R+s] = strip of s-th point of row i
static inline int dom(const int*a,const int*b){ // a dominates b (a at least as good)
    for(int d=0;d<R;d++) if(a[d]>b[d]) return 0;
    for(int d=R;d<DIM;d++) if(a[d]<b[d]) return 0;
    return 1;
}
static long truncated;
static void insert(Front*F,const int*s){
    int *base=F->v;
    for(int q=0;q<F->n;q++) if(dom(base+q*DIM,s)) return;
    int w=0; for(int q=0;q<F->n;q++){ if(!dom(s,base+q*DIM)){ if(w!=q) memcpy(base+w*DIM,base+q*DIM,DIM*sizeof(int)); w++; } }
    F->n=w;
    if(F->n==F->cap){ F->cap=F->cap?2*F->cap:16; F->v=realloc(F->v,(size_t)F->cap*DIM*sizeof(int)); base=F->v; }
    memcpy(base+F->n*DIM,s,DIM*sizeof(int)); F->n++;
}
static int score(const int*s){ int t=0; for(int d=0;d<R;d++) t+=s[d]; for(int d=R;d<DIM;d++) t-=s[d]; return t; }
static int cmpsc(const void*a,const void*b){ return score((const int*)a)-score((const int*)b); }
static void prune(Front*F){ if(BEAM&&F->n>BEAM){ qsort(F->v,F->n,DIM*sizeof(int),cmpsc); F->n=BEAM; truncated=1; } }
static int *tmp; static Front *add;
// brute force: DFS embedding of pi_tau (pi[t] = tau[t]*H + t/R, 0-indexed values) into Y, with/without strip constraint
static int pi_[4096]; static int chosen[4096];
static int dfs(int t,int lastx,int fixedmode){
    if(t==K) return 1;
    for(int x=lastx+1;x<=N-(K-t);x++){
        int y=Y[x]; if(fixedmode && strip[x]!=tau[t]) continue;
        int okk=1; for(int u=0;u<t && okk;u++){ if((pi_[u]<pi_[t]) != (Y[chosen[u]]<y)) okk=0; }
        if(!okk) continue; chosen[t]=x; if(dfs(t+1,x,fixedmode)) return 1;
    }
    return 0;
}

int main(int argc,char**argv){
    if(argc<6){fprintf(stderr,"usage: tg r h N reps seed [-free] [-beam B] [-tau eps]\n");return 1;}
    R=atoi(argv[1]);H=atoi(argv[2]);N=atoi(argv[3]);int reps=atoi(argv[4]); rs=0x1234567ULL+(uint64_t)atoi(argv[5])*0xD1B54A32D192ED03ULL;
    FREE=0;BEAM=0;double eps=0;
    int BF=0; for(int a=6;a<argc;a++){ if(!strcmp(argv[a],"-bf"))BF=1; else if(!strcmp(argv[a],"-free"))FREE=1; else if(!strcmp(argv[a],"-iid"))IID=1; else if(!strcmp(argv[a],"-beam"))BEAM=atoi(argv[++a]); else if(!strcmp(argv[a],"-tau"))eps=atof(argv[++a]); }
    K=R*H; DIM=FREE?2*R-1:R;
    fr=calloc(K+1,sizeof(Front)); add=calloc(K+1,sizeof(Front)); tmp=malloc(DIM*sizeof(int));
    Y=malloc(N*sizeof(int)); strip=malloc(N*sizeof(int)); tau=malloc(K*sizeof(int));
    int found=0,notf=0,unk=0;
    for(int rep=0;rep<reps;rep++){
        for(int i=0;i<N;i++)Y[i]=i; for(int i=N-1;i>0;i--){int j=(int)(rng()%(uint64_t)(i+1));int t=Y[i];Y[i]=Y[j];Y[j]=t;}
        for(int i=0;i<N;i++) strip[i]=IID?(int)(rng()%(uint64_t)R):(int)(((long)Y[i]*R)/N);
        for(int i=0;i<H;i++){ for(int s=0;s<R;s++) tau[i*R+s]=s; int m=(int)(eps*R+0.5);
            if(m>=2){ int pos[64]; for(int t=0;t<m;t++){int again;do{pos[t]=(int)(rng()%R);again=0;for(int q=0;q<t;q++)if(pos[q]==pos[t])again=1;}while(again);}
                int first=tau[i*R+pos[0]]; for(int t=0;t<m-1;t++) tau[i*R+pos[t]]=tau[i*R+pos[t+1]]; tau[i*R+pos[m-1]]=first; } }
        for(int t=0;t<=K;t++){fr[t].n=0;add[t].n=0;}
        // level 0: one empty state: l = -1, f = +inf (N)
        for(int d=0;d<R;d++)tmp[d]=-1; for(int d=R;d<DIM;d++)tmp[d]=N; insert(&fr[0],tmp);
        truncated=0; int ok=0;
        for(int x=0;x<N && !ok;x++){
            int y=Y[x];
            for(int t=0;t<K;t++){
                if(!fr[t].n) continue;
                int i=t/R, s=t%R, j=tau[t]; // point goes to column j (strip j)
                if(!FREE && strip[x]!=j) continue;
                for(int q=0;q<fr[t].n;q++){
                    const int*st=fr[t].v+q*DIM;
                    if(y<=st[j]) continue;                      // column chain (st[j] = -1 if column j is empty)
                    if(FREE){ int bad=0;
                        for(int jj=0;jj<j;jj++) if(st[jj]>=y) bad=1;            // above every point of lower columns
                        for(int jj=j+1;jj<R && !bad;jj++) if(y>=st[R+jj-1]) bad=1; // below the first (=lowest) point of higher columns
                        if(bad) continue; }
                    memcpy(tmp,st,DIM*sizeof(int)); tmp[j]=y; if(FREE && i==0 && j>0) tmp[R+j-1]=y;
                    insert(&add[t+1],tmp);
                }
            }
            for(int t=1;t<=K;t++) if(add[t].n){ for(int q=0;q<add[t].n;q++) insert(&fr[t],add[t].v+q*DIM); add[t].n=0; prune(&fr[t]); }
            if(fr[K].n) ok=1;
        }
        if(ok) found++; else if(truncated) unk++; else notf++;
        if(BF){ for(int t=0;t<K;t++) pi_[t]=tau[t]*H+t/R; int b=dfs(0,-1,!FREE); if(b!=ok){ printf("MISMATCH rep %d dp=%d bf=%d\n",rep,ok,b); } }
    }
    printf("%d %d %d %d %d %d %d\n",R,H,N,reps,found,notf,unk);
    return 0;
}
