// exact evaluation of (1.2): B = 2^-N sum_m C(N,m) m! [z^m] F(z)^{2(k-1)}, F = sum z^n/(n!)^2 ; log domain
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int N;
static double lse(double a,double b){ if(a==-INFINITY)return b; if(b==-INFINITY)return a; double m=a>b?a:b; return m+log1p(exp(-fabs(a-b))); }
static void mul(const double*a,const double*b,double*o){ for(int i=0;i<=N;i++)o[i]=-INFINITY; for(int i=0;i<=N;i++){ if(a[i]==-INFINITY)continue; for(int j=0;i+j<=N;j++){ if(b[j]==-INFINITY)continue; o[i+j]=lse(o[i+j],a[i]+b[j]); } } }
int main(int argc,char**argv){ int k=atoi(argv[1]); double C=atof(argv[2]); N=(int)(C*k*k); int L=2*(k-1);
  double *base=malloc((N+1)*sizeof(double)),*res=malloc((N+1)*sizeof(double)),*tmp=malloc((N+1)*sizeof(double)); int have=0;
  for(int n=0;n<=N;n++)base[n]=-2*lgamma(n+1);
  for(int e=L;e;e>>=1){ if(e&1){ if(!have){for(int i=0;i<=N;i++)res[i]=base[i];have=1;} else {mul(res,base,tmp);double*t=res;res=tmp;tmp=t;} } if(e>1){mul(base,base,tmp);double*t=base;base=tmp;tmp=t;} }
  double mx=-INFINITY; int am=0; for(int m=0;m<=N;m++){ double t=lgamma(N+1)-lgamma(N-m+1)+res[m]; tmp[m]=t; if(t>mx){mx=t;am=m;} }
  double s=0; for(int m=0;m<=N;m++) s+=exp(tmp[m]-mx); double lb=mx+log(s)-N*log(2);
  printf("k=%d C=%g N=%d  -lnB/N = %.4f  beta* = %.3f\n",k,C,N,-lb/N,(double)am/N); return 0; }
