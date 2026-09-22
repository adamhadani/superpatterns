# W40 — exact frontier milestone

**Full result and prior-art comparison:** [experiment report](report.md),
[standalone PDF](../../output/pdf/repeated-21-frontier.pdf) and
[readable Markdown](../../output/pdf/repeated-21-frontier.md).
These now present the complete pruning proof and the precise Alon criterion
prominently; the historical sample below remains finite-host evidence.

**Current continuation:** permanent dominance pruning gives an exact
O(n log n)-time, O(n)-space algorithm in `pruned.c`; see [pruning.md](pruning.md).
All 372,249 prefix states of 46,342 hosts agree with an independent unpruned
recurrence. The host set includes every permutation through length 8; their
final lengths also agree with brute subsequences. An exact marked-state flux
identity passed 5912 finite cut checks. Even all thresholds and all pending
apices fail to determine the next update without activation marks, as a
four-point counterexample shows. The original sample below is preserved.

`verify.py` compared the frontier algorithm with exhaustive subsequences on
6,113 hosts: all permutations through n=7 and 200 seeded random hosts of
lengths 8,10,12,14. All passed; see `verification.txt`.

For 64 seeded uniform hosts of length 4096, the exact number L₂₁ of completed
21 blocks divided by √4096 has sample mean 0.941162109375 and standard error
0.00316547. The per-host counts are in `samples_n4096.csv`. This is a finite
sample statistic, not a new asymptotic bound or proof of c₂₁=1.

The conceptual output is the exact joint evolution in `proof.md`. A
stationary comparison must handle all pending profiles together and their
shared arrivals. The exhibited downward jump prevents importing W36's
monotone compound-Poisson boundary law directly.

Reproduce the saved sample (byte-for-byte checked on 2026-09-10):

```sh
/private/tmp/superpatterns-c21-frontier --random 4096 64 20260910 > /private/tmp/c21-samples.csv
cmp experiments/w40-c21-frontier/samples_n4096.csv /private/tmp/c21-samples.csv
```

The generator uses xoshiro256** and the repository's Fisher–Yates shuffle.
The exact containment algorithm is deterministic for each supplied host.
