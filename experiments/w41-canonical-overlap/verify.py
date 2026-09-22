#!/usr/bin/env python3
"""Independent exhaustive host count vs the gap-integration formula."""
from collections import defaultdict
from itertools import combinations, permutations
import json
from pathlib import Path
from overlap import moment_numerators


def host_pairs(sigma, k, target=None):
    """Direct replacement test; does not use rectangles or gap matrices."""
    n = len(sigma)
    groups = defaultdict(list)
    for positions in combinations(range(n), k):
        values = [sigma[p] for p in positions]
        pat = tuple(sum(w < v for w in values) for v in values)
        if target is not None and pat != target:
            continue
        good = True
        for r, p in enumerate(positions):
            start = positions[r-1]+1 if r else 0
            for q in range(start, p):
                replaced = values.copy()
                replaced[r] = sigma[q]
                other = tuple(sum(w < v for w in replaced) for v in replaced)
                if other == pat:
                    good = False
                    break
            if not good:
                break
        if good:
            groups[pat].append(set(positions))
    result = [0]*(k+1)
    for group in groups.values():
        for a in group:
            for b in group:
                result[len(a & b)] += 1
    return result


def main():
    records = []
    # Includes up to three background points: tests more than the empty union.
    for k in range(2, 6):
        result = moment_numerators(k, k-2, 7)
        for n in range(k+2, 8):
            direct = sum(host_pairs(sigma, k)[k-2]
                         for sigma in permutations(range(1, n+1)))
            expected = result['numerators'][n-k-2]
            assert direct == expected, (k, n, direct, expected)
            print(f'PASS k={k}, n={n}: ordered-pair sum={direct} over {__import__("math").factorial(n)} hosts', flush=True)
        # A second normalization/sanity check: k-1 compatibility is impossible.
        rigid = moment_numerators(k, k-1, k+1)
        assert rigid['types'] == 0
        print(f'PASS k={k}: overlap k-1 has zero compatible union types', flush=True)
        records.append(result)
    Path(__file__).with_name('exact_results.json').write_text(json.dumps(records, indent=2)+'\n')
    print('PASS: every formula numerator equals independent exhaustive enumeration')


if __name__ == '__main__':
    main()
