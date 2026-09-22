#!/usr/bin/env python3
"""Verify every completed threshold at every prefix, plus larger hosts."""
import itertools
import random
import subprocess
import sys
from verify import brute


def full_thresholds(values):
    """Independent quadratic pending-list evolution, without any pruning."""
    f = [0] + [float('inf')]*(len(values)//2+1)
    pending = [[] for _ in f]
    states = []
    for y in values:
        old = f.copy()
        for m in range(len(f)-1):
            choices = [z for lower, z in pending[m] if lower < y < z]
            if choices:
                f[m+1] = min(f[m+1], min(choices))
            if old[m] < y:
                pending[m].append((old[m], y))
        states.append([a for a in f[1:] if a < float('inf')])
    return states


def main():
    binary = sys.argv[1]
    rng = random.Random(20260911)
    cases = [p for n in range(1, 9) for p in itertools.permutations(range(1, n+1))]
    exhaustive = len(cases)
    for n in (12, 25, 64, 128):
        for _ in range(25):
            p = list(range(1, n+1)); rng.shuffle(p); cases.append(p)
    # Extreme shapes exercise empty queries, repeated root clears and deep levels.
    for n in (64, 127, 1024):
        cases.extend([list(range(1,n+1)), list(range(n,0,-1)),
                      [i+1 if i%2 else i-1 for i in range(1,n-(n%2)+1)] + ([n] if n%2 else [])])
    data = ''.join(f'{len(p)} '+ ' '.join(map(str,p))+'\n' for p in cases)
    run = subprocess.run([binary,'--trace'],input=data,text=True,capture_output=True,check=True)
    rows = iter(run.stdout.splitlines())
    prefixes = 0
    for p in cases:
        reference = full_thresholds(p)
        for expected in reference:
            row = list(map(int,next(rows).split()))
            assert row == [len(expected)] + expected, (p,row,expected)
            prefixes += 1
        if len(p)<=8:
            assert len(reference[-1]) == brute(p), p
    assert next(rows,None) is None
    print(f'PASS: {exhaustive} exhaustive hosts (all S_n, n<=8), 100 random hosts, 9 extreme hosts')
    print(f'PASS: {prefixes} prefix states; every completed threshold agrees with the unpruned recurrence')
    print('PASS: exhaustive final lengths also agree with independent brute subsequences')


if __name__ == '__main__':
    main()
