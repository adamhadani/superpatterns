// leftmost-canonical test (W12 §2.1): copy A (positions a[0..k-1] sorted, 1-based, values v[i]=sigma[a[i]]) is canonical iff
// for every r the strip (a[r-1], a[r]) x (prev value in A, next value in A) contains no point of sigma (a[-1]:=0; values 0/N+1 at ends).
// P[x][y] = #{q<=x : sigma(q)<=y}, sigma 1-based.
static int *P_; static int NP_;
static inline int rect(int x1,int x2,int y1,int y2){ // count points with x1<=x<=x2, y1<=y<=y2 (inclusive), empty if x1>x2 or y1>y2
  if(x1>x2||y1>y2) return 0; return P_[x2*NP_+y2]-P_[(x1-1)*NP_+y2]-P_[x2*NP_+(y1-1)]+P_[(x1-1)*NP_+(y1-1)]; }
static void build_prefix(const int *sigma1,int N){ // sigma1[1..N]
  NP_=N+1; for(int x=0;x<=N;x++) for(int y=0;y<=N;y++) P_[x*NP_+y]= x==0||y==0?0: P_[(x-1)*NP_+y]+P_[x*NP_+(y-1)]-P_[(x-1)*NP_+(y-1)]+(sigma1[x]==y);
}
static int is_canonical(const int *a,const int *v,int k,int N){
  for(int r=0;r<k;r++){ int lo=0,hi=N+1; for(int i=0;i<k;i++){ if(v[i]<v[r]&&v[i]>lo) lo=v[i]; if(v[i]>v[r]&&v[i]<hi) hi=v[i]; }
    int x1=(r==0?0:a[r-1])+1, x2=a[r]-1; if(rect(x1,x2,lo+1,hi-1)) return 0; }
  return 1;
}
