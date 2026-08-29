/* fibres: for a permutation sigma (1-based) and a partition of values into rows (row id per value, weakly
   increasing in value), enumerate every k-subset of positions; for each k-pattern record
     tot   = number of embeddings,
     mono  = number of embeddings in which every fibre (set of chosen positions whose values lie in one row)
             is monotone (increasing or decreasing) as a subsequence of sigma,
     maxfib = over embeddings, the minimum (over embeddings) of the largest fibre size ... (not needed)
   Output: one line per pattern: rank tot mono   (only patterns with tot>0 or with a flag -a for all)
   usage: fibres k n s1..sn r1..rn      (r_v = row id of value v, 1-based, weakly increasing) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int k,n,s[64],row[64]; static long fact[13]; static int sel[16];
static unsigned int *tot,*mono;
static void rec(int d,int start){
  if(d==k){
    long r=0; for(int i=0;i<k;i++){int c=0;for(int j=i+1;j<k;j++) if(sel[j]<sel[i]) c++; r+=c*fact[k-1-i];}
    tot[r]++;
    /* fibre monotonicity: for each row present, take chosen values in that row in position order */
    int ok=1;
    for(int i=0;i<k && ok;i++){
      int rw=row[sel[i]];
      /* find the sequence of chosen values in row rw in position order; check monotone */
      int prev=-1, dir=0;
      for(int j=0;j<k;j++) if(row[sel[j]]==rw){
        if(prev>=0){ int d2=(sel[j]>prev)?1:-1; if(dir==0) dir=d2; else if(dir!=d2){ok=0;break;} }
        prev=sel[j];
      }
    }
    if(ok) mono[r]++;
    return; }
  for(int p=start;p<=n-(k-d);p++){ sel[d]=s[p]; rec(d+1,p+1);} }
int main(int argc,char**argv){ k=atoi(argv[1]); n=atoi(argv[2]);
  for(int i=0;i<n;i++) s[i]=atoi(argv[3+i]); for(int v=1;v<=n;v++) row[v]=atoi(argv[3+n+v-1]);
  fact[0]=1; for(int i=1;i<13;i++) fact[i]=fact[i-1]*i;
  tot=calloc(fact[k],4); mono=calloc(fact[k],4); rec(0,0);
  long nmiss=0,nnomono=0;
  for(long r=0;r<fact[k];r++){ if(!tot[r]) nmiss++; else if(!mono[r]) nnomono++; }
  printf("SUMMARY missing=%ld need_nonmono=%ld\n",nmiss,nnomono);
  for(long r=0;r<fact[k];r++) printf("%ld %u %u\n",r,tot[r],mono[r]);
  return 0; }
