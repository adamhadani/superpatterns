// Exact maximum number of direct-summed 21 pairs, with all pending choices.
// cc -O3 -std=c11 frontier.c -lm -o frontier
// stdin: one line N followed by a permutation of 1..N; stdout: max pairs.
// Or: frontier --random N HOSTS SEED (CSV sample output).
#include "../w38-second-moment/common.h"
#include <assert.h>

static int base, inf;
static int first_match(const int *tree,int node,int lo,int hi,int start,int y) {
    if(hi<start || tree[node]>=y)return 0;
    if(lo==hi)return lo;
    int mid=(lo+hi)/2;
    int answer=first_match(tree,2*node,lo,mid,start,y);
    return answer?answer:first_match(tree,2*node+1,mid+1,hi,start,y);
}
static void insert(int *tree,int z,int lower) {
    int index=base+z-1;
    if(lower>=tree[index])return;
    tree[index]=lower;
    for(index/=2;index;index/=2)
        tree[index]=tree[2*index]<tree[2*index+1]?tree[2*index]:tree[2*index+1];
}
static int *new_tree(void) {
    int *tree=malloc((size_t)2*base*sizeof(*tree));
    if(!tree){perror("malloc");exit(2);}
    for(int i=0;i<2*base;i++)tree[i]=inf;
    return tree;
}
static int maximum_pairs(const int *values,int n) {
    base=1;while(base<n)base*=2;inf=n+1;
    int **trees=calloc(n/2+2,sizeof(*trees)), *completed=malloc((n/2+2)*sizeof(*completed));
    if(!trees||!completed)exit(2);
    for(int i=0;i<n/2+2;i++)completed[i]=inf;
    completed[0]=0;trees[0]=new_tree();int maximum=0;
    for(int i=0;i<n;i++) {
        int y=values[i],old_maximum=maximum;
        // Descending order ensures completed[m] still refers to the prefix
        // BEFORE the current point when it starts a new pending pair.
        for(int m=old_maximum;m>=0;m--) {
            int z=first_match(trees[m],1,1,base,y+1,y);
            if(z && z<completed[m+1]) {
                completed[m+1]=z;
                if(m+1>maximum){maximum=m+1;trees[maximum]=new_tree();}
            }
            if(completed[m]<y)insert(trees[m],y,completed[m]);
        }
    }
    for(int m=0;m<=maximum;m++)free(trees[m]);free(trees);free(completed);
    return maximum;
}
int main(int argc,char **argv) {
    if(argc==5 && !strcmp(argv[1],"--random")) {
        int n=atoi(argv[2]),hosts=atoi(argv[3]);if(n<2||n>100000||hosts<1)return 2;
        seed_rng(strtoull(argv[4],NULL,10));int *v=malloc(n*sizeof(*v));if(!v)return 2;
        puts("host,n,pairs,normalized");
        for(int h=0;h<hosts;h++) {
            for(int i=0;i<n;i++)v[i]=i+1;shuffle(v,n);
            int m=maximum_pairs(v,n);
            printf("%d,%d,%d,%.12g\n",h,n,m,m/sqrt(n));fflush(stdout);
        }
        free(v);return 0;
    }
    if(argc!=1)return 2;
    int n;
    while(scanf("%d",&n)==1) {
        if(n<1||n>100000)return 2;
        int *v=malloc(n*sizeof(*v));unsigned char *seen=calloc(n+1,1);
        if(!v||!seen)return 2;
        for(int i=0;i<n;i++) {
            if(scanf("%d",v+i)!=1 || v[i]<1 || v[i]>n || seen[v[i]])return 2;
            seen[v[i]]=1;
        }
        printf("%d\n",maximum_pairs(v,n));free(v);free(seen);
    }
    return 0;
}
