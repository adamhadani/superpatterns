// Pattern containment test for uniform random permutations, CSP-style search:
// "most constrained pattern element first" + cell-count pruning.  Same interface as contain_gen:
//   contain_mrv n samples seed pat1 pat2 ...   (patterns as comma lists or digit strings; k<=32)
// State: each placed pattern element e has a sigma position; unplaced element e has a window
//   (index gap between placed neighbours in index) x (value gap between placed neighbours in value);
//   the number of sigma points in the window rectangle is c_e.  Prune: c_e = 0, or, for every cell (index gap,
//   value gap), #unplaced pattern elements in the cell > #sigma points in the cell.  Branch on min c_e.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static uint64_t rng_s[2];
static inline uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static uint64_t rnd(void){uint64_t s0=rng_s[0],s1=rng_s[1],r=s0+s1;s1^=s0;rng_s[0]=rotl(s0,55)^s1^(s1<<14);rng_s[1]=rotl(s1,36);return r;}
#define MAXK 32
#define MAXN 1024
static int n,k,pi[MAXK],sig[MAXN];
static int *cnt; // cnt[i*(n+1)+v] = #{j<i: sig[j]<v}
static inline int rect(int i1,int i2,int v1,int v2){ // open rectangle (i1,i2)x(v1,v2)
    if(i2-i1<2||v2-v1<2) return 0;
    return cnt[i2*(n+1)+v2]-cnt[i2*(n+1)+v1+1]-cnt[(i1+1)*(n+1)+v2]+cnt[(i1+1)*(n+1)+v1+1];
}
static int pos[MAXK]; // -1 if unplaced
static long nodes;
static int dfs(int placed){
    if(placed==k) return 1;
    nodes++;
    int need[MAXK+1][MAXK+1]; memset(need,0,sizeof(need));
    int loi[MAXK],hii[MAXK],lov[MAXK],hiv[MAXK],gi[MAXK],gv[MAXK],c[MAXK];
    int best=-1,bestc=1<<30;
    for(int e=0;e<k;e++){
        if(pos[e]>=0) continue;
        int li=-1,hi=n,lv=-1,hv=n,a=0,b=0;
        for(int f=0;f<k;f++){ if(pos[f]<0) continue;
            if(f<e){ if(pos[f]>li) li=pos[f]; a++; } else { if(pos[f]<hi) hi=pos[f]; }
            if(pi[f]<pi[e]){ if(sig[pos[f]]>lv) lv=sig[pos[f]]; b++; } else { if(sig[pos[f]]<hv) hv=sig[pos[f]]; }
        }
        loi[e]=li;hii[e]=hi;lov[e]=lv;hiv[e]=hv;gi[e]=a;gv[e]=b;
        c[e]=rect(li,hi,lv,hv);
        if(c[e]==0) return 0;
        if(++need[a][b]>c[e]) return 0;
        if(c[e]<bestc){bestc=c[e];best=e;}
    }
    int e=best;
    for(int j=loi[e]+1;j<hii[e];j++){
        int v=sig[j]; if(v<=lov[e]||v>=hiv[e]) continue;
        pos[e]=j;
        if(dfs(placed+1)){pos[e]=-1;return 1;}
    }
    pos[e]=-1;
    return 0;
}
int main(int argc,char**argv){
    if(argc<5){fprintf(stderr,"usage: n samples seed pat...\n");return 1;}
    n=atoi(argv[1]); int samples=atoi(argv[2]); uint64_t seed=atoll(argv[3]);
    rng_s[0]=seed*0x9E3779B97F4A7C15ULL+1; rng_s[1]=seed^0xD1B54A32D192ED03ULL; for(int i=0;i<20;i++)rnd();
    int np=argc-4; long *hits=calloc(np,sizeof(long));
    cnt=malloc(sizeof(int)*(n+2)*(n+2));
    for(int t=0;t<samples;t++){
        for(int i=0;i<n;i++)sig[i]=i;
        for(int i=n-1;i>0;i--){int j=rnd()%(i+1);int tmp=sig[i];sig[i]=sig[j];sig[j]=tmp;}
        for(int v=0;v<=n;v++) cnt[v]=0;
        for(int i=0;i<n;i++) for(int v=0;v<=n;v++) cnt[(i+1)*(n+1)+v]=cnt[i*(n+1)+v]+(sig[i]<v);
        for(int p=0;p<np;p++){
            const char*s=argv[4+p]; k=0;
            if(strchr(s,',')){ char buf[512]; strncpy(buf,s,511); buf[511]=0; char*tok=strtok(buf,","); while(tok){pi[k++]=atoi(tok)-1;tok=strtok(NULL,",");} }
            else { for(;*s;s++) pi[k++]=*s-'1'; }
            for(int e=0;e<k;e++) pos[e]=-1;
            hits[p]+=dfs(0);
        }
    }
    for(int p=0;p<np;p++) printf("%s %.4f\n",argv[4+p],(double)hits[p]/samples);
    fprintf(stderr,"nodes=%ld\n",nodes);
    return 0;
}
