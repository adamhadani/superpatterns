// ./structX2 n M L K first : word=(1..n)^M X (n..1)^K (n..2); X increasing of length L with X[0]=first
#define NOMAIN
#include "roscheck.c"
int n,M,L,K; int base[600]; int pos,r; long found=0,tested=0;
void gen(int d,int minv){ if(d==L){ tested++; long m=check(n,r,base); if(m==0){found++; printf("FOUND X=");for(int i=0;i<L;i++)printf("%d ",base[pos+i]);printf("\n");fflush(stdout);} return;}
  for(int v=minv;v<=n;v++){ base[pos+d]=v; gen(d+1,v+1);} }
int main(int argc,char**argv){ quiet=1; n=atoi(argv[1]);M=atoi(argv[2]);L=atoi(argv[3]);K=atoi(argv[4]); int first=atoi(argv[5]);
  r=0; for(int rep=0;rep<M;rep++) for(int l=1;l<=n;l++) base[r++]=l; pos=r; r+=L; for(int rep=0;rep<K;rep++) for(int l=n;l>=1;l--) base[r++]=l; for(int l=n;l>=2;l--) base[r++]=l;
  base[pos]=first; gen(1,first+1); printf("done first=%d tested=%ld found=%ld\n",first,tested,found); }
