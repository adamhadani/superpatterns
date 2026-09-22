// Verify the stored Bellman potentials as a supersolution with outward bounds.
// cc -O2 -std=c11 -ffp-contract=off -I/opt/homebrew/include \
//   certify_mpfr.c -L/opt/homebrew/lib -lmpfr -lgmp -lm -o certify_mpfr
// ./certify_mpfr dp_cert_eps0.02.txt 512 > mpfr_certificate.tsv
// Inputs are the exact binary64 values parsed from the potential table;
// their hexadecimal representations are included in the certificate.
#include <assert.h>
#include <fenv.h>
#include <float.h>
#include <math.h>
#include <mpfr.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct { double lo, hi; } I;
static mpfr_t mx, my;
static mpfr_t rm,rd,rt,rl,rh,rden,rnum;
static unsigned long evaluations;
#define EPS (1.0/64.0)
static double down(double x) { return nextafter(x, -INFINITY); }
static double up(double x) { return nextafter(x, INFINITY); }
static I pt(double x) { return (I){x,x}; }
static I add(I a,I b) { return (I){down(a.lo+b.lo),up(a.hi+b.hi)}; }
static I neg(I a) { return (I){-a.hi,-a.lo}; }
static I sub(I a,I b) { return add(a,neg(b)); }
static I mul(I a,I b) {
    double v[4]={a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi};
    double lo=v[0],hi=v[0];
    for(int j=1;j<4;j++){lo=fmin(lo,v[j]);hi=fmax(hi,v[j]);}
    return (I){down(lo),up(hi)};
}
static I divi(I a,I b) {
    assert(b.lo>0 || b.hi<0);
    return mul(a,(I){down(1/b.hi),up(1/b.lo)});
}
static I square(I a) {
    I v=mul(a,a); if(a.lo<=0 && a.hi>=0)v.lo=0;
    return v;
}
static I elementary(I a,int op) {
    I result;
    for(int j=0;j<2;j++) {
        mpfr_rnd_t rounding=j?MPFR_RNDU:MPFR_RNDD;
        mpfr_set_d(mx,j?a.hi:a.lo,MPFR_RNDN);
        if(op==0)mpfr_exp(my,mx,rounding);
        if(op==1)mpfr_log(my,mx,rounding);
        if(op==2)mpfr_sqrt(my,mx,rounding);
        double v=mpfr_get_d(my,rounding);
        if(j)result.hi=v;else result.lo=v;
    }
    return result;
}
static I iexp(I a){return elementary(a,0);}
static I ilog(I a){assert(a.lo>0);return elementary(a,1);}
static I isqrt(I a){assert(a.hi>=0);a.lo=fmax(0,a.lo);return elementary(a,2);}
static I clip(I a,double lo,double hi) {
    return (I){fmin(hi,fmax(lo,a.lo)),fmin(hi,fmax(lo,a.hi))};
}

typedef struct { I area,width; } Section;
static Section section(double s,double A,double B) {
    evaluations++;
    I S=pt(s),a=pt(A),b=pt(B),zero=pt(0);
    // Exact complementary dyadic endpoints preserve A/B reflection symmetry.
    // These windows contain the old epsilon=0.02 windows. The old table is
    // only a candidate; every supersolution inequality is checked anew.
    double lo=A>0?EPS:0, hi=B>0?1.0-EPS:1;
    if(A==0 && B==0)return (Section){S,pt(1)};
    // For the bounded binary64 inputs below, the quadratic discriminant is
    // an EXACT dyadic polynomial at 256 bits. This avoids interval dependency
    // inflation at its double root. Square roots/divisions remain directed.
    assert(s>=1 && s<0x1p24 && (A==0 || (A>=1 && A<0x1p24)) && (B==0 || (B>=1 && B<0x1p24)));
    mpfr_set_d(rm,s,MPFR_RNDN);mpfr_add_d(rm,rm,A,MPFR_RNDN);mpfr_sub_d(rm,rm,B,MPFR_RNDN);
    mpfr_mul(rd,rm,rm,MPFR_RNDN);
    mpfr_set_d(rt,s,MPFR_RNDN);mpfr_mul_d(rt,rt,A,MPFR_RNDN);mpfr_mul_2ui(rt,rt,2,MPFR_RNDN);
    mpfr_sub(rd,rd,rt,MPFR_RNDN);
    if(mpfr_sgn(rd)<=0)return (Section){zero,zero};
    mpfr_sqrt(rl,rd,MPFR_RNDD);mpfr_sqrt(rh,rd,MPFR_RNDU);
    mpfr_set_d(rden,s,MPFR_RNDN);mpfr_mul_2ui(rden,rden,1,MPFR_RNDN);
    I y1,y2;
    mpfr_sub(rnum,rm,rh,MPFR_RNDD);mpfr_div(rnum,rnum,rden,MPFR_RNDD);y1.lo=mpfr_get_d(rnum,MPFR_RNDD);
    mpfr_sub(rnum,rm,rl,MPFR_RNDU);mpfr_div(rnum,rnum,rden,MPFR_RNDU);y1.hi=mpfr_get_d(rnum,MPFR_RNDU);
    mpfr_add(rnum,rm,rl,MPFR_RNDD);mpfr_div(rnum,rnum,rden,MPFR_RNDD);y2.lo=mpfr_get_d(rnum,MPFR_RNDD);
    mpfr_add(rnum,rm,rh,MPFR_RNDU);mpfr_div(rnum,rnum,rden,MPFR_RNDU);y2.hi=mpfr_get_d(rnum,MPFR_RNDU);
    y1=clip(y1,lo,hi);y2=clip(y2,lo,hi);
    if(y2.hi<=y1.lo)return (Section){zero,zero};
    I width=sub(y2,y1), area=mul(S,width);
    if(A>0)area=sub(area,mul(a,ilog(divi(y2,y1))));
    if(B>0)area=add(area,mul(b,ilog(divi(sub(pt(1),y2),sub(pt(1),y1)))));
    if(width.lo<=0)area.lo=0;
    area.lo=fmax(0,area.lo);area.hi=fmax(0,area.hi);
    width.lo=fmax(0,width.lo);width.hi=fmax(0,width.hi);
    assert(area.lo<=area.hi && isfinite(area.hi));
    return (Section){area,width};
}

static double log_sinhc_upper(double z) {
    if(z==0)return 0;
    mpfr_set_d(mx,z,MPFR_RNDN);
    mpfr_sinh(my,mx,MPFR_RNDU);
    mpfr_div(my,my,mx,MPFR_RNDU);
    mpfr_log(my,my,MPFR_RNDU);
    return fmax(0,mpfr_get_d(my,MPFR_RNDU));
}
static double exp_ratio_lower(double d) {
    // (1-exp(-d))/d, decreasing in d>=0; no subtractive cancellation.
    if(d==0)return 1;
    mpfr_set_d(mx,-d,MPFR_RNDN);
    mpfr_expm1(my,mx,MPFR_RNDU);
    mpfr_neg(my,my,MPFR_RNDD);
    mpfr_div_d(my,my,d,MPFR_RNDD);
    return mpfr_get_d(my,MPFR_RNDD);
}

static double integrate(double left,double right,Section sl,Section sr,
                        double A,double B,double tolerance,int depth) {
    if(depth>=45){fprintf(stderr,"quadrature unresolved A=%.17g B=%.17g left=%.17g right=%.17g tol=%.17g\n",A,B,left,right,tolerance);exit(2);}
    double mid=(left+right)/2;
    assert(mid>left && mid<right);
    Section sm=section(mid,A,B);
    I h=sub(pt(right),pt(left));
    double upper_rect=mul(h,iexp(neg(sl.area))).hi;
    // Convex area lies above its tangent. Integrate that tangent's
    // exponential on the symmetric interval, with a slope upper bound.
    // The midpoint may incur binary rounding: use the larger half-width
    // and enlarge to a symmetric interval about the exact dyadic mid.
    double half=up(fmax(mid-left,right-mid));
    I full=mul(pt(2),pt(half));
    double z=mul(sm.width,pt(half)).hi;
    I log_upper=add(sub(ilog(full),pt(sm.area.lo)),pt(log_sinhc_upper(z)));
    double upper=fmin(upper_rect,iexp(log_upper).hi);

    // Convex area lies below the chord of upper endpoint enclosures.
    double difference=fmax(0,up(sr.area.hi-sl.area.hi));
    double lower=mul(mul(h,iexp(pt(-fmax(sl.area.hi,sr.area.hi-difference)))),
                     pt(exp_ratio_lower(difference))).lo;
    // The expression above uses the left endpoint. If endpoint intervals
    // cross, a constant upper area bound supplies a simpler valid lower bound.
    if(sr.area.hi<sl.area.hi)
        lower=mul(h,iexp(pt(-sl.area.hi))).lo;
    assert(lower<=upper && lower>=0 && isfinite(upper));
    if(up(upper-lower)<=tolerance)return upper;
    double first=integrate(left,mid,sl,sm,A,B,tolerance/2,depth+1);
    double second=integrate(mid,right,sm,sr,A,B,tolerance/2,depth+1);
    return up(first+second);
}

static double W_upper(double A,double B) {
    if(A==0 && B==0)return 1;
    double lo=A>0?EPS:0,hi=B>0?1.0-EPS:1;
    double y=fmin(hi,fmax(lo,sqrt(A)/(sqrt(A)+sqrt(B))));
    I minimum=pt(0);
    if(A>0)minimum=add(minimum,divi(pt(A),pt(y)));
    if(B>0)minimum=add(minimum,divi(pt(B),sub(pt(1),pt(y))));
    // Any feasible y gives an upper bound on the true minimum. The interval
    // below this start contributes at most start, since survival<=1.
    double start=minimum.hi, step=1, end,tail;
    double tolerance=1e-5*(A+B+1); // controls refinement, never a proof margin
    Section se;
    for(int j=0;;j++) {
        assert(j<60);
        end=up(start+step);se=section(end,A,B);
        tail=se.width.lo>0?divi(iexp(neg(se.area)),se.width).hi:INFINITY;
        if(tail<tolerance/16)break;
        step*=2;
    }
    Section ss=section(start,A,B);
    double integral=integrate(start,end,ss,se,A,B,tolerance,0);
    return add(add(pt(start),pt(integral)),pt(tail)).hi;
}

int main(int argc,char **argv) {
    if(argc!=3){fprintf(stderr,"usage: %s potentials.txt max_n\n",argv[0]);return 2;}
    assert(FLT_RADIX==2 && DBL_MANT_DIG==53 && fegetround()==FE_TONEAREST);
    mpfr_init2(mx,128);mpfr_init2(my,128);
    mpfr_inits2(256,rm,rd,rt,rl,rh,rden,rnum,(mpfr_ptr)0);
    int maxn=atoi(argv[2]);if(maxn<2 || maxn>512)return 2;
    double values[513]={0};
    FILE *input=fopen(argv[1],"r");if(!input){perror(argv[1]);return 2;}
    char line[512];int found=0;
    while(fgets(line,sizeof(line),input)) {
        int n;double v,ratio;
        if(sscanf(line,"%d %lf %lf",&n,&v,&ratio)==3 && n<=maxn) {
            assert(n==found+1 && v>values[n-1]); values[n]=v;found=n;
        }
    }
    fclose(input);assert(found==maxn);
    assert(W_upper(0,0)==1);
    double test=W_upper(1,0);assert(test>=3 && test<3.001);
    fprintf(stderr,"MPFR %s; 128-bit directed transcendentals; W(1,0) upper %.17g\n",mpfr_get_version(),test);
    puts("n\tpotential_hex\tpotential\trecurrence_upper\tgap_lower\tratio_upper\tevaluations");
    for(int n=1;n<=maxn;n++) {
        I sum=pt(0);
        for(int m=0;m<=(n-1)/2;m++) {
            double w=W_upper(values[m],values[n-1-m]);
            sum=add(sum,mul(pt(m==n-1-m?1:2),pt(w)));
        }
        I recurrence=divi(sum,pt(n)),gap=sub(pt(values[n]),recurrence);
        I ratio=divi(pt(values[n]),pt(n*n));
        printf("%d\t%a\t%.17g\t%.17g\t%.17g\t%.17g\t%lu\n",n,values[n],values[n],recurrence.hi,gap.lo,ratio.hi,evaluations);
        fflush(stdout);
        if(gap.lo<0){fprintf(stderr,"FAIL at n=%d: candidate is not certified\n",n);return 1;}
    }
    if(maxn==512)assert(divi(pt(values[maxn]),pt(maxn*maxn)).hi<divi(pt(4649),pt(10000)).lo);
    fprintf(stderr,"PASS: every recurrence inequality through n=%d; epsilon=1/64\n",maxn);
    mpfr_clear(mx);mpfr_clear(my);
    mpfr_clears(rm,rd,rt,rl,rh,rden,rnum,(mpfr_ptr)0);
    return 0;
}
