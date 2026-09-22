#!/usr/bin/env python3
"""Compare the frontier with exhaustive subsequences, independently."""
import itertools
from pathlib import Path
import random
import subprocess
import sys


def brute(permutation):
    n = len(permutation)
    for m in range(n//2,0,-1):
        for values in itertools.combinations(permutation,2*m):
            if all(values[2*j]>values[2*j+1] for j in range(m)) and all(
                    values[2*j]<values[2*j+3] for j in range(m-1)):
                return m
    return 0


if __name__ == "__main__":
    binary = sys.argv[1] if len(sys.argv)>1 else str(Path(__file__).with_name("frontier"))
    rng = random.Random(20260910)
    cases = [p for n in range(1,8) for p in itertools.permutations(range(1,n+1))]
    for n in (8,10,12,14):
        for _ in range(50):
            p = list(range(1,n+1));rng.shuffle(p);cases.append(tuple(p))
    inputs = "".join(f"{len(p)} "+" ".join(map(str,p))+"\n" for p in cases)
    result = subprocess.run([binary],input=inputs,text=True,capture_output=True,check=True)
    got = list(map(int,result.stdout.split()))
    assert len(got)==len(cases)
    for p, answer in zip(cases,got):
        expected = brute(p)
        assert answer==expected,(p,answer,expected)
    print(f"PASS: {len(cases)} hosts; exhaustive S_n for n<=7 plus 200 random hosts through n=14")
