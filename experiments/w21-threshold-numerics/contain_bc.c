// contain_bc: pattern containment in uniform random permutations, CSP search with
// 2-D bounds consistency.  Interface (superset of contain_mrv):
//   contain_bc n samples seed pat1 pat2 ...      patterns as comma lists or digit strings, k <= 64
// Output per pattern: "<pat> <fraction> hits=<h> nodes=<N> sec=<t>" on stdout.
//
// State: pos[e] = sigma position of placed pattern element e (or -1).  Every element e (placed or not) has an
// open window (li,hi) x (lv,hv) of feasible positions x values.  Windows are tightened to a fixpoint by
//   position chain: li[e] >= first(e-1), hi[e] <= last(e+1)      (first/last = min/max position in window(e±1))
//   rank chain:     lv[e] >= minval(rankpred(e)), hv[e] <= maxval(ranksucc(e))
// using binary searches on the dominance table cnt[i][v] = #{j<i : sig[j]<v}.  Fail if a window is empty.
// Cell prune: unplaced elements sharing the same (index gap, value gap) w.r.t. the placed elements need at
// least that many sigma points in the gap rectangle.  Branch on the unplaced element with the fewest points.
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
static inline int C(int i,int v){return cnt[i*N1+v];}
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
int main(int argc,char**argv){
    if(argc<5){fprintf(stderr,"usage: n samples seed pat...\n");return 1;}
    verbose=getenv("VERBOSE")!=NULL; if(getenv("NOLIS")) uselis=0;
    n=atoi(argv[1]); int samples=atoi(argv[2]); uint64_t seed=atoll(argv[3]);
    if(n>=MAXN){fprintf(stderr,"n too large\n");return 1;}
    rng_s[0]=seed*0x9E3779B97F4A7C15ULL+1; rng_s[1]=seed^0xD1B54A32D192ED03ULL; for(int i=0;i<20;i++)rnd();
    int np=argc-4; long *hits=calloc(np,sizeof(long)); long long *nd=calloc(np,sizeof(long long)); double *tm=calloc(np,sizeof(double));
    N1=n+1; cnt=malloc(sizeof(int)*(n+2)*(n+2));
    int (*pats)[MAXK]=malloc(sizeof(int[MAXK])*np); int *ks=malloc(sizeof(int)*np);
    for(int p=0;p<np;p++){ ks[p]=parse(argv[4+p],pats[p]); if(ks[p]>MAXK){fprintf(stderr,"k too large\n");return 1;} }
    for(int t=0;t<samples;t++){
        for(int i=0;i<n;i++)sig[i]=i;
        for(int i=n-1;i>0;i--){int j=rnd()%(i+1);int tmp=sig[i];sig[i]=sig[j];sig[j]=tmp;}
        for(int v=0;v<=n;v++) cnt[v]=0;
        for(int i=0;i<n;i++){ int *r0=cnt+i*N1,*r1=cnt+(i+1)*N1; int s=sig[i]; for(int v=0;v<=s;v++) r1[v]=r0[v]; for(int v=s+1;v<=n;v++) r1[v]=r0[v]+1; }
        for(int p=0;p<np;p++){
            k=ks[p]; for(int e=0;e<k;e++){pi[e]=pats[p][e]; pinv[pi[e]]=e; pos[e]=-1;}
            struct timespec a,b; clock_gettime(CLOCK_MONOTONIC,&a);
            long long n0=nodes;
            {int h=dfs(0); hits[p]+=h; if(verbose) printf("S %d %d %d\n",t,p,h);}
            clock_gettime(CLOCK_MONOTONIC,&b);
            tm[p]+=(b.tv_sec-a.tv_sec)+1e-9*(b.tv_nsec-a.tv_nsec); nd[p]+=nodes-n0;
        }
    }
    for(int p=0;p<np;p++) printf("%s %.4f hits=%ld nodes=%lld sec=%.2f\n",argv[4+p],(double)hits[p]/samples,hits[p],nd[p],tm[p]);
    return 0;
}
