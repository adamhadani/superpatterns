// gg.c — general greedy embeddings of a pattern pi in a Poisson process of intensity N = C k^2 on [0,1]^2.
//
// modes (argv[1]):
//   rows       k C reps seed            rigid rows of height 1/k, leftmost point in row pi(p) right of the x-level (any pi)
//   runs       k C reps seed L          strips = maximal monotone value-runs of pi^{-1}; runs of length >= L use the
//                                       corner rule (lower corner for up-runs, upper corner for down-runs), shorter runs
//                                       are split into rigid rows.  pi uniformly random.  L=0: all rigid rows.
//   verbatim   k C reps seed r          equal strips of h=k/r values, corner rule, ignoring monotonicity (the false
//                                       "verbatim" claim): counts how often the output is NOT a copy of pi.
//   grid       k C reps seed r delta    block-grid pi_tau (random tau_i), rigid strips, free slabs, x-offset delta/k
//                                       after every point, phase-2 repair of bad columns through the boxes
//                                       (x(i,j)+V/k, x(i,j)+(V+delta)/k) x S_j (lowest point above the level); the
//                                       x-level advances by (V+delta)/k past each point so that boxes avoid explored triangles.
// For every found copy an O(k^2) order-isomorphism check is performed ("noncopy" counts violations).
// "thm" = the event of the theorem (extended-process minimiser inside its region at every step); "prac" = the
// practical run (search restricted to the region inside the square) produced a copy.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static unsigned long long rs;
static inline unsigned long long rng(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static inline double unif(void){ return (rng()>>11)*(1.0/9007199254740992.0); }
static int poisson(double lam){ // simple for lam up to ~1e5: normal approx not needed, use inversion in blocks
    int n=0; double L=lam;
    while(L>500){ double x=0; for(int i=0;i<500;i++) x-=log(1-unif()); if(x>1) break; n+=500; L-=500; } // crude; fine
    // exact for the remainder via exponential waiting times
    double t=-log(1-unif()); while(t<=L){ n++; t+=-log(1-unif()); }
    return n;
}

static int K; static double Cc, Nn;
static int npts; static double *PX,*PY; // sorted by x
static int cmpx(const void*a,const void*b){ double d=PX[*(const int*)a]-PX[*(const int*)b]; return d<0?-1:d>0; }
static void gen_points(void){
    // exact Poisson(N) count: sum of exponentials
    int n=0; double t=-log(1-unif()); while(t<=Nn){ n++; t+=-log(1-unif()); }
    npts=n;
    double *tx=malloc(n*sizeof(double)),*ty=malloc(n*sizeof(double)); int *idx=malloc(n*sizeof(int));
    for(int i=0;i<n;i++){ tx[i]=unif(); ty[i]=unif(); idx[i]=i; }
    PX=tx; qsort(idx,n,sizeof(int),cmpx);
    double *sx=malloc(n*sizeof(double)),*sy=malloc(n*sizeof(double));
    for(int i=0;i<n;i++){ sx[i]=tx[idx[i]]; sy[i]=ty[idx[i]]; }
    free(tx);free(ty);free(idx); PX=sx; PY=sy;
}
static int first_after(double a){ int lo=0,hi=npts; while(lo<hi){int m=(lo+hi)/2; if(PX[m]>a) hi=m; else lo=m+1;} return lo; }

// corner search: region x>a, x<1, ylo<y<yhi; minimise (x-a)+ (dir>0 ? (y-ylo) : (yhi-y)).
// returns index or -1; *thm_ok set to 0 if the extended minimiser would lie outside the region.
static double LAM=1.0;
static int corner(double a,double ylo,double yhi,int dir,int*thm_ok){
    int best=-1; double bt=1e9;
    for(int i=first_after(a); i<npts; i++){
        double dx=PX[i]-a; if(dx>=bt) break;
        double y=PY[i]; if(y<=ylo||y>=yhi) continue;
        double t=dx+LAM*(dir>0? y-ylo : yhi-y); if(t<bt){bt=t;best=i;}
    }
    if(best<0){ *thm_ok=0; return -1; }
    // outside area of the triangle {u,v>0,u+v<bt} beyond v<tb (height of region) or u<xa (=1-a)
    double tb=yhi-ylo, xa=1-a, t=bt;
    #define SQ(z) ((z)>0?(z)*(z)/2:0.0)
    double inside=SQ(t)-SQ(t-tb)-SQ(t-xa)+SQ(t-tb-xa); if(LAM!=1.0) inside=SQ(t); /* thm event only meaningful for lam=1 */
    double outside=SQ(t)-inside;
    if(outside>0 && unif()<1-exp(-Nn*outside)) *thm_ok=0;
    return best;
}
// row search: leftmost point with x>a, ylo<y<yhi
static int leftmost(double a,double ylo,double yhi){
    for(int i=first_after(a); i<npts; i++){ double y=PY[i]; if(y>ylo&&y<yhi) return i; }
    return -1;
}
static int is_copy(const int*pi,const int*ch){
    for(int p=0;p<K;p++) if(ch[p]<0) return 0;
    for(int p=0;p<K;p++) for(int q=p+1;q<K;q++){
        if(PX[ch[p]]>=PX[ch[q]]) return 0;
        if((PY[ch[p]]<PY[ch[q]])!=(pi[p]<pi[q])) return 0;
    }
    return 1;
}
static void random_perm(int*pi,int n){ for(int i=0;i<n;i++)pi[i]=i; for(int i=n-1;i>0;i--){int j=rng()%(i+1);int t=pi[i];pi[i]=pi[j];pi[j]=t;} }

int main(int argc,char**argv){
    if(argc<6){fprintf(stderr,"usage: gg mode k C reps seed [extra]\n");return 1;}
    const char*mode=argv[1]; K=atoi(argv[2]); Cc=atof(argv[3]); int reps=atoi(argv[4]);
    rs=0x9E3779B97F4A7C15ULL*(unsigned long long)(atoi(argv[5])+1); for(int i=0;i<10;i++)rng();
    Nn=Cc*(double)K*K;
    int *pi=malloc(K*sizeof(int)),*pinv=malloc(K*sizeof(int)),*ch=malloc(K*sizeof(int));
    int prac=0,thm=0,noncopy=0; double xsum=0; long nsteps=0;
    if(!strcmp(mode,"rows")){
        for(int rep=0;rep<reps;rep++){
            gen_points(); random_perm(pi,K);
            double a=0; int ok=1;
            for(int p=0;p<K&&ok;p++){ int i=leftmost(a,(double)pi[p]/K,(double)(pi[p]+1)/K); if(i<0){ok=0;break;} ch[p]=i; a=PX[i]; }
            if(ok){ if(is_copy(pi,ch)) {prac++;thm++;} else noncopy++; }
            free(PX);free(PY);
        }
        printf("rows k=%d C=%g reps=%d success=%d thm=%d noncopy=%d  bound=Pr(Poisson(Ck)<=k-1)\n",K,Cc,reps,prac,thm,noncopy);
    } else if(!strcmp(mode,"runs")||!strcmp(mode,"verbatim")){
        int L=argc>6?atoi(argv[6]):2; int verb=!strcmp(mode,"verbatim"); int r=verb?L:0; int variant=argc>7?atoi(argv[7]):0; double beta=argc>8?atof(argv[8]):0; LAM=argc>9?atof(argv[9]):1.0; double sumx=0, sumx2=0; int *left=malloc(K*sizeof(int));
        int *runlo=malloc(K*sizeof(int)),*runhi=malloc(K*sizeof(int)),*rundir=malloc(K*sizeof(int)),*runof=malloc(K*sizeof(int));
        double *lev=malloc(K*sizeof(double));
        long totruns=0, totcorner=0; int stripfail=0, xfail=0;
        for(int rep=0;rep<reps;rep++){
            gen_points(); random_perm(pi,K); for(int p=0;p<K;p++) pinv[pi[p]]=p;
            int nr=0;
            if(verb){ int h=K/r; for(int j=0;j<r;j++){ runlo[j]=j*h; runhi[j]=(j+1)*h-1; rundir[j]=+1; for(int v=j*h;v<(j+1)*h;v++) runof[v]=j; } nr=r; }
            else {
                int v=0;
                while(v<K){
                    int s=v, e=v, dir=0;
                    while(e+1<K){ int d = pinv[e+1]>pinv[e] ? +1 : -1; if(dir==0) dir=d; if(d!=dir) break; e++; }
                    if(dir==0) dir=+1;
                    if(e-s+1>=L && L>0){ runlo[nr]=s; runhi[nr]=e; rundir[nr]=dir; for(int u=s;u<=e;u++) runof[u]=nr; nr++; }
                    else { for(int u=s;u<=e;u++){ runlo[nr]=u; runhi[nr]=u; rundir[nr]=0; runof[u]=nr; nr++; } }
                    v=e+1;
                }
            }
            for(int j=0;j<nr;j++){ totruns++; if(rundir[j]) totcorner+=runhi[j]-runlo[j]+1; lev[j]= rundir[j]>=0 ? (double)runlo[j]/K : (double)(runhi[j]+1)/K; left[j]=runhi[j]-runlo[j]+1; }
            double a=0; int ok=1, tok=1;
            for(int p=0;p<K;p++){
                int j=runof[pi[p]]; double lo=(double)runlo[j]/K, hi=(double)(runhi[j]+1)/K; int i;
                if(rundir[j]==0){ i=leftmost(a,lo,hi); if(i<0) tok=0; }
                else if(variant && left[j]==1){ if(rundir[j]>0) i=leftmost(a,lev[j],hi); else i=leftmost(a,lo,lev[j]); }
                else if(rundir[j]>0){ int t=1; i=corner(a,lev[j],hi-beta*(left[j]-1)/K,+1,&t); if(!t) tok=0; if(i>=0) lev[j]=PY[i]; }
                else { int t=1; i=corner(a,lo+beta*(left[j]-1)/K,lev[j],-1,&t); if(!t) tok=0; if(i>=0) lev[j]=PY[i]; }
                left[j]--;
                if(i<0){ ok=0; xsum+=K*(1-a); break; }
                xsum+=K*(PX[i]-a); ch[p]=i; a=PX[i];
            }
            if(ok){ if(is_copy(pi,ch)){ prac++; if(tok) thm++; } else noncopy++; }
            free(PX);free(PY);
        }
        printf("%s beta=%g lam=%g k=%d C=%g reps=%d L=%d var=%d success=%d thm=%d noncopy=%d avg#strips=%.1f avg#corner-values=%.1f meanX/value=%.4f\n",mode,beta,LAM,K,Cc,reps,L,variant,prac,thm,noncopy,(double)totruns/reps,(double)totcorner/reps,xsum/((double)reps*K));
    } else if(!strcmp(mode,"grid")){
        int r=atoi(argv[6]); double delta=argc>7?atof(argv[7]):0; int h=K/r; if(r*h!=K){fprintf(stderr,"r must divide k\n");return 1;}
        int *tau=malloc(K*sizeof(int)); double *lev=malloc(r*sizeof(double)); int *bad=malloc(r*sizeof(int));
        long badcols=0, rescued=0; int xf=0, ph1=0, ph2=0, ph2thm=0; int *ch2=malloc(K*sizeof(int)); double *xcell=malloc(K*sizeof(double));
        for(int rep=0;rep<reps;rep++){
            gen_points();
            for(int i=0;i<h;i++){ random_perm(tau+i*r,r); for(int s=0;s<r;s++) pi[i*r+s]=tau[i*r+s]*h+i; }
            for(int j=0;j<r;j++){ lev[j]=(double)j/r; bad[j]=0; }
            double a=0; int tok=1, xok=1;
            for(int p=0;p<K;p++){
                int j=tau[p]; int t=1; double top=(double)(j+1)/r;
                // phase 1 search in the strip's process: emulate extension by searching the whole quadrant (any y>lev) inside
                // the square, and marking the column bad if the point is outside the strip
                int i=corner(a,lev[j],1.0,+1,&t);
                if(i<0){ xok=0; ch[p]=-1; break; }
                if(PY[i]>=top) bad[j]=1; if(!t) tok=0;
                double Vp=PY[i]-lev[j]; ch[p]=i; lev[j]=PY[i]; xcell[p]=PX[i]+Vp; a=PX[i]+Vp+delta/K; /* box starts beyond the explored triangle */
                if(a>=1){ xok=0; break; }
            }
            if(!xok){ xf++; free(PX);free(PY); continue; }
            int nb=0; for(int j=0;j<r;j++) nb+=bad[j]; badcols+=nb;
            if(nb==0){ if(is_copy(pi,ch)) {ph1++; if(tok) ph2thm++;} else noncopy++; free(PX);free(PY); continue; }
            // phase 2: for bad columns, chain through boxes [x(i,j), x(i,j)+delta/K] x S_j
            int allok=1;
            for(int j=0;j<r&&allok;j++){ if(!bad[j]) continue;
                double b=(double)j/r, top=(double)(j+1)/r; int colok=1;
                for(int i=0;i<h;i++){ // find position p of cell (i,j)
                    int p=-1; for(int s=0;s<r;s++) if(tau[i*r+s]==j){p=i*r+s;break;}
                    double x0=xcell[p], x1=x0+delta/K; int best=-1; double by=2;
                    for(int q=first_after(x0); q<npts && PX[q]<x1; q++){ double y=PY[q]; if(y>b&&y<top&&y<by){by=y;best=q;} }
                    if(best<0){colok=0;break;} ch[p]=best; b=by;
                }
                if(colok) rescued++; else allok=0;
            }
            if(allok){ if(is_copy(pi,ch)){ ph2++; } else noncopy++; }
            free(PX);free(PY);
        }
        printf("grid k=%d r=%d h=%d C=%g delta=%g reps=%d xfail=%d ok_phase1=%d ok_after_phase2=%d thm1=%d badcols=%ld rescued=%ld noncopy=%d\n",K,r,h,Cc,delta,reps,xf,ph1,ph1+ph2,ph2thm,badcols,rescued,noncopy);
    }
    return 0;
}
