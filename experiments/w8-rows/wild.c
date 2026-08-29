/* wild: coverage of a word w over [m] under WILDCARD rows: tau embeds iff there is a k-subsequence of w whose
   letters u_1..u_k satisfy  tau_i < tau_j  =>  u_i <= u_j  (equal letters impose nothing: the fibre of a letter
   may carry ANY pattern).  This is the union over all row-pattern choices, hence an UPPER BOUND on the coverage of
   every row-structured permutation with this word (any rho_l).  With -P B the word is B copies of rho.
   usage: wild -k K -n N [-m M] [-P B] [-w "word"] [-s seed] [-i iters]   (SA over words if -i > 0)
   prints covered/k!  and (for -i>0) the best word. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
static int k,n,m,B=0,w[64]; static unsigned char *seen; static long fact[13]; static long cnt;
static int sel[16];          /* letters of the chosen subsequence */
static int val[16];          /* tau values assigned to chosen positions */
static int order[16];        /* indices 0..k-1 sorted by letter (stable) */
static int used[16];
static void mark(void){ long r=0; for(int i=0;i<k;i++){int c=0;for(int j=i+1;j<k;j++) if(val[j]<val[i]) c++; r+=c*fact[k-1-i];} if(!seen[r]){seen[r]=1;cnt++;} }
/* assign values to fibres: positions in 'order' grouped by letter; fibre gets value interval [lo, lo+t) in any order */
static void assign(int idx,int lo){
    if(idx==k){ mark(); return; }
    int t=1; while(idx+t<k && sel[order[idx+t]]==sel[order[idx]]) t++;
    /* enumerate all bijections of the t positions order[idx..idx+t-1] to values lo..lo+t-1 */
    int perm[16]; for(int j=0;j<t;j++) perm[j]=j;
    /* Heap's algorithm iterative would be nicer; recursion is fine for t<=6 */
    int c[16]={0}; int j=0;
    for(int q=0;q<t;q++) val[order[idx+q]]=lo+perm[q]; assign(idx+t,lo+t);
    while(j<t){ if(c[j]<j){ if(j%2==0){int x=perm[0];perm[0]=perm[j];perm[j]=x;} else {int x=perm[c[j]];perm[c[j]]=perm[j];perm[j]=x;}
            for(int q=0;q<t;q++) val[order[idx+q]]=lo+perm[q]; assign(idx+t,lo+t); c[j]++; j=0; } else { c[j]=0; j++; } }
}
static void leaf(void){
    /* stable sort indices by letter */
    for(int i=0;i<k;i++) order[i]=i;
    for(int a=1;a<k;a++){ int x=order[a],b=a-1; while(b>=0 && sel[order[b]]>sel[x]){ order[b+1]=order[b]; b--; } order[b+1]=x; }
    assign(0,0);
}
static void rec(int d,int start){ if(d==k){ leaf(); return; } for(int p=start;p<=n-(k-d);p++){ sel[d]=w[p]; rec(d+1,p+1);} }
static long score(void){ memset(seen,0,fact[k]); cnt=0; rec(0,0); return cnt; }
static unsigned long long rs; static inline unsigned long long rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
int main(int argc,char**argv){ const char*ws=NULL; long iters=0; unsigned long long seed=(unsigned long long)time(NULL)^getpid(); m=0; n=0;
  for(int i=1;i<argc;i++){ if(!strcmp(argv[i],"-k")) k=atoi(argv[++i]); else if(!strcmp(argv[i],"-n")) n=atoi(argv[++i]); else if(!strcmp(argv[i],"-m")) m=atoi(argv[++i]);
    else if(!strcmp(argv[i],"-P")) B=atoi(argv[++i]); else if(!strcmp(argv[i],"-w")) ws=argv[++i]; else if(!strcmp(argv[i],"-s")) seed=strtoull(argv[++i],0,10); else if(!strcmp(argv[i],"-i")) iters=atol(argv[++i]); }
  fact[0]=1; for(int i=1;i<13;i++) fact[i]=fact[i-1]*i; seen=malloc(fact[k]); rs=seed*2654435761ULL+1;
  if(B){ n=m*B; }
  if(ws){ int c=0; const char*s=ws; char*e; while(1){ long v=strtol(s,&e,10); if(e==s) break; w[c++]=(int)v-1; s=e; } if(n==0) n=c; if(c!=n){fprintf(stderr,"len %d != n %d\n",c,n);return 1;} if(m==0){ for(int i=0;i<n;i++) if(w[i]+1>m) m=w[i]+1; } }
  else if(B){ int rho[64]; for(int i=0;i<m;i++) rho[i]=i; for(int i=m-1;i>0;i--){int j=rnd()%(i+1);int t=rho[i];rho[i]=rho[j];rho[j]=t;} for(int b=0;b<B;b++) for(int i=0;i<m;i++) w[b*m+i]=rho[i]; }
  else { for(int p=0;p<n;p++) w[p]=p%m; for(int i=n-1;i>0;i--){int j=rnd()%(i+1);int t=w[i];w[i]=w[j];w[j]=t;} }
  if(getenv("EXH") && B){ /* exhaustive over rho in S_m with rho[0] < rho[m-1] complement symmetry not applied; just all */
    int rho[64]; for(int i=0;i<m;i++) rho[i]=i; int c[64]={0}; long bestx=-1; long tot=0; int bx[64];
    #define SETW for(int b=0;b<B;b++) for(int i=0;i<m;i++) w[b*m+i]=rho[i];
    SETW; { long s=score(); tot++; if(s>bestx){bestx=s; memcpy(bx,rho,sizeof(rho));} }
    int j=0; while(j<m){ if(c[j]<j){ if(j%2==0){int x=rho[0];rho[0]=rho[j];rho[j]=x;} else {int x=rho[c[j]];rho[c[j]]=rho[j];rho[j]=x;}
        SETW; long s=score(); tot++; if(s>bestx){bestx=s; memcpy(bx,rho,sizeof(rho)); fprintf(stderr,"exh %ld: best %ld rho:",tot,bestx); for(int i=0;i<m;i++) fprintf(stderr," %d",bx[i]+1); fprintf(stderr,"\n"); if(bestx==fact[k]) break; }
        c[j]++; j=0; } else { c[j]=0; j++; } }
    printf("EXH k=%d m=%d B=%d tried=%ld best=%ld/%ld rho:",k,m,B,tot,bestx,fact[k]); for(int i=0;i<m;i++) printf(" %d",bx[i]+1); printf("\n"); return 0; }
  long cur=score(), best=cur; int bw[64]; memcpy(bw,w,sizeof(w));
  if(getenv("MISS")){ for(long r=0;r<fact[k];r++) if(!seen[r]){ long x=r; int c[16]; for(int i=0;i<k;i++){ c[i]=x/fact[k-1-i]; x%=fact[k-1-i]; } int av[16]; for(int i=0;i<k;i++) av[i]=i+1; printf("missing:"); for(int i=0;i<k;i++){ int v=av[c[i]]; printf(" %d",v); for(int j=c[i];j<k-1-i;j++) av[j]=av[j+1]; } printf("\n"); } }
  fprintf(stderr,"start k=%d n=%d m=%d B=%d covered=%ld/%ld\n",k,n,m,B,cur,fact[k]);
  double T0=3.0,T1=0.2;
  for(long it=0; it<iters && best<fact[k]; it++){
    double T=T0*pow(T1/T0,(double)it/iters); int save[64]; memcpy(save,w,sizeof(w));
    if(B){ int a=rnd()%m,b=rnd()%m; if(a==b) continue; for(int bb=0;bb<B;bb++){int x=w[bb*m+a];w[bb*m+a]=w[bb*m+b];w[bb*m+b]=x;} }
    else { int p=rnd()%n,q; if(rnd()&1){ q=p+1; if(q>=n) continue; } else q=rnd()%n; if(w[p]==w[q]) continue; int x=w[p];w[p]=w[q];w[q]=x; }
    long s=score();
    if(s>=cur || exp((s-cur)/T)*4294967296.0 > (double)(rnd()&0xffffffff)){ cur=s; if(s>best){ best=s; memcpy(bw,w,sizeof(w)); fprintf(stderr,"it %ld best %ld/%ld:",it,best,fact[k]); for(int i=0;i<n;i++) fprintf(stderr," %d",bw[i]+1); fprintf(stderr,"\n"); } }
    else memcpy(w,save,sizeof(w));
  }
  printf("WILD k=%d n=%d m=%d B=%d best=%ld/%ld word:",k,n,m,B,best,fact[k]); for(int i=0;i<n;i++) printf(" %d",bw[i]+1); printf("\n"); return best!=fact[k]; }
