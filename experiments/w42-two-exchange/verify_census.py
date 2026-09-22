#!/usr/bin/env python3
"""Recount the minimal counterexample using direct replacement searches."""
from itertools import combinations, permutations
import json
from pathlib import Path
from verify import local_minimum, pattern

root = Path(__file__).parent
reference = json.loads((root / 'exact-census.json').read_text())[0]
assert (reference['k'], reference['n']) == (3, 6)
totals = {p: [0, 0, 0, 0, 0, 0] for p in permutations(range(3))}
for sigma in permutations(range(1, 7)):
    counts = {p: [0, 0, 0] for p in totals}
    for a in combinations(range(6), 3):
        row = counts[pattern(sigma, a)]
        row[0] = 1
        row[1] += local_minimum(sigma, a, 3, 1)
        row[2] += local_minimum(sigma, a, 3, 2)
    for p, (hit, one, two) in counts.items():
        row = totals[p]
        for i, value in enumerate((hit, one, two, one**2, two**2)):
            row[i] += value
        row[5] = max(row[5], two)
for row in reference['patterns']:
    p = tuple(v-1 for v in row['pattern'])
    assert totals[p] == [row[key] for key in
                        ('hits', 'y1', 'y2', 'y1_squared', 'y2_squared', 'max_y2')]
    print(''.join(str(v+1) for v in p), *totals[p])
print('PASS: independent exact counts for all six targets on every host in S_6')
