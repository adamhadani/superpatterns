/* enum3.c -- exact evaluation of the strip and square first-occurrence rules for a pattern tau.
   For m = |tau| .. M: enumerate sigma in Av_{m-1}(tau) (x-ranks 1..m-1, values = y-ranks), insert the new
   point at x-rank m with y-rank r in 1..m (shifting), and if the m points contain tau (necessarily using the
   new point), record minTop = min over copies of the max y-rank of the copy.
   Output per m: cnt_m = #(sigma,r) with a copy; sumTop_m = sum of minTop.  Then
     p_m = cnt_m/m!,  q_m = sumTop_m/((m+1) m!).
   Usage: ./enum3 tau M      (tau as digits, e.g. 321) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int J, tau[8]; int M;
double cnt[40], sumTop[40];
int perm[40];
/* does the sequence a[0..n-1] contain tau with a copy that includes position n-1 (the last)?  return min top rank (or 0) */
static int mintop_last(int *a,int n){
  int best=0;
  if(J==2){ for(int i=0;i<n-1;i++){ int ok=(tau[0]<tau[1])?(a[i]<a[n-1]):(a[i]>a[n-1]); if(ok){int t=a[i]>a[n-1]?a[i]:a[n-1]; if(!best||t<best)best=t;} } }
  else if(J==3){ for(int i=0;i<n-1;i++)for(int k=i+1;k<n-1;k++){ int y[3]={a[i],a[k],a[n-1]}; int ok=1; for(int p=0;p<3&&ok;p++)for(int q=p+1;q<3;q++) if((tau[p]<tau[q])!=(y[p]<y[q])){ok=0;break;} if(ok){int t=y[0];if(y[1]>t)t=y[1];if(y[2]>t)t=y[2]; if(!best||t<best)best=t;} } }
  else if(J==4){ for(int i=0;i<n-1;i++)for(int k=i+1;k<n-1;k++)for(int l=k+1;l<n-1;l++){ int y[4]={a[i],a[k],a[l],a[n-1]}; int ok=1; for(int p=0;p<4&&ok;p++)for(int q=p+1;q<4;q++) if((tau[p]<tau[q])!=(y[p]<y[q])){ok=0;break;} if(ok){int t=y[0];for(int z=1;z<4;z++)if(y[z]>t)t=y[z]; if(!best||t<best)best=t;} } }
  return best;
}
static int used[40];
/* recursively build tau-avoiding perms of length n (values 1..n) */
static void rec(int pos,int n){
  if(pos==n){
    /* sigma = perm[0..n-1] avoids tau.  insert new point with y-rank r in 1..n+1 */
    int m=n+1; int a[41];
    for(int r=1;r<=m;r++){
      for(int i=0;i<n;i++) a[i]= perm[i]>=r ? perm[i]+1 : perm[i];
      a[n]=r;
      int t=mintop_last(a,m);
      if(t){cnt[m]+=1; sumTop[m]+=t;}
    }
    return;
  }
  for(int v=1;v<=n;v++) if(!used[v]){
    perm[pos]=v;
    if(pos+1>=J && mintop_last(perm,pos+1)) continue; /* prefix would contain tau */
    used[v]=1; rec(pos+1,n); used[v]=0;
  }
}
int main(int argc,char**argv){
  char*t=argv[1]; J=strlen(t); for(int i=0;i<J;i++)tau[i]=t[i]-'0'; M=atoi(argv[2]);
  for(int n=J-1;n<M;n++){ memset(used,0,sizeof used); rec(0,n); printf("m %d cnt %.0f sumTop %.0f\n",n+1,cnt[n+1],sumTop[n+1]); fflush(stdout);}
  return 0;
}
