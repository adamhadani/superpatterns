// Per-host sufficient statistics for a covariance-aware canonical audit.
// Enumerates every k-subset, then every same-pattern canonical pair.
// Usage: diagnose_can K N HOSTS SEED > hosts.csv
#include "common.h"
#include "canon.h"
#include <assert.h>

static int K, N, sigma1[65], vals[14], pos[14];
static uint32_t *counts, *canonical;
typedef struct { long code; uint64_t mask; } Copy;
static Copy *copies;
static size_t length, capacity;

static int compare(const void *a, const void *b) {
    long x = ((const Copy *)a)->code, y = ((const Copy *)b)->code;
    return (x > y) - (x < y);
}

static void enumerate(int depth, int previous, long code) {
    if (depth == K) {
        counts[code]++;
        if (!is_canonical(pos, vals, K, N)) return;
        canonical[code]++;
        if (length == capacity) {
            capacity = capacity ? 2 * capacity : 1024;
            Copy *next = realloc(copies, capacity * sizeof(*copies));
            if (!next) { perror("realloc"); exit(2); }
            copies = next;
        }
        uint64_t mask = 0;
        for (int j = 0; j < K; j++) mask |= UINT64_C(1) << (pos[j] - 1);
        copies[length++] = (Copy){code, mask};
        return;
    }
    for (int q = previous + 1; q <= N - K + depth + 1; q++) {
        int value = sigma1[q], rank = 0;
        for (int j = 0; j < depth; j++) rank += vals[j] < value;
        pos[depth] = q; vals[depth] = value;
        enumerate(depth + 1, q, code * (depth + 1) + rank);
    }
}

static int uniform_int(int n) {
    uint64_t bound = (uint64_t)n, cutoff = -bound % bound, value;
    do { value = rng(); } while (value < cutoff);
    return (int)(value % bound);
}

static void unbiased_shuffle(int *v, int n) {
    for (int j = n - 1; j > 0; j--) {
        int i = uniform_int(j + 1), value = v[i];
        v[i] = v[j]; v[j] = value;
    }
}

int main(int argc, char **argv) {
    if (argc != 5) { fprintf(stderr, "usage: %s K N HOSTS SEED\n", argv[0]); return 2; }
    K = atoi(argv[1]); N = atoi(argv[2]); long hosts = atol(argv[3]);
    if (K < 4 || K > 10 || N < K || N > 63 || hosts < 1) return 2;
    init_fact(); long total_patterns = fact_[K];
    counts = calloc(total_patterns, sizeof(*counts));
    canonical = calloc(total_patterns, sizeof(*canonical));
    P_ = malloc(sizeof(*P_) * (N + 1) * (N + 1));
    if (!counts || !canonical || !P_) return 2;

    int target[4][14]; long codes[4];
    for (int j = 0; j < K; j++) target[0][j] = target[1][j] = j;
    seed_rng(20260910); unbiased_shuffle(target[1], K);
    // Two value strips, with the last singleton in the lower strip if K is odd.
    int h = (K + 1) / 2, j = 0;
    for (int i = 0; i < h; i++) {
        target[2][j++] = i;
        if (h + i < K) target[2][j++] = h + i;
    }
    for (int i = 0; i < K; i++) target[3][i] = i;
    for (int i = 0; i + 1 < K; i += 2) { target[3][i] = i + 1; target[3][i + 1] = i; }
    for (int q = 0; q < 4; q++) codes[q] = pat_code(target[q], K);
    fprintf(stderr, "k=%d N=%d hosts=%ld seed=%s target_codes=%ld,%ld,%ld,%ld\n",
            K, N, hosts, argv[4], codes[0], codes[1], codes[2], codes[3]);
    seed_rng(strtoull(argv[4], NULL, 10));
    printf("host,sum_y,sum_y2,sum_m2,distinct");
    for (int q = 0; q <= K; q++) printf(",overlap_%d", q);
    for (int q = 0; q < 4; q++) printf(",target%d_y,target%d_y2,target%d_hit", q, q, q);
    putchar('\n');

    for (long host = 0; host < hosts; host++) {
        int sigma[64]; for (int i = 0; i < N; i++) sigma[i] = i + 1;
        unbiased_shuffle(sigma, N);
        for (int i = 0; i < N; i++) sigma1[i + 1] = sigma[i];
        build_prefix(sigma1, N);
        memset(counts, 0, total_patterns * sizeof(*counts));
        memset(canonical, 0, total_patterns * sizeof(*canonical));
        length = 0; enumerate(0, 0, 0);
        qsort(copies, length, sizeof(*copies), compare);
        uint64_t overlap[14] = {0}; overlap[K] = length;
        for (size_t i = 0; i < length; i++)
            for (size_t j2 = i + 1; j2 < length && copies[j2].code == copies[i].code; j2++)
                overlap[__builtin_popcountll(copies[i].mask & copies[j2].mask)] += 2;
        uint64_t sy = 0, sy2 = 0, sm2 = 0, distinct = 0, pair_sum = 0;
        for (long c = 0; c < total_patterns; c++) {
            uint64_t y = canonical[c], m = counts[c];
            sy += y; sy2 += y * y; sm2 += m * m; distinct += m > 0;
            // Every contained pattern has a leftmost-canonical occurrence.
            assert((m > 0) == (y > 0));
        }
        for (int q = 0; q <= K; q++) pair_sum += overlap[q];
        assert(pair_sum == sy2 && overlap[K - 1] == 0 && overlap[K] == sy);
        printf("%ld,%llu,%llu,%llu,%llu", host, (unsigned long long)sy,
               (unsigned long long)sy2, (unsigned long long)sm2, (unsigned long long)distinct);
        for (int q = 0; q <= K; q++) printf(",%llu", (unsigned long long)overlap[q]);
        for (int q = 0; q < 4; q++) {
            uint64_t y = canonical[codes[q]];
            printf(",%llu,%llu,%d", (unsigned long long)y, (unsigned long long)(y * y), counts[codes[q]] > 0);
        }
        putchar('\n');
    }
    free(counts); free(canonical); free(P_); free(copies);
    return 0;
}
