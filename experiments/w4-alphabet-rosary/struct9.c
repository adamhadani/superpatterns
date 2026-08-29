#define NOMAIN
#include "roscheck.c"
int main(){ quiet=1; int base[64]; int r=0; int n=9;
  for(int rep=0;rep<2;rep++) for(int l=1;l<=n;l++) base[r++]=l;
  int pos=r; r+=4; for(int l=n;l>=1;l--) base[r++]=l; for(int l=n;l>=2;l--) base[r++]=l;
  long found=0;
  for(int a=1;a<=n;a++)for(int b=1;b<=n;b++)for(int c=1;c<=n;c++)for(int d=1;d<=n;d++){
    base[pos]=a;base[pos+1]=b;base[pos+2]=c;base[pos+3]=d;
    long m=check(n,r,base); if(m==0){found++; printf("FOUND X=%d%d%d%d\n",a,b,c,d); fflush(stdout);} }
  printf("done found=%ld\n",found); }
