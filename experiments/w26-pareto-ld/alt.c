// alt.c — alternating-colour LIS in N iid uniform points with iid colours {0,1}.
// usage: alt k C reps seed  -> prints k N C reps  #(altLIS<k)  mean altLIS  mean frac generators (minimal elements of level classes)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static unsigned long long rs; static inline unsigned long long rng(void){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
int main(int argc,char**argv){
  int k=atoi(argv[1]); double C=atof(argv[2]); int reps=atoi(argv[3]); rs=0x9E3779B97F4A7C15ULL*(atoi(argv[4])+1);
  int N=(int)(C*k*k+0.5);
  int *Y=malloc(N*sizeof(int)),*col=malloc(N*sizeof(int)),*lam=malloc(N*sizeof(int));
  int *fw0=malloc((N+1)*sizeof(int)),*fw1=malloc((N+1)*sizeof(int));
  int *minl=malloc(2*(N+2)*sizeof(int)); // for generator count: per (colour,level) track... use O(N k)? instead: p is minimal in its class iff no q<p same colour same level; use fenwick of max level per colour: minimal iff max λ over same-colour q<p is < λ(p)
  int *gw0=malloc((N+1)*sizeof(int)),*gw1=malloc((N+1)*sizeof(int));
  long absent=0; double sumL=0, sumG=0;
  for(int rep=0;rep<reps;rep++){
    for(int i=0;i<N;i++)Y[i]=i; for(int i=N-1;i>0;i--){int j=rng()%(i+1);int t=Y[i];Y[i]=Y[j];Y[j]=t;}
    for(int i=0;i<N;i++)col[i]=rng()&1;
    memset(fw0,0,(N+1)*sizeof(int));memset(fw1,0,(N+1)*sizeof(int));memset(gw0,0,(N+1)*sizeof(int));memset(gw1,0,(N+1)*sizeof(int));
    int L=0; long gen=0;
    for(int i=0;i<N;i++){
      int y=Y[i]+1; int c=col[i]; int *fo=c?fw0:fw1, *fs=c?fw1:fw0, *gs=c?gw1:gw0;
      int m=0; for(int j=y-1;j>0;j-=j&-j) if(fo[j]>m)m=fo[j];
      int l=m+1; lam[i]=l; if(l>L)L=l;
      int ms=0; for(int j=y-1;j>0;j-=j&-j) if(gs[j]>ms)ms=gs[j];
      if(ms<l) gen++;   // no same-colour point below-left with level >= l (levels monotone within colour, so ms<=l always)
      for(int j=y;j<=N;j+=j&-j){ if(fs[j]<l)fs[j]=l; if(gs[j]<l)gs[j]=l; }
    }
    if(L<k)absent++; sumL+=L; sumG+=(double)gen/N;
  }
  printf("%d %d %.3f %d %ld %.3f %.4f\n",k,N,C,reps,absent,sumL/reps,sumG/reps);
  return 0;
}
