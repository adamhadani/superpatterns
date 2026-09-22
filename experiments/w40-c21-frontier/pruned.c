// Exact repeated-21 frontier, O(n log n) time and O(n) space.
// One global segment tree; see pruning.md for the dominance proof.
// Input/output as frontier.c; --trace additionally prints all finite F_m.
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { int *minimum; unsigned char *cleared; int base, infinity; } Tree;

static void clear_node(Tree *t, int node) {
    t->minimum[node]=t->infinity; t->cleared[node]=1;
}
static void push(Tree *t, int node) {
    if(t->cleared[node]) {
        clear_node(t,2*node); clear_node(t,2*node+1); t->cleared[node]=0;
    }
}
static void pull(Tree *t, int node) {
    int a=t->minimum[2*node], b=t->minimum[2*node+1];
    t->minimum[node]=a<b?a:b;
}
static void clear_range(Tree *t,int node,int lo,int hi,int a,int b) {
    if(b<lo || hi<a)return;
    if(a<=lo && hi<=b){clear_node(t,node);return;}
    push(t,node);int mid=(lo+hi)/2;
    clear_range(t,2*node,lo,mid,a,b);
    clear_range(t,2*node+1,mid+1,hi,a,b);pull(t,node);
}
static void insert(Tree *t,int node,int lo,int hi,int y,int lower) {
    if(lo==hi){t->minimum[node]=lower;t->cleared[node]=0;return;}
    push(t,node);int mid=(lo+hi)/2;
    if(y<=mid)insert(t,2*node,lo,mid,y,lower);
    else insert(t,2*node+1,mid+1,hi,y,lower);
    pull(t,node);
}
static int first_cover(Tree *t,int node,int lo,int hi,int y) {
    if(hi<=y || t->minimum[node]>=y)return 0;
    if(lo==hi)return lo;
    push(t,node);int mid=(lo+hi)/2;
    int found=first_cover(t,2*node,lo,mid,y);
    return found?found:first_cover(t,2*node+1,mid+1,hi,y);
}
static int solve(const int *values,int n,int trace) {
    Tree t={0};t.base=1;t.infinity=n+1;
    while(t.base<n)t.base*=2;
    t.minimum=malloc((size_t)2*t.base*sizeof(int));
    t.cleared=calloc((size_t)2*t.base,1);
    int *f=malloc((size_t)(n/2+2)*sizeof(int));
    if(!t.minimum||!t.cleared||!f){perror("allocation");exit(2);}
    for(int i=0;i<2*t.base;i++)t.minimum[i]=t.infinity;
    int maximum=0;f[0]=0;f[1]=t.infinity;
    for(int i=0;i<n;i++) {
        int y=values[i],lo=0,hi=maximum+1;
        while(lo+1<hi){int mid=(lo+hi)/2;if(f[mid]<y)lo=mid;else hi=mid;}
        int j=lo, old_right=f[j+1];
        assert(f[j]<y && y<old_right);
        int z=first_cover(&t,1,1,t.base,y);
        if(z) {
            assert(y<z && z<old_right);
            clear_range(&t,1,1,t.base,z,old_right-1);
            f[j+1]=z;
            if(j==maximum){maximum++;f[maximum+1]=t.infinity;}
        }
        insert(&t,1,1,t.base,y,f[j]);
        if(trace) {
            printf("%d",maximum);
            for(int m=1;m<=maximum;m++)printf(" %d",f[m]);
            putchar('\n');
        }
    }
    free(t.minimum);free(t.cleared);free(f);return maximum;
}
int main(int argc,char **argv) {
    int trace=argc==2&&!strcmp(argv[1],"--trace");
    if(argc!=1&&!trace)return 2;
    int n;
    while(scanf("%d",&n)==1) {
        if(n<1||n>10000000)return 2;
        int *values=malloc((size_t)n*sizeof(int));
        unsigned char *seen=calloc((size_t)n+1,1);
        if(!values||!seen)return 2;
        for(int i=0;i<n;i++) {
            if(scanf("%d",values+i)!=1||values[i]<1||values[i]>n||seen[values[i]])return 2;
            seen[values[i]]=1;
        }
        int answer=solve(values,n,trace);
        if(!trace)printf("%d\n",answer);
        free(values);free(seen);
    }
    return 0;
}
