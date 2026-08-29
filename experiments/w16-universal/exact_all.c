// Exact Pr(pi ⊂ sigma_n) for ALL pi in S_k, by enumerating all sigma in S_n and all k-subsets.
// usage: exact_all n k   -> prints, for every pi (as pattern index), the count of sigma containing pi; then a summary:
// the identity's count, the max count and its argmax, and the number of pi with count > identity's.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int n,k; static int fact[13];
static int rank_perm(const int*p,int m){ // lexicographic rank of a permutation of 0..m-1
    int r=0; for(int i=0;i<m;i++){int c=0;for(int j=i+1;j<m;j++) if(p[j]<p[i]) c++; r+=c*fact[m-1-i];} return r;
}
int main(int argc,char**argv){
    n=atoi(argv[1]); k=atoi(argv[2]);
    fact[0]=1; for(int i=1;i<13;i++) fact[i]=fact[i-1]*i;
    int np=fact[k]; long *cnt=calloc(np,sizeof(long)); char *seen=malloc(np);
    int sig[12]; for(int i=0;i<n;i++) sig[i]=i;
    // iterate all permutations via next_permutation
    long total=0;
    while(1){
        memset(seen,0,np); total++;
        // enumerate k-subsets
        int idx[12]; for(int i=0;i<k;i++) idx[i]=i;
        while(1){
            int vals[12]; for(int i=0;i<k;i++) vals[i]=sig[idx[i]];
            int pat[12]; for(int i=0;i<k;i++){int c=0;for(int j=0;j<k;j++) if(vals[j]<vals[i]) c++; pat[i]=c;}
            seen[rank_perm(pat,k)]=1;
            int i=k-1; while(i>=0 && idx[i]==n-k+i) i--; if(i<0) break; idx[i]++; for(int j=i+1;j<k;j++) idx[j]=idx[j-1]+1;
        }
        for(int p=0;p<np;p++) cnt[p]+=seen[p];
        // next permutation of sig
        int i=n-2; while(i>=0 && sig[i]>sig[i+1]) i--; if(i<0) break;
        int j=n-1; while(sig[j]<sig[i]) j--; int t=sig[i];sig[i]=sig[j];sig[j]=t;
        for(int a=i+1,b=n-1;a<b;a++,b--){t=sig[a];sig[a]=sig[b];sig[b]=t;}
    }
    long idc=cnt[0]; long mx=0; int arg=0; int nbetter=0;
    for(int p=0;p<np;p++){ if(cnt[p]>mx){mx=cnt[p];arg=p;} if(cnt[p]>idc) nbetter++; }
    // decode arg
    int pat[12], used[12]={0}; int r=arg; for(int i=0;i<k;i++){int c=r/fact[k-1-i]; r%=fact[k-1-i]; int v=0; for(int j=0;j<k;j++){ if(!used[j]){ if(c==0){v=j;break;} c--; } } used[v]=1; pat[i]=v; }
    printf("n=%d k=%d  Pr(id)=%.6f  max=%.6f at ",n,k,(double)idc/total,(double)mx/total);
    for(int i=0;i<k;i++) printf("%d",pat[i]+1);
    printf("   #pi with Pr>Pr(id): %d of %d\n",nbetter,np);
    return 0;
}
