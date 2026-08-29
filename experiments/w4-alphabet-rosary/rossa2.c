// SA from given initial word: ./rossa2 n seed iters word
#define NOMAIN
#include "roscheck.c"
#include <math.h>
int main(int argc,char**argv){
  int nn=atoi(argv[1]); unsigned seed=atoi(argv[2]); long iters=atol(argv[3]); char*s=argv[4];
  srand(seed); quiet=1; int ww[512]; int rr=0; char*t=strtok(s,","); while(t){ww[rr++]=atoi(t); t=strtok(NULL,",");}
  long cur=check(nn,rr,ww), best=cur; double T=0.5;
  fprintf(stderr,"init missing=%ld\n",cur);
  for(long it=0;it<iters && cur>0;it++){
    int i=rand()%rr, old=ww[i]; int j=rand()%rr, oldj=ww[j]; int mv=rand()%2;
    if(mv==0) ww[i]=rand()%nn+1; else { ww[i]=oldj; ww[j]=old; }
    long c=check(nn,rr,ww);
    if(c<=cur || exp((cur-c)/T) > (double)rand()/RAND_MAX){ cur=c; if(c<best){best=c; fprintf(stderr,"it=%ld best=%ld\n",it,best);} }
    else { ww[i]=old; ww[j]=oldj; }
  }
  printf("n=%d r=%d final missing=%ld word=",nn,rr,cur); for(int i=0;i<rr;i++)printf("%d%s",ww[i],i<rr-1?",":"\n");
  return cur?1:0;
}
