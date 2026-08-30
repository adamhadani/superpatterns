// W37: exact containment counts for ALL patterns of length 3..7 simultaneously.
// Enumerates all sigma in S_n with sigma(1)=a, sigma(n)=b (1-based values); for each pattern
// length j<=K and each pattern index (Lehmer rank), counts the number of sigma containing it.
// Method: DFS over prefixes; maintain, for each j, the list of all j-subsets of the prefix as
// (value bitmask, pattern index); extending a (j-1)-subset by the new element costs O(1) via a
// precomputed extension table.  A pattern is counted with multiplicity fact[#free slots] the
// first time it appears in the prefix (first_dep stamp), so each sigma is counted exactly once.
// usage: allpat n a b outfile     (n<=16, K=min(7,n))
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define KMAX 7
static int N, A, B, K;
static int factj[KMAX + 2];               // j! for pattern lengths
static uint64_t factn[20];                // n!
static uint16_t *ext[KMAX];               // ext[j]: (j! x (j+1)) table: extend length-j pattern
static const int JFACT[8] = {1, 1, 2, 6, 24, 120, 720, 5040};

static int rankp(const int *p, int j) {
    int r = 0;
    for (int i = 0; i < j; i++) {
        int c = 0;
        for (int t = i + 1; t < j; t++) if (p[t] < p[i]) c++;
        r = r * (j - i) + c;
    }
    return r;
}
static void unrankp(int idx, int j, int *p) {
    int code[KMAX + 1];
    for (int i = j - 1; i >= 0; i--) { code[i] = idx % (j - i); idx /= (j - i); }
    // wrong order: recompute properly
    // (radix: rank = ((c0*(j-1)+c1)*(j-2)+c2)... ) -> extract from the right
    // handled below; p filled from code
    int used[KMAX + 1];
    memset(used, 0, sizeof(used));
    for (int i = 0; i < j; i++) {
        int c = code[i], v = 0;
        while (1) { if (!used[v]) { if (c == 0) break; c--; } v++; }
        used[v] = 1; p[i] = v;
    }
}
static void build_ext(void) {
    for (int j = 0; j < KMAX; j++) {
        ext[j] = malloc(sizeof(uint16_t) * (size_t)JFACT[j] * (j + 1));
        int p[KMAX + 1], q[KMAX + 1];
        for (int idx = 0; idx < JFACT[j]; idx++) {
            unrankp(idx, j, p);
            if (rankp(p, j) != idx) { fprintf(stderr, "unrank bug\n"); exit(1); }
            for (int r = 0; r <= j; r++) {
                for (int t = 0; t < j; t++) q[t] = p[t] + (p[t] >= r ? 1 : 0);
                q[j] = r;
                ext[j][(size_t)idx * (j + 1) + r] = (uint16_t)rankp(q, j + 1);
            }
        }
    }
}

typedef struct { uint16_t mask; uint16_t idx; } Ent;
static Ent *list[KMAX + 1];
static int sz[KMAX + 1];
static int8_t *first_dep[KMAX + 1];
static uint64_t *cnt[KMAX + 1];
typedef struct { uint8_t j; uint16_t idx; } Undo;
static Undo undo_stack[1 << 16];
static int undo_top;

static int oldsz_stack[20][KMAX + 1];
static int undo_mark[20];

// place value v (0-based) at depth d (1-based number of placed elements after placing)
static void place(int v, int d) {
    uint64_t comp = factn[N - 1 - d >= 0 ? N - 1 - d : 0];
    uint32_t low = (1u << v) - 1;
    for (int j = (d < K ? d : K); j >= 1; j--) {
        int m = sz[j - 1];
        Ent *src = list[j - 1];
        Ent *dst = list[j];
        int s = sz[j];
        const uint16_t *E = ext[j - 1];
        int8_t *fd = first_dep[j];
        uint64_t *cj = cnt[j];
        for (int i = 0; i < m; i++) {
            uint16_t mask = src[i].mask;
            int r = __builtin_popcount(mask & low);
            uint16_t ni = E[(size_t)src[i].idx * j + r];
            dst[s].mask = mask | (1u << v);
            dst[s].idx = ni;
            s++;
            if (fd[ni] < 0) {
                fd[ni] = (int8_t)d;
                undo_stack[undo_top].j = (uint8_t)j;
                undo_stack[undo_top].idx = ni;
                undo_top++;
                cj[ni] += comp;
            }
        }
        sz[j] = s;
    }
}
static void save(int d) { memcpy(oldsz_stack[d], sz, sizeof(sz)); undo_mark[d] = undo_top; }
static void restore(int d) {
    memcpy(sz, oldsz_stack[d], sizeof(sz));
    while (undo_top > undo_mark[d]) {
        undo_top--;
        first_dep[undo_stack[undo_top].j][undo_stack[undo_top].idx] = -1;
    }
}

static void dfs(int d, uint32_t used) {
    // d = number placed so far; next placement is depth d+1
    if (d == N - 1) {
        save(d);
        place(B, N);   // depth N: last position
        restore(d);
        return;
    }
    for (int v = 0; v < N; v++) {
        if (used & (1u << v)) continue;
        if (v == B) continue;
        save(d);
        place(v, d + 1);
        dfs(d + 1, used | (1u << v));
        restore(d);
    }
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: allpat n a b outfile\n"); return 1; }
    N = atoi(argv[1]); A = atoi(argv[2]) - 1; B = atoi(argv[3]) - 1;
    if (N > 16) { fprintf(stderr, "n too big\n"); return 1; }
    K = N < KMAX ? N : KMAX;
    factn[0] = 1;
    for (int i = 1; i < 20; i++) factn[i] = factn[i - 1] * i;
    build_ext();
    for (int j = 0; j <= KMAX; j++) {
        int cap = 1;                       // C(n,j) bound: use generous 1<<n
        cap = 1 << N;
        list[j] = malloc(sizeof(Ent) * (size_t)cap);
        first_dep[j] = malloc(JFACT[j]);
        memset(first_dep[j], -1, JFACT[j]);
        cnt[j] = calloc(JFACT[j], sizeof(uint64_t));
        sz[j] = 0;
    }
    list[0][0].mask = 0; list[0][0].idx = 0; sz[0] = 1;
    save(0);
    place(A, 1);
    dfs(1, 1u << A);
    FILE *f = fopen(argv[4], "w");
    for (int j = 3; j <= K; j++)
        for (int idx = 0; idx < JFACT[j]; idx++)
            fprintf(f, "%d %d %llu\n", j, idx, (unsigned long long)cnt[j][idx]);
    fclose(f);
    return 0;
}
