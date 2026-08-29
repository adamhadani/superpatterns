// General pattern containment test for uniform random permutations (or Poisson point sets).
// usage: contain_gen n samples seed pattern1 pattern2 ...   (patterns as digit strings, or comma lists for k>9)
// Prints, for each pattern, the fraction of the SAME samples containing it (common random numbers).
// Method: DFS over pattern positions left to right; at step r choose sigma-position i > i_{r-1} whose value lies
// strictly between the values of the already-chosen points of pattern-rank pi(r)-1 and pi(r)+1 (among chosen),
// with a lookahead prune: for the remaining pattern elements, enough positions must remain, and the value window
// of the chosen "rank neighbourhood" must contain enough distinct future values (cheap count via prefix tables).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static uint64_t rng_s[2];
static inline uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static uint64_t rnd(void){uint64_t s0=rng_s[0],s1=rng_s[1],r=s0+s1;s1^=s0;rng_s[0]=rotl(s0,55)^s1^(s1<<14);rng_s[1]=rotl(s1,36);return r;}
static double urand(void){return (rnd()>>11)*(1.0/9007199254740992.0);}

#define MAXK 16
#define MAXN 1024
static int n,k,pi[MAXK];
static int sig[MAXN];
// cnt[i][v] = number of positions j >= i with sig[j] < v  (v in 0..n) -> prefix counts for pruning
static int *cnt; // (n+1)*(n+1)
static int chosen_val[MAXK];   // chosen_val[r] = value of pattern point r
static int chosen_pos[MAXK];

static int dfs(int r,int lastpos){
    if(r==k) return 1;
    // value window: largest chosen value with pattern rank < pi[r], smallest chosen value with rank > pi[r]
    int lo=-1,hi=n;
    for(int s=0;s<r;s++){
        if(pi[s]<pi[r]){ if(chosen_val[s]>lo) lo=chosen_val[s]; }
        else            { if(chosen_val[s]<hi) hi=chosen_val[s]; }
    }
    int need=k-r; // points still to place incl. this one
    // how many future pattern points have rank between the ranks bounding this window? -> need at least that many values in (lo,hi)
    // ranks of the window: lo has rank rl (max rank < pi[r] among chosen), hi rank rh; count pattern elems s>=r with rl<pi[s]<rh
    int rl=-1,rh=k;
    for(int s=0;s<r;s++){ if(pi[s]<pi[r]&&pi[s]>rl) rl=pi[s]; if(pi[s]>pi[r]&&pi[s]<rh) rh=pi[s]; }
    int needwin=0; for(int s=r;s<k;s++) if(pi[s]>rl&&pi[s]<rh) needwin++;
    for(int i=lastpos+1;i<=n-need;i++){
        int v=sig[i];
        if(v<=lo||v>=hi) continue;
        // prune: values in (lo,hi) at positions > i must be >= needwin-1
        int avail=cnt[(i+1)*(n+1)+hi]-cnt[(i+1)*(n+1)+lo+1];
        if(avail<needwin-1) continue;
        chosen_val[r]=v; chosen_pos[r]=i;
        if(dfs(r+1,i)) return 1;
    }
    return 0;
}

static int contains(void){ return dfs(0,-1); }

int main(int argc,char**argv){
    if(argc<5){fprintf(stderr,"usage: n samples seed pat...\n");return 1;}
    n=atoi(argv[1]); int samples=atoi(argv[2]); uint64_t seed=atoll(argv[3]);
    rng_s[0]=seed*0x9E3779B97F4A7C15ULL+1; rng_s[1]=seed^0xD1B54A32D192ED03ULL; for(int i=0;i<20;i++)rnd();
    int np=argc-4; long *hits=calloc(np,sizeof(long));
    cnt=malloc(sizeof(int)*(n+2)*(n+1));
    for(int t=0;t<samples;t++){
        for(int i=0;i<n;i++)sig[i]=i;
        for(int i=n-1;i>0;i--){int j=rnd()%(i+1);int tmp=sig[i];sig[i]=sig[j];sig[j]=tmp;}
        // prefix counts: cnt[i][v] = #{j>=i: sig[j]<v}
        for(int v=0;v<=n;v++) cnt[n*(n+1)+v]=0;
        for(int i=n-1;i>=0;i--){ for(int v=0;v<=n;v++) cnt[i*(n+1)+v]=cnt[(i+1)*(n+1)+v]+(sig[i]<v); }
        for(int p=0;p<np;p++){
            const char*s=argv[4+p]; k=0;
            if(strchr(s,',')){ char buf[256]; strncpy(buf,s,255); buf[255]=0; char*tok=strtok(buf,","); while(tok){pi[k++]=atoi(tok)-1;tok=strtok(NULL,",");} }
            else { for(;*s;s++) pi[k++]=*s-'1'; }
            {int h=contains(); hits[p]+=h; if(getenv("VERBOSE")) printf("S %d %d %d\n",t,p,h);}
        }
    }
    for(int p=0;p<np;p++) printf("%s %.4f\n",argv[4+p],(double)hits[p]/samples);
    return 0;
}
