/* W29: y-only reserve/band greedy on a strip of h values with a uniformly random sub-pattern.
   Outputs Omega_h = E[sum_i 1/W_i]/h (threshold constant of the rule), plus sd of the per-strip cost.
   usage: strip h w beta mode wmin nsamp seed
   mode 0: absolute target y0 = v+1/2 ; mode 1: proportional target in gap ; mode 2: no band (window = reserve interval)
   band [y0-w/2,y0+w/2] ∩ reserve; if length < wmin the band is widened symmetrically until length = wmin
   (reserve interval always has length >= beta, so take wmin <= beta). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
static uint64_t s[2];
static inline uint64_t rotl(uint64_t x,int k){return (x<<k)|(x>>(64-k));}
static inline uint64_t nxt(void){uint64_t s0=s[0],s1=s[1],r=s0+s1;s1^=s0;s[0]=rotl(s0,55)^s1^(s1<<14);s[1]=rotl(s1,36);return r;}
static inline double unif(void){return (nxt()>>11)*(1.0/9007199254740992.0);}
static double isect(double lo,double hi,double y0,double sh){double a=fmax(lo,y0-sh),b=fmin(hi,y0+sh);return b-a;}
int main(int argc,char**argv){
  int h=atoi(argv[1]); double w=atof(argv[2]),beta=atof(argv[3]); int mode=atoi(argv[4]); double wmin=atof(argv[5]);
  long ns=atol(argv[6]); uint64_t seed=atoll(argv[7]); double Cc=(argc>8)?atof(argv[8]):0; int NT=40; double *lm=calloc(NT,sizeof(double)); double *logw=malloc(h*sizeof(double)); s[0]=seed*0x9E3779B97F4A7C15ULL+1; s[1]=seed^0xDEADBEEFCAFEULL; for(int i=0;i<20;i++)nxt();
  int *perm=malloc(h*sizeof(int)); char*placed=malloc(h); double*y=malloc(h*sizeof(double));
  double sum=0,sum2=0; double minW=1e9;
  for(long t=0;t<ns;t++){
    for(int i=0;i<h;i++)perm[i]=i;
    for(int i=h-1;i>0;i--){int j=nxt()%(i+1);int tmp=perm[i];perm[i]=perm[j];perm[j]=tmp;}
    for(int i=0;i<h;i++)placed[i]=0;
    double cost=0;
    for(int i=0;i<h;i++){
      int v=perm[i]; int L=v-1; while(L>=0&&!placed[L])L--; int R=v+1; while(R<h&&!placed[R])R++;
      double yL=(L<0)?0:y[L], yR=(R>=h)?h:y[R]; int mb=v-L-1, ma=R-v-1;
      double lo=yL+beta*mb, hi=yR-beta*ma;
      double a=lo,b=hi;
      if(mode!=2){
        double y0=(mode==0)? v+0.5 : yL+(yR-yL)*(mb+0.5)/(mb+ma+1);
        double sh=w/2; double len=isect(lo,hi,y0,sh);
        if(len<wmin){ /* widen: bisection on sh in [w/2, hi-lo+|y0-lo|+|hi-y0|] */
          double s1=sh,s2=(hi-lo)+fabs(y0-lo)+fabs(hi-y0)+1;
          for(int it=0;it<60;it++){double sm=0.5*(s1+s2); if(isect(lo,hi,y0,sm)<wmin)s1=sm;else s2=sm;}
          sh=s2;
        }
        a=fmax(lo,y0-sh); b=fmin(hi,y0+sh);
      }
      double W=b-a; if(W<minW)minW=W; cost+=1.0/W; logw[i]=W; y[v]=a+W*unif(); placed[v]=1;
    }
    sum+=cost; sum2+=cost*cost;
    if(Cc>0){ for(int j=1;j<NT;j++){ double th=Cc*beta*j/NT, lp=0; for(int i=0;i<h;i++) lp-=log(1.0-th/(Cc*logw[i])); lm[j]+=exp(lp);} }
  }
  double m=sum/ns, var=sum2/ns-m*m;
  printf("h=%d w=%g beta=%g mode=%d wmin=%g ns=%ld  Omega=%.5f  sd(T/h)=%.5f minW=%.4f\n",h,w,beta,mode,wmin,ns,m/h,sqrt(var>0?var:0)/h,minW);
  if(Cc>0){ double best=-1e9; int bj=0; for(int j=1;j<NT;j++){ double th=Cc*beta*j/NT; double e=(th*h-log(lm[j]/ns))/h; if(e>best){best=e;bj=j;} } printf("  C=%g: Chernoff exponent per point eta=%.5f at theta=%.4f (MGF via windows, ns=%ld)\n",Cc,best,Cc*beta*bj/NT,ns);}
  return 0;
}
