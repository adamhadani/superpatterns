// strict LIS of Bernoulli(p) sites on an n x n grid (Seppalainen 1997 check): L/n -> 2 sqrt p/(1+sqrt p)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static unsigned long long rs=88172645463325252ULL; static double u01(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return (rs>>11)*(1.0/9007199254740992.0);}
int main(int argc,char**argv){ int n=atoi(argv[1]); double p=atof(argv[2]); int reps=atoi(argv[3]); rs^=atoll(argv[4]);
  int *best=malloc((n+1)*sizeof(int)); // best[j] = longest chain ending with y-index exactly... use patience over columns
  // process columns x=0..n-1; row set of open sites; strict in both: chain uses distinct columns automatically, distinct rows needed.
  // f[y] = longest chain ending at row y (over columns processed so far). Column x with open rows Y: new f[y] = 1 + max_{y'<y} f[y'] computed from old f. Use prefix max as we go up.
  int *f=malloc((n+1)*sizeof(int)); int *open=malloc(n*sizeof(int));
  double sum=0,sum2=0;
  for(int r=0;r<reps;r++){ for(int y=0;y<=n;y++)f[y]=0; int L=0;
    for(int x=0;x<n;x++){ int m=0; for(int y=0;y<n;y++) if(u01()<p) open[m++]=y;
      int pm=0, yy=0; // scan open rows increasing; prefix max of old f over y'<y
      int *nf=best; // temp values
      for(int i=0;i<m;i++){ int y=open[i]; while(yy<y){ if(f[yy]>pm)pm=f[yy]; yy++; } nf[i]=pm+1; }
      for(int i=0;i<m;i++){ int y=open[i]; if(nf[i]>f[y]) f[y]=nf[i]; if(f[y]>L)L=f[y]; }
    }
    sum+=L; sum2+=(double)L*L; }
  double mean=sum/reps, sd=sqrt(sum2/reps-mean*mean);
  printf("n=%d p=%.3f  E L/n = %.5f (sd %.4f)   Seppalainen 2sqrt(p)/(1+sqrt p) = %.5f\n",n,p,mean/n,sd/n,2*sqrt(p)/(1+sqrt(p)));
}
