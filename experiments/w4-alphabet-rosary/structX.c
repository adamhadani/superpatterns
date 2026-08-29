// ./structX n M X_len K  : word = (1..n)^M X (n..1)^K (n..2), enumerate all X in [n]^len (or increasing only if argv[5]=="inc")
#define NOMAIN
#include "roscheck.c"
int n,M,L,K,inc; int base[600]; int pos,r; long found=0;
void gen(int d,int minv){ if(d==L){ long m=check(n,r,base); if(m==0){found++; printf("FOUND X=");for(int i=0;i<L;i++)printf("%d ",base[pos+i]);printf("\n");fflush(stdout);} return;}
  for(int v=(inc?minv:1);v<=n;v++){ base[pos+d]=v; gen(d+1,v+1);} }
int main(int argc,char**argv){ quiet=1; n=atoi(argv[1]);M=atoi(argv[2]);L=atoi(argv[3]);K=atoi(argv[4]); inc=argc>5;
  r=0; for(int rep=0;rep<M;rep++) for(int l=1;l<=n;l++) base[r++]=l; pos=r; r+=L; for(int rep=0;rep<K;rep++) for(int l=n;l>=1;l--) base[r++]=l; for(int l=n;l>=2;l--) base[r++]=l;
  printf("n=%d total length %d\n",n,r); gen(0,1); printf("done found=%ld\n",found); }
