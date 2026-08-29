#include <math.h>
// Longest chain of tau-blocks in n uniform random points: max L with (tau)^{oplus L} contained.
// tau=21: O(n^2 log n) via sweep + Fenwick prefix-max. Generic |tau|=3: enumerate triples, O(n^3 log n).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static uint64_t s=0x9E3779B97F4A7C15ULL; static inline uint64_t rng(){ s^=s<<7; s^=s>>9; return s; }
static int n; static int *y; // points sorted by x = index; y[i] in 0..n-1 = random perm
static int *fen; static void fupd(int i,int v){ for(i++;i<=n;i+=i&-i) if(fen[i]<v) fen[i]=v; }
static int fq(int i){ int r=0; for(i++;i>0;i-=i&-i) if(fen[i]>r) r=fen[i]; return r; } // max over ranks <= i
typedef struct{int xq,yp,d;} Blk; // insertion key: corner (x of last point, y of max point)
static int cmpb(const void*a,const void*b){ return ((Blk*)a)->xq-((Blk*)b)->xq; }
// tau=21 : block (p,q), p<q, y[p]>y[q]; corner=(q, y[p]); query needs prior corners with xq<p and yp<y[q]
static int desc21=1;
int chain21(){
    long cap=(long)n*n/2+n; Blk *B=malloc(cap*sizeof(Blk)); long nb=0;
    memset(fen,0,(n+1)*sizeof(int));
    long ptr=0; int best=0;
    // process p in x order; before computing blocks (p,*), insert all blocks with xq < p
    // blocks sorted by xq only after computed... blocks (p,q) have xq=q>p; insertion order = by q.
    // So maintain heap? Simpler: two passes impossible; use bucket lists by xq.
    int *head=malloc(n*sizeof(int)); for(int i=0;i<n;i++)head[i]=-1; int *nxt=malloc(cap*sizeof(int));
    for(int p=0;p<n;p++){
        // insert blocks with xq == p-1 ... i.e. all with xq<p: bucket p-1
        if(p>0) for(int b=head[p-1];b!=-1;b=nxt[b]) fupd(B[b].yp,B[b].d);
        for(int q=p+1;q<n;q++) if(desc21 ? y[q]<y[p] : y[q]>y[p]){
            int lo=y[q]<y[p]?y[q]:y[p], hi=y[q]<y[p]?y[p]:y[q];
            int d=1+ (lo>0? fq(lo-1):0);
            B[nb].xq=q;B[nb].yp=hi;B[nb].d=d; nxt[nb]=head[q]; head[q]=nb; nb++;
            if(d>best)best=d;
        }
    }
    free(B);free(head);free(nxt); return best;
}
// generic tau of length 3 given as perm t[0..2] (values 1..3): block = points a<b<c (x order) with y-pattern tau
// corner = (c, ymax); previous corner must have x < a and ymax < ymin of this block
int chain3(int t0,int t1,int t2){
    memset(fen,0,(n+1)*sizeof(int));
    // buckets by insertion x=c
    typedef struct{int yp,d;} E; long cap=1000000; E *B=malloc(cap*sizeof(E)); long nb=0;
    int *head=malloc(n*sizeof(int)); for(int i=0;i<n;i++)head[i]=-1; int *nxt=malloc(cap*sizeof(int));
    int best=0;
    for(int a=0;a<n;a++){
        if(a>0) for(int b=head[a-1];b!=-1;b=nxt[b]) fupd(B[b].yp,B[b].d);
        for(int b=a+1;b<n;b++) for(int c=b+1;c<n;c++){
            int ya=y[a],yb=y[b],yc=y[c];
            int ra=1+(ya>yb)+(ya>yc), rb=1+(yb>ya)+(yb>yc), rc=1+(yc>ya)+(yc>yb);
            if(ra!=t0||rb!=t1||rc!=t2) continue;
            int ymin=ya<yb?(ya<yc?ya:yc):(yb<yc?yb:yc), ymax=ya>yb?(ya>yc?ya:yc):(yb>yc?yb:yc);
            int d=1+(ymin>0?fq(ymin-1):0);
            if(nb>=cap){cap*=2;B=realloc(B,cap*sizeof(E));nxt=realloc(nxt,cap*sizeof(int));}
            B[nb].yp=ymax;B[nb].d=d;nxt[nb]=head[c];head[c]=nb;nb++;
            if(d>best)best=d;
        }
    }
    free(B);free(head);free(nxt); return best;
}
int main(int argc,char**argv){
    n=atoi(argv[1]); int reps=atoi(argv[2]); const char*tau=argv[3]; s^=atoi(argv[4])*0x1234567ULL; rng();
    y=malloc(n*sizeof(int)); fen=malloc((n+1)*sizeof(int));
    double sum=0;
    for(int r=0;r<reps;r++){
        for(int i=0;i<n;i++)y[i]=i; for(int i=n-1;i>0;i--){int j=rng()%(i+1);int t=y[i];y[i]=y[j];y[j]=t;}
        desc21 = (tau[0]=='2');
        int L = strlen(tau)==2 ? chain21() : chain3(tau[0]-'0',tau[1]-'0',tau[2]-'0');
        sum+=L;
    }
    double L=sum/reps; int k=strlen(tau);
    printf("tau=%s n=%d reps=%d meanL=%.2f  c=L/sqrt(n)=%.4f  (Alon needs c>=%.4f)  k=|tau|L=%.1f vs 2sqrt(n)=%.1f\n",tau,n,reps,L,L/sqrt((double)n),2.0/k,k*L,2*sqrt((double)n));
}
