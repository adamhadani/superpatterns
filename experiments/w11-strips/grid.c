// grid.c — corner-greedy embedding of block-grid patterns pi_tau (k = r*h) into N uniform points.
// Cells (i,j) = slab i (x in [i/h,(i+1)/h)) x strip j (y in [j/r,(j+1)/r)).  Row i visits strips in the
// order tau_i(0..r-1) (tilted grid: tau_i = id).  In each cell take the point with x > a (x of the previous
// point of the row) and y > b_j (y of the previous point of strip j) minimising phi = r(x-a) + h(y-b_j)
// (mode 1), max(r(x-a),h(y-b_j)) (mode 2), or lexicographic (mode 3: min y then x), with the option (-skip)
// of discarding rows that fail and using H = h+extra slabs instead of h.
// usage: grid r h N reps seed [mode] [-tau eps] [-skip extra]
// output: r h N reps successes
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static uint64_t rs;
static inline uint64_t rng(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double U(void){ return (rng()>>11)*(1.0/9007199254740992.0); }
int main(int argc,char**argv){
    if(argc<6){fprintf(stderr,"usage: grid r h N reps seed [mode] [-tau eps] [-skip extra]\n");return 1;}
    int r=atoi(argv[1]),h=atoi(argv[2]),N=atoi(argv[3]),reps=atoi(argv[4]); rs=0x9E3779B97F4A7C15ULL^((uint64_t)atoi(argv[5])*0xD1B54A32D192ED03ULL+1);
    int mode=1; double eps=0; int extra=0;
    for(int a=6;a<argc;a++){ if(!strcmp(argv[a],"-tau")) eps=atof(argv[++a]); else if(!strcmp(argv[a],"-skip")) extra=atoi(argv[++a]); else mode=atoi(argv[a]); }
    int H=h+extra; int k=r*h;
    // points: N uniform in unit square; slabs have width 1/H
    double *px=malloc(N*sizeof(double)),*py=malloc(N*sizeof(double));
    int *cellstart=malloc((H*r+1)*sizeof(int)),*cnt=malloc(H*r*sizeof(int)),*ord=malloc(N*sizeof(int));
    double *b=malloc(r*sizeof(double)); int *tau=malloc(r*sizeof(int));
    int succ=0;
    for(int rep=0;rep<reps;rep++){
        for(int p=0;p<N;p++){px[p]=U();py[p]=U();}
        memset(cnt,0,H*r*sizeof(int));
        for(int p=0;p<N;p++){ int i=(int)(px[p]*H), j=(int)(py[p]*r); if(i>=H)i=H-1; if(j>=r)j=r-1; cnt[i*r+j]++; }
        cellstart[0]=0; for(int c=0;c<H*r;c++) cellstart[c+1]=cellstart[c]+cnt[c];
        memset(cnt,0,H*r*sizeof(int));
        for(int p=0;p<N;p++){ int i=(int)(px[p]*H), j=(int)(py[p]*r); if(i>=H)i=H-1; if(j>=r)j=r-1; ord[cellstart[i*r+j]+cnt[i*r+j]++]=p; }
        for(int j=0;j<r;j++) b[j]=0;
        int rows=0, ok=1;
        for(int i=0;i<H && rows<h;i++){
            // tau_i: identity with a random derangement-ish perturbation on eps*r letters
            for(int s=0;s<r;s++) tau[s]=s;
            int m=(int)(eps*r+0.5);
            if(m>=2){ // pick m positions, cyclically rotate them (no fixed points among them)
                int *pos=malloc(m*sizeof(int)); for(int t=0;t<m;t++){ int again; do{ pos[t]=(int)(rng()%r); again=0; for(int q=0;q<t;q++) if(pos[q]==pos[t]) again=1; }while(again); }
                int first=tau[pos[0]]; for(int t=0;t<m-1;t++) tau[pos[t]]=tau[pos[t+1]]; tau[pos[m-1]]=first; free(pos);
            }
            double a=0, bnew[64]; int rowok=1;
            for(int s=0;s<r && rowok;s++){
                int j=tau[s]; int c=i*r+j; double best=1e30; int bp=-1;
                double lo=i/(double)H, hi=(i+1)/(double)H; double ylo=j/(double)r;
                for(int q=cellstart[c];q<cellstart[c+1];q++){ int p=ord[q]; double x=(px[p]-lo)*H, y=(py[p]-ylo)*r;
                    if(x<=a||y<=b[j]) continue; double u=r*(x-a), v=h*(y-b[j]); double phi;
                    if(mode==1) phi=u+v; else if(mode==2) phi=(u>v?u:v); else phi=y*1e6+x;
                    if(phi<best){best=phi;bp=p;} }
                if(bp<0){ rowok=0; break; }
                a=(px[bp]-lo)*H; bnew[j]=(py[bp]-ylo)*r;
            }
            if(rowok){ for(int j=0;j<r;j++) b[j]=bnew[j]; rows++; }
            else if(!extra){ ok=0; break; }
        }
        if(ok && rows>=h) succ++;
    }
    printf("%d %d %d %d %d\n",r,h,N,reps,succ);
    return 0;
}
