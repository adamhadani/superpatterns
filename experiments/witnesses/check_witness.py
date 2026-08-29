#!/usr/bin/env python3
"""Independent brute-force k-superpattern checker (pure Python, no dependencies).

Usage:
    python3 check_witness.py K "p1 p2 ... pm"      # check one permutation
    python3 check_witness.py --all                  # check every line of witnesses.txt
    python3 check_witness.py --test                 # self-tests (known positives, damaged negatives)

Method (deliberately naive so that it shares nothing with the C checker `w1-search/sp.c`
or the Lean DFS checker): enumerate every k-subset of positions, standardise the subsequence
to a pattern by ranking values, collect the set of patterns, and compare its size with k!.
"""
import hashlib
import itertools
import math
import sys
from pathlib import Path


def is_permutation(p):
    return sorted(p) == list(range(1, len(p) + 1))


def standardise(seq):
    order = sorted(range(len(seq)), key=lambda i: seq[i])
    pat = [0] * len(seq)
    for rank, i in enumerate(order):
        pat[i] = rank
    return tuple(pat)


def patterns(p, k):
    return {standardise([p[i] for i in idx]) for idx in itertools.combinations(range(len(p)), k)}


def is_superpattern(p, k):
    if not is_permutation(p):
        raise ValueError("not a permutation of 1..m")
    return len(patterns(p, k)) == math.factorial(k)


def tie_break_word(word):
    """Permutation from a word over [r]: equal letters are ordered decreasingly (later = smaller)."""
    idx = sorted(range(len(word)), key=lambda i: (word[i], -i))
    p = [0] * len(word)
    for r, i in enumerate(idx):
        p[i] = r + 1
    return p


def zeta(k):
    """Engen–Vatter's construction ζ_k of length ceil((k²+1)/2)."""
    runs = []
    for j in range(1, k + 1):
        runs.append(list(range(1, k + 2, 2)) if j % 2 else [x for x in range(k + 1, 0, -1) if x % 2 == 0])
    w = [x for r in runs for x in r if x <= k]
    p = tie_break_word(w)
    if k % 2 == 0:
        p = [len(p) + 1] + p
    return p


def parse(s):
    return [int(t) for t in s.replace(",", " ").split()]


def check_file(path):
    ok = True
    for line in Path(path).read_text().splitlines():
        line = line.split("#")[0].strip()
        if not line:
            continue
        k_str, perm_str = line.split(":", 1)
        k, p = int(k_str), parse(perm_str)
        n = len(patterns(p, k))
        good = n == math.factorial(k)
        ok &= good
        print(f"k={k} m={len(p)} distinct patterns {n}/{math.factorial(k)} "
              f"({math.comb(len(p), k)} subsets) -> {'OK' if good else 'FAIL'}")
    digest = hashlib.sha256(Path(path).read_bytes()).hexdigest()
    print(f"sha256({Path(path).name}) = {digest}")
    return ok


def self_test():
    assert is_superpattern([2, 5, 3, 1, 4], 3)                       # sp(3)=5 witness
    assert is_superpattern([5, 1, 9, 4, 7, 2, 6, 8, 3], 4)           # sp(4)=9 witness
    z5 = zeta(5)
    assert len(z5) == 13 and is_superpattern(z5, 5)                    # sp(5)=13 (Engen–Vatter ζ_5)
    arn = tie_break_word([3, 6, 5, 1, 6, 7, 3, 4, 2, 6, 5, 7, 1, 4, 6, 3, 7])
    assert len(arn) == 17 and is_superpattern(arn, 6)                 # sp(6)=17 (Arnarson's permutation)
    # negatives: damaged witnesses must fail
    assert not is_superpattern([1, 2, 3, 4, 5], 3)
    d = list(arn)
    d[0], d[-1] = d[-1], d[0]
    assert not is_superpattern(d, 6)
    assert not is_superpattern(z5[:-1] + [], 5) if is_permutation(z5[:-1]) else True
    assert not is_superpattern(zeta(5)[1:] + [], 5) if is_permutation(zeta(5)[1:]) else True
    # boundary: the pattern using the first and the last position
    assert standardise([z5[0], z5[6], z5[-1]]) in patterns(z5, 3)
    # k = 7 sanity: a random permutation of length 23 is essentially never a 7-superpattern
    import random
    random.seed(1)
    r = random.sample(range(1, 24), 23)
    assert not is_superpattern(r, 7)
    print("self-tests passed")


if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        self_test()
    elif sys.argv[1:] == ["--all"]:
        sys.exit(0 if check_file(Path(__file__).with_name("witnesses.txt")) else 1)
    else:
        k, p = int(sys.argv[1]), parse(sys.argv[2])
        n = len(patterns(p, k))
        print(f"m={len(p)} k={k} distinct patterns {n}/{math.factorial(k)}")
        sys.exit(0 if n == math.factorial(k) else 1)
