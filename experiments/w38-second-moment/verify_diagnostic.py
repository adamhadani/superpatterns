#!/usr/bin/env python3
"""Independent direct canonical test and pair enumeration on small hosts."""
from collections import Counter, defaultdict
import csv
import io
import itertools
from pathlib import Path
import subprocess

MASK = (1 << 64)-1


class RNG:
    def __init__(self, seed):
        self.state = []
        for _ in range(4):
            seed = (seed+0x9e3779b97f4a7c15) & MASK
            z = seed
            z = ((z ^ (z >> 30))*0xbf58476d1ce4e5b9) & MASK
            z = ((z ^ (z >> 27))*0x94d049bb133111eb) & MASK
            self.state.append(z ^ (z >> 31))

    def next(self):
        a,b,c,d = self.state
        value = (b*5) & MASK
        value = (((value << 7) | (value >> 57))*9) & MASK
        shift = (b << 17) & MASK
        c ^= a; d ^= b; b ^= c; a ^= d; c ^= shift
        d = ((d << 45) | (d >> 19)) & MASK
        self.state = [a,b,c,d]
        return value

    def shuffle(self, n):
        values = list(range(1,n+1))
        for i in range(n-1,0,-1):
            bound = i+1
            while True:
                x = self.next()
                if x >= ((1 << 64) % bound):
                    break
            j = x % bound
            values[i],values[j] = values[j],values[i]
        return values


def stats(sigma, k):
    count = Counter(); canonical = defaultdict(list)
    n = len(sigma)
    for positions in itertools.combinations(range(n),k):
        values = [sigma[i] for i in positions]
        pattern = tuple(sorted(values).index(v) for v in values)
        count[pattern] += 1
        ok = True
        for r,(position,value) in enumerate(zip(positions,values)):
            lower = max([0]+[v for v in values if v < value])
            upper = min([n+1]+[v for v in values if v > value])
            start = positions[r-1]+1 if r else 0
            if any(lower < sigma[i] < upper for i in range(start,position)):
                ok = False; break
        if ok:
            canonical[pattern].append(set(positions))
    overlap = [0]*(k+1)
    for occurrences in canonical.values():
        for a in occurrences:
            for b in occurrences:
                overlap[len(a & b)] += 1
    assert set(canonical) == set(count)
    return dict(sum_y=sum(map(len,canonical.values())),
                sum_y2=sum(len(v)**2 for v in canonical.values()),
                sum_m2=sum(v*v for v in count.values()), distinct=len(count),
                **{f"overlap_{j}":v for j,v in enumerate(overlap)})


if __name__ == "__main__":
    binary = Path(__file__).resolve().parent / "out/review-20260910/diagnose_can"
    cases = [(4,7,20),(5,9,10),(6,10,5)]
    for k,n,hosts in cases:
        seed = 731+k
        run = subprocess.run([str(binary),str(k),str(n),str(hosts),str(seed)],text=True,capture_output=True,check=True)
        rows = list(csv.DictReader(io.StringIO(run.stdout)))
        rng = RNG(seed)
        for row in rows:
            expected = stats(rng.shuffle(n),k)
            assert all(int(row[key]) == value for key,value in expected.items())
        print(f"PASS k={k} N={n}: {hosts} hosts, every count and overlap agrees")
