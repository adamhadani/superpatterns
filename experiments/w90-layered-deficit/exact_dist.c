// Exact distribution over S_n of L21 = max m with 21^{(+)m} contained, and of LIS, jointly.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int n;
static long long joint[16][16]; // [L21][LIS]
static int l21(const int *s){
  // G[i][j] = min top value over chains of j pairs within positions < i ; G[.][0] = -1
  int G[14][8];
  int m = n/2;
  for(int j=0;j<=m;j++) G[0][j] = (j==0)? -1 : 100;
  for(int i=0;i<n;i++){
    for(int j=0;j<=m;j++) G[i+1][j]=G[i][j];
    for(int a=0;a<i;a++) if(s[a]>s[i]){
      // largest j with G[a][j] < s[i]
      int j=0; while(j<m && G[a][j+1]<s[i]) j++;
      if(j<m && s[a]<G[i+1][j+1]) G[i+1][j+1]=s[a];
    }
  }
  int j=0; while(j<m && G[n][j+1]<100) j++;
  return j;
}
static int lis(const int *s){
  int t[14],len=0;
  for(int i=0;i<n;i++){int lo=0,hi=len;while(lo<hi){int md=(lo+hi)/2; if(t[md]<s[i])lo=md+1;else hi=md;} t[lo]=s[i]; if(lo==len)len++;}
  return len;
}
static int s[14],used[14];
static void rec(int pos){
  if(pos==n){ joint[l21(s)][lis(s)]++; return; }
  for(int v=0;v<n;v++) if(!used[v]){used[v]=1;s[pos]=v;rec(pos+1);used[v]=0;}
}
int main(int argc,char**argv){
  n=atoi(argv[1]);
  rec(0);
  printf("n=%d\n",n);
  long long dL[16]={0},dF[16]={0};
  for(int a=0;a<16;a++)for(int b=0;b<16;b++){dL[a]+=joint[a][b];dF[b/2]+=joint[a][b];}
  for(int a=0;a<=n/2;a++) printf("  m=%d: #L21=m %lld   #floor(LIS/2)=m %lld   diff %lld\n",a,dL[a],dF[a],dL[a]-dF[a]);
  return 0;
}
