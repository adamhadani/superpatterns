// W33: exact p_id(n) = Pr(LIS(sigma_n) < k) = (1/n!) sum_{lambda |- n, rows<=k-1} f_lambda^2  (hook length formula, log-doubles)
// usage: lis_exact k nmax   -> lines: n  ln p_id(n)  slope s(n)=ln p(n-1)-ln p(n)   E[T]=n*exp(-s)
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int m, lam[64], N;
static double acc; // sum of f^2 / n!  accumulated as exp(logs) relative to a reference
static double lfact[400];
static double ref;
static void visit(int parts){
    // hook product
    int conj[400]; // lambda'_j
    for(int j=0;j<lam[0];j++){ int c=0; for(int i=0;i<parts;i++) if(lam[i]>j) c++; conj[j]=c; }
    double lh=0;
    for(int i=0;i<parts;i++) for(int j=0;j<lam[i];j++) lh += log((double)(lam[i]-j+conj[j]-i-1));
    double lf = lfact[N]-lh; // ln f_lambda
    acc += exp(2*lf - lfact[N] - ref);
}
static void rec(int i,int rem,int maxpart){
    if(rem==0){ visit(i); return; }
    if(i==m) return;
    int hi = rem<maxpart?rem:maxpart;
    for(int p=hi;p>=1;p--){ lam[i]=p; rec(i+1,rem-p,p); }
}
int main(int argc,char**argv){
    int k=atoi(argv[1]), nmax=atoi(argv[2]); m=k-1;
    lfact[0]=0; for(int i=1;i<400;i++) lfact[i]=lfact[i-1]+log((double)i);
    double prev=0;
    for(N=1;N<=nmax;N++){
        // reference: ln f^2/n! for the "balanced" shape ~ use previous value
        ref = prev; acc=0; rec(0,N,N);
        double lp = ref+log(acc);
        double s = (N>1)? prev - lp : 0;
        printf("%d %.8f %.6f %.4f\n",N,lp,s,N*exp(-s)); fflush(stdout);
        prev=lp;
    }
    return 0;
}
