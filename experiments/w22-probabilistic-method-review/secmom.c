/* Exact second moment of X = #copies of a pattern pi (length k) in a uniform
   random permutation of length n.  E X = C(n,k)/k!,
   E X^2 = sum_{u=k}^{2k} C(n,u) * A_u / u!,  where
   A_u = #{(rho in S_u, I, J): |I|=|J|=k, I u J = [u], rho|_I ~ pi, rho|_J ~ pi}.
   Usage: ./secmom k pi_1 ... pi_k   (pi as a permutation of 1..k) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
static int k, pi[16];
static int u; static int rho[20];
static long long A[40];
static unsigned masks[100000]; static int nm;
static int fits(unsigned m){ /* does rho restricted to positions in m have pattern pi? */
  int idx[16], c=0; for(int i=0;i<u;i++) if(m>>i&1) idx[c++]=i;
  for(int a=0;a<k;a++) for(int b=a+1;b<k;b++){
    int lt = rho[idx[a]] < rho[idx[b]]; int plt = pi[a] < pi[b]; if(lt!=plt) return 0; }
  return 1; }
static void process(){
  nm=0; unsigned full=(1u<<u)-1;
  /* enumerate k-subsets of [u] */
  for(unsigned m=0;m<=full;m++){ if(__builtin_popcount(m)!=k) continue; if(fits(m)) masks[nm++]=m; }
  for(int a=0;a<nm;a++) for(int b=0;b<nm;b++) if((masks[a]|masks[b])==full) A[u]++;
}
static void perm(int pos){ if(pos==u){process();return;} for(int i=pos;i<u;i++){int t=rho[pos];rho[pos]=rho[i];rho[i]=t; perm(pos+1); t=rho[pos];rho[pos]=rho[i];rho[i]=t;} }
static double lbinom(int n,int r){ return lgamma(n+1)-lgamma(r+1)-lgamma(n-r+1); }
int main(int argc,char**argv){ k=atoi(argv[1]); for(int i=0;i<k;i++) pi[i]=atoi(argv[2+i]);
  for(u=k;u<=2*k;u++){ for(int i=0;i<u;i++) rho[i]=i; A[u]=0; perm(0); }
  printf("# k=%d pi=",k); for(int i=0;i<k;i++) printf("%d",pi[i]); printf("\n# A_u:"); for(u=k;u<=2*k;u++) printf(" %lld",A[u]); printf("\n");
  printf("# n  C=n/k^2  EX  EX2/EX^2  (Delta_j/mu^2 by overlap j=k..0 i.e. u=k..2k)\n");
  for(int n=k*k/2; n<=6*k*k; n+= (k*k)/4){
    double lmu = lbinom(n,k)-lgamma(k+1); double s=0; double terms[40];
    for(u=k;u<=2*k;u++){ double t = exp(lbinom(n,u) + log((double)A[u]) - lgamma(u+1) - 2*lmu); terms[u]=t; s+=t; }
    printf("%d %.3f %.3e %.4f  ", n, (double)n/(k*k), exp(lmu), s);
    for(u=k;u<=2*k;u++) printf(" %.3g", terms[u]); printf("\n"); }
  return 0; }
