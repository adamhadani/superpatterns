# Cross-check mslack dumps against a naive brute force: regenerate the same sigma? Not possible (RNG internal),
# so instead compare via a tiny modified driver: we feed sigma through stdin in a debug binary.
import subprocess, random, sys
from patlib import *
k = int(sys.argv[1]); n = int(sys.argv[2]); trials = int(sys.argv[3])
random.seed(7)
bad = 0
for t in range(trials):
    sigma = list(range(n)); random.shuffle(sigma)
    out = subprocess.run(['./mslack_stdin', str(k)], input=' '.join(map(str, sigma)), capture_output=True, text=True).stdout.split()
    got = sorted(map(int, out[1:])); assert int(out[0]) == len(got) or int(out[0]) > 100000
    exp = missing_bruteforce(sigma, k)
    if got != exp: bad += 1; print('MISMATCH', sigma, got[:5], exp[:5])
    # also check decode/encode roundtrip
    for c in exp[:3]: assert encode(decode(c, k)) == c
print(f'k={k} n={n}: {trials} perms, {bad} mismatches')
