// rosary checker: ./roscheck n word(as digits or comma list) [quiet]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int n,r,w[512],nxt[1024][16],perm[16],used[16]; long missing; int quiet=0;
long fact(int m){long f=1;for(int i=2;i<=m;i++)f*=i;return f;}
void rec(int d,int *pos,int *stj,int np){
  if(np==0){ missing+=fact(n-d); if(!quiet&&missing<=5){printf("  missing prefix:");for(int i=0;i<d;i++)printf(" %d",perm[i]);printf("\n");} return; }
  if(d==n) return;
  int np2[512],sj2[512];
  for(int l=1;l<=n;l++) if(!used[l]){
    used[l]=1; perm[d]=l; int nn=0;
    for(int i=0;i<np;i++){ int q=nxt[pos[i]][l]; if(q<stj[i]+r){ np2[nn]=q+1; sj2[nn]=stj[i]; nn++; } }
    rec(d+1,np2,sj2,nn); used[l]=0;
  }
}
long check(int nn,int rr,int*ww){ n=nn;r=rr; for(int i=0;i<r;i++)w[i]=ww[i];
  int R2=2*r; for(int l=1;l<=n;l++){ int last=R2; for(int i=R2;i>=0;i--){ if(i<R2 && w[i%r]==l) last=i; nxt[i][l]=last; } }
  int pos[512],stj[512]; for(int j=0;j<r;j++){pos[j]=j;stj[j]=j;}
  missing=0; memset(used,0,sizeof used); rec(0,pos,stj,r); return missing; }
#ifndef NOMAIN
int main(int argc,char**argv){
  int nn=atoi(argv[1]); char*s=argv[2]; int rr=0; int ww[512];
  if(argc>3) quiet=1;
  if(strchr(s,',')){ char*t=strtok(s,","); while(t){ww[rr++]=atoi(t); t=strtok(NULL,",");} }
  else for(int i=0;s[i];i++) ww[rr++]=s[i]-'0';
  long m=check(nn,rr,ww);
  printf("n=%d r=%d missing=%ld\n",nn,rr,m);
  return m?1:0;
}
#endif
