// P(tau contained in uniform sigma in S_k) exactly, k<=KMAX, by enumeration; several tau at once.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int K; static int perm[16]; static int ntau; static int taus[64][8], tlen[64]; static long long cnt[64];
static int contains(int *t,int j){ // does perm (length K) contain pattern t of length j?  DFS over positions
  int idx[8]; int pos=0; idx[0]=-1;
  while(pos>=0){ idx[pos]++; if(idx[pos]>K-(j-pos)){pos--; continue;}
    int ok=1; for(int q=0;q<pos&&ok;q++){ if((perm[idx[q]]<perm[idx[pos]])!=(t[q]<t[pos])) ok=0; }
    if(!ok) continue; if(pos==j-1) return 1; pos++; idx[pos]=idx[pos-1]; }
  return 0; }
static void rec(int i, unsigned used){ if(i==K){ for(int a=0;a<ntau;a++) cnt[a]+=contains(taus[a],tlen[a]); return; }
  for(int v=0;v<K;v++) if(!(used>>v&1)){ perm[i]=v; rec(i+1,used|(1u<<v)); } }
int main(int argc,char**argv){ K=atoi(argv[1]); ntau=argc-2; for(int a=0;a<ntau;a++){ tlen[a]=strlen(argv[a+2]); for(int i=0;i<tlen[a];i++) taus[a][i]=argv[a+2][i]-'0'; }
  rec(0,0); double kf=1; for(int i=2;i<=K;i++)kf*=i;
  for(int a=0;a<ntau;a++) printf("%d %s %lld %.10f\n",K,argv[a+2],cnt[a],cnt[a]/kf); }
