#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
static uint64_t rng_s[2];
static inline uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static uint64_t rnd(void){uint64_t s0=rng_s[0],s1=rng_s[1],r=s0+s1;s1^=s0;rng_s[0]=rotl(s0,55)^s1^(s1<<14);rng_s[1]=rotl(s1,36);return r;}
#define MAXK 64
#define MAXN 2048
static int n,k,pi[MAXK],pinv[MAXK],sig[MAXN];
static int *cnt,N1; // cnt[i*N1+v] = #{j<i: sig[j]<v}, N1=n+1
static int insp=-1,insm; // W27: virtual insertion of value insm at position insp into the base table
static inline int C(int i,int v){ if(insp<0) return cnt[i*N1+v]; return i<=insp ? cnt[i*N1+v] : cnt[(i-1)*N1+v]+(v>insm); }
// count of points with position in (i1,i2) and value in (v1,v2) (open)
static inline int rect(int i1,int i2,int v1,int v2){
    if(i2-i1<2||v2-v1<2) return 0;
    return C(i2,v2)-C(i2,v1+1)-C(i1+1,v2)+C(i1+1,v1+1);
}
// smallest position j in (i1,i2) with value in (v1,v2); requires rect>0
static inline int firstpos(int i1,int i2,int v1,int v2){
    int base=C(i1+1,v2)-C(i1+1,v1+1); // points before i1+1
    int lo=i1+1,hi=i2-1; // answer in [lo,hi]; predicate: C(j+1,..)-base>=1
    while(lo<hi){int m=(lo+hi)>>1; if(C(m+1,v2)-C(m+1,v1+1)-base>=1) hi=m; else lo=m+1;}
    return lo;
}
static inline int lastpos(int i1,int i2,int v1,int v2){
    int tot=C(i2,v2)-C(i2,v1+1);
    int lo=i1+1,hi=i2-1; // largest j with tot-(C(j,v2)-C(j,v1+1))>=1 i.e. a point at position>=j
    while(lo<hi){int m=(lo+hi+1)>>1; if(tot-(C(m,v2)-C(m,v1+1))>=1) lo=m; else hi=m-1;}
    return lo;
}
// smallest value v in (v1,v2) held by a point at position in (i1,i2)
static inline int minval(int i1,int i2,int v1,int v2){
    int lo=v1+1,hi=v2-1; // predicate on v: rect(i1,i2,v1,v+1)>=1  i.e. C(i2,v+1)-C(i2,v1+1)-C(i1+1,v+1)+C(i1+1,v1+1)>=1
    int b=C(i1+1,v1+1)-C(i2,v1+1);
    while(lo<hi){int m=(lo+hi)>>1; if(C(i2,m+1)-C(i1+1,m+1)+b>=1) hi=m; else lo=m+1;}
    return lo;
}
static inline int maxval(int i1,int i2,int v1,int v2){
    int lo=v1+1,hi=v2-1; // largest v with a point of value>=v: rect(i1,i2,v-1,v2)>=1
    int b=C(i2,v2)-C(i1+1,v2);
    while(lo<hi){int m=(lo+hi+1)>>1; if(b-(C(i2,m)-C(i1+1,m))>=1) lo=m; else hi=m-1;}
    return lo;
}
static int pos[MAXK];
static long long nodes;
static int maxpass=6; static int verbose=0; static int uselis=1; static int ptail_i[MAXN],ptail_d[MAXN];
static int dfs(int placed){
    if(placed==k) return 1;
    nodes++;
    int li[MAXK],hi[MAXK],lv[MAXK],hv[MAXK],c[MAXK];
    // initial windows from placed neighbours (as in contain_mrv) + cell prune
    { int need[MAXK+1][MAXK+1]; memset(need,0,sizeof(need)); int cell[MAXK]; int rep[(MAXK+1)*(MAXK+1)];
      // gaps: sorted placed positions / values give gap rectangles.  Compute per element as before (O(k^2)).
      for(int e=0;e<k;e++){
        if(pos[e]>=0){li[e]=pos[e]-1;hi[e]=pos[e]+1;lv[e]=sig[pos[e]]-1;hv[e]=sig[pos[e]]+1;cell[e]=-1;continue;}
        int l=-1,h=n,a=-1,b=n,ga=0,gb=0;
        for(int f=0;f<k;f++){ if(pos[f]<0) continue;
            if(f<e){ if(pos[f]>l) l=pos[f]; ga++; } else { if(pos[f]<h) h=pos[f]; }
            if(pi[f]<pi[e]){ if(sig[pos[f]]>a) a=sig[pos[f]]; gb++; } else { if(sig[pos[f]]<b) b=sig[pos[f]]; }
        }
        li[e]=l;hi[e]=h;lv[e]=a;hv[e]=b;
        int cc=rect(l,h,a,b);
        if(cc==0) return 0;
        cell[e]=ga*(MAXK+1)+gb; if(need[ga][gb]==0) rep[cell[e]]=e;
        if(++need[ga][gb]>cc) return 0;
      }
      if(uselis){
        // per cell with >= 2 elements: LIS/LDS of the sub-pattern must fit in LIS/LDS of the cell's points
        for(int e=0;e<k;e++){
          if(cell[e]<0||rep[cell[e]]!=e) continue;   // handle each cell once, at its first element
          int ce=cell[e]; int m=need[ce/(MAXK+1)][ce%(MAXK+1)]; if(m<2) continue;
          int ti[MAXK],td[MAXK],Li=0,Ld=0;
          for(int f=e;f<k;f++){ if(cell[f]!=ce) continue; int x=pi[f];
            int lo=0,h2=Li; while(lo<h2){int mm=(lo+h2)>>1; if(ti[mm]<x) lo=mm+1; else h2=mm;} ti[lo]=x; if(lo==Li) Li++;
            lo=0;h2=Ld; while(lo<h2){int mm=(lo+h2)>>1; if(td[mm]>x) lo=mm+1; else h2=mm;} td[lo]=x; if(lo==Ld) Ld++;
          }
          int Pi=0,Pd=0; int *pti=ptail_i,*ptd=ptail_d;
          for(int j=li[e]+1;j<hi[e];j++){ int x=sig[j]; if(x<=lv[e]||x>=hv[e]) continue;
            int lo=0,h2=Pi; while(lo<h2){int mm=(lo+h2)>>1; if(pti[mm]<x) lo=mm+1; else h2=mm;} pti[lo]=x; if(lo==Pi) Pi++;
            lo=0;h2=Pd; while(lo<h2){int mm=(lo+h2)>>1; if(ptd[mm]>x) lo=mm+1; else h2=mm;} ptd[lo]=x; if(lo==Pd) Pd++;
            if(Pi>=Li&&Pd>=Ld) break;
          }
          if(Pi<Li||Pd<Ld) return 0;
        }
      }
    }
    // bounds propagation to fixpoint
    for(int pass=0;pass<maxpass;pass++){
        int changed=0;
        // position chain, left to right then right to left
        for(int e=1;e<k;e++){
            if(pos[e]>=0) continue;
            int f=firstpos(li[e-1],hi[e-1],lv[e-1],hv[e-1]);
            if(f>li[e]){li[e]=f;changed=1; if(hi[e]-li[e]<2||rect(li[e],hi[e],lv[e],hv[e])==0) return 0;}
        }
        for(int e=k-2;e>=0;e--){
            if(pos[e]>=0) continue;
            int f=lastpos(li[e+1],hi[e+1],lv[e+1],hv[e+1]);
            if(f<hi[e]){hi[e]=f;changed=1; if(hi[e]-li[e]<2||rect(li[e],hi[e],lv[e],hv[e])==0) return 0;}
        }
        for(int r=1;r<k;r++){
            int e=pinv[r]; if(pos[e]>=0) continue;
            int q=pinv[r-1];
            int m=minval(li[q],hi[q],lv[q],hv[q]);
            if(m>lv[e]){lv[e]=m;changed=1; if(hv[e]-lv[e]<2||rect(li[e],hi[e],lv[e],hv[e])==0) return 0;}
        }
        for(int r=k-2;r>=0;r--){
            int e=pinv[r]; if(pos[e]>=0) continue;
            int q=pinv[r+1];
            int m=maxval(li[q],hi[q],lv[q],hv[q]);
            if(m<hv[e]){hv[e]=m;changed=1; if(hv[e]-lv[e]<2||rect(li[e],hi[e],lv[e],hv[e])==0) return 0;}
        }
        if(!changed) break;
    }
    int best=-1,bestc=1<<30;
    for(int e=0;e<k;e++){ if(pos[e]>=0) continue; c[e]=rect(li[e],hi[e],lv[e],hv[e]); if(c[e]<bestc){bestc=c[e];best=e;} }
    int e=best;
    for(int j=li[e]+1;j<hi[e];j++){
        int v=sig[j]; if(v<=lv[e]||v>=hv[e]) continue;
        pos[e]=j;
        if(dfs(placed+1)){pos[e]=-1;return 1;}
    }
    pos[e]=-1;
    return 0;
}
static int parse(const char*s,int*p){
    int kk=0;
    if(strchr(s,',')){ char buf[1024]; strncpy(buf,s,1023); buf[1023]=0; char*tok=strtok(buf,","); while(tok){p[kk++]=atoi(tok)-1;tok=strtok(NULL,",");} }
    else { for(;*s;s++) p[kk++]=*s-'1'; }
    return kk;
}
