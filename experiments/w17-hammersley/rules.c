/* rules.c -- Monte Carlo for local ("renewal") 21-chain construction rules in the
   scaled Poisson process (intensity 1 on the plane).  A rule starts at a corner c,
   explores a region above-right of c, finds a descent pair (a,b) (a above-left of b)
   and moves the corner to (x_b, y_a).  Increments (dx,dy) are i.i.d. as long as the
   explored region has x <= x_b (strip sweep) or one of the new pair's points lies on the
   sweep boundary (growing square).  Then c_21 >= 2/E[dx+dy] (alternating with the
   transposed rule) and >= 1/max(E dx, E dy).
   Usage: ./rules <rule> <param1> <param2> <nsamples> [seed]
     rule 0: strip of height h=param1, first descent, a = lowest seen point above b.
     rule 1: growing square, first descent (a lowest / b leftmost).
     rule 2: growing square, accept the pair completed at scale m iff cost <= param1*m.
     rule 3: strip h=param1, accept descent iff h*V_a <= param2 + (elapsed dx) * param3(=1).
     rule 4: strip h=param1, first copy of pattern tau (param2 = tau as digits, e.g. 321)
             ending at the current point; Delta y = top of the copy (min over copies).
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
static unsigned long long s[4];
static inline unsigned long long rotl(unsigned long long x,int k){return (x<<k)|(x>>(64-k));}
static unsigned long long next(void){unsigned long long r=rotl(s[1]*5,7)*9,t=s[1]<<17;s[2]^=s[0];s[3]^=s[1];s[1]^=s[2];s[0]^=s[3];s[2]^=t;s[3]=rotl(s[3],45);return r;}
static inline double U(void){return (next()>>11)*(1.0/9007199254740992.0);}
static inline double Exp(double rate){double u; do u=U(); while(u<=0); return -log(u)/rate;}
#define MAXP 4096
int main(int argc,char**argv){
  int rule=atoi(argv[1]); double p1=atof(argv[2]), p2=atof(argv[3]); long ns=atol(argv[4]);
  unsigned long long seed=argc>5?atoll(argv[5]):12345; s[0]=seed^0x9E3779B97F4A7C15ULL;s[1]=seed*7+1;s[2]=seed*13+5;s[3]=seed*31+9; for(int i=0;i<20;i++)next();
  double sx=0,sy=0,sc=0,sc2=0; long maxn=0; double sn=0;
  static double px[MAXP],py[MAXP];
  int tau[16],J=0; if(rule==4){char*t=argv[3];J=strlen(t);for(int i=0;i<J;i++)tau[i]=t[i]-'0';}
  for(long it=0;it<ns;it++){
    double dx=0,dy=0; int n=0;

    if(rule==5){ /* l_p sweep: explored region {(u^p+v^p)^{1/p} < s}; first descent; new point may be a or b */
      double P=p1; double t=0; n=0;
      /* area of unit lp ball in positive quadrant: A = Gamma(1+1/p)^2/Gamma(1+2/p) */
      double A=exp(2*lgamma(1+1/P)-lgamma(1+2/P));
      for(;;){
        t+=Exp(1.0); double sc_=sqrt(t/A);
        double u,v; do{u=U();v=U();}while(pow(pow(u,P)+pow(v,P),1/P)>1.0); double r=pow(pow(u,P)+pow(v,P),1/P); u=u/r*sc_; v=v/r*sc_;
        double bestcost=1e300,bdx=0,bdy=0;
        { double lowest=1e300; for(int i=0;i<n;i++) if(px[i]<u && py[i]>v && py[i]<lowest) lowest=py[i];
          if(lowest<1e299 && u+lowest<bestcost){bestcost=u+lowest;bdx=u;bdy=lowest;} }
        { double leftmost=1e300; for(int i=0;i<n;i++) if(px[i]>u && py[i]<v && px[i]<leftmost) leftmost=px[i];
          if(leftmost<1e299 && leftmost+v<bestcost){bestcost=leftmost+v;bdx=leftmost;bdy=v;} }
        n++;
        if(bestcost<1e299){dx=bdx;dy=bdy;break;}
        px[n-1]=u;py[n-1]=v; if(n>=MAXP){fprintf(stderr,"overflow\n");exit(1);}
      }
    } else
    if(rule==0||rule==3||rule==4){
      double h=p1; double x=0;
      for(;;){
        x+=Exp(h); double v=U()*h; /* new point (x,v) */
        if(rule==4){
          /* find copies of tau among seen points + new as last; need J-1 earlier points in x-order
             with y-pattern tau; minimize top height. brute force over combinations (J<=4). */
          double best=1e300;
          if(n>=J-1){
            if(J==2){ for(int i=0;i<n;i++){ double ya=py[i],yb=v; int ok=(tau[0]<tau[1])?(ya<yb):(ya>yb); if(ok){double top=ya>yb?ya:yb; if(top<best)best=top;} } }
            else if(J==3){ for(int i=0;i<n;i++)for(int k=i+1;k<n;k++){ double y[3]={py[i],py[k],v}; int ok=1; for(int a=0;a<3&&ok;a++)for(int b=a+1;b<3;b++){ if((tau[a]<tau[b])!=(y[a]<y[b])){ok=0;break;} } if(ok){double top=y[0];if(y[1]>top)top=y[1];if(y[2]>top)top=y[2]; if(top<best)best=top;} } }
            else if(J==4){ for(int i=0;i<n;i++)for(int k=i+1;k<n;k++)for(int l=k+1;l<n;l++){ double y[4]={py[i],py[k],py[l],v}; int ok=1; for(int a=0;a<4&&ok;a++)for(int b=a+1;b<4;b++){ if((tau[a]<tau[b])!=(y[a]<y[b])){ok=0;break;} } if(ok){double top=y[0];for(int q=1;q<4;q++)if(y[q]>top)top=y[q]; if(top<best)best=top;} } }
          }
          if(best<1e299){dx=x;dy=best;n++;break;}
          px[n]=x;py[n]=v;n++; if(n>=MAXP){fprintf(stderr,"overflow\n");exit(1);} continue;
        }
        double lowest=1e300; for(int i=0;i<n;i++) if(py[i]>v && py[i]<lowest) lowest=py[i];
        n++;
        if(lowest<1e299){
          int accept=1;
          if(rule==3) accept = (lowest <= p2 + x); /* threshold grows with elapsed dx */
          if(accept){dx=x;dy=lowest;break;}
        }
        px[n-1]=x;py[n-1]=v; if(n>=MAXP){fprintf(stderr,"overflow\n");exit(1);}
      }
    } else { /* growing square */
      double t=0;
      for(;;){
        t+=Exp(1.0); double m=sqrt(t); int right=(next()&1); double w=U()*m; /* other coordinate */
        double cx,cy; if(right){cx=m;cy=w;}else{cx=w;cy=m;}
        double bestcost=1e300,bdx=0,bdy=0;
        if(right){ /* new point is b at (m,w); a = lowest earlier point with y>w */
          double lowest=1e300; for(int i=0;i<n;i++) if(py[i]>w && py[i]<lowest) lowest=py[i];
          if(lowest<1e299){bestcost=m+lowest;bdx=m;bdy=lowest;}
        } else { /* new point is a at (w,m); b = leftmost earlier point with x>w */
          double leftmost=1e300; for(int i=0;i<n;i++) if(px[i]>w && px[i]<leftmost) leftmost=px[i];
          if(leftmost<1e299){bestcost=m+leftmost;bdx=leftmost;bdy=m;}
        }
        n++;
        if(bestcost<1e299){
          int accept=1; if(rule==2) accept=(bestcost<=p1*m);
          if(accept){dx=bdx;dy=bdy;break;}
        }
        px[n-1]=cx;py[n-1]=cy; if(n>=MAXP){fprintf(stderr,"overflow\n");exit(1);}
      }
    }
    sx+=dx;sy+=dy;sc+=dx+dy;sc2+=(dx+dy)*(dx+dy);sn+=n; if(n>maxn)maxn=n;
  }
  double Ex=sx/ns,Ey=sy/ns,Ec=sc/ns,se=sqrt((sc2/ns-Ec*Ec)/ns);
  double mx=Ex>Ey?Ex:Ey;
  printf("rule %d p1 %g p2 %g ns %ld: E dx %.5f E dy %.5f E cost %.5f (se %.5f) E n %.4f maxn %ld | 1/max %.5f  2/Ecost %.5f\n",rule,p1,p2,ns,Ex,Ey,Ec,se,sn/ns,maxn,1/mx,2/Ec);
  return 0;
}
