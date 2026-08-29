// simulated annealing for rosaries: ./rossa n r seed [iters]
#define NOMAIN
#include "roscheck.c"
#include <math.h>
#include <time.h>
int main(int argc,char**argv){
  int nn=atoi(argv[1]), rr=atoi(argv[2]); unsigned seed=atoi(argv[3]); long iters=argc>4?atol(argv[4]):2000000;
  srand(seed); quiet=1; int ww[512];
  // init: LZ-like: (1..n) repeated then descending
  for(int i=0;i<rr;i++) ww[i]=rand()%nn+1;
  long cur=check(nn,rr,ww), best=cur; double T=2.0;
  for(long it=0;it<iters && cur>0;it++){
    int i=rand()%rr, old=ww[i]; int mv=rand()%3;
    int j=rand()%rr, oldj=ww[j];
    if(mv==0) ww[i]=rand()%nn+1;
    else if(mv==1){ ww[i]=oldj; ww[j]=old; }
    else { // shift segment
      ww[i]=rand()%nn+1; ww[j]=rand()%nn+1; }
    long c=check(nn,rr,ww);
    if(c<=cur || exp((cur-c)/T) > (double)rand()/RAND_MAX){ cur=c; if(c<best){best=c; fprintf(stderr,"it=%ld best=%ld T=%.3f\n",it,best,T);} }
    else { ww[i]=old; ww[j]=oldj; }
    T*=0.99999; if(T<0.05)T=0.05;
  }
  printf("n=%d r=%d final missing=%ld word=",nn,rr,cur); for(int i=0;i<rr;i++)printf("%d%s",ww[i],i<rr-1?",":"\n");
  return cur?1:0;
}
